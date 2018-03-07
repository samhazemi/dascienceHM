
# coding: utf-8

# In[1]:


import pandas as pd
import os
readfile = os.path.join('purchase_data2.json')
pur_data = pd.read_json(readfile)


# In[3]:


player_count = len(pur_data['SN'].unique())
players_df = pd.DataFrame([{'Total Players': player_count}])
players_df.set_index('Total Players', inplace = True)
players_df


# In[4]:


no_dup_items = pur_data.drop_duplicates(['Item ID'], keep = 'last')
total_unique = len(no_dup_items)
#number of total purchases by counting occurances of price
total_pur = pur_data['Price'].count()
#calculates total revenue for table by summing occurance of price and below calc
total_rev = round(pur_data['Price'].sum(),2)
#calculates total_rev
avg_price = round(total_rev/total_pur, 2)

#creates Purchase Analysis DataFrame
pur_analysis = pd.DataFrame([{
    
    "Number of Unique Items": total_unique,
    'Average Purchase Price': avg_price,
    'Total Purchases': total_pur,
    'Total Revenue': total_rev
}])

#format Purchases Analysis Table
pur_analysis.style.format({'Average Purchase Price': '${:.2f}', 'Total Revenue': '${:,.2f}'})


# In[5]:


#creates df of unique player names by only keeping the last occurance
no_dup_players = pur_data.drop_duplicates(['SN'], keep ='last')

#counts gender values from the df with no duplicate screen names
gender_counts = no_dup_players['Gender'].value_counts().reset_index()
#adds column for % of players using player count from first table and gender_count 
#column which is a count from line above
gender_counts['% of Players'] = gender_counts['Gender']/player_count * 100
#renames columns
gender_counts.rename(columns = {'index': 'Gender', 'Gender': '# of Players'}, inplace = True)
#sets index as Gender for aesthetics 
gender_counts.set_index(['Gender'], inplace = True)
#just checking percents sum to 100%
#gender_counts['% of Players'].sum()
#formats table
gender_counts.style.format({"% of Players": "{:.1f}%"})


# In[6]:


pur_count_by_gen = pd.DataFrame(pur_data.groupby('Gender')['Gender'].count())
# sums price by gender
total_pur_by_gen = pd.DataFrame(pur_data.groupby('Gender')['Price'].sum())
#merges the two data frames from above
pur_analysis_gen = pd.merge(pur_count_by_gen, total_pur_by_gen, left_index = True, right_index = True)
#renames columns
pur_analysis_gen.rename(columns = {'Gender': '# of Purchases', 'Price':'Total Purchase Value'}, inplace=True)
#adds column for average purchase price by gender by dividing total purcahse value by gender by # of purchases by gender
pur_analysis_gen['Average Purchase Price'] = pur_analysis_gen['Total Purchase Value']/pur_analysis_gen['# of Purchases']
#merges gender counts from above table (excluding dup SNs) into current df 
pur_analysis_gen = pur_analysis_gen.merge(gender_counts, left_index = True, right_index = True)
# calculates and adds normalized total column by dividing total purchase value by unique # of players by genger
pur_analysis_gen['Normalized Totals'] = pur_analysis_gen['Total Purchase Value']/pur_analysis_gen['# of Players']
pur_analysis_gen
#deletes columns not needed for table (# of Players was used for normalized totals while % of players came from gender count table)
del pur_analysis_gen['% of Players']
del pur_analysis_gen['# of Players']
# #resets index for aesthetics 
# # pur_analysis_gen.set_index('Gender', inplace=True)
# #formats table
pur_analysis_gen.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}', 'Normalized Totals': '${:.2f}'})


# In[7]:


# The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
# Purchase Count
# Average Purchase Price
# Total Purchase Value
# Normalized Totals

#creates a column 'age_bin' based on conditional of age range
pur_data.loc[(pur_data['Age'] < 10), 'age_bin'] = "< 10"
pur_data.loc[(pur_data['Age'] >= 10) & (pur_data['Age'] <= 14), 'age_bin'] = "10 - 14"
pur_data.loc[(pur_data['Age'] >= 15) & (pur_data['Age'] <= 19), 'age_bin'] = "15 - 19"
pur_data.loc[(pur_data['Age'] >= 20) & (pur_data['Age'] <= 24), 'age_bin'] = "20 - 24"
pur_data.loc[(pur_data['Age'] >= 25) & (pur_data['Age'] <= 29), 'age_bin'] = "25 - 29"
pur_data.loc[(pur_data['Age'] >= 30) & (pur_data['Age'] <= 34), 'age_bin'] = "30 - 34"
pur_data.loc[(pur_data['Age'] >= 35) & (pur_data['Age'] <= 39), 'age_bin'] = "35 - 39"
pur_data.loc[(pur_data['Age'] >= 40), 'age_bin'] = "> 40"
#double checked count
# pur_data[['age_bin', 'Age']].count()

