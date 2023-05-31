

class Customer:
    fname = "Erik"
    lname = "Smith"
    email = "eriksmith@gmail.com"
    customer_id = "11256"

    def loginInfo(self):
        entry_fname = input("Enter your name: ")
        entry_lname = input("Enter your last name: ")
        entry_email = input("Enter your customer email: ")
        entry_customer_id = input("Enter your customer id: ")
        if (entry_email == self.email and entry_customer_id == self.customer_id):
            print("Welcome back, {}!".format(entry_fname))
        else:
            print("Your customer ID is incorrect. ")

#child class employee
class Employee(Customer):
    fname = "Bob"
    email2 = "bob@gmail.com"
    salary = 16
    department = "IT"
    password = "7728"

    def loginInfo(self):
        entry_fname = input("Enter your fname: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email2 and entry_password == self.password):
            print("Welcome back, {}!".format(entry_fname))
        else:
            print("your password is incorrect")

#another child class
class Supplier(Customer):
    fname = "Sally"
    supplier_pin = "3345"
    price = 67
    address = "123 lane drive"
    email = "sally@gmail.com"

    def loginInfo(self):
        entry_fname = input("Enter your fname: ")
        entry_supplier_pin = input("Enter your pin: ")
        if (entry_fname == self.fname and entry_supplier_pin == self.supplier_pin):
            print("Welcome back, {}!".format(entry_fname))
        else:
            print("your pin is incorrect")

customer = Customer()
customer.loginInfo()
employee = Employee()
employee.loginInfo()
supplier = Supplier()
supplier.loginInfo()
    

        
    
