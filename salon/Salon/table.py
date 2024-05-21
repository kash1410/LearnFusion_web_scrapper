import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
mycursor.execute("create database stylo")

#table 1 : employee

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor()
mycursor.execute("create table employee(employee_id VARCHAR(50),name VARCHAR(50),phone_no VARCHAR(12),salary VARCHAR(10),address VARCHAR(100))")

# table 2 : client profile

import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor()
mycursor.execute("create table client_profile(name VARCHAR(50),phone_no VARCHAR(12),treatment VARCHAR(50),amount VARCHAR(10))")

#table 3 : packages 

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor()
mycursor.execute("create table packages(sno VARCHAR(10),package_name VARCHAR(50),amount VARCHAR(10))")

#table 4 : appointments

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor()
mycursor.execute("create table appointments(name VARCHAR(50),phone_no VARCHAR(12), scheduled_date VARCHAR(50),time VARCHAR(10))")

# table 5 : products for sale

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",db="stylo")
mycursor=mydb.cursor()
mycursor.execute("create table products_for_sale(product_name VARCHAR(50),quantity VARCHAR(10),amount VARCHAR(50),expiry_date VARCHAR(50))")

