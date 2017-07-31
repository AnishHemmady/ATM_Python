import threading
import logging
import time
import pdb
'''logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)'''

class Person(object):
	def __init__(self,name):
		self.__name=name
		
	def set_name(self,nme):
		self.__name=nme
		
	def get_name(self):
		return self.__name
		
	
class Account(object):
	def __init__(self):
		self.__balance=10
		self.person=None
		self.account=None
		self.lock=threading.Lock()
		
		
	def get_account(self,p):
		if self.account==None:
			self.account=Account()
		self.account.person=p
		return self.account
		
	
	def get_balance(self):
		return self.__balance
		
	def deposit(self,money):
		#pdb.set_trace()
		self.lock.acquire()
		try:
			if self.__balance>0:
				print("{}is trying to deposit".format(self.person.get_name()))
				time.sleep(10)
				self.__balance=self.__balance+money
				print("Deposited {}".format(money))
				self.lock.release()
		except Exception as e:
			print ("error")
		
		
	def withdraw(self,amount):
		self.lock.acquire()
		try:
			if self.__balance>10 and self.__balance>amount:
				print("{} is trying to withdraw".format(self.person.get_name()))
				time.sleep(10)
				self.__balance=self.__balance-amount
				print("Removed {}".format(amount))
		except Exception as e:
			print("some error occurred")
		finally:
			self.lock.release()

class Multi(threading.Thread):
	def __init__(self,p):
		#pdb.set_trace()
		self.person=p
		threading.Thread.__init__(self)
		
	def run(self):
		#pdb.set_trace()
		for k in range(0,3):
			acc=Account()
			ac=acc.get_account(self.person)
			ac.deposit(100)
			time.sleep(10)
			ac.withdraw(50)
			if ac.get_balance()<0:
				print("overdrawn")
				ac.deposit(45)
			else:
				pass
			
				
		print("final balance is {}".format(ac.get_balance()))
		
		
def main():
	t1=Multi(Person("thread 1"))
	t1.start()
	t2=Multi(Person("thread 2"))
	t2.start()
	
	
if __name__=='__main__':
	main()
				
			