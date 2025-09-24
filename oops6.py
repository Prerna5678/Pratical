class Bank:

    def __init__(self,Acc_no,Acc_name):
        self.list=[]
        self.Acc_no=Acc_no
        self.Acc_name=Acc_name

    def deposit(self,balance,total,dep):
        self.data=balance
        total=balance+dep
        print(total)
        self.list.append(total)

    def withdraw(self,total,wit,balance):
        total=balance-wit
        print(total)

    def display(self):
        print(self.list)

bank1=Bank()
bank1.deposit(500)
bank1.withdraw(100)
bank1.display()

        