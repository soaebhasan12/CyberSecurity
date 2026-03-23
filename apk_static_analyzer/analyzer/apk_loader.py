# Responsibility: loads APK file and return objects

from androguard.misc import AnalyzeAPK


def load_apk(file_path):
    a, d, dx = AnalyzeAPK(file_path)
    return a, d, dx
