from subprocess import call

# the main programm opens
call(["python", './authentification/request.py'])

print("print help to list comands")
print()

call(['python', './python/keywordRequest.py'])
