
import pygal
import numpy as np
import pandas as pd 

donors = pd.read_csv('donors2016.csv')

collect_donations = donors.groupby(['contbr_nm', 'contbr_city', 'contbr_st', 'contbr_employer'], as_index = False)['contb_receipt_amt'].sum()
# print(pd.DataFrame(collect_donations))

# collect_donations = donors.groupby(['contbr_st'], as_index = False)['contb_receipt_amt'].sum()
collect_donations = pd.DataFrame(collect_donations)
collect_donations.to_csv('pivot.csv', columns = ['contbr_nm', 'contbr_city', 'contbr_st', 'contbr_employer', 'contb_receipt_amt'], index = False)
print(collect_donations.head())
# collect_donations.to_csv('pivot.csv',)

# pie_chart = pygal.Pie()
# pie_chart.title = "Ratio of Trump 2016 donations"

# for index, row in collect_donations.iterrows():
#     pie_chart.add(row['contbr_st'], row['contb_receipt_amt'])

# pie_chart.render_to_file('output.svg')
# pie_chart.render_to_png(filename = 'output.png')