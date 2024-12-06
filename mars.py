import matplotlib.pyplot as plt

student_names = ["Aditya", "Masha", "Sadman", "Naihan", "Haaland", "SuiiRonaldo", "De Meao", "Farhan"]
student_marks = [35,50,20,45,25,40,25,40]

marks_perc = []

for x in student_marks:
    res = (x/50) * 100
    marks_perc.append(res)
    
print(marks_perc)

def line_chart_of_students_and_marks():
    plt.plot(student_names, student_marks)
    plt.title("Student Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage")
    plt.show()

line_chart_of_students_and_marks()

def percentage_bar_chart():
    plt.bar(student_names, student_marks)
    plt.title("Students Percentage Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Students Percentage")
    plt.show()

percentage_bar_chart()