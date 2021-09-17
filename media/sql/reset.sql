use pydb;

drop  table login;

create table login(
	id int primary key auto_increment,
    name text not null,
    email text not null,
    username text not null,
    password text not null,
    organisation text not null
)

select * from login;