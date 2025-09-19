uemail = input("Enter email id : ")
upass = input("Enter password : ")
#query = "select * from users where email = 'uemail' and password = 'upass'";
query = "select * from users where email = '"+uemail+"' and password = '"+upass+"'";
#query = "select * from users where email = 'dhruv@gi.com' and password = 'dhruv@123'";
print(query)