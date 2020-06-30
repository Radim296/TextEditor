from tkinter import *                            # Вызов необходимых библиотек
from tkinter import filedialog as fd
from tkinter.colorchooser import *
from tkinter import messagebox as mb
import os
from tkinter import ttk
from pathlib import Path
from sys import platform
import webbrowser
import smtplib as sm 
def clean():
  if platform.count('win') == 1:
    os.system('cls')
  elif platform.count('linux') == 1:
    os.system('clear')

#SETUP
STATUS_INFORMATION_TEXT = 1
clean()
#GLOBAL VARIABLES
text_information = ''
hello_text = ''
TEXT_ERROR='..'
THEME_CONFIG='.theme.PyDev.textED.dat'
THEME_INF_CONFIG='Themes'
EMAIL_ADRESS='testmailradim@gmail.com'
EMAIL_PASSWORD='radim2006'
HTML_ADDRES='file://'
server=''
if STATUS_INFORMATION_TEXT == 1:
  text_information='''                                  '''
elif STATUS_INFORMATION_TEXT == 0:
  file = open('information.txt', 'r', encoding='utf-8')
  text_information = file.read()
  file.close()
if platform == 'win32':
  hello_text='Эта программа работает на операционной системе Windows'
  print(hello_text)
elif platform == 'linux' or 'linux64' or 'linux32':
  hello_text='Эта программа работает на операционной системе Linux'
  print(hello_text)
try:
  file = open('datanamescash', 'r')
  file.close()
except:
  file = open('datanamescash', 'w')
  file.close()
try:
  file = open('cashcolor', 'r')
  file.close()
except:
  file = open('cashcolor', 'w')
  file.write('black red')
  file.close()
try:
  file = open('cash.txt', 'r')
  file.close()
except:
  file = open('cash.txt', 'w')
  file.close()
try:
  file = open('Themes', 'r')
  file.close()
except:
  file = open('Themes', 'w')
  file.close()
