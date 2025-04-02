#from taskManagerv1 import *
#from taskManagerv2 import *
from taskManagerv3 import *
from fileTaskManager import *


# Creating an instance of TaskManager
#manager = TaskManager("My Task Manager")
manager = FileTaskManager("My Task Manager")

# Accessing the attributes initialized by __init__
print(manager.name)  # Output: My Task Manager
print(manager.tasks)  #

#Encapsulation
print("Encapsulation")
manager.add_task("Write documentation")
manager.add_task("Implement feature X")
print(manager.list_tasks())
manager.remove_task("Write documentation")
print(manager.list_tasks())
manager.clear_all_tasks()
print(manager.list_tasks())

#Abstraction
print("Encapsulation")
manager.add_task("Write documentation")
manager.add_task("Implement feature X")
print(manager.list_tasks())
manager.complete_task("Write documentation")
print(manager.list_tasks())

#inheritance
manager.save_to_file()
print("Tasks saved. Goodbye!")
#manager.load_from_file()  # Load tasks from file (if it exists)


