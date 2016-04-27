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

#my_path="/home/jbp/Desktop/"
#my_file="timekeeper"
my_path="/home/jbp/Dropbox/Past_Rx/"
my_file="Past_Rx"


class TimeClock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self,parent, *args, **kwargs)        
        self.makeentry()
        self.makebuttons()
        self.pack( expand='true', fill='x')
    
    def multi_task(self, *m_tasks):
        def tasks(*args, **kwargs):
            for task in m_tasks:
                task(*args, **kwargs)
        return tasks
    
    def makeentry(self):
        self.e=Entry(self,text='Message',font=("times",16))
        self.e.delete(0,"end")
        self.e.pack(side='top')        
        self.e.focus()

    def makebuttons(self):
        self.b1 = Button(self, text="Tock" ,font=("times",16),
                         bg='BLUE', activebackground="Blue",
                         activeforeground='White',fg='white',
                         height='2', width='8' , 
                         command = self.multi_task( 
                                                    self.write,
                                                    self.makeentry
                                                    )                                                   
                         ) 
                         
        self.b2 = Button(self, text="Tick", font=("times",16),
                         activebackground='red', bg='red', 
                         activeforeground='White',fg='white',
                         command = self.multi_task( 
                                                    self.quit 
                                                    ) 
                         )       
        self.b1.pack(side='right', fill='both')
        self.b2.pack(side='left', fill='both')
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
            #self.message=self.e.delete(0,"end")
            self.message=self.e.get()
            print( "input text is equal to->",self.message)
            root.title(self.message+":TIMER")
            self.e.destroy()
            self.B.destroy()            
        self.B= Button(
                        self,
                        text='start', 
                        font=("times",16), 
                        command=callback)
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
        filename = my_path + Datename +"_" + my_file + ".csv"
        print( filename)
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
        file.write(self.time_str_to_d_day( self.lastTime )) ## default time format on csv/spreadsheet
        file.write( ', ')
        file.write(str(self.message))
        #file.write('\n')        
        file.close()
        self.start_timer()

    
    def quit(self):
        self.write()
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("TimeKeeper")
    root.iconphoto(True, PhotoImage(file="/home/jbp/Documents/myPythonStuff/tk-time/timeKeeper.png"))
    frame = TimeClock(root,bg='purple') 
    frame.pack( expand='false', fill ='both')
    root.mainloop()
