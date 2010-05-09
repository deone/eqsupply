use eqsupply;
-- MySQL dump 10.11
--
-- Host: localhost    Database: eqsupply
-- ------------------------------------------------------
-- Server version	5.0.88

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account_account` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `reg_id` varchar(50) NOT NULL,
  `phone` varchar(15) default NULL,
  `company` varchar(100) default NULL,
  `position` varchar(100) default NULL,
  `company_street_address` varchar(100) default NULL,
  `country` varchar(100) default NULL,
  `city` varchar(100) default NULL,
  `location` varchar(100) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account_account`
--

LOCK TABLES `account_account` WRITE;
/*!40000 ALTER TABLE `account_account` DISABLE KEYS */;
INSERT INTO `account_account` VALUES (1,21,'65abb51a185ad826296845b0fa016189','08029299274','Aerix Global Solutions','Software Developer','19A, Olosa Street','Nigeria','Lagos','6');
/*!40000 ALTER TABLE `account_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `permission_id_refs_id_5886d21f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `auth_message_user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=84 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add manufacturer',9,'add_manufacturer'),(26,'Can change manufacturer',9,'change_manufacturer'),(27,'Can delete manufacturer',9,'delete_manufacturer'),(28,'Can add category',10,'add_category'),(29,'Can change category',10,'change_category'),(30,'Can delete category',10,'delete_category'),(31,'Can add product',11,'add_product'),(32,'Can change product',11,'change_product'),(33,'Can delete product',11,'delete_product'),(34,'Can add quote',12,'add_quote'),(35,'Can change quote',12,'change_quote'),(36,'Can delete quote',12,'delete_quote'),(37,'Can add price',13,'add_price'),(38,'Can change price',13,'change_price'),(39,'Can delete price',13,'delete_price'),(40,'Can add quote item',14,'add_quoteitem'),(41,'Can change quote item',14,'change_quoteitem'),(42,'Can delete quote item',14,'delete_quoteitem'),(81,'Can delete account',27,'delete_account'),(80,'Can change account',27,'change_account'),(79,'Can add account',27,'add_account'),(46,'Can add category',16,'add_category'),(47,'Can change category',16,'change_category'),(48,'Can delete category',16,'delete_category'),(86,'Can change weight',29,'change_weight'),(87,'Can delete weight',29,'delete_weight'),(52,'Can add product',18,'add_product'),(53,'Can change product',18,'change_product'),(54,'Can delete product',18,'delete_product'),(55,'Can add division',19,'add_division'),(56,'Can change division',19,'change_division'),(57,'Can delete division',19,'delete_division'),(88,'Can add zone',30,'add_zone'),(61,'Can add accessory',21,'add_accessory'),(62,'Can change accessory',21,'change_accessory'),(63,'Can delete accessory',21,'delete_accessory'),(85,'Can add weight',29,'add_weight'),(67,'Can add quotation',23,'add_quotation'),(68,'Can change quotation',23,'change_quotation'),(69,'Can delete quotation',23,'delete_quotation'),(70,'Can add line item',24,'add_lineitem'),(71,'Can change line item',24,'change_lineitem'),(72,'Can delete line item',24,'delete_lineitem'),(83,'Can change product variant',28,'change_productvariant'),(82,'Can add product variant',28,'add_productvariant'),(84,'Can delete product variant',28,'delete_productvariant'),(89,'Can change zone',30,'change_zone'),(90,'Can delete zone',30,'delete_zone'),(91,'Can add cost',31,'add_cost'),(92,'Can change cost',31,'change_cost'),(93,'Can delete cost',31,'delete_cost'),(94,'Can add location',32,'add_location'),(95,'Can change location',32,'change_location'),(96,'Can delete location',32,'delete_location');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'zedd','','','alwaysdeone@gmail.com','sha1$efcfe$fddbda51ed026393546cae6807bdf0f6d60014c0',1,1,1,'2010-04-19 12:37:03','2010-01-19 09:03:53'),(21,'deone125','Dayo','Osikoya','alwaysdeone@gmail.com','sha1$ab651$efadbd2475f7d5308ff883397e7caa2e2beaa72e',0,1,0,'2010-05-06 13:38:43','2010-04-14 08:52:43');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `group_id_refs_id_f116770` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `permission_id_refs_id_67e79cb` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cost_cost`
--

DROP TABLE IF EXISTS `cost_cost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cost_cost` (
  `id` int(11) NOT NULL auto_increment,
  `weight_id` int(11) NOT NULL,
  `zone_id` int(11) NOT NULL,
  `cost` decimal(20,2) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `cost_cost_weight_id` (`weight_id`),
  KEY `cost_cost_zone_id` (`zone_id`)
) ENGINE=MyISAM AUTO_INCREMENT=54 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cost_cost`
--

LOCK TABLES `cost_cost` WRITE;
/*!40000 ALTER TABLE `cost_cost` DISABLE KEYS */;
INSERT INTO `cost_cost` VALUES (1,1,1,'3394.00'),(2,2,1,'4038.00'),(3,3,1,'4516.00'),(4,4,1,'4997.00'),(5,5,1,'5484.00'),(6,6,1,'5953.00'),(7,7,1,'6425.00'),(8,8,1,'6903.00'),(9,9,1,'7385.00'),(10,10,1,'7931.00'),(11,11,1,'8385.00'),(12,12,1,'8839.00'),(13,13,1,'9292.00'),(14,14,1,'9746.00'),(15,15,1,'10201.00'),(16,16,1,'10654.00'),(17,17,1,'11108.00'),(18,18,1,'11562.00'),(19,19,1,'12015.00'),(20,20,1,'12469.00'),(21,21,1,'13377.00'),(22,22,1,'14285.00'),(23,23,1,'15192.00'),(24,24,1,'16100.00'),(25,25,1,'17007.00'),(26,26,1,'17915.00'),(27,27,1,'18823.00'),(28,28,1,'19730.00'),(29,29,1,'20638.00'),(30,30,1,'21546.00'),(31,31,1,'22453.00'),(32,32,1,'23360.00'),(33,33,1,'24269.00'),(34,34,1,'25176.00'),(35,35,1,'26083.00'),(36,36,1,'26992.00'),(37,37,1,'27899.00'),(38,38,1,'28806.00'),(39,39,1,'29713.00'),(40,40,1,'30622.00'),(41,41,1,'31529.00'),(42,42,1,'32436.00'),(43,43,1,'33345.00'),(44,44,1,'34252.00'),(45,45,1,'35159.00'),(46,46,1,'39698.00'),(47,47,1,'44236.00'),(48,48,1,'48774.00'),(49,49,1,'53312.00'),(50,50,1,'57849.00'),(51,51,1,'62388.00'),(52,52,1,'66926.00'),(53,1,2,'2496.00');
/*!40000 ALTER TABLE `cost_cost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cost_location`
--

DROP TABLE IF EXISTS `cost_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cost_location` (
  `id` int(11) NOT NULL auto_increment,
  `zone_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `cost_location_zone_id` (`zone_id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cost_location`
--

LOCK TABLES `cost_location` WRITE;
/*!40000 ALTER TABLE `cost_location` DISABLE KEYS */;
INSERT INTO `cost_location` VALUES (1,2,'Abia'),(2,3,'Ogun'),(3,2,'Abuja'),(4,2,'Ekiti'),(5,2,'Ondo'),(6,1,'Bauchi'),(7,3,'Edo'),(8,2,'Calabar'),(9,2,'Ebonyi'),(10,2,'Enugu'),(11,1,'Gombe'),(12,3,'Osun'),(13,3,'Oyo'),(14,2,'Kwara'),(15,2,'Plateau'),(16,2,'Kaduna'),(17,2,'Jigawa'),(18,2,'Kano'),(19,1,'Katsina'),(20,4,'Lagos'),(21,1,'Kogi'),(22,2,'Yobe'),(23,2,'Borno'),(24,1,'Nasarawa'),(25,1,'Niger'),(26,1,'Benue'),(27,2,'Anambra'),(28,2,'Imo'),(29,2,'Bayelsa'),(30,2,'Rivers'),(31,1,'Kebbi'),(32,1,'Zamfara'),(33,1,'Sokoto'),(34,2,'Akwa Ibom'),(35,2,'Delta'),(36,1,'Taraba'),(37,1,'Adamawa'),(38,1,'Zaria');
/*!40000 ALTER TABLE `cost_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cost_weight`
--

DROP TABLE IF EXISTS `cost_weight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cost_weight` (
  `id` int(11) NOT NULL auto_increment,
  `weight` decimal(5,1) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cost_weight`
--

LOCK TABLES `cost_weight` WRITE;
/*!40000 ALTER TABLE `cost_weight` DISABLE KEYS */;
INSERT INTO `cost_weight` VALUES (1,'0.5'),(2,'1.0'),(3,'1.5'),(4,'2.0'),(5,'2.5'),(6,'3.0'),(7,'3.5'),(8,'4.0'),(9,'4.5'),(10,'5.0'),(11,'5.5'),(12,'6.0'),(13,'6.5'),(14,'7.0'),(15,'7.5'),(16,'8.0'),(17,'8.5'),(18,'9.0'),(19,'9.5'),(20,'10.0'),(21,'11.0'),(22,'12.0'),(23,'13.0'),(24,'14.0'),(25,'15.0'),(26,'16.0'),(27,'17.0'),(28,'18.0'),(29,'19.0'),(30,'20.0'),(31,'21.0'),(32,'22.0'),(33,'23.0'),(34,'24.0'),(35,'25.0'),(36,'26.0'),(37,'27.0'),(38,'28.0'),(39,'29.0'),(40,'30.0'),(41,'31.0'),(42,'32.0'),(43,'33.0'),(44,'34.0'),(45,'35.0'),(46,'40.0'),(47,'45.0'),(48,'50.0'),(49,'55.0'),(50,'60.0'),(51,'65.0'),(52,'70.0');
/*!40000 ALTER TABLE `cost_weight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cost_zone`
--

DROP TABLE IF EXISTS `cost_zone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cost_zone` (
  `id` int(11) NOT NULL auto_increment,
  `zone` int(11) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cost_zone`
--

LOCK TABLES `cost_zone` WRITE;
/*!40000 ALTER TABLE `cost_zone` DISABLE KEYS */;
INSERT INTO `cost_zone` VALUES (1,20),(2,21),(3,22),(4,23);
/*!40000 ALTER TABLE `cost_zone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
) ENGINE=MyISAM AUTO_INCREMENT=87 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2009-12-03 08:21:35',1,3,'2','deone',1,''),(2,'2010-01-27 11:32:05',1,16,'1','Inspection Equipment',1,''),(3,'2010-01-27 11:33:14',1,16,'2','Pressure Measurement',1,''),(4,'2010-01-28 12:47:21',1,16,'1','Inspection Equipment',1,''),(5,'2010-01-28 12:47:27',1,16,'2','Pressure Measurement',1,''),(6,'2010-01-28 12:47:50',1,16,'2','Pressure Measurement',2,'Changed description.'),(7,'2010-01-28 12:48:29',1,16,'1','Inspection Equipment',2,'Changed description.'),(8,'2010-01-28 12:48:45',1,16,'2','Pressure Measurement',2,'Changed description.'),(19,'2010-01-29 11:21:40',1,16,'3','Amine Blush',1,''),(18,'2010-01-29 11:21:32',1,16,'2','Adhesion',1,''),(17,'2010-01-29 11:21:22',1,16,'1','Abrasion',1,''),(15,'2010-01-29 11:20:14',1,19,'1','Inspection Equipment',1,''),(16,'2010-01-29 11:20:25',1,19,'2','Pressure Measurement',1,''),(14,'2010-01-29 10:54:28',1,16,'3','Flanges',1,''),(20,'2010-01-29 11:22:03',1,16,'4','Industrial Pressure Transmitters',1,''),(21,'2010-01-29 11:22:10',1,16,'5','Screw-in Transmitters for Level Monitoring and Processing Industry',1,''),(22,'2010-01-29 14:32:56',1,16,'1','Abrasion Testers',2,'Changed name.'),(23,'2010-01-29 14:33:03',1,16,'2','Adhesion Testers',2,'Changed name.'),(24,'2010-01-29 14:46:39',1,18,'1','Elcometer 1730 Car Wash Simulator',1,''),(25,'2010-01-29 14:47:46',1,18,'2','Elcometer 1720 Abrasion Testers and Washability Testers',1,''),(26,'2010-01-29 15:25:34',1,18,'2','Elcometer 1720 Abrasion Testers and Washability Testers',2,'Changed image.'),(27,'2010-01-29 15:38:39',1,18,'1','Car Wash Simulator',1,''),(28,'2010-01-29 15:39:27',1,18,'1','Car Wash Simulator',2,'Changed image.'),(29,'2010-01-29 15:40:29',1,18,'2','Abrasion Testers & Washability Testers',1,''),(30,'2010-02-03 09:43:59',1,16,'7','Density',1,''),(31,'2010-02-03 09:44:43',1,16,'8','Dry Film Thickness',1,''),(32,'2010-02-03 11:08:03',1,18,'1','Elcometer 1800 Density Cup',1,''),(33,'2010-02-03 11:23:08',1,18,'2','Elcometer 8720 KB Balance',1,''),(34,'2010-02-03 11:26:11',1,18,'3','Elcometer 8721 Analytical Balance',1,''),(35,'2010-02-03 13:56:04',1,18,'2','Elcometer 8720 KB Balance',2,'Changed description.'),(36,'2010-02-03 13:56:28',1,18,'2','Elcometer 8720 KB Balance',2,'Changed description.'),(37,'2010-02-09 11:49:55',1,21,'2','PC Interface Cable',1,''),(74,'2010-04-14 12:43:27',1,28,'1','Elcometer 1800 Density Cup - K0001800M001',2,'Changed weight.'),(73,'2010-04-14 12:43:09',1,28,'1','Elcometer 1800 Density Cup - K0001800M001',1,''),(72,'2010-03-25 14:28:00',1,31,'6','Weight: 3.0, Zone: 20, Cost: 5953',2,'Changed cost.'),(71,'2010-03-25 14:27:48',1,31,'5','Weight: 2.5, Zone: 20, Cost: 5484',2,'Changed cost.'),(70,'2010-03-25 14:27:40',1,31,'4','Weight: 2.0, Zone: 20, Cost: 4997',2,'Changed cost.'),(69,'2010-03-25 14:27:31',1,31,'3','Weight: 1.5, Zone: 20, Cost: 4516',2,'Changed cost.'),(68,'2010-03-25 14:27:14',1,31,'2','Weight: 1.0, Zone: 20, Cost: 4038',2,'Changed cost.'),(67,'2010-03-25 14:26:55',1,31,'1','Weight: 0.5, Zone: 20, Cost: 3394',2,'Changed cost.'),(66,'2010-03-25 13:59:59',1,31,'6','Weight: 3.0, Zone: 20, Cost: 6847',1,''),(65,'2010-03-25 13:59:44',1,29,'6','3.0',1,''),(53,'2010-02-11 10:32:45',1,21,'1','PC Interface Cable',1,''),(54,'2010-02-11 10:35:06',1,21,'1','PC Interface Cable',1,''),(55,'2010-02-11 10:35:26',1,21,'2','PC Interface Cable',1,''),(56,'2010-02-11 11:23:00',1,21,'1','STANDARD BALANCE - PC CONNECTION CABLE',1,''),(57,'2010-02-11 11:29:32',1,21,'2','ANALYTICAL BALANCE - PC CONNECTION CABLE - Elcometer 8721 Analytical Balance',1,''),(63,'2010-03-25 13:59:05',1,29,'5','2.5',1,''),(64,'2010-03-25 13:59:27',1,31,'5','Weight: 2.5, Zone: 20, Cost: 6307',1,''),(61,'2010-03-25 13:58:37',1,29,'4','2.0',1,''),(62,'2010-03-25 13:58:53',1,31,'4','Weight: 2.0, Zone: 20, Cost: 5748',1,''),(75,'2010-04-14 12:44:16',1,28,'None','Elcometer 1800 Density Cup - K0001800M001',3,''),(76,'2010-04-14 12:46:03',1,28,'8','Elcometer 1800 Density Cup - K0001800M008',2,'Changed weight.'),(77,'2010-04-14 12:46:15',1,28,'7','Elcometer 1800 Density Cup - K0001800M007',2,'Changed weight.'),(78,'2010-04-14 12:46:25',1,28,'6','Elcometer 1800 Density Cup - K0001800M006',2,'Changed weight.'),(79,'2010-04-14 12:46:33',1,28,'5','Elcometer 1800 Density Cup - K0001800M005',2,'Changed weight.'),(80,'2010-04-14 12:46:41',1,28,'4','Elcometer 1800 Density Cup - K0001800M004',2,'Changed weight.'),(81,'2010-04-14 12:46:45',1,28,'3','Elcometer 1800 Density Cup - K0001800M003',2,'Changed weight.'),(82,'2010-04-14 12:46:51',1,28,'2','Elcometer 1800 Density Cup - K0001800M002',2,'Changed weight.'),(83,'2010-04-14 12:46:56',1,28,'1','Elcometer 1800 Density Cup - K0001800M001',2,'Changed weight.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(9,'manufacturer','quote_generator','manufacturer'),(10,'category','quote_generator','category'),(11,'product','quote_generator','product'),(12,'quote','quote_generator','quote'),(13,'price','quote_generator','price'),(14,'quote item','quote_generator','quoteitem'),(27,'account','account','account'),(16,'category','products','category'),(18,'product','products','product'),(19,'division','products','division'),(21,'accessory','products','accessory'),(29,'weight','cost','weight'),(23,'quotation','quote','quotation'),(24,'line item','quote','lineitem'),(28,'product variant','products','productvariant'),(30,'zone','cost','zone'),(31,'cost','cost','cost'),(32,'location','cost','location');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_accessory`
--

LOCK TABLES `products_accessory` WRITE;
/*!40000 ALTER TABLE `products_accessory` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_accessory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_article`
--

DROP TABLE IF EXISTS `products_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_article` (
  `id` int(11) NOT NULL auto_increment,
  `headline` varchar(100) NOT NULL,
  `weight` decimal(5,1) NOT NULL,
  `pub_date` datetime NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_article`
--

LOCK TABLES `products_article` WRITE;
/*!40000 ALTER TABLE `products_article` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_category`
--

DROP TABLE IF EXISTS `products_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_category` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `division_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `products_category_division_id` (`division_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_division` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products_productvariant` (
  `id` int(11) NOT NULL auto_increment,
  `product_id` int(11) NOT NULL,
  `part_number` varchar(50) NOT NULL,
  `weight` decimal(5,1) NOT NULL,
  `description` longtext NOT NULL,
  `cost` decimal(20,2) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `part_number` (`part_number`),
  KEY `products_productvariant_product_id` (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_productvariant`
--

LOCK TABLES `products_productvariant` WRITE;
/*!40000 ALTER TABLE `products_productvariant` DISABLE KEYS */;
INSERT INTO `products_productvariant` VALUES (1,1,'K0001800M001','0.5','PICNOMETER 50CC - STAINLESS STEEL','135.00'),(2,1,'K0001800M002','0.5','PICNOMETER 50CC - STAINLESS STEEL WITH TEST CERTIFICATE','185.00'),(3,1,'K0001800M003','0.5','PICNOMETER 50CC - ALUMINIUM','135.00'),(4,1,'K0001800M004','0.5','PICNOMETER 50CC - ALUMINIUM WITH TEST CERTIFICATE','185.00'),(5,1,'K0001800M005','0.5','PICNOMETER 100CC - STAINLESS STEEL','140.00'),(6,1,'K0001800M006','0.5','PICNOMETER 100CC - STAINLESS STEEL WITH TEST CERTIFICATE','185.00'),(7,1,'K0001800M007','0.5','PICNOMETER 100CC - ALUMINIUM','135.00'),(8,1,'K0001800M008','0.5','PICNOMETER 100CC - ALUMINIUM WITH TEST CERTIFICATE','185.00'),(9,2,'K0008720M001','1.0','STANDARD BALANCE, 0-1210G - 220V','332.00'),(10,2,'K0008720M002','1.0','STANDARD BALANCE, 0-10100G - 220V','352.00'),(11,2,'K0UK8720M001','1.0','STANDARD BALANCE, 0-1210G - 240V','332.00'),(12,2,'K0UK8720M002','1.0','STANDARD BALANCE, 0-10100G - 240V','352.00'),(13,2,'K0US8720M001','1.0','STANDARD BALANCE, 0-1210G - 110V','332.00'),(14,2,'K0US8720M002','1.0','STANDARD BALANCE, 0-10100G - 110V','352.00'),(15,3,'K0008721M001','7.0','ANALYTICAL BALANCE, 0-220G - 220V','1133.00'),(16,3,'K0UK8721M001','7.0','ANALYTICAL BALANCE, 0-220G - 240V','1133.00'),(17,3,'K0US8721M001','7.0','ANALYTICAL BALANCE, 0-220G - 110V','1133.00');
/*!40000 ALTER TABLE `products_productvariant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quote_cost`
--

DROP TABLE IF EXISTS `quote_cost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quote_cost` (
  `id` int(11) NOT NULL auto_increment,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quote_lineitem` (
  `id` int(11) NOT NULL auto_increment,
  `quotation_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `cost_per_unit` decimal(20,2) NOT NULL,
  `cost` decimal(20,2) NOT NULL,
  `courier_charge_per_unit` decimal(10,2) default NULL,
  `courier_charge` decimal(20,2) default NULL,
  PRIMARY KEY  (`id`),
  KEY `quote_lineitem_quotation_id` (`quotation_id`),
  KEY `quote_lineitem_product_id` (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quote_lineitem`
--

LOCK TABLES `quote_lineitem` WRITE;
/*!40000 ALTER TABLE `quote_lineitem` DISABLE KEYS */;
INSERT INTO `quote_lineitem` VALUES (1,1,1,5,'135.00','675.00','14.25','71.25'),(2,1,2,8,'185.00','1480.00','14.25','114.00'),(3,2,1,12,'135.00','1620.00','14.25','171.00'),(4,2,2,2,'185.00','370.00','14.25','28.50'),(5,2,3,3,'135.00','405.00','14.25','42.75'),(6,2,4,4,'185.00','740.00','14.25','57.00'),(7,2,5,5,'140.00','700.00','14.25','71.25'),(8,2,6,7,'185.00','1295.00','14.25','99.75'),(9,2,7,5,'135.00','675.00','14.25','71.25'),(10,2,8,8,'185.00','1480.00','14.25','114.00'),(11,2,9,4,'332.00','1328.00','16.96','67.84'),(12,2,10,3,'352.00','1056.00','16.96','50.88'),(13,2,11,5,'332.00','1660.00','16.96','84.80'),(14,2,12,2,'352.00','704.00','16.96','33.92'),(15,2,13,6,'332.00','1992.00','16.96','101.76'),(16,2,14,8,'352.00','2816.00','16.96','135.68'),(17,2,15,3,'1133.00','3399.00','40.93','122.79'),(18,2,16,6,'1133.00','6798.00','40.93','245.58'),(19,2,17,9,'1133.00','10197.00','40.93','368.37');
/*!40000 ALTER TABLE `quote_lineitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quote_quotation`
--

DROP TABLE IF EXISTS `quote_quotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quote_quotation` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `time_created` datetime NOT NULL,
  `quotation_no` varchar(20) NOT NULL,
  `cost` decimal(20,2) NOT NULL,
  `courier_charge` decimal(20,2) default NULL,
  `pdf` varchar(100) default NULL,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `quote_quotation_user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quote_quotation`
--

LOCK TABLES `quote_quotation` WRITE;
/*!40000 ALTER TABLE `quote_quotation` DISABLE KEYS */;
INSERT INTO `quote_quotation` VALUES (1,21,'2010-04-20 12:55:41','AGS 04-10-01','2155.00','185.25','',1),(2,21,'2010-05-06 13:38:51','AGS 05-10-01','37235.00','1867.12','',1);
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

-- Dump completed on 2010-05-07 20:08:14
