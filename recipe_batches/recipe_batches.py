#!/usr/bin/python

import math

'''
Your function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary.

Look at ingredients on hand
Compare available amount of ingredients to recipe
how many times will recipe amount go into available ingredients
return the amount of times

def rec_batches(rec, ing):
    loop through ingredients on hand and recipe at same time comparing values
    keep track of how many times avail ingreds value goes into recipe value
    what is the largest number that EACH ingredient can go into rec

    ie milk 1288 // 100 = 12 but butter 0 // 5 = 0 so no batches can be made
'''

rec = {'milk': 2}
ingreds = {'milk': 200}


# for key, value in rec.items():
#     print(f"{key}: {value}")

# for key, value in ingreds.items():
#     print(f"{key}: {value}")


def recipe_batches(recipe, ingredients):
    if len(ingredients) < len(recipe):
        return 0
    else:
        for key in recipe and ingredients:
            return min([ingredients[key] // recipe[key]])


print(recipe_batches(rec, ingreds))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
