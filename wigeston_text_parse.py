#!/usr/bin/env python
# coding: utf-8

# In[19]:


import re
import pandas as pd

# Function to extract entries based on the entry number
def extract_entries(text):
    entries = []
    last_entry_num = 0
    for match in re.finditer(r'(?:\n|^)(\d+)\.', text):
        entry_num = int(match.group(1))
        if entry_num > last_entry_num:
            entries.append(match.start())
            last_entry_num = entry_num
    entry_texts = [text[start:end].strip() for start, end in zip(entries, entries[1:] + [None])]
    return entry_texts

# Function to extract details from each entry
def extract_details(entry_text):
    details = {
        'entry_number': None,
        'date': None,
        'location': None,
        'description': None
    }
    entry_number_match = re.search(r'^\d+', entry_text)
    if entry_number_match:
        details['entry_number'] = entry_number_match.group()
    start_date = len(details['entry_number']) + 1
    details['date'] = entry_text[start_date:start_date + 60].strip()
    location_match = re.search(r'(?:\]|\.)\s+([a-zA-Z-\s]{4,})\.', entry_text[start_date:start_date + 100])
    if location_match:
        details['location'] = re.sub(r'\s+', '', location_match.group(1))
        end_location = location_match.end()
    else:
        details['location'] = 'NA'
        end_location = start_date + 60
    details['description'] = entry_text[end_location:].strip()
    return details

# Read the text file
with open('path_to_text_file', 'r') as f:
    sample_text = f.read()

# Extract entries
sample_entries = extract_entries(sample_text)

# Extract details from each entry and create a DataFrame
all_details = [extract_details(entry) for entry in sample_entries]
df = pd.DataFrame(all_details)

# Export the DataFrame to a CSV file
output_csv_path = 'path_to_output_csv_file'
df.to_csv(output_csv_path, index=False)


