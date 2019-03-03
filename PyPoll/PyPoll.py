#!/usr/bin/env python
# coding: utf-8

# In[33]:


import os
import pandas as pd
df = pd.read_csv ("C:/Users/Sisay/Desktop/Resources/election_data.csv")
# ATotal vote casted 
Total_votes = df["Candidate"].count()

Total_votes

Cand_votes = df["Candidate"].value_counts()

Cand_votes

#Convert to DataFrame
Cand_votes = pd.DataFrame(Cand_votes)

Cand_votes.head()

#Renaming the column
Cand_votes.Columns = ["votes"]

Candidate_list = Cand_votes.index.tolist()
Candidate_list

# Cand votes and list
Vote_list = Cand_votes.iloc[:,0].tolist()

Vote_list

#Percentages
Percent_votes = ((Vote_list/Total_votes)*100).round(2)

Percent_votes

#Percentage list
Percent_list = list(map('{}%'.format, Percent_votes))
Percent_list

#Result
Result = pd.DataFrame({"Candidate" : Candidate_list, "Vote" : Vote_list, "% Vote": Percent_votes})
Result

Win = Result.set_index("Vote")
Win

Win_votes = max(Vote_list)

Win_votes
Winner = Win.loc[Win_votes].Candidate
Winner

print(Total_votes, Win, Winner)

df3 = pd.DataFrame(Win)
df3 = df3.reset_index()

df3 = df3.rename(columns={"Vote":"Total_Votes"})
df3
df3.to_csv('desktop/output.csv', index=False)
Win





