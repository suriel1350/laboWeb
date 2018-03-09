create table productos (
	id SERIAL NOT NULL,
	codigo int,
	nombre varchar(100),
	precio float,
	exist int,
	"createdAt" date not null default CURRENT_DATE,
	"updatedAt" date not null default CURRENT_DATE 
);

i n s e r t i n t o p r o d u c t o s v a l u e s ( 1 , ’ dron ’ ,
’ dron with r a s p b e r r y p i 3 ’ , 8000 , 1 0 ) ;

insert into productos(codigo, nombre, precio, exist) values (12, 'dron with raspberry', 8000, 10);
insert into productos(codigo, nombre, precio, exist) values (3, 'dron without raspberry', 9000, 20);
insert into productos(codigo, nombre, precio, exist) values (3, 'dron for raspberry', 10000, 20);



alter table productos add constraint pk_productos primary key ( codigo ) ;

create table proveedores (
	codigo int,
	nombre varchar(100),
	direccion varchar (200),
	lat float,
	lon float
);

alter table proveedores add constraint pk_prov primary key (codigo);

insert into proveedores(codigo, nombre, direccion, lat, lon) values (1, 'intel', '5th street 13', 95.000, -200.234);
insert into proveedores(codigo, nombre, direccion, lat, lon) values (2, 'dell', '20th street 190', 120.23, -150.235);

create table prov_prod (
	id_product int,
	id_prov int,
	precio float,
	exist int
);

alter table prov_prod add constraint pk_prov_prod primary key (id_product, id_prov);
alter table prov_prod add constraint fk_id_product foreign key (id_product) references productos(codigo);
alter table prov_prod add constraint fk_id_prov foreign key (id_prov) references proveedores(codigo);

insert into prov_prod(id_product, id_prov, precio, exist) values (3, 1, 100, 10);
insert into prov_prod(id_product, id_prov, precio, exist) values (3, 2, 100, 10);
insert into prov_prod(id_product, id_prov, precio, exist) values (3, 1, 100, 10);

git clone https://github.com/redrbrt/sepomex-zip-codes.git 

CREATE TABLE sepomex ( 
	id SERIAL PRIMARY KEY NOT NULL, 
	idEstado INT NOT NULL, 
	estado VARCHAR(100) NOT NULL,
	idMunicipio SMALLINT NOT NULL, 
	municipio VARCHAR(160) NOT NULL, 
	ciudad VARCHAR(160), 
	zona VARCHAR(15) NOT NULL,
	cp INT NOT NULL , 
	asentamiento VARCHAR(700) NOT NULL, 
	tipo VARCHAR(200) NOT NULL,
	"createdAt" date not null default CURRENT_DATE,
	"updatedAt" date not null default CURRENT_DATE 
);