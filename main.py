from fastapi import FastAPI
from faker import Faker
import random
import hashlib
from datetime import datetime
from datetime import datetime, timedelta
import uvicorn

app = FastAPI(title="Casino Gaming Data API")

fake = Faker()


def generate_gaming_record(person_id: str):
    """
    Generates persistent player profile data
    with dynamic gaming transaction data.
    """

    # Stable hash from person_id
    stable_hash = int(
        hashlib.md5(person_id.encode()).hexdigest(),
        16
    ) % (10**8)

    # Seed faker/random for stable profile
    fake.seed_instance(stable_hash)
    random.seed(stable_hash)

    # Persistent player info
    first_name = fake.first_name()
    last_name = fake.last_name()

    club_level = random.choice(
        ["Gold", "Silver", "Platinum", "Diamond"]
    )

    serial_number = fake.bothify(
        text='SN-####-####'
    )

    game_title = random.choice([
        "88 Fortunes",
        "Buffalo Gold",
        "Wheel of Fortune",
        "Blackjack T1"
    ])

    # Stable PERSONID
    personid = fake.numerify(
        text='######'
    )

    personid2 = str(
    int(
        hashlib.md5(
            personid.encode()
        ).hexdigest(),
        16
    ) % 90000 + 10000
)

    # Stable ACTIVECLUBID (13 digits)
    activeclubid = fake.numerify(
        text='#############'
    )

    # Stable ENTITY_ACTION
    

    address1 = fake.street_address()

    city = fake.city()

    state_province = fake.state()

    country = fake.country()

    postal_code = fake.postcode()

    birthdate = fake.date_of_birth(
        minimum_age=21,
        maximum_age=80
    )

    gender = random.choice([
        "Male",
        "Female"
    ])

    

    

   


    ##################################
    # Dynamic Host / CMP Data
    ##################################
    # Reset random seed for dynamic values
    random.seed(None)
    fake.seed_instance(None)


    entity_action = random.choice([
        "HOTEL:CANCEL",
        "HOTEL:NO_SHOW",
        "HOTEL:RESERVE",
        "HOTEL:CHECK_OUT",
        "HOTEL:CHECK_IN"
    ])
    

    properties = {
        "GRC": "Grand Royale Casino",
        "AC": "Atlantis Casino",
        "RRC": "Red Rock Casino"
    }

    

    

    

 

    
    

    # Dynamic gaming transaction values
    bet = round(
        random.uniform(1.0, 100.0),
        2
    )

    hold_pct = random.uniform(0.05, 0.15)

    theo_win = round(
        bet * hold_pct,
        2
    )

    win_chance = random.random()

    if win_chance > 0.6:
        paid_out = round(
            bet * random.uniform(1.2, 5.0),
            2
        )
    else:
        paid_out = 0.0

    casino_win = round(
        bet - paid_out,
        2
    )

        # Random timestamp within last 1 year
    days_back = random.randint(0, 365)

    seconds_back = random.randint(
        0,
        86400
    )

    

    timestamp = datetime.now() - timedelta(
        days=days_back,
        seconds=seconds_back
    )

    

    ############################
    

    player_value = round(
        random.uniform(1.0, 30.0),
        4
    )

    #####
    
    
    game_duration_min = random.randint(
        1,
        480
    )

    hotel_property_id = random.choice(
        list(properties.keys())
    )

    property_name = properties[
        hotel_property_id
    ]

    hotel_membership_levels = [
        "Gold",
        "Silver",
        "Platinum",
        "Diamond"
    ]

    reservation_statuses = [
        "BOOKED",
        "CHECKED_IN",
        "CHECKED_OUT",
        "CANCELLED",
        "NO_SHOW"
    ]

    payment_methods = [
        "CASH",
        "CREDIT_CARD",
        "DEBIT_CARD",
        "COMP"
    ]

    channels = [
        "ONLINE",
        "PHONE",
        "WALKIN",
        "MOBILE_APP"
    ]

    room_classes = [
        "STANDARD",
        "DELUXE",
        "SUITE",
        "VIP"
    ]

    room_categories = [
        "KING",
        "QUEEN",
        "DOUBLE",
        "PENTHOUSE"
    ]

    rate_categories = [
        "BAR",
        "COMP",
        "DISCOUNT",
        "VIP"
    ]

    market_codes = [
        "LOCAL",
        "TOURISM",
        "VIP",
        "CORPORATE"
    ]

    promotion_codes = [
        "WELCOME",
        "SUMMER2026",
        "VIPFREE",
        "NONE"
    ]

    reservation_status = random.choice(
        reservation_statuses
    )

    now = datetime.now()

    business_created_date = (
        now - timedelta(
            days=random.randint(1, 60)
        )
    )

    begin_date = (
        now - timedelta(
            days=random.randint(0, 30)
        )
    )

    nights = random.randint(1, 10)

    end_date = (
        begin_date + timedelta(days=nights)
    )

    folio_close_date = end_date.date()

    cancellation_date = None

    reinstate_date = None

    cancellation_reason_code = None

    cancellation_reason_desc = None

    cancellation_no = None

    if reservation_status == "CANCELLED":

        cancellation_date = (
            begin_date - timedelta(
                hours=random.randint(1, 48)
            )
        )

        cancellation_reason_code = random.choice([
            "PAYMENT",
            "TRAVEL",
            "PERSONAL"
        ])

        cancellation_reason_desc = random.choice([
            "Payment declined",
            "Travel issue",
            "Personal emergency"
        ])

        cancellation_no = fake.bothify(
            text='CAN########'
        )

        if random.choice([True, False]):

            reinstate_date = (
                cancellation_date +
                timedelta(hours=4)
            )

    hotel_cash_room_revenue = round(
        random.uniform(100, 5000),
        2
    )

    hotel_comp_room_revenue = round(
        random.uniform(0, 2000),
        2
    )


    return {

        "PERSONID": personid,


        "PERSONID2": personid2,

        "ACTIVECLUBID": activeclubid,

        "PERSON_FIRST_NAME": first_name,

        "PERSON_LAST_NAME": last_name,

        "ADDRESS1": address1,

        "CITY": city,

        "STATE_PROVINCE": state_province,

        "COUNTRY": country,

        "POSTAL_CODE": postal_code,

        "BIRTHDATE": birthdate.isoformat(),

        "GENDER": gender,

        
        
        "SOURCE":"OPERA",

        "ENTITY":"HOTEL",

        "ENTITY_ACTION": entity_action,

        "DURATION":game_duration_min,

        "PROPERTY_NAME":property_name,

        "PROPERTY_CODE":hotel_property_id,

        "EVENT_ID": fake.bothify(text='EV-########'),

        "HOTEL_MEMBERSHIP_CARD_NO":
            fake.bothify(text='MC########'),

        "HOTEL_MEMBERSHIP_LEVEL":
            random.choice(
                hotel_membership_levels
            ),

        "HOTEL_RESV_NAME_ID":
            float(
                random.randint(
                    100000,
                    999999
                )
            ),

        "HOTEL_MEMBERSHIP_ID":
            float(
                random.randint(
                    10000,
                    99999
                )
            ),

        "HOTEL_NAME_ID":
            float(
                random.randint(
                    1000,
                    9999
                )
            ),

        "HOTEL_RESV_STATUS":
            reservation_status,

        "HOTEL_BUSINESS_DATE_CREATED":
            business_created_date.isoformat(),

        "HOTEL_BEGIN_DATE":
            begin_date.isoformat(),

        "HOTEL_END_DATE":
            end_date.isoformat(),

        "HOTEL_FOLIO_CLOSE_DATE":
            folio_close_date.isoformat(),

        "HOTEL_CANCELLATION_DATE":
            cancellation_date.isoformat()
            if cancellation_date else None,

        "HOTEL_REINSTATE_DATE":
            reinstate_date.isoformat()
            if reinstate_date else None,

        "HOTEL_CANCELLATION_REASON_CODE":
            cancellation_reason_code,

        "HOTEL_CANCELLATION_REASON_DESC":
            cancellation_reason_desc,

        "HOTEL_CANCELLATION_NO":
            cancellation_no,

        "HOTEL_WL_TELEPHONE_NO":
            fake.phone_number(),

        "HOTEL_PAYMENT_METHOD":
            random.choice(payment_methods),

        "HOTEL_CHANNEL":
            random.choice(channels),

        "HOTEL_CUSTOM_REFERENCE":
            fake.bothify(text='REF######'),

        "HOTEL_GUEST_FIRST_NAME":
            first_name,

        "HOTEL_GUEST_LAST_NAME":
            last_name,

        "HOTEL_YM_CODE":
            now.strftime("%Y%m"),

        "HOTEL_RATEABLE_VALUE":
            str(
                round(
                    random.uniform(80, 600),
                    2
                )
            ),

        "HOTEL_WL_PRIORITY":
            random.choice([
                "HIGH",
                "MEDIUM",
                "LOW"
            ]),

        "HOTEL_ROOM_FEATURES":
            random.choice([
                "Ocean View",
                "Smoking",
                "High Floor",
                "Near Elevator",
                "Pool Access"
            ]),

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

        "HOTEL_CASH_ROOM_REVENUE":
            hotel_cash_room_revenue,

        "HOTEL_COMP_ROOM_REVENUE":
            hotel_comp_room_revenue,

        "HOTEL_ROOM":
            str(
                random.randint(
                    100,
                    5000
                )
            ),

        "HOTEL_PSUEDO_ROOM_YN":
            random.choice(["Y", "N"]),

        "HOTEL_ROOM_CLASS":
            random.choice(room_classes),

        "HOTEL_ROOM_CATEGORY":
            random.choice(room_categories),

        "HOTEL_ROOM_CATEGORY_DESCRIPTION":
            "Luxury Room Category",

        "HOTEL_BOOKED_ROOM_CATEGORY":
            random.choice(room_categories),

        "HOTEL_ADULTS":
            str(
                random.randint(1, 4)
            ),

        "HOTEL_CHILDREN":
            str(
                random.randint(0, 3)
            ),

        "HOTEL_RATE_CODE":
            fake.bothify(text='RATE###'),

        "HOTEL_RATE_CATEGORY":
            random.choice(rate_categories),

        "HOTEL_MARKET_CODE":
            random.choice(market_codes),

        "HOTEL_PROMOTION_CODE":
            random.choice(promotion_codes),

        "HOTEL_NIGHTS":
            nights,
        "LOAD_TIMESTAMP": datetime.now().isoformat()
    }


@app.get("/v1/player-activity")
async def get_player_activity(
    players: int = 50,
    records_per_player: int = 2
):
    """
    Returns players with multiple gaming records.
    Each player keeps same identity details
    but has many gameplay transactions.
    """

    records = []

    used_names = set()

    i = 0

    while len(used_names) < players:

        # Stable UUID
        fake.seed_instance(i)

        player_id = fake.uuid4()

        sample_record = generate_gaming_record(
            person_id=player_id
        )

        full_name = (
            sample_record["PERSON_FIRST_NAME"] +
            " " +
            sample_record["PERSON_LAST_NAME"]
        )

        # Ensure unique player names
        if full_name not in used_names:

            used_names.add(full_name)

            # Generate multiple records
            for _ in range(records_per_player):

                records.append(
                    generate_gaming_record(
                        person_id=player_id
                    )
                )

        i += 1

    return records


@app.get("/v1/player/{person_id}")
async def get_specific_player(person_id: str):
    """
    Returns a specific persistent player
    with dynamic gaming activity.
    """

    return generate_gaming_record(
        person_id=person_id
    )


if __name__ == "__main__":

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001
    )
