# https://github.com/mi4code/tk_helper_lib
# licensed under GNU GPL
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import sys


def tk_init(title, size, resizable=False):

    global tk_current_position
    global tk_pady

    global root
    global window

    tk_current_position = 1
    tk_pady = 5

    root = tk.Tk()
    root.title(title)
    root.geometry(size)
    root.resizable(resizable, resizable)
    window = ttk.Frame(root)
    #window.pack(padx=20, pady=20, fill='x', expand=True)
    window.place(relx=.45, rely=.5,anchor= tk.CENTER)


def tk_label(label):
    global tk_current_position
    tkw_label = ttk.Label(window, text=label+" ")
    tkw_label.grid(column=1, row=tk_current_position, padx=3, pady=tk_pady, columnspan=2)
    
    tk_current_position+=1

def tk_entry_text(label, variable, value=None):
    if value is None:
        try: value=eval("sys.modules['__main__']."+variable)
        except: value=""
    exec("sys.modules['__main__']."+variable+" = tk.StringVar()")
    exec("sys.modules['__main__']."+variable+".set(value)")
    
    global tk_current_position
    tkw_label = ttk.Label(window, text=label+" ")
    tkw_label.grid(column=1, row=tk_current_position, sticky=tk.E, padx=3, pady=tk_pady)
    
    tkw_entry = ttk.Entry(window, textvariable=eval("sys.modules['__main__']."+variable))
    tkw_entry.grid(column=2, row=tk_current_position, sticky=tk.W, padx=3, pady=tk_pady)
    
    tk_current_position+=1
    
def tk_entry_text_multiline(label, variable, value=None): # broken initial value, add size
    #import ScrolledText  # from <https://github.com/igeekdom/Custom-Tkinter-ScrolledText>
    class ScrolledText(tk.Frame):
        def __init__(self, parent, textvariable, *args, **kwargs):
            tk.Frame.__init__(self, parent)       
            self.text = tk.Text(self, *args, **kwargs)
            self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
            self.text.configure(yscrollcommand=self.vsb.set)
            self.vsb.pack(side="right", fill="y")
            self.text.pack(side="left", fill="both", expand=True)
            self.text.bind("<KeyRelease>", self.text_changed)
            self.text.bind('<Delete>', self.text_del)
            self.text.bind('<BackSpace>', self.text_backspace)
            self.textvariable = textvariable
            self.text.bind('<Enter>', self.enter)
            self.text.bind('<Leave>', self.leave)
           
        def configure(self, **kwargs):
            self.state(kwargs.get('state',None))
            
        def state(self, state):
            self.text.configure(state=state)
            
        def delete(self, first, last=None):
            self.text.delete(first, last)
            
        def insert(self, location, item):
            self.text.insert(location, item)
        
            
        def enter(self, event):
            self.text.config(cursor="hand2")

        def leave(self, event):
            self.text.config(cursor="")

        def text_changed(self, key):
            if str(self.text.cget('state')) == 'normal':
                self.textvariable.set('')
                self.textvariable.set(self.text.get('1.0', tk.END))
            
        def text_backspace(self, key):
            self.textvariable.set(self.text.get('1.0', self.text.index(tk.CURRENT + ' -1 chars')))
        
        def text_del(self, key):
            self.textvariable.set(self.text.get('1.0', self.text.index(tk.INSERT)))
    
    if value is None:
        try: value=eval("sys.modules['__main__']."+variable)
        except: value=""
    exec("sys.modules['__main__']."+variable+" = tk.StringVar()")
    exec("sys.modules['__main__']."+variable+".set(value)")
    
    global tk_current_position
    tkw_label = ttk.Label(window, text=label+" ")
    tkw_label.grid(column=1, row=tk_current_position, sticky=tk.E, padx=3, pady=tk_pady)
    
    #tkw_entry = ttk.Entry(window, textvariable=globals()[variable])
    tkw_entry = ScrolledText(window, textvariable=eval("sys.modules['__main__']."+variable), wrap=tk.WORD, width=14, height=3)
    #tkw_scroll = tk.Scrollbar(window)
    #tkw_entry.configure(yscrollcommand=tkw_scroll.set)
    tkw_entry.grid(column=2, row=tk_current_position, sticky=tk.W, padx=3, pady=tk_pady)
    #tkw_scroll.config(command=text.yview)
    #tkw_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    tk_current_position+=1

def tk_entry_file(label, variable, value=None): # add in text area button for browse
    if value is None:
        try: value=eval("sys.modules['__main__']."+variable)
        except: value=""
    exec("sys.modules['__main__']."+variable+" = tk.StringVar()")
    exec("sys.modules['__main__']."+variable+".set(value)")
    
    global tk_current_position
    tkw_label = ttk.Label(window, text=label+" ")
    tkw_label.grid(column=1, row=tk_current_position, sticky=tk.E, padx=3, pady=tk_pady)
    
    tkw_entry = ttk.Entry(window, textvariable=eval("sys.modules['__main__']."+variable))
    tkw_entry.bind('<Double-1>', lambda x: exec("sys.modules['__main__']."+variable+".set( fd.askopenfile(filetypes= [('All files', '*.*')] ).name )") )
    tkw_entry.grid(column=2, row=tk_current_position, sticky=tk.W, padx=3, pady=tk_pady)
    
    tk_current_position+=1

def tk_entry_dir(label, variable, value=None): # add in text area button for browse
    if value is None:
        try: value=eval("sys.modules['__main__']."+variable)
        except: value=""
    exec("sys.modules['__main__']."+variable+" = tk.StringVar()")
    exec("sys.modules['__main__']."+variable+".set(value)")
    
    global tk_current_position
    tkw_label = ttk.Label(window, text=label+" ")
    tkw_label.grid(column=1, row=tk_current_position, sticky=tk.E, padx=3, pady=tk_pady)
    
    tkw_entry = ttk.Entry(window, textvariable=eval("sys.modules['__main__']."+variable))
    tkw_entry.bind('<Double-1>', lambda x: exec("sys.modules['__main__']."+variable+".set( fd.askdirectory() )") )
    tkw_entry.grid(column=2, row=tk_current_position, sticky=tk.W, padx=3, pady=tk_pady)
    
    tk_current_position+=1

def tk_button(label, onclick):
    globals_dict = dict()
    for d in dir(sys.modules['__main__']):
        globals_dict[d] = eval("sys.modules['__main__']."+d)
    #print(globals_dict)
    
    global tk_current_position
    tkw = ttk.Button(window, text = label, command = lambda : exec (onclick,globals_dict))
    tkw.grid(column=1, row=tk_current_position, padx=10, pady=tk_pady, columnspan=2)
    tk_current_position+=1

def tk_buttons2(label1, label2, onclick1, onclick2):
    globals_dict = dict()
    for d in dir(sys.modules['__main__']):
        globals_dict[d] = eval("sys.modules['__main__']."+d)
    
    global tk_current_position
    tkw = ttk.Button(window, text = label1, command = lambda : exec (onclick1,globals_dict))
    tkw.grid(column=1, row=tk_current_position, padx=10, pady=tk_pady, columnspan=1)
    
    tkw = ttk.Button(window, text = label2, command = lambda : exec (onclick2,globals_dict))
    tkw.grid(column=2, row=tk_current_position, padx=10, pady=tk_pady, columnspan=1)
    
    tk_current_position+=1
    

def tk_handle():
    root.mainloop()  # keep the window displaying