import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    
    date_object = datetime.strptime(iso_string, "%Y-%m-%d")
    readable_date = f"{date_object: %A %d %B %Y}"
    return readable_date

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    celcius_temp = (temp_in_fahrenheit - 32) * 5/9
    return f"The temperature is {round (celcius_temp, 1)} °C"


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    if not weather_data:
        return 0.0
    
    total_sum = sum(weather_data)
    count = len(weather_data)
    mean_value = total_sum / count
    return float(mean_value)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data = []
    # csv_file = "tests/data/example_one.csv"
    with open(csv_file, mode="r", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
            return data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. 
        (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return (None, None)
    min_value = min(weather_data)
    last_index = None
    for i in range(len(weather_data)):
        if weather_data[i] == min_value:
            last_index = i
    return (min_value, last_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. 
        (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if not weather_data:
        return (None, None)
    max_value = max(weather_data)
    last_index = None
    for i in range(len(weather_data)):
        if weather_data[i] == max_value:
            last_index = i
    return (max_value, last_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


