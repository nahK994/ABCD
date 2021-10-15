import os

os.chdir('Auth')
os.system("gnome-terminal -e 'bash -c \"python3 manage.py runserver 127.0.0.1:8000; bash\" '")

os.chdir('../TeacherCommand')
os.system("gnome-terminal -e 'bash -c \"python3 manage.py runserver 127.0.0.1:8002; bash\" '")
os.system("gnome-terminal -e 'bash -c \"python3 manage.py runscript eventConsumer; bash\" '")

os.chdir('../TeacherQuery')
os.system("gnome-terminal -e 'bash -c \"python3 manage.py runserver 127.0.0.1:8001; bash\" '")
os.system("gnome-terminal -e 'bash -c \"python3 manage.py runscript eventConsumer; bash\" '")

os.chdir('../Frontend')
os.system("gnome-terminal -e 'bash -c \"ng serve; bash\" '")

print("done")

# https://stackoverflow.com/questions/43332703/open-terminal-run-command-python


# 8000 ==> Auth
# 8001 ==> TeacherQuery
# 8002 ==> TeacherCommand