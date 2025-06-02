# with no type annotation : no editor support
def get_full_name_no_type(first_name, last_name):
    full_name = first_name.title()+" " + last_name.title()
    return full_name

print(get_full_name_no_type("Swata Swayam", "Dash"))

# with type annotation : editor support
def get_full_name_with_type(first_name: str, last_name: str):
    full_name = first_name.title()+" "+last_name.title()
    return full_name

print(get_full_name_with_type("Swata Swayam", "Dash"))

def get_name_with_age(name: str, age: int):
    name_with_age = name + " "+str(age)
    return name_with_age

print(get_name_with_age("Paplu", 21))


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e

def process_items_i(items: list[str]):
    for item in items:
        print(item)

def process_items_ii(items_t: tuple[int , int, str], items_s: set[bytes]):
    return items_t, items_s

def process_items_iii(prices: dict[str, float]):
    for item_name , item_price in prices.items():
        print(item_name)
        print(item_price)

def process_items_iv(item: int | str):
    print(item)


from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}")
    else:
        print("Hello World")

def say_hi_ii(name: str | None = None):
    if name is not None:
        print(f"Hey {name}")
    else:
        print("Hello World")