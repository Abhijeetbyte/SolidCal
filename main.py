from tkinter import * # all


root=Tk() #call tkinter function
root.geometry("320x480") #Width x Height (320,480)
root.resizable(False,False) # window always stay in same size 
root.title("Volume Calculator") #Title bar

root.iconbitmap('volcon.ico')# Setting icon of master window,The image is of .ico extension 


 
# setting variables types for entry field

heightValue=DoubleVar() 
radiusValue=DoubleVar()

lengthValue=DoubleVar()
widthValue=DoubleVar()

unit_List= ["mm","cm","in"] #list of options
unitVarible=StringVar() #varible to store selected unit
unitVarible.set("Select") # set the placeholder

shape_List= ["Cylinder","Cone","Cuboid","Sphere"] #list of shape options
shapeVarible=StringVar() #varible to store selected shape
shapeVarible.set("Select") # set the placeholder to select



# Controle Structure/Logic---------------------------------------------------------------------



def show_selected_unit(*args): #function to get Selected value from list DropDown menu ( show_selected, button command)

    global Selected_unit #Value of varible (created in function) outside the function

    Selected_unit = unitVarible.get() # getting selected unit from stored varible
      

show_selected_unit()



def show_selected_shape(*args): #function to get Selected shape from list DropDown Menu and Push Entry fields
                                 # and Labels accordangily

    global Selected_shape  # Setting shape varible global for different functions

    Selected_shape = shapeVarible.get() # getting selected shape from stored varible
    

    if Selected_shape =='Cuboid':

          print('Shape Selected : ',Selected_shape) # for shell

          #location of entry field for cuboid [ Only visible when cuboid shape selected]

          radiusEntry.place(x=80,y=110) # in cuboid labeled as Lenght entry field
          heightEntry.place(x=80,y=160)   
          widthEntry.place(x=80,y=205)

          # Location, for first time selection or after;
          
          L3.place(x=20,y=110) # length label
          L3.config(text="Length",font=20)  #length label, change radius to length, if selected after cylinder 

          L2.place(x=20,y=160) # height label
          L4.place(x=20,y=205) # width label         
          L5.place(x=20,y=240) # unit label
    
          dropDownMenu.place(x=80,y=240)#option menu of unit


    elif (Selected_shape =='Cylinder' or  Selected_shape =='Cone'):# both shapes have same entry fields
          
          print('Shape Selected : ',Selected_shape) # for shell

          # Erase unwanted fields and rename and locations

          widthEntry.place_forget()#entry fields , no need forget 
          L4.place_forget() # width label , no need
          

          # Location and name for first time selection or after;
          
          L3.config(text="Radius",font=20)  #length label, change to radius
          L3.place(x=20,y=110) # radius location
          L2.place(x=20,y=160) # height label
          L5.place(x=20,y=210) #unit label, change loction after cuboid or first time placement
          L6.place(x=105,y=270) #Results label, change location
          
          radiusEntry.place(x=80,y=110) # first time placement
          heightEntry.place(x=80,y=160) # first time placement

          dropDownMenu.place(x=80,y=210) #change loction after cuboid or first time placement
          

    elif Selected_shape =='Sphere':

        print('Shape Selected : ',Selected_shape) # for shell

        # Erase unwanted fields and rename and locations

        L2.place_forget() # height label, no need
        L4.place_forget() # width label , no need
        
        widthEntry.place_forget()#entry fields , no need forget
        heightEntry.place_forget()#entry fields , no need forget
          
        L4.place_forget() # width label , no need
        L5.place_forget() #height label, no need

        # Location and name for first time selection or after;

        L3.config(text="Radius",font=20)  #length label, change to radius
        L3.place(x=20,y=140) # radius location, first time placement
        L5.place(x=20,y=210) #unit label, change loction after cuboid or first time placement
        
        radiusEntry.place(x=80,y=140) # first time placement
         
        dropDownMenu.place(x=80,y=210) #change loction after cuboid or first time placement


show_selected_shape() 

    


