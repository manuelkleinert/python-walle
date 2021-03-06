from tkinter import Frame, Label, StringVar, OptionMenu, W, Entry

class Select(Frame):
    def __init__(self, master = None, labelText = '', options = [], width = 30):
        '''
        Create a selector with label
        :param master: Frame, frame
        :param labelText: Frame, label texte 
        :param options: Array, Frame options
        :param width: Int, label with
        '''
        Frame.__init__(self, master)
        
        self.pack()
        
        self.options = options
        
        self.label = Label(self, anchor = W, text = labelText, width = width)
        self.label.pack(side = 'left')
        
        self.var = StringVar()
        self.var.set(list(self.options.keys())[0])
        self.select = OptionMenu(self, self.var, *self.options.keys())
        self.select.pack(side='right')
    
    def setEvent(self, event):
        self.var.trace("w", event)
        
    def get(self):
        return self.options[self.var.get()]
    
    def setValue(self, value):
        self.var.set(value)


class TextField(Frame):
    def __init__(self, master = None, labelText = '', options = [], width = 30):
        '''
        Create a imput with label
        '''
        Frame.__init__(self, master)
        
        self.pack()
        
        self.options = options
        
        self.label = Label(self, anchor = W, text = labelText, width = width)
        self.label.pack(side = 'left')
        
        self.input = Entry(self)
        self.input.pack(side='right')
        
    def get(self):
        return self.input.get()
    
    def setValue(self, value):
        self.input.delete(0,"end")
        self.input.insert(0, value)