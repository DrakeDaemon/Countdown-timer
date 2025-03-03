import time
import winsound
import customtkinter

sound1 = 'waterdrop'

class App(customtkinter.CTk):
    #* Gui
    def __init__(self):
        super().__init__()

        self.title('Countdown timer')
        self.eval('tk::PlaceWindow . center')
        self.resizable(width=False, height=False)
        self.geometry('160x210')
        self.grid_rowconfigure((0, 1), weight=5)
        self.grid_columnconfigure((0, 1, 2), weight=5)

        self.label = customtkinter.CTkLabel(self, text='Countdown:\n', font=('Arial', 15), width=30, justify='center')
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky='new') 
        self.timer = customtkinter.CTkLabel(self, text='00:00', font=('Arial', 16), width=40)
        self.timer.grid(row=0, column=0, padx=5, pady=25, sticky='n')

        self.entry = customtkinter.CTkEntry(self, placeholder_text='Amount of seconds.', width=158)
        self.entry.grid(row=4, column=0, padx=5, pady=0, sticky='w')

        self.sound_label = customtkinter.CTkLabel(self, text='Select your sound:', font=('Arial', 12))
        self.sound_label.grid(padx=5, row=2, column=0, sticky='w')
        self.combo = customtkinter.CTkComboBox(self, values=['Water Drop', 'Loud', 'Notification', 'Success'])
        self.combo.grid(padx=5, pady=5, column=0, row=3, sticky='sew')

        self.button = customtkinter.CTkButton(self, text='Start countdown', command=self.event, width=158)
        self.button.grid(row=5, column=0, padx=5, pady=5, sticky='w')

    #* Timer
    def countdown(self, usr_ti, sound1):
        if usr_ti > 0:
            mins, sec = divmod(usr_ti, 60)
            timer = '{:02d}:{:02d}'.format(mins, sec)
            self.timer.configure(text=timer)
            self.after(1000, self.countdown, usr_ti - 1, sound1)
        else:
            self.timer.configure(text='00:00')
            winsound.PlaySound(sound=f"sounds\{sound1}.wav", flags=winsound.SND_ALIAS)

    def event(self):
        try:
            sound1 = self.combo.get().lower().replace(' ', "")
            usr_ti = int(self.entry.get())
            self.countdown(usr_ti, sound1)
        except ValueError:
            self.timer.configure(text="Invalid input")

app = App()

if __name__ == '__main__':
    app.mainloop()