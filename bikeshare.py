import time
import pandas as pd
import numpy as np

CITY_DATA = { 'c': 'chicago.csv',
              'n': 'new_york_city.csv',
              'w': 'washington.csv' }

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
    city =input("Which city do you want? please choose a city by typing (c) for chicago or (n) for new york or (w) for washington: \n\n ").lower()
    # Validate the city input
    while city not in (CITY_DATA.keys()):
        print("\n Error: That's invalid city name.\n")
        city =input("Which city do you want? please choose a city by typing (c) for chicago or (n) for new york or (w) for washington: \n\n ").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january','february','march','april','may','june','all']
    month = input("\n\nTo filter {}\'s data by a particular month ,so please type the month or all for not filtering by month:\n-january\n-february\n-march\n-april\n-may\n-june\n-all\n\n:".format(city.title())).lower() 
    # Validate the user input
    while month not in months:
         print("\nError:  That's invalid input please write a valid month name or all.\n")    
         month =input("\n\n To filter {}\'s data by a particular month ,so please type the month or all for not filtering by month:\n-january\n-february\n-march\n-april\n-may\n-june\n-all\n\n:".format(city.title())).lower()      
                 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    Days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day =input("\n\n To filter {}\'s data by a particular day ,so please type the day or all for not filtering by day:\n-monday\n-tuesday\n-thursday\n-friday\n-saturday\n-sunday\n-all\n\n:".format(city.title())).lower()            
     #Validate the user input
    while day not in Days:
         print("\nError:  That's invalid input please write a valid day name or all.\n")  
         day =input("\n\n To filter {}\'s data by a particular day ,so please type the day or all for not filtering by day:\n-monday\n-tuesday\n-thursday\n-friday\n-saterday\n-sunday\n-all\n\n:".format(city.title())).lower()      
               

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
#     load datafile into a dataframe
    df=pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

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
    most_common_month=df['month'].value_counts().idxmax()
    print('The most common month is: {} '.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day_of_week=df['day_of_week'].value_counts().idxmax()
    print('The most common day of week is: {} '.format(most_common_day_of_week))

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_start_hour=df['Hour'].value_counts().idxmax()
    print('The most common start hour is: {} '.format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station= df['Start Station'].value_counts().idxmax()
    print('The most common start station is: {} '.format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].value_counts().idxmax()
    print('The most common end station is: {} '.format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station=df[['Start Station','End Station']].mode().loc[0]
    print('The most commonly start station and end station is: {},{} '.format(most_common_start_station[0], most_common_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel =df['Trip Duration'].sum()
    print('Total travel time :',total_travel)

    # TO DO: display mean travel time
    mean_travel =df['Trip Duration'].mean()
    print('Total travel time :',mean_travel)
    max_travel =df['Trip Duration'].max()
    print('Total travel time :',max_travel)
    print('Travel time for each user type:\n')
    # TO DO: display total travel time for each user type
    group_by_user_trip= df.groupby(['User Type']).sum()['Trip Duration']
    for index, user_trip in enumerate(group_by_user_trip):
        print(" {}: {} ".format(group_by_user_trip.index[index],user_trip))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    print('\n\n')

    # TO DO: Display counts of gender
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
        print('\n\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in(df.columns):
        year = df['Birth Year'].fillna(0).astype('int64')
        print(f'Earliest birth year is: {year.min()}\nmost recent is: {year.max()}\nand most common birth year is: {year.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    

    
def display_raw_data(city):
    """Ask the user if he wants to display the raw data and 5 rows at time."""
    
    print('\nRaw data is available to examine\n')
    raw = input('Would you like to examine 5 raw data? please enter [yes / no]: \n').lower()
   
    while raw == 'yes':
        try:
             for chunk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(chunk)
                raw = input('\nWould you like to examine 5 raw data once again? please enter [yes / no]: \n').lower() 
                if raw != 'yes':
                    print("\nThank's, I hope you had fun")
                    break 
             break
        except KeyboardInterrupt:
             print("Thank's")    

 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
