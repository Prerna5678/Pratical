create database Library;
use Library;

-- admin login
CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

-- staff login
CREATE TABLE staff 
(
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,        -- Librarian, Assistant
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

-- users login
CREATE TABLE users 
(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    user_type ENUM('Student','Faculty') NOT NULL
) ENGINE=InnoDB;

-- add books table
CREATE TABLE books 
(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    images VARCHAR(255) NOT NULL,   
    quantity INT NOT NULL
) ENGINE=InnoDB;
 
 -- issue book
CREATE TABLE issue_records 
(
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    user_id INT NOT NULL,
    staff_id INT NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE NOT NULL,
    status ENUM('Issued','Returned') NOT NULL,

    CONSTRAINT fk_issue_book
        FOREIGN KEY (book_id) REFERENCES books(book_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT fk_issue_user
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT fk_issue_staff
        FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- return book
CREATE TABLE returns 
(
    return_id INT AUTO_INCREMENT PRIMARY KEY,
    issue_id INT NOT NULL,
    return_date DATE NOT NULL,
    fine DECIMAL(10,2) DEFAULT 0,

    CONSTRAINT fk_return_issue
        FOREIGN KEY (issue_id) REFERENCES issue_records(issue_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

 -- ENGINE=InnoDB = “Use the InnoDB engine so this table can support foreign keys, transactions, and data safety.”

ALTER TABLE users
MODIFY user_type ENUM('Student') NOT NULL;

ALTER TABLE staff
MODIFY role ENUM('Librarian','Assistant') NOT NULL;





















