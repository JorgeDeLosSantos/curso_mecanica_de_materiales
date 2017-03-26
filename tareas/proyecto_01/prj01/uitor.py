# -*- coding: utf-8 -*-
import wx
import ui
import numpy as np

class wxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title="ABC",size=(600,450))
        self.init_ctrls()
        self.SetBackgroundColour("#E5E5E5")
        self.Show()
        
    def init_ctrls(self):
        self.msz = wx.BoxSizer(wx.VERTICAL)
        self.numsz = wx.BoxSizer(wx.HORIZONTAL)
        self.dep = wx.StaticBox(self, -1, 'Datos de entrada')
        self.desz = wx.StaticBoxSizer(self.dep, wx.VERTICAL) 
        self.dsp = wx.StaticBox(self, -1, 'Datos de salida')
        self.dssz = wx.StaticBoxSizer(self.dsp, wx.VERTICAL)
        
        lb = wx.StaticText(self, -1, u"Número de elementos", size=(120,-1))
        self.numel = wx.TextCtrl(self, -1, "", size=(80,-1))
        self.oknumel = wx.Button(self, -1, "OK", size=(40,-1))
        
        # Datos de entrada
        self.input_data = ui.DataGrid(self,(5,5))
        self.desz.Add(self.input_data, 1, wx.EXPAND)
        
        # Datos de salida
        self.output_data = ui.DataGrid(self,(5,2))
        self.dssz.Add(self.output_data, 1, wx.EXPAND)
        
        # Botón calcular
        self.calc = wx.Button(self, -1, "Calcular")
        
        self.numsz.Add(lb, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.numsz.Add(self.numel, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.numsz.Add(self.oknumel, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        
        self.msz.Add(self.numsz, 1, wx.EXPAND)
        self.msz.Add(self.desz, 5, wx.EXPAND|wx.ALL, 5)
        self.msz.Add(self.dssz, 5, wx.EXPAND|wx.ALL, 5)
        self.msz.Add(self.calc, 1, wx.ALL|wx.ALIGN_CENTRE, 5)
        self.SetSizer(self.msz)
        
        colnames = "ID,OD,L,T,G".split(",")
        for k,col in enumerate(colnames):
            self.input_data.SetColLabelValue(k,col)
            
        colnames_out = u"\N{GREEK SMALL LETTER TAU},\N{GREEK SMALL LETTER PHI}".split(",")
        for k,col in enumerate(colnames_out):
            self.output_data.SetColLabelValue(k,col)
            
        self.Bind(wx.EVT_BUTTON,  self.on_numel, self.oknumel)
        self.Bind(wx.EVT_BUTTON,  self.calcular, self.calc)
        
    def on_numel(self,event):
        numel = int(self.numel.GetValue())
        self.input_data.UpdateGridSize(numel,5)
        self.output_data.UpdateGridSize(numel,2)
        
    def calcular(self,event):
        data = self.input_data.GetArrayData()
        ID = data[:,0]
        OD = data[:,1]
        L = data[:,2]
        T = data[:,3]
        G = data[:,4]
        J = np.pi/2*((OD/2)**4-(ID/2)**4)
        
        TS = []
        for k in range(len(T)):
            _ts = sum(T[0:k+1])
            TS.append(_ts)

        TS = np.array(TS)
        phi = ((TS*L)/(J*G))*(180/np.pi)
        tau = (TS*OD)/J
        
        self.output_data.SetArrayData(np.column_stack((tau,phi)))
        
        
if __name__ == '__main__':
    app = wx.App()
    fr = wxFrame()
    app.MainLoop()
