import os
os.system('git pull')

if __name__ == "__main__":
        try:
                __import__("cr1").login()
        except Exception as e:
                exit(str(e))