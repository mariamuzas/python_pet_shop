# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]


def get_total_cash(shop_cash):
    return shop_cash["admin"]["total_cash"]


def add_or_remove_cash(shop_cash, add_cash):
    shop_cash["admin"]["total_cash"] += add_cash


def add_or_remove_cash(shop_cash, remove_cash):
    shop_cash["admin"]["total_cash"] += remove_cash


def get_pets_sold(shop_cash):
    return shop_cash["admin"]["pets_sold"]


def increase_pets_sold(pet_sold, num_pets):
    pet_sold["admin"]["pets_sold"] += num_pets


def get_stock_count(store_pets):
    return len(store_pets["pets"])


