time= list()
sum=0
for i in range(5):
    t = int(input("Timer: "))
    time.append(t)
    sum=sum+time[i]
average= sum/len(time)
print("Average: " +str(average))