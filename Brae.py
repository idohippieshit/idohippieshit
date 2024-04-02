# time_module.py
from datetime import datetime

def display_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("CurrentTime:", current_time)

    if __name__ == "__main__":
        display_time(0900) 
          #gpt psated ahead
        
     # time_module.py
from datetime import datetime

def display_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time:", current_time)

if __name__ == "__main__":
    display_time()
   