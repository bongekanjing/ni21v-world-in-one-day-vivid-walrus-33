"""Saturday 21 November 2026, one record per story.

Every figure and claim below is taken from the reporting named in "outlet".
Region tags are counted, not typed: the region strip and every total on the
sheet are derived from these records, so the arithmetic on the page cannot
drift away from the stories the page shows.
"""

DAY_LABEL = "Saturday 21 November 2026"

# Three sell lines under the date, in the order the leads appear.
STRAPLINE = (
    "Cartel boss taken in Mexico",
    "Russian projectiles land in Poland",
    "Iran says it hit a US F-16",
)

REGIONS = [
    ("EUROPE", (31, 78, 121)),
    ("MIDDLE EAST", (140, 31, 43)),
    ("AMERICAS", (46, 107, 79)),
    ("ASIA-PACIFIC", (184, 98, 27)),
    ("AFRICA", (122, 82, 48)),
    ("WORLD", (91, 61, 130)),
]

# The three leads: most consequential of the day, each with a full illustration.
LEADS = [
    {
        "num": 1,
        "tab": "KINGPIN TAKEN",
        "kicker": "GUASAVE, MEXICO · DRUGS",
        "head": ["Mexico seizes an FBI", "top-ten cartel boss"],
        "deck": "Soldiers take Fausto Isidro Meza Flores; 11 die as gunmen fight back.",
        "chip": "11 dead",
        "outlet": "AP, Reuters",
        "region": "AMERICAS",
        "icon": "capture",
        "lat": 25.6, "lon": -108.5,
    },
    {
        "num": 2,
        "tab": "NATO: AIRSPACE HIT",
        "kicker": "LUBLIN, POLAND · WAR",
        "head": ["Russian projectiles", "fall inside Poland"],
        "deck": "Two missiles and a drone land 35km from allied troops; Warsaw calls it a provocation.",
        "chip": "3 fell",
        "outlet": "Al Jazeera, France 24",
        "region": "EUROPE",
        "icon": "missiles",
        "lat": 51.2, "lon": 22.6,
    },
    {
        "num": 3,
        "tab": "IRAN: JET HIT",
        "kicker": "TEHRAN · IRAN WAR",
        "head": ["Iran says it struck", "a US F-16 with a missile"],
        "deck": "State media report a damaged jet and an emergency landing; Washington has not commented.",
        "chip": "1 F-16",
        "outlet": "Middle East Eye",
        "region": "MIDDLE EAST",
        "icon": "jet",
        "lat": 35.7, "lon": 51.4,
    },
]

# Twice-told stories: illustrated cards, numbered on from the leads.
CARDS = [
    {
        "num": 4, "tab": "CITY STRUCK", "kicker": "KRYVYI RIH · WAR",
        "head": ["Missile kills two and", "wounds 60 at home"],
        "deck": "A 7-year-old and a 20-year-old die; 25 blocks are damaged.",
        "outlet": "ABC News", "region": "EUROPE", "icon": "ruins",
    },
    {
        "num": 5, "tab": "SHIP ABLAZE", "kicker": "GULF OF FINLAND · WAR",
        "head": ["Drone strike sets a", "Russian cargo ship alight"],
        "deck": "Finland alerts NATO and restricts air and sea near Suursaari.",
        "outlet": "France 24", "region": "EUROPE", "icon": "ship",
    },
    {
        "num": 6, "tab": "PROTESTS GROW", "kicker": "PARIS · UNREST",
        "head": ["Marches reach a sixth", "weekend across Europe"],
        "deck": "Cost-of-living protests spread to more than 20 countries.",
        "outlet": "France 24", "region": "EUROPE", "icon": "crowd",
    },
    {
        "num": 7, "tab": "PLOT THWARTED", "kicker": "COPENHAGEN · SECURITY",
        "head": ["Denmark expels an attache", "over a murder plot"],
        "deck": "It says Russia planned to kill the rapper Kyivstoner.",
        "outlet": "Al Jazeera, Sky", "region": "EUROPE", "icon": "spy",
    },
    {
        "num": 8, "tab": "SIX KILLED", "kicker": "GAZA · CEASEFIRE",
        "head": ["Strikes kill six despite", "the ceasefire"],
        "deck": "Civil defence reports four dead near Bureij and two in drone strikes.",
        "outlet": "Middle East Eye", "region": "MIDDLE EAST", "icon": "rubble",
    },
    {
        "num": 9, "tab": "DRONE DOWNED", "kicker": "STRAIT OF HORMUZ · WAR",
        "head": ["Iran says it shot down", "a US MQ-9 drone"],
        "deck": "The IRGC calls it the 58th such drone destroyed over the strait.",
        "outlet": "Middle East Eye", "region": "MIDDLE EAST", "icon": "dronehit",
    },
    {
        "num": 10, "tab": "MISSILES DOWNED", "kicker": "RIYADH · IRAN WAR",
        "head": ["Air defences stop three", "missiles over Riyadh"],
        "deck": "The Saudi-led coalition says Houthi ballistic missiles were intercepted.",
        "outlet": "Middle East Eye", "region": "MIDDLE EAST", "icon": "intercept",
    },
    {
        "num": 11, "tab": "POWER PLANT FIRE", "kicker": "BASRA, IRAQ · ENERGY",
        "head": ["Fire stops an 800MW", "plant near Basra"],
        "deck": "At least two die and 28 are hurt; the cause is not yet known.",
        "outlet": "Al Jazeera, Reuters", "region": "MIDDLE EAST", "icon": "powerplant",
    },
    {
        "num": 12, "tab": "TOXIC ALCOHOL", "kicker": "MANIPUR, INDIA · HEALTH",
        "head": ["Spurious liquor kills", "11 and poisons 180"],
        "deck": "Officials warn against drink from Sugnu town after the deaths.",
        "outlet": "Al Jazeera", "region": "ASIA-PACIFIC", "icon": "bottle",
    },
]

