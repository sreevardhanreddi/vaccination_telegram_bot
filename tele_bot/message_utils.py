""" sample_message = {
    "center_id": 572674,
    "name": "Yashoda Hospital Secbad Site 1",
    "address": "Yashoda Hospital Behind Harihara Kalavhavan Sec-bad",
    "state_name": "Telangana",
    "district_name": "Hyderabad",
    "block_name": "Secunderabad",
    "pincode": 500003,
    "from": "09:00:00",
    "to": "14:00:00",
    "lat": 17,
    "long": 79,
    "fee_type": "Paid",
    "session_id": "35e407ca-4692-47c4-9b20-43636c7fa442",
    "date": "09-06-2021",
    "available_capacity_dose1": 3,
    "available_capacity_dose2": 0,
    "available_capacity": 3,
    "fee": "1200",
    "min_age_limit": 18,
    "vaccine": "COVAXIN",
    "slots": [
        "09:00AM-10:00AM",
        "10:00AM-11:00AM",
        "11:00AM-12:00PM",
        "12:00PM-02:00PM",
    ],
} """


def _format_message(message={}):
    """
    utility to format message
    """
    center_name = message.get("name", "")
    address = "{} {} {} {}".format(
        message.get("address", ""),
        message.get("state_name", ""),
        message.get("district_name", ""),
        message.get("block_name", ""),
    )
    pincode = message.get("pincode", "")
    from_to = "{}-{}".format(message.get("from", ""), message.get("to", ""))
    fee_type = "{}::{}".format(message.get("fee_type", ""), message.get("fee", ""))
    date = "{}".format(message.get("date", ""))
    available_capacity = "{}".format(message.get("available_capacity", ""))
    available_capacity_dose1 = "{}".format(message.get("available_capacity_dose1", ""))
    available_capacity_dose2 = "{}".format(message.get("available_capacity_dose2", ""))
    min_age_limit = "{}".format(message.get("min_age_limit", ""))
    vaccine = "{}".format(message.get("vaccine", ""))
    slots = " ".join(message.get("slots", []))

    return """ 
    <b>Center : {center_name}</b>
    \n<b>Vaccine : {vaccine}</b>
    \n<b>Address</b> : {address}
    \n<b>Pincode : {pincode}</b>
    \n<b>Timings : {from_to}</b>
    \n<b>Fee : {fee_type}</b>
    \n<b>Date : {date}</b>
    \n<b>Available Capacity : {available_capacity}</b>
    \n<b>Available Capacity Dose 1: {available_capacity_dose1}</b>
    \n<b>Available Capacity Dose 2: {available_capacity_dose2}</b>
    \n<b>Min Age Limit: {min_age_limit}</b>
    \n<b>Slots: \n{slots}</b>
    """.format(
        center_name=center_name,
        vaccine=vaccine,
        address=address,
        pincode=pincode,
        from_to=from_to,
        fee_type=fee_type,
        date=date,
        available_capacity=available_capacity,
        available_capacity_dose1=available_capacity_dose1,
        available_capacity_dose2=available_capacity_dose2,
        min_age_limit=min_age_limit,
        slots=slots,
    )
