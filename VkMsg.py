The code creates a window program that, when launched, asks the user to enter the vk token of the session to be accessed, then the fields "dialog number" and "message" are filled in


    from tkinter import *
    from tkinter import messagebox
    import subprocess
    import vk_api
    import webbrowser

    def information():
        messagebox.showinfo("Важно!","Данная программа еще вышла с Beta-версии 0.302.031.1     О всех найденных ошибках просим уведомить разработчика")

    information()


    def exxt():
        window.destroy()


    def tok():
        messagebox.showinfo("Внимание!", "Выберите параметр [Сообщения] для стабильной работы программы , после введите ваш токен в программе")
        webbrowser.open_new("https://vkhost.github.io")



    def click():


        def send(msg):




            vk.messages.send(user_id = txt_id.get(), message = msg, random_id = 0)


        def click():

            password = txt_password.get()


            if password:
                send(password)
            else:
                messagebox.showinfo("Ошибка!","Введите текст")

        def delete_text():
            txt_password.delete("0", "end")
        def delete_dialog():
            txt_id.delete("0", "end")

        def ext():
            win.destroy()



        my_token = text.get()   
        session = vk_api.VkApi(token = my_token)
        vk = session.get_api()


        win = Tk()
        win.geometry("400x300")
        win.title("Сообщения в вк")
        win.resizable(width=False, height=False)


        menu = Menu(win)  
        new_item = Menu(menu)  
        new_item.add_command(label='Очисить номер диалога', command=delete_dialog)  
        new_item.add_command(label='Очисить сообщение', command=delete_text)  
        new_item.add_command(label='Справка') 
        menu.add_cascade(label='Файл', menu=new_item)  
        win.config(menu=menu)  


        ttk = Label(win, text="Отправка сообщений в ВК", font="Arial, 20")
        ttk.grid(padx=40, pady=10)

        ttk = Label(win, text="Введите номер переписки", font="Arial, 10")
        ttk.grid(padx=20, pady=0)

        txt_id = Entry(win, width=30)
        txt_id.grid(padx=20, pady=5)


        ttk = Label(win, text="Введите текст", font="Arial, 10")
        ttk.grid(padx=20, pady=0)

        txt_password = Entry(win, width=30)
        txt_password.grid(padx=20, pady=5)

        btn = Button(win, text="Отправить", font="Arial, 15", command=click)
        btn.grid(padx=60, pady=20)
        bttn = Button(win, text="Закрыть программу", font="Arial, 15", command=ext)
        bttn.grid(padx=60, pady=0)
        win.mainloop()

    window = Tk()
    window.geometry("400x300")
    window.title("Сообщения в вк")
    window.resizable(width=False, height=False)

    txt = Label(window, text="Введите ваш токен", font="Arial, 15")
    txt.grid(padx=100, pady=0)
    text = Entry(window)
    text.grid(padx=100, pady=20)


    btn = Button(window, text="Запустить программу", font="Arial, 15", command=click)
    btn.grid(padx=100, pady=0)

    btn = Button(window, text="Узнать мой токен", font="Arial, 15", command=tok)
    btn.grid(padx=100, pady=20)

    bttn = Button(window, text="Закрыть программу", font="Arial, 15", command=exxt)
    bttn.grid(padx=60, pady=0)

    window.mainloop()


