import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/4MBF-DATA')
except:pass
try:os.system('mkdir OK')
except:pass
try:os.system('mkdir CP')
except:pass
if __name__ == "__main__":
        try:
                __import__("Brute").login()
        except Exception as e:
                exit(str(e))
