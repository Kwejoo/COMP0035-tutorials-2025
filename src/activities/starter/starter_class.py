class ParalympicEvent:
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in the event

     Methods:
         describe() Prints a description of the event
         register_athlete() Adds an athlete to the list of athletes

     """
    
    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []  # Empty list to hold athlete names

    def describe(self):
        """ Describes the event """
        print(f"{self.name} is a {self.sport} event for classification {self.classification}.")
        print("Athletes competing:", ", ".join(self.athletes))

    def register_athlete(self, athlete_name):
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)


sprint = ParalympicEvent("100m Sprint", "Athletics", 1)

longJump = ParalympicEvent("Long Jump", "Athletics", 2)

swimming = ParalympicEvent("50m Freestyle", "Swimming", 3)

waterPolo = ParalympicEvent("Water Polo", "Team Sport", 4)

football = ParalympicEvent("5-a-side Football", "Team Sport", 5)

sprint.register_athlete("Athlete A")
sprint.register_athlete("Athlete B")


class Athlete:
    def __init__(self, name, team, disability):
        self.name = name
        self.team = team
        self.disability = disability
    
    def introduce(self):
        print(
            f"My name is {self.name}, I represent {self.team}, and I have a "
            f"{self.disability} disability."
        )

athlete1 = Athlete("Athlete A", "Country X", "visual impairment")

athlete1.introduce()