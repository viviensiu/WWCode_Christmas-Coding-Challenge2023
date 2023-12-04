#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:39:27 2023

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
# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.
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
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+
# Example 2:
# 
# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | null                   |
# +------------------------+
# 
# =============================================================================
# =============================================================================
# solution
# =============================================================================
import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col_name = 'getNthHighestSalary({})'.format(N)
    employee = employee.drop_duplicates(subset=['salary'], ignore_index=True)
    employee = employee.sort_values(by='salary', ascending=False).rename(columns={'salary':col_name})
    try:
        return employee[[col_name]].iloc[[N-1]] 
    except:
        return pd.DataFrame({col_name: [np.nan]})