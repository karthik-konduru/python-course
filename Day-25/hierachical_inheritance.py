class Company:
    def Rules(self):
        print('Follow the company rules')
class HR_team(Company):
    def Hiring(self):
        print('Hiring the Employees')
class frontend_team(Company):
    def Design(self):
        print('Designing the Website')
class Backend_Team(Company):
    def python_operations(self):
        print('Writing python code to develop the company')
hr=HR_team()
f=frontend_team()
b=Backend_Team()
hr.Rules()
hr.Hiring()
print()
f.Rules()
f.Design()
print()
b.Rules()
b.python_operations()