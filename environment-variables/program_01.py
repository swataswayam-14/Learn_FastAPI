import os
name = os.getenv("MY_NAME", "WORLD")
print(f"Hello {name} from python")

#  MY_NAME="Swayam" python program_01.py

# when we install python , PATH environment variable
# /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/custompython/bin
# This way, when we type python in the terminal, the system will find the Python program in /opt/custompython/bin (the last directory) and use that one.

# The system will find the python program in /opt/custompython/bin and run it.