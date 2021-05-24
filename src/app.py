import os
import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")

# lambda function to clear the screen
cls = lambda: os.system('cls')

def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add(element):
    queue.enqueue(element)

def dequeue():
    if queue.size() == 0: 
        return None

    return queue.dequeue()

def save():
    queueAsObj = queue.get_queue()
    with open("queue.json", 'w') as jsonFile:
        json.dump(queueAsObj, jsonFile, indent=4)

def load():
    infoAsPython = None
    with open("queue.json", 'r') as jsonFile:
        try:
            infoAsPython = json.load(jsonFile)
        except:
            infoAsPython = []

    for element in infoAsPython:
        queue.enqueue(element)
    

cls()
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = None
    try:
        option = int(input("Enter a number: "))
    except:
        #Doing nothing because the cls of the else 
        pass
    # add your options here using conditionals (if)
    if option == 1:
        cls()
        newPerson = input("Enter name and cellphone separated by comma:\n")
        try:
            info = [x.strip() for x in newPerson.split(',')]
            info = [info[0], info[1]]
            add(info)
        except:
            print('Invalid information')

    elif option == 2:
        cls()
        removedPerson = dequeue()
        if removedPerson == None: 
            print("The list is empty")
            continue
        print("Removing the first person")
        print(removedPerson[0], removedPerson[1])
        send(removedPerson[0]+" was removed from the queue", removedPerson[1])

    elif option == 3:
        cls()
        print_queue()
    
    elif option == 4:
        cls()
        save()

    elif option == 5:
        cls()
        load()

    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        cls()
        print("Not implemented yet or invalid option "+str(option))
