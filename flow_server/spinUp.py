import subprocess
import time

subprocess.call(['python3', 'manage.py', 'initialize_db'])
interrupt_controller = subprocess.Popen(['python3', 'pin_interrupt_parent.py'])
#screen_controller = subprocess.Popen(['python3', 'screen_count.py'])
server = subprocess.Popen(['python3', 'manage.py', 'runserver', '192.168.86.29:8000'])

while(True):
    time.sleep(5)
