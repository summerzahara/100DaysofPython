# Iterate through pandas dataframe
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

grades = {
    "student": ["Meredith", "Alex", "George", "Izzie", "Christina"],
    "scores": [98, 82, 93, 67, 99]
}

grades_df = pandas.DataFrame(grades)
print(grades_df)

ninety = {row.student:row.scores for (index, row) in grades_df.iterrows() if row.scores >= 90}
print(ninety)

