# -*- coding: utf-8 -*-
input_ = 'employee_data1.csv' # or employee_data2.csv
import os
import pandas as pd

path = os.path.join(os.environ["HOMEPATH"], 'Desktop', 'python-challenge', 'PyBoss', 'raw_data', input_)
f = pd.read_csv(path)

# =============================================================================
# * The `Name` column should be split into separate `First Name` and `Last Name` columns.
# * The `DOB` data should be re-written into `MM/DD/YYYY` format.
# * The `SSN` data should be re-written such that the first five numbers are hidden from view.
# * The `State` data should be re-written as simple two-letter abbreviations.
# =============================================================================

f['First Name'], f['Last Name'] = f['Name'].str.split(' ', 1, expand = True)[0], f['Name'].str.split(' ', 1, expand = True)[1]


f['DOB'] = pd.to_datetime(f['DOB']).dt.strftime('%m/%d/%Y')



path2 = os.path.join(os.environ["HOMEPATH"], 'Desktop', 'python-challenge', 'PyBoss', 'raw_data', 'State Abbreviation.csv')
state = pd.read_csv(path2)

fi = pd.merge(f, state, how = 'left', left_on = 'State', right_on = 'Name')
fi.drop(['Name_x', 'Name_y', 'State'], axis=1, inplace=True)
fi.rename(columns = {'Abbreviation': 'State'}, inplace = True)

fi.SSN = '***-**-' + fi.SSN.str.split('-', expand = True)[2]

final = fi[['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]

print(final)