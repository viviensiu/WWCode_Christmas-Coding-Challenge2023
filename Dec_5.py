#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:34:16 2023

@author: graeme
"""

# =============================================================================
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
#  
# 
# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).
# 
# The result format is in the following example.
# 
#  
# 
# Example 1:
# 
# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | 200                 |
# +---------------------+
# Example 2:
# 
# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# Output: 
# +---------------------+
# | SecondHighestSalary |
# +---------------------+
# | null                |
# +---------------------+
# 
# =============================================================================
# =============================================================================
# solution
# =============================================================================
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    new_col = 'SecondHighestSalary'
    employee = employee.drop_duplicates(subset=['salary']).sort_values(by='salary', ascending=False).rename(columns={'salary':new_col})[[new_col]]
    try:
        return employee.iloc[[1]]
    except:
        return pd.DataFrame({new_col: [np.nan]})