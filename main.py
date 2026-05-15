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


def generate_hotel_event(activeclubid, event_action):

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

    reservation_id = fake.numerify("##########")

    membership_id = fake.numerify("######")

    membership_card = fake.bothify("MC########")

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

    cancel_date = begin_date - timedelta(hours=3)

    timezone_map = {
        "ADT": begin_date.isoformat(),
        "AST": begin_date.isoformat(),
        "CDT": begin_date.isoformat(),
        "CST": begin_date.isoformat(),
        "EST": begin_date.isoformat(),
        "MDT": begin_date.isoformat(),
        "MST": begin_date.isoformat(),
        "PDT": begin_date.isoformat()
    }

    reservation_status = {
        "HOTEL:RESERVE": "RESERVED",
        "HOTEL:CHECK_IN": "CHECKED_IN",
        "HOTEL:CHECK_OUT": "CHECKED_OUT"
    }[event_action]

    return {

        "EVENT_GROUP_ID":
            fake.uuid4(),

        "PERSONID": personid,

        "ACTIVECLUBID":
            activeclubid,

        "ENTITY":
            "HOTEL",

        "ENTITY_ACTION":
            event_action,

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

        "HOTEL_RESERVATION_STATUS":
            reservation_status,

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

        "HOTEL_RESERVATION_TIMESTAMP_ADT":
            timezone_map["ADT"],

        "HOTEL_RESERVATION_TIMESTAMP_AST":
            timezone_map["AST"],

        "HOTEL_RESERVATION_TIMESTAMP_CDT":
            timezone_map["CDT"],

        "HOTEL_RESERVATION_TIMESTAMP_CST":
            timezone_map["CST"],

        "HOTEL_RESERVATION_TIMESTAMP_EST":
            timezone_map["EST"],

        "HOTEL_RESERVATION_TIMESTAMP_MDT":
            timezone_map["MDT"],

        "HOTEL_RESERVATION_TIMESTAMP_MST":
            timezone_map["MST"],

        "HOTEL_RESERVATION_TIMESTAMP_PDT":
            timezone_map["PDT"],

        "HOTEL_CHECK_IN_TIMESTAMP_PROPERTY":
            begin_date.isoformat(),

        "HOTEL_CHECK_OUT_TIMESTAMP_PROPERTY":
            check_out_date.isoformat(),

        "HOTEL_CHECK_IN_DATE":
            begin_date.date().isoformat(),

        "HOTEL_CHECK_IN_TIMESTAMP_ADT":
            timezone_map["ADT"],

        "HOTEL_CHECK_IN_TIMESTAMP_AST":
            timezone_map["AST"],

        "HOTEL_CHECK_IN_TIMESTAMP_CDT":
            timezone_map["CDT"],

        "HOTEL_CHECK_IN_TIMESTAMP_CST":
            timezone_map["CST"],

        "HOTEL_CHECK_IN_TIMESTAMP_EST":
            timezone_map["EST"],

        "HOTEL_CHECK_IN_TIMESTAMP_MDT":
            timezone_map["MDT"],

        "HOTEL_CHECK_IN_TIMESTAMP_MST":
            timezone_map["MST"],

        "HOTEL_CHECK_IN_TIMESTAMP_PDT":
            timezone_map["PDT"],

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

        "HOTEL_CHECK_OUT_TIMESTAMP_ADT":
            check_out_date.isoformat(),

        "HOTEL_CHECK_OUT_TIMESTAMP_AST":
            check_out_date.isoformat(),

        "HOTEL_CHECK_OUT_TIMESTAMP_CDT":
            check_out_date.isoformat(),

        "HOTEL_CHECK_OUT_TIMESTAMP_CST":
            check_out_date.isoformat(),

        "HOTEL_CHECK_OUT_TIMESTAMP_EST":
            check_out_date.isoformat(),

        "HOTEL_CHECK_OUT_TIMESTAMP_MDT":
            check_out_date.isoformat(),

        "HOTEL_CHECK_OUT_TIMESTAMP_MST":
            check_out_date.isoformat(),

        "HOTEL_CHECK_OUT_TIMESTAMP_PDT":
            check_out_date.isoformat(),

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

        "HOTEL_CANCEL_TIMESTAMP_ADT":
            None,

        "HOTEL_CANCEL_TIMESTAMP_AST":
            None,

        "HOTEL_CANCEL_TIMESTAMP_CDT":
            None,

        "HOTEL_CANCEL_TIMESTAMP_CST":
            None,

        "HOTEL_CANCEL_TIMESTAMP_EST":
            None,

        "HOTEL_CANCEL_TIMESTAMP_MDT":
            None,

        "HOTEL_CANCEL_TIMESTAMP_MST":
            None,

        "HOTEL_CANCEL_TIMESTAMP_PDT":
            None,

        "FUTURE_CHECK_IN_PROPERTIES":
            property_name,

        "FUTURE_CHECK_IN_DATES":
            begin_date.date().isoformat(),

        "FUTURE_CHECK_IN_PROPERTIES_WITH_DATES":
            f"{property_name} - {begin_date.date().isoformat()}"
    }


@app.get("/v1/hotel-activity")
async def hotel_activity():

    api_url = "https://casino-api-ob26.onrender.com/v1/player-activity"

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

        for action in [
            "HOTEL:RESERVE",
            "HOTEL:CHECK_IN",
            "HOTEL:CHECK_OUT"
        ]:

            final_records.append(
                generate_hotel_event(
                    activeclubid,
                    action
                )
            )

    return final_records


if __name__ == "__main__":

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001
    )
