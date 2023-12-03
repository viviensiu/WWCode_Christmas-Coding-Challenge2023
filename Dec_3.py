#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:40:20 2023

@author: graeme
"""
import pandas as pd
# =============================================================================
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | user_id        | int     |
# | name           | varchar |
# +----------------+---------+
# user_id is the primary key (column with unique values) for this table.
# This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.
#  
# 
# Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.
# 
# Return the result table ordered by user_id.
# 
# The result format is in the following example.
# 
#  
# 
# Example 1:
# 
# Input: 
# Users table:
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | aLice |
# | 2       | bOB   |
# +---------+-------+
# Output: 
# +---------+-------+
# | user_id | name  |
# +---------+-------+
# | 1       | Alice |
# | 2       | Bob   |
# +---------+-------+
# =============================================================================
# =============================================================================
# solution
# =============================================================================
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users.name = users.name.str.capitalize()
    return users.sort_values(by='user_id')

# =============================================================================
# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# | mail          | varchar |
# +---------------+---------+
# user_id is the primary key (column with unique values) for this table.
# This table contains information of the users signed up in a website. Some e-mails are invalid.
#  
# 
# Write a solution to find the users who have valid emails.
# 
# A valid e-mail has a prefix name and a domain where:
# 
# The prefix name is a string that may contain letters (upper or lower case), digits, underscore '_', period '.', and/or dash '-'. The prefix name must start with a letter.
# The domain is '@leetcode.com'.
# Return the result table in any order.
# 
# The result format is in the following example.
# 
#  
# 
# Example 1:
# 
# Input: 
# Users table:
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 2       | Jonathan  | jonathanisgreat         |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# | 5       | Marwan    | quarz#2020@leetcode.com |
# | 6       | David     | david69@gmail.com       |
# | 7       | Shapiro   | .shapo@leetcode.com     |
# +---------+-----------+-------------------------+
# Output: 
# +---------+-----------+-------------------------+
# | user_id | name      | mail                    |
# +---------+-----------+-------------------------+
# | 1       | Winston   | winston@leetcode.com    |
# | 3       | Annabelle | bella-@leetcode.com     |
# | 4       | Sally     | sally.come@leetcode.com |
# +---------+-----------+-------------------------+
# Explanation: 
# The mail of user 2 does not have a domain.
# The mail of user 5 has the # sign which is not allowed.
# The mail of user 6 does not have the leetcode domain.
# The mail of user 7 starts with a period.
# 
# =============================================================================
# =============================================================================
# solution
# =============================================================================
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    def check_email(email):
        special_char = set("\"!@#$%^&*()+?=,<>/'")

        if "@" in email:
            try:
                prefix, postfix = tuple(email.split("@"))
                if postfix != "leetcode.com":
                    return False
                elif prefix[0].isalpha():
                    if len(set(prefix).intersection(special_char)) > 0:
                        return False
                    else:
                        return True
                else:
                    return False
            except:
                return False
        else:
            return False
    users['valid'] = users.apply(lambda row: check_email(row['mail']), axis=1)
    return users.loc[users.valid==True, ['user_id', 'name', 'mail']]

# =============================================================================
# +--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | patient_id   | int     |
# | patient_name | varchar |
# | conditions   | varchar |
# +--------------+---------+
# patient_id is the primary key (column with unique values) for this table.
# 'conditions' contains 0 or more code separated by spaces. 
# This table contains information of the patients in the hospital.
#  
# 
# Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. Type I Diabetes always starts with DIAB1 prefix.
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
# Patients table:
# +------------+--------------+--------------+
# | patient_id | patient_name | conditions   |
# +------------+--------------+--------------+
# | 1          | Daniel       | YFEV COUGH   |
# | 2          | Alice        |              |
# | 3          | Bob          | DIAB100 MYOP |
# | 4          | George       | ACNE DIAB100 |
# | 5          | Alain        | DIAB201      |
# +------------+--------------+--------------+
# Output: 
# +------------+--------------+--------------+
# | patient_id | patient_name | conditions   |
# +------------+--------------+--------------+
# | 3          | Bob          | DIAB100 MYOP |
# | 4          | George       | ACNE DIAB100 | 
# +------------+--------------+--------------+
# Explanation: Bob and George both have a condition that starts with DIAB1.
# =============================================================================
# =============================================================================
# solution
# =============================================================================
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    def check_diab1(cond):
        for s in cond.split():
            if s.startswith("DIAB1"):
                return True
                break
            else:
                pass
        return False
        
    patients['DIAB1'] = patients.apply(lambda row: check_diab1(row['conditions']), axis=1) 
    return patients.loc[patients['DIAB1']==True, ['patient_id', 'patient_name', 'conditions']]