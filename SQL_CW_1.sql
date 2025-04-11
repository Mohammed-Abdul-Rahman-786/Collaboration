-- use dataanalytics;

-- create table products(Product_id int, ProductName varchar(30),Price int);

-- insert into products values(1,'bike5',200000),(2,'bike6',300000);

-- select * from products;

-- select min(price) from products;

-- select max(price) from products;

-- select avg(price) from products;

-- insert into products values(2,'bike4',100000);

-- select min(price) as SamllestPrice,Product_id
-- from products
-- group by Product_id;

-- select max(price) as LargestPrice,Product_id
-- from products
-- group by Product_id;

-- select avg(price) as avg,Product_id
-- from products
-- group by Product_id;

-- select count(*) as numberOfRows
-- from products;

-- select count(Product_id)
-- from products
-- where price>=200000;

-- select count(distinct price)
-- from products;

-- select sum(price)
-- from products;

-- create table Customers(
-- 	Customer_id int primary key,
--     name varchar(100)
-- );

-- create table Orders(
-- 	Order_id int primary key,
--     Customer_id int,
--     Product varchar(100),
--     foreign key (Customer_id) references Customers(Customer_id)
--     on delete cascade
-- );

-- INSERT INTO Customers (Customer_id, name) VALUES
-- (1, 'Alice'),
-- (2, 'Bob'),
-- (3, 'Charlie');

-- INSERT INTO Orders (Order_id, Customer_id, Product) VALUES
-- (101, 1, 'Laptop'),
-- (102, 1, 'Mouse'),
-- (103, 2, 'Keyboard'),
-- (104, 3, 'Monitor'),
-- (105, 2, 'USB Cable');

-- select * from customers;
-- select * from orders;

-- delete from customers where customer_id=1;

-- select * from products
-- order by price;

-- select * from products
-- order by price desc;

-- select productname,price/2 as offerprice
-- from products
-- order by offerprice;

-- select productname,price/2 as offerprice
-- from products
-- order by offerprice desc; 

-- CREATE TABLE Customerstable (

--     CustomerID INT PRIMARY KEY,

--     CustomerName VARCHAR(100),

--     ContactName VARCHAR(100),

--     Country VARCHAR(50)

-- );
--  
-- CREATE TABLE Orderstable (

--     OrderID INT PRIMARY KEY,

--     OrderDate DATE,

--     CustomerID INT,

--     Amount DECIMAL(10, 2),

--     FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)

-- );
--  
-- INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES

-- (1, 'John Doe', 'John D.', 'USA'),

-- (2, 'Jane Smith', 'Jane S.', 'UK'),

-- (3, 'Alice Brown', 'Alice B.', 'Canada'),

-- (4, 'Bob Johnson', 'Bob J.', 'Australia');
--  
-- INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES

-- (101, '2024-09-01', 1, 250.00),

-- (102, '2024-09-05', 2, 300.00),

-- (103, '2024-09-07', 1, 150.00),

-- (104, '2024-09-10', 3, 450.00);

-- select * from customerstable;
-- select * from orderstable;

-- select customerstable.customerid,customerstable.customername,orderstable.orderid,orderstable.orderdate,orderstable.amount
-- from customerstable inner join orderstable
-- on customerstable.customerid=orderstable.customerid;

-- select customerstable.customerid,customerstable.customername,orderstable.orderid,orderstable.orderdate,orderstable.amount
-- from customerstable left join orderstable
-- on customerstable.customerid=orderstable.customerid;

-- select customerstable.customerid,customerstable.customername,orderstable.orderid,orderstable.orderdate,orderstable.amount
-- from customerstable right join orderstable
-- on customerstable.customerid=orderstable.customerid;

-- select customerstable.customerid,customerstable.customername,orderstable.orderid,orderstable.orderdate,orderstable.amount
-- from customerstable join orderstable
-- on customerstable.customerid=orderstable.customerid;

-- create table Drinks(
-- 	Did int,
--     DName varchar(100)
-- );

-- create table Snacks(
-- 	Sid int,
--     SName varchar(100)
-- );

-- insert into drinks values(1,'tea'),(2,'coffee');
-- insert into snacks values(1,'cookie'),(2,'chips');

-- select * 
-- from drinks cross join snacks;

-- CREATE TABLE EMPLOYEE (EMP_ID INT, ENAME VARCHAR(20), JOB_DESC VARCHAR(25), SALARY INT, HIRE_DATE date);

-- INSERT INTO EMPLOYEE VALUES (1, 'RAM', 'ADMIN', 100000, DATE '2024-02-02');
-- INSERT INTO EMPLOYEE VALUES (2, 'george', 'MANAGER', 200000, DATE '2024-02-02');
-- INSERT INTO EMPLOYEE VALUES (3, 'Aravind', 'SALES', 300000, DATE '2024-02-02');
-- INSERT INTO EMPLOYEE VALUES (4, 'Nivetha', 'SALES', 250000, DATE '2024-02-02');
-- INSERT INTO EMPLOYEE VALUES (5, 'Hussain', 'HR', 350000, DATE '2024-02-02');
-- INSERT INTO EMPLOYEE VALUES (6, 'A', 'ABC', 500000, DATE '2024-02-02');
-- INSERT INTO EMPLOYEE VALUES (7, 'B', 'XYZ', 600000, DATE '2024-02-02');
-- INSERT INTO EMPLOYEE VALUES (8, 'C', 'ABC', 500000, DATE '2024-02-02');
-- INSERT INTO EMPLOYEE VALUES (9, 'D', 'XYZ', 600000, DATE '2024-02-02');

-- select Job_desc,avg(salary)
-- from employee
-- group by job_desc;

-- select Job_desc,count(*)
-- from employee
-- group by job_desc;

-- select Job_desc,count(*)
-- from employee
-- group by job_desc
-- having count(*)>1
-- order by job_desc;

-- select * from employee;

-- select Job_desc,count(*)
-- from employee
-- where salary>400000
-- group by job_desc
-- having count(*)>1
-- order by job_desc;









