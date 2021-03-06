import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wa': 'washington.csv' }

def get_filters():
    """
    Asks user to input a city, month, and day to analyze.

    Returns:
        city - city name to analyze
        month - month name to filter by, or "all" to select all months (6)
        day - day of week name to filter by, or "all" to select all days of week
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user's input for the city to analyze (chicago, new york , washington). 
    city = input("\nWhich city you wish to inspect? Please type ch for Chicage or ny for New York or wa for Washington \n").lower()

    #City validaton for user inpiut
    while city not in CITY_DATA.keys():
        print("Sorry! This is not a city name. Try again please")
        
    # Ask for the city again    
        city = input("\nWhich city you wish to inspect? Please type ch for Chicage or ny for New York or wa for Washington \n").lower()
    
    # Get user input for months (all, jan, feb, mar, apr, may,jun)
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
    month = input("\nWhich month you wish to inspect? Please type Jan, Feb, Mar, Apr, May or Jun or all \n").lower()

    #Month validaton for user inpiut
    
    while month not in months:
        print("Sorry! This is not a correct month. Try again please")
        
    # Ask for the month again    
        month = input("\nWhich month you wish to inspect? Please type Jan, Feb, Mar, Apr, May or Jun or all \n").lower()

    # Get user input for day of week (all, sat, sun, mon, tue, wed, thu)
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'all']
    day = input("\nWhich day you wish to inspect? Please type Sat, Sun, Mon, Tue, Wed, Thu, Fri, or all \n").lower()

    #Day validaton for user inpiut
    
    while day not in days:
        print("Sorry! This is not a correct day. Try again please")
        
    # Ask for the day again    
        day = input("\nWhich day you wish to inspect? Please type Sat, Sun, Mon, Tue, Wed, Thu, Fri, or all \n").lower()


    print('-'*40)
    return city, month, day

def load_data(city, month,day):
    #read data and put into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    """
    Loads the data for the selected city and then filters by month and day (if applicable).

    Args:
        city - city name to analyze
        month - month name to filter by, or "all" to select all months (6)
        day - day of week name to filter by, or "all" to select all days of week
    Returns:
        Pandas DataFrame (df) which contains the city data filtered by month and day
    """

    # converts the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract the month & day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        
        # filtering by month to create the new dataframe
        df = df[df['month'].str.startswith(month.title())]
        
        # filtering by day of week (if applicable)
    if day != 'all':
        # filtering by day of week to create the new dataframe
        df = df[df['day_of_week'].str.startswith(day.title())]
    

    return df
    
    
def time_stats(df):
    """Grab the stats of the most frequent times people travel"""

    print('\nFetching The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Displays the most common month
    popular_month = df['month'].mode()[0]
    print('The Most Common Month is:', popular_month)
          

    # Displays the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The Most Common Day is:', popular_day)
          
    # Displays the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The Most Common hour is:', popular_hour)

    print("\nThis process took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Shows the stats for the most popular stations & trip"""

    print('\nFetching The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Shows the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The Most Commonly used start station is:', common_start_station)

    # Shows the most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The Most Commonly used end station is:', common_end_station)
    
    # Shows the most frequent combination of start station and end station trip
    comb_station = (df["Start Station"] + "-" + df["End Station"]).mode()[0]
    print('The Most Common Used Combination of (start + end station) is:', comb_station)
     
    print("\nThis process took %s seconds." % (time.time() - start_time))
    print('-'*40)    
      
def trip_duration_stats(df):
    """Shows the stats for the total and average trip duration"""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total Travel Time in (Seconds):', total_travel_time)                    

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The Mean Travel Time in (Seconds):', mean_travel_time)                     

    print("\nThis process took %s seconds." % (time.time() - start_time))
    print('-'*40)        
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types 
    count_user_types = df['User Type'].value_counts()
    print('The count of user types are:', count_user_types)

    # Display counts of gender - Chicago and New York ONLY were having Gender column
    try:
        gender_counts = df['Gender'].value_counts()
        print('The count of gender types are:', gender_counts)
    
    # Displays the earliest, the most recent, and most common year of birth
    # Chicago and New York ONLY were having Birth Year column
    
        earliest_year = df['Birth Year'].min()
        print('Earliest Year of Birth is:', earliest_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year of Birth is:', most_recent_year)
        common_year = df['Birth Year'].mode()[0]
        print('Most Common Year of Birth is:', common_year)
        
    except KeyError:
      print('Sorry, Gender & Birth year data is not available for Washington')
        
    print("\nThis process took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def ask_for_raw_data(city):
    """Shows rows of data according to user's request"""
        
    user_answer = input("Do you want to see more & check out the 1st five rows of raw data? Y/N \n").lower()
    while user_answer == 'y':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize = 5): #Pulls the first 5 rows of data
                print (chunk)
                
                user_answer = input("Do you want to see 5 more rows of the data? Y/N \n").lower() #Asks if user want more data
                if user_answer != 'y':
                    print('Bye for now')
                    break #end the asking for data loop
            break        
        except KeyboardInterrupt:
            print('Bye')
                                     
      
        
def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
       

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_for_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()    
    