def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, soldpets):
    pet_shop["admin"]["pets_sold"] += soldpets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    breed_no = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            breed_no.append(pet)
    return breed_no

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer_index):
    return customer_index["cash"]

def remove_customer_cash(customer_index, cash):
    customer_index["cash"] -= cash

def get_customer_pet_count(customer_index):
    return len(customer_index["pets"])

def add_pet_to_customer(customer_index, new_pet):
    customer_index["pets"].append(new_pet)

def customer_can_afford_pet(customer_index, new_pet):
    if customer_index["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop, pet, customer_index):
    if pet in pet_shop["pets"] and customer_can_afford_pet(customer_index, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        remove_customer_cash(customer_index, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)
        add_pet_to_customer(customer_index, pet)

