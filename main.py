import wx


class MaineR(wx.Frame):

    pc = [None, 0, 0, 0]

    def __init__(self):
        wx.Frame.__init__(self,
                          parent=None,
                          title="MOUSE EVENT TEST",
                          size=(318, 350),
                          style=(wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN))
        self.SetBackgroundColour("#000000")

        #mb  = wx.MenuBar()
        # self.Bind(wx.EVT_TREE_KEY_DOWN)
        # self.ShowFullScreen(True, wx.FULLSCREEN_ALL)

        self.p1 = wx.Panel(self, id=1,  pos=(-1, -1),  size=(100, 200))
        self.p1.Bind(wx.EVT_MOUSEWHEEL, self.onWheel)
        self.p1T = wx.StaticText(self.p1, label=str(self.pc[1]))
        r = wx.StaticText(self.p1, label="RED", pos=(5, 80))

        self.p2 = wx.Panel(self, id=2,  pos=(101, -1),  size=(100, 200))
        self.p2.Bind(wx.EVT_MOUSEWHEEL, self.onWheel)
        self.p2T = wx.StaticText(self.p2, label=str(self.pc[2]))
        g = wx.StaticText(self.p2, label="GREEN", pos=(5, 80))

        self.p3 = wx.Panel(self, id=3,  pos=(202, -1),  size=(100, 200))
        self.p3.Bind(wx.EVT_MOUSEWHEEL, self.onWheel)
        self.p3T = wx.StaticText(self.p3, label=str(self.pc[3]))
        b = wx.StaticText(self.p3, label="BLUE", pos=(5, 80))

        self.p1.SetBackgroundColour("rgb({},{},{})".format(str(self.pc[1]), "000", "000"))
        self.p2.SetBackgroundColour("rgb({},{},{})".format("000", str(self.pc[2]), "000"))
        self.p3.SetBackgroundColour("rgb({},{},{})".format("000", "000", str(self.pc[3])))

        self.panels = [None, self.p1, self.p2, self.p3]
        c = [None, r, g, b]
        self.Texts = [None, self.p1T, self.p2T, self.p3T]

        for i in self.Texts[1:]:
            i.SetFont(wx.Font(30, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
            i.SetForegroundColour("white")

        for i in c[1:]:
            i.SetFont(wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
            i.SetForegroundColour("white")

        self.Center()
        self.Show()

    def onWheel(self, event):
        id = event.Id
        x = event.GetWheelRotation()
        print(x)

        if x > 0:
            if self.pc[id] < 255:
                self.pc[id] += 5
            else:
                self.pc[id] = 0

        else:
            if self.pc[id] > 0:
                self.pc[id] -= 5
            else:
                self.pc[id] = 255

        if id == 1:
            self.panels[id].SetBackgroundColour("rgb({},{},{})".format(str(self.pc[id]), "000", "000"))
            self.Texts[id].SetLabel(str(self.pc[id]))
        elif id == 2:
            self.panels[id].SetBackgroundColour("rgb({},{},{})".format("000", str(self.pc[id]), "000"))
            self.Texts[id].SetLabel(str(self.pc[id]))
        else:
            self.panels[id].SetBackgroundColour("rgb({},{},{})".format("000", "000", str(self.pc[id])))
            self.Texts[id].SetLabel(str(self.pc[id]))

        self.SetBackgroundColour("rgb({},{},{})".format(str(self.pc[1]), str(self.pc[2]), str(self.pc[3])))
        self.Refresh()
        print("MOUSE WHEEL RECEIVED FROM ID [{}], COLOR LEVEL [{}]".format(id, self.pc[id]))


app = wx.App()
frame_obj = MaineR()
app.MainLoop()
