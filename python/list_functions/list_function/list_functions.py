#!/usr/bin/env python3
class Error(Exception):
    pass
class DontMatchList(Error):
    pass
class OutOfList(Error):
    pass

# Initialize the list by giving length and elements(list lenght and elements custom definition)
def initList():
    listLenght = input("Enter list lenght please: ")
    while True:
        try:    
           elements = [int(x) for x in input("Type list values separated by space: ").split()]
           if len(elements) != int(listLenght):
               raise DontMatchList
           else:
               return elements
        except DontMatchList:      
             print("Typed elements count don't match to list lenght: Try again please")
       
# User sets the index based on which minimum element should be founded.
def enterIndexForList(listLenght):
    while True:
        try:
            index = int(input("Enter index: "))
            if index > int(listLenght):
                raise OutOfList
            else:
                return index
        except OutOfList:
            print("Typed index out of list")

# Loop over list specific elements to find minimum list value and set it all list elements. 
def mainFunc():
    items = initList();
    index = enterIndexForList(len(items));
    print(items, items[index], items[-index])
    minvalue = min(items[index], items[-index])
    #minvalue = items[index]
    #for i in items[index:-index]:
    #   if i < minvalue:
    #       minvalue = i
    for i in range(0, len(items)):
        items[i] = minvalue
    return items
          
        
listitem = mainFunc();
print(listitem)
