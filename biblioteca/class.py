class student:
    def __init__(self,name):
        self.name = name
        self.attend = 0
        self.grades = []
        print("Hi!My nema is {0}".format(self.name))
    def addGrade(self,grade):
        self.grades.append(grade)
    def attendDay(self):
        self.attend +=1
    def getAverage (self):
        return sum(self.grades)/len(self.grades)

##>>> student1 = student("Carol")
##Hi!My nema is Carol
##>>> student1.attendDay()
##>>> student1.attend
##1
##>>> for x in range(1,11):
##        student1.attendDay()      
##>>> student1.attend
##11
##>>> for x in range (1,11):
##        student1.addGrade(x)
##>>> student1.grades
## [1,2,3,4,5,..,10]
