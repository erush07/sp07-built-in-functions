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
You are designing a name tag generator for a conference.

1. Ask the user for their first name.
2. Ask the user for their last name.
3. Print their name in this format: "LAST, First"
   (last name should be uppercase, first name should be capitalized)
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

first = input("Enter your first name: ")
last = input("Enter your last name: ")

print(f"{last.upper()}, {first.capitalize()}")
