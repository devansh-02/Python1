noOfStudents = int(input("Enter the number of students: "))     # no of students

marksDict = {}                      # student name as key and marks as value

nameList = []                       # list to store student name
markList = []                       # list to store student mark

for i in range(0, noOfStudents):
    print("\nEnter the name of the Student no.", i + 1, ":")
    name = input()
    nameList.append(name)

    print("Enter the marks", name, "has gotten:")
    mark = int(input())
    markList.append(mark)

    marksDict[name] = mark          # adding name and mark in dictionary

print("\nPrinting all the students marks :-\n", marksDict)                    # printing marks dictionary

markList.sort()
markList.reverse()

j = 1

print("\nRank of all the students without any updatation :-")
for i in markList:
    print("Rank", j, "is: ", list(marksDict.keys())[list(marksDict.values()).index(i)])
    j = j + 1


while(1):
    print('\nType :-\n1. Update the marks\n2. Exit the updatation program:')
    userWant = input()
    if userWant == "1":
        print("Whose marks you want to update? Enter Student's name:")
        updateName = input()
        if updateName in nameList:
            print("Enter the marks: ")
            updateMarks = int(input())

            marksDict[updateName] = int(marksDict[updateName] + updateMarks)
        else:
            print("\nEntered name is invalid!\nSelect again...\n")

    elif userWant == "2":
        print("\nYou exit the updation program.")
        break
    
    else:
        print("Please enter a valid input.\nTry again...\n")

markNew = list(marksDict.values())

print("\nStudent's name list:", nameList)
print("Student's marks list:", markList)
print("Student's marks after updatation program:", markNew)

print("\nPrinting all the students marks after updatation:\n ", marksDict)

print("\nThe student who got the hightest marks is: ", list(marksDict.keys())[list(marksDict.values()).index(max(marksDict.values()))])

j = 1

markNew.sort()
markNew.reverse()

print("\nRank of all the students after updatation program :-")

for i in markNew:
    print("Rank", j, "is: ", list(marksDict.keys())[list(marksDict.values()).index(i)])
    j = j + 1

