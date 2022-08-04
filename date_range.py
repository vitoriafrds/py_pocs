from ast import arg
from datetime import datetime
from datetime import timedelta
import argparse


def get_days_between(start_date, end_date):
    '''
    This function get all days between start_date and end_date
    Example:
    start_date = '2022-07-31'
    end_date = '2022-08-03'
    return: a list of: [2022-07-31, 2022-08-04, 2022-08-02, 2022-08-03]
    '''
    dates = []
    diff = end_date - start_date
    
    for i in range(diff.days + 1):
        dates.append(start_date + timedelta(days=i))
    
    return dates

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--start_date')
    parser.add_argument('--end_date')
    arguments = parser.parse_args()

    dates = get_days_between(datetime.strptime(arguments.start_date, '%Y-%m-%d').date(), 
                             datetime.strptime(arguments.end_date, '%Y-%m-%d').date())
    
    for day in dates:
        print(day)