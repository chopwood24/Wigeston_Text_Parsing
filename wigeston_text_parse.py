#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd

# Function to extract entries based on the entry number
def extract_entries_fixed(text):
    entries = []
    last_entry_num = 0  # Initialize variable to keep track of last entry number

    for match in re.finditer(r'(?:\n|^)(\d+)\.', text):
        entry_num = int(match.group(1))  # Convert matched entry number to integer

        if entry_num > last_entry_num:
            entries.append(match.start())  # Store the start index of this entry
            last_entry_num = entry_num  # Update the last entry number

    entry_texts = [text[start:end].strip() for start, end in zip(entries, entries[1:] + [None])]
    
    return entry_texts

# Function to extract details from each entry
def extract_details_hyphen_linebreak_refined(entry_text):
    details = {
        'entry_number': None,
        'date': None,
        'location': None,
        'description': None
    }
    
    # Extract entry number
    entry_number_match = re.search(r'^\d+', entry_text)
    if entry_number_match:
        details['entry_number'] = entry_number_match.group()
    
    # Extract date (first 60 characters after entry number)
    start_date = len(details['entry_number']) + 1  # 1 for the period following the entry number
    details['date'] = entry_text[start_date:start_date + 60].strip()
    
    # Attempt to extract location within a specific range (e.g., within 100 characters after the date)
    # Now allowing hyphenated words that could be broken across lines
    location_match = re.search(r'(?:\]|\.)\s+([a-zA-Z-\s]{4,})\.', entry_text[start_date:start_date + 100])
    
    if location_match:
        # Remove potential line breaks and extra spaces
        details['location'] = re.sub(r'\s+', '', location_match.group(1))
        end_location = location_match.end()
    else:
        details['location'] = 'NA'
        end_location = start_date + 60  # End of the date sentence
    
    # Extract description (rest of the entry)
    details['description'] = entry_text[end_location:].strip()
    
    return details

# Read the text file
with open('path_to_text_file', 'r') as f:
    sample_text = f.read()

# Extract entries
sample_entries_fixed = extract_entries_fixed(sample_text)

# Extract details from each entry and create a DataFrame
all_details_hyphen_linebreak_refined = [extract_details_hyphen_linebreak_refined(entry) for entry in sample_entries_fixed]
df_hyphen_linebreak_refined = pd.DataFrame(all_details_hyphen_linebreak_refined)

# Export the DataFrame to a CSV file
output_csv_path_hyphen_linebreak_refined = 'path_to_output_csv_file'
df_hyphen_linebreak_refined.to_csv(output_csv_path_hyphen_linebreak_refined, index=False)

