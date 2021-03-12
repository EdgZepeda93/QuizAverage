gradeList = []

i = 0
while i < 3:
  grade = float(input("Enter exam grade: "))
  if grade >= 0 and grade <= 100:
    # add to list
    gradeList.append(grade)
    # print("Grade list: " , gradeList)
  else:
    raise("Invalid input! Input must be within 0-100.")
  i += 1

# len() returns the number of items in list
length = len(gradeList)

# loop list adding each item into sum
sum = 0
j = 0
for j in range(length):
  sum += gradeList[j]

average = sum / length

j = 0
for j in range(length):
  print("Exam %d: %.2f "%(j + 1, gradeList[j]))

print("\nAverage grade: % .2f "%(average))

if average <= 100 and average >= 93:
  print("\nLetter grade: A")
elif average <= 92 and average >= 90:
  print("\nLetter grade: A-")
elif average <= 89 and average >= 87:
  print("\nLetter grade: B+")
elif average <= 86 and average >= 83 :
  print("\nLetter grade: B")
elif average <= 82 and average >= 80:
  print("\nLetter grade: B-")
elif average <= 79 and average >= 77:
  print("\nLetter grade: C+")
elif average <= 76 and average >= 73:
  print("\nLetter grade: C")
elif average <= 72 and average >= 70:
  print("\nLetter grade: C-")
elif average <= 69 and average >= 67:
  print("\nLetter grade: D+")
elif average <= 66 and average >= 60:
  print("\nLetter grade: D")
elif average <= 59:
  print("\nLetter grade: F")
