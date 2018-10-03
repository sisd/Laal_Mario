import os 
import sys
import termios
import atexit
import time
from select import select

class Input:
    def __init__(self):
        if os.name == 'nt':
            pass
        else:
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)
            atexit.register(self.set_normal_term)
    def set_normal_term(self):
        if os.name == 'nt':
            pass
        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    def getch(self):
        s = ''
        if os.name == 'nt':
            return msvcrt.getch().decode('utf-8')
        else:
            return sys.stdin.read(1)

    def input(self):
        if os.name == 'nt':
            return msvcrt.input()
        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []   
'''ino = Input()
while True:
    if ino.input():
        cin=ino.getch()
        print(cin)
    else:
        print("hi")
        time.sleep(0.1)
ino.set_normal_term()'''