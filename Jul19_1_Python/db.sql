create table jul19_weather(
	w_no number(3) primary key,
	w_time number(2) not null,
	w_temp number(5, 1) not null,
	w_max_temp number(5, 1) not null,
	w_weather varchar2(10 char) not null,
	w_wind_direct varchar2(10 char) not null
);

create sequence jul19_weather_seq;

drop table jul19_weather cascade constraint purge;

select * from jul19_weather;


create table jul19_seoul_air(
	s_no number(3) primary key,
	s_name varchar2(10 char) not null,
	s_pm10 number(6, 2) not null,
	s_pm25 number(6, 2) not null
);

create sequence jul19_seoul_air_seq;

drop table jul19_seoul_air cascade constraint purge;
select * from jul19_seoul_air

---------------------------------------------------------------------
-- (table간 제약조건 고려 X)
-- 학생 : 이름, 생일, 몇 강의장, 중간, 기말

---------------------------------------------------------------------
-- 강의장 : 몇 강의장, 강의장 위치
-- 1강의장 : 5층 복도 오른쪽		/ 2강의장 : 5층 복도 왼쪽 끝
-- 3강의장 : 5층 복도 왼쪽 첫번째	/ 4강의장 : 6층 정면 / 5강의장 : 6층 오른쪽
-- 강의장에 대한 데이터는 여기에서 insert로 처리!
create table jul19_student(
	s_no number(3) primary key,
	s_name varchar2(10 char) not null,
	s_date date not null,
	s_class number(1) not null,
	s_middleScore number(3) not null,
	s_finalScore number(3) not null
);
select * from jul19_student

create sequence jul19_student_seq;
drop table jul19_student cascade constraint purge;
create table jul19_class(
	c_class number(1) primary key,
	c_location varchar2(15 char) not null
);

drop table jul19_class cascade constraint purge;
select * from jul19_class;
insert into JUL19_CLASS values(1, '5층 복도 오른쪽')
insert into JUL19_CLASS values(2, '5층 복도 왼쪽 끝')
insert into JUL19_CLASS values(3, '5층 복도 왼쪽 첫번째')
insert into JUL19_CLASS values(4, '6층 정면')
insert into JUL19_CLASS values(5, '6층 오른쪽')
