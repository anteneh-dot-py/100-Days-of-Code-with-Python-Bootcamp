# student_scores = [180, 124, 165]
# max=0
# for number in student_scores:
#     if max<number:
#         max=number
# print(max)

# accept from the user
score=input("Insert score, separate by comma").split(",")
print(score)
max=0
for number in score:
    number=int(number)
    if max<=number:
        max=number
print("The maximum number is ",max)