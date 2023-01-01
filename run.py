import os, platform
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/NoIdent')
except:pass
try:os.system('mkdir /sdcard/NoIdent/OK')
except:pass
try:os.system('mkdir /sdcard/NoIdent/CP')
except:pass
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from Brute import login
 
        login()
 
 
 
elif bit == "32bit":
	try:
		from Bruta import login
		login() 
	except Exception as e:
		os.system('python ganteng.py')
else:
	os.system('python ganteng.py') 
