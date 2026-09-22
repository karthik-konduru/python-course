class Employee:
    def work(self):
        print('Working')
class Developer(Employee):
    def develop(self):
        print('Developing the website')
class tester(Developer):
    def Testing(self):
        print('Testing the Website')
t=tester()
t.work()
t.develop()
t.Testing()