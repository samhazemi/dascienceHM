
# coding: utf-8

# In[23]:


import pandas as pd
import os
readfile = os.path.join('purchase_data2.json')
pur_data = pd.read_json(readfile)


# In[24]:


player_count = len(pur_data['SN'].unique())
players_df = pd.DataFrame([{'Total Players': player_count}])
players_df.set_index('Total Players', inplace = True)
players_df


# In[25]:


no_dup_items = pur_data.drop_duplicates(['Item ID'], keep = 'last')
total_unique = len(no_dup_items)

total_pur = pur_data['Price'].count()

total_rev = round(pur_data['Price'].sum(),2)

avg_price = round(total_rev/total_pur, 2)


pur_analysis = pd.DataFrame([{
    
    "Number of Unique Items": total_unique,
    'Average Purchase Price': avg_price,
    'Total Purchases': total_pur,
    'Total Revenue': total_rev
}])


pur_analysis.style.format({'Average Purchase Price': '${:.2f}', 'Total Revenue': '${:,.2f}'})


# In[26]:



no_dup_players = pur_data.drop_duplicates(['SN'], keep ='last')


gender_counts = no_dup_players['Gender'].value_counts().reset_index()

gender_counts['% of Players'] = gender_counts['Gender']/player_count * 100

gender_counts.rename(columns = {'index': 'Gender', 'Gender': '# of Players'}, inplace = True)

gender_counts.set_index(['Gender'], inplace = True)

gender_counts.style.format({"% of Players": "{:.1f}%"})


# In[27]:


pur_count_by_gen = pd.DataFrame(pur_data.groupby('Gender')['Gender'].count())

total_pur_by_gen = pd.DataFrame(pur_data.groupby('Gender')['Price'].sum())

pur_analysis_gen = pd.merge(pur_count_by_gen, total_pur_by_gen, left_index = True, right_index = True)

pur_analysis_gen.rename(columns = {'Gender': '# of Purchases', 'Price':'Total Purchase Value'}, inplace=True)

pur_analysis_gen['Average Purchase Price'] = pur_analysis_gen['Total Purchase Value']/pur_analysis_gen['# of Purchases']

pur_analysis_gen = pur_analysis_gen.merge(gender_counts, left_index = True, right_index = True)

pur_analysis_gen['Normalized Totals'] = pur_analysis_gen['Total Purchase Value']/pur_analysis_gen['# of Players']
pur_analysis_gen

del pur_analysis_gen['% of Players']
del pur_analysis_gen['# of Players']

pur_analysis_gen.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}', 'Normalized Totals': '${:.2f}'})


# In[28]:


# By AGE

pur_data.loc[(pur_data['Age'] < 10), 'age_bin'] = "< 10"
pur_data.loc[(pur_data['Age'] >= 10) & (pur_data['Age'] <= 14), 'age_bin'] = "10 - 14"
pur_data.loc[(pur_data['Age'] >= 15) & (pur_data['Age'] <= 19), 'age_bin'] = "15 - 19"
pur_data.loc[(pur_data['Age'] >= 20) & (pur_data['Age'] <= 24), 'age_bin'] = "20 - 24"
pur_data.loc[(pur_data['Age'] >= 25) & (pur_data['Age'] <= 29), 'age_bin'] = "25 - 29"
pur_data.loc[(pur_data['Age'] >= 30) & (pur_data['Age'] <= 34), 'age_bin'] = "30 - 34"
pur_data.loc[(pur_data['Age'] >= 35) & (pur_data['Age'] <= 39), 'age_bin'] = "35 - 39"
pur_data.loc[(pur_data['Age'] >= 40), 'age_bin'] = "> 40"



pur_count_age = pd.DataFrame(pur_data.groupby('age_bin')['SN'].count())

avg_price_age = pd.DataFrame(pur_data.groupby('age_bin')['Price'].mean())

tot_pur_age = pd.DataFrame(pur_data.groupby('age_bin')['Price'].sum())

no_dup_age = pd.DataFrame(pur_data.drop_duplicates('SN', keep = 'last').groupby('age_bin')['SN'].count())

merge_age = pd.merge(pur_count_age, avg_price_age, left_index = True, right_index = True).merge(tot_pur_age, left_index = True, right_index = True).merge(no_dup_age, left_index = True, right_index = True)

merge_age.rename(columns = {"SN_x": "# of Purchases", "Price_x": "Average Purchase Price", "Price_y": "Total Purchase Value", "SN_y": "# of Purchasers"}, inplace = True)

merge_age['Normalized Totals'] = merge_age['Total Purchase Value']/merge_age['# of Purchasers']

merge_age.index.rename("Age", inplace = True)

merge_age.style.format({'Average Purchase Price': '${:.2f}', 'Total Purchase Value': '${:.2f}', 'Normalized Totals': '${:.2f}'})


# In[29]:


# Identify the the top 5 spenders in the game by total purchase value, then list (in a table):



purchase_amt_by_SN = pd.DataFrame(pur_data.groupby('SN')['Price'].sum())
num_purchase_by_SN = pd.DataFrame(pur_data.groupby('SN')['Price'].count())
avg_purchase_by_SN = pd.DataFrame(pur_data.groupby('SN')['Price'].mean())

merged_top5 = pd.merge(purchase_amt_by_SN, num_purchase_by_SN, left_index = True, right_index = True).merge(avg_purchase_by_SN, left_index=True, right_index=True)

merged_top5.rename(columns = {'Price_x': 'Total Purchase Value', 'Price_y':'Purchase Count', 'Price':'Average Purchase Price'}, inplace = True)

merged_top5.sort_values('Total Purchase Value', ascending = False, inplace=True)

merged_top5 = merged_top5.head()

merged_top5.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}'})


# In[30]:


# Identify the 5 most popular items by purchase count, then list (in a table):



top5_items_ID = pd.DataFrame(pur_data.groupby('Item ID')['Item ID'].count())

top5_items_ID.sort_values('Item ID', ascending = False, inplace = True)

top5_items_ID = top5_items_ID.iloc[0:6][:]

top5_items_total = pd.DataFrame(pur_data.groupby('Item ID')['Price'].sum())
 
top5_items = pd.merge(top5_items_ID, top5_items_total, left_index = True, right_index = True)

no_dup_items = pur_data.drop_duplicates(['Item ID'], keep = 'last')

top5_merge_ID = pd.merge(top5_items, no_dup_items, left_index = True, right_on = 'Item ID')

top5_merge_ID = top5_merge_ID[['Item ID', 'Item Name', 'Item ID_x', 'Price_y', 'Price_x']]

top5_merge_ID.set_index(['Item ID'], inplace = True)

top5_merge_ID.rename(columns =  {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace=True)

top5_merge_ID.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})


# In[31]:


# Most Profitable Items


top5_profit = pd.DataFrame(pur_data.groupby('Item ID')['Price'].sum())
top5_profit.sort_values('Price', ascending = False, inplace = True)

top5_profit = top5_profit.iloc[0:5][:]

pur_count_profit = pd.DataFrame(pur_data.groupby('Item ID')['Item ID'].count())

top5_profit = pd.merge(top5_profit, pur_count_profit, left_index = True, right_index = True, how = 'left')
top5_merge_profit = pd.merge(top5_profit, no_dup_items, left_index = True, right_on = 'Item ID', how = 'left')
top5_merge_profit = top5_merge_profit[['Item ID', 'Item Name', 'Item ID_x', 'Price_y','Price_x']]
top5_merge_profit.set_index(['Item ID'], inplace=True)
top5_merge_profit.rename(columns = {'Item ID_x': 'Purchase Count', 'Price_y': 'Item Price', 'Price_x': 'Total Purchase Value'}, inplace = True)
top5_merge_profit.style.format({'Item Price': '${:.2f}', 'Total Purchase Value': '${:.2f}'})

