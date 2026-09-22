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
class clients(HR_team,Backend_Team,Company): # Multiple Inheritance
    def meetups(self):
        print('client meetings')
client=clients()
client.meetups()
client.python_operations()
client.Hiring()
client.Rules()
