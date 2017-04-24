/*This file is to be used ONLY for the structure of the database!*/

CREATE DATABASE  IF NOT EXISTS `fapi`;

USE `api`;

-- Users

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;