def newopen():
 pf=0
 def frame1(name1):
  global pf
  pf=1
  notebook.add(f1, text=name1)
 def frame1n():
  global pf
  p=1
  file=open('datanamescash','r')
  gf=file.read()
  file.close()
  name3=os.path.basename(os.path.normpath(gf))
  frame1(name3)
 
 def Save1(event):                   # Функция которая считывает нажатие на клавишу
  Open()

 def whosave1(event):                 # Функция которая считывает нажатие на клавишу
  whosave()

 def tools():                                     # Функция которая открывает окно настроек 
  notebook.add(f2, text='   Настройки    ')

 def getColor():                          # Инструмент с помощью которого можно подобрать цвет
  color = str(askcolor())
  color1=''
  color2=''
  l=0
  for i in color:
    if i == '#':
      color1=color1+'#'
      l=1
    elif l == 1:
      if (i != ')') and (i != '''"''') and (i != ''''''''):
        color1=color1+i
  for i in color1:
    if color1.index(i) != len(color1)-1:
      color2=color2+i
  text.insert(END,color2)
 def connectServer():
      global server
      server=sm.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(EMAIL_ADRESS, EMAIL_PASSWORD)
 def Save():                        # Функция которая просто сохраняет файл
    try:
      file1=open('datanamescash', 'r')
      filename=file1.read()
      file1.close()
      s = text.get(1.0, END)
      file = open(filename, 'w')
      file.write(s)
      file.close()
    except:
      print(TEXT_ERROR)

 def whosave():                      # Функция которая сохраняет файл в выбранной директорий
  try:
   filename = fd.asksaveasfilename( filetypes=(("Txt", "*.txt"),
                                        ("Html", "*.html;*.htm"),
                                        ("Python", "*.py"),
                                                ("All files", "*.*") ))
   file1=open('datanamescash', 'w')
   file1.write(filename)
   file1.close()
   file = open(filename, 'w')
   s = text.get(1.0, END)
   file.write(s)
   file.close()
   file2 = open('cash.txt', 'w')
   file2.write(filename)
   file3.close()
   frame1n()
  except :
    print(TEXT_ERROR)

 def Open():                        # Открытие файла 
  try:
    filename = fd.askopenfilename(filetypes=(("Txt", "*.txt"),
                                        ("Html", "*.html;*.htm"),
                                        ("Python", "*.py"),
                                                ("All files", "*.*") ))
    file1=open('datanamescash', 'w')
    file1.write(filename)
    if filename.count('html') < 0:
      HTML_ADDRES='file:///'+filename
    file1.close()
    f=open(filename, 'r')
    s=f.read()
    text.delete(1.0, END)
    text.insert(1.0, s)
    global p
    p=True
    f.close()
    file = open('cash.txt', 'w')
    file.write(filename)
    file.close()
    n1 = Frame(notebook, bg=bgtext, width=c, height=v)
    frame1n()
  except TypeError:
    print(TEXT_ERROR)
 def simsum():
    root=Tk()
    root.mainloop()
 win = ''  
 def runfile():                         # Функция которая запускает файлы   #bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
  global win
  def python():
   n=text.get(1.0, END)
   file=open('python1.py','w',encoding='utf-8')
   file.write(n)
   file.close()
   os.system('python python1.py')
  def html():
   n = text.get(1.0, END)
   file=open('html.html','w',encoding='utf-8')
   file.write(n)
   file.close()
   url = HTML_ADDRES
   webbrowser.open(HTML_ADDRES)
  notebook.add(f6, text='Запуск')
  # Испрвиить 
  t = Label(f6, fg = fgtext, bg = bgtext, text = '            Здесь вы можете запустить свой проект            ').pack()
  t1 = Label(f6, fg = fgtext, bg = bgtext, text = 'Выберите язык програмирования: ').pack(side=LEFT)
  b90 = Button(f6, text = "Pyhton", fg = fgtext, bg = bgtext, command = python).pack(side=LEFT)
  b70 = Button(f6, text = "HTML", fg = fgtext, bg = bgtext, command = html).pack(side=LEFT)
 def idouble(event):
   text.insert(END, ')')
 def exit1():                  
  answer = mb.askyesno('Вы уверенны?', 'Программа будет закрыта и все несохраненные данные будут удаленны')
  if answer == True:
    root.destroy()
    exit()

 def doSomething():               # Предупреждение всплывающее при нажатий кнопки закрытия 
  file=open('datanamescash','r')
  gf=file.read()
  file.close()
  name3=os.path.basename(os.path.normpath(gf))
  g='Сохранить документ'+' '+name3+'?'
  if pf == 1:
   answer = mb.askyesno('Сохранить документ?', g)
   if answer == True:
    try: 
      Save()
      root.destroy()
      try:
        win.destroy()
      except:
        print(TEXT_ERROR)
      exit()
    except:
      root.destroy()
      try:
        win.destroy()
      except:
        print(TEXT_ERROR)
      exit()
   if answer == 'False':
    try:
      root.destroy()
      exit()
    except:
      root.destroy()
      exit()
  if pf == False:
    exit1()
 def new():
  text.delete(1.0, END)
  Save()
  filename='unitiled.txt'
  file=open(filename, 'w')
  file = open('cash.txt', 'w')
  file.write(filename)
  file.close()
  file1=open('datanamescash', 'w')
  file1.write(filename)
  file1.close()
  frame1(filename)
 def new1(event):
  new()
 def runfile1(event):
  runfile()
 def Save1(event):                   # Функция которая считывает нажатие на клавишу
  Open()

 def whosave1(event):                 # Функция которая считывает нажатие на клавишу
  whosave()
 def addTheme():                                                   #
    try:
          filename = fd.askopenfilename(filetypes=(("Txt", "*.txt"),
                                        ("Html", "*.html;*.htm"),
                                        ("Python", "*.py"),
                                                ("All files", "*.*") ))
    except:
      print(text_information)
    try:
       file=open(THEME_INF_CONFIG, 'a')
    except:
       file=open(THEME_INF_CONFIG, 'a')
    file.write(open(filename, 'r').read())
 def tools():                                     # Функция которая открывает окно настроек 
  notebook.add(f2, text='Темы')
 def kl():
   Save()
   lj=text.get(1.0,END)
   lj = len(lj) - 1
   f = Label(f1, text = str(lj)).pack()
   f1.after(200, kl)
   lj=0
 def Saveclick(event):
    Save()
 def newopen1():
   root.destroy()
   Save( )
   try:
          win.destroy()
   except:
          print(TEXT_ERROR)
   newopen()
 def runfilehtml():
   pass
 def ema():
    def send():
      EMAIL = message.get()
      rs = text.get(1.0, END)
      server.sendmail(EMAIL_ADRESS, EMAIL, rs)
      server.quit()
    message=StringVar()

    notebook.add(f8, text='Отправить текст')
    l1=Label(f8, fg=fgtext, bg=bgtext, text='Введите email адрес получателя').pack()

    txt1 = Entry(f8,insertbackground=fgtext, justify=CENTER,selectforeground=bgtext,selectbackground=fgtext, width=20, bg=bgtext, text='....', fg=fgtext, textvariable=message).pack(side=LEFT)
    b1u=Button(f8, fg=fgtext, bg=bgtext, text='Отправить', command=send).pack(side=LEFT)
 print(EMAIL_ADRESS)
 def inf():
    notebook.add(f5, text='Справка')
    w1 = Label(f5, text = text_information, bg= bgtext, fg=fgtext).pack()
    w2 = Label(f5, text = hello_text, bg= bgtext, fg=fgtext).pack()
 file=open('cashcolor', 'r')
 info=file.read()
 file.close()
 bgtext,fgtext=info.split()
 colorbg=['white','black','#3f3f40','white']
 colorfg=['black','green','#adadad','#a607eb']
 v=int(553)    # Размеры фрейма(Высота)
 c=int(802)    # Размеры фрейма(Ширина)
 wt=62
 ht=32
 a=bgtext   # Фон виджета меню
 b=fgtext     # Цвет текста виджета меню

 root = Tk()
 root.title('TextED')   # Название программы
 w = root.winfo_screenwidth() # ширина экрана
 h = root.winfo_screenheight() # высота экрана
 w = w//2 # середина экрана
 h = h//2 
 w = w - 200 # смещение от середины
 h = h - 200
 root.geometry('627x570+{}+{}'.format(w, h)) 
 #root.geometry('627x570') # Размеры окна по умолчанию
 root['bg'] =  bgtext   # Цвет фона окна 
 mainmenu = Menu(root, bg=bgtext, fg=fgtext)
 root.config(menu = mainmenu)
 root.resizable(True, True)     # Ограничения в расширений окна 
 root.option_add("*Font", "courier 12")   # Шрифт 
 root.protocol('WM_DELETE_WINDOW', doSomething)       # Функция присваевает нажатие кнопки закрыть программу на определенную комманду
 root.overrideredirect(False)

 def theme1():
      file=open('cashcolor', 'w')
      g=colorbg[0]+' '+colorfg[0]
      bg=colorbg[0]
      fg=colorfg[0]
      file.write(g)
      file.close()
      answer = mb.askyesno('Вы уверенны?', 'Программа будет перезагружена и все несохраненные данные будут удаленны')
      if answer == True:
       try: 
         root.destroy()
         try:
          win.destroy()
         except:
          print(TEXT_ERROR)
       except:
        return 0
 def theme3():
    file=open('cashcolor', 'w')
    indb=2
    indfg=2
    g=colorbg[indb]+' '+colorfg[indfg]
    bg=colorbg[indb]
    fg=colorfg[indfg]
    file.write(g)
    file.close()
    answer = mb.askyesno('Вы уверенны?', 'Программа будет перезагружена и все несохраненные данные будут удаленны')
    if answer == True:
      try: 
       root.destroy()
       try:
          win.destroy()
       except:
          print(TEXT_ERROR)
      except:
       return TEXT_ERROR
 def theme4():
    file=open('cashcolor', 'w')
    indb=3
    indfg=3
    g=colorbg[indb]+' '+colorfg[indfg]
    bg=colorbg[indb]
    fg=colorfg[indfg]
    file.write(g)
    file.close()
    answer = mb.askyesno('Вы уверенны?', 'Программа будет перезагружена и все несохраненные данные будут удаленны')
    if answer == True:
      try: 
       root.destroy()
       try:
          win.destroy()
       except:
          print(TEXT_ERROR)
      except:
       return TEXT_ERROR
      
 def theme5():
    file=open('cashcolor', 'w')
    bg='black'
    fg='red'
    g=bg+" "+fg
    file.write(g)
    file.close()
    answer = mb.askyesno('Вы уверенны?', 'Программа будет перезагружена и все несохраненные данные будут удаленны')
    if answer == True:
      try: 
       root.destroy()
       try:
          win.destroy()
       except:
          print(TEXT_ERROR)
      except:
       return TEXT_ERROR
 def openwelcome():
   l1      
 def theme2():
    file=open('cashcolor', 'w')
    indb=1
    indfg=2
    g=colorbg[indb]+' '+colorfg[indfg]
    bg=colorbg[indb]
    fg=colorfg[indfg]
    file.write(g)
    file.close()
    answer = mb.askyesno('Вы уверенны?', 'Программа будет перезагружена и все несохраненные данные будут удаленны')
    if answer == True:
      try: 
       root.destroy()
       try:
          win.destroy()
       except:
          print(TEXT_ERROR)
      except:
       return TEXT_ERROR
 def theme6():
    file=open('cashcolor', 'w')
    bg='#adadad'
    fg='red'
    g=bg+" "+fg
    file.write(g)
    file.close()
    answer = mb.askyesno('Вы уверенны?', 'Программа будет перезагружена и все несохраненные данные будут удаленны')
    if answer == True:
      try: 
       root.destroy()
       try:
          win.destroy()
       except:
          print(TEXT_ERROR)
      except:
       return TEXT_ERROR
 def theme7():
    file=open('cashcolor', 'w')
    bg='#adadad'
    fg='blue'
    g=bg+" "+fg
    file.write(g)
    file.close()
    answer = mb.askyesno('Вы уверенны?', 'Программа будет перезагружена и все несохраненные данные будут удаленны')
    if answer == True:
      try: 
       root.destroy()
       try:
          win.destroy()
       except:
          print(TEXT_ERROR)
      except:
       return TEXT_ERROR

 style = ttk.Style(root)
 style.configure('lefttab.TNotebook', tabposition='')

 notebook = ttk.Notebook(root, style='lefttab.TNotebook')

 f1 = Frame(notebook, bg=bgtext, width=c, height=v)

 f2 = Frame(notebook, bg=bgtext, width=c, height=v)
 f4 = Frame(root, bg=bgtext, width=c, height=v)
 f5 = Frame(root, bg=bgtext, width=c, height=v)
 f6 = Frame(notebook, bg=bgtext, width=c, height=v)
 f7 = Frame(f2, bg=bgtext, width=c, height=5)
 f8 = Frame(notebook, bg=bgtext, width=c, height=v)
 r1 = Button(f2, fg='black',bg='white', text='Default theme', command=theme1)
 r1.grid(row=2, column=1)
 r2 = Button(f2, fg='green',bg='black', text=' Hacker theme',highlightcolor='green', command=theme2)
 r2.grid(row=2, column=2)
 r3 = Button(f2, fg='#adadad',bg='#3f3f40', text=' Gray theme  ', command=theme3)
 r3.grid(row=2, column=3)
 r4 = Button(f2, fg='#a607eb',bg='white', text='Violet theme', command=theme4)
 r4.grid(row=2, column=4)
 r5 = Button(f2, fg='red',bg='black', text=' Diablo theme', command=theme5)
 r5.grid(row=3, column=1)
 r6 = Button(f2, fg='red',bg='#adadad', text='  Theme one  ', command=theme6)
 r6.grid(row=3, column=2)
 r7 = Button(f2, fg='blue',bg='#adadad', text='  Theme two  ', command=theme7)
 r7.grid(row=3, column=3)
 
 #61
 text = Text(f1,insertbackground=fgtext,selectforeground=bgtext,selectbackground=fgtext, width=wt, bg=bgtext, font= "Courier",  height=ht, fg=fgtext, wrap=WORD)
 text.pack()
 scroll = Scrollbar(bg=bgtext, command=text.yview)
 scroll.pack(side=RIGHT, fill='y')
 text.config(yscrollcommand=scroll.set)
 notebook.pack()

 filemenu = Menu(mainmenu, tearoff=0)
 filemenu.add_command(label="Открыть...", command=Open)
 filemenu.add_command(label="Новый", command=new)
 filemenu.add_command(label="Сохранить", command=Save)
 filemenu.add_command(label="Сохранить как", command=whosave)
 filemenu.entryconfig(0, background=a, foreground=b)
 filemenu.entryconfig(1, background=a, foreground=b)
 filemenu.entryconfig(2, background=a, foreground=b)
 filemenu.entryconfig(3, background=a, foreground=b)
 filemenu.entryconfig(4, background=a, foreground=b)
 

 runmenu = Menu(mainmenu, tearoff=0)
 runmenu.add_command(label="Запуск", command=runfile)
 runmenu.add_command(label="Отправить по email", command=ema)
 runmenu.add_command(label = 'Выбрать цвет', command=getColor)
 runmenu.entryconfig(0, background=a, foreground=b)
 runmenu.entryconfig(1, background=a, foreground=b)
 runmenu.entryconfig(2, background=a, foreground=b)

 toolsmenu = Menu(mainmenu, tearoff=0)
 toolsmenu.add_command(label = 'Выбрать тему', command=tools)
 toolsmenu.add_command(label="Закрыть редактор", command=exit1) 
 toolsmenu.add_command(label="Закрыть все вкладки", command=newopen1) 
 toolsmenu.add_command(label="Очистить консоль", command=clean)
 toolsmenu.add_command(label="Подключится к серверу", command=connectServer)
 toolsmenu.entryconfig(0, background=a, foreground=b)
 toolsmenu.entryconfig(2, background=a, foreground=b)
 toolsmenu.entryconfig(3, background=a, foreground=b)
 toolsmenu.entryconfig(4, background=a, foreground=b)
 toolsmenu.entryconfig(5, background=a, foreground=b)


 iformation = Menu(mainmenu, tearoff = 0)
 iformation.add_command(label = 'Справка', command = inf)
 iformation.entryconfig(0, background=a, foreground=b)

 mainmenu.add_cascade(label="Файл", menu=filemenu)
 mainmenu.add_cascade(label="Дополнения", menu=runmenu)
 mainmenu.add_cascade(label="Инструменты", menu=toolsmenu)
 mainmenu.add_cascade(label="Справка", menu=iformation)
 root.bind('<Control-o>', Save1)                  
 root.bind('<Control-s>', whosave1)
 root.bind('<Control-n>', new1)

 root.bind('F5', runfile1)
 root.bind('<q>', Saveclick)
 root.bind('<w>', Saveclick)
 root.bind('<e>', Saveclick)
 root.bind('<r>', Saveclick)
 root.bind('<t>', Saveclick)
 root.bind('<y>', Saveclick)
 root.bind('<u>', Saveclick)
 root.bind('<i>', Saveclick)
 root.bind('<o>', Saveclick)
 root.bind('<p>', Saveclick)
 root.bind('<a>', Saveclick)
 root.bind('<s>', Saveclick)
 root.bind('<d>', Saveclick)
 root.bind('<f>', Saveclick)
 root.bind('<g>', Saveclick)
 root.bind('<h>', Saveclick)
 root.bind('<j>', Saveclick)
 root.bind('<k>', Saveclick)
 root.bind('<l>', Saveclick)
 root.bind('<z>', Saveclick)
 root.bind('<x>', Saveclick)
 root.bind('<c>', Saveclick)
 root.bind('<v>', Saveclick)
 root.bind('<b>', Saveclick)
 root.bind('<n>', Saveclick)
 root.bind('<m>', Saveclick)
 root.bind('<Enter>', Saveclick)
 root.bind('<1>', Saveclick)
 root.bind('<2>', Saveclick)
 root.bind('<3>', Saveclick)
 root.bind('<4>', Saveclick)
 root.bind('<5>', Saveclick)
 root.bind('<6>', Saveclick)
 root.bind('<7>', Saveclick)
 root.bind('<8>', Saveclick)
 root.bind('<9>', Saveclick)
 root.bind('<0>', Saveclick)
 root.mainloop()
while True:
  newopen()
  clean()
