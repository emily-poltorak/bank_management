from datetime import datetime
import random
import csv

bank_accounts = {}

def save_to_csv(account_number, user_name, user_balance, filename="bank_account.csv"):
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ["Account Number", "User Name", "User Balance"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({"Account Number": account_number, "User Name": user_name, "User Balance": user_balance})

def load_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  

        data_dict = {}
        for row in reader:
            acc_num, user_name, user_balance = row
            data_dict[acc_num] = [user_name, int(user_balance)]  


def log_to_file(msg):
    print(datetime.now(), msg, file=open('bank_account.csv', 'a'))


def create_account():
    user_balance = None
    user_name = str(input("Enter name: \n"))

    while user_balance is None:
        try:
            user_balance = int(input("Enter initial deposit amount in USD: \n"))
        except ValueError:
            print("Invalid Value!")
            user_balance = None

    account_number = random.randint(500, 1000)
    bank_accounts[account_number] = [user_name, user_balance]

    print("Your bank account number is:", account_number)
    save_to_csv(account_number, user_name, user_balance)
    log_to_file(f"Account created, {user_name}")
    print("Bank account created successfully!")


def login():
    user_number = int(input("Enter your bank account number: \n"))
    if user_number in bank_accounts.keys():
        print(f"Logged in successfully, welcome {bank_accounts[user_number][0]}\n")
    
    log_in = 0
    while log_in == 0:
        user_selection2 = int(input("Enter 1 to check your balance\nEnter 2 to deposit an amount\nEnter 3 to Withdraw\nEnter 4 to log out\n"))
        if user_selection2 == 1:
            print("Your balance is: $", bank_accounts[user_number][1])

        elif user_selection2 == 2:
            user_add = int(input("How much would you like to deposit?:\n"))
            bank_accounts[user_number][1] += user_add
            save_to_csv(user_number, *bank_accounts[user_number])

        elif user_selection2 == 3:
            user_sub = int(input("How much would you like to withdraw?:\n"))

            if user_sub > bank_accounts[user_number][1]:
                print("The amount you want to withdraw is more than your balance\n")
            else:
                bank_accounts[user_number][1] -= user_sub
                save_to_csv(user_number, *bank_accounts[user_number])

        elif user_selection2 == 4:
            log_in = 1
            print("You have successfully logged out, come again")
            break

def main():
    while True:
        print("Welcome to: Bank of Aardvark")
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y")
        print("Today's date is", dt_string)

        user_selection = input("Enter 1 to create a new account\nEnter 2 to log in to an existing account\nEnter 3 to quit\n")
        if user_selection == "1":
            create_account()

        elif user_selection == "2":
            login()

        elif user_selection == "3":
            print("You have successfully quit, come again")
            break

        else:
            print("Input error")


if __name__ == "__main__":
    main()