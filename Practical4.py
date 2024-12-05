import os
import stat
import time

def print_file_lekhka_jokha(file_name):
  file_details = os.stat(file_name)
  file_permission = stat.filemode(file_details.st_mode)
  file_acces_time = time.ctime(file_details.st_atime)

  print(file_details)
  print(file_permission)
  print(file_acces_time)
  
print_file_lekhka_jokha('example.txt')