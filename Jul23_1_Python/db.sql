create table jul23_location(
	l_no number(3) primary key,
	l_name varchar2(20 char) not null,
	l_phone varchar2(20 char) default ' - ',
	l_x number(10, 6) not null,
	l_y number(10, 6) not null
);

create sequence jul23_location_seq;
drop sequence jul23_location_seq;
drop table jul23_location cascade constraint purge;
select * from jul23_location

-- NVL 함수 : null일때 지정한 값으로 대치하는 함수
-- NVL(값, (값이)null일때 대체 값)
select nvl(null, '-'), nvl('null', '-') from dual;

-- NVL2 함수 : null의 여부에 따라서 지정한 값으로 대치하는 함수
-- NVL2(값, 값이 있을때 대체값, 값이 없을때 대체값)
select nvl2(null, 'A', 'B'), nvl2(null, 'A', 'B') from dual;