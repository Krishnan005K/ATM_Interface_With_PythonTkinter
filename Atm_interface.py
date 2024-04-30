import tkinter as tk
from tkinter import simpledialog, messagebox
from collections import defaultdict

class ATM:
    def __init__(self):
        self.initial_balance = 0
        self.balance = self.initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        transaction_detail = f'Deposited ${amount}'
        self.transaction_history.append(transaction_detail)
        return f'Deposited ${amount}. New balance: ${self.balance}'

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawn ${amount}')
            return f'Withdrawn ${amount}. New balance: ${self.balance}'
        else:
            return 'Insufficient funds'

    def get_balance(self):
        return f'Current balance: ${self.balance}'

    def get_transaction_history(self):
        return self.transaction_history

class MainApplicationFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.account_balances = defaultdict(float)
        self.user_transactions = defaultdict(list)
        self.current_user = None

        self.atm = ATM()

        self.account_balances[self.current_user] = self.atm.initial_balance

        self.title("Banking Application")
        self.geometry("500x500")

        self.balance_label = tk.Label(self, text=self.atm.get_balance())
        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit,height=5,width=20,padx=10,pady=10)
        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw,height=5,width=20,padx=10,pady=10)
        self.history_button = tk.Button(self, text="Transaction History", command=self.show_transaction_history,height=5,width=20,padx=10,pady=10)
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_application)

        self.balance_label.pack()
        self.deposit_button.pack()
        self.withdraw_button.pack()
        self.history_button.pack()
        self.exit_button.pack()

        self.authenticate_user()

    def authenticate_user(self):
        # Simple authentication system using a hardcoded username and password
        username = "user"
        password = "password"
        while True:
            entered_username = simpledialog.askstring("Login", "Enter username:")
            entered_password = simpledialog.askstring("Login", "Enter password:")
            if entered_username == username and entered_password == password:
                self.current_user = username
                break
            else:
                messagebox.showerror("Error", "Invalid username or password. Please try again.")

    def deposit(self):
        amount = float(simpledialog.askstring("Deposit", "Enter amount to deposit:"))
        result = self.atm.deposit(amount)
        self.account_balances[self.current_user] = self.atm.balance
        self.update_balance_label(result)

    def withdraw(self):
        amount = float(simpledialog.askstring("Withdraw", "Enter amount to withdraw:"))
        result = self.atm.withdraw(amount)
        self.account_balances[self.current_user] = self.atm.balance
        self.update_balance_label(result)

    def show_transaction_history(self):
        history = self.atm.get_transaction_history()
        if len(history) > 0:
            history_str = "\n".join(history)
            messagebox.showinfo("Transaction History", history_str)
        else:
            messagebox.showinfo("Transaction History", "Transaction history is empty.")

    def update_balance_label(self, result):
        self.balance_label.config(text=result)

    def exit_application(self):
        self.destroy()

if __name__ == "__main__":
    app = MainApplicationFrame()
    app.mainloop()
