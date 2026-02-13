# Responsibility: Detects dangerous permissions used by the app

DANGEROUS_PERMISSIONS = [ "android.permission.SEND_SMS", 
                         "android.permission.READ_SMS", 
                         "android.permission.RECORD_AUDIO", 
                         "android.permission.ACCESS_FINE_LOCATION" 
                         ]

def analyze_permissions(apk_obj):
  found = []
  
  permissions = apk_obj.get_permissions()
  
  for perm in permissions:
    if perm in DANGEROUS_PERMISSIONS:
      found.append(perm)
  
  return found

"""
Concept used: 
  Static metadata analysis 
  Security rule matching
"""