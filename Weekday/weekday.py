# program determining whether you can be happy based on the day of the week

import datetime

now = datetime.datetime.now()
day = now.weekday
weekend = (5,8)
dayname = {0:'Monday', 1:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}

if day == weekend:
    print ("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")