def Calculate_Vol(*args): #function to Calculate volume ( Calculate_Vol, button command)


    #Get appropriate Dividing constant as per Unit selected
  
    print('Unit Selected : ',Selected_unit) # For Shell

    if Selected_unit =='mm':
       Liters_Constant = float(1000000) # divide the volume value by 1000000 to change in leters
       print('Liters Constant : ', Liters_Constant)# For Shell
       
    elif Selected_unit == 'cm':
       Liters_Constant = float(1000)# divide the volume value by 1000
       print('Liters Constant : ', Liters_Constant)
      
    elif Selected_unit == 'in':
       Liters_Constant = float(61.024) #  divide the volume value by 61.024
       print('Liters Constant : ', Liters_Constant)
       

    #Conversion of parameters into Cubic Units for Different Shapes
       

    RADIUS = float(radiusEntry.get())# Get data from entry field varible, valid for all shapes

    PI=22/7 # Value of PI, valid for shapes



    #Cylinder

    if Selected_shape == ('Cylinder'):

        HEIGHT = float(heightEntry.get())# Get data from entry field varible
                                     #can't define for all cuz in sphere height feild is empty(generate error)so, specific.

        CubicUnits=(PI*RADIUS*RADIUS*HEIGHT)#Volume of cylinder is PI x R2 x H (varible created in function)
        
        print('Calculate volume for : ',Selected_shape) # for shell
        print('Radius : ',RADIUS)
        print('Height : ',HEIGHT)
        
    
        
    #Cone

    elif Selected_shape == ('Cone'):

        HEIGHT = float(heightEntry.get())# Get data from entry field varible
        
        CubicUnits=(PI*RADIUS*RADIUS*HEIGHT/3)#Volume of cone is PI x R2 x H/3 

        print('Calculate volume for : ',Selected_shape) # for shell
        print('Radius : ',RADIUS)
        print('Height : ',HEIGHT)

        
    #Cuboid

    elif Selected_shape == ('Cuboid'):

        HEIGHT = float(heightEntry.get())# Get data from entry field varible
        WIDTH = float(widthEntry.get())
                                    #can't define for all cuz in sphere height & Width feild is empty(generate error)so, specific.

        CubicUnits=(RADIUS*WIDTH*HEIGHT)#Volume of cubiod is L x W x H
        #RADIUS and Length Entry feild are same only show or hide or change label name as per selected shape

        print('Calculate volume for : ',Selected_shape) # for shell
        print('Length : ',RADIUS) # as length
        print('Width : ',WIDTH)
        print('Height : ',HEIGHT)

        
    #Sphere

    elif Selected_shape == ('Sphere'):

        CubicUnits=(4/3*PI*RADIUS*RADIUS*RADIUS)#Volume of cone is 4/3 x PI x R3

        print('Calculate volume for : ',Selected_shape) # for shell
        print('Radius : ',RADIUS)



    #Conversion of Cubic Units into Liters

     
    Liters=(CubicUnits/Liters_Constant) # divide the volume value by liters constant
                                        # liters constant changes according to selected units for correct conversion into liters
                                        
    Round_Liters = float(round(Liters,3)) #Rounding off by 2 decimal places
    Round_CubicUnits=float( round(CubicUnits,3))
    
    print('CubicUnits : ',Round_CubicUnits)# For Shell
    print('Liters : ',Round_Liters)
    print('\n') #blank line
    
  
    #Push Results to GUI labels
    
    L6=Label(text=f"{Round_CubicUnits} {unitVarible.get()}3 ",font=('Helvetica',12,'bold'),bg="#FFFFFF",width=25, height=3).place(x=30,y=310)
    L7=Label(text=f"{Round_Liters} Liters ",font=('Helvetica',12,'bold'),bg="#FFFFFF",width=25, height=2).place(x=30,y=360)



def CLEAR(*args): # Function to clear/reset all input fields ( CLEAR, button command)
    
    unitVarible.set("Select") #clear unit selection
    heightValue.set("")#clear input fields parameters
    radiusValue.set("")
    lengthValue.set("")
    widthValue.set("")
    Round_CubicUnits=()# clear result varible
    Round_Liters=()
    
    L7=Label(text=f"",font=('Helvetica',12,'bold'),bg="#FFFFFF",width=25, height=3).place(x=30,y=310) #Clear labels (empty label)
    L8=Label(text=f"",font=('Helvetica',12,'bold'),bg="#FFFFFF",width=25, height=2).place(x=30,y=360)
    
    print(" Clear ")
    print('\n') #blank line

CLEAR()# Call function , So things already clear in starting


   
# Graphical User Interface (GUI)----------------------------------------------------------------------                                   



# Labels

L0=Label(root,font=('Helvetica',17,'bold'),text="Volume Calculator",justify=CENTER,bg="#1b6a97",borderwidth=3, relief="raised",fg='white',width=100) #Head Label
L0.pack(padx=2)

L1=Label(text="Shape",font=20).place(x=20,y=60)# Text, FontSize
L2=Label(text="Height",font=20)
L3=Label(text="Length",font=20) # can change into radius in function
L4=Label(text="Width",font=20)
L5=Label(text="Units",font=20)
L6=Label(text="Results",font=("Courier", 16, "bold"),fg='#1b6a97')

#(All above label location is in show shape function)



# Creating widget/ DropDown Menu

dropDownMenu1 = OptionMenu(root,shapeVarible,*shape_List, command = show_selected_shape ) #DropDown menu, Varible, shape list/optons & command
dropDownMenu1.pack(expand=True)
dropDownMenu1.place(x=80,y=60) #location of DropDown menu1

dropDownMenu = OptionMenu(root,unitVarible,*unit_List, command = show_selected_unit ) #DropDown menu, Varible, Unit list/optons & command
 #(location is in show shape function)


#Entry fields

#cylinder and cone, sphere (have same inputs fields)

heightEntry=Entry(root,textvariable=heightValue,width=20,bd=3,font=20) # Entry/Input field for height

radiusEntry=Entry(root,textvariable=radiusValue,width=20,bd=3,font=20)  # Entry field for length and radius (both)
                                                                        #only label and location  changes as per shape
widthEntry=Entry(root,textvariable=widthValue,width=20,bd=3,font=20)

#( All widget location is in show shape function)

  
         
#Buttons

Clear_Button=Button(text ="Clear",font=('Helvetica',12), bg="#1b6a97",fg="white",width=8,height=1, command = CLEAR).place(x=30,y=430) #Clear All command button & location 
Cal_Button=Button(text ="Calculate",font=('Helvetica',12), bg="#1b6a97",fg="white",width=8,height=1, command = Calculate_Vol ).place(x=200,y=430) #Calculte Volume command button & location 


root.mainloop() #Execute tkinter
