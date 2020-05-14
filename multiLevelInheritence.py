class MusicalInstruments:
    numberofMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = "ToneWood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar consists of {} strings. It is made of {} and it can play {} keys".format(self.numberOfStrings, self.typeOfWood, self.numberofMajorKeys))


guitar = Guitar()