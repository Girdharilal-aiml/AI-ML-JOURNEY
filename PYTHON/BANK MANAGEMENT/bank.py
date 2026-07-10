import json
import random
from pathlib import Path


class Bank:
    database = "database.json"

    def __init__(self):
        if Path(self.database).exists():
            with open(self.database, "r") as f:
                self.data = json.load(f)
        else:
            self.data = []

    def save(self):
        with open(self.database, "w") as f:
            json.dump(self.data, f, indent=4)

    def find_user(self, acc_no, pin):
        for user in self.data:
            if user["Account Number"] == acc_no and user["Pin"] == pin:
                return user
        return None

    def create_account(self, name, age, email, pin):
        if age < 18:
            return "Age must be 18+"

        if len(str(pin)) != 4:
            return "PIN must be 4 digits"

        account = {
            "name": name,
            "age": age,
            "Email": email,
            "Pin": pin,
            "Account Number": random.randint(1000000000, 9999999999),
            "Balance": 0
        }

        self.data.append(account)
        self.save()

        return account

    def deposit(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)

        if not user:
            return "Account not found"

        user["Balance"] += amount
        self.save()

        return "Deposit successful"

    def withdraw(self, acc_no, pin, amount):
        user = self.find_user(acc_no, pin)

        if not user:
            return "Account not found"

        if amount > user["Balance"]:
            return "Insufficient balance"

        user["Balance"] -= amount
        self.save()

        return "Withdrawal successful"

    def details(self, acc_no, pin):
        return self.find_user(acc_no, pin)

    def update_details(self, acc_no, pin, name, email, new_pin):
        user = self.find_user(acc_no, pin)

        if not user:
            return "Account not found"

        user["name"] = name
        user["Email"] = email
        user["Pin"] = new_pin

        self.save()

        return "Updated successfully"

    def delete_account(self, acc_no, pin):
        user = self.find_user(acc_no, pin)

        if not user:
            return "Account not found"

        self.data.remove(user)
        self.save()

        return "Deleted successfully"