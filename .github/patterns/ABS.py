import abc


class FormalClothesFactory(abc.ABC):
    @abc.abstractmethod
    def create_shirt(self):
        pass

    @abc.abstractmethod
    def create_pants(self):
        pass


class CasualClothesFactory(abc.ABC):
    @abc.abstractmethod
    def create_shirt(self):
        pass

    @abc.abstractmethod
    def create_pants(self):
        pass


class FormalShirt:
    def wear(self):
        return "Надел рубашку с галстуком"


class FormalPants:
    def wear(self):
        return "Надел классические брюки"


class CasualShirt:
    def wear(self):
        return "Надел футболку"


class CasualPants:
    def wear(self):
        return "Надел джинсы"


class OfficeFormalFactory(FormalClothesFactory):
    def create_shirt(self):
        return FormalShirt()

    def create_pants(self):
        return FormalPants()


class StreetCasualFactory(CasualClothesFactory):
    def create_shirt(self):
        return CasualShirt()

    def create_pants(self):
        return CasualPants()


class Person:
    def __init__(self, formal_factory, casual_factory):
        self.formal_factory = formal_factory
        self.casual_factory = casual_factory

    def dress_formal(self):
        shirt = self.formal_factory.create_shirt()
        pants = self.formal_factory.create_pants()
        return f"Формальная одежда: {shirt.wear()}, {pants.wear()}"

    def dress_casual(self):
        shirt = self.casual_factory.create_shirt()
        pants = self.casual_factory.create_pants()
        return f"Повседневная одежда: {shirt.wear()}, {pants.wear()}"

office_factory = OfficeFormalFactory()
street_factory = StreetCasualFactory()

person = Person(office_factory, street_factory)

print(person.dress_formal())
print(person.dress_casual())