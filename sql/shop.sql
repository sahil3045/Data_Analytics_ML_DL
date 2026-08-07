create database shop_db;

use shop_db;

create table customers(
	customer_id int auto_increment primary key,
    name varchar(100),
    email varchar(100) unique,
    address varchar(100)
);

insert into customers (name, email, address)
values ('Sahil kanchan', 'sahil.kanchan@somaiya.edu', '400075 - Ghatkopar'),
('Manas kanchan', 'manas.kanchan@somaiya.edu', '400075 - Ghatkopar'),
('Shivam Bhosle', 'shivam.bhosle@somaiya.edu', '411068 - Seawoods');

select * from customers;

select distinct name,address from customers;

select address from customers where address like '%Ghatkopar%';

select * from customers where name like '%sahil%' and address like '%Ghatkopar%';

select * from customers order by name ASC;
select * from customers order by customer_id desc;

update customers 
set address = '400610 - Thane' 
where customer_id = 1;

delete from customers where customer_id = 3;
 


