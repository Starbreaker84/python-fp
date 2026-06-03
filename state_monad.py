from dataclasses import dataclass
from pymonad.state import State
from pymonad.tools import curry


@dataclass
class Coffee:
    price: int = 0
    calories: int = 0

@dataclass
class Ingredient:
    price: int = 0
    calories: int = 0

ingredients = {
    'espresso': Ingredient(60, 30),
    'milk': Ingredient(40, 50),
    'vanilla': Ingredient(30, 10),
    'caramel': Ingredient(10, 20),
}

coffee_init = {'ingredients': [], 'coffee': Coffee(0, 0)}

new_order = State.insert(coffee_init['ingredients'])

@curry(2)
def add_ingredient(ingredient_name: str, order_ingredients: list[str]):
    def transition(coffee: Coffee):
        ingredient = ingredients[ingredient_name]
        new_coffee = Coffee(
                price = coffee.price + ingredient.price,
                calories = coffee.calories + ingredient.calories
        )
        return order_ingredients + [ingredient_name], new_coffee
    return State(transition)

def main():
    order = (
        new_order
            .then(add_ingredient('espresso'))
            .then(add_ingredient('milk'))
            .then(add_ingredient('vanilla'))
            .then(add_ingredient('caramel'))
    )

    result = order.run(coffee_init['coffee'])

    print(result)
    
if __name__ == "__main__":
    main()