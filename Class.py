class ATM(object):
	def __init__(self,cardno,withdrawl,balance=None):
		self.cardno = cardno
		self.withdrawl = withdrawl
		self.balance = balance or {}
	def setBalance(self,cardno,withdrawl):
		self.cardno[withdrawl] = balance

	def setGrade(self,cardno,withdrawl):
		return self.cardno[withdrawl]

c1 = ATM("Gautham", 13,{"math":4.5})
c2 = ATM("Cynna", 13,{"math":3.5})

print(c1.withdrawl)
print(c2.balance)