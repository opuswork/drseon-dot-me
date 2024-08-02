-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 02, 2024 at 11:23 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drseon_me`
--

-- --------------------------------------------------------

--
-- Table structure for table `home_contactmessage`
--

CREATE TABLE `home_contactmessage` (
  `id` bigint(20) NOT NULL,
  `sender_name` varchar(100) NOT NULL,
  `sender_email` varchar(254) NOT NULL,
  `sender_phone` varchar(15) DEFAULT NULL,
  `sender_message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `home_contactmessage`
--

INSERT INTO `home_contactmessage` (`id`, `sender_name`, `sender_email`, `sender_phone`, `sender_message`, `created_at`) VALUES
(1, 'Jon Stewart Doe', 'test@example.us', '6019521325', 'testtesttest', '2024-08-02 20:58:09.437470');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `home_contactmessage`
--
ALTER TABLE `home_contactmessage`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `home_contactmessage`
--
ALTER TABLE `home_contactmessage`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
