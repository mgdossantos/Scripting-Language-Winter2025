#step 1: create an empty list named beatles;
#beatles=[]
beatles = list()
#step 2: use the append() method to add the following
# members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
beatles.append('John Lennon')
beatles.append(' Paul McCartney')
beatles.append('George Harrison')

for i in beatles:
    print (i)
#step 3: use the for loop and the append() method to
# prompt the user to add the following members of
# the band to the list: Stu Sutcliffe, and Pete Best;
answer= input("Do you want to add Stu Sutcliffe in the band?")
if answer.lower()=="yes":
    beatles.append("Stu Sutcliffe")

answer = input("Do you want to add Pete Best in the band?")
if answer.lower() == "yes":
    beatles.append("Pete Best")
for i in beatles:
    print (i)
#step 4: use the del instruction to remove
# Stu Sutcliffe and Pete Best from the list;
beatles.remove("Stu Sutcliffe")
beatles.remove("Pete Best")
for i in beatles:
    print (i)
#step 5: use the insert() method to add Ringo Starr
# to the beginning of the list.
beatles.insert(0,"Ringo Starr")

for i in beatles:
    print (i)

