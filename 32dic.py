stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def display(inventory,num):
    # stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    # print("Inventory:")
    a = 0
    # for k, v in inventory.items():
    a = a + inventory.get(num)
        # a = a + inventory[num]
    return a
# displayInventory(stuff,'rope' )

print("Inventory:")
for i in stuff.keys():
    print(i,' has items', str(display(stuff,i)))

