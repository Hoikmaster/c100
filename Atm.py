class Atm(object):
    def __init__(self,cash_withdrawl,balance_enquiry):
        self.cash_withdrawl = cash_withdrawl
        self.balance_enquiry = balance_enquiry

    def check(self):
        print("checked")

    def fail(self):
        print("failed")

    def broke(self):
        print("no money")

BOFA = Atm("$50","$0")

print(BOFA.check())
print(BOFA.fail())