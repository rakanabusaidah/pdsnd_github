import time
import pandas as pd
import numpy as np

# The available data
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
    city = input('\nWhat city you want to explore? Chicago, New york City, Washington.\n')
    city = city.lower()
    cities = ['chicago', 'new york city', 'washington']
    while(city not in cities):
        city = input('\nSorry! we do not have data in this city! What city you want to explore? Chicago, New york City, Washington.\n')
    # get user input for month (all, january, february, ... , june)
    month = input('\nWhat month you wanna see? select all if you are not sure!\n')
    month = month.lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while(month not in months):
        month = input('\nSorry! we do not have data in {}! looking for another month?\n'.format(month))
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhat day you wanna see? select all if you are not sure!\n')
    day = day.lower()
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'all']
    while(day not in days):
        day = input('\nThere is no day called {}? select all if you are not sure!\n'.format(day))

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    monthsnames = ['january', 'february', 'march', 'april', 'may', 'june']
    months = df['Start Time'].dt.month
    popular_month = months.mode()[0]
    print('\nMost Common Month is: ', monthsnames[popular_month - 1])
    # display the most common day of week
    days = df['Start Time'].dt.day_name()
    popular_day = days.mode()[0]
    print('\nMost Common Day of Week:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nMost commonly used start station is:', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\nMost commonly used end station is:', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    trip = df[['Start Station', 'End Station']]
    print('\nMost frequent combination of start station and end station trip is: ', trip.mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\n total travel time is:', df['Trip Duration'].sum())

    # display mean travel time
    print('\n mean travel time is:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('\nCounts of user Types:\n', user_types)


    # Display counts of gender
    try:
        gincoun = df['Gender'].value_counts()
        print('\nCounts of users gender:\n', gincoun)
    except:
        print('\nNo data about Genders in this city')
    # Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode())
        print('\n The earliest birth year is {}, while the most recent is {}, and the most common is {}'.format(earliest, recent, common))
    except:
        print('\nNo data about Birthdays in this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view == 'yes'):
        print(df.iloc[start_loc : start_loc + 5, 1:])
        start_loc += 5
        view = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
