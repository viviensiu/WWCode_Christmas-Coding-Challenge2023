#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:03:02 2023

@author: graeme
"""

# =============================================================================
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | department  | varchar |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name of an employee, their department, and the id of their manager.
# If managerId is null, then the employee does not have a manager.
# No employee will be the manager of themself.
#  
# 
# Write a solution to find managers with at least five direct reports.
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
# Employee table:
# +-----+-------+------------+-----------+
# | id  | name  | department | managerId |
# +-----+-------+------------+-----------+
# | 101 | John  | A          | null      |
# | 102 | Dan   | A          | 101       |
# | 103 | James | A          | 101       |
# | 104 | Amy   | A          | 101       |
# | 105 | Anne  | A          | 101       |
# | 106 | Ron   | B          | 101       |
# +-----+-------+------------+-----------+
# Output: 
# +------+
# | name |
# +------+
# | John |
# +------+
# =============================================================================
# =============================================================================
# solution
# =============================================================================
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    valid_id = employee['id'].unique().tolist()
    direct_reports = employee.groupby(['managerId'])['id'].count().reset_index().rename(columns={'id': 'count'})
    manager = direct_reports.merge(employee, how='left', left_on='managerId', right_on='id', suffixes=['', '_r'])
    return manager[(manager['count'] >=5) & (manager['managerId'].isin(valid_id))][['name']]