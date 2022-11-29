from collections import defaultdict
import re

file_name = 'events.log'
pattern_datetime = re.compile('\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).+\]')
date_by_counter = defaultdict(int)

with open(file_name) as file:
    for line in file:
        if 'NOK' not in line:
            continue

        match = pattern_datetime.search(line)
        if match:
            date_str = match.group(1)
            date_by_counter[date_str] += 1

for k, v in date_by_counter.items():
    print(f'[{k}] {v}')