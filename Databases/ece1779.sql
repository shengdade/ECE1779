-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0;
SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0;
SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema ece1779
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ece1779
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ece1779`
  DEFAULT CHARACTER SET latin1;
USE `ece1779`;

-- -----------------------------------------------------
-- Table `ece1779`.`students`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ece1779`.`students`;

CREATE TABLE IF NOT EXISTS `ece1779`.`students` (
  `id`               INT  NOT NULL AUTO_INCREMENT,
  `name`             TEXT NOT NULL,
  `email`            TEXT NOT NULL,
  `date_of_birth`    DATE NOT NULL,
  `program_of_study` TEXT NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = MyISAM
  AUTO_INCREMENT = 5
  DEFAULT CHARACTER SET = latin1;

-- -----------------------------------------------------
-- Table `ece1779`.`courses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ece1779`.`courses`;

CREATE TABLE IF NOT EXISTS `ece1779`.`courses` (
  `id`          INT  NOT NULL AUTO_INCREMENT,
  `code`        TEXT NOT NULL,
  `title`       TEXT NOT NULL,
  `description` TEXT NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ece1779`.`sections`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ece1779`.`sections`;

CREATE TABLE IF NOT EXISTS `ece1779`.`sections` (
  `id`                INT  NOT NULL AUTO_INCREMENT,
  `courses_id`        INT  NOT NULL,
  `time`              TEXT NULL,
  `location`          TEXT NULL,
  `maximum_enrolment` INT  NULL,
  `current_enrolment` INT  NULL,
  INDEX `fk_sections_courses_idx` (`courses_id` ASC),
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_sections_courses`
  FOREIGN KEY (`courses_id`)
  REFERENCES `ece1779`.`courses` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION
)
  ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `ece1779`.`students_has_sections`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ece1779`.`students_has_sections`;

CREATE TABLE IF NOT EXISTS `ece1779`.`students_has_sections` (
  `students_id` INT NOT NULL,
  `sections_id` INT NOT NULL,
  PRIMARY KEY (`students_id`, `sections_id`),
  INDEX `fk_students_has_sections_sections1_idx` (`sections_id` ASC),
  INDEX `fk_students_has_sections_students1_idx` (`students_id` ASC)
)
  ENGINE = MyISAM
  DEFAULT CHARACTER SET = latin1;


SET SQL_MODE = @OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS;
