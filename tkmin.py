from tkinter import Tk, Frame, Button ,Entry, BOTH

class Demo(Frame):
    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args,**kw)
        self.e=Entry(self, text='Message')
        self.e.delete(0,'end')
        self.e.pack()
        self.makebuttons()        
        self.pack(expand='true',fill='x')

    def makebuttons(self):
        self.b1=Button(self, text="restart",bg="blue",fg='white',command= self.restart )
        self.b1.pack(side='right',fill='both' )
        self.b2=Button(self,text='quit',bg='green',fg='white',command=self.quit)
        self.b2.pack(side='left',fill='both')
        self.lastTime=""
        self.start_timer()
        
    def start_timer(self):
        pass

    def destroy(self):
        self.pack_forget()
    

    def restart(self):
        self.destroy()
        D=Demo(root,bg='purple')
        print ("killed")
        D.__init__(self,root)
        pass
    
    def quit(self):
        root.destroy()
    
        




if __name__=='__main__':
    root= Tk()
    root.title('')
    D=Demo(root,bg='purple')
    root.mainloop()
