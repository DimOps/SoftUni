class Vet:
    animals = []  # total amount of animals for all vets
    space = 5  # clinics capacity

    def __init__(self, name):
        self.name = name
        self.animals = []  # personal animals

    def register_animal(self, animal_name):
        if len(Vet.animals) < Vet.space:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)

            return f'{animal_name} registered in the  clinic'

        return 'Not enough space'

    def unregister_animal(self, animal_name):
        if animal_name in Vet.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)

            return f'{animal_name} unregistered successfully'

        return f'{animal_name} not in the clinic'

    def info(self):
        return f'{self.name} has {len(self.animals)} animals. ' \
            f'{Vet.space - len(Vet.animals)} space left in clinic'


peter = Vet("Peter")
george = Vet("George")

print(peter.register_animal("Tom"))  # Tom registered in the  clinic
print(george.register_animal("Cory"))  # Cory registered in the  clinic
print(peter.register_animal("Fishy"))  # Fishy registered in the  clinic
print(peter.register_animal("Bobby"))  # Bobby registered in the  clinic
print(george.register_animal("Kay"))  # Kay registered in the  clinic
print(george.unregister_animal("Cory"))  # Cory unregistered successfully
print(peter.register_animal("Silky"))  # Silky registered in the  clinic
print(peter.unregister_animal("Molly"))  # Molly not in the clinic
print(peter.unregister_animal("Tom"))  # Tom unregistered successfully
print(peter.info())  # Peter has 3 animals.1 space left in clinic
print(george.info())  # George has 1 animals.1 space left in clinic