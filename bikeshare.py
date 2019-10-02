import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Would you like to see data for Chicago, New York City, or Washington\n').lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('Sorry your city name is invalid ,please try again.\n')
    while True:
        month=input('Which month - January, February, March, April, May, or June?\n').lower()
        if month in ('all','january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print('sorry your city name is invalid ,please try again.\n')
    while True:
        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday\n').lower()
        if day in ('all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday'):
            break
        else:
            print('sorry the day you entered is invalid ,please enter avalid day.\n')
    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

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
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mc_month=df['month'].mode()[0]
    print('Most common month:', mc_month)
    # TO DO: display the most common day of week
    mc_day=df['day_of_week'].mode()[0]
    print('Most common day: ',mc_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mc_hour = df['hour'].mode()[0]
    print('Most common Start Hour:', mc_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start=df['Start Station'].mode()[0]
    print('Most common start station: ',most_common_start)
    # TO DO: display most commonly used end station
    mc_end=df['End Station'].mode()[0]
    print('Most common end station: ',mc_end)
    # TO DO: display most frequent combination of start station and end station trip
    mc_compination=df[['Start Station', 'End Station']].mode().loc[0]
    print('Most common comoination of start station and end station is from {} to {}'.format(mc_compination[0],mc_compination[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tt_time=df['Trip Duration'].sum()
    print('The total travel time is: ',tt_time)
    # TO DO: display mean travel time
    mt_time=df['Trip Duration'].mean()
    print('The mean travel time is: ',mt_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types are ',user_types)
    # TO DO: Display counts of gender
    try:
        gender_count=df['Gender'].value_counts()
        print('The counts of gender are: ', gender_count)
    except:
        print('\nThere is no gender data for this city\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        e_yob=int(df['Birth Year'].min())
        print('\nThe earliest year of birth is:\n', e_yob)
        r_yob=int(df['Birth Year'].max())
        print('\nThe most recent year of birth is:\n', r_yob)
        c_yob=df['Birth Year'].mode()[0]
        print('\nThe most common year of birth is:\n',c_yob)
    except:
        print('\nThere is no birth data in this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def it_data(df):
    print('Would you like to view indivisual trip data?\n')
    i=0
    while True:
        choise=input('Please enter yes or no: \n')
        if choise == 'yes':
            print(df.iloc[i:i + 5,:])
            i+=5
            print('Do you want to keep printing raw data?\n')
        elif choise == 'no':
            break
        else:
            print('invalid input')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        it_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
