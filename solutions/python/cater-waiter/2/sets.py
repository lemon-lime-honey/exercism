"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    ingredients_set = set(dish_ingredients)
    return (dish_name, ingredients_set)

def check_drinks(drink_name, drink_ingredients):
    type = str()
    for item in drink_ingredients:
        if item in ALCOHOLS:
            type = 'Cocktail'
    if type == '':
        type = 'Mocktail'
    return drink_name + ' ' + type

def categorize_dish(dish_name, dish_ingredients):
    type = str()
    if dish_ingredients.issubset(VEGAN):
        type = 'VEGAN'
    elif dish_ingredients.issubset(VEGETARIAN):
        type = 'VEGETARIAN'
    elif dish_ingredients.issubset(PALEO):
        type = 'PALEO'
    elif dish_ingredients.issubset(KETO):
        type = 'KETO'
    elif dish_ingredients.issubset(OMNIVORE):
        type = 'OMNIVORE'
    return dish_name + ': ' + type

def tag_special_ingredients(dish):
    special = set()
    for item in dish[1]:
        if item in SPECIAL_INGREDIENTS:
            special.add(item)
    return (dish[0], special)

def compile_ingredients(dishes):
    compiled = set()
    for dish in dishes:
        compiled = compiled | dish
    return compiled

def separate_appetizers(dishes, appetizers):
    set_dish = set(dishes) - set(appetizers)
    return list(set_dish)

def singleton_ingredients(dishes, intersection):
    result = set()
    for item in dishes:
        result = (result | item) - intersection
    return result
