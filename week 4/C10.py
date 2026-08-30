items = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 120,
    "Pencil": 5,
    "Bottle": 80
}

highest_item = max(items, key=items.get)
lowest_item = min(items, key=items.get)

print("Item with highest price:", highest_item, "=", items[highest_item])
print("Item with lowest price:", lowest_item, "=", items[lowest_item])
