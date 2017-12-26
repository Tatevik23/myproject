#!/usr/bin/python3
import random
import os.path
import argparse
import logging
logging.basicConfig(filemode="w", 
                    filename="test.log",
                    level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s"
                   )
parser = argparse.ArgumentParser()
parser.add_argument('maxSize', help="maximum list size", type=int)
args = parser.parse_args()

class Stack():

# List definition inside constructor
    def __init__(self):
        self.stack = []
        self.maximum_size = args.maxSize

# Stack real size(with elements)
    def real_size(self):
        logging.debug("Stack size: {} ".format(len(self.stack)))
        return len(self.stack)

# Stack full size
    def capacity(self):
        logging.debug("Capacity: {}".format(self.maximum_size))
        return self.maximum_size

# Add elements to the stack
    def push(self,data):
        if self.isFull():
            return 
        self.stack.append(data)
        logging.info("Adding: {}".format(data))

# Remove elements from the stack
    def pop(self):
        if self.isEmpty():
            return
        top_element = self.stack[len(self.stack)-1]
        self.stack.pop()
        logging.info("Removing: {}".format(top_element))

# Top element of the stack
    def top(self):
        logging.debug("Top element: {}".format(self.stack[len(self.stack)-1]))
        return self.stack[len(self.stack)-1]

# Check whether stack is empty or not
    def isEmpty(self):
        if len(self.stack) == 0:
            logging.debug("Empty: True")
            return True 
        else:
            return False 
 
# Check whether stack is full or not        
    def isFull(self):
        if len(self.stack) == self.maximum_size:
            logging.debug("Full: True")
            return True
        else:
            return False
            
def main():
    instance = Stack()
    file = open('golden', 'w')   
    if os.path.isfile('file'):
        file2 = open('newfile', 'w')
        print("Heloooooo")
    instance.pop()
    if (instance.isEmpty()):
        file.write("Stack is empty\n")
    file.write("Removing top element\n")

    for number in random.sample(range(1,10),5):
        instance.push(number)
    if (instance.isFull()):
        file.write("Stack is full\n")

    instance.top()
    file.write("Calling top element\n")

    instance.pop()
    if (instance.isEmpty()):
        file.write("Stack is empty\n")
    file.write("Removing top element\n")

    instance.capacity()
    capacity = str(instance.maximum_size)
    file.write("Stack size is: " + capacity + '\n')
    
    instance.top()
    file.write("Calling top element\n")

    instance.isEmpty()
    if (instance.isEmpty()):
        file.write("Stack is empty\n")

    instance.pop()
    if (instance.isEmpty()):
       file.write("Stack is empty" + '\n')
    file.write("Removing top element" + '\n')

    instance.top()
    file.write("Calling top element\n")

    instance.push(30)
    file.write("Adding element\n")

    instance.top()
    file.write("Calling top element\n")

    instance.real_size()
    
    #compareWithGolden()
main()
