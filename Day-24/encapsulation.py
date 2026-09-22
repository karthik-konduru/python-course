class company:
    def __init__(self,emp_name,emp_id,emp_Salary):
        self.emp_name =emp_name
        self._emp_id = emp_id
        self.__emp_Salary =emp_Salary
    def emp_salary(self):
        return self.__emp_Salary
    def emp_details(self):
        print(f"employee name{self.emp_name}employee id{self._emp_id}")
employee1 =company("karthik",480,987654)
print(employee1.emp_name)
print(employee1._emp_id)
#print(employee1.__emp_Salary) if we print this error will occur.
employee1.emp_salary()
print(employee1.emp_salary())
