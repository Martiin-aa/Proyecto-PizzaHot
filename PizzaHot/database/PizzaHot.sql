CREATE DATABASE  IF NOT EXISTS `pizzas_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `pizzas_schema`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pizzas_schema
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `pizza_id` int unsigned NOT NULL,
  `user_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pizzas_has_users_users1_idx` (`user_id`),
  KEY `fk_pizzas_has_users_pizzas_idx` (`pizza_id`),
  CONSTRAINT `fk_pizzas_has_users_pizzas` FOREIGN KEY (`pizza_id`) REFERENCES `pizzas` (`id`),
  CONSTRAINT `fk_pizzas_has_users_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (6,2,1,'2023-07-11 14:05:33','2023-07-11 14:05:33');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pizzas`
--

DROP TABLE IF EXISTS `pizzas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pizzas` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `size` varchar(45) DEFAULT NULL,
  `crust` varchar(45) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pizzas`
--

LOCK TABLES `pizzas` WRITE;
/*!40000 ALTER TABLE `pizzas` DISABLE KEYS */;
INSERT INTO `pizzas` VALUES (1,'Peperonni','Large','Thin',12200,'https://wepik.com/api/image/ai/6c8964bf-42d0-4d94-b788-6708585d384d','2023-07-11 13:09:31','2023-07-11 13:09:31'),(2,'Peperonni','Medium','Stuffed',8200,'https://wepik.com/api/image/ai/6c8964bf-42d0-4d94-b788-6708585d384d','2023-07-11 13:09:31','2023-07-11 13:09:31'),(3,'Peperonni','Small','Cracker',4200,'https://wepik.com/api/image/ai/6c8964bf-42d0-4d94-b788-6708585d384d','2023-07-11 13:09:31','2023-07-11 13:09:31'),(4,'Neapolitan','Large','Stuffed',12800,'https://wepik.com/api/image/ai/e33cd5e4-5c03-465d-a6ad-1d293ef108c6','2023-07-11 13:09:31','2023-07-11 13:09:31'),(5,'Neapolitan','Medium','Thin',8800,'https://wepik.com/api/image/ai/e33cd5e4-5c03-465d-a6ad-1d293ef108c6','2023-07-11 13:09:31','2023-07-11 13:09:31'),(6,'Neapolitan','Small','Cracker',5000,'https://wepik.com/api/image/ai/e33cd5e4-5c03-465d-a6ad-1d293ef108c6','2023-07-11 13:09:31','2023-07-11 13:09:31'),(7,'Margherita','Large','Cracker',14200,'https://wepik.com/api/image/ai/ab9bb8b1-5b8e-48eb-ba68-bafee7e4d351','2023-07-11 13:09:31','2023-07-11 13:09:31'),(8,'Margherita','Medium','Thin',9200,'https://wepik.com/api/image/ai/ab9bb8b1-5b8e-48eb-ba68-bafee7e4d351','2023-07-11 13:09:31','2023-07-11 13:09:31'),(9,'Margherita','Small','Stuffed',5800,'https://wepik.com/api/image/ai/ab9bb8b1-5b8e-48eb-ba68-bafee7e4d351','2023-07-11 13:09:31','2023-07-11 13:09:31');
/*!40000 ALTER TABLE `pizzas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pizzas_toppings`
--

DROP TABLE IF EXISTS `pizzas_toppings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pizzas_toppings` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `pizza_id` int unsigned NOT NULL,
  `topping_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pizzas_has_toppings_toppings1_idx` (`topping_id`),
  KEY `fk_pizzas_has_toppings_pizzas1_idx` (`pizza_id`),
  CONSTRAINT `fk_pizzas_has_toppings_pizzas1` FOREIGN KEY (`pizza_id`) REFERENCES `pizzas` (`id`),
  CONSTRAINT `fk_pizzas_has_toppings_toppings1` FOREIGN KEY (`topping_id`) REFERENCES `toppings` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pizzas_toppings`
--

LOCK TABLES `pizzas_toppings` WRITE;
/*!40000 ALTER TABLE `pizzas_toppings` DISABLE KEYS */;
/*!40000 ALTER TABLE `pizzas_toppings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `toppings`
--

DROP TABLE IF EXISTS `toppings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `toppings` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `toppings`
--

LOCK TABLES `toppings` WRITE;
/*!40000 ALTER TABLE `toppings` DISABLE KEYS */;
INSERT INTO `toppings` VALUES (1,'olive',200,'2023-07-11 13:09:23','2023-07-11 13:09:23'),(2,'onion',150,'2023-07-11 13:09:23','2023-07-11 13:09:23'),(3,'mushroom',300,'2023-07-11 13:09:23','2023-07-11 13:09:23'),(4,'basil',350,'2023-07-11 13:09:23','2023-07-11 13:09:23');
/*!40000 ALTER TABLE `toppings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(1005) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Martin','Araya','martin.arayaantezana@gmail.com','Pj. El Genoves','Santiago','$2b$12$20HpF4/kxGlViXHHia91Tu6jzGGar/.k2Ovm4hegLkOnCU2jMA3Ja','2023-07-11 13:10:21','2023-07-11 13:10:21');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-11 18:42:23
