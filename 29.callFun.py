name = "Obama"
def showname():
    global name
    print ("Function 1:", name)
    name = "John"
    print ("Function 2:", name)
print ("Main program 1:", name)
showname()
print ("Main program 2:", name)