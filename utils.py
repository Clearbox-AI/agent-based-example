import random
from datetime import datetime, timedelta
from datetime import datetime


def generate_days(n):
    days = []
    date = datetime.today()
    while len(days) < n:
        if date.weekday() != 6: # Check if the day is not Sunday (Monday=0, Sunday=6)
            days.append(date.strftime('%d/%m/%Y'))
        date -= timedelta(days=1)
    return days[::-1] # Reverse the list to be chronologically ordered


distances = {
    'Brussels': {'Brussels': 0, 'Ghent': 56, 'Liege': 97},
    'Antwerp': {'Brussels': 43,'Ghent': 60, 'Liege': 126},
    'Ghent': {'Brussels': 56, 'Ghent': 0, 'Liege': 184},
    'Bruges': {'Brussels': 97, 'Ghent': 50, 'Liege': 218},
    'Liege': {'Brussels': 97, 'Ghent': 184, 'Liege': 0},
    'Leuven': {'Brussels': 24, 'Ghent': 89, 'Liege': 106},
    'Mechelen': {'Brussels': 24, 'Ghent': 89, 'Liege': 106},    
    'Namur': {'Brussels': 24, 'Ghent': 89, 'Liege': 106},    
    'Hasselt': {'Brussels': 24, 'Ghent': 89, 'Liege': 106},    
} 

def generate_random_time():
    # Generate a random time between 9:00 and 19:00
    hour = random.randint(9, 18)
    minute = random.randint(0, 59)
    return datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0)

def generate_datetime_string(date_str):
    # Parse the date string into a datetime object
    date = datetime.strptime(date_str, '%d/%m/%Y')
    
    # Generate a random time
    time = generate_random_time()
    
    # Combine the date and time into a datetime object
    datetime_obj = datetime(date.year, date.month, date.day, time.hour, time.minute)
    
    # Format the datetime object as a string in the desired format
    datetime_str = datetime_obj.strftime('%d/%m/%Y %H:%M')
    
    return datetime_str