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

def diffrent_telephone_numbers(texts,calls):
    all_numbers = set()
    
    for text in texts:
        all_numbers.add(text[0])
        all_numbers.add(text[1])
    
    for call in calls:
        all_numbers.add(call[0])
        all_numbers.add(call[1])
    return len(all_numbers)    

count = diffrent_telephone_numbers(texts, calls)
print(f"There are {count} different telephone numbers in the records.")    
        
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
