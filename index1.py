class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}
    def add_scores(self, course, score):
        self.scores[course] = score
        print(f"Added {score} for {course}")

    def average(self):
        if not self.scores:
            print('No scores to calcualte')
            return 0
        else:
            return sum(self.scores.values()) / len(self.scores)
        
    def grade(self):
        avg = self.average()

        if avg >= 70:
            return 'A'
        elif avg >= 60:
            return 'B'
        elif avg  >= 50:
            return 'C'
        elif avg >= 45:
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
            course = input('ENter course name:')
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

    else:
        print("Invalid choice. Try again.")