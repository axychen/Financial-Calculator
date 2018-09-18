#!/usr/bin/python
import math
import tkinter as tk

root = tk.Tk() #create a window 
#modify the root window
root.title("financial calculator")
root.geometry("400x500") #weight*height

class Calculator(tk.Frame):

    def __init__(self, master =None):
        super().__init__(master)
        self.pack()
        self.create_widgets() #call the first function
        self.inputbox() # here!
        
    def create_widgets (self):
        self.hi = tk.Button(self)
        self.hi["text"] = "Welcome to Finance Calculator\n"  # text in button
        self.hi["command"] =self.say_hi #call another function
        self.hi.pack(side ="top")  #decide this is on top of the other buttons
             
        self.quit = tk.Button( self, text = "Exit", fg = "red", command = root.destroy) #close the program
        self.quit.pack(side ="bottom")
        ''' side can also be left, right or others, it will be alligned with other buttons '''
        
    def inputbox(self):
        self.entry = tk.Entry() # create a user-entry box
        self.entry.pack() 
        self.contents = tk.StringVar() # user can enter their own string
        self.contents.set("type in here") #the default text
        self.entry["textvariable"] = self.contents 
        self.entry.bind('<Key-Return>', self.print_contents)   #new contents will be set with new input
        
    def print_contents(self, event):
            print("hi. contents of entry is now ---->", self.contents.get())        
        
    def say_hi(self):
        #self.PV=input("present value is: ")
        print("your input is ")
    
        

'''
#calculate the future value of the coumpound, ex: saving in a bank account 
def cpFV(year, timepy, interest, capital):
   fv = (1+interest/timepy) ** (year*timepy) * capital
   print("Future value is", fv)
   return

#calculate the year taking for present value to reach the future value, 
def years(interest, PV, FV):
   years = math.log(FV/PV) / math.log(1+interest)
   print ("Year taking to accumulate is",years )
   return 

#calculate the arithmatic and geometriv average
def arithmeticAVG(PV, FV1,FV2):
   interest1 = (FV1-PV)/PV
   interest2 = (FV2-FV1)/FV1
   arithmetic = (interest1 + interest2) / 2
   geometric = (1+ interest1)*(1+interest2)/2
   print("Arithmetic average (garden variety average) is ",arithmetic)
   print("Geometric average (garden variety average) is ",geometric)
   return 

#calculate the conpound annual interest / growth rate 
def cpInterest(FV,PV,year, timepy):
   i=(FV/PV) ** (1/(year *timepy))-1
   print("the compound average (geometric average) ", i)
   return

# calculate the effective interest rate, ex: to find the difference between montly compound and quartly compond
def EIR(interest,year, timepy):
   eir=(1+interest/timepy)**timepy-1
   print("The effective interest rate is ", eir)
   return 


# Annuity Problem starts here

#NEED TO BE TESTED
#pay at each month end, calculate the future receivng value ,lampsum
def anuFV (timePY, year, payment,interest):
    FV=payment*(1 / (interest / timePY)) *[(interest**(timePY*year) )-1] 
    print("The future value will be " FV)
    return

#NEED TO BE TESTED (Q4)
#what you have to have for a lampsum every year investment
def anuPV(timePY, year, payment,interest):
    PV = payment * (1/ (investment/timePY)) * [1 - (1+investment/timePY)**(- (timePY*year)))]
    print("You need to have these money to invest ", PV)
    return
    
    
    
    
    
'''
calculator = Calculator(master = root)
calculator.mainloop()#kick off  event loop
