from tkinter import *
from tkinter import messagebox
from tkinter import font
import random
import pyperclip
import json
RED="#008000"
window=Tk()

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    web=web_input.get().capitalize()
    try:
        with open("data.json") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Error","data not found")
    else:
        if web in data:
            email = data[web]["Email"]
            password = data[web]["Password"]
            messagebox.showinfo(web,f"Email: {email}\n  Password:{password} ")
        else:
            messagebox.showinfo(web,"no data found")
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters= random.randint(2,5)
    nr_symbols = random.randint(2,5)
    nr_numbers = random.randint(2,5)


    pass_letters=[random.choice(letters) for _ in range(1,nr_letters)]
    pass_symbols=[random.choice(symbols) for _ in range(1,nr_symbols)]
    pass_numbers=[random.choice(numbers) for _ in range(1,nr_numbers)]
    password=pass_letters+pass_symbols+pass_numbers
    random.shuffle(password)
    password=''.join(password)
    pass_input.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    web=web_input.get().title()
    user_name=user_input.get()
    password=pass_input.get()
    if len(web)==0 or len(user_name)==0 or len(password)==0:
        messagebox.showinfo("OOPS","You shouldnt leave any fields empty")

    else:
        new_data={
            web:{
            "Email":user_name,
            "Password":password,
            },
        }

        try:
            with open("data.json", "r") as file:
                    data=json.load(file)
        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
            new_data.update(data)
            with open("data.json","w") as file:
                json.dump(new_data,file,indent=4)
        finally:
            pass_input.delete(0, 'end')
            web_input.delete(0, 'end')
            messagebox.showinfo("Success","Successfully added")

# ---------------------------- UI SETUP ------------------------------- #
window.minsize(height=500,width=500)
window.config(padx=20,pady=20)
window.title("Password Manager")
canva=Canvas(window,width=200,height=200)
myimg=PhotoImage(file="C:/Users/herne/Downloads/password-manager-start/logo.png")
canva.create_image(100,100,image=myimg)
canva.grid(row=0,column=2)
label=Label(text="   Web site: ")
label.grid(row=1,column=1)
web_input=Entry(window,width=35)
web_input.grid(row=1,column=2)
search_btn=Button(text="Search",highlightthickness=0,width=15,command=find_password,bg="blue")
search_btn.grid(row=1,column=3)
user_label=Label(text="Email/Username: ")
user_label.grid(row=2,column=1)
user_input=Entry(window,width=35)
user_input.insert(0,"vanshika.saxena@gmail.com")
user_input.grid(row=2,column=2)
pass_label=Label(text="Password:")
pass_label.grid(row=3,column=1)
pass_input=Entry(window,width=21)
pass_input.grid(row=3,column=2)
pass_btn=Button(text="Generate Password",highlightthickness=0,command=password_generator,bg="grey")
pass_btn.grid(row=3,column=3)
add_btn=Button(text="Add",width=36,command=save_pass,bg="yellow")
add_btn.grid(row=4,column=2)


window.mainloop()