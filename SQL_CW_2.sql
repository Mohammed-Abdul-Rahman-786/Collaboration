-- SELECT * FROM dataanalytics.employee;

-- use dataanalytics;

-- select ename 
-- from employee 
-- where salary > (select avg(salary) from employee); 

-- select ename, salary
-- from employee 
-- where salary > (select avg(salary) from employee); 

-- CREATE TABLE departments (
--     department_id INT PRIMARY KEY,
--     department_name VARCHAR(50)
-- );

-- CREATE TABLE employees (
--     employee_id INT PRIMARY KEY,
--     employee_name VARCHAR(50),
--     department_id INT,
--     FOREIGN KEY (department_id) REFERENCES departments(department_id)
-- );

-- INSERT INTO departments (department_id, department_name) VALUES
-- (1, 'Sales'),
-- (2, 'Marketing'),
-- (3, 'HR');

-- INSERT INTO employees (employee_id, employee_name, department_id) VALUES
-- (101, 'Alice', 1),
-- (102, 'Bob', 1),
-- (103, 'Charlie', 2),
-- (104, 'Diana', 3);

-- select * from employees;
-- select * from departments;

-- select * 
-- from employees
-- where department_id in (select department_id 
-- 	from departments 
--     where department_name='sales');
--     
--     
-- select employee_name,
-- 	(select department_name
-- 	from departments
--     where departments.department_id = employees.department_id) as DNAME
-- from employees;


-- SELECT *
-- FROM employees
-- WHERE department_id IN (
--     SELECT department_id
--     FROM employees
--     GROUP BY department_id
--     HAVING COUNT(*) > 1
-- );

-- SELECT department_id
--     FROM employees
--     GROUP BY department_id
--     HAVING COUNT(*) > 1;
--     
-- SELECT *
-- FROM departments d
-- WHERE exists  (
--     SELECT 1
--     FROM employees e
--     where e.department_id=d.department_id
-- );

-- SELECT 1
--     FROM employees e, departments d
--     where e.department_id=d.department_id;
--     
--     
-- INSERT INTO departments (department_id, department_name) VALUES
-- (4, 'XYZ');


-- SELECT *
-- FROM departments d
-- WHERE not exists  (
--     SELECT 1
--     FROM employees e
--     where e.department_id=d.department_id
-- );

-- select department_id
-- from employees
-- group by department_id
-- having avg(employee_id)>102;

-- select department_id,avg(employee_id) from employees;

-- select department_id
-- from employees
-- where employee_id > (select avg(employee_id) from employees);

-- select ucase("hello world") as UPPER_CASE;

-- select lcase("HELLO WORLD") as lower_case;

-- select mid("hello world",4,8) as SUB_STRING;

-- select length("hello world") as LENGTH;

-- select round(1560.44444) as ROUND_OFF;

-- select now() as CURRENT_DATE_TIME;

-- select format(1234.1234,2) as FORMAT;

-- select * from orderstable;







