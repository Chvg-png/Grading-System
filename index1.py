class Student:
    thresholds = None
    def __init__(self, name):
        self.name = name
        self.scores = {}
    def add_scores(self, course, score):
        self.scores[course] = score
        print(f"Added {score} for {course}")

    @classmethod 
    def calculate_scores(cls, A_score, B_score, C_score, D_score):
        cls.thresholds = [A_score, B_score, C_score, D_score]

    def average(self):
        if not self.scores:
            print('No scores to calcualte')
            return 0
        else:
            return sum(self.scores.values()) / len(self.scores)
        
    def grade(self):
        avg = self.average()
        t = Student.thresholds
    
        if avg >= t[0]:
            return 'A'
        elif avg >= t[1]:
            return 'B'
        elif avg >= t[2]:
            return 'C'
        elif avg >= t[3]:
            return 'D'
        else:
            return 'F'
            
    def show_report(self):
        with open(f'{self.name}.txt', 'w') as file:
            file.write(f"Report for {self.name}\n")
            file.write("_________________\n")
            for coure, score in self.scores.items():
                file.write(f"{coure}: {score}\n")
            avg = self.average()
            grd = self.grade()
            file.write(f"\n Average score: {avg:.2f}\n")
            file.write(f"\n Grade: {grd}\n")
        print(f"Report saved to {self.name}.txt")



students = {}
while True:
    print("\n1: Add New Student")
    print("2: Add Course Score")
    print("3: Show Student Report")
    print("4: Show All Students")
    print("5: Exit")
    print("6: Enter grade thresholds")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        if name in students:
            print("Students already exsits")
        else:
            students[name]  = Student(name)
            print(name, 'added')
    elif choice == '2':
        name = input("Enter student name: ")
        if name in students:
            course = input('Enter course name:')  #Typo. Looks a bit unprofessional.
            score = float(input("Enter score: "))
            students[name].add_scores(course, score)
        else:
            print("Student not found.")

    elif choice == '3':
        name = input("Enter student name: ")
        if name in students:
            students[name].show_report()
        else:
            print("Student not found.")

    elif choice == '4':
        print("\nAll Students:")
        for student_name in students:
            print(f"- {student_name}")

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    elif choice == '6':
        grades = ['A','B','C','D']
        result = []
        for letter in grades:
            grade_avg = int(input("Enter the grade needed for an " + letter + ": "))
            result.append(grade_avg)
        Student.calculate_scores(result[0], result[1], result[2], result[3])
        print("Grade thresholds set for all students.")
            

    else:
        print("Invalid choice. Try again.")
