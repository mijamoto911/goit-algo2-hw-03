import csv
import timeit
from BTrees.OOBTree import OOBTree


# Функція для завантаження даних із CSV
def load_data_from_csv(file_path):
    data = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["ID"] = int(row["ID"])
            row["Price"] = float(row["Price"])
            data.append(row)
    return data


# Функції для додавання товарів
def add_item_to_tree(tree, item):
    tree[item["ID"]] = item


def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item


# Функції для діапазонного запиту
def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item["Price"] <= max_price]


def range_query_dict(dictionary, min_price, max_price):
    return [
        item for item in dictionary.values() if min_price <= item["Price"] <= max_price
    ]


# Основний код
file_path = "generated_items_data.csv"
data = load_data_from_csv(file_path)

# Створення структур даних
oob_tree = OOBTree()
dictionary = {}

# Додавання даних у структури
for item in data:
    add_item_to_tree(oob_tree, item)
    add_item_to_dict(dictionary, item)

# Вимірювання продуктивності
min_price, max_price = 10.0, 50.0

# Вимірювання часу виконання діапазонного запиту для OOBTree
tree_time = timeit.timeit(
    lambda: range_query_tree(oob_tree, min_price, max_price), number=100
)

# Вимірювання часу виконання діапазонного запиту для dict
dict_time = timeit.timeit(
    lambda: range_query_dict(dictionary, min_price, max_price), number=100
)

# Вивід результатів
print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
print(f"Total range_query time for Dict: {dict_time:.6f} seconds")
