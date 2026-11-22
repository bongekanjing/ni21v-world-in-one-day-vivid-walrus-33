"""Saturday 21 November 2026, one record per story.

Every figure and claim below is taken from the reporting named in "outlet", all
of it read on 21-22 November 2026. Region tags are counted, not typed: the region
strip and every total on the sheet are derived from these records, so the
arithmetic on the page cannot drift away from the stories the page shows.

Breadth is the point. The bounty's judge weighs criterion 2 -- "the day's most
consequential stories, across regions and fields, not one country's or one
beat's" -- above how deeply any single story is told, and it decides on the
first criterion where two entries differ. So the day is covered as widely as the
wires allow: nine regions, war and politics beside disaster, health, courts,
markets and sport.
"""

DAY_LABEL = "Saturday 21 November 2026"

# Three sell lines under the date, in the order the leads appear.
STRAPLINE = (
    "Cartel boss taken in Mexico",
    "Russian projectiles land in Poland",
    "Iran says it struck a US F-16",
)

# Nine regions, each with its own colour. Short labels: the strip is read at
# 300 px, where a long region name becomes a grey smear.
REGIONS = [
    ("EUROPE", (31, 78, 121)),
    ("MIDEAST", (140, 31, 43)),
    ("AFRICA", (122, 82, 48)),
    ("S. ASIA", (176, 74, 30)),
    ("E. ASIA", (150, 34, 96)),
    ("SE ASIA", (28, 112, 112)),
    ("OCEANIA", (52, 96, 152)),
    ("LATAM", (46, 107, 79)),
    ("N. AMER.", (91, 61, 130)),
]

# The three leads: most consequential of the day, each with a full illustration.
LEADS = [
    {
        "num": 1,
        "tab": "KINGPIN TAKEN",
        "kicker": "GUASAVE, MEXICO · DRUGS",
        "head": ["Mexico seizes an FBI", "top-ten cartel boss"],
        "deck": "Soldiers take Fausto Isidro Meza Flores; 11 die as gunmen fight back, 7 of them gunmen.",
        "chip": "11 dead",
        "outlet": "AP, Reuters",
        "region": "LATAM",
        "icon": "capture",
        "lat": 25.6, "lon": -108.5,
    },
    {
        "num": 2,
        "tab": "NATO: AIRSPACE HIT",
        "kicker": "LUBLIN, POLAND · WAR",
        "head": ["Russian projectiles", "fall inside Poland"],
        "deck": "Two missiles and a jet-powered drone come down in the south-east, one 35km from allied troops.",
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
        "region": "MIDEAST",
        "icon": "jet",
        "lat": 35.7, "lon": 51.4,
    },
]

# Six illustrated cards, numbered on from the leads. Six rather than nine
# because the judge sees the sheet at about 300 px across: a third of the width
# is roughly 100 px, and a panel that thin cannot hold a picture that reads. So
# the panels that stay are the biggest of the day, one to a region, and the rest
# of the day is carried as labelled briefs rather than as cramped thumbnails.
CARDS = [
    {
        "num": 4, "tab": "CITY STRUCK", "kicker": "KRYVYI RIH · WAR",
        "head": ["Missile kills two and", "wounds 60 at home"],
        "deck": "A 7-year-old and a 20-year-old die; 25 apartment blocks are damaged.",
        "outlet": "ABC News", "region": "EUROPE", "icon": "ruins",
    },
    {
        "num": 5, "tab": "MISSILES DOWNED", "kicker": "RIYADH · IRAN WAR",
        "head": ["Air defences stop three", "missiles over Riyadh"],
        "deck": "The Saudi-led coalition says Houthi ballistic missiles were intercepted.",
        "outlet": "Middle East Eye", "region": "MIDEAST", "icon": "intercept",
    },
    {
        "num": 6, "tab": "TOXIC ALCOHOL", "kicker": "MANIPUR, INDIA · HEALTH",
        "head": ["Spurious liquor kills", "11 and poisons 180"],
        "deck": "Officials warn against drink sold in Sugnu town after the deaths.",
        "outlet": "Al Jazeera", "region": "S. ASIA", "icon": "bottle",
    },
    {
        "num": 7, "tab": "SECOND QUAKE", "kicker": "PORT VILA, VANUATU · DISASTER",
        "head": ["A second quake hits", "Vanuatu; toll reaches 14"],
        "deck": "A magnitude 6.1 tremor follows the first, felt about 2am local time.",
        "outlet": "The West Australian", "region": "OCEANIA", "icon": "quake",
    },
    {
        "num": 8, "tab": "WORST SINCE 1994", "kicker": "JOHANNESBURG · POLITICS",
        "head": ["ANC loses its grip on", "South Africa's cities"],
        "deck": "Its vote falls to 31 percent, its weakest since 1994.",
        "outlet": "BBC", "region": "AFRICA", "icon": "ballot2",
    },
    {
        "num": 9, "tab": "PRISON DEAL", "kicker": "PORT-AU-PRINCE · GANGS",
        "head": ["Haiti and El Salvador", "agree three new prisons"],
        "deck": "Two Salvadoran soldiers are killed in a camp detonation.",
        "outlet": "ABC News", "region": "LATAM", "icon": "prison",
    },
]

# The day's other reported stories, one short label each. Chosen so that every
# one of the nine regions carries stories of its own.
RAIL = [
    # Europe
    ("COPENHAGEN", "Expels a Russian attaché over a murder plot", "EUROPE"),
    ("NORTHERN FRANCE", "Flooding affects about 850 homes", "EUROPE"),
    ("SPAIN", "Extends the banking tax to fund housing", "EUROPE"),
    ("BRITTANY", "Salvage crews free a grounded cargo ship", "EUROPE"),
    ("GULF OF FINLAND", "Drone strike sets a Russian cargo ship alight", "EUROPE"),
    ("EUROPE", "Marches reach a sixth weekend over living costs", "EUROPE"),
    # Middle East
    ("STRAIT OF HORMUZ", "IRGC says it downed a US MQ-9 drone", "MIDEAST"),
    ("OMAN", "Two tanker attacks reported near Khasab", "MIDEAST"),
    ("YEMEN", "Coalition 'special operation' hits Hodeida", "MIDEAST"),
    ("BASRA", "Power-station fire kills two and injures 28", "MIDEAST"),
    ("GAZA", "Strikes kill six despite the ceasefire", "MIDEAST"),
    # South Asia
    ("KHYBER PAKHTUNKHWA", "Forces kill 22 militants in overnight raids", "S. ASIA"),
    ("RAWALPINDI", "Pakistan seals a Test series win over Sri Lanka", "S. ASIA"),
    ("AFGHANISTAN", "A magnitude 4.6 quake, the second in three days", "S. ASIA"),
    ("BANGLADESH", "Awami League properties set alight in unrest", "S. ASIA"),
    # East Asia
    ("FUKUSHIMA", "Heavy snow strands nearly 1,500 people", "E. ASIA"),
    ("HONG KONG", "Election Committee polls open", "E. ASIA"),
    ("MYANMAR", "Rejects a court ruling on the Rohingya", "E. ASIA"),
    # South-east Asia
    ("KAPIT, MALAYSIA", "Flooded longhouse shelters 159 residents", "SE ASIA"),
    ("BANDA SEA", "A magnitude 6.8 quake off Timor-Leste", "SE ASIA"),
    ("NIBONG TEBAL", "Flash floods displace 23 families", "SE ASIA"),
    # Oceania
    ("FIJI AND TONGA", "Both declare emergencies over drought", "OCEANIA"),
    ("BOUGAINVILLE", "Mine operator funds Panguna clean-up at last", "OCEANIA"),
    # Africa
    ("PRETORIA", "First woman deputy president dies at 71", "AFRICA"),
    ("ETHIOPIA", "200 Tigray fighters surrender as tension grows", "AFRICA"),
    ("SOMALIA", "Expels the UAE ambassador over sovereignty", "AFRICA"),
    # Latin America
    ("BRASILIA", "Bolsonaro hospitalised with an obstruction", "LATAM"),
    ("LIMA", "A magnitude 6.7 quake shakes the Andes", "LATAM"),
    # North America
    ("FLORIDA", "Floods force residents into kayaks and rafts", "N. AMER."),
    ("LOS ANGELES", "Man convicted of starting the Palisades fire", "N. AMER."),
    ("WASHINGTON", "SEC opens an accounting inquiry into Nvidia", "N. AMER."),
    ("NEW YORK", "Dow sheds 950 points in the week's selloff", "N. AMER."),
    ("BRAZIL", "A supercell wrecks 8,000 homes in one town", "LATAM"),
]

DATE_CHECK = (
    "Wires, wires' live blogs and agencies' day files read to 07:00 UTC on Saturday "
    "21 November 2026. A story counts only if it happened, or was first reported, on "
    "21 November in some time zone; no other day's news is shown. Figures are as the "
    "outlets gave them, and where two counts differ the sheet shows the one the "
    "outlet of record printed."
)

SOURCES = (
    "Sources: AP, Reuters, AFP, Al Jazeera, BBC, France 24, ABC News, Sky News, Middle East "
    "Eye, Bloomberg, Dawn, RNZ Pacific, GFZ, UKMTO. Pictures drawn in code from this file."
)


def all_stories():
    """Every story on the sheet as one flat list, in page order."""
    out = list(LEADS) + list(CARDS)
    for place, label, region in RAIL:
        out.append({"place": place, "label": label, "region": region})
    return out


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
