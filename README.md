# Grandstream-Provisioning-new

create database Gakk character set utf8;
use Gakk;
create table users ( id_user int (10) NOT NULL AUTO_INCREMENT, name varchar(200) NOT NULL, ext int(50) NOT NULL UNIQUE, ip3 int(50) NOT NULL, ip4 int(50) NOT NULL, email varchar(50) DEFAULT NULL, pickup varchar(50) DEFAULT NULL, callGroup varchar(50) DEFAULT NULL, ring varchar(50) DEFAULT NULL, mac varchar(50) DEFAULT NULL, secret varchar(150) DEFAULT NULL UNIQUE, model int(50) NOT NULL, DID varchar(50) NOT NULL, PRIMARY KEY (id_user) );
