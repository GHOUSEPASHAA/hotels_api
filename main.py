from fastapi import FastAPI
from faker import Faker
import random
import hashlib
from datetime import datetime, timedelta
import requests
import uvicorn

app = FastAPI(title="Hotel Activity API")

fake = Faker()

properties = {
    "GRC": "Grand Royale Casino",
    "AC": "Atlantis Casino",
    "RRC": "Red Rock Casino"
}


def create_hotel_stay(activeclubid):

    personid = str(
        int(
            hashlib.md5(
                activeclubid.encode()
            ).hexdigest(),
            16
        ) % 90000 + 10000
    )

    property_id = random.choice(
        list(properties.keys())
    )

    property_name = properties[property_id]

    reservation_id = fake.numerify(
        "##########"
    )

    membership_id = fake.numerify(
        "######"
    )

    membership_card = fake.bothify(
        "MC########"
    )

    room_number = str(
        random.randint(100, 999)
    )

    begin_date = datetime.now() - timedelta(
        days=random.randint(1, 30)
    )

    nights = random.randint(1, 5)

    check_out_date = begin_date + timedelta(
        days=nights
    )

    stay_data = {

        "PERSONID":
            personid,

        "ACTIVECLUBID":
            activeclubid,

        "EVENT_GROUP_ID":
            fake.uuid4(),

        "PROPERTY_ID":
            property_id,

        "SF_PROPERTY_ID":
            property_id,


        "PROPERTY_NAME":
            property_name,

        "HOTEL_RESERVATION_ID":
            reservation_id,

        "HOTEL_MEMBERSHIP_CARD_NO":
            membership_card,

        "HOTEL_MEMBERSHIP_ID":
            membership_id,

        "HOTEL_MEMBERSHIP_LEVEL":
            random.choice([
                "Gold",
                "Silver",
                "Platinum",
                "Diamond"
            ]),

        "HOTEL_NAME_ID":
            fake.numerify("#####"),

        "HOTEL_FOLIO_CLOSE_DATE":
            check_out_date.date().isoformat(),

        "HOTEL_ADVANCE_CHECKED_IN_YN":
            random.choice(["Y", "N"]),

        "HOTEL_POSTING_ALLOWED_YN":
            random.choice(["Y", "N"]),

        "HOTEL_VIDEO_CHECKOUT_YN":
            random.choice(["Y", "N"]),

        "HOTEL_INTERMEDIARY_YN":
            random.choice(["Y", "N"]),

        "HOTEL_WALKIN_YN":
            random.choice(["Y", "N"]),

        "HOTEL_PSUEDO_ROOM_YN":
            random.choice(["Y", "N"]),

        "HOTEL_WL_TELEPHONE_NO":
            fake.phone_number(),

        "HOTEL_PAYMENT_METHOD":
            random.choice([
                "CASH",
                "CARD",
                "COMP"
            ]),

        "HOTEL_CHANNEL":
            random.choice([
                "ONLINE",
                "PHONE",
                "WALKIN"
            ]),

        "HOTEL_CUSTOM_REFERENCE":
            fake.bothify("REF######"),

        "HOTEL_RATEABLE_VALUE":
            round(
                random.uniform(100, 800),
                2
            ),

        "HOTEL_REINSTATE_TIMESTAMP_PROPERTY":
            None,

        "HOTEL_EVENT_TIMESTAMP_PROPERTY_TIMEZONE":
            "America/New_York",

        "HOTEL_EVENT_TIMESTAMP_PROPERTY_TIMEZONE_ABBR":
            "EST",

        "HOTEL_RESERVATION_TIMESTAMP_PROPERTY":
            begin_date.isoformat(),

        "HOTEL_RESERVATION_CREATION_DATE":
            begin_date.date().isoformat(),

        "HOTEL_CHECK_IN_TIMESTAMP_PROPERTY":
            begin_date.isoformat(),

        "HOTEL_CHECK_OUT_TIMESTAMP_PROPERTY":
            check_out_date.isoformat(),

        "HOTEL_CHECK_IN_DATE":
            begin_date.date().isoformat(),

        "HOTEL_WL_PRIORITY":
            random.choice([
                "HIGH",
                "MEDIUM",
                "LOW"
            ]),

        "HOTEL_ROOM_FEATURES":
            random.choice([
                "Ocean View",
                "VIP Lounge",
                "Smoking"
            ]),

        "HOTEL_BOOKED_ROOM_CATEGORY":
            random.choice([
                "KING",
                "QUEEN",
                "SUITE"
            ]),

        "HOTEL_RATE_CODE":
            fake.bothify("RATE###"),

        "HOTEL_RATE_CATEGORY":
            random.choice([
                "BAR",
                "COMP",
                "VIP"
            ]),

        "HOTEL_MARKET_CODE":
            random.choice([
                "LOCAL",
                "VIP",
                "TOURISM"
            ]),

        "HOTEL_PROMOTION_CODE":
            random.choice([
                "WELCOME",
                "SUMMER",
                "VIPFREE"
            ]),

        "HOTEL_NUM_OF_NIGHTS_STAY":
            nights,

        "HOTEL_NUM_OF_NIGHTS_STAYS":
            nights,

        "HOTEL_ROOM_CLASS":
            random.choice([
                "STANDARD",
                "DELUXE",
                "SUITE"
            ]),

        "HOTEL_TRANSACTION_AMOUNT":
            round(
                random.uniform(100, 5000),
                2
            ),

        "HOTEL_NUM_OF_ADULTS":
            random.randint(1, 4),

        "HOTEL_NUM_OF_CHILDREN":
            random.randint(0, 3),

        "HOTEL_SMOKING_ROOM":
            random.choice(["Y", "N"]),

        "HOTEL_ROOM_CATEGORY":
            "KING",

        "HOTEL_ROOM_CATEGORY_DESCRIPTION":
            "Luxury King Room",

        "HOTEL_ROOM_NUMBER":
            room_number,

        "HOTEL_CASH_ROOM_REVENUE":
            round(
                random.uniform(100, 3000),
                2
            ),

        "HOTEL_COMP_ROOM_REVENUE":
            round(
                random.uniform(0, 1500),
                2
            ),

        "HOTEL_CHECK_OUT_DATE":
            check_out_date.date().isoformat(),

        "HOTEL_CANCELLATION_NO":
            None,

        "HOTEL_CANCELLATION_REASON":
            None,

        "HOTEL_CANCELLATION_REASON_CODE":
            None,

        "HOTEL_CANCEL_TIMESTAMP_PROPERTY":
            None,

        "HOTEL_CANCEL_DATE":
            None,

        "FUTURE_CHECK_IN_PROPERTIES":
            property_name,

        "FUTURE_CHECK_IN_DATES":
            begin_date.date().isoformat(),

        "FUTURE_CHECK_IN_PROPERTIES_WITH_DATES":
            f"{property_name} - {begin_date.date().isoformat()}"
    }

    return stay_data


