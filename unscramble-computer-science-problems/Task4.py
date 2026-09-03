"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def Possible_telemarketers(texts,calls):
    outgoing_calls = set()
    text_senders = set()
    text_receivers = set()
    incoming_calls = set()
    
    for call in calls:
        outgoing_calls.add(call[0])
        incoming_calls.add(call[1])
    for text in texts:
        text_senders.add(text[0])
        text_receivers.add(text[1])    
    possible_telemarketers = set()

    for number in outgoing_calls:
        if number not in text_senders and number not in text_receivers and number not in incoming_calls:
            possible_telemarketers.add(number)    
    return sorted(possible_telemarketers)
telemarketers = Possible_telemarketers(texts, calls)

print("These numbers could be telemarketers:")
for number in telemarketers:
    print(number)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

