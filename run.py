import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/NoIdent')
except:pass
try:os.system('mkdir /sdcard/NoIdent/OK')
except:pass
try:os.system('mkdir /sdcard/NoIdent/CP')
except:pass
if __name__ == "__main__":
        try:
                __import__("Brute").login()
        except Exception as e:
                exit(str(e))
