use eqsupply;
-- MySQL dump 10.11
--
-- Host: localhost    Database: eqsupply
-- ------------------------------------------------------
-- Server version	5.0.67

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account_account`
--

DROP TABLE IF EXISTS `account_account`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `account_account` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `reg_id` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `account_account`
--

LOCK TABLES `account_account` WRITE;
/*!40000 ALTER TABLE `account_account` DISABLE KEYS */;
INSERT INTO `account_account` VALUES (2,12,'dbc0dd07badb6e956328780043c248bd');
/*!40000 ALTER TABLE `account_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_5886d21f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `auth_message_user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=85 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add manufacturer',9,'add_manufacturer'),(26,'Can change manufacturer',9,'change_manufacturer'),(27,'Can delete manufacturer',9,'delete_manufacturer'),(28,'Can add category',10,'add_category'),(29,'Can change category',10,'change_category'),(30,'Can delete category',10,'delete_category'),(31,'Can add product',11,'add_product'),(32,'Can change product',11,'change_product'),(33,'Can delete product',11,'delete_product'),(34,'Can add quote',12,'add_quote'),(35,'Can change quote',12,'change_quote'),(36,'Can delete quote',12,'delete_quote'),(37,'Can add price',13,'add_price'),(38,'Can change price',13,'change_price'),(39,'Can delete price',13,'delete_price'),(40,'Can add quote item',14,'add_quoteitem'),(41,'Can change quote item',14,'change_quoteitem'),(42,'Can delete quote item',14,'delete_quoteitem'),(81,'Can delete account',27,'delete_account'),(80,'Can change account',27,'change_account'),(79,'Can add account',27,'add_account'),(46,'Can add category',16,'add_category'),(47,'Can change category',16,'change_category'),(48,'Can delete category',16,'delete_category'),(52,'Can add product',18,'add_product'),(53,'Can change product',18,'change_product'),(54,'Can delete product',18,'delete_product'),(55,'Can add division',19,'add_division'),(56,'Can change division',19,'change_division'),(57,'Can delete division',19,'delete_division'),(61,'Can add accessory',21,'add_accessory'),(62,'Can change accessory',21,'change_accessory'),(63,'Can delete accessory',21,'delete_accessory'),(67,'Can add quotation',23,'add_quotation'),(68,'Can change quotation',23,'change_quotation'),(69,'Can delete quotation',23,'delete_quotation'),(70,'Can add line item',24,'add_lineitem'),(71,'Can change line item',24,'change_lineitem'),(72,'Can delete line item',24,'delete_lineitem'),(73,'Can add cost',25,'add_cost'),(74,'Can change cost',25,'change_cost'),(75,'Can delete cost',25,'delete_cost'),(83,'Can change product variant',28,'change_productvariant'),(82,'Can add product variant',28,'add_productvariant'),(84,'Can delete product variant',28,'delete_productvariant');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'zedd','','','alwaysdeone@gmail.com','sha1$efcfe$fddbda51ed026393546cae6807bdf0f6d60014c0',1,1,1,'2010-03-19 15:21:12','2010-01-19 09:03:53'),(13,'dayo123','','','alwaysdeone@yahoo.com','sha1$18060$77e9dfc40968624ddd463a3b8d61c71e8612e65f',0,1,0,'2010-02-02 09:32:01','2010-02-02 09:32:01'),(12,'deone125','Dayo','Osikoya','a@a.com','sha1$0ea76$33b4bc6f93538cb6eb61610628620f97429474ab',0,1,0,'2010-03-23 12:51:35','2010-01-22 09:54:59'),(14,'deone','Oladayo','Osikoya','alwaysdeone@yahoo.com','sha1$uyb1U$16a51ab26e4903e0bed2b33c37ae03313a76f4ba',0,0,0,'2010-02-25 14:42:02','2010-02-25 14:42:02'),(15,'me','','','me@me.com','me',0,1,0,'2010-03-11 11:30:46','2010-03-11 11:30:46');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f116770` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL auto_increment,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) default NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `django_admin_log_user_id` (`user_id`),
  KEY `django_admin_log_content_type_id` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2009-12-03 08:21:35',1,3,'2','deone',1,''),(2,'2010-01-27 11:32:05',1,16,'1','Inspection Equipment',1,''),(3,'2010-01-27 11:33:14',1,16,'2','Pressure Measurement',1,''),(4,'2010-01-28 12:47:21',1,16,'1','Inspection Equipment',1,''),(5,'2010-01-28 12:47:27',1,16,'2','Pressure Measurement',1,''),(6,'2010-01-28 12:47:50',1,16,'2','Pressure Measurement',2,'Changed description.'),(7,'2010-01-28 12:48:29',1,16,'1','Inspection Equipment',2,'Changed description.'),(8,'2010-01-28 12:48:45',1,16,'2','Pressure Measurement',2,'Changed description.'),(19,'2010-01-29 11:21:40',1,16,'3','Amine Blush',1,''),(18,'2010-01-29 11:21:32',1,16,'2','Adhesion',1,''),(17,'2010-01-29 11:21:22',1,16,'1','Abrasion',1,''),(15,'2010-01-29 11:20:14',1,19,'1','Inspection Equipment',1,''),(16,'2010-01-29 11:20:25',1,19,'2','Pressure Measurement',1,''),(14,'2010-01-29 10:54:28',1,16,'3','Flanges',1,''),(20,'2010-01-29 11:22:03',1,16,'4','Industrial Pressure Transmitters',1,''),(21,'2010-01-29 11:22:10',1,16,'5','Screw-in Transmitters for Level Monitoring and Processing Industry',1,''),(22,'2010-01-29 14:32:56',1,16,'1','Abrasion Testers',2,'Changed name.'),(23,'2010-01-29 14:33:03',1,16,'2','Adhesion Testers',2,'Changed name.'),(24,'2010-01-29 14:46:39',1,18,'1','Elcometer 1730 Car Wash Simulator',1,''),(25,'2010-01-29 14:47:46',1,18,'2','Elcometer 1720 Abrasion Testers and Washability Testers',1,''),(26,'2010-01-29 15:25:34',1,18,'2','Elcometer 1720 Abrasion Testers and Washability Testers',2,'Changed image.'),(27,'2010-01-29 15:38:39',1,18,'1','Car Wash Simulator',1,''),(28,'2010-01-29 15:39:27',1,18,'1','Car Wash Simulator',2,'Changed image.'),(29,'2010-01-29 15:40:29',1,18,'2','Abrasion Testers & Washability Testers',1,''),(30,'2010-02-03 09:43:59',1,16,'7','Density',1,''),(31,'2010-02-03 09:44:43',1,16,'8','Dry Film Thickness',1,''),(32,'2010-02-03 11:08:03',1,18,'1','Elcometer 1800 Density Cup',1,''),(33,'2010-02-03 11:23:08',1,18,'2','Elcometer 8720 KB Balance',1,''),(34,'2010-02-03 11:26:11',1,18,'3','Elcometer 8721 Analytical Balance',1,''),(35,'2010-02-03 13:56:04',1,18,'2','Elcometer 8720 KB Balance',2,'Changed description.'),(36,'2010-02-03 13:56:28',1,18,'2','Elcometer 8720 KB Balance',2,'Changed description.'),(37,'2010-02-09 11:49:55',1,21,'2','PC Interface Cable',1,''),(53,'2010-02-11 10:32:45',1,21,'1','PC Interface Cable',1,''),(54,'2010-02-11 10:35:06',1,21,'1','PC Interface Cable',1,''),(55,'2010-02-11 10:35:26',1,21,'2','PC Interface Cable',1,''),(56,'2010-02-11 11:23:00',1,21,'1','STANDARD BALANCE - PC CONNECTION CABLE',1,''),(57,'2010-02-11 11:29:32',1,21,'2','ANALYTICAL BALANCE - PC CONNECTION CABLE - Elcometer 8721 Analytical Balance',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(9,'manufacturer','quote_generator','manufacturer'),(10,'category','quote_generator','category'),(11,'product','quote_generator','product'),(12,'quote','quote_generator','quote'),(13,'price','quote_generator','price'),(14,'quote item','quote_generator','quoteitem'),(27,'account','account','account'),(16,'category','products','category'),(18,'product','products','product'),(19,'division','products','division'),(21,'accessory','products','accessory'),(23,'quotation','quote','quotation'),(24,'line item','quote','lineitem'),(25,'cost','quote','cost'),(28,'product variant','products','productvariant');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_accessory`
