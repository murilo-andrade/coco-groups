# coco-groups

A collection of python functions to group coco detection classes.

The basic idea is to create boolean functions to test if some detected item is part of a group of similar classes. A simple example, cars, motorcycles, and bicycles can be part of the "vehicles" group.

## Available Groups

The following functions are available to check if a class ID (`cls_id`) belongs to a specific group. Each function returns `True` or `False`.

*   `is_person(cls_id)`: Checks if the object is a person.
*   `is_vehicle(cls_id)`: Checks for vehicles (e.g., car, motorcycle, bus, train).
*   `is_animal(cls_id)`: A broad category that checks for any animal.
*   `is_pet(cls_id)`: Checks for common pets (e.g., bird, cat, dog).
*   `is_wild_animal(cls_id)`: Checks for wild animals (e.g., bear, zebra, giraffe).
*   `is_farm_animal(cls_id)`: Checks for farm animals (e.g., sheep, cow, horse).
*   `is_food(cls_id)`: Checks for food items (e.g., fruits, vegetables, pizza).
*   `is_fruit(cls_id)`: Checks for fruits (e.g., banana, apple, orange).
*   `is_vegetable(cls_id)`: Checks for vegetables (e.g., broccoli, carrot).
*   `is_furniture(cls_id)`: Checks for furniture (e.g., chair, couch, bed).
*   `is_electronic(cls_id)`: Checks for electronics (e.g., tv, laptop, phone).
*   `is_sportsgear(cls_id)`: Checks for sports equipment (e.g., sports ball, skis, baseball bat).

## Usage Example
```
from coco-groups import is_vehicle
from labels import get_label

if __name__ == "__main__":
    # Just a test
    cls = int(3)
    if is_vehicle(cls):
        print(f"{get_label(cls)} is a vehicle")
    else:
        print(f"{get_label(cls)} is not a vehicle")
```