class food_items:
    def __init__(self, recipe, ingredients, time) -> None:
        self.recipe = recipe
        self.ingredients = ingredients
        self.time = time

    def server(self):
        print("The " + self.recipe + " has " + str(self.ingredients) + " and will take " + str(self.time) + " min to prepare")

ig = food_items("Pizza", ["papparoni", "Cheese", "Chickedn"], 45)
ig.server()