

class GradeCutoffs:
    # takes in percentages for each letter grade
    def __init__(self, A=90, B=80, C=70, D=60):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def get_letter(self, percentage):
        if (percentage >= self.A):
            return 'A'
        elif (percentage >= self.B):
            return 'B'
        elif (percentage >= self.C):
            return 'C'
        elif (percentage >= self.D):
            return 'D'
        else:
            return 'F' 
        
class GradeWeights:
    def __init__(self, homework=None, quiz=None, midterm=None, final=None):
        self.homework = homework
        self.quiz = quiz
        self.midterm = midterm
        self.final = final
    


class Course:

    def __init__(self, course_code, grade_cutoffs, grade_weights):
        self.code = course_code
        self.cutoffs = grade_cutoffs
        self.weights = grade_weights

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

custom_cutoffs = GradeCutoffs()

def main():
    matrices_cutoffs = custom_cutoffs
    matrices_weights = GradeWeights()
    Matrices = Course(21241, matrices_cutoffs, matrices_weights)

    print(matrices_cutoffs.A)
    print(Matrices.code)

main()