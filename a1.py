
Labs = int(input("Enter the number of labs completed: "))
if Labs > 6:
    Labs = 6
Lab_grade = ((Labs/6 * 0.20)*100)

Quizzes = int(input("Enter the number of quizzes completed: "))
if Quizzes > 6:
    Quizzes = 6
Quizzes_grade = ((Quizzes/6 * 0.15) * 100)

A_1 = float(input("Enter grade for Assigmnent 1: "))
A_2 = float(input("Enter grade for Assignment 2: "))
A_3 = float(input("Enter grade for Assigment 3: "))
A_4 = float(input("Enter grade for Assignment 4: "))

Assignment_grade = (( A_1 * 0.04)+(A_2 * 0.04)+(A_3 * 0.04)+(A_4 *0.04))


M_1 = float(input("Enter grade for Midterm 1: "))
M_2 = float(input("Enter grade for Midterm 2: "))

Midterm_grade = ((M_1 * 0.125) + (M_2 *0.125))


F_E = float(input("Enter grade for final Exam: "))
Final_Exam_Grade = (F_E * 0.18)


M_F_Prep = float(input("Enter grade for Midterms and Final Preperation: "))
Midterms_Final_Prep_Grade = (M_F_Prep * 0.06)

def grade_total(grades):
 grades =(Labs + Quizzes + Assignment_grade + Midterm_grade + Midterms_Final_Prep_Grade)

 

print("Your grade is: " + str(round((((Labs/6 * 0.20)*100))+(((Quizzes/6 * 0.15)*100)) + (((A_1 + A_2 + A_3 + A_4)*0.04)) + ((M_1 * 0.125) + (M_2 * 0.125)) + ((F_E * 0.18))  + ((M_F_Prep * 0.06))))) 

