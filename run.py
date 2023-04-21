
import os
import subprocess

# check if pip is installed
try:
    subprocess.check_call(['pip', '--version'])
except subprocess.CalledProcessError:
    print("pip is not installed correctly. Most likely it is not added to path. Please re-install pip and python following these directions and try again: https://pip.pypa.io/en/stable/installation/.")
    exit(1)

# set the virtual environment directory path
venv_dir = os.path.join(os.getcwd(), 'venv')

# check if the virtual environment already exists
if not os.path.exists(venv_dir):
    print("Performing first time setup. This may take a few minutes...")
    # create virtual environment
    subprocess.check_call(['python', '-m', 'venv', venv_dir])
    print("Virtual environment created. Installing dependencies...")

    # activate the virtual environment
    if os.name == 'nt':  # for Windows
        activate_path = os.path.join(venv_dir, 'Scripts', 'activate.bat')
    else:  # for Linux/MacOS
        activate_path = os.path.join(venv_dir, 'bin', 'activate')
        
    subprocess.check_call(['cmd.exe', '/c', activate_path, '&&', 'pip', 'install', '-r', 'requirements.txt'])   
    

# activate the virtual environment
if os.name == 'nt':  # for Windows
    activate_path = os.path.join(venv_dir, 'Scripts', 'activate')
else:  # for Linux/MacOS
    activate_path = os.path.join(venv_dir, 'bin', 'activate')
    
# use Popen to start Django server and display output in real-time
    
    
print("Activating virtual environment...")
os.system( activate_path )

print("Starting django server...")
os.system("python manage.py runserver")