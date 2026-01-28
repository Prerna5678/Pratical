create database Library;
use Library;

-- books table
CREATE TABLE books 
(
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    quantity INT
) ENGINE=InnoDB;

-- users table
CREATE TABLE users 
(
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
)ENGINE=InnoDB;

-- staff table
CREATE TABLE staff (
    staff_id INT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(50),       -- Librarian, Assistant
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50)
)ENGINE=InnoDB;

-- issue-records table
CREATE TABLE issue_records 
(
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    user_id INT,
    staff_id INT,
    issue_date DATE,
    return_date DATE,
    status VARCHAR(20),

    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
)ENGINE=InnoDB; 

 -- ENGINE=InnoDB = “Use the InnoDB engine so this table can support foreign keys, transactions, and data safety.”

show tables;
Show table status WHERE Name='books';














