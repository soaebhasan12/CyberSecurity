# Detects suspicious strings (URLs, IPs)

import re

def analyze_strings(dx):
  suspicious = []
  url_pattern = r"http[s]?://"
  
  for string in dx.get_strings():
    actual_string = string.get_value()
    if re.search(url_pattern, actual_string):
      suspicious.append(actual_string)
  
  return suspicious


"""
Concept: 
  Pattern matching 
  Data leakage detection
"""