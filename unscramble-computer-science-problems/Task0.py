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

def main(text,call):  
    first_text = texts[0]
    last_call = calls[-1]
    
    text_incoming = first_text[0]
    text_answering = first_text[1]
    text_time = first_text[2]
    first_text_output = f"First record of texts, {text_incoming} texts {text_answering} at time {text_time}"
    
    call_incoming = last_call[0]
    call_answering = last_call[1]
    call_time = last_call[2]
    call_duration = last_call[3]
    last_call_output = f"Last record of calls, {call_incoming} calls {call_answering} at time {call_time}, lasting {call_duration} seconds"

    return first_text_output, last_call_output

first_text, last_call = main(texts, calls)

print(first_text)
print(last_call)



    

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

