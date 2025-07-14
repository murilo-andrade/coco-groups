from labels import get_label # Only if you need class names


def is_person(cls_id):
    if cls_id == 0:
        return True
    else:
        return False

def is_vehicle(cls_id):
    vehicles = [1, 2, 3, 4, 5, 6, 7, 8]
    if cls_id in vehicles:
        return True
    else:
        return False

def is_pet(cls_id):
    pets = [14, 15, 16]
    if cls_id in pets:
        return True
    else:
        return False

def is_wild_animal(cls_id):
    wild_animals = [20, 21, 22, 23]
    if cls_id in wild_animals:
        return True
    else:
        return False

def is_farm_animal(cls_id):
    farm_animals = [17, 18, 19]
    if cls_id in farm_animals:
        return True
    else:
        return False

def is_fruit(cls_id):
    fruits = [46, 47, 49]
    if cls_id in fruits:
        return True
    else:
        return False

def is_vegetable(cls_id):
    vegetables = [50, 51]
    if cls_id in vegetables:
        return True
    else:
        return False

def is_furniture(cls_id):
    furnitures = [56, 57, 59, 60]
    if cls_id in furnitures:
        return True
    else:
        return False

def is_electronic(cls_id):
    electronics = [62, 63, 64, 65, 66, 67]
    if cls_id in electronics:
        return True
    else:
        return False

def is_sportsgear(cls_id):
    sportsgears = [29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
    if cls_id in sportsgears:
        return True
    else:
        return False

def is_food(cls_id):
    foods = [46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
    if cls_id in foods:
        return True
    else:
        return False

def is_animal(cls_id):
    animals = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    if cls_id in animals:
        return True
    else:
        return False


if __name__ == "__main__":
    # Just a test
    cls = int(3)
    if is_vehicle(cls):
        print(f"{get_label(cls)} is a vehicle")
    else:
        print(f"{get_label(cls)} is not a vehicle")


