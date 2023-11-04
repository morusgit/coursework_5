--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET default_tablespace = '';

SET default_with_oids = false;

---
--- drop tables
---

DROP TABLE IF EXISTS vacancy_table;
DROP TABLE IF EXISTS employee_table;

CREATE TABLE vacancy_table (
    vacancy_name character varying(100),
    salary_from integer DEFAULT 0,
    salary_to integer DEFAULT 0,
    salary_currency character varying(100) DEFAULT NULL,
    company_name character varying(100),
    vacancy_url character varying(100)
    );

CREATE TABLE employee_table (
    employee_id text PRIMARY KEY,
    company_name character varying(100),
    employee_url text,
    employee_open_vacancy integer
    );
