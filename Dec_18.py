#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:51:18 2023

@author: graeme
"""

# =============================================================================
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp is the primary key (column with unique values) for this table.
#  
# 
# Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
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
# ActorDirector table:
# +-------------+-------------+-------------+
# | actor_id    | director_id | timestamp   |
# +-------------+-------------+-------------+
# | 1           | 1           | 0           |
# | 1           | 1           | 1           |
# | 1           | 1           | 2           |
# | 1           | 2           | 3           |
# | 1           | 2           | 4           |
# | 2           | 1           | 5           |
# | 2           | 1           | 6           |
# +-------------+-------------+-------------+
# Output: 
# +-------------+-------------+
# | actor_id    | director_id |
# +-------------+-------------+
# | 1           | 1           |
# +-------------+-------------+
# Explanation: The only pair is (1, 1) where they cooperated exactly 3 times.
# 
# =============================================================================
# =============================================================================
# solution
# =============================================================================
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    output = actor_director.groupby(['actor_id', 'director_id']).count().reset_index()
    return output.loc[output.timestamp >= 3, ['actor_id', 'director_id']]
