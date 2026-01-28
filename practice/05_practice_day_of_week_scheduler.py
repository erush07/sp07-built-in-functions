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

from datetime import datetime

now = datetime.now().isoweekday()

if now == 1:
    print("Today is Monday. Start strong!")
elif now == 2:
   print("Today is Tuesday. Keep going!")
elif now == 3:
   print("Today is Wednesday. You're halfway there!")
elif now == 4:
   print("Today is Thursday. Keep going!")
elif now == 5:
   print("Today is Friday. You made it to the weekend!")
elif now == 6:
   print("Today is Sunday. Keep going!")
else:
   print("Today is Sunday. Keep going!")
   