# counts purchases by age bin by counting screen names (non-unique)
pur_count_age = pd.DataFrame(pur_data.groupby('age_bin')['SN'].count())
#finds avg price of purchases by age bin
avg_price_age = pd.DataFrame(pur_data.groupby('age_bin')['Price'].mean())
#finds total purchase value by age bin
tot_pur_age = pd.DataFrame(pur_data.groupby('age_bin')['Price'].sum())
#deletes multiple occurances of SN while only keeping last, then counts # of unique
#players by age bin
no_dup_age = pd.DataFrame(pur_data.drop_duplicates('SN', keep = 'last').groupby('age_bin')['SN'].count())
#merges all info from above into one df
merge_age = pd.merge(pur_count_age, avg_price_age, left_index = True, right_index = True).merge(tot_pur_age, left_index = True, right_index = True).merge(no_dup_age, left_index = True, right_index = True)
#renames columns
merge_age.rename(columns = {"SN_x": "# of Purchases", "Price_x": "Average Purchase Price", "Price_y": "Total Purchase Value", "SN_y": "# of Purchasers"}, inplace = True)
#calculates normalized totals
merge_age['Normalized Totals'] = merge_age['Total Purchase Value']/merge_age['# of Purchasers']
#rest index for aesthetics
merge_age.index.rename("Age", inplace = True)
# formats
merge_age.style.format({'Average Purchase Price': '${:.2f}', 'Total Purchase Value': '${:.2f}', 'Normalized Totals': '${:.2f}'})


# In[8]:


# Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
# SN
# Purchase Count
# Average Purchase Price
# Total Purchase Value

#Group by screen name to find, total purchase per person, number of purchases per person, and average price price per person
purchase_amt_by_SN = pd.DataFrame(pur_data.groupby('SN')['Price'].sum())
num_purchase_by_SN = pd.DataFrame(pur_data.groupby('SN')['Price'].count())
avg_purchase_by_SN = pd.DataFrame(pur_data.groupby('SN')['Price'].mean())
# merge the above dfs
merged_top5 = pd.merge(purchase_amt_by_SN, num_purchase_by_SN, left_index = True, right_index = True).merge(avg_purchase_by_SN, left_index=True, right_index=True)
# rename columns
merged_top5.rename(columns = {'Price_x': 'Total Purchase Value', 'Price_y':'Purchase Count', 'Price':'Average Purchase Price'}, inplace = True)
# sort from highest purchase value to lowest
merged_top5.sort_values('Total Purchase Value', ascending = False, inplace=True)
# take top 5 only
merged_top5 = merged_top5.head()
# format
merged_top5.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}'})


# In[9]:


# Identify the 5 most popular items by purchase count, then list (in a table):
# Item ID
# Item Name
# Purchase Count
# Item Price
# Total Purchase Value

# gets a count of each item by grouping by Item ID and counting the number of each IDs occurances
top5_items_ID = pd.DataFrame(pur_data.groupby('Item ID')['Item ID'].count())
#sort from high to low total purchase count
top5_items_ID.sort_values('Item ID', ascending = False, inplace = True)
#keep the first 6 rows because there is a tie
top5_items_ID = top5_items_ID.iloc[0:6][:]
#find the total purchase value of each item
top5_items_total = pd.DataFrame(pur_data.groupby('Item ID')['Price'].sum())
#merge purcahse count and total purcahse value 
top5_items = pd.merge(top5_items_ID, top5_items_total, left_index = True, right_index = True)
#drop duplicate items from original Df
no_dup_items = pur_data.drop_duplicates(['Item ID'], keep = 'last')
# merge to get all other info from the top 6 using the no dup df
top5_merge_ID = pd.merge(top5_items, no_dup_items, left_index = True, right_on = 'Item ID')
#keep only neede columns
top5_merge_ID = top5_merge_ID[['Item ID', 'Item Name', 'Item ID_x', 'Price_y', 'Price_x']]
#reset index as item ID for aesthetics
top5_merge_ID.set_index(['Item ID'], inplace = True)
# rename columns
top5_merge_ID.rename(columns =  {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace=True)
#format
top5_merge_ID.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})


# In[10]:


# Most Profitable Items

# Identify the 5 most profitable items by total purchase value, then list (in a table):
# Item ID
# Item Name
# Purchase Count
# Item Price
# Total Purchase Value

# find total purcahse value and sort by high to low
top5_profit = pd.DataFrame(pur_data.groupby('Item ID')['Price'].sum())
top5_profit.sort_values('Price', ascending = False, inplace = True)
# only keep top 5
top5_profit = top5_profit.iloc[0:5][:]
#get item purchase count
pur_count_profit = pd.DataFrame(pur_data.groupby('Item ID')['Item ID'].count())

top5_profit = pd.merge(top5_profit, pur_count_profit, left_index = True, right_index = True, how = 'left')
top5_merge_profit = pd.merge(top5_profit, no_dup_items, left_index = True, right_on = 'Item ID', how = 'left')
top5_merge_profit = top5_merge_profit[['Item ID', 'Item Name', 'Item ID_x', 'Price_y','Price_x']]
top5_merge_profit.set_index(['Item ID'], inplace=True)
top5_merge_profit.rename(columns = {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace = True)
top5_merge_profit.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})


# In[11]:


highest_priced = no_dup_items.sort_values('Price', ascending = False)
highest_priced[['Item ID', 'Item Name', 'Price']].head(18)


# In[12]:


lowest_priced = no_dup_items.sort_values('Price', ascending = True)
lowest_priced[['Item ID', 'Item Name', 'Price']].head(18)


# In[13]:


pur_analysis_gen.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}', 'Normalized Totals': '${:.2f}'})


# In[14]:


percent_total_gen = pur_analysis_gen['Total Purchase Value']/total_rev
percent_total_gen

