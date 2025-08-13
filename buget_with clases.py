class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(i["amount"] for i in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f'{self.name:*^30}'
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        # Total line
        total = f"Total: {self.get_balance():.2f}"
        return f"{title}\n{items}{total}"


def create_spend_chart(categories):
    spending = []
    for category in categories:
        total = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spending.append(total)

    total_spent = sum(spending)
    percentages = [(amount / total_spent) * 100 for amount in spending]
    percentages = [int(p // 10) * 10 for p in percentages]  

    lines = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        lines += f"{level:>3}|"
        for p in percentages:
            lines += " o " if p >= level else "   "
        lines += " \n"

    # Separator line
    lines += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category name labels
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        lines += " "*5 
        for name in names:
            lines += f"{name[i] if i < len(name) else ' '}  "  
        lines += "\n"  

    return lines.strip("\n")

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(create_spend_chart([food, clothing, auto]))