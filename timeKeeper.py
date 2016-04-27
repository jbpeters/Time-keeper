#! /usr/bin/python3

from tkinter import *
#Tk,Button,Frame,Entry,BOTH,Toplevel
import sys
import time
import datetime as dt

def time_str_to_d_day(T_string):
    try:
        hours, minutes,seconds = T_string.split(':')
    except ValueError:
            return -1
    return str(int(hours)/(24.0)+int(minutes)/(24.0*60) + int(seconds)/(24.0*60*60))
                                                    

class TimeClock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self,parent, *args, **kwargs)        
        self.e=Entry(self,text='Message',font=("times",16))
        self.e.delete(0,"end")
        self.e.pack()        
        self.makebuttons()
        self.pack( expand='true', fill='x')
        
    
    def makebuttons(self):
        self.b1 = Button(self, text="Tock" ,font=("times",16),
                         bg='BLUE', activebackground="Blue",
                         activeforeground='White',fg='white',
                         height='2', width='8' , command = self.write )
        self.b2 = Button(self, text="Tick", font=("times",16),
                         activebackground='red', bg='red', 
                         activeforeground='White',fg='white',
                         command = self.quit )        
        self.b1.pack(side='right', fill='both')
        self.b2.pack(side='left', fill='both')
        self.lastTime = ""
        self.start_timer()

    def start_timer(self):
        def callback():
            #self.message=self.e.delete(0,"end")
            self.message=self.e.get()
            print( "input text is equal to->",self.message)
            root.title(self.message+":TIMER")
            #self.e.destroy()
            self.B.destroy()            
        self.B= Button(self,text='start', font=("times",16), command=callback)
        self.B.pack()
        t=time.localtime()
        self.zeroTime = dt.timedelta(hours=t[3], minutes=t[4], seconds=t[5])
        self.tick()
        
    def tick(self):
        self.now = dt.datetime(1, 1, 1).now()
        elapsedTime = self.now - self.zeroTime
        time2 = elapsedTime.strftime('%H:%M:%S')
        if time2 != self.lastTime:
            self.lastTime = time2
            self.b1.config(text=time2)
            self.b2.config(text=self.now.strftime('%I:%M:%S'))
        self.after(20, self.tick)

    def write(self):
        g=time.localtime()
        Datename = dt.datetime(1,1,1).now().strftime('%Y%m%d')
        my_Time = dt.timedelta(hours=g[3], minutes=g[4], seconds=g[5])
        #filename="C:\\Users\\jpeters\\Timer.log_"+Datename+"_TNS.csv"
        filename="/home/jbp/Dropbox/Past_Rx/"+Datename+"_Past_Rx.csv"
        file =open(filename, 'a' )
        file.write(str(Datename))
        file.write(', ')
        file.write(str(my_Time))
        file.write(', ')
        file.write((self.lastTime))
        file.write(', ')
        file.write(time_str_to_d_day( self.lastTime )) ## default time format on csv/spreadsheet
        file.write( ', ')
        file.write(str(self.message))
        file.write('\n')        
        file.close()
        self.start_timer()

    
    def quit(self):
        self.write()
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("TimeKeeper")
    root.iconphoto(True, PhotoImage(file="/home/jbp/Documents/myPythonStuff/tk-time/timeKeeper.png"))
    frame= TimeClock(root,bg='purple') 
    frame.pack( expand='false', fill ='both')
    root.mainloop()
