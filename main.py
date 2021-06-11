import json
import os
import threading
import time
from datetime import datetime, timedelta
from pprint import pprint

import requests
from dotenv import load_dotenv
from fake_useragent import UserAgent

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
import logging

from tele_bot import send_message

logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    level=logging.INFO,
)


PINCODES = [p.strip() for p in os.getenv("PINCODES").split(";")]
UA = UserAgent()
SLEEP_INTERVAL = int(os.getenv("SLEEP_INTERVAL", "3"))
MIN_AGE = 18


def get_sessions(pincode, date, sessions=[]):
    try:
        # request cowin portal API for available sessions
        logging.info("fetching data for date: {}, PINCODE: {}".format(date, pincode))
        res = requests.get(
            "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}".format(
                pincode, date
            ),
            headers={"User-Agent": str(UA.random)},
            timeout=5,
        )

        if res.status_code == 403:
            logging.error("403 Cowin portal is blocking your IP address")
        response_sessions = res.json()["sessions"] if res.ok else []

        # condition to check
        for s in response_sessions:
            if MIN_AGE >= s.get("min_age_limit") and (
                s.get("available_capacity_dose1") > 0
                and s.get("available_capacity") > 0
            ):
                logging.info("-" * 50)
                logging.info(s)
                logging.info("-" * 50)
                sessions.append(s)

        return res
    except Exception as e:
        logging.error("{}".format(e), exc_info=True)
        return []


def check_slots():
    today = datetime.now()
    next_few_days = [(today + timedelta(days=i)).strftime("%d-%m-%Y") for i in range(3)]
    request_threads = []
    sessions = []  # store the return value of the response
    for pincode in PINCODES:
        for date in next_few_days:
            request_thread = threading.Thread(
                target=get_sessions,
                args=(
                    pincode,
                    date,
                ),
                kwargs={
                    "sessions": sessions,
                },
            )
            request_thread.start()
            request_threads.append(request_thread)

    [request_thread.join() for request_thread in request_threads]

    bot_threads = []
    for s in sessions:
        bot_thread = threading.Thread(target=send_message, args=(s,))
        bot_thread.start()
        bot_threads.append(bot_thread)

    [bot_thread.join() for bot_thread in bot_threads]


def main():
    while True:
        check_slots()
        logging.info("sleeping for {} seconds".format(SLEEP_INTERVAL))
        time.sleep(SLEEP_INTERVAL)


if __name__ == "__main__":
    main()
