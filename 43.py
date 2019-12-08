# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# def addToInventory(inventory, addedItems):
#      # your code goes here
#     inv = {'gold coin': 42, 'rope': 1}
#     dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#     inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v, k)
        item_total =item_total+ v
    print("Total number of items: " + str(item_total))

# def addToInventory(inventory, addedItems):
#     for i in range(len(addedItems)):
#         inventory.setdefault(addedItems[i],0)
#         inventory[addedItems[i]]=inventory[addedItems[i]]+1
#     return inventory

inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)