#!/usr/bin/env python3.10

import wx

class WxButton(wx.Frame):

    def __init__(self, *args, **kw):
        super(WxButton, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)
        closeButton = wx.Button(pnl, label='Close Me')

        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer()
        sizer.Add(closeButton, 0, wx.ALIGN_CENTER)
        sizer.AddStretchSpacer()
        pnl.SetSizer(sizer)

        self.SetSize((350, 250))
        self.SetTitle('Close Button')
        self.Centre()

    def OnClose(self, e):
        self.Close(True)

def main():
    app = wx.App()
    ex = WxButton(None)
    ex.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
