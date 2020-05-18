class Employee:
    def setNumberOfWorkingHours(self):
        self.NumberOfWorkingHours = 40

    def displayNumberOfWorkingHours(self):
        print(self.NumberOfWorkingHours)

class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.NumberOfWorkingHours = 45

    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

employee= Employee()
employee.setNumberOfWorkingHours()
print("number of working hours: ", end = ' ')
employee.displayNumberOfWorkingHours()

trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("number of working hours: ", end = ' ')
trainee.displayNumberOfWorkingHours()
trainee.resetNumberOfWorkingHours()
print("number of working hours: ", end = ' ')
trainee.displayNumberOfWorkingHours()