## Task0
**Description**: The problem involves grabbing the first record from texts.csv and the last record from calls.csv, then producing an output in the following format:
First record of texts, 97424 22395 texts 90365 06212 at time 01-09-2016 06:03:22
Last record of calls, 98447 62998 calls (080)46304537 at time 30-09-2016 23:57:15, lasting 2151 seconds.

**Approach**: Accessed the first record from texts and the last record from calls, then extracted the required fields and formatted the output

**Complexity Analysis**:
- **Algorithm**: A function that takes the texts and calls data from their files, accesses the required records using their indexes, separates the records into incoming number, answering number, and time, and generates the required output using f-strings.
- **Big O Notation**: O(1), because the algorithm directly accesses the first record of texts and the last record of calls using their indexes without iterating through the arrays.
- **Justification**: The algorithm directly accesses only the first record of texts and the last record of calls using their indexes, so the number of operations does not depend on the size of the data.

## Task1
**Description**: The problem involves finding all the unique telephone numbers in both `texts.csv` and `calls.csv`, then counting the number of different telephone numbers and producing the required output.

**Approach**: Iterated through the records in both texts and calls, added the incoming and answering numbers to a set to avoid duplicates, then counted the unique numbers.

**Complexity Analysis**:

* **Algorithm**: A function that takes the texts and calls data, creates a set to store unique telephone numbers, iterates through both datasets, adds the incoming and answering numbers to the set, and returns the total number of unique telephone numbers.

* **Big O Notation**: O(n)

* **Justification**: The function iterates through the texts and calls records once. Since the number of iterations grows linearly with the number of records, the time complexity is O(n). The two loops are sequential rather than nested, so their complexities are added rather than multiplied.

## Task2
**Description**: The problem involves finding the telephone number that spent the longest total time on the phone during September 2016, including both the incoming and answering sides of each call.

**Approach**: Iterated through all the records in `calls.csv`, added the duration of each call to both the incoming and answering telephone numbers, then found the telephone number with the highest total time.

**Complexity Analysis**:

* **Algorithm**: A function that takes the calls data, creates a dictionary to store the total time spent by each telephone number, iterates through all calls and adds each call's duration to both numbers involved, then finds the telephone number with the maximum total time and returns the required output.

* **Big O Notation**: O(n)

* **Justification**: The function iterates through all call records once to calculate the total time for each telephone number. It then iterates through the stored telephone numbers to find the one with the longest total time. These operations are sequential rather than nested, so their complexities are added. Therefore, the overall time complexity is O(n).



## Task3
**Description**: The problem involves finding all the area codes and mobile prefixes called by people in Bangalore, whose telephone numbers start with `(080)`. It also requires calculating the percentage of calls from Bangalore fixed lines that are made to other Bangalore fixed lines.

**Approach**: Iterated through the call records and selected calls that were initiated by numbers starting with `(080)`. For Part A, identified the type of the answering number, extracted its area code or mobile prefix, and stored the codes in a set to avoid duplicates. The codes were then sorted in lexicographic order. For Part B, counted the total number of calls made from `(080)` numbers and the number of those calls that were made to other `(080)` numbers, then calculated the percentage.

**Complexity Analysis**:

* **Algorithm**: A function iterates through all call records to find calls made from Bangalore. For each matching call, it extracts the appropriate code from the answering number and stores it in a set. The resulting codes are then sorted and printed. A second function iterates through the calls to calculate the percentage of Bangalore-to-Bangalore calls.

* **Big O Notation**: O(n log n)

* **Justification**: The algorithm iterates through the call records, which takes O(n) time. For Part A, the unique codes are sorted using `sorted()`, which has a worst-case time complexity of O(n log n). Part B takes O(n) time because it requires a single pass through the call records. Since these operations are sequential, the overall complexity is dominated by the sorting operation, resulting in O(n log n).


## Task4


**Description**: The problem involves identifying telephone numbers that could be telemarketers. These are numbers that make outgoing calls but never send texts, receive texts, or receive incoming calls.

**Approach**: Created separate sets to store numbers that make outgoing calls, receive incoming calls, send texts, and receive texts. Iterated through the calls and texts to populate these sets. Then iterated through the outgoing call numbers and selected only the numbers that did not appear in the text sender, text receiver, or incoming call sets. Finally, sorted the possible telemarketers in lexicographic order and printed them.

**Complexity Analysis**:

* **Algorithm**: A function creates sets for outgoing calls, incoming calls, text senders, and text receivers. It iterates through the calls and texts to populate the sets, then checks each outgoing number against the other sets. The resulting possible telemarketers are sorted and returned.

* **Big O Notation**: O(n log n)

* **Justification**: The algorithm performs several sequential iterations over the calls and texts, each taking O(n) time. It then sorts the possible telemarketer numbers using `sorted()`, which has a worst-case time complexity of O(n log n). Since the sorting operation dominates the linear operations, the overall time complexity is O(n log n).
