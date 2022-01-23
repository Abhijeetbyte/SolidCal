from tkinter import * # all


root=Tk() #call tkinter function
root.geometry("320x480") #Width x Height (320,480)
root.resizable(False,False) # window always stay in same size 
root.title("Cylinder Volume Calculator") #Title bar


# Creating object of photoimage class
p1= PhotoImage(file = 'wincon.png')
root.iconphoto(False, p1)# Setting icon of master window

 
# setting variables types for entry feild

heightValue=DoubleVar() 
radiusValue=DoubleVar()
unit_List= ["mm","cm","in"] #list of options
unitVarible=StringVar() #varible to store selected unit
unitVarible.set("Select") # set the placeholder


# Controle Structure/Logic----------------------------------------------------------------------------



def show_selected(*args): #function to get Selected value from list DropDown menu ( show_selected, button command)
    
      global Selected_unit #Value of varible (created in function) outside the function
      Selected_unit = unitVarible.get() # getting selected unit from stored varible
      
show_selected() #function close




def Calculate_Vol(*args): #function to Calculate volume ( Calculate_Vol, button command)

    #Get appropriate Dividing constant as per Unit selected
  
    
    print('Unit ',Selected_unit) # For Shell

    if Selected_unit =='mm':
       Liters_Constant = float(1000000) # divide the volume value by 1000000 to change in leters
       print(Liters_Constant,' constant in mm')# For Shell
       
    elif Selected_unit == 'cm':
       Liters_Constant = float(1000)# divide the volume value by 1000
       print(Liters_Constant,' constant in Cm')
      
    elif Selected_unit == 'in':
       Liters_Constant = float(61.024) #  divide the volume value by 61.024
       print(Liters_Constant,' constant in inches')
       

    #Conversion of parameters into Cubic Units and Liters
   

    HEIGHT = float(heightEntry.get()) # Get data from entry feild varible
    RADIUS = float(radiusEntry.get())

    PI=22/7 # Value of PI

    print(HEIGHT) # For Shell
    print(RADIUS)
    
    CubicUnits=(PI*RADIUS*RADIUS*HEIGHT)#Volume of cylinder is PI x R2 x H (varible created in function)
     
    Liters=(CubicUnits/Liters_Constant) # divide the volume value by liters constant
                                        # liters constant changes according to selected units for correct conversion into liters
                                        
    Round_Liters = float(round(Liters,3)) #Rounding off by 2 decimal places
    Round_CubicUnits=float( round(CubicUnits,3))
    
    print(Round_Liters,'Liters')# For Shell
    print(Round_CubicUnits,'Cubic uints')

    
    #Push Results to GUI labels
    
    L6=Label(text=f"{Round_CubicUnits} {unitVarible.get()}3 ",font=('Helvetica',12,'bold'),bg="#FFFFFF",width=25, height=3).place(x=30,y=300)
    L7=Label(text=f"{Round_Liters} Liters ",font=('Helvetica',12,'bold'),bg="#FFFFFF",width=25, height=2).place(x=30,y=350)




def CLEAR(*args): # Function to clear/reset all input feilds ( CLEAR, button command)
    
    unitVarible.set("Select") #clear unit selection
    heightValue.set("")#clear input feilds parameters
    radiusValue.set("")
    Round_CubicUnits=()# clear result varible
    Round_Liters=()
    
    L6=Label(text=f"",font=('Helvetica',12,'bold'),bg="#FFFFFF",width=25, height=3).place(x=30,y=300) #Clear labels (empty label)
    L7=Label(text=f"",font=('Helvetica',12,'bold'),bg="#FFFFFF",width=25, height=2).place(x=30,y=350)
    
    print(" Clear ")

CLEAR()#function close


   
# Graphical User Interface (GUI)---------------------------------------------------------------------------------------------------------                                        



# Labels
L0=Label(root,font=('Helvetica',18,'bold'),text="Cylinder Volume Calculator",justify=CENTER,bg="#8abbff",width=100) #Head Label
L0.pack(padx=2)

L1=Label(text="Parameters",font=("Courier", 16, "italic")).place(x=90,y=50) #Text, FontSize/style, Location ( input parameters )

L2=Label(text="Height",font=20).place(x=20,y=100) # Text, FontSize, Location 
L3=Label(text="Radius",font=20).place(x=20,y=150)
L4=Label(text="Unit",font=20).place(x=20,y=200)

L5=Label(text="Results",font=("Courier", 16, "italic")).place(x=105,y=250) #Text, FontSize/style, Location ( Result )


# Creating widget/ DropDown Menu
dropDownMenu = OptionMenu(root,unitVarible,*unit_List, command = show_selected ) #DropDown menu, Varible, Unit list/optons & command
dropDownMenu.pack(expand=True)
dropDownMenu.place(x=80,y=200) #location of DropDown menu 


#Entry feilds
heightEntry=Entry(root,textvariable=heightValue,width=20,bd=3,font=20) # Entry/Input feild for height
heightEntry.place(x=80,y=100) #location of entry feild

radiusEntry=Entry(root,textvariable=radiusValue,width=20,bd=3,font=20) # Entry/Input  feild for radius
radiusEntry.place(x=80,y=150)


#Buttons
Clear_Button=Button(text ="Clear",font=('Helvetica',12,'bold'), bg="#8abbff",fg="black",width=8,height=1, command = CLEAR).place(x=30,y=430) #Clear All command button & location 
Cal_Button=Button(text ="Calculate",font=('Helvetica',12,'bold'), bg="#8abbff",fg="black",width=8,height=1, command = Calculate_Vol ).place(x=200,y=430) #Calculte Volume command button & location 


root.mainloop() #Execute tkinter
