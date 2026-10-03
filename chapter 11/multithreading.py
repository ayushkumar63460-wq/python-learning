'''Multithreading: Used to perform multiple tasks concurrently (multitasking) 
                   Good for I/0 bound tasks like reading files or fetching data from APIs
                   threading. Thread(target=my_function) '''


import threading
import time


def walk_dog(first, last):
    time.sleep(8)
    print(f"you finished walking {first} {last}.")

def takeout_trash():
    time.sleep(2)
    print("you take out the trash.")

def wash_dish():
    time.sleep(5)
    print("you washed the dishes.")


chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=takeout_trash)
chore2.start()

chore3 = threading.Thread(target=wash_dish)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All your chores has been completed!")