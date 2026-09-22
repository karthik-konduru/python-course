class Company:
    def main_agenda(self):
        print('Abstract of Comapny')
    def clients(self):
        print('Clients')
    def CEO(self):
        print('I am the CEO')
class Cloud_Company(Company):
    def cloud(self):
        print('Company Data in the Cloud')
c=Cloud_Company()
c.main_agenda()
c.cloud()