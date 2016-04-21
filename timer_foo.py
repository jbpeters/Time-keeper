from tkinter import Tk,Button,Frame,Entry,BOTH,Toplevel
import sys
import time
import datetime as dt

class TimeClock(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self,parent, *args, **kwargs)        
        self.e=Entry(self,text='Message')
        self.e.delete(0,"end")
        self.e.pack()        
        self.makebuttons()
        self.pack( expand='true', fill='x')
        
    
    def makebuttons(self):
        self.b1 = Button(self, text="Tock" ,
                         bg='BLUE', activebackground="Blue",
                         activeforeground='White',fg='white',
                         height='2', width='8' , command = self.write )
        self.b2 = Button(self, text="Tick", 
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
            print ("input text is equal to->",self.message)
            root.title(self.message+":TIMER")
            self.e.destroy()
            self.B.destroy()            
        self.B= Button(self,text='start', command=callback)
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
        #filename="C:\Users\jpeters\Timer.log\\"+Datename+"_demo.csv"
        filename="/home/jeff/Desktop/"+Datename+"_demo.csv"
        file =open(filename, 'a' )
        file.write(str(Datename))
        file.write(', ')
        file.write(str(my_Time))
        file.write(', ')
        file.write((self.lastTime))
        file.write(', ')
        file.write(str(self.message))
        file.write('\n')        
        file.close()
        self.start_timer()

    
    def quit(self):
        self.write()
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("foo")
    holder= TimeClock(root,bg='purple') 
    holder.pack( expand='false', fill ='both')
    root.mainloop()
