from labels import get_label # Only if you need class names


def is_vehicle(cls_id):
    vehicles = [1, 2, 3, 5, 7]
    if cls_id in vehicles:
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


