import tkinter as tk
import time
import pyautogui as pgui
from pynput.keyboard import Key, Listener
pgui.PAUSE=1  
    
time = 12
p1 = pgui.position() #x
p2 = pgui.position() #quick connects
p3 = pgui.position() #call

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.enter:
        pgui.click(p1)   #x button
        pgui.click(p2)  #Quick Connects button
#         pgui.scroll(-5000)
        pgui.click(p3)   #call 
#         pgui.moveTo(p1)   #x button
#         pgui.moveTo(p2)  #Quick Connects button
#         pgui.moveTo(p3)   #call 
    else:
        return False

def mvmnt():
    # Collect events until released
    with Listener(on_release=on_release) as listener:
        print("listening")
        status = listener.join()
        print("not listening")

class HomeWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master, background="bisque")
        self.master.title("autoTranferInator")
        
        self.startprompt=tk.StringVar()
        self.startprompt.set('Press the button below to start recording positions')
        self.label_text2 = tk.Label(self.frame, textvariable=self.startprompt)
        self.label_text2.pack()
        
        self.button1 = tk.Button(self.frame, text = 'Start recording positions', width = 20, command = self.new_window)
        self.button1.pack()
        self.frame.pack()
        
    def cntdwn(self):
        print("test")

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

class Demo2:
    def cntdwn1(self):    
        global time
        global p2
        time-=1 
        self.prompt.set("recording location of quick connects button in: " +str((time%3)+1)) 
        p2 = pgui.position()
        
    def cntdwn2(self):    
        global time
        global p3
        time-=1 
        self.prompt.set("recording location of call button in: " +str((time%3)+1)) 
        p3 = pgui.position()
    
    def cntdwn3(self):    
        global time
        global p1
        time-=1 
        self.prompt.set("recording location of x button in: " +str((time%3)+1)) 
        p1=pgui.position()
        
    def rdy(self):
        print(p2)
        print(p3)
        print(p1)
        self.prompt.set("Recording finished. Press enter to redial. Press any key, then close the window to rerecord")
    
    def __init__(self, master):
        global time
        time = 12
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("autoTranferInator")
        
        self.prompt=tk.StringVar()
        self.prompt.set('Recording mouse position momentarily..')
        self.label_text2 = tk.Label(self.frame, textvariable=self.prompt)
        self.label_text2.pack()
        
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
        
        for i in range(1,4):
            self.master.after(i*1000, self.cntdwn1)
        for i in range(4,7):
            self.master.after(i*1000, self.cntdwn2)
        for i in range(7,11):
            self.master.after(i*1000, self.cntdwn3)
        self.master.after(11100, self.rdy)
        self.master.after(11200, mvmnt)


    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = HomeWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()