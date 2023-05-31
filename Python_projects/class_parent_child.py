
#parent class
class organism:
    name = "unknown"
    species = "unknown"
    legs = None
    arms = None
    dna = "sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

#child class instance
class Human(organism):
    name = "MacGuyver"
    legs = 2
    arms = 2
    origin = 'Earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a peper clip, chewing gum, and a roll of duct tape!"
        return msg

#another child class instance
class Dog(organism):
    name = "spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on  it's targer!"
        return msg

# another child class instance

class Bacteria(organism):
    name = "x"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms!"


if __name__ == "__main__":
        human = Human()
        print(human.information())
        print(human.ingenuity())

        dog = Dog()
        print(dog.information())
        print(dog.bite())

        bacteria = Bacteria()
        print(bacteria.information())
        print(bacteria.replication())
        


                                                                                                          
