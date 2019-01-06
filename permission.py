import os
import subprocess

subprocess.call(['chmod', '+x', '/home/abhijit/atom_projects/test_capture.py'])
os.chmod('/home/abhijit/atom_projects/test_capture.py', 0o777)
os.chmod('/home/abhijit/atom_projects/test_capture.py', 0o755)
os.chmod('/home/abhijit/atom_projects/test_capture.py', 0o744)
