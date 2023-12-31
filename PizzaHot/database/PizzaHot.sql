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
-- Table structure for table `addresses`
--

DROP TABLE IF EXISTS `addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addresses` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `district` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `house_number` int DEFAULT NULL,
  `telephone` bigint DEFAULT NULL,
  `user_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  KEY `fk_addresses_users1_idx` (`user_id`),
  CONSTRAINT `fk_addresses_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addresses`
--

LOCK TABLES `addresses` WRITE;
/*!40000 ALTER TABLE `addresses` DISABLE KEYS */;
/*!40000 ALTER TABLE `addresses` ENABLE KEYS */;
UNLOCK TABLES;

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
  `deletable` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pizzas_has_users_users1_idx` (`user_id`),
  KEY `fk_pizzas_has_users_pizzas_idx` (`pizza_id`),
  CONSTRAINT `fk_pizzas_has_users_pizzas` FOREIGN KEY (`pizza_id`) REFERENCES `pizzas` (`id`),
  CONSTRAINT `fk_pizzas_has_users_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
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
  `deletable` tinyint(1) NOT NULL DEFAULT '1',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pizzas`
--

LOCK TABLES `pizzas` WRITE;
/*!40000 ALTER TABLE `pizzas` DISABLE KEYS */;
INSERT INTO `pizzas` VALUES (1,'Peperonni','Familiar','Delgada',12200,'https://wepik.com/api/image/ai/6c8964bf-42d0-4d94-b788-6708585d384d',1,'2023-07-26 14:39:05','2023-07-26 14:39:05'),(2,'Peperonni','Mediana','Rellena',8200,'https://wepik.com/api/image/ai/6c8964bf-42d0-4d94-b788-6708585d384d',1,'2023-07-26 14:39:05','2023-07-26 14:39:05'),(3,'Peperonni','Individual','Galleta',4200,'https://wepik.com/api/image/ai/6c8964bf-42d0-4d94-b788-6708585d384d',1,'2023-07-26 14:39:05','2023-07-26 14:39:05'),(4,'Napolitana','Familiar','Rellena',12800,'https://wepik.com/api/image/ai/e33cd5e4-5c03-465d-a6ad-1d293ef108c6',1,'2023-07-26 14:39:05','2023-07-26 14:39:05'),(5,'Napolitana','Mediana','Delgada',8800,'https://wepik.com/api/image/ai/e33cd5e4-5c03-465d-a6ad-1d293ef108c6',1,'2023-07-26 14:39:05','2023-07-26 14:39:05'),(6,'Napolitana','Individual','Galleta',5000,'https://wepik.com/api/image/ai/e33cd5e4-5c03-465d-a6ad-1d293ef108c6',1,'2023-07-26 14:39:05','2023-07-26 14:39:05'),(7,'Margarita','Familiar','Galleta',14200,'https://wepik.com/api/image/ai/ab9bb8b1-5b8e-48eb-ba68-bafee7e4d351',1,'2023-07-26 14:39:05','2023-07-26 14:39:05'),(8,'Margarita','Mediana','Delgada',9200,'https://wepik.com/api/image/ai/ab9bb8b1-5b8e-48eb-ba68-bafee7e4d351',1,'2023-07-26 14:39:05','2023-07-26 14:39:05'),(9,'Margarita','Individual','Rellena',5800,'https://wepik.com/api/image/ai/ab9bb8b1-5b8e-48eb-ba68-bafee7e4d351',1,'2023-07-26 14:39:05','2023-07-26 14:39:05');
/*!40000 ALTER TABLE `pizzas` ENABLE KEYS */;
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
INSERT INTO `toppings` VALUES (1,'Aceituna',200,'2023-07-26 14:38:52','2023-07-26 14:38:52'),(2,'Cebolla',150,'2023-07-26 14:38:52','2023-07-26 14:38:52'),(3,'Champiñón',300,'2023-07-26 14:38:52','2023-07-26 14:38:52'),(4,'Albahaca',350,'2023-07-26 14:38:52','2023-07-26 14:38:52');
/*!40000 ALTER TABLE `toppings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `toppings_pizzas`
--

DROP TABLE IF EXISTS `toppings_pizzas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `toppings_pizzas` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `topping_id` int unsigned NOT NULL,
  `pizza_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_toppings_has_pizzas_pizzas1_idx` (`pizza_id`),
  KEY `fk_toppings_has_pizzas_toppings1_idx` (`topping_id`),
  CONSTRAINT `fk_toppings_has_pizzas_pizzas1` FOREIGN KEY (`pizza_id`) REFERENCES `pizzas` (`id`),
  CONSTRAINT `fk_toppings_has_pizzas_toppings1` FOREIGN KEY (`topping_id`) REFERENCES `toppings` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `toppings_pizzas`
--

LOCK TABLES `toppings_pizzas` WRITE;
/*!40000 ALTER TABLE `toppings_pizzas` DISABLE KEYS */;
/*!40000 ALTER TABLE `toppings_pizzas` ENABLE KEYS */;
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
  `password` varchar(255) DEFAULT NULL,
  `logo` varchar(1055) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
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

-- Dump completed on 2023-07-26 14:40:17
