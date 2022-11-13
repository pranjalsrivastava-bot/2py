from tkinter import *
root= Tk()

root.title("Addition")
root.geometry("600x300")


show_result=Label(root)

def add():
    result= 7+4+6+5+4+10009
    show_result["text"]=result
    
btn = Button(root, text="Do it", command=add)
btn.pack()
    
show_result.pack()
    
root.mainloop()