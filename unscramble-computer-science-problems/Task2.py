"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def get_total_time(calls):
    total_time = {}

    for call in calls:
        incoming_call = call[0]
        answering_call = call[1]
        duration = int(call[3])

        total_time[incoming_call] = total_time.get(incoming_call, 0) + duration
        total_time[answering_call] = total_time.get(answering_call, 0) + duration

    longest_number = max(total_time, key=total_time.get)
    longest_time = total_time[longest_number]

    return f"{longest_number} spent the longest time, {longest_time} seconds, on the phone during September 2016."


result = get_total_time(calls)
print(result)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

