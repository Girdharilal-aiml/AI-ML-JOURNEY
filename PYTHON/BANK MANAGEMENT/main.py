import json
import random
from pathlib import Path


class Bank:
    database = 'database.json'
    data = []

    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.load(fs)
        else:
            data = []
    except Exception as err:
        print(f"An exception occurred: {err}")
        data = []

    @staticmethod
    def Update():
        with open(Bank.database, 'w') as fs:
            json.dump(Bank.data, fs)

    def CreateAccount(self):
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "Email": input("Enter your email: "),
            "Pin": int(input("Enter your 4 number pin: ")),
            "Account Number": random.randint(1000000000, 9999999999),
            "Balance": 0
        }

        if info["age"] < 18 or len(str(info["Pin"])) != 4:
            print("Sorry you cannot create an account")
        else:
            print("Account created successfully")

            for i in info:
                print(f"{i} : {info[i]}")

            Bank.data.append(info)
            Bank.Update()

    def Deposit(self):
        accnumber = int(input("Enter your account number: "))
        pin = int(input("Enter your pin: "))

        userdata = [
            i for i in Bank.data
            if i["Account Number"] == accnumber and i["Pin"] == pin
        ]

        if not userdata:
            print("Account not found")
        else:
            amount = int(input("Enter the amount to deposit: "))

            if amount > 10000 or amount < 0:
                print("You cannot deposit more than 10000 at a time")
            else:
                userdata[0]["Balance"] += amount
                Bank.Update()
                print("Deposit successful")

    def Withdraw(self):
        accnumber = int(input("Enter your account number: "))
        pin = int(input("Enter your pin: "))

        userdata = [
            i for i in Bank.data
            if i["Account Number"] == accnumber and i["Pin"] == pin
        ]

        if not userdata:
            print("Account not found")
        else:
            amount = int(input("Enter the amount to withdraw: "))

            if userdata[0]["Balance"] < amount:
                print("You cannot withdraw more than your balance at a time")
            else:
                userdata[0]["Balance"] -= amount
                Bank.Update()
                print("Withdrawal successful")

    def Details(self):
        accnumber = int(input("Enter your account number: "))
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i["Account Number"] == accnumber and i["Pin"] == pin]

        print("Account Details")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    
    def UpdateDetails(self):
        accnumber = int(input("Enter your account number: "))
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i["Account Number"] == accnumber and i["Pin"] == pin]

        if userdata == False:
            print("Account not found")
        else:
            print("You cannot update your age, account number and balance")
            print("Fill the details you want to update and leave the rest blank")

            newdata = {
                "name": input("Enter your name: "),
                "Email": input("Enter your email: "),
                "Pin": input("Enter your 4 number pin: "),
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]["name"]
            if newdata["Email"] == "":
                newdata["Email"] = userdata[0]["Email"]
            if newdata["Pin"] == "":
                newdata["Pin"] = userdata[0]["Pin"]

            newdata['age'] = userdata[0]['age']
            newdata['Account Number'] = userdata[0]['Account Number']
            newdata['Balance'] = userdata[0]['Balance']

            if type(newdata['Pin']) == str:
                newdata['Pin'] = int(newdata['Pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.Update()
            print("Details updated successfully")

    def DeleteAccount(self):
        accnumber = int(input("Enter your account number: "))
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data
                    if i["Account Number"] == accnumber and i["Pin"] == pin]

        if not userdata:
            print("Account not found")
        else:
            check = input("Are you sure you want to delete your account? (y/n): ")

            if check == 'y' or check == 'Y':
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.Update()
                print("Account deleted successfully")

            elif check == 'n' or check == 'N':
                print("Account deletion cancelled")

user = Bank()

print("1. Create Account") 
print("2. Deposit") 
print("3. Withdraw") 
print("4. Details") 
print("5. Update Details") 
print("6. Delete Account") 
print("7. Exit")

check = int(input("Enter your choice: "))

if check == 1:
    user.CreateAccount()
elif check == 2:
    user.Deposit()
elif check == 3:
    user.Withdraw()
elif check == 4:
    user.Details()
elif check == 5:
    user.UpdateDetails()
elif check == 6:
    user.DeleteAccount()
elif check == 7:
    print("Thank you for using our services")