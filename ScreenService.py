import tkinter as tk
import tkinter.font as tkFont

class ScreenService:
    def __init__(self, sharedData):
        self.sharedData = sharedData

    def start(self):
        self.window = tk.Tk()
        self.window.configure(background="black")
        self.window.attributes("-fullscreen", True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.window.config(cursor="none")

        self.buildBaseWindow()
        self.window.after(100, self.updateWindowLabels)
        self.window.mainloop()

    def updateWindowLabels(self):
        if 'curTimeString' in self.sharedData:
            self.labelCurTime.config(text=self.sharedData['curTimeString'])
        if 'countDownString' in self.sharedData:
            self.labelCountDown.config(text=self.sharedData['countDownString'])
        if 'showTimeString' in self.sharedData:
            self.labelShowTime.config(text=self.sharedData['showTimeString'])

        # Keep on updating window
        self.window.after(100, self.updateWindowLabels)

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

    def buildBaseWindow(self):
        self.window.rowconfigure((0,1,2), weight=1)
        self.window.columnconfigure(0, weight=1)

        self.buildLabel("labelCurTime", "00:00:00", 0, "#ff0000")
        self.buildLabel("labelCountDown", "00:00:00:00", 1, "#00ff00")
        self.buildLabel("labelShowTime", "00:00:00", 2)

    def buildLabel(self, name, text, row, color="#ffffff"):
        label = tk.Label(
            self.window, text=text, foreground=color, bg="black", font=self.getMainFont()
        )
        label.grid(row=row, column=0, sticky="EW")
        # set self.{name} = label
        setattr(self, name, label)

    def getMainFont(self):
        font = tkFont.Font(size=230, family="alarm clock")
        return font
