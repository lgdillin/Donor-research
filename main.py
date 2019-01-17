
import pygal
import numpy as np
import pandas as pd 

from pandas import pivot_table

# for donors2020.csv
donors_2020 = pd.read_csv('donors2020.csv')
donors_2020 = donors_2020.groupby([
        'contributor_name', 
        'contributor_state', 
        'contributor_city', 
        'contributor_zip',
        'contributor_street_1', 
        'contributor_employer',
        'contributor_occupation'
    ], as_index = False)['contributor_aggregate_ytd'].max()
donors_2020 = pd.DataFrame(donors_2020)
print(donors_2020.head())

print('')
print('-------------------------------')
print('')

# for donors2016.csv
donors_2016 = pd.read_csv('donors2016.csv')
donors_2016 = donors_2016.groupby([
        'contbr_nm',
        'contbr_st',
        'contbr_city',
        'contbr_zip',
        'contbr_employer',
        'contbr_occupation'
    ], as_index = False)['contb_receipt_amt'].sum()
donors_2016 = pd.DataFrame(donors_2016)
print(donors_2016.head())

# cd = pivot_table(donors, values = ['contb_receipt_amt', 'total_donations'], index = ['contbr_nm', 'contbr_city', 'contbr_st', 'contbr_employer'], aggfunc = {'total_donations': np.sum})

# collect_donations = donors.groupby(['contbr_st'], as_index = False)['contb_receipt_amt'].sum()
#collect_donations = pd.DataFrame(collect_donations)
#collect_donations.to_csv('pivot.csv', columns = ['contbr_nm', 'contbr_city', 'contbr_st', 'contbr_employer', 'contb_receipt_amt'], index = False)
#print(collect_donations.head())
# collect_donations.to_csv('pivot.csv',)

# pie_chart = pygal.Pie()
# pie_chart.title = "Ratio of Trump 2016 donations"

# for index, row in collect_donations.iterrows():
#     pie_chart.add(row['contbr_st'], row['contb_receipt_amt'])

# pie_chart.render_to_file('output.svg')
# pie_chart.render_to_png(filename = 'output.png')