-- SELECT * FROM dataanalytics.users;

-- create table user(
-- 	user_id int auto_increment,
--     name varchar(45),
--     primary key(user_id)
-- );
-- alter table user auto_increment=1001;

-- insert into user(name) values('A'),('B'),('C');

-- select * from user;

-- insert into user(name) values(null),(null),(null);

-- select user_id, coalesce(name, 'default') as name
-- from user;

-- start transaction;
-- savepoint A;
-- delete from user where user_id>1004;

-- SET SQL_SAFE_UPDATES = 0;

-- select * from user;

-- rollback to A;

-- select * from user;

-- commit;

-- select * from user;

-- start transaction;
-- savepoint A;

-- insert into user(name) values('D'),('E'),('F');

-- rollback to A;

-- select * from employees;

-- delimiter //
-- create procedure GetEmp()
-- begin
-- 	select * from employees;
-- end;
-- //

-- call GetEmp()

-- delimiter //

-- create procedure GetEmployeeById(in id int)
-- begin
-- 	select * from employees where employee_id = id;
-- end
-- //
-- call GetEmployeeById(102);

-- delimiter //
-- create procedure GetUserName(in id int, out name varchar(45))
-- begin
-- 	select employee_name into name
-- 	from employees
--     where employee_id=id;
-- end //

-- set @name='';
-- call GetUserName(101,@name);
-- select @name;




