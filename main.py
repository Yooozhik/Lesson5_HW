class MedicalPlants:
    biology_class = 'Plant'

    def __init__(self, _name, medical_part, gather_time):
        self._name = _name
        self.medical_part = medical_part
        self.gather_time = gather_time

    def get_name(self):
        return f'It is {self._name}'

    def get_medical_part(self):
        return f'{self._name} has {self.medical_part} as a medical part'

    def get_recomendation(self):
        return f'{self._name} should be used carefully'

    def set_name(self, new_name):
        self._name = new_name

plant1 = MedicalPlants('Oak', 'bark', 'autumn')
print(plant1._name)
print(plant1.get_medical_part())
print(plant1.get_recomendation())
print(plant1.biology_class)
plant1.gather_time = 'summer'
print(plant1.gather_time)
print(plant1.__dict__)
print(plant1.set_name('aspen'))
print(plant1.get_name())
print()

class MedicalHerbs(MedicalPlants):
    biology_class = 'Herb'

    def __init__(self, _name, medical_part, gather_time, recipe):
        super().__init__(_name, medical_part, gather_time)
        self.recipe = recipe

    def get_disease_name(self):
        return f'You can select your disease from the applied list'

    def get_recomendation(self):
        return f'{self._name} should be gathered only in {self.gather_time}'

    def get_recipe(self):
        return f'You should go to the doctor for {self.recipe}'

herb1 = MedicalHerbs('Chamomile', 'flowers', 'summer', 'resipe1')
print(herb1._name)
print(herb1.get_medical_part())
print(herb1.get_recomendation())
print(herb1.biology_class)
print(herb1.get_disease_name())
print(herb1.__dict__)
print(herb1.get_recipe())
print()

herb2 = MedicalHerbs('Dandelion', 'roots', 'spring', 'resipe2')
print(herb2._name)
print(herb2.get_medical_part())
print(herb2.get_recomendation())
print(herb2.biology_class)
print()

herb3 = MedicalHerbs('Nettle', 'leaves', 'spring', 'resipe3')
print(herb3._name)
print(herb3.get_medical_part())
print(herb3.get_recomendation())
print(herb3.biology_class)
