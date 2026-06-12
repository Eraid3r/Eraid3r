
import tkinter.messagebox
from tkinter import*
from tkinter import ttk
import sys
import time
def scrolltxt (text):
     for char in text:
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.04)


scrolltxt ("Hello user! May I get your name?")
name = input(">")
scrolltxt ("Why hello ")

print (name + "!")

scrolltxt ('''Welcome to Eric's Resistor Color Code Calculator programed in...
Python3! ''')
scrolltxt ('''This took me several days and many sessions of trouble shooting.
''')
scrolltxt ('''Now, before we can begin.
May I get a password?''')


while True:
     
     password = input(">")
     if password == "R3sistC@lc":
          scrolltxt ("Great! The program is open. Just click on the app icon and find the window!")
          

          

          class Resistor:
           
               def __init__(self, root):  
                                    
                   #setting up the graphics for the main menu
                   self.root = root
                   self.root.title("Resistor Calculator")
                   self.root.geometry("1352x652+0+0")
                   self.root.configure(background="Dark Grey")

                   var1 = IntVar()
                   var2 = IntVar()
                   var3 = IntVar()
                   var4 = StringVar()
                   var5 = IntVar()
                   var6 = IntVar()
                   var7 = IntVar()
                   var8 = IntVar()
                   var9 = IntVar()

                   var1.set("")
                   var2.set("")
                   var3.set("")
                   var4.set("")
                   var5.set("")
                   var6.set("")
                   var7.set("")
                   var8.set("")
                   var9.set("")
                   
          #=============================================================================================================================================#
                   
                   def Band1_Black():
                        var1.set(0)
                   def Band1_Brown():
                        var1.set(1)
                   def Band1_Red():
                        var1.set(2)
                   def Band1_Orange():
                        var1.set(3)
                   def Band1_Yellow():
                        var1.set(4)
                   def Band1_Green():
                        var1.set(5)
                   def Band1_Blue():
                        var1.set(6)
                   def Band1_Violet():
                        var1.set(7)
                   def Band1_Grey():
                        var1.set(8)
                   def Band1_White():
                        var1.set(9)     
          #=============================================================================================================================================#

                   def Band2_Black():
                        var2.set(0)
                   def Band2_Brown():
                        var2.set(1)
                   def Band2_Red():
                        var2.set(2)
                   def Band2_Orange():
                        var2.set(3)
                   def Band2_Yellow():
                        var2.set(4)
                   def Band2_Green():
                        var2.set(5)
                   def Band2_Blue():
                        var2.set(6)
                   def Band2_Violet():
                        var2.set(7)
                   def Band2_Grey():
                        var2.set(8)
                   def Band2_White():
                        var2.set(9)     
          #=============================================================================================================================================#
                   
                   def Multiplier_Black():
                        var3.set(1)
                   def Multiplier_Brown():
                        var3.set(10)
                   def Multiplier_Red():
                        var3.set(100)
                   def Multiplier_Orange():
                        var3.set(1000)
                   def Multiplier_Yellow():
                        var3.set(10000)
                   def Multiplier_Green():
                        var3.set(100000)
                   def Multiplier_Blue():
                        var3.set(1000000)
                   def Multiplier_Violet():
                        var3.set(10000000)
                   def Multiplier_Grey():
                        var3.set(100000000)
                   def Multiplier_White():
                        var3.set(1000000000)
                   def Multiplier_Gold():
                        var3.set(0.1)
          #=============================================================================================================================================#
                   def Tolerance_Gold():
                        var4.set(0.05)
                   def Tolerance_Silver():
                        var4.set(0.1)
                   def Tolerance_None():
                        var4.set(0.2)
          #=============================================================================================================================================#
                   def IExit():
                        IExit = tkinter.messagebox.askyesno("Resistor Color Code Calculator", "Would you like to exit?")
                        if IExit > 0:
                             root.destroy()
                             scrolltxt ('''

I hope you liked the program!''')
                             return

                       

                   

                   def IReset():
                        IReset = tkinter.messagebox.askyesno("Resistor Color Code Calculator", "Would you like to restart?")
                        if IReset > 0:
                             var1.set("")
                             var2.set("")
                             var3.set("")
                             var4.set("")
                             var5.set("")
                             var6.set("")
                             var7.set("")
                             var8.set("")
                             var9.set("")
                             return
                   def CalculateResistor():
                        var9 = "%d%d" %((var1.get(),var2.get()))
                        t = float(var9)
                        m = float(var3.get())
                        s = float(var4.get())
                        if (s == 0.05):
                             q = ((t * m) / 1000) * 0.05
                             a = (q)
                             var5.set(str('%.1f'%(a)))
                             var6.set(str('%.1f'%(t) + 'k ohms'))
                             var7.set(str('%.1f'%(t - q) + 'k ohms'))
                             var8.set(str('%.1f'%(t + q) + 'k ohms'))
                             
                        elif (s == 0.1):
                             q = ((t * m) / 1000) * 0.1
                             a = (q)
                             var5.set(str('%.1f'%(a)))
                             var6.set(str('%.1f'%(t) + 'k ohms'))
                             var7.set(str('%.1f'%(t - q) + 'k ohms'))
                             var8.set(str('%.1f'%(t + q) + 'k ohms'))
                        elif (s == 0.2):
                             q = ((t * m) / 1000) * 0.2
                             a = (q)
                             var5.set(str('%.1f'%(a)))
                             var6.set(str('%.1f'%(t) + 'k ohms'))
                             var7.set(str('%.1f'%(t - q) + 'k ohms'))
                             var8.set(str('%.1f'%(t + q) + 'k ohms'))
                              
                    
                   mainFrame = Frame(self.root, bg = 'Dark Grey')
                   mainFrame.grid()

                   #Creating a rectangle frame for title card
                   TitleFrame = Frame(mainFrame, bd=10, width = 1650, padx=3, bg = 'Black', relief = RIDGE)
                   TitleFrame.grid(row=0, column=0, columnspan = 2)
                   self.lbTitle = Label(TitleFrame, font=('Times New Roman' ,50, 'bold'),text="Resistor Color Code Calculator",padx=215, bg = 'silver')
                   self.lbTitle.grid(row = 0, column = 0,)
                   #creating frame that will have our resistor values
                   ResistorFrame = Frame(mainFrame, bd=10, width = 1650, padx=20, bg = 'silver', relief = RIDGE)
                   ResistorFrame.grid(row=1, column=0, sticky = E)
                   #Indicator frame
                   IndicatorFrame = Frame(mainFrame, bd=10, width = 1650, padx=10, bg = 'silver', relief = RIDGE)
                   IndicatorFrame.grid(row=1, column=1,sticky = W)


                   #labels buttons below.
                   self.lblTitle = Label(ResistorFrame, font=('Times New Roman' ,15, 'bold'),text="1st Band", padx=10, bg = 'silver')
                   self.lblTitle.grid(row=0,column=0)
                   self.lblTitle = Label(ResistorFrame, font=('Times New Roman' ,15, 'bold'),text="2nd Band", bg = 'silver')
                   self.lblTitle.grid(row=0,column=1)
                   self.lblTitle = Label(ResistorFrame, font=('Times New Roman' ,15, 'bold'),text="Multiplier", bg = 'silver')
                   self.lblTitle.grid(row=0,column=2)
                   self.lblTitle = Label(ResistorFrame, font=('Times New Roman' ,15, 'bold'),text="Tolerance", bg = 'silver')
                   self.lblTitle.grid(row=0,column=3)

                   
                   #Creating the first button for the program
                   #(fg affects color of font when button is pressed)
                   #(bg affects color of text when color is not pressed) 
                   self.bkcolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'black', fg = 'white', bg = 'black',
                                          command = Band1_Black,)
                   self.bkcolor1.grid(row = 1, column = 0)
                   self.bkcolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '0', fg = 'white', bg = 'black',
                                          command = Band2_Black,)
                   self.bkcolor2.grid(row = 1, column = 1)
                   self.bkcolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '1', fg = 'white', bg = 'black',
                                          command = Multiplier_Black,)
                   self.bkcolor3.grid(row = 1, column = 2)
                   self.bkcolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'white', bg = 'black')
                   self.bkcolor4.grid(row = 1, column = 3)
                   
           #=====================================================================================================================================================================#
                   self.browncolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'brown', fg = 'black', bg = 'brown',
                                             command = Band1_Brown,)
                   self.browncolor1.grid(row = 2, column = 0)
                   self.browncolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '1', fg = 'white', bg = 'brown',
                                             command = Band2_Brown,)
                   self.browncolor2.grid(row = 2, column = 1)
                   self.browncolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '10', fg = 'white', bg = 'brown',
                                             command = Multiplier_Brown,)
                   self.browncolor3.grid(row = 2, column = 2)
                   self.browncolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'white', bg = 'brown')
                   self.browncolor4.grid(row = 2, column = 3)

           #=========================================================================================================================================================================#
                   self.redcolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'red', fg = 'black', bg = 'red',
                                           command = Band1_Red,)
                   self.redcolor1.grid(row = 3, column = 0)
                   self.redcolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '2', fg = 'white', bg = 'red',
                                           command = Band2_Red,)
                   self.redcolor2.grid(row = 3, column = 1)
                   self.redcolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '100', fg = 'white', bg = 'red',
                                           command = Multiplier_Red,)
                   self.redcolor3.grid(row = 3, column = 2)
                   self.redcolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'white', bg = 'red')
                   self.redcolor4.grid(row = 3, column = 3)
           #=========================================================================================================================================================================#
                   self.orangecolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'orange', fg = 'black', bg = 'orange',
                                              command = Band1_Orange,)
                   self.orangecolor1.grid(row = 4, column = 0)
                   self.orangecolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '3', fg = 'white', bg = 'orange',
                                              command = Band2_Orange,)
                   self.orangecolor2.grid(row = 4, column = 1)
                   self.orangecolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '1000', fg = 'white', bg = 'orange',
                                              command = Multiplier_Orange,)
                   self.orangecolor3.grid(row = 4, column = 2)
                   self.orangecolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'white', bg = 'orange')
                   self.orangecolor4.grid(row = 4, column = 3)
          #=========================================================================================================================================================================#
                   self.yellowcolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'yellow', fg = 'black', bg = 'yellow',
                                              command = Band1_Yellow,)
                   self.yellowcolor1.grid(row = 5, column = 0)
                   self.yellowcolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '4', fg = 'white', bg = 'yellow',
                                              command = Band2_Yellow,)
                   self.yellowcolor2.grid(row = 5, column = 1)
                   self.yellowcolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '10000', fg = 'white', bg = 'yellow',
                                              command = Multiplier_Yellow)
                   self.yellowcolor3.grid(row = 5, column = 2)
                   self.yellowcolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'white', bg = 'yellow')
                   self.yellowcolor4.grid(row = 5, column = 3)
          #=========================================================================================================================================================================#
                   self.greencolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'green', fg = 'black', bg = 'green',
                                             command = Band1_Green,)
                   self.greencolor1.grid(row = 6, column = 0)
                   self.greencolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '5', fg = 'white', bg = 'green',
                                             command = Band2_Green,)
                   self.greencolor2.grid(row = 6, column = 1)
                   self.greencolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '100000', fg = 'white', bg = 'green',
                                             command = Multiplier_Green,)
                   self.greencolor3.grid(row = 6, column = 2)
                   self.greencolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'white', bg = 'green')
                   self.greencolor4.grid(row = 6, column = 3)
          #=========================================================================================================================================================================#
                   self.bluecolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'blue', fg = 'black', bg = 'blue',
                                            command = Band1_Blue,)
                   self.bluecolor1.grid(row = 7, column = 0)
                   self.bluecolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '6', fg = 'white', bg = 'blue',
                                            command = Band2_Blue,)
                   self.bluecolor2.grid(row = 7, column = 1)
                   self.bluecolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '1000000', fg = 'white', bg = 'blue',
                                            command = Multiplier_Blue,)
                   self.bluecolor3.grid(row = 7, column = 2)
                   self.bluecolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'white', bg = 'blue')
                   self.bluecolor4.grid(row = 7, column = 3)
          #=========================================================================================================================================================================#
                   self.violetcolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'violet', fg = 'black', bg = 'violet',
                                              command = Band1_Violet,)
                   self.violetcolor1.grid(row = 8, column = 0)
                   self.violetcolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '7', fg = 'white', bg = 'violet',
                                              command = Band2_Violet,)
                   self.violetcolor2.grid(row = 8, column = 1)
                   self.violetcolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '10000000', fg = 'white', bg = 'violet',
                                              command = Multiplier_Violet,)
                   self.violetcolor3.grid(row = 8, column = 2)
                   self.violetcolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'white', bg = 'violet')
                   self.violetcolor4.grid(row = 8, column = 3)
          #=========================================================================================================================================================================#
                   self.greycolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'grey', fg = 'black', bg = 'grey',
                                            command = Band1_Grey,)
                   self.greycolor1.grid(row = 9, column = 0)
                   self.greycolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '8', fg = 'white', bg = 'grey',
                                            command = Band2_Grey,)
                   self.greycolor2.grid(row = 9, column = 1)
                   self.greycolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '100000000', fg = 'white', bg = 'grey',
                                            command = Multiplier_Grey,)
                   self.greycolor3.grid(row = 9, column = 2)
                   self.greycolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'white', bg = 'grey')
                   self.greycolor4.grid(row = 9, column = 3)
          #=========================================================================================================================================================================#
                   self.whitecolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'white', fg = 'black', bg = 'white',
                                             command = Band1_White,)
                   self.whitecolor1.grid(row = 10, column = 0)
                   self.whitecolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '9', fg = 'black', bg = 'white',
                                             command = Band2_White,)
                   self.whitecolor2.grid(row = 10, column = 1)
                   self.whitecolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '1000000000', fg = 'black', bg = 'white',
                                             command = Multiplier_White)
                   self.whitecolor3.grid(row = 10, column = 2)
                   self.whitecolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'black', bg = 'white')
                   self.whitecolor4.grid(row = 10, column = 3)
          #=========================================================================================================================================================================#
                   self.goldcolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'gold', fg = 'black', bg = 'gold',)
                   self.goldcolor1.grid(row = 11, column = 0)
                   
                   self.goldcolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'black', bg = 'gold')
                   self.goldcolor2.grid(row = 11, column = 1)
                   
                   self.goldcolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = '0.1', fg = 'black', bg = 'gold',
                                            command = Multiplier_Gold,)
                   self.goldcolor3.grid(row = 11, column = 2)
                   
                   self.goldcolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = "5%", fg = 'black', bg = 'gold',
                                            command = Tolerance_Gold, )
                   self.goldcolor4.grid(row = 11, column = 3)
          #=========================================================================================================================================================================#
                   self.silvercolor1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'silver', fg = 'black', bg = 'silver',)
                   self.silvercolor1.grid(row = 12, column = 0)
                   
                   self.silvercolor2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'black', bg = 'silver')
                   self.silvercolor2.grid(row = 12, column = 1)
                   
                   self.silvercolor3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'black', bg = 'silver')
                   self.silvercolor3.grid(row = 12, column = 2)
                   
                   self.silvercolor4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = "10%", fg = 'black', bg = 'silver',
                                              command = Tolerance_Silver, )
                   self.silvercolor4.grid(row = 12, column = 3)
          #=========================================================================================================================================================================#
                   self.none1 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = 'none', fg = 'black', bg = 'white')
                   self.none1.grid(row = 13, column = 0)
                   
                   self.none2 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'black', bg = 'white')
                   self.none2.grid(row = 13, column = 1)
                   
                   self.none3 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), fg = 'black', bg = 'white')
                   self.none3.grid(row = 13, column = 2)
                   
                   self.none4 = Button(ResistorFrame, width = 16, font=('Times New Roman' ,14, "bold"), text = "20%", fg = 'black', bg = 'white',
                                       command = Tolerance_None, )
                   
                   self.none4.grid(row = 13, column = 3)

          #=============================================================Indicator Frame============================================================================================================
                   self.lblFirst = Label(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="1st Band", bg = 'silver')
                   self.lblFirst.grid(row=0,column=0,sticky = W,pady = 10)
                   self.txtFirst = Entry(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),width = 24, textvariable = var1)
                   self.txtFirst.grid(row=0,column=1,pady = 10, columnspan = 3)
                   
                   self.lblSecond = Label(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="2nd Band", bg = 'silver')
                   self.lblSecond.grid(row=1,column=0,sticky = W,pady = 10 , )
                   self.txtSecond = Entry(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),width = 24, textvariable = var2)
                   self.txtSecond.grid(row=1,column=1,sticky = W,pady = 10, columnspan = 3)

                   self.lblMultiplier = Label(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="Multiplier", bg = 'silver')
                   self.lblMultiplier.grid(row=2,column=0,sticky = W,pady = 10)
                   self.txtMultiplier = Entry(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),width = 24, textvariable = var3)
                   self.txtMultiplier.grid(row=2,column=1,sticky = W,pady = 10, columnspan = 3)

                   self.lblTolerance = Label(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="Tolerance", bg = 'silver')
                   self.lblTolerance.grid(row=3,column=0,sticky = W,pady = 10)
                   self.txtTolerance = Entry(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),width = 24, textvariable = var4)
                   self.txtTolerance.grid(row=3,column=1,sticky = W,pady = 10, columnspan = 3)
                   
                   self.lblDivideBy1000 = Label(IndicatorFrame, font=('Times New Roman' ,15, 'bold'),text="Divide By 1000", bg = 'silver')
                   self.lblDivideBy1000.grid(row=4,column=0,sticky = W,pady = 10)
                   self.txtDivideBy1000 = Entry(IndicatorFrame, font=('Times New Roman' ,16, 'bold'), width = 24, textvariable = var5)
                   self.txtDivideBy1000.grid(row=4,column=1,sticky = W,pady = 10, columnspan = 3)

                   
                   
                   self.lblResistorValue = Label(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="Resistor Value", bg = 'silver')
                   self.lblResistorValue.grid(row=5,column=0,sticky = W,pady = 10)
                   self.txtResistorValue = Entry(IndicatorFrame, font=('Times New Roman' ,16, 'bold'), width = 24, textvariable = var6)
                   self.txtResistorValue.grid(row=5,column=1,sticky = W,pady = 10, columnspan = 3)

                   self.lblMinRange = Label(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="Min Range", bg = 'silver')
                   self.lblMinRange.grid(row=6,column=0,sticky = W,pady = 10)
                   self.txtMinRange = Entry(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),width = 24, textvariable = var7)
                   self.txtMinRange.grid(row=6,column=1,pady = 10, columnspan = 3)
                   
                   self.lblMaxRange = Label(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="Max Range", bg = 'silver')
                   self.lblMaxRange.grid(row=7,column=0,sticky = W, pady = 10)
                   self.txtMaxRange = Entry(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),width = 24, textvariable = var8)
                   self.txtMaxRange.grid(row=7,column=1, pady = 10, columnspan = 3)

                   btncalc= Button(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="Calculate", width = 8, height = 4,
                                   command = CalculateResistor)
                   
                   btncalc.grid(row = 8, column = 0, pady = 10)
                   
                   btnRe= Button(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="Restart", width = 8, height = 4, command = IReset)
                   btnRe.grid(row = 8, column = 1, pady = 10)
                   
                   btnExit= Button(IndicatorFrame, font=('Times New Roman' ,16, 'bold'),text="Exit", width = 8, height = 4, command = IExit)
                   btnExit.grid(row = 8, column = 2, pady = 10)






                   
          if __name__=='__main__':
              root = Tk()
              application = Resistor(root)
              root.mainloop()

              
     else:
          scrolltxt ("Try Again!")
          #Password is R3sistC@lc