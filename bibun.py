# -*- coding: utf-8 -*-

import numpy as np
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider
from bokeh.layouts import column
from bokeh.io import curdoc

h = 1e-5

def getTangentData(a):
    df = (TestFunc(a+h)-TestFunc(a))/h
    txs = np.linspace(-0.5+a,0.5+a,10)
    tys = df*(txs-a)+TestFunc(a)
    return txs, tys

def TestFunc(xs, a=3.0):
    return 1/(1+np.exp(-a*xs))

class DerivViewer(object):
    def __init__(self):
        self.xs = np.linspace(-2.0,2.0,100)
        self.ys = TestFunc(self.xs)

        self.source1 = ColumnDataSource(data=dict(xs=self.xs,ys=self.ys))

        a=0
        txs,tys = getTangentData(a)
        self.source2 = ColumnDataSource(data=dict(txs=txs,tys=tys))

        self.source3 = ColumnDataSource(data=dict(x=[a],y=[TestFunc(a)]))
        self.fig = figure(title='曲線の接線を求める(微分係数を求める)',x_range=(-2.0,2.0),y_range=(-0.2,1.2))

        self.fig.line('xs','ys',source=self.source1)
        self.fig.line('txs','tys',source=self.source2,color='orange')
        self.fig.circle('x','y',source=self.source3,color='red')

        self.slider = Slider(title='position',value=0,start=-1.5,end=1.5,step=0.1)
        self.slider.on_change('value',self.update_data)
        self.plot = column(self.slider,self.fig)

    def update_data(self,attr,old,new):
        a = self.slider.value
        txs, tys = getTangentData(a)
        self.source2.data = dict(txs=txs, tys=tys)
        self.source3.data = dict(x=[a],y=[TestFunc(a)])

def main():
    viewer = DerivViewer()
    document = curdoc()
    document.add_root(viewer.plot)

main()
