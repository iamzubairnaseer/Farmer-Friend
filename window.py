from speech_recognition import*
import time
import SmsSender
from tkinter import*
import tkinter.messagebox
import fertilizer
from abc import ABCMeta, abstractmethod

class window(metaclass=ABCMeta):

    def __init__(self,Title,Geometry):
        self.Title=Title
        self.Geometry=Geometry

    @abstractmethod
    def Create_Windows(self):
        pass

class Fertilizers_Updates_Window(window):

    def __init__(self,Title,Geometry):
        super(Fertilizers_Updates_Window,self).__init__(Title,Geometry)

    def Create_Windows(self):
        self.F_U_Window=Toplevel(main_window)
        self.F_U_Window.geometry(self.Geometry)
        self.F_U_Window.title(self.Title)

        
        frame1 = Frame(self.F_U_Window, bg='light green')
        frame1.pack(fill=BOTH)
        
        data = StringVar()

        label = Label(frame1, font=('times', 16, ' roman'),
                      textvariable=data, bg='light green', fg='violet red')
        label.pack(fill=BOTH)

        list_of_fertilizer_updates =fertilizer.Fertilizers_Updates.getListOfFertilizers()

        count = 0

        for i in list_of_fertilizer_updates:

            count += 1

            data.set(data.get() + "\n(" + str(
                count) + ") FERTILIZER: " + i.name + "\nPRICE: " + i.price + "\nWEIGHT: "
                     + i.weight + "\nRATING: " + i.rating + "\nDESCRIPTION: " + i.description + "\n")

        destroy.images()
        button = Button(frame1,image=destroy.BButton,
                        command=destroy.FUWindow, padx=22, pady=8,
                        bg='light green')
        button.pack()

        self.F_U_Window.mainloop()

class Alternatives_Fertilizers_Window(window):

    def __init__(self,Title,Geometry):
        super(Alternatives_Fertilizers_Window,self).__init__(Title,Geometry)

    def Create_Windows(self):
        self.A_F_Window = Toplevel(main_window)
        self.A_F_Window.geometry(self.Geometry)
        self.A_F_Window.title(self.Title)

        frame1 = Frame(self.A_F_Window, bg='light green')
        frame1.pack(fill=BOTH)

        data = StringVar()

        label = Label(frame1, font=('times', 18, ' roman'),
                      textvariable=data, bg='light green', fg='violet red')
        label.pack(fill=BOTH)

        list_of_alternative_fertilizers = fertilizer.Alternatives_Of_Fertilizers.getListOfFertilizers()

        count = 0

        for i in list_of_alternative_fertilizers:

            count += 1

            data.set(data.get() + "\n(" + str(
                count) + ") FERTILIZER: " + i.name + "\nPRICE: " + i.price + "\nRATING: " + i.rating + "\nDESCRIPTION: " + i.description + "\n\n")

        destroy.images()
        button = Button(frame1, image=destroy.BButton, command=destroy.AFWindow,
                        padx=22, pady=3, bg='light green')
        button.pack()

        self.A_F_Window.mainloop()

class Suggestions_Fertlizers_Window(window):

    def __init__(self,Title,Geometry):
        super(Suggestions_Fertlizers_Window,self).__init__(Title,Geometry)

    def Create_Windows(self):
        self.S_F_Window = Toplevel(main_window)
        self.S_F_Window.geometry(self.Geometry)
        self.S_F_Window.title(self.Title)

        frame1 = Frame(self.S_F_Window, bg='light green')
        frame1.pack(fill=BOTH)

        data = StringVar()

        label = Label(frame1, font=('times', 18, ' roman'),
                      textvariable=data, bg='light green', fg='violet red')
        label.pack(fill=BOTH)

        list_of_suggested_fertilizers =(fertilizer.Suggestions_Of_Fertilizers.getListOfSuggestedFertilizers())

        count = 0

        for i in list_of_suggested_fertilizers:

            count += 1

            data.set(data.get() + "\n(" + str(
                count) + ") FERTILIZER SUGGESTION: " + i.suggestion + "\nUSE FOR: "
                     + i.UseFor + "\n\n")

        destroy.images()
        button = Button(frame1, image=destroy.BButton, command=destroy.SFWindow,
                        padx=22, pady=3, bg='light green')
        button.pack()

        self.S_F_Window.mainloop()

class Weather_Notification_Window(window):

    def __init__(self,Title,Geometry):
        super(Weather_Notification_Window,self).__init__(Title,Geometry)

    def Create_Windows(self):
        self.W_N_Window = Toplevel(main_window)
        self.W_N_Window.geometry(self.Geometry)
        self.W_N_Window.title(self.Title)

        frame1=Canvas(self.W_N_Window,bg='green',width=1366,height=700)
        Image = PhotoImage(file="weather.png")
        frame1.create_image(0,0,anchor=NW,image=Image)
        frame1.place(x=0,y=0)

##        frame1 = Frame(self.W_N_Window, bg='light blue',width=1366,height=700)
##        frame1.pack(fill=BOTH)
        
        label1 = Label(frame1, text='Enter city name for weather forecast',
                       font=('times', 25, 'roman'), bg='light blue')
        label1.place(x=425,y=150)

        self.data = StringVar()

        self.entry = Entry(frame1,textvariable=self.data,width=30, font=('times', 25, 'roman'))
        self.entry.place(x=425,y=200)

        button1=Button(frame1,text='Process',height =1,width=10,font=('arial', 22, 'roman'),bg='light blue'
                       ,command=Weather_Notification_Window.SMS_SENDER)
        button1.place(x=600,y=250)

        mic=PhotoImage(file='mic.png')
        vobutt=Button(frame1,image=mic,bg='light blue',command=Weather_Notification_Window.Voice)
        vobutt.place(x=940,y=200)