--

DROP TABLE IF EXISTS `products_accessory`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `products_accessory` (
  `id` int(11) NOT NULL auto_increment,
  `product_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `part_number` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `accessory_page` varchar(255) NOT NULL,
  `cost` decimal(20,2) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `part_number` (`part_number`),
  KEY `products_accessory_product_id` (`product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `products_accessory`
--

LOCK TABLES `products_accessory` WRITE;
/*!40000 ALTER TABLE `products_accessory` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_accessory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_category`
--

DROP TABLE IF EXISTS `products_category`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `products_category` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `division_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `products_category_division_id` (`division_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `products_category`
--

LOCK TABLES `products_category` WRITE;
/*!40000 ALTER TABLE `products_category` DISABLE KEYS */;
INSERT INTO `products_category` VALUES (1,'Abrasion Testers','',1),(2,'Adhesion Testers','',1),(3,'Amine Blush','',1),(4,'Industrial Pressure Transmitters','',2),(5,'Screw-in Transmitters for Level Monitoring and Processing Industry','',2),(7,'Density','',1),(8,'Dry Film Thickness','',1);
/*!40000 ALTER TABLE `products_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_division`
--

DROP TABLE IF EXISTS `products_division`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `products_division` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `products_division`
--

LOCK TABLES `products_division` WRITE;
/*!40000 ALTER TABLE `products_division` DISABLE KEYS */;
INSERT INTO `products_division` VALUES (1,'Inspection Equipment',''),(2,'Pressure Measurement','');
/*!40000 ALTER TABLE `products_division` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_product`
--

DROP TABLE IF EXISTS `products_product`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `products_product` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `category_id` int(11) NOT NULL,
  `code` varchar(50) NOT NULL,
  `small_image` varchar(100) NOT NULL,
  `large_image` varchar(100) NOT NULL,
  `product_page` varchar(255) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `code` (`code`),
  KEY `products_product_category_id` (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `products_product`
--

LOCK TABLES `products_product` WRITE;
/*!40000 ALTER TABLE `products_product` DISABLE KEYS */;
INSERT INTO `products_product` VALUES (1,'Elcometer 1800 Density Cup','Elcometer 1800 is a stainless steel or anodised aluminium precision cup for determining the specific gravity or density of paints and similar products.',7,'Elcometer 1800','site_media/products/small/density_cup_s.jpg','site_media/products/large/density_cup_l.jpg','http://www.elcometer.com/international index pages/international/product pages - English/product pages/main pages/1800.htm'),(2,'Elcometer 8720 KB Balance','The Elcometer 8720 KB is a compact, low cost balance which offers extensive weighing functions selectable by the user.\r\n\r\nThere are two models available in two scale ranges. The Elcometer 8720/1 and Elcometer 8720/2 balances are very easy to use and supplied with a protective working cover and adjusting weight to allow the user to quickly adjust the calibration.',7,'Elcometer 8720','site_media/products/small/kb_balance_s.jpg','site_media/products/large/kb_balance_l.jpg','http://www.elcometer.com/international index pages/international/product pages - English/product pages/main pages/1800.htm'),(3,'Elcometer 8721 Analytical Balance','The Elcometer 8721 Analytical Balance is a very stable and robust balance due to its metal casing.\r\n\r\nSupplied with a glass draft excluder, the Elcometer 8721 is more accurate than the Elcometer 8720 and allows the user to take repeatable and accurate measurements.\r\n\r\nEach balance is supplied with a test weight to allow the user to quickly adjust the calibration and can be connected to a PC for digital data readings.',7,'Elcometer 8721','site_media/products/small/analytical_balance_s.jpg','site_media/products/large/analytical_balance_l.jpg','http://www.elcometer.com/international index pages/international/product pages - English/product pages/main pages/1800.htm');
/*!40000 ALTER TABLE `products_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_productvariant`
--

DROP TABLE IF EXISTS `products_productvariant`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `products_productvariant` (
  `id` int(11) NOT NULL auto_increment,
  `product_id` int(11) NOT NULL,
  `part_number` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `cost` decimal(20,2) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `part_number` (`part_number`),
  KEY `products_productvariant_product_id` (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `products_productvariant`
--

LOCK TABLES `products_productvariant` WRITE;
/*!40000 ALTER TABLE `products_productvariant` DISABLE KEYS */;
INSERT INTO `products_productvariant` VALUES (1,1,'K0001800M001','PICNOMETER 50CC - STAINLESS STEEL','135.00'),(2,1,'K0001800M002','PICNOMETER 50CC - STAINLESS STEEL WITH TEST CERTIFICATE','185.00'),(3,1,'K0001800M003','PICNOMETER 50CC - ALUMINIUM','135.00'),(4,1,'K0001800M004','PICNOMETER 50CC - ALUMINIUM WITH TEST CERTIFICATE','185.00'),(5,1,'K0001800M005','PICNOMETER 100CC - STAINLESS STEEL','140.00'),(6,1,'K0001800M006','PICNOMETER 100CC - STAINLESS STEEL WITH TEST CERTIFICATE','185.00'),(7,1,'K0001800M007','PICNOMETER 100CC - ALUMINIUM','135.00'),(8,1,'K0001800M008','PICNOMETER 100CC - ALUMINIUM WITH TEST CERTIFICATE','185.00'),(9,2,'K0008720M001','STANDARD BALANCE, 0-1210G - 220V','332.00'),(10,2,'K0008720M002','STANDARD BALANCE, 0-10100G - 220V','352.00'),(11,2,'K0UK8720M001','STANDARD BALANCE, 0-1210G - 240V','332.00'),(12,2,'K0UK8720M002','STANDARD BALANCE, 0-10100G - 240V','352.00'),(13,2,'K0US8720M001','STANDARD BALANCE, 0-1210G - 110V','332.00'),(14,2,'K0US8720M002','STANDARD BALANCE, 0-10100G - 110V','352.00'),(15,3,'K0008721M001','ANALYTICAL BALANCE, 0-220G - 220V','1133.00'),(16,3,'K0UK8721M001','ANALYTICAL BALANCE, 0-220G - 240V','1133.00'),(17,3,'K0US8721M001','ANALYTICAL BALANCE, 0-220G - 110V','1133.00');
/*!40000 ALTER TABLE `products_productvariant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quote_cost`
--

DROP TABLE IF EXISTS `quote_cost`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `quote_cost` (
  `id` int(11) NOT NULL auto_increment,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `quote_cost`
--

LOCK TABLES `quote_cost` WRITE;
/*!40000 ALTER TABLE `quote_cost` DISABLE KEYS */;
/*!40000 ALTER TABLE `quote_cost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quote_lineitem`
--

DROP TABLE IF EXISTS `quote_lineitem`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `quote_lineitem` (
  `id` int(11) NOT NULL auto_increment,
  `quotation_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `cost_per_unit` decimal(20,2) NOT NULL,
  `cost` decimal(20,2) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `quote_lineitem_quotation_id` (`quotation_id`),
  KEY `quote_lineitem_product_id` (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `quote_lineitem`
--

LOCK TABLES `quote_lineitem` WRITE;
/*!40000 ALTER TABLE `quote_lineitem` DISABLE KEYS */;
INSERT INTO `quote_lineitem` VALUES (3,1,1,5,'135.00','675.00'),(4,1,3,7,'135.00','945.00'),(5,1,5,4,'140.00','560.00'),(6,1,15,9,'1133.00','10197.00');
/*!40000 ALTER TABLE `quote_lineitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quote_quotation`
--

DROP TABLE IF EXISTS `quote_quotation`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `quote_quotation` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `time_created` datetime NOT NULL,
  `quotation_no` varchar(20) NOT NULL,
  `cost` decimal(20,2) NOT NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `quote_quotation_user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `quote_quotation`
--

LOCK TABLES `quote_quotation` WRITE;
/*!40000 ALTER TABLE `quote_quotation` DISABLE KEYS */;
INSERT INTO `quote_quotation` VALUES (1,12,'2010-03-22 14:07:30','AGS 03-10-01','0.00',0);
/*!40000 ALTER TABLE `quote_quotation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2010-03-23 12:11:04
