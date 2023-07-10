import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Word Autocomplete')
        panel = wx.Panel(self)
        file = open('popular.txt', 'r')
        
        self.word_list = [s for s in file]
        self.valid_words = []

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5), size=(375,20))

        self.Bind(wx.EVT_TEXT, self.TextUpdated, self.text_ctrl)

        self.list = wx.ListBox(panel, pos=(5,35), size=(375,150))

        self.Show()

    def UpdateList(self, keyword):
        self.valid_words = [s for s in self.word_list if s and keyword and s.startswith(keyword)]
        self.list.Clear()
        self.list.Append(self.valid_words[0:10])

    def TextUpdated(self, ControlEvent):
        text = self.text_ctrl.GetValue()
        self.UpdateList(text)
        pass



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
