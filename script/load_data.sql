CREATE DATABASE IF NOT EXISTS test_21b;

USE test_21b;

CREATE TABLE IF NOT EXISTS `signals` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `tag_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `product_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY(`user_id`),
  KEY(`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOAD DATA LOCAL INFILE '/21B_tag_views_dataset.csv'
INTO TABLE signals
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;