##        self.var=StringVar()
##        self.var.set('')

##        label2 = Label(frame1, textvariable=self.var, font=('times', 25, 'roman'), bg='light blue',
##                       fg='violet red')
##        label2.place(x=425,y=375)

        self.label2 = Label(frame1,bg='light blue',fg='violet red')
        self.label2.place(x=425,y=375)

        destroy.images()
        button2 = Button(frame1, font=('arial', 23, 'roman'),image=destroy.BButton ,
                         command=destroy.WNWindow, bg='light blue', padx=22, pady=4)
        button2.place(x=625,y=550)

        self.W_N_Window.mainloop()

    @staticmethod
    def Voice():
        r=Recognizer()
        with Microphone() as source:
            audio=r.listen(source)
            try:
                text = r.recognize_google(audio)
                Object_W_N_W.data.set(text)
            except:
                 Object_W_N_W.data.set('Sorry could not recognizied your voice')

    @staticmethod
    def SMS_SENDER():

        localtime = time.strftime('%I:%M:%S%p,%d-%B-%y')

        city_name = Object_W_N_W.data.get()

        SmsSender.send_sms(city_name)

        temperature=SmsSender.get_weather(city_name)

        Object_W_N_W.label2.config(font=('times', 25, 'roman'), text="Temperature at " + city_name + " on (" + localtime + ") is "+ str(temperature) + "'C")

##        Object_W_N_W.var.set("Temperature at " + city_name + " on (" + localtime + ") is "
##                + str(temperature) + "'C")

class destroy():

    @staticmethod
    def images():
        destroy.BButton=PhotoImage(file="bb.png")
    
    @staticmethod
    def mainwindow():
        answer=tkinter.messagebox.askquestion("Confirmation","Do you want to exit?")
        if answer=="yes":
            main_window.destroy()

    @staticmethod
    def WNWindow():
        Object_W_N_W.W_N_Window.destroy()

    @staticmethod
    def SFWindow():
        Object_S_F_W.S_F_Window.destroy()

    @staticmethod
    def AFWindow():
        Object_A_F_W.A_F_Window.destroy()

    @staticmethod
    def FUWindow():
        Object_F_U_W.F_U_Window.destroy()

#===================================IMAGE===============================================

root = Tk()
root.geometry('1366x700+0+0')
root.title('Welcome To Farmer Friend')

frame0 = Frame(root, bg='Green')
frame0.pack(fill=BOTH)

image = PhotoImage(file="farmland.gif")
label = Label(frame0,compound=CENTER,text="WELCOME TO FARMER FRIEND",fg='yellow',font="Times 60 bold",image=image)
label.pack(fill=BOTH)

Continue=PhotoImage(file='c.png')
bttn=Button(frame0,image=Continue,bg='Light Green',command=root.destroy,
            font=('arial', 32, 'roman'), bd=10,pady=3, padx=90)
bttn.pack()

root.mainloop()

# =================================MAIN_WINDOW============================================

main_window = Tk()
main_window.geometry('1350x699+0+0')
main_window.title('Farmer Friend')

# =========================FRAME==============================================================
frame = Frame(main_window, bg='light green')
frame.pack(fill=BOTH)

# =========================TIME===============================================================

time1=''

label1=Label(frame,font=('times',20,'bold'),bg='green')
label1.pack()

def ti():
    global time1
    time2=time.strftime('%I:%M:%S%p')
    date=time.strftime('%d-%B-%y')
    if time2!=time1:
        time1=time2
        label1.config(text=('Time:',time2,',Date:',date))
    label1.after(200,ti)

ti()
# =======================LABELS============================================================
label2=Label(frame, text='farmer friend', font=('calibri', 65, 'bold italic underline'),
             fg='green', bg='light green')
label2.pack()

label3 = Label(frame, font=('times', 30, 'bold'), text='MAIN MENU\n', bg='light green')
label3.pack(pady=30)

# ===================BUTTONS/OBJECTS=========================================================
Object_F_U_W=Fertilizers_Updates_Window('Updates','1399x768+0+0')
button1 = Button(frame, font=('arial', 20, ' roman'), bd=10,bg='Green',
                 text='Fertilizers Updates',command=Object_F_U_W.Create_Windows, pady=3,
                 padx=111)
button1.pack()

Object_A_F_W=Alternatives_Fertilizers_Window('Alternative','1399x768+0+0')
button2 = Button(frame, font=('arial', 20, 'roman'), bd=10,bg='Yellow',
                 text='Best Alternatives of Fertilizers',command=Object_A_F_W.Create_Windows,
                 pady=3, padx=43)
button2.pack()

Object_S_F_W=Suggestions_Fertlizers_Window('Suggestions','1399x768+0+0')
button3 = Button(frame, font=('arial', 20, 'roman'), bd=10,bg='Blue',
                 text='Fertilizers Suggestions',command=Object_S_F_W.Create_Windows,
                 pady=3, padx=85)
button3.pack()

Object_W_N_W=Weather_Notification_Window('Weather','1399x768+0+0')
button4 = Button(frame, font=('arial', 20, 'roman'), bd=10,bg='Light Blue',
                 text='Weather Notifications',command=Object_W_N_W.Create_Windows, pady=3,
                 padx=93)
button4.pack()

Exit=PhotoImage(file="exit1.png")
button5 = Button(frame, font=('arial', 20, 'roman'),image=Exit, bd=10,bg='light green'
                 ,command=destroy.mainwindow,pady=3,padx=90)
button5.pack()

main_window.mainloop()
