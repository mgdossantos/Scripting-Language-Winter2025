# Scenario: You are organizing a conference where each
# participant's information (name, age, and profession)
# must remain unchanged once registered.
#
# Task:
#
# In pairs, define a tuple structure to store a participant's
# information.
# Write a function that accepts a participant's details and
# returns a tuple.
# Print all participant details in a structured format.
#

def register_participant (name, age,profession):
    return (name, age, profession)

def showInfo(participant):
    print("Name: " + participant[0])
    print("Age: " + str(participant[1]))
    print("Profession: " + participant[2])


name = input("Name: ")
age = int(input("Age: "))
profession = input("Profession: ")

participant1=register_participant(name,age,profession)
showInfo(participant1)