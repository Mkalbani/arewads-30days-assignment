"""
Day 16: 30 Days of python programming
"""

# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime, timedelta
current_date = datetime.now()
current_day = current_date.day
current_month = current_date.month
current_year = datetime.now().year
current_timestamp = datetime.now().timestamp()

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = current_timestamp.strftime("%m/%d/%Y, %H:%M:%S")

# Today is 5 December, 2019. Change this time string to time.
time_string = "5 December, 2019"
changed_time = datetime.strptime(time_string, "%d %B, %Y")
# Calculate the time difference between now and new year.
new_year = datetime(current_year + 1, 1, 1)
time_till_new_year = new_year - current_date

# Calculate the time difference between 1 January 1970 and now.
time_diff = datetime(1970, 1, 1)
time_since_time_diff = current_date - time_diff
#
#Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
# Age Calculation App
# Handling timezone information
# Logging and Logout Information
# Creating schedules
# Surveliance purposes