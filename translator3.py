from translate import Translator
from tkinter import *
from tkinter import messagebox



def strt() :
    win = Toplevel(root)
    win.title("TRANSLATOR")
    win.geometry('500x400')
    #win.iconbitmap('Custom-Icon-Design-Flatastic-5-Select-language.ico')
    win.configure(bg='magenta')


    def French():
      word = E1.get()
      translator=Translator(to_lang='French')
      translation = translator.translate(word)
      l2=Label(win,text=f'translated word : {translation}',font=('Arial Bold',12),fg='DodgerBlue2')
      l2.place(x=5, y=180)

    def german():
      word = E1.get()
      translator = Translator(to_lang='German')
      translation = translator.translate(word)
      l2 = Label(win, text=f'translated word : {translation}', font=('Arial  Bold', 12), fg='DodgerBlue2')
      l2.place(x=5,y=180)
    def spanish():
      word = E1.get()
      translator = Translator(to_lang='Spanish')
      translation = translator.translate(word)
      l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
      l2.place(x=5,y=180)
    def hindi():
      word = E1.get()
      translator = Translator(to_lang='Hindi')
      translation = translator.translate(word)
      l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
      l2.place(x=5,y=180)
    def turkish():
      word = E1.get()
      translator = Translator(to_lang='Turkish')
      translation = translator.translate(word)
      l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
      l2.place(x=5, y=180)
    def chinese():
      word = E1.get()
      translator = Translator(to_lang='Chinese')
      translation = translator.translate(word)
      l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
      l2.place(x=5, y=180)
    def Arabic():
      word = E1.get()
      translator = Translator(to_lang='Arabic')
      translation = translator.translate(word)
      l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
      l2.place(x=5, y=180)
    def Persian():
      word = E1.get()
      translator = Translator(to_lang='Arabic')
      translation = translator.translate(word)
      word= " "
      l2 = Label(win, text=f'translated word : {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')
      l2.place(x=5,y=180)

    txt=StringVar()
    l1=Label(win,text="Enter your text Here!!")
    l1.place(x=40,y=3)
    l3=Label(win,text="Translation:",font=('Bold',10))
    l3.place(x=5,y=160)
    E1=Entry(win,textvariable=txt,width=23,font=('Arial Bold',15),bg="white")
    E1.place(x=17,y=20)
    Btn1=Button(win,text='French',bd=5,padx=8,pady=8,bg="powder blue",width=6,command=French)
    Btn1.place(x=5,y=55)
    Btn2=Button(win,text='German',bd=5,padx=8,pady=8,bg="yellow",width=6,command=german)
    Btn2.place(x=75,y=55)
    Btn3=Button(win,text='Spanish',bd=5,padx=8,pady=8,bg="blue",width=6,command=spanish)
    Btn3.place(x=145,y=55)
    Btn4=Button(win,text='Hindi',bd=5,padx=8,pady=8,bg="Green",width=6,command=hindi)
    Btn4.place(x=215,y=55)
    Btn5=Button(win,text='Turkish',bd=5,padx=8,pady=8,bg="Pink",width=6,command=turkish)
    Btn5.place(x=5,y=100)
    Btn6=Button(win,text='Chinese',bd=5,padx=8,pady=8,bg="orange",width=6,command=chinese)
    Btn6.place(x=75,y=100)
    Btn7=Button(win,text='Arabic',bd=5,padx=8,pady=8,bg="white",width=6,command=Arabic)
    Btn7.place(x=145,y=100)
    Btn8=Button(win,text='Persian',bd=5,padx=8,pady=8,bg="DodgerBlue2",width=6,command=Persian)
    Btn8.place(x=215,y=100)
    btn9=Button(win, text="BACK", fg="blue", bg="cyan", bd=15, command=win.destroy)
    btn9.place(x=400, y=300)



root = Tk()
title = Label(text='''WELCOME \n TO \n LANGUAGE TRANSLATOR ''', font="stencil 14 bold", bg="cyan", fg="red")
title.place(x=100, y=5)
btn_start = Button(root, text="START", bg="yellow", fg="green", bd=15, command=strt)
btn_start.place(x=100, y=120)
underline = Label(text='''___________________________
      \n_____________________________''', bg="blue", fg="red")
underline.place(x=20, y=200)



def main_exit():
    rr = messagebox.askyesnocancel('EXIT', 'Are you want to exit !', parent=root)
    if (rr == True):
     root.destroy()

def on_enterbtn2(e):
       btn2['bg'] = 'springgreen'
def on_leavebtn2(e):
        btn2['bg'] = 'yellow'

#imgbt2 = PhotoImage(file='sign-out.png')
#imgbt2 = imgbt2.subsample(10, 10)
btn2 = Button(root, text='Exit',bd=20,fg="black", activebackground='red', width=120, height=70,font=("times 15 italic bold"), compound=BOTTOM, command=main_exit)
btn2.place(x=280, y=260)

btn2.bind('<Enter>', on_enterbtn2)
btn2.bind('<Leave>', on_leavebtn2)

root.geometry('500x400')
root.title('Translater')
#root.iconbitmap('download.ico')
root.configure(bg='pink')

root.mainloop()