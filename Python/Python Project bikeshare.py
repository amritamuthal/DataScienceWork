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
    def choice(prompt, choices=('y', 'n')):
    """Return a valid input from the user given an array of possible answers.
    """
    
    while
        while True:
        choice = input(prompt).lower().strip()
        
        if choice == 'end':
            raise SystemExit
        
        elif ',' not in choice:
            if choice in choices:
                break
        
        elif ',' in choice:
            choice = [i.strip().lower() for i in choice.split(',')]
            if list(filter(lambda x: x in choices, choice)) == choice:
                break

        prompt = ("\nError\n")

    return choice

def get_filters():
    
    Returns:
        (str) city - name of the city(ies) to analyze
        (str) month - name of the month(s) to filter
        (str) day - name of the day(s) of week to filter
    
    while True:
        city = choice("\nSelect city\n>", CITY_DATA.keys())
        month = choice("\nSelect month\n>", months)
        day = choice("\nSelect weekday\n>", weekdays)

     
        confirmation = choice("\nPlease confirm\n>" .format(city, month, day))
        if confirmation == 'y':
            break
        else:
            print("\nLet's try this again!")

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
 print("\nLoading.")
    start_time = time.time()

    # filter the data according to the selected city filters
    if isinstance(city, list):
        df = pd.concat(map(lambda city: pd.read_csv(CITY_DATA[city]), city),
                       sort=True)
        # reorganize DataFrame columns after a city concat
        try:
            df = df.reindex(columns=['Unnamed: 0', 'Start Time', 'End Time',
                                     'Trip Duration', 'Start Station',
                                     'End Station', 'User Type', 'Gender',
                                     'Birth Year'])
        except:
            pass
    else:
        df = pd.read_csv(CITY_DATA[city])

    # create columns to display statistics
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour

    # filter the data according to month and weekday into two new DataFrames
    if isinstance(month, list):
        df = pd.concat(map(lambda month: df[df['Month'] ==
                           (months.index(month)+1)], month))
    else:
        df = df[df['Month'] == (months.index(month)+1)]

    if isinstance(day, list):
        df = pd.concat(map(lambda day: df[df['Weekday'] ==
                           (day.title())], day))
    else:
        df = df[df['Weekday'] == day.title()]

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['Month'].mode()[0]
    print('most common month: ' + str(months[most_common_month-1]).title() + '.')

    # display the most common day of week

    most_common_day = df['Weekday'].mode()[0]
    print('most common day of the week: ' + str(most_common_day) + '.')

    # display the most common start hour
    
    most_common_hour = df['Start Hour'].mode()[0]
    print('most common start hour: ' + str(most_common_hour) + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = str(df['Start Station'].mode()[0])
    print("most common start station: " + most_common_start_station)

    # TO DO: display most commonly used end station

    most_common_end_station = str(df['End Station'].mode()[0])
    print("most common start end: " + most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

     df['Start-End Combination'] = (df['Start Station'] + ' - ' + df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination'] .mode()[0])
    print("most common start-end combination " + most_common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = (str(int(total_travel_time//86400)) +
                         'd ' +
                         str(int((total_travel_time % 86400)//3600)) +
                         'h ' +
                         str(int(((total_travel_time % 86400) % 3600)//60)) +
                         'm ' +
                         str(int(((total_travel_time % 86400) % 3600) % 60)) +
                         's')
    print('total travel time: ' + total_travel_time + '.')

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')
    print("mean travel time: " + mean_travel_time + ".")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts().to_string()
    print("user types:")
    print(user_types)

    # TO DO: Display counts of gender

    try:
        gender_distribution = df['Gender'].value_counts().to_string()
        print("\nDistribution for each gender:")
        print(gender_distribution)
    except KeyError:
        print("There is no data of user genders for {}." .format(city.title()))

    # TO DO: Display earliest, most recent, and most common year of birth
 try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nFor the selected filter, the oldest person to ride one "
              "bike was born in: " + earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("For the selected filter, the youngest person to ride one "
              "bike was born in: " + most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("For the selected filter, the most common birth year amongst "
              "riders is: " + most_common_birth_year)
    except:
        print("no data of birth year for {}."
              .format(city.title()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
