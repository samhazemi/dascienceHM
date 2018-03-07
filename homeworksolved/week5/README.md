

```python
import pandas as pd
import os
readfile = os.path.join('purchase_data2.json')
pur_data = pd.read_json(readfile)
```


```python
player_count = len(pur_data['SN'].unique())
players_df = pd.DataFrame([{'Total Players': player_count}])
players_df.set_index('Total Players', inplace = True)
players_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
    </tr>
    <tr>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>74</th>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<style  type="text/css" >
</style>  
<table id="T_8bfc67fe_1b3b_11e8_9dfd_f8633f2f6c86" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Average Purchase Price</th> 
        <th class="col_heading level0 col1" >Number of Unique Items</th> 
        <th class="col_heading level0 col2" >Total Purchases</th> 
        <th class="col_heading level0 col3" >Total Revenue</th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_8bfc67fe_1b3b_11e8_9dfd_f8633f2f6c86level0_row0" class="row_heading level0 row0" >0</th> 
        <td id="T_8bfc67fe_1b3b_11e8_9dfd_f8633f2f6c86row0_col0" class="data row0 col0" >$2.92</td> 
        <td id="T_8bfc67fe_1b3b_11e8_9dfd_f8633f2f6c86row0_col1" class="data row0 col1" >64</td> 
        <td id="T_8bfc67fe_1b3b_11e8_9dfd_f8633f2f6c86row0_col2" class="data row0 col2" >78</td> 
        <td id="T_8bfc67fe_1b3b_11e8_9dfd_f8633f2f6c86row0_col3" class="data row0 col3" >$228.10</td> 
    </tr></tbody> 
</table> 




```python

no_dup_players = pur_data.drop_duplicates(['SN'], keep ='last')


gender_counts = no_dup_players['Gender'].value_counts().reset_index()

gender_counts['% of Players'] = gender_counts['Gender']/player_count * 100

gender_counts.rename(columns = {'index': 'Gender', 'Gender': '# of Players'}, inplace = True)

gender_counts.set_index(['Gender'], inplace = True)

gender_counts.style.format({"% of Players": "{:.1f}%"})
```




<style  type="text/css" >
</style>  
<table id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" ># of Players</th> 
        <th class="col_heading level0 col1" >% of Players</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86level0_row0" class="row_heading level0 row0" >Male</th> 
        <td id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86row0_col0" class="data row0 col0" >60</td> 
        <td id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86row0_col1" class="data row0 col1" >81.1%</td> 
    </tr>    <tr> 
        <th id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86level0_row1" class="row_heading level0 row1" >Female</th> 
        <td id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86row1_col0" class="data row1 col0" >13</td> 
        <td id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86row1_col1" class="data row1 col1" >17.6%</td> 
    </tr>    <tr> 
        <th id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86row2_col0" class="data row2 col0" >1</td> 
        <td id="T_8d0a4736_1b3b_11e8_be3b_f8633f2f6c86row2_col1" class="data row2 col1" >1.4%</td> 
    </tr></tbody> 
</table> 




```python
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
```




<style  type="text/css" >
</style>  
<table id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" ># of Purchases</th> 
        <th class="col_heading level0 col1" >Total Purchase Value</th> 
        <th class="col_heading level0 col2" >Average Purchase Price</th> 
        <th class="col_heading level0 col3" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Gender</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86level0_row0" class="row_heading level0 row0" >Female</th> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row0_col0" class="data row0 col0" >13</td> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row0_col1" class="data row0 col1" >$41.38</td> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row0_col2" class="data row0 col2" >$3.18</td> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row0_col3" class="data row0 col3" >$3.18</td> 
    </tr>    <tr> 
        <th id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86level0_row1" class="row_heading level0 row1" >Male</th> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row1_col0" class="data row1 col0" >64</td> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row1_col1" class="data row1 col1" >$184.60</td> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row1_col2" class="data row1 col2" >$2.88</td> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row1_col3" class="data row1 col3" >$3.08</td> 
    </tr>    <tr> 
        <th id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86level0_row2" class="row_heading level0 row2" >Other / Non-Disclosed</th> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row2_col0" class="data row2 col0" >1</td> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row2_col1" class="data row2 col1" >$2.12</td> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row2_col2" class="data row2 col2" >$2.12</td> 
        <td id="T_8e39ddf6_1b3b_11e8_bbcf_f8633f2f6c86row2_col3" class="data row2 col3" >$2.12</td> 
    </tr></tbody> 
</table> 




```python
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
```




<style  type="text/css" >
</style>  
<table id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" ># of Purchases</th> 
        <th class="col_heading level0 col1" >Average Purchase Price</th> 
        <th class="col_heading level0 col2" >Total Purchase Value</th> 
        <th class="col_heading level0 col3" ># of Purchasers</th> 
        <th class="col_heading level0 col4" >Normalized Totals</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Age</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86level0_row0" class="row_heading level0 row0" >10 - 14</th> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row0_col0" class="data row0 col0" >3</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row0_col1" class="data row0 col1" >$2.99</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row0_col2" class="data row0 col2" >$8.96</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row0_col3" class="data row0 col3" >3</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row0_col4" class="data row0 col4" >$2.99</td> 
    </tr>    <tr> 
        <th id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86level0_row1" class="row_heading level0 row1" >15 - 19</th> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row1_col0" class="data row1 col0" >11</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row1_col1" class="data row1 col1" >$2.76</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row1_col2" class="data row1 col2" >$30.41</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row1_col3" class="data row1 col3" >11</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row1_col4" class="data row1 col4" >$2.76</td> 
    </tr>    <tr> 
        <th id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86level0_row2" class="row_heading level0 row2" >20 - 24</th> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row2_col0" class="data row2 col0" >36</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row2_col1" class="data row2 col1" >$3.02</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row2_col2" class="data row2 col2" >$108.89</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row2_col3" class="data row2 col3" >34</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row2_col4" class="data row2 col4" >$3.20</td> 
    </tr>    <tr> 
        <th id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86level0_row3" class="row_heading level0 row3" >25 - 29</th> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row3_col0" class="data row3 col0" >9</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row3_col1" class="data row3 col1" >$2.90</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row3_col2" class="data row3 col2" >$26.11</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row3_col3" class="data row3 col3" >8</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row3_col4" class="data row3 col4" >$3.26</td> 
    </tr>    <tr> 
        <th id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86level0_row4" class="row_heading level0 row4" >30 - 34</th> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row4_col0" class="data row4 col0" >7</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row4_col1" class="data row4 col1" >$1.98</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row4_col2" class="data row4 col2" >$13.89</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row4_col3" class="data row4 col3" >6</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row4_col4" class="data row4 col4" >$2.31</td> 
    </tr>    <tr> 
        <th id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86level0_row5" class="row_heading level0 row5" >35 - 39</th> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row5_col0" class="data row5 col0" >6</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row5_col1" class="data row5 col1" >$3.56</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row5_col2" class="data row5 col2" >$21.37</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row5_col3" class="data row5 col3" >6</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row5_col4" class="data row5 col4" >$3.56</td> 
    </tr>    <tr> 
        <th id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86level0_row6" class="row_heading level0 row6" >< 10</th> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row6_col0" class="data row6 col0" >5</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row6_col1" class="data row6 col1" >$2.76</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row6_col2" class="data row6 col2" >$13.82</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row6_col3" class="data row6 col3" >5</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row6_col4" class="data row6 col4" >$2.76</td> 
    </tr>    <tr> 
        <th id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86level0_row7" class="row_heading level0 row7" >> 40</th> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row7_col0" class="data row7 col0" >1</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row7_col1" class="data row7 col1" >$4.65</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row7_col2" class="data row7 col2" >$4.65</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row7_col3" class="data row7 col3" >1</td> 
        <td id="T_8f5c136c_1b3b_11e8_adcb_f8633f2f6c86row7_col4" class="data row7 col4" >$4.65</td> 
    </tr></tbody> 
</table> 




```python
# Identify the the top 5 spenders in the game by total purchase value, then list (in a table):



purchase_amt_by_SN = pd.DataFrame(pur_data.groupby('SN')['Price'].sum())
num_purchase_by_SN = pd.DataFrame(pur_data.groupby('SN')['Price'].count())
avg_purchase_by_SN = pd.DataFrame(pur_data.groupby('SN')['Price'].mean())

merged_top5 = pd.merge(purchase_amt_by_SN, num_purchase_by_SN, left_index = True, right_index = True).merge(avg_purchase_by_SN, left_index=True, right_index=True)

merged_top5.rename(columns = {'Price_x': 'Total Purchase Value', 'Price_y':'Purchase Count', 'Price':'Average Purchase Price'}, inplace = True)

merged_top5.sort_values('Total Purchase Value', ascending = False, inplace=True)

merged_top5 = merged_top5.head()

merged_top5.style.format({'Total Purchase Value': '${:.2f}', 'Average Purchase Price': '${:.2f}'})
```




<style  type="text/css" >
</style>  
<table id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Total Purchase Value</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Average Purchase Price</th> 
    </tr>    <tr> 
        <th class="index_name level0" >SN</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86level0_row0" class="row_heading level0 row0" >Sundaky74</th> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row0_col0" class="data row0 col0" >$7.41</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row0_col1" class="data row0 col1" >2</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row0_col2" class="data row0 col2" >$3.71</td> 
    </tr>    <tr> 
        <th id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86level0_row1" class="row_heading level0 row1" >Aidaira26</th> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row1_col0" class="data row1 col0" >$5.13</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row1_col1" class="data row1 col1" >2</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row1_col2" class="data row1 col2" >$2.56</td> 
    </tr>    <tr> 
        <th id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86level0_row2" class="row_heading level0 row2" >Eusty71</th> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row2_col0" class="data row2 col0" >$4.81</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row2_col1" class="data row2 col1" >1</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row2_col2" class="data row2 col2" >$4.81</td> 
    </tr>    <tr> 
        <th id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86level0_row3" class="row_heading level0 row3" >Chanirra64</th> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row3_col0" class="data row3 col0" >$4.78</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row3_col1" class="data row3 col1" >1</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row3_col2" class="data row3 col2" >$4.78</td> 
    </tr>    <tr> 
        <th id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86level0_row4" class="row_heading level0 row4" >Alarap40</th> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row4_col0" class="data row4 col0" >$4.71</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row4_col1" class="data row4 col1" >1</td> 
        <td id="T_8fe899da_1b3b_11e8_aa0d_f8633f2f6c86row4_col2" class="data row4 col2" >$4.71</td> 
    </tr></tbody> 
</table> 




```python
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
```




<style  type="text/css" >
</style>  
<table id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item Name</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Item Price</th> 
        <th class="col_heading level0 col3" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86level0_row0" class="row_heading level0 row0" >94</th> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row0_col0" class="data row0 col0" >Mourning Blade</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row0_col1" class="data row0 col1" >3</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row0_col2" class="data row0 col2" >$3.64</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row0_col3" class="data row0 col3" >$10.92</td> 
    </tr>    <tr> 
        <th id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86level0_row1" class="row_heading level0 row1" >90</th> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row1_col0" class="data row1 col0" >Betrayer</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row1_col1" class="data row1 col1" >2</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row1_col2" class="data row1 col2" >$4.12</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row1_col3" class="data row1 col3" >$8.24</td> 
    </tr>    <tr> 
        <th id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86level0_row2" class="row_heading level0 row2" >111</th> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row2_col0" class="data row2 col0" >Misery's End</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row2_col1" class="data row2 col1" >2</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row2_col2" class="data row2 col2" >$1.79</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row2_col3" class="data row2 col3" >$3.58</td> 
    </tr>    <tr> 
        <th id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86level0_row3" class="row_heading level0 row3" >64</th> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row3_col0" class="data row3 col0" >Fusion Pummel</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row3_col1" class="data row3 col1" >2</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row3_col2" class="data row3 col2" >$2.42</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row3_col3" class="data row3 col3" >$4.84</td> 
    </tr>    <tr> 
        <th id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86level0_row4" class="row_heading level0 row4" >154</th> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row4_col0" class="data row4 col0" >Feral Katana</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row4_col1" class="data row4 col1" >2</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row4_col2" class="data row4 col2" >$4.11</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row4_col3" class="data row4 col3" >$8.22</td> 
    </tr>    <tr> 
        <th id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86level0_row5" class="row_heading level0 row5" >126</th> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row5_col0" class="data row5 col0" >Exiled Mithril Longsword</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row5_col1" class="data row5 col1" >2</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row5_col2" class="data row5 col2" >$1.08</td> 
        <td id="T_9072f070_1b3b_11e8_aec4_f8633f2f6c86row5_col3" class="data row5 col3" >$2.16</td> 
    </tr></tbody> 
</table> 




```python
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
```




<style  type="text/css" >
</style>  
<table id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86" > 
<thead>    <tr> 
        <th class="blank level0" ></th> 
        <th class="col_heading level0 col0" >Item Name</th> 
        <th class="col_heading level0 col1" >Purchase Count</th> 
        <th class="col_heading level0 col2" >Item Price</th> 
        <th class="col_heading level0 col3" >Total Purchase Value</th> 
    </tr>    <tr> 
        <th class="index_name level0" >Item ID</th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
        <th class="blank" ></th> 
    </tr></thead> 
<tbody>    <tr> 
        <th id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86level0_row0" class="row_heading level0 row0" >94</th> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row0_col0" class="data row0 col0" >Mourning Blade</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row0_col1" class="data row0 col1" >3</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row0_col2" class="data row0 col2" >$3.64</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row0_col3" class="data row0 col3" >$10.92</td> 
    </tr>    <tr> 
        <th id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86level0_row1" class="row_heading level0 row1" >117</th> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row1_col0" class="data row1 col0" >Heartstriker, Legacy of the Light</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row1_col1" class="data row1 col1" >2</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row1_col2" class="data row1 col2" >$4.71</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row1_col3" class="data row1 col3" >$9.42</td> 
    </tr>    <tr> 
        <th id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86level0_row2" class="row_heading level0 row2" >93</th> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row2_col0" class="data row2 col0" >Apocalyptic Battlescythe</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row2_col1" class="data row2 col1" >2</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row2_col2" class="data row2 col2" >$4.49</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row2_col3" class="data row2 col3" >$8.98</td> 
    </tr>    <tr> 
        <th id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86level0_row3" class="row_heading level0 row3" >90</th> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row3_col0" class="data row3 col0" >Betrayer</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row3_col1" class="data row3 col1" >2</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row3_col2" class="data row3 col2" >$4.12</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row3_col3" class="data row3 col3" >$8.24</td> 
    </tr>    <tr> 
        <th id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86level0_row4" class="row_heading level0 row4" >154</th> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row4_col0" class="data row4 col0" >Feral Katana</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row4_col1" class="data row4 col1" >2</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row4_col2" class="data row4 col2" >$4.11</td> 
        <td id="T_90ea486c_1b3b_11e8_8a44_f8633f2f6c86row4_col3" class="data row4 col3" >$8.22</td> 
    </tr></tbody> 
</table> 


