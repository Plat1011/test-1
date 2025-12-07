class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""
        self.cheese = ""

    def __str__(self):
        return f"Пицца: тесто={self.dough}, соус={self.sauce}, начинка={self.topping}, сыр={self.cheese}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_dough(self, dough_type):
        self.pizza.dough = dough_type
        return self

    def add_sauce(self, sauce_type):
        self.pizza.sauce = sauce_type
        return self

    def add_topping(self, topping_type):
        self.pizza.topping = topping_type
        return self

    def add_cheese(self, cheese_type):
        self.pizza.cheese = cheese_type
        return self

    def get_pizza(self):
        return self.pizza


class PizzaCook:
    def make_margherita(self):
        return (PizzaBuilder()
                .add_dough("тонкое")
                .add_sauce("томатный")
                .add_topping("помидоры")
                .add_cheese("моцарелла")
                .get_pizza())

    def make_pepperoni(self):
        return (PizzaBuilder()
                .add_dough("толстое")
                .add_sauce("томатный")
                .add_topping("пепперони")
                .add_cheese("чеддер")
                .get_pizza())
builder = PizzaBuilder()
custom_pizza = (builder
                .add_dough("среднее")
                .add_sauce("сливочный")
                .add_topping("грибы")
                .add_cheese("пармезан")
                .get_pizza())
print(custom_pizza)

cook = PizzaCook()
margherita = cook.make_margherita()
pepperoni = cook.make_pepperoni()
print(f"Маргарита: {margherita}")
print(f"Пепперони: {pepperoni}")