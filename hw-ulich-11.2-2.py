from abc import ABC, abstractmethod

# Абстрактная фабрика
class PastaFactory(ABC):
    @abstractmethod
    def create_pasta(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_filling(self):
        pass

    @abstractmethod
    def create_toppings(self):
        pass

# Конкретные фабрики
class SpaghettiFactory(PastaFactory):
    def create_pasta(self):
        return Spaghetti()

    def create_sauce(self):
        return TomatoSauce()

    def create_filling(self):
        return None

    def create_toppings(self):
        return [Parmesan(), Basil()]

class RavioliFactory(PastaFactory):
    def create_pasta(self):
        return Ravioli()

    def create_sauce(self):
        return PestoCream()

    def create_filling(self):
        return RicottaFilling()

    def create_toppings(self):
        return [Parmesan(), Spinach()]

class Pasta(ABC):
    @abstractmethod
    def type(self):
        pass

class Sauce(ABC):
    @abstractmethod
    def name(self):
        pass

class Filling(ABC):
    @abstractmethod
    def name(self):
        pass

class Topping(ABC):
    @abstractmethod
    def name(self):
        pass

class Spaghetti(Pasta):
    def type(self):
        return "Spaghetti"

class Ravioli(Pasta):
    def type(self):
        return "Ravioli"

class TomatoSauce(Sauce):
    def name(self):
        return "Tomato Sauce"

class PestoCream(Sauce):
    def name(self):
        return "Pesto Cream"

class RicottaFilling(Filling):
    def name(self):
        return "Ricotta Filling"

class Parmesan(Topping):
    def name(self):
        return "Parmesan"

class Basil(Topping):
    def name(self):
        return "Basil"

class Spinach(Topping):
    def name(self):
        return "Spinach"

# проверка
def make_pasta(pasta_factory):
    pasta = pasta_factory.create_pasta()
    sauce = pasta_factory.create_sauce()
    filling = pasta_factory.create_filling()
    toppings = pasta_factory.create_toppings()

    print(f"You ordered {pasta.type()} with {sauce.name()}")
    if filling:
        print(f"Filled with {filling.name()}")
    print("Topped with:")
    for topping in toppings:
        print(f"- {topping.name()}")

if __name__ == "__main__":
    spaghetti_factory = SpaghettiFactory()
    make_pasta(spaghetti_factory)

    print()

    ravioli_factory = RavioliFactory()
    make_pasta(ravioli_factory)


# Я использовал паттерн "Абстрактная фабрика", потому что он позволяет создавать семейства взаимосвязанных
# объектов (пасту, соус, начинку, добавки) без привязки к конкретным классам. Это дает гибкость и расширяемость,
# так как мы можем легко добавлять новые виды пасты, соусов, начинок и добавок, не меняя существующий код.
