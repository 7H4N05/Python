class student_marks:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg_marks(self):
        sum=0
        for val in self.marks:
                sum+=val
        # print("Your avg score is:",sum/len(self.marks))  
        print("Your avg score is:",sum/6)        
      


s1 = student_marks("Tanush Bamnote",[94,91,94,94,76,84])
s1.avg_marks()