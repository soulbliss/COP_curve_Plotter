# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Heady
###########################################################################

class Heady ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 364,346 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		paddy = wx.BoxSizer( wx.VERTICAL )
		
		self.sometext = wx.StaticText( self, wx.ID_ANY, u"Input a temp value within range -25°C to 15°C for the Evaporator", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sometext.Wrap( -1 )
		self.sometext.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		paddy.Add( self.sometext, 0, wx.ALL, 5 )
		
		self.tect = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		paddy.Add( self.tect, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Accept_temp = wx.Button( self, wx.ID_ANY, u"Click to Enter", wx.DefaultPosition, wx.DefaultSize, 0 )
		paddy.Add( self.Accept_temp, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		chotubox = wx.GridSizer( 0, 2, 0, 0 )
		
		self.leftbox = wx.Button( self, wx.ID_ANY, u"P vs H", wx.DefaultPosition, wx.DefaultSize, 0 )
		chotubox.Add( self.leftbox, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.righbox = wx.Button( self, wx.ID_ANY, u"COP vs Temp", wx.DefaultPosition, wx.DefaultSize, 0 )
		chotubox.Add( self.righbox, 0, wx.ALL|wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		
		paddy.Add( chotubox, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( paddy )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Accept_temp.Bind( wx.EVT_BUTTON, self.To_accep_temp )
		self.leftbox.Bind( wx.EVT_BUTTON, self.pvsh )
		self.righbox.Bind( wx.EVT_BUTTON, self.copvstemp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def To_accep_temp( self, event ):
		event.Skip()
	
	def pvsh( self, event ):
		event.Skip()
	
	def copvstemp( self, event ):
		event.Skip()
	

