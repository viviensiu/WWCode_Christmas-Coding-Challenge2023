#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:43:46 2023

@author: graeme
"""

# =============================================================================
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID and name of a customer.
#  
# 
# Table: Orders
# 
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
#  
# 
# Write a solution to find all customers who never order anything.
# 
# Return the result table in any order.
# 
# The result format is in the following example.
# 
#  
# 
# Example 1:
# 
# Input: 
# Customers table:
# +----+-------+
# | id | name  |
# +----+-------+
# | 1  | Joe   |
# | 2  | Henry |
# | 3  | Sam   |
# | 4  | Max   |
# +----+-------+
# Orders table:
# +----+------------+
# | id | customerId |
# +----+------------+
# | 1  | 3          |
# | 2  | 1          |
# +----+------------+
# Output: 
# +-----------+
# | Customers |
# +-----------+
# | Henry     |
# | Max       |
# +-----------+
# 
# =============================================================================
# =============================================================================
# solution
# =============================================================================
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    set_customers = set(customers.id)
    set_orders = set(orders.customerId)
    set_no_orders = set_customers - set_orders
    return customers.loc[customers['id'].isin(list(set_no_orders)), ['name']].rename(columns={'name':'Customers'})

# =============================================================================
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | article_id    | int     |
# | author_id     | int     |
# | viewer_id     | int     |
# | view_date     | date    |
# +---------------+---------+
# There is no primary key (column with unique values) for this table, the table may have duplicate rows.
# Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
# Note that equal author_id and viewer_id indicate the same person.
#  
# 
# Write a solution to find all the authors that viewed at least one of their own articles.
# 
# Return the result table sorted by id in ascending order.
# 
# The result format is in the following example.
# 
#  
# 
# Example 1:
# 
# Input: 
# Views table:
# +------------+-----------+-----------+------------+
# | article_id | author_id | viewer_id | view_date  |
# +------------+-----------+-----------+------------+
# | 1          | 3         | 5         | 2019-08-01 |
# | 1          | 3         | 6         | 2019-08-02 |
# | 2          | 7         | 7         | 2019-08-01 |
# | 2          | 7         | 6         | 2019-08-02 |
# | 4          | 7         | 1         | 2019-07-22 |
# | 3          | 4         | 4         | 2019-07-21 |
# | 3          | 4         | 4         | 2019-07-21 |
# +------------+-----------+-----------+------------+
# Output: 
# +------+
# | id   |
# +------+
# | 4    |
# | 7    |
# +------+
# =============================================================================
# =============================================================================
# solution
# =============================================================================
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.loc[views.author_id == views.viewer_id, ['author_id']].rename(
        columns={'author_id':'id'}).drop_duplicates().sort_values(by='id')

# =============================================================================
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | tweet_id       | int     |
# | content        | varchar |
# +----------------+---------+
# tweet_id is the primary key (column with unique values) for this table.
# This table contains all the tweets in a social media app.
#  
# 
# Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.
# 
# Return the result table in any order.
# 
# The result format is in the following example.
# 
#  
# 
# Example 1:
# 
# Input: 
# Tweets table:
# +----------+----------------------------------+
# | tweet_id | content                          |
# +----------+----------------------------------+
# | 1        | Vote for Biden                   |
# | 2        | Let us make America great again! |
# +----------+----------------------------------+
# Output: 
# +----------+
# | tweet_id |
# +----------+
# | 2        |
# +----------+
# Explanation: 
# Tweet 1 has length = 14. It is a valid tweet.
# Tweet 2 has length = 32. It is an invalid tweet.
# =============================================================================
# =============================================================================
# solution
# =============================================================================
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[tweets.content.str.len() > 15, ['tweet_id']]

# =============================================================================
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | employee_id | int     |
# | name        | varchar |
# | salary      | int     |
# +-------------+---------+
# employee_id is the primary key (column with unique values) for this table.
# Each row of this table indicates the employee ID, employee name, and salary.
#  
# 
# Write a solution to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.
# 
# Return the result table ordered by employee_id.
# 
# The result format is in the following example.
# 
#  
# 
# Example 1:
# 
# Input: 
# Employees table:
# +-------------+---------+--------+
# | employee_id | name    | salary |
# +-------------+---------+--------+
# | 2           | Meir    | 3000   |
# | 3           | Michael | 3800   |
# | 7           | Addilyn | 7400   |
# | 8           | Juan    | 6100   |
# | 9           | Kannon  | 7700   |
# +-------------+---------+--------+
# Output: 
# +-------------+-------+
# | employee_id | bonus |
# +-------------+-------+
# | 2           | 0     |
# | 3           | 0     |
# | 7           | 7400  |
# | 8           | 0     |
# | 9           | 7700  |
# +-------------+-------+
# Explanation: 
# The employees with IDs 2 and 8 get 0 bonus because they have an even employee_id.
# The employee with ID 3 gets 0 bonus because their name starts with 'M'.
# The rest of the employees get a 100% bonus.
# 
# =============================================================================
# =============================================================================
# solution
# =============================================================================
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    def set_bonus(id, name, salary):
        if ((id % 2 < 1) | (name.startswith('M'))):
            return 0
        else:
            return salary
    
    employees['bonus'] = employees.apply(lambda row: set_bonus(row['employee_id'], row['name'], row['salary']), axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')
    