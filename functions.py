import pandas as pd

df = pd.read_csv('sample_csa.csv', index_col=0)
df.drop(['Unnamed: 5', 'Unnamed: 6'], axis=1, inplace=True)
df.columns = ['fname', 'lname', 'salary', 'eligibility']
df['eligibility'] = df['eligibility'].apply(lambda x: x.lower())
print(df)


# returns a boolean value if the first and lastname are present in the df might
# would want to add the employee id check to this function as well

def check_name(fname, lname):
    employee = False
    test_df = df[(df.fname == fname) & (df.lname == lname)]
    if len(test_df) > 0:
        employee = True
    return employee


def check_eligibility(fname, lname):
    record = df[(df.fname == fname) & (df.lname == lname)]
    eligibility = record['eligibility']
    if eligibility == 'full':
        message = 'You are eligible for a full CSA benefit.'
        survey = True
    elif eligibility == 'partial':
        message = 'You are eligible for a partial CSA benefit.'
        survey = True
    else:
        message = 'You are ineligible for the CSA benefit.'
        survey = False
    return message, survey




