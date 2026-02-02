import pymysql

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "username@2811",
        db='library',
        )
    
    cur = conn.cursor()
    cur.execute("select * from staff")
    output = cur.fetchall()
    print(output)
    
    # To close the connection
    conn.close()

# Driver Code
if __name__ == "__main__" :
    mysqlconnect()

print("MySQL Connection Successful")