# The day's other reported stories, one short label each.
RAIL = [
    {"place": "HONG KONG", "label": "Election Committee polls open on Sunday", "region": "ASIA-PACIFIC"},
    {"place": "SOUTH AFRICA", "label": "ANC slides to 31pc, its worst local result since 1994", "region": "AFRICA"},
    {"place": "HAITI", "label": "El Salvador to build three new prisons", "region": "AMERICAS"},
    {"place": "SOUTH AFRICA", "label": "First woman deputy president dies at 71", "region": "AFRICA"},
    {"place": "ETHIOPIA", "label": "200 Tigray fighters surrender as Eritrea tension grows", "region": "AFRICA"},
    {"place": "BRAZIL", "label": "Bolsonaro hospitalised with an obstruction", "region": "AMERICAS"},
    {"place": "PERU", "label": "Magnitude 6.7 quake shakes the Andes, no damage", "region": "AMERICAS"},
    {"place": "GENEVA", "label": "UN agrees two more years of talks on killer robots", "region": "WORLD"},
    {"place": "UNITED STATES", "label": "Buffett gives $5.5bn to family foundations", "region": "AMERICAS"},
    {"place": "UNITED NATIONS", "label": "UK, France and China block the UAE's Nusseibeh", "region": "WORLD"},
    {"place": "PHILIPPINES", "label": "Air Niugini jet lands safely after an engine alarm", "region": "ASIA-PACIFIC"},
    {"place": "SPACE", "label": "SpaceX will not refly its caught Starship stage", "region": "WORLD"},
]

DATE_CHECK = (
    "Wires read to 06:00 UTC on Saturday 21 November 2026. Every story here was reported, "
    "or still developing, on 21 November in at least one time zone; the Hong Kong poll was "
    "announced on the 21st for the following day. Left out as other days' news: the "
    "Kryvyi Rih toll first reported on the 21st is kept, the Shenzhen summit (10 Nov) and "
    "the earlier Kerch bridge strikes are not."
)

SOURCES = (
    "Sources: AP, Reuters, AFP, Al Jazeera, BBC, France 24, ABC News, Sky News, Middle East "
    "Eye, AsiaShift. Pictures drawn in code from this file; no photograph is used."
)


def all_stories():
    """Every story on the sheet as one flat list, in page order."""
    return list(LEADS) + list(CARDS) + list(RAIL)


def region_counts():
    """Count the stories per region, straight from the records above."""
    counts = {name: 0 for name, _ in REGIONS}
    for story in all_stories():
        counts[story["region"]] += 1
    return counts


def total_stories():
    """How many stories the sheet carries, counted rather than asserted."""
    return len(LEADS) + len(CARDS) + len(RAIL)


def rail_start():
    """The number the rail starts at, derived from the sections above it."""
    return len(LEADS) + len(CARDS) + 1
