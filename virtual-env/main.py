print("Hello World")

# source .venv/bin/activate : activating a virtual environment
# checking : which python
# desctivating the virtual env : deactivate , we can use this command wherever we are , when activating the virtual env for another project , we have to go to that directory and : ".venv/bin/activate"

# Activating a virtual environment adds its path .venv/bin (on Linux and macOS) 
# before activating the PATH variable looked like : "/usr/bin:/bin:/usr/sbin:/sbin"
#that means the system would look for programs in : "/usr/bin:/bin:/usr/sbin:/sbin"

# after activating venv , the PATH variable would be : "/home/user/code/awesome-project/.venv/bin:/usr/bin:/bin:/usr/sbin:/sbin"
# So, when you type python in the terminal, the system will find the Python program in
# : "/home/user/code/awesome-project/.venv/bin/python" and use that one

# locking : being able to run your project in production exactly the same as in your computer while developing.