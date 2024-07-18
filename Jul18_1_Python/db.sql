create table jul18_coffee(
   c_no number(3) primary key,
   c_name varchar2(10 char) not null,
   c_price number(5) not null,
   c_bean varchar2(10 char) not null
)

select * from JUL18_COFFEE
update JUL18_COFFEE set c_name = '로부스타1' where c_name = '커피1'

delete from JUL18_COFFEE where c_no = 2
create sequence jul18_coffee_seq;
drop table jun18_coffee;
drop sequence jun18_coffee_seq;


select avg(c_price) from 
(select rownum as rn, c_no, c_name, c_price, c_bean from 
(select c_no, c_name, c_price, c_bean from jul18_coffee
)
)
where rn >= 1 and rn <= 5 order by c_price desc