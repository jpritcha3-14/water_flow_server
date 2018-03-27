import subprocess
import time

ip_address = '192.168.86.29'
port = '8000'

subprocess.call(['python3', 'manage.py', 'initialize_db'])
interrupt_controller = subprocess.Popen(['python3', 'pin_interrupt_parent.py'])
screen_controller = subprocess.Popen(['python3', 'screen_count.py'])
server = subprocess.Popen(['python3', 'manage.py', 'runserver', ip_address + ':' + port])

while(True):
    time.sleep(5)
