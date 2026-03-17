


class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


class Manager(Employee):
    def work(self):
        print("Manager is managing the team")



emp_instance = Employee()
dev_instance = Developer()
man_instance = Manager()


emp_instance.work()
dev_instance.work()
man_instance.work()