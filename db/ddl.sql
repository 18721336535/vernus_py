  --词集表
 drop table if exists Car_Model_Info;
 create table Car_Model_Info(
     id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
     brand VARCHAR(32)  default '',
     series VARCHAR(32)  default '',
     engine VARCHAR(32)  default '',
     displacement VARCHAR(32)  default '',
     transmission VARCHAR(32)  default '',
     pyear VARCHAR(16)  default '',
     sell_name VARCHAR(64)  default '',
     create_by VARCHAR(32) NOT NULL DEFAULT 'ADMIN',
     create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
     update_by VARCHAR(32) NOT NULL DEFAULT 'ADMIN',
     update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间'
 )ENGINE=InnoDB DEFAULT CHARSET=utf8;

 create unique index Car_Model_Info_index on Car_Model_Info(id);
 create  index brand_name_index on Car_Model_Info(brand);

 insert into Car_Model_Info
  (brand,series,engine,displacement,transmission,pyear,sell_name)
  values('一汽大众','夏利A','CE16','1.6T','MT','2016','夏利 三厢 2016款 1.6 MT 定制版');

 --词集表
drop table if exists Wset_Weight;
create table Wset_Weight(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    facture_name VARCHAR(32)  default '',
    wscore DOUBLE default 0,
    create_by VARCHAR(32) NOT NULL DEFAULT 'ADMIN',
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    update_by VARCHAR(32) NOT NULL DEFAULT 'ADMIN',
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间'
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create unique index Wset_Weight_index on Wset_Weight(id);
create  index facture_name_index on Wset_Weight(facture_name);


drop table if exists ly_fv_matrix;
create table ly_fv_matrix(
   id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
   ly_id INT,
   ly_fv text,
   ly_fv_wset VARCHAR(1024)  default '',
   score DOUBLE default 0,
   status varchar(8) default '0',
   create_by VARCHAR(32) NOT NULL DEFAULT 'ADMIN',
   create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
   update_by VARCHAR(32) NOT NULL DEFAULT 'ADMIN',
   update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间'
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;

  create unique index ly_fv_matrix_index on ly_fv_matrix(id);




  drop table if exists Wset_Weight;
  create table Wset_Weight(
      id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
      facture_name VARCHAR(32)  default '',
      wscore DOUBLE default 0,
      create_by VARCHAR(32) NOT NULL DEFAULT 'ADMIN',
      create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
      update_by VARCHAR(32) NOT NULL DEFAULT 'ADMIN',
      update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间'
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;

  create unique index Wset_Weight_index on Wset_Weight(id);
  create  index facture_name_index on Wset_Weight(facture_name);