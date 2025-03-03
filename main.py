import time
import winsound
import customtkinter



class App(customtkinter.CTk):
    #* Gui
    def __init__(self):
        super().__init__()

        self.title('Countdown timer')
        self.eval('tk::PlaceWindow . center')
        self.resizable(width=False, height=False)
        self.geometry('160x140')
        self.grid_rowconfigure((0, 1), weight=5)
        self.grid_columnconfigure((0, 1, 2), weight=5)

        self.label = customtkinter.CTkLabel(self, text='Countdown:\n', font=('Arial', 15), width=30)
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky='new') 
        self.timer = customtkinter.CTkLabel(self, text='00:00', font=('Arial', 16), width=40)
        self.timer.grid(row=0, column=0, padx=5, pady=4, sticky='sew')

        self.entry = customtkinter.CTkEntry(self, placeholder_text='Enter amount of seconds.', width=158)
        self.entry.grid(row=1, column=0, padx=5, pady=0, sticky='w')

        self.button = customtkinter.CTkButton(self, text='Start countdown', command=self.event, width=158)
        self.button.grid(row=2, column=0, padx=5, pady=5, sticky='w')

    #* Timer
    def countdown(self, usr_ti):
        if usr_ti >= 0:
            mins, sec = divmod(usr_ti, 60)
            timer = '{:02d}:{:02d}'.format(mins, sec)
            self.timer.configure(text=timer)
            if usr_ti >= 0:
                self.after(1000, self.countdown, usr_ti - 1)
        else:
            winsound.PlaySound(sound="SystemHand", flags=winsound.SND_ALIAS)

    def event(self):
        try:
            usr_ti = int(self.entry.get())
            self.countdown(usr_ti)
        except ValueError:
            self.timer.configure(text="Invalid input")

app = App()

if __name__ == '__main__':
    app.mainloop()















# try:
#     usr_t = int(input('Enter Total Number of Seconds for Countdown Timer:\n'))
#     countdown(usr_t)
# except ValueError:
#     print("An error occurred.")
#     exit()
# except KeyboardInterrupt:
#     print("Shutting off.")
#     exit()