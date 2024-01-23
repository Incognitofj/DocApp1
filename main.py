import pickle
import tkinter as tk
from tkinter.font import BOLD, ITALIC

# Database
appontments=[]

def send_message():
    with open("appontments.dat", "wb") as f:
        pickle.dump(appontments, f) #запись в файл
    print("Your appointment") #приходит sms

#функции для кнопок с врачами
def btn1_click():
    btn11 = tk.Button(root, text="14-15", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn12 = tk.Button(root, text="15-16", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn13 = tk.Button(root, text="16-17", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn14 = tk.Button(root, text="17-18", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn15 = tk.Button(root, text="18-19", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn16 = tk.Button(root, text="19-20", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)

    btn11.grid(row=1,column=3)
    btn12.grid(row=1,column=4)
    btn13.grid(row=1,column=5)
    btn14.grid(row=1,column=6)
    btn15.grid(row=1,column=7)
    btn16.grid(row=1,column=8)

def btn2_click():
    btn21 = tk.Button(root, text="08-09", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn22 = tk.Button(root, text="09-10", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn23 = tk.Button(root, text="10-11", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn24 = tk.Button(root, text="11-12", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn25 = tk.Button(root, text="12-13", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn26 = tk.Button(root, text="13-14", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)

    btn21.grid(row=2,column=3)
    btn22.grid(row=2,column=4)
    btn23.grid(row=2,column=5)
    btn24.grid(row=2,column=6)
    btn25.grid(row=2,column=7)
    btn26.grid(row=2,column=8)

def btn3_click():
    btn31 = tk.Button(root, text="14-15", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn32 = tk.Button(root, text="15-16", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn33 = tk.Button(root, text="16-17", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn34 = tk.Button(root, text="17-18", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn35 = tk.Button(root, text="18-19", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn36 = tk.Button(root, text="19-20", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)

    btn31.grid(row=3,column=3)
    btn32.grid(row=3,column=4)
    btn33.grid(row=3,column=5)
    btn34.grid(row=3,column=6)
    btn35.grid(row=3,column=7)
    btn36.grid(row=3,column=8)

def btn4_click():
    btn41 = tk.Button(root, text="08-09", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn42 = tk.Button(root, text="09-10", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn43 = tk.Button(root, text="10-11", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn44 = tk.Button(root, text="11-12", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn45 = tk.Button(root, text="12-13", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn46 = tk.Button(root, text="13-14", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)

    btn41.grid(row=4,column=3)
    btn42.grid(row=4,column=4)
    btn43.grid(row=4,column=5)
    btn44.grid(row=4,column=6)
    btn45.grid(row=4,column=7)
    btn46.grid(row=4,column=8)

def btn5_click():
    btn51 = tk.Button(root, text="14-15", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn52 = tk.Button(root, text="15-16", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn53 = tk.Button(root, text="16-17", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn54 = tk.Button(root, text="17-18", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn55 = tk.Button(root, text="18-19", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)
    btn56 = tk.Button(root, text="19-20", bg="#FEBAF6", fg="#000000", font=("Calibri", 12, BOLD), padx=1, pady=1,command=send_message)

    btn51.grid(row=5,column=3)
    btn52.grid(row=5,column=4)
    btn53.grid(row=5,column=5)
    btn54.grid(row=5,column=6)
    btn55.grid(row=5,column=7)
    btn56.grid(row=5,column=8)


# создаем окно
root=tk.Tk()
root.title("Doctor Appointment App")
root.geometry("480x300+300+100")
# сохранить png картинку в папку с программой
photo=tk.PhotoImage(file="ImageDoctor.png")
root.iconphoto(False,photo)
root.minsize(300,150)
root.maxsize(700,700)
root.resizable(True,True)
root.config(bg="#FAEBD7")

# добавляем текст
l1=tk.Label(root,text="Select a doctor",bg="#1AF2BC",fg="#F2501A",font=("Arial",20,BOLD,ITALIC),padx=10,pady=10)
l1.grid(row=0,column=0,columnspan=9,sticky="ew")

# добавляем кнопку
# btn2=tk.Button(root,text="Physician",command=btn1_click)

btn1=tk.Button(root, text="Pediatrician",bg="#0BECFD",fg="#000000",width=20,font=("Calibri",12,BOLD),padx=1,pady=1,underline=(0),command=btn1_click)

btn2=tk.Button(root, text="Physician",bg="#0BECFD",fg="#000000",width=20,font=("Calibri",12,BOLD),padx=1,pady=1,underline=(0),command=btn2_click)

btn3=tk.Button(root, text="Therapist",bg="#0BECFD",fg="#000000",width=20,font=("Calibri",12,BOLD),padx=1,pady=1,underline=(0),command=btn3_click)

btn4=tk.Button(root, text="Andrologist",bg="#0BECFD",fg="#000000",width=20,font=("Calibri",12,BOLD),padx=1,pady=1,underline=(0),command=btn4_click)

btn5=tk.Button(root, text="Ophthalmologist",bg="#0BECFD",fg="#000000",width=20,font=("Calibri",12,BOLD),padx=1,pady=1,underline=(0),command=btn5_click)

# btn2.grid(row=2,column=0)
btn1.grid(row=1,column=0,padx=5, pady=5) #ipadx=6, ipady=6,
btn2.grid(row=2,column=0,padx=5, pady=5)
btn3.grid(row=3,column=0,padx=5, pady=5)
btn4.grid(row=4,column=0,padx=5, pady=5)
btn5.grid(row=5,column=0,padx=5, pady=5)

root.mainloop()