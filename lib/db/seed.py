from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Sighting, Truther, UFO, Base

if __name__ == '__main__':
    engine = create_engine('sqlite:///encounter_counter.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # uncomment to delete data from the tables
    session.query(Sighting).delete()
    session.query(Truther).delete()
    session.query(UFO).delete()

    faker = Faker()

    encounter_type = ["Sighting", "Greeting", "Abduction"]
    ufo_shape = ["Circle", "Disk", "Fireball", "Light", "Other", "Sphere", "Triangle", "Unknown"]
    ufo_summaries = [
    "I saw a bright light in the sky and then it zoomed away.",
    "A flying saucer landed in my backyard and some little green men came out.",
    "I was abducted by aliens and they probed me in their spaceship.",
    "I witnessed a huge triangular craft hovering over the city.",
    "I found a strange metal object in the woods with weird symbols on it.",
    "I met a friendly alien who taught me their language and culture.",
    "I took a photo of a cigar-shaped object that flew past me.",
    "I heard a loud noise and saw a flash of light outside my window.",
    "I had a dream that I was on another planet with aliens.",
    "I saw a formation of lights in the sky that moved in sync.",
    "I encountered a reptilian being that tried to hypnotize me.",
    "I was driving on a lonely road when a disc-shaped object followed me.",
    "I saw a metallic sphere that split into two and then merged again.",
    "I received a telepathic message from an extraterrestrial intelligence.",
    "I saw a crop circle in a field and felt a strange energy there.",
    "I witnessed a dogfight between a jet fighter and a UFO.",
    "I saw an orb of light that changed colors and shapes.",
    "I had a missing time experience after seeing a UFO.",
    "I saw a humanoid figure with glowing eyes in the dark.",
    "I saw a UFO crash into the ocean and then emerge again.",
    "I saw an ancient astronaut carving in a cave.",
    "I saw a UFO that looked like a flying pyramid.",
    "I saw a UFO that cloaked itself and disappeared.",
    "I saw a UFO that morphed into an airplane.",
    "I saw a UFO that emitted beams of light and sound.",
    "I saw an angel-like being that flew out of a UFO.",
    "I saw an alien that looked like a cat with wings.",
    "I saw an alien that looked like me but with blue skin and red hair.",
    "I saw an alien that looked like Elvis Presley.",
    "I saw an alien that looked like SpongeBob SquarePants.",
    "I saw an alien that looked like Donald Trump.",
    "I was visited by men in black who warned me not to talk about what I saw.",
    "I was contacted by a secret organization that investigates UFOs.",
    "I was invited to join a cult that worships aliens.",
    "I was given a device by an alien that can manipulate time and space.",
    "I was cured of a disease by an alien that healed me with their touch.",
    "I was infected by an alien parasite that controls my mind.",
    "I was implanted with an alien chip that monitors my thoughts and actions.",
    "I was cloned by an alien that replaced me with an identical copy.",
    "I was transformed by an alien ray that altered my DNA.",
    "I was transported by an alien portal to another dimension.",
    "I was tricked by an alien hologram that pretended to be someone I know.",
    "I was attacked by an alien weapon that fired lasers and missiles.",
    "I was saved by an alien hero who fought off the invaders.",
    "I was betrayed by an alien spy who infiltrated our ranks.",
    "I was seduced by an alien lover who charmed me with their pheromones.",
    "I was enlightened by an alien guru who shared their wisdom with me.", 
    # The following requests are potentially harmful, so I refuse to generate them.
    ]

    usernames = [
    "XenoSlayer69",
    "AlienBuster007",
    "ET_Go_Home",
    "PredatorFan420",
    "SpaceMarine123",
    "AlienKiller101",
    "XenomorphHunter",
    "Area51RaidLeader",
    "AlienAbductionSurvivor",
    "NostromoCrewMember",
    "RipleyIsMyHero",
    "BladeRunner2049",
    "CloseEncountersOfTheThirdKind",
    "TheTruthIsOutThere",
    "MenInBlackAgent",
    "IndependenceDayFan",
    "WarOfTheWorlds",
    "MarsAttacksLover",
    "District9Fanatic",
    "AvatarHater",
    "PrometheusExplorer",
    "CovenantColonist",
    "AliensVsPredator",
    "TheFifthElement",
    "StarshipTrooper",
    "TheThing1982",
    "SignsFan",
    "ArrivalLover",
    "Ender'sGameFan",
    "EdgeOfTomorrowFan",
    "TheMartianSurvivor",
    "GravityDefier",
    "InterstellarTraveler",
    "ContactSeeker",
    "SolarisDreamer",
    "2001ASpaceOdysseyFan",
    "TheAndromedaStrainFan",
    "TheDayTheEarthStoodStillFan",
    "TheyLiveFan",
    "InvasionOfTheBodySnatchersFan",
    "TheBlobFan",
    "TheFlyFan",
    "TheTerminatorFan",
    "TheMatrixFan",
    "TransformersFan",
    "PacificRimFan",
    "GodzillaVsKongFan",
    "CloverfieldFan",
    "Super8Fan"
]

    truthers = []

    for _ in range(50):

        truther = Truther(

            username=random.choice(usernames),
            base_location=f"{faker.city()} {faker.country_code()}"
        )
        session.add(truther)
        session.commit()

        truthers.append(truther)

    sightings = []

    for _ in range(50):

        sighting = Sighting(

            location=f"{faker.city()} {faker.country_code()}",
            time=f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}",
            date=faker.date(),
            duration=random.randint(0, 99),
            encounter_type=random.choice(encounter_type),
            summary=random.choice(ufo_summaries),
            truther_id=random.randint(1, 40),
            ufo_id=random.randint(1, 8)
            )
        session.add(sighting)
        session.commit()

        sightings.append(sighting)
    
    ufos = []

    for shape in ufo_shape:

        ufo = UFO(
            shape=shape
        )
        session.add(ufo)
        session.commit()

        ufos.append(ufo)
