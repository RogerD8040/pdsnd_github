import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
Day_Data ={0:'Sunday',1: 'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
Month_Data = {1: 'January',2: 'February',3: 'March',4: 'April',5: 'May',6: "June",
              7: 'July',8: 'August',9:'Septmeber',10: 'October',11:'November',12:'December'}

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
    city = input("Would you like to see data for city chicago, new york, or washington?   ")
    date_type = input("Would you like to filter data by day, month, both, or no filter at all? Type \"none\" for no filter.   ")
    # get user input for month (all, january, february, ... , june)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if date_type == "day":
        day = input("Which day? Please type it in integer (note: 0=Monday,1=Tuesday 2=Wednesday... 6=Sunday)  ")
        month = "none"
    elif date_type == "month":
        month = "day"
        month = input("Which month? (1,2,3,4,5,6,7,8,9,10,11,12)")
    elif date_type == "both":
        month = input("Which month? (1,2,3,4,5,6,7,8,9,10,11,12)")
        day = input("Which day? Please type your response as an integer (note: 0=Monday,1=Tuesday 2=Wednesday... 6=Sunday)")
    elif date_type == "none":
        month = "none"
        day = "none"

    print('-'*40)
    return city.lower(), month,day


def load_data(city, day, month):
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
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    df['start_to_end_station'] = df['Start Station'] + ' to ' + df['End Station']

    if month != "none":
        if day != "none":
            df1 = df[(df['month'] == int(month)) & (df['weekday'] == int(day))]
        else:
            df1 = df[(df['month'] == int(month))]
    else:
        if day != "none":
            df1 = df[(df['weekday'] == int(day))]
        else:
            df1 = df
    return df1


def time_status(df1):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is: " + Month_Data[df1['month'].mode()[0]])

    # display the most common day of week
    print("The most common day is: " + df1['Start Time'].dt.weekday_name.mode()[0])

    # display the most common start hour
    print("The most common start hour is: " + str(df1['hour'].mode()[0]))
    print("\nIt tooks %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_status(df1):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common start station is: " + df1['Start Station'].mode()[0])

    # display most commonly used end station
    print("The most common end station is: " + df1['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("The most common trip is: " + df1['start_to_end_station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_status(df1):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is: " + str(df1['Trip Duration'].sum()))

    # display mean travel time
    print("Mean travel time is: " + str(df1['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_status(df1,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:")
    print(df1['User Type'].value_counts())
    print("")

    if city != 'washington':
        print("Counts of gender :\n",df1['Gender'].value_counts())
        print("")
        print("The earliest year of birth: " + str(int(df1['Birth Year'].min())))
        print("The most Recent year of birth: " + str(int(df1['Birth Year'].max())))
        print("The most common year of birth: " + str(int(df1['Birth Year'].mode()[0])))
    else:
        print("There is no \'gender\' and \'birth year\' data for Washington!!!")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def print_dataset(city, month, day):
    if month == "none":
        if day == "none":
            print("City: ", city, " Month: none", " Day: none")
        else:
            print("City: ", city, " Month: none", " Day: ", Day_Data[int(day)])
    else:
        if day == "none":
            print("City: ", city, " Month: ", Month_Data[int(month)], " Day: none")
        else:
            print("City: ", city, " Month: ", Month_Data[int(month)], " Day: ", Day_Data[int(day)])

def display_data(df1):
    pd.set_option('display.max_columns', None)# configuration to show all columns
    start_index = 0
    feedback = input("Would you like to see the first 5 rows of data? Enter yes or no.")
    while feedback == "yes":
        print('-' * 40)
        print(df1.iloc[start_index:(start_index + 5)])
        print('-' * 40)
        start_index += 5
        feedback = input("Would you like to see next 5 rows of data? Enter yes or no.")

def main():
    while True:
        city, month, day = get_filters()
        print_dataset(city, month, day)
        df1 = load_data(city, month, day)
        if df1.shape[0] > 0:
            time_status(df1)
            print_dataset(city, month, day)
            station_status(df1)
            print_dataset(city, month, day)
            trip_duration_status(df1)
            print_dataset(city, month, day)
            user_status(df1, city)
            display_data(df1)
        else:
            print("\nThere is no data for the current filtering!!!")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

    