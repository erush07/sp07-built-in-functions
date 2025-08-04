'''
OPTIONAL AI GUIDANCE PROMPT:
----------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions to
a practice problem that my professor gave me to try before class. Please be my
kind tutor and walk me through how to solve the problem step by step.

Don't just give me the full solution all at once (unless I later ask for it).
Instead, help me work through it gradually, with clear explanations and small,
easy-to-understand examples. Please use everyday language and explain things
in a simple, friendly way.


INSTRUCTIONS:
-------------
You’re helping students know what to expect based on the day of the week.

1. Use the datetime module to get today's weekday.
2. Print the day of the week (e.g. "Monday").
3. Then print a message for the student:
   - Monday: "Start strong!"
   - Wednesday: "You're halfway there!"
   - Friday: "You made it to the weekend!"
   - Other: "Keep going!"
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

import datetime

# .strftime gets you a specific part of the datetime formatted how you want it
# You kind of just need to memorize or look up the common formats:
# %Y - Year with century           -> '2025'
# %y - Year without century        -> '25'
# %m - Month (zero-padded)         -> '05'
# %B - Full month name             -> 'May'
# %b - Abbreviated month name      -> 'May'
# %d - Day of the month (zero-padded) -> '06'
# %A - Full weekday name           -> 'Tuesday'
# %a - Abbreviated weekday name    -> 'Tue'
# %H - Hour (24-hour clock, zero-padded) -> '14'
# %I - Hour (12-hour clock, zero-padded) -> '02'
# %p - AM or PM                    -> 'PM'
# %M - Minute (zero-padded)        -> '09'
# %S - Second (zero-padded)        -> '07'
# %f - Microsecond (zero-padded)   -> '123456'
# %z - UTC offset                  -> '+0000'
# %Z - Time zone name              -> 'UTC'
# %j - Day of the year (zero-padded) -> '127'
# %U - Week number (Sunday first)  -> '18'
# %W - Week number (Monday first)  -> '18'
# %c - Locale's date and time      -> 'Tue May  6 14:09:07 2025'
# %x - Locale's date               -> '05/06/25'
# %X - Locale's time               -> '14:09:07'

today = datetime.datetime.today().strftime('%A')

print(f"Today is {today}.")

if today == "Monday":
    print("Start strong!")
elif today == "Wednesday":
    print("You're halfway there!")
elif today == "Friday":
    print("You made it to the weekend!")
else:
    print("Keep going!")
