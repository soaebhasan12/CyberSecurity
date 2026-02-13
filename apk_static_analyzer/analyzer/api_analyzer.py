# Detects Sensitive API usage.

SUSPICIOUS_CLASSES = [
  "Landroid/telephony/SmsManager",
  "Landroid/location/LocationManager"
]

def api_analysis(dx):
  findings = []
  
  for cls in SUSPICIOUS_CLASSES:
    for method in dx.find_method(classnam=cls):
      findings.append(str(method))
      
  return findings


"""
Concept: 
  Call graph scanning 
  API signature detection
"""