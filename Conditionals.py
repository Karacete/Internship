def num_days(month):
    days = 31
    if month in ('apr','jun','sep','nov'):
        days = 30
    elif month == 'feb':
        days = 28
    print('number of days in',month,'is',days)

num_days('jun')