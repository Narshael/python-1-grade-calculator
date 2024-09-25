"""
TODO
    - remove the hello name
    - configure the course total: add the remaining numbers, inputs etc..

"""
course_total = 0
Labs_completed = int(input("Enter the number of labs completed"))
if Labs_completed > 6:
    Labs_completed = 6
lab_weight = 0.2

course_total += Labs_completed/6 *lab_weight
print(course_total)



