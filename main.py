from subprocess import call

# the main programm opens
print("print help to list comands")
print()

while True: # main cycle
    call(['python', './python/request.py'])
