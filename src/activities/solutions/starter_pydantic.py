""" Starter for activity 5.4 Pydantic classes with validation """
from datetime import date
from enum import Enum

from pydantic import BaseModel, ValidationError


# This is not a Pydantic class! It is an Enum https://docs.python.org/3/library/enum.html
class MedalType(Enum):
    BRONZE = 3
    SILVER = 2
    GOLD = 1


class Medal(BaseModel):
    """ Represents a Medal

    Attributes:
        type (MedalType):  A string representing "gold", "silver", "bronze"
        date_won (date):  Date the medal was won

    """
    type: MedalType
    date_won: date


class Athlete(BaseModel):
    """ Represents an Athlete

        Attributes:
            first_name (str): The first name of the athlete.
            last_name (str): The last name of the athlete.
            team_code (str): The team code the athlete represents.
            disability_class (str): The disability classification of the athlete.

        Methods:
            introduce(): Prints an introduction of the athlete.
    """
    first_name: str
    last_name: str
    team_code: str
    disability_class: str
    medals: list[Medal]

    def introduce(self) -> str:
        """
        Prints an introduction of the athlete, including their name, team, and disability class.
        """
        count = len(self.medals)
        medal_word = "medal" if count == 1 else "medals"
        message = f"{self.first_name} {self.last_name} represents {self.team_code} in class {self.disability_class}. He has won {count} {medal_word}."
        print(message)
        return message


class ParalympicEvent(BaseModel):
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in the event

     Methods:
         register_athlete() Adds an athlete to the list of athletes

     """
    name: str
    sport: str
    classification: str
    athletes: list[Athlete]

    def register_athlete(self, athlete: Athlete):
        """ Register the athlete with the event

        Args:
            athlete (Athlete): The athlete to register
        """
        self.athletes.append(athlete)

medals1 = Medal(type=MedalType.GOLD, date_won=date(2024, 8, 29))

athlete = Athlete(
    first_name="Yuyan",
    last_name="Jiang",
    team_code="CHN",
    disability_class="T44",
    medals=[]
)

athlete.introduce()

athlete.medals.append(medals1) # "Yuyan Jiang represents CHN in class T44."

athlete.introduce()
  # "Yuyan Jiang represents CHN in class T44."

athlete.medals.append(medals1) # "Yuyan Jiang represents CHN in class T44."

athlete.introduce()



try:
    bp = Athlete(first_name="Bianka", medals=1)
except ValidationError as e:
    print(e.errors())