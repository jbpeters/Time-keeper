#! /usr/bin/python3
"""
Timekeeper:  a stop-watch style program program  that records and 
annotates sequentcial time slices  into a date labled ,
coma seperated variable (.CSV)file whose values can be manipulated 
in a spreadsheet
"""

from tkinter import *
import sys
import time
import datetime as dt

my_path="/home/jbp/Dropbox/Past_Rx/"
my_file="timeKeeper"
my_job="PastRx"


class TimeClock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self,parent, *args, **kwargs)        
        self.makeentry()
        self.makebuttons()
        self.pack( expand='true', fill='x')
    
    def makeentry(self):
        self.input = Entry(self,text='Message',font=("times",16))
        self.input.delete(0,"end")
        self.input.pack(side='top')        
        self.input.focus()

    def makebuttons(self):
        self.b_restart = Button(self, text="Tock" ,font=("times",16),
                         bg='BLUE', activebackground="Blue",
                         activeforeground='White',fg='white',
                         height='2', width='8' , 
                         command = self.write )
                         
        self.b_quit = Button(self, text="Tick", font=("times",16),
                         activebackground='red', bg='red', 
                         activeforeground='White',fg='white',
                         command = self.quit )

        self.b_restart.pack(side='right', fill='both')
        self.b_quit.pack(side='left', fill='both')
        self.lastTime = ""
        self.start_timer()


    def time_str_to_d_day( self, T_string):
        try:
            hours, minutes,seconds = T_string.split(':')
        except ValueError:
            return -1
        return str(int(hours)/(24.0)+int(minutes)/(24.0*60) + int(seconds)/(24.0*60*60))
                                                    
    def start_timer(self):
        def callback():
            self.message=self.input.get()
            root.title(self.message+":TimeKeeper")
            self.input.destroy()
            self.b_start.destroy()
            
        self.b_start= Button(
                        self,
                        text='start', 
                        font=("times",16), 
                        command=callback)
        self.b_start.pack()
        t=time.localtime()
        self.zeroTime = dt.timedelta(hours=t[3], minutes=t[4], seconds=t[5])
        self.tick()
        
    def tick(self):
        self.now = dt.datetime(1, 1, 1).now()
        self.elapsedTime = self.now - self.zeroTime
        time2 = self.elapsedTime.strftime('%H:%M:%S')
        if time2 != self.lastTime:
            self.lastTime = time2
            self.b_restart.config(text=time2)
            self.b_quit.config(text=self.now.strftime('%I:%M:%S'))
        self.after(20, self.tick)

    def write(self):
        g=time.localtime()
        Datename = dt.datetime(1,1,1).now().strftime('%Y%m%d')
        Filename = dt.datetime(1,1,1).now().strftime('week-%W_%Y')
        my_Time = dt.timedelta(hours=g[3], minutes=g[4], seconds=g[5])
        fractional_day = self.time_str_to_d_day(self.lastTime)
        """
        print( str(Datename),", ",end="")
        print( str(self.zeroTime),", ",end="")
        print( str(my_Time),", ",end="")
        print( str(self.lastTime),", ",end="")
        print( str(fractional_day),", ",end="")
        print( str(self.message))
        """
        filename = my_path + Filename +"_"+ my_job +"_"+ my_file + ".csv"
        file =open(filename, 'a' )
        file.write('\n')
        file.write(str(Datename))
        file.write(', ')
        file.write(str(self.zeroTime))
        file.write(', ')
        file.write(str(my_Time))
        file.write(', ')
        file.write((self.lastTime))
        file.write(', ')
        file.write( fractional_day)  ## default time format on csv/spreadsheet
        file.write( ', ')
        file.write(str(self.message))
        #file.write('\n')        
        file.close()
        self.restart()
    
    def restart(self):
        root.title("              ")
        self.destroy()
        frame = TimeClock(root,bg='purple')
    
    def quit(self):
        self.message="quit"
        self.write()
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("TimeKeeper")
    root.iconphoto(True, PhotoImage(file="/home/jbp/bin/timekeeper.png"))
    frame = TimeClock(root,bg='purple') 
    frame.pack( expand='false', fill ='both')
    root.mainloop()
