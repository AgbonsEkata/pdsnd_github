from ast import Break
import time
import pandas as pd
import numpy as np

# We are using a virtual environment
# python -m venv venv

# source venv/bin/activate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago','new york city','washington']
        city= input("\n Which city would you like to analyse? (Chicago, New york city, Washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a valid city name")

    # get user input for month (all, january, february, ... , june)
    while True:
        months = {'January':1, 'Febuary':2, 'March':3, 'April':4, 'May':5, 'June':6, 'None':0}
        month = input("\n which month would you like to consider? (January, February, March, April, May, June)? Type 'None' for no month filter\n").title()
        if month in months:
            break
        else:
            print("\n Please enter a valid month name")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','None']
        day = input("\n which day of the week would you like to consider? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? Type 'None' for no day filter \n)").title()
        if day in days:
            break
        else:
            print("\n Please enter a valid day")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    months = {'January':1, 'Febuary':2, 'March':3, 'April':4, 'May':5, 'June':6, 'None':0}
    days = {'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month != 'None':
        df = df.loc[df['Start Time'].dt.month == months[month]]
    if day != 'None':
        df = df.loc[df['Start Time'].dt.day == days[day]]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    dict_months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
    }

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # find the most common month
    common_month = df['month'].mode()[0]

    print('Most Common Month:', dict_months[common_month])


    # display the most common day of week
    # extract Day from the Start Time column to create a Day column
    df['day'] = df['Start Time'].dt.day_name()

    # find the most common day
    common_day = df['day'].mode()[0]
    print('Most Common Day:', common_day)


    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common start hour
    common_hour = df['hour'].mode()[0]

    print("The common Start Hour is {}:00 hrs".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\n', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['combination']= df['Start Station']+" "+"to"+" "+ df['End Station']
    popular_combination= df['combination'].mode()[0]
    print("The most frequent combination of Start and End Station is {} ".format(popular_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel Time', df['Trip Duration'].sum())


    # display mean travel time
    print('Mean travel Time', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts()
    print('the user count for the data is:', '\n', user_count)

    try:
        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('the gender count for the data is:', '\n', gender_count)

        # Display earliest, most recent, and most common year of birth
        # most common birth year
        common_birth_year = df['Birth Year'].mode()[0]
        common_birth_year

        # earliest birth year
        earliest_birth_year = df['Birth Year'].min()
        earliest_birth_year

        # latest birth year
        latest_birth_year = df['Birth Year'].max()
        latest_birth_year
    except Exception as e:
        print(f'Information not available for specified city:', e)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    runs = 0
def raw_data(df):
    runs = 0
    while True:
        ask_user = input('Would you like to view more raw data for the city selected? \nEnter yes or no: ')
        if ask_user == 'yes':
            runs += 1 #Adds 1 to current value, same as runs = runs + 1
            print(df.iloc[runs:runs + 5])
            runs += 5
        elif ask_user == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()

        dataframe = load_data(city, month, day)


        time_stats(dataframe)
        station_stats(dataframe)
        trip_duration_stats(dataframe)
        user_stats(dataframe)
        raw_data(dataframe)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()


#first change made in refactoring

#second change made in refactoring
