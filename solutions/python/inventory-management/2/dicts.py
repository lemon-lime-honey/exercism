"""Functions to keep track and alter inventory."""


def create_inventory(items):
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    return inventory

def add_items(inventory, items):
    pre_inventory = create_inventory(items)
    for key, value in inventory.items():
        if key in pre_inventory:
            pre_inventory[key] += value
        else:
            pre_inventory.setdefault(key, value)
    return pre_inventory

def decrement_items(inventory, items):
    temp = create_inventory(items)
    for key, value in temp.items():
        if key in inventory:
            if inventory[key] > value:
                inventory[key] -= value
            else:
                inventory[key] = 0
    return inventory

def remove_item(inventory, item):
    inventory.pop(item, 0)
    return inventory

def list_inventory(inventory):
    output = []
    for key, value in inventory.items():
        if value > 0:
            output.append((key, value))
    return output