def build_hotel_event(
    stay_data,
    event_action
):

    record = stay_data.copy()

    reservation_status = {
        "HOTEL:RESERVE": "RESERVED",
        "HOTEL:CHECK_IN": "CHECKED_IN",
        "HOTEL:CHECK_OUT": "CHECKED_OUT"
    }

    record["ENTITY"] = "HOTEL"

    record["ENTITY_ACTION"] = event_action

    record["HOTEL_RESERVATION_STATUS"] = (
        reservation_status[event_action]
    )

    return {

    "EVENT_GROUP_ID":
        record["EVENT_GROUP_ID"],

    "PERSONID": record["PERSONID"],

    "ACTIVECLUBID":
            record["ACTIVECLUBID"],

    "PROPERTY_ID":
        record["PROPERTY_ID"],

    "SF_PROPERTY_ID":
        record["SF_PROPERTY_ID"],

    "PROPERTY_NAME":
        record["PROPERTY_NAME"],

    "HOTEL_RESERVATION_ID":
        record["HOTEL_RESERVATION_ID"],

    "HOTEL_MEMBERSHIP_CARD_NO":
        record["HOTEL_MEMBERSHIP_CARD_NO"],

    "HOTEL_MEMBERSHIP_ID":
        record["HOTEL_MEMBERSHIP_ID"],

    "HOTEL_MEMBERSHIP_LEVEL":
        record["HOTEL_MEMBERSHIP_LEVEL"],

    "HOTEL_NAME_ID":
        record["HOTEL_NAME_ID"],

    "HOTEL_FOLIO_CLOSE_DATE":
        record["HOTEL_FOLIO_CLOSE_DATE"],

    "HOTEL_ADVANCE_CHECKED_IN_YN":
        record["HOTEL_ADVANCE_CHECKED_IN_YN"],

    "HOTEL_POSTING_ALLOWED_YN":
        record["HOTEL_POSTING_ALLOWED_YN"],

    "HOTEL_VIDEO_CHECKOUT_YN":
        record["HOTEL_VIDEO_CHECKOUT_YN"],

    "HOTEL_INTERMEDIARY_YN":
        record["HOTEL_INTERMEDIARY_YN"],

    "HOTEL_WALKIN_YN":
        record["HOTEL_WALKIN_YN"],

    "HOTEL_PSUEDO_ROOM_YN":
        record["HOTEL_PSUEDO_ROOM_YN"],

    "HOTEL_WL_TELEPHONE_NO":
        record["HOTEL_WL_TELEPHONE_NO"],

    "HOTEL_PAYMENT_METHOD":
        record["HOTEL_PAYMENT_METHOD"],

    "HOTEL_CHANNEL":
        record["HOTEL_CHANNEL"],

    "HOTEL_CUSTOM_REFERENCE":
        record["HOTEL_CUSTOM_REFERENCE"],

    "HOTEL_RATEABLE_VALUE":
        record["HOTEL_RATEABLE_VALUE"],

    "HOTEL_RESERVATION_STATUS":
        record["HOTEL_RESERVATION_STATUS"],

    "HOTEL_REINSTATE_TIMESTAMP_PROPERTY":
        record["HOTEL_REINSTATE_TIMESTAMP_PROPERTY"],

    "HOTEL_EVENT_TIMESTAMP_PROPERTY_TIMEZONE":
        record["HOTEL_EVENT_TIMESTAMP_PROPERTY_TIMEZONE"],

    "HOTEL_EVENT_TIMESTAMP_PROPERTY_TIMEZONE_ABBR":
        record["HOTEL_EVENT_TIMESTAMP_PROPERTY_TIMEZONE_ABBR"],

    "HOTEL_RESERVATION_TIMESTAMP_PROPERTY":
        record["HOTEL_RESERVATION_TIMESTAMP_PROPERTY"],

    "HOTEL_RESERVATION_CREATION_DATE":
        record["HOTEL_RESERVATION_CREATION_DATE"],

    "HOTEL_RESERVATION_TIMESTAMP_ADT":
        record.get("HOTEL_RESERVATION_TIMESTAMP_ADT"),

    "HOTEL_RESERVATION_TIMESTAMP_AST":
        record.get("HOTEL_RESERVATION_TIMESTAMP_AST"),

    "HOTEL_RESERVATION_TIMESTAMP_CDT":
        record.get("HOTEL_RESERVATION_TIMESTAMP_CDT"),

    "HOTEL_RESERVATION_TIMESTAMP_CST":
        record.get("HOTEL_RESERVATION_TIMESTAMP_CST"),

    "HOTEL_RESERVATION_TIMESTAMP_EST":
        record.get("HOTEL_RESERVATION_TIMESTAMP_EST"),

    "HOTEL_RESERVATION_TIMESTAMP_MDT":
        record.get("HOTEL_RESERVATION_TIMESTAMP_MDT"),

    "HOTEL_RESERVATION_TIMESTAMP_MST":
        record.get("HOTEL_RESERVATION_TIMESTAMP_MST"),

    "HOTEL_RESERVATION_TIMESTAMP_PDT":
        record.get("HOTEL_RESERVATION_TIMESTAMP_PDT"),

    "HOTEL_CHECK_IN_TIMESTAMP_PROPERTY":
        record["HOTEL_CHECK_IN_TIMESTAMP_PROPERTY"],

    "HOTEL_CHECK_OUT_TIMESTAMP_PROPERTY":
        record["HOTEL_CHECK_OUT_TIMESTAMP_PROPERTY"],

    "HOTEL_CHECK_IN_DATE":
        record["HOTEL_CHECK_IN_DATE"],

    "HOTEL_CHECK_IN_TIMESTAMP_ADT":
        record.get("HOTEL_CHECK_IN_TIMESTAMP_ADT"),

    "HOTEL_CHECK_IN_TIMESTAMP_AST":
        record.get("HOTEL_CHECK_IN_TIMESTAMP_AST"),

    "HOTEL_CHECK_IN_TIMESTAMP_CDT":
        record.get("HOTEL_CHECK_IN_TIMESTAMP_CDT"),

    "HOTEL_CHECK_IN_TIMESTAMP_CST":
        record.get("HOTEL_CHECK_IN_TIMESTAMP_CST"),

    "HOTEL_CHECK_IN_TIMESTAMP_EST":
        record.get("HOTEL_CHECK_IN_TIMESTAMP_EST"),

    "HOTEL_CHECK_IN_TIMESTAMP_MDT":
        record.get("HOTEL_CHECK_IN_TIMESTAMP_MDT"),

    "HOTEL_CHECK_IN_TIMESTAMP_MST":
        record.get("HOTEL_CHECK_IN_TIMESTAMP_MST"),

    "HOTEL_CHECK_IN_TIMESTAMP_PDT":
        record.get("HOTEL_CHECK_IN_TIMESTAMP_PDT"),

    "HOTEL_WL_PRIORITY":
        record["HOTEL_WL_PRIORITY"],

    "HOTEL_ROOM_FEATURES":
        record["HOTEL_ROOM_FEATURES"],

    "HOTEL_BOOKED_ROOM_CATEGORY":
        record["HOTEL_BOOKED_ROOM_CATEGORY"],

    "HOTEL_RATE_CODE":
        record["HOTEL_RATE_CODE"],

    "HOTEL_RATE_CATEGORY":
        record["HOTEL_RATE_CATEGORY"],

    "HOTEL_MARKET_CODE":
        record["HOTEL_MARKET_CODE"],

    "HOTEL_PROMOTION_CODE":
        record["HOTEL_PROMOTION_CODE"],

    "HOTEL_NUM_OF_NIGHTS_STAY":
        record["HOTEL_NUM_OF_NIGHTS_STAY"],

    "HOTEL_NUM_OF_NIGHTS_STAYS":
        record["HOTEL_NUM_OF_NIGHTS_STAYS"],

    "HOTEL_ROOM_CLASS":
        record["HOTEL_ROOM_CLASS"],

    "HOTEL_TRANSACTION_AMOUNT":
        record["HOTEL_TRANSACTION_AMOUNT"],

    "HOTEL_NUM_OF_ADULTS":
        record["HOTEL_NUM_OF_ADULTS"],

    "HOTEL_NUM_OF_CHILDREN":
        record["HOTEL_NUM_OF_CHILDREN"],

    "HOTEL_SMOKING_ROOM":
        record["HOTEL_SMOKING_ROOM"],

    "HOTEL_ROOM_CATEGORY":
        record["HOTEL_ROOM_CATEGORY"],

    "HOTEL_ROOM_CATEGORY_DESCRIPTION":
        record["HOTEL_ROOM_CATEGORY_DESCRIPTION"],

    "HOTEL_ROOM_NUMBER":
        record["HOTEL_ROOM_NUMBER"],

    "HOTEL_CASH_ROOM_REVENUE":
        record["HOTEL_CASH_ROOM_REVENUE"],

    "HOTEL_COMP_ROOM_REVENUE":
        record["HOTEL_COMP_ROOM_REVENUE"],

    "HOTEL_CHECK_OUT_DATE":
        record["HOTEL_CHECK_OUT_DATE"],

    "HOTEL_CHECK_OUT_TIMESTAMP_ADT":
        record.get("HOTEL_CHECK_OUT_TIMESTAMP_ADT"),

    "HOTEL_CHECK_OUT_TIMESTAMP_AST":
        record.get("HOTEL_CHECK_OUT_TIMESTAMP_AST"),

    "HOTEL_CHECK_OUT_TIMESTAMP_CDT":
        record.get("HOTEL_CHECK_OUT_TIMESTAMP_CDT"),

    "HOTEL_CHECK_OUT_TIMESTAMP_CST":
        record.get("HOTEL_CHECK_OUT_TIMESTAMP_CST"),

    "HOTEL_CHECK_OUT_TIMESTAMP_EST":
        record.get("HOTEL_CHECK_OUT_TIMESTAMP_EST"),

    "HOTEL_CHECK_OUT_TIMESTAMP_MDT":
        record.get("HOTEL_CHECK_OUT_TIMESTAMP_MDT"),

    "HOTEL_CHECK_OUT_TIMESTAMP_MST":
        record.get("HOTEL_CHECK_OUT_TIMESTAMP_MST"),

    "HOTEL_CHECK_OUT_TIMESTAMP_PDT":
        record.get("HOTEL_CHECK_OUT_TIMESTAMP_PDT"),

    "HOTEL_CANCELLATION_NO":
        record["HOTEL_CANCELLATION_NO"],

    "HOTEL_CANCELLATION_REASON":
        record["HOTEL_CANCELLATION_REASON"],

    "HOTEL_CANCELLATION_REASON_CODE":
        record["HOTEL_CANCELLATION_REASON_CODE"],

    "HOTEL_CANCEL_TIMESTAMP_PROPERTY":
        record["HOTEL_CANCEL_TIMESTAMP_PROPERTY"],

    "HOTEL_CANCEL_DATE":
        record["HOTEL_CANCEL_DATE"],

    "HOTEL_CANCEL_TIMESTAMP_ADT":
        record.get("HOTEL_CANCEL_TIMESTAMP_ADT"),

    "HOTEL_CANCEL_TIMESTAMP_AST":
        record.get("HOTEL_CANCEL_TIMESTAMP_AST"),

    "HOTEL_CANCEL_TIMESTAMP_CDT":
        record.get("HOTEL_CANCEL_TIMESTAMP_CDT"),

    "HOTEL_CANCEL_TIMESTAMP_CST":
        record.get("HOTEL_CANCEL_TIMESTAMP_CST"),

    "HOTEL_CANCEL_TIMESTAMP_EST":
        record.get("HOTEL_CANCEL_TIMESTAMP_EST"),

    "HOTEL_CANCEL_TIMESTAMP_MDT":
        record.get("HOTEL_CANCEL_TIMESTAMP_MDT"),

    "HOTEL_CANCEL_TIMESTAMP_MST":
        record.get("HOTEL_CANCEL_TIMESTAMP_MST"),

    "HOTEL_CANCEL_TIMESTAMP_PDT":
        record.get("HOTEL_CANCEL_TIMESTAMP_PDT"),

    "FUTURE_CHECK_IN_PROPERTIES":
        record["FUTURE_CHECK_IN_PROPERTIES"],

    "FUTURE_CHECK_IN_DATES":
        record["FUTURE_CHECK_IN_DATES"],

    "FUTURE_CHECK_IN_PROPERTIES_WITH_DATES":
        record["FUTURE_CHECK_IN_PROPERTIES_WITH_DATES"]
    }


@app.get("/v1/hotel-activity")
async def hotel_activity():

    api_url = (
        "https://casino-api-ob26.onrender.com/"
        "v1/player-activity"
    )

    response = requests.get(api_url)

    player_data = response.json()

    unique_activeclubids = []

    seen = set()

    for row in player_data:

        activeclubid = row["ACTIVECLUBID"]

        if activeclubid not in seen:

            seen.add(activeclubid)

            unique_activeclubids.append(
                activeclubid
            )

        if len(unique_activeclubids) == 50:
            break

    final_records = []

    for activeclubid in unique_activeclubids:

        stay_data = create_hotel_stay(
            activeclubid
        )

        for action in [
            "HOTEL:RESERVE",
            "HOTEL:CHECK_IN",
            "HOTEL:CHECK_OUT"
        ]:

            final_records.append(
                build_hotel_event(
                    stay_data,
                    action
                )
            )

    return final_records


if __name__ == "__main__":

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
