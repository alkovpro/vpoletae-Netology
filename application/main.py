from people import People
from salary import Salary

def key_func():
      employees_list = People.get_employees()
      salary = Salary.calculate_salary()

      print(employees_list)
      print(salary)

if __name__=='__main__':
      key_func()
