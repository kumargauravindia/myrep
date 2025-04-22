import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        self.panel = wx.Panel(self)
        self.text1 = wx.TextCtrl(self.panel, pos=(10, 10))
        self.text2 = wx.TextCtrl(self.panel, pos=(10, 40))
        self.result = wx.TextCtrl(self.panel, pos=(10, 70), style=wx.TE_READONLY)
        
        self.button = wx.Button(self.panel, label="Sum", pos=(10, 100))
        self.button.Bind(wx.EVT_BUTTON, self.on_click)
        
        self.SetSize((250, 200))
        self.SetTitle('Sum of Two Numbers')
        self.Centre()
        self.Show()

    def on_click(self, event):
        num1 = self.text1.GetValue()
        num2 = self.text2.GetValue()
        try:
            sum_result = float(num1) + float(num2)
            self.result.SetValue(str(sum_result))
        except ValueError:
            self.result.SetValue("Invalid input")

app = wx.App(False)
MyFrame(None)
app.MainLoop()
