class User():
    def __init__(self, first_name, last_name, address, phone_number, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.sex = sex
    
    def describe_user(self):
        print("\nUser  fullname is "+(self.first_name + ' '+ self.last_name).title())
        print("User address is "+ self.address)
        print("User phone number is "+ self.phone_number)
        print("User is "+ self.sex)
    
    def greet_user(self):
        print("\nHello "+(self.first_name + ' '+ self.last_name).title())

user1 = User('sud','kasir','JC','012','Male')
user2 = User('Pra','kasir','JC','552','Female')
user3 = User('Bhav','kasir','JC','987','F')
user4 = User('Div','kasir','JC','665','F')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
user4.describe_user()
user4.greet_user()
