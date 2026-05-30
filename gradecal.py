# ============================================
#   STUDENT GRADE CALCULATOR
# ============================================

name = input("Enter the student name: ")

marks1 = int(input("English marks: "))
marks2 = int(input("Hindi marks: "))
marks3 = int(input("Mathematic marks: "))
marks4 = int(input("Science marks: "))
marks5 = int(input("Social Studies marks: "))
marks6 = int(input("Computer marks: "))

total = marks1 + marks2 + marks3 + marks4 + marks5 + marks6
average = total / 6

if average >= 90:
    grade = "A+"
    remark = "Outstanding!"
elif average >= 80:
    grade = "A"
    remark = "Excellent!"
elif average >= 70:
    grade = "B"
    remark = "Very Good!"
elif average >= 60:
    grade = "C"
    remark = "Good"
elif average >= 50:
    grade = "D"
    remark = "Average - aur mehnat karo"
else:
    grade = "F"
    remark = "Fail - dobara try karo"

print ("-----------------------------")
print("          RESULT CARD         ")
print ("-----------------------------")
print(f"NAME : {name}")
print(f"TOTAL MARKS : {total} / 600 ")
print(f"PERCENTAGE : {average:.2f}%")
print(f"GRADE : {grade}")
print ("-----------------------------")