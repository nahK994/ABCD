import subprocess as sp
import os
import multiprocessing as mp

# def runFrontend():
#     os.chdir('Frontend')
#     print(os.getcwd())
#     sp.call(['ng', 'serve'])

# def runAuth():
#     os.chdir('Auth')
#     print(os.getcwd())
#     sp.call(['python3', 'manage.py', 'runserver'])

# p1 = mp.process(target=runFrontend)
# p2 = mp.process(target=runAuth)

# p1.run()
# p2.run()

# p1.join()
# p2.join()

#sp.run(['cd Frontend/'])
#os.chdir('Frontend')
#print(os.getcwd())
#sp.call(['ng', 'serve'])
#os.chdir('../TeacherQuery')
#print(os.getcwd())
#sp.run(['python3', 'manage.py', 'runserver'])


# 8000 ==> Auth
# 8001 ==> TeacherQuery
# 8002 ==> TeacherCommand