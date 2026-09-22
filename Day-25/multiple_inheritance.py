class Employee:
    def work(self):
        print('Working')
class Developer:
    def develop(self):
        print('Developing the website')
class tester(Employee,Developer):
    def Testing(self):
        print('Testing the Website')
t=tester()
t.work()
t.develop()
t.Testing()