# Detects suspicious strings (URLs, IPs)

import re

def analyzer_strings(dx):
  suspicious = []
  url_pattern = r"http[s]?://"
  
  for string in dx.get_strings():
    if re.search(url_pattern, string):
      suspicious.append(string)
  
  return suspicious


"""
Concept: 
  Pattern matching 
  Data leakage detection
"""