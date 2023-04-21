
import os
import subprocess

# check if pip is installed
try:
    subprocess.check_call(['pip', '--version'])
except subprocess.CalledProcessError:
    print("pip is not installed. Please install pip and try again.")
    exit(1)

venv_name = os.environ.get('VIRTUAL_ENV')
venv_dir = os.path.join(os.getcwd(), 'venv')

print(venv_name)
if venv_name != venv_dir:
    # check if the virtual environment already exists
    if not os.path.exists(venv_dir):
        # create virtual environment
        subprocess.check_call(['python', '-m', 'venv', venv_dir])
        
    # Prompt user to load venv
    if os.name == 'nt':  # for Windows
        activate_path = os.path.join(venv_dir, 'Scripts', 'activate.bat')
    else:  # for Linux/MacOS
        activate_path = "source bin/activate"
    print()
    print("You need to activate the virtual environment before running the server.")
    print("Do this by Running the following command: " + activate_path)
    print("Once the environment is loaded, run the run.py file again.")


else:    
    # activate the virtual environment and install the requirements
    os.system('pip install -r requirements.txt')
    os.system("python manage.py runserver")
