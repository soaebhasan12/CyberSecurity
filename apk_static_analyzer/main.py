from analyzer.permission_analyzer import analyze_permissions
from analyzer.string_analyzer import analyze_strings
from analyzer.api_analyzer import api_analysis
from analyzer.apk_loader import load_apk
from analyzer.report_generator import generate_report
from pathlib import Path


def main():
  file_path = Path("D:/16 IITR INTERNSHIP/01 CyberSecurity GitHub Repository/CyberSecurity/apk_static_analyzer/reports/TEST_2.apk")
  
  a, d, dx = load_apk(file_path)
  
  report = {
    "dangerous_permissions": analyze_permissions(a),
    "suspicious_strings": analyze_strings(dx),
    "suspicious_api_usage": api_analysis(dx)
  }
  
  generate_report(report, "reports/output.json")
  

if __name__ == "__main__":
  main()