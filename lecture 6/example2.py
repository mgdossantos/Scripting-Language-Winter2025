# data = list()
# data.append('Marcela')
# data.append(41)
# #
# print(data)
# print(data[0])
# print(data[-1])
# #
# people = list()
# people.append(data[:])
# print(people)
# #
# print(people[0])
# print(people[0][0])
# #
# # people.append(['Bruna',35])
# # print(people)
# #
# # print(people[1][0])
# # print(people[1])
#
data= list()
people= list()
for i in range(3):
    data.append(input('Name: '))
    data.append(int(input('Age: ')))
    people.append(data[:])
    data.clear()

for l in range(len(people)):
    for c in range(2):
        print('[', people[l][c],']')
    print()








#
#
#
#
#
#







