from tkinter import ttk 
from tkinter import *
from ttkthemes import themed_tk as th
from PIL import ImageTk, Image
from Zone_options import OPTIONS

class MainApplication():

    def __init__(self, root):
    
        self.my_notebook = ttk.Notebook(root)
        root.title("QuestHelper")
        root.lift()
        root.attributes('-topmost', True)
        root.geometry("330x530")
    
    #Initializing Frames
    def Frames(self):

        self.my_frame1 = ttk.Frame(self.my_notebook)
        
        self.my_frame2 = ttk.Frame(self.my_notebook)
        self.my_frame3 = ttk.Frame(self.my_notebook)
        self.my_frame4 = ttk.Frame(self.my_notebook)
        self.my_frame5 = ttk.Frame(self.my_notebook)
        self.my_frame6 = ttk.Frame(self.my_notebook)
        self.my_frame7 = ttk.Frame(self.my_notebook)
        self.my_frame8 = ttk.Frame(self.my_notebook)
        self.my_frame9 = ttk.Frame(self.my_notebook)
        self.my_frame10 = ttk.Frame(self.my_notebook)


    #Adding Tabs to Main
    def Tabs(self): 
    
        self.my_notebook.add(self.my_frame1, text="Act1")
        self.my_notebook.add(self.my_frame2, text="Act2")
        self.my_notebook.add(self.my_frame3, text="Act3")
        self.my_notebook.add(self.my_frame4, text="Act4")
        self.my_notebook.add(self.my_frame5, text="Act5")
        self.my_notebook.add(self.my_frame6, text="Act6")
        self.my_notebook.add(self.my_frame7, text="Act7")
        self.my_notebook.add(self.my_frame8, text="Act8")
        self.my_notebook.add(self.my_frame9, text="Act9")
        self.my_notebook.add(self.my_frame10, text="Act10")
        self.my_notebook.pack(expand = 1, fill="both")

        #Act1 Map Hide button
        mapHide = Button(self.my_frame1, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'ne')

        #Act2 Map Hide button
        mapHide = Button(self.my_frame2, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'ne')

        #Act3 Map Hide button
        mapHide = Button(self.my_frame3, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'ne')

        #Act4 Map Hide button
        mapHide = Button(self.my_frame4, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'ne')

        #Act5 Map Hide button
        mapHide = Button(self.my_frame5, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'ne')

        #Act6 Map Hide button
        mapHide = Button(self.my_frame6, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'ne')

        #Act7 Map Hide button
        mapHide = Button(self.my_frame7, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'ne')

        #Act8 Map Hide button
        mapHide = Button(self.my_frame8, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'e')

        #Act9 Map Hide button
        mapHide = Button(self.my_frame9, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'ne')

        #Act10 Map Hide button
        mapHide = Button(self.my_frame10, text="Hide", command=self.window_hide)
        mapHide.pack(anchor = 'ne')

        
        
            
        #Act1 tab lock button 
        lockButton = Button(self.my_frame1, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)

        #Act2 tab lock button 
        lockButton = Button(self.my_frame2, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)

        #Act3 tab lock button 
        lockButton = Button(self.my_frame3, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)

        #Act4 tab lock button 
        lockButton = Button(self.my_frame4, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)

        #Act5 tab lock button 
        lockButton = Button(self.my_frame5, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)

        #Act6 tab lock button 
        lockButton = Button(self.my_frame6, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)

        #Act7 tab lock button 
        lockButton = Button(self.my_frame7, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)

        #Act8 tab lock button 
        lockButton = Button(self.my_frame8, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)

        #Act9 tab lock button 
        lockButton = Button(self.my_frame9, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)

        #Act10 tab lock button 
        lockButton = Button(self.my_frame10, text="Lock", command=self.window_Top)
        lockButton.pack(side=RIGHT, padx=5, pady=5)


        #Add Text box and Scrollbar to Act1 tab
        self.textBox = Text(self.my_frame1, width=30, height=12, wrap=WORD)
        self.textBox.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame1, orient='vertical')
        self.textBox.config(yscrollcommand=scrollBar.set)
        scrollBar.config(command=self.textBox.yview)
        scrollBar.pack(in_=self.my_frame1, side=LEFT, fill = Y)
        self.textBox.pack(in_=self.my_frame1, fill = "both", expand=True)

        #Add Text box and Scrollbar to Act2 tab
        self.textBox2 = Text(self.my_frame2, width=30, height=12, wrap=WORD)
        self.textBox2.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame2, orient='vertical')
        self.textBox2.config(yscrollcommand=scrollBar.set)
        scrollBar.config(command=self.textBox.yview)
        scrollBar.pack(in_=self.my_frame2, side=LEFT, fill = Y)
        self.textBox2.pack(in_=self.my_frame2, fill = "both", expand=True)

        #Add Text box and Scrollbar to Act3 tab
        self.textBox3 = Text(self.my_frame3, width=30, height=12, wrap= WORD)
        self.textBox3.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame3, orient='vertical')
        self.textBox3.config(yscrollcommand=scrollBar.set)
        scrollBar.pack(in_=self.my_frame3, side=LEFT, fill = Y)
        self.textBox3.pack(in_=self.my_frame3, fill = "both", expand=True)

        #Add Text box and Scrollbar to Act4 tab
        self.textBox4 = Text(self.my_frame4, width=30, height=12, wrap= WORD)
        self.textBox4.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame4, orient='vertical')
        self.textBox4.config(yscrollcommand=scrollBar.set)
        scrollBar.pack(in_=self.my_frame4, side=LEFT, fill = Y)
        self.textBox4.pack(in_=self.my_frame4, fill = "both", expand=True)

        #Add Text box and Scrollbar to Act5 tab
        self.textBox5 = Text(self.my_frame5, width=30, height=12, wrap= WORD)
        self.textBox5.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame5, orient='vertical')
        self.textBox5.config(yscrollcommand=scrollBar.set)
        scrollBar.pack(in_=self.my_frame5, side=LEFT, fill = Y)
        self.textBox5.pack(in_=self.my_frame5, fill = "both", expand=True)

        #Add Text box and Scrollbar to Act6 tab
        self.textBox6 = Text(self.my_frame6, width=30, height=12, wrap= WORD)
        self.textBox6.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame6, orient='vertical')
        self.textBox6.config(yscrollcommand=scrollBar.set)
        scrollBar.pack(in_=self.my_frame6, side=LEFT, fill = Y)
        self.textBox6.pack(in_=self.my_frame6, fill = "both", expand=True)

        #Add Text box and Scrollbar to Act7 tab
        self.textBox7 = Text(self.my_frame7, width=30, height=12, wrap= WORD)
        self.textBox7.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame7, orient='vertical')
        self.textBox7.config(yscrollcommand=scrollBar.set)
        scrollBar.pack(in_=self.my_frame7, side=LEFT, fill = Y)
        self.textBox7.pack(in_=self.my_frame7, fill = "both", expand=True)

        #Add Text box and Scrollbar to Act8 tab
        self.textBox8 = Text(self.my_frame8, width=30, height=12, wrap= WORD)
        self.textBox8.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame8, orient='vertical')
        self.textBox8.config(yscrollcommand=scrollBar.set)
        scrollBar.pack(in_=self.my_frame8, side=LEFT, fill = Y)
        self.textBox8.pack(in_=self.my_frame8, fill = "both", expand=True)
    
        #Add Text box and Scrollbar to Act9 tab
        self.textBox9 = Text(self.my_frame9, width=30, height=12, wrap= WORD)
        self.textBox9.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame9, orient='vertical')
        self.textBox9.config(yscrollcommand=scrollBar.set)
        scrollBar.pack(in_=self.my_frame9, side=LEFT, fill = Y)
        self.textBox9.pack(in_=self.my_frame9, fill = "both", expand=True)

        #Add Text box and Scrollbar to Act10 tab
        self.textBox10 = Text(self.my_frame10, width=30, height=12, wrap= WORD)
        self.textBox10.configure(font=("Verdana", 10))
        scrollBar = Scrollbar(self.my_frame10, orient='vertical')
        self.textBox10.config(yscrollcommand=scrollBar.set)
        scrollBar.pack(in_=self.my_frame10, side=LEFT, fill = Y)
        self.textBox10.pack(in_=self.my_frame10, fill = "both", expand=True)


        #Zone layout image list Act1
        zoneList = StringVar()
        zoneList.set(Act1_zones[0])

        #Add drop down menu to Act1 tab
        menuDrop = OptionMenu(self.my_frame1, zoneList, *Act1_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)

        #Zone layout image list Act2
        zoneList = StringVar()
        zoneList.set(Act2_zones[0])

        #Add drop down menu to Act2 tab
        menuDrop = OptionMenu(self.my_frame2, zoneList, *Act2_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)

        #Zone layout image list Act3
        zoneList = StringVar()
        zoneList.set(Act3_zones[0])

        #Add drop down menu to Act3 tab
        menuDrop = OptionMenu(self.my_frame3, zoneList, *Act3_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)

        #Zone layout image list Act4
        zoneList = StringVar()
        zoneList.set(Act4_zones[0])

        #Add drop down menu to Act4 tab
        menuDrop = OptionMenu(self.my_frame4, zoneList, *Act4_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)

        #Zone layout image list Act5
        zoneList = StringVar()
        zoneList.set(Act5_zones[0])

        #Add drop down menu to Act5 tab
        menuDrop = OptionMenu(self.my_frame5, zoneList, *Act5_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)

        #Zone layout image list Act6  
        zoneList = StringVar()
        zoneList.set(Act6_zones[0])

        #Add drop down menu to Act6 tab
        menuDrop = OptionMenu(self.my_frame6, zoneList, *Act6_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)

        #Zone layout image list Act7
        zoneList = StringVar()
        zoneList.set(Act7_zones[0])

        #Add drop down menu to Act7 tab 
        menuDrop = OptionMenu(self.my_frame7, zoneList, *Act7_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)

        #Zone layout image list Act8
        zoneList = StringVar()
        zoneList.set(Act8_zones[0])

        #Add drop down menu to Act8 tab 
        menuDrop = OptionMenu(self.my_frame8, zoneList, *Act8_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)

        #Zone layout image list Act9
        zoneList = StringVar()
        zoneList.set(Act9_zones[0])

        #Add drop down menu to Act9 tab
        menuDrop = OptionMenu(self.my_frame9, zoneList, *Act9_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)

        #Zone layout image list Act10
        zoneList = StringVar()
        zoneList.set(Act10_zones[0])

        #Add drop down menu to Act10 tab 
        menuDrop = OptionMenu(self.my_frame10, zoneList, *Act10_zones, command=self.selected)
        menuDrop.pack(side=LEFT, padx=5, pady=5)



        #Show text button Act1 tab
        textButton = Button(self.my_frame1, text="Show Text", command=self.text_click) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")
        
        #Show text button Act2 tab
        textButton = Button(self.my_frame2, text="Show Text", command=self.text_click_2) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")
        
        #Show text button Act3 tab
        textButton = Button(self.my_frame3, text="Show Text", command=self.text_click_3) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")
        
        #Show text button Act4 tab
        textButton = Button(self.my_frame4, text="Show Text", command=self.text_click_4) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")
        
        #Show text button Act5 tab
        textButton = Button(self.my_frame5, text="Show Text", command=self.text_click_5) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")

        #Show text button Act6 tab
        textButton = Button(self.my_frame6, text="Show Text", command=self.text_click_6) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")

        #Show text button Act7 tab
        textButton = Button(self.my_frame7, text="Show Text", command=self.text_click_7) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")

        #Show text button Act8 tab
        textButton = Button(self.my_frame8, text="Show Text", command=self.text_click_8) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")

        #Show text button Act9 tab
        textButton = Button(self.my_frame9, text="Show Text", command=self.text_click_9) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")

        #Show text button Act10 tab
        textButton = Button(self.my_frame10, text="Show Text", command=self.text_click_10) 
        textButton.pack(side=RIGHT, padx=5, pady=5, fill="both")

    
        #Image initialization and image copy 
        global photo
        img = PhotoImage(file='Cavern of Anger.png')
        photo = Label(root, image=img)
        photo.image = img
        photo.config(image = img)
        photo.pack() 


    #Image replacement on select 
    def selected(self,event):
        photo.config(image ="")        
        self.event = event
        if event in OPTIONS:
            print("{} is the value".format(event))
            archive = (str(event) + '.png')
            img2 = PhotoImage(file=archive)
            photo.image =img2
            photo.config(image =img2)
            photo.pack()
        
    #Open Act1 text file 
    def text_click(self):
        with open('act1.txt', 'r') as f:
            self.textBox.insert(INSERT, f.read())

    #Open Act2 text file 
    def text_click_2(self):
        with open('act2.txt', 'r') as f:
            self.textBox2.insert(INSERT, f.read())

    #Open Act3 text file 
    def text_click_3(self):
        with open('act3.txt', 'r') as f:
            self.textBox3.insert(INSERT, f.read())

    #Open Act4 text file 
    def text_click_4(self):
        with open('act4.txt', 'r') as f:
            self.textBox4.insert(INSERT, f.read())

    #Open Act5 text file 
    def text_click_5(self):
        with open('act5.txt', 'r') as f:
            self.textBox5.insert(INSERT, f.read())

    #Open Act6 text file 
    def text_click_6(self):
        with open('act6.txt', 'r') as f:
            self.textBox6.insert(INSERT, f.read())

    #Open Act7 text file 
    def text_click_7(self):
        with open('act7.txt', 'r') as f:
            self.textBox7.insert(INSERT, f.read())

    #Open Act8 text file 
    def text_click_8(self):
        with open('act8.txt', 'r') as f:
            self.textBox8.insert(INSERT, f.read())

    #Open Act9 text file 
    def text_click_9(self):
        with open('act9.txt', 'r') as f:
            self.textBox9.insert(INSERT, f.read())

    #Open Act10 text file 
    def text_click_10(self):
        with open('act10.txt', 'r') as f:
            self.textBox10.insert(INSERT, f.read())

    #Hide window function
    def window_hide(self):
        if root.counter_hide !=10000:
           if root.counter_hide % 2 == 0:
               root.geometry("330x50")      
           else:
                root.geometry("330x530")
        root.counter_hide += 1

    #Lock window frame function
    def window_Top(self):

        if root.counter != 10000:
            if root.counter % 2 == 0:
                root.lift()
                root.attributes('-topmost', False)
            else:     
                root.attributes('-topmost', True)

            root.counter += 1

    

Act1_zones = [

"Cavern of Anger",
"Cavern of Anger 2",
"Cavern of Wrath",
"Cavern of Wrath 2",
"Coast",
"Coast 2",
"Flooded Depths",
"Flooded Depths 2",
"Lower Prison",
"Lower Prison 2",
"Lower Prison 3",
"Lower Prison 4",
"Mud Flats",
"Prisoner's Gate",
"Ship Graveyard",
"Ship Graveyard 2",
"Ship Graveyard 3",
"Submerged Passage 1" ,
"Submerged Passage 2",
"Submerged Passage 3",
"Upper Prison",
"Upper Prison 2",
"Upper Prison 3",

]


Act2_zones = [
"Caverns",
"Caverns 2",
"Caverns 3",
"Chamber of Sins 1",
"Chamber of Sins 1_2",
"Chamber of Sins 1_3",
"Chamber of Sins 2",
"Vaal Ruins",
"Vaal Ruins 2",
"Vaal Ruins 3",
"Wetlands",
"Wetlands 2",
"Weaver's Chambers",
"Weaver's Chambers 2",
    
    

    
    ]

Act3_zones = [
"Crematorium",
"Crematorium 2",
"Crematorium 3",
"Docks",
"Docks 2",
"Docks 3",
"Ebony Barracks",
"Ebony Barracks 2",
"Imperial Gardens",
"Lunaris Temple 1",
"Lunaris Temple 2_1",
"Lunaris Temple 2_2",
"Marketplace",
"Marketplace 2",
"Slums",
"Slums 2",
"Solaris Temple 1",
"Solaris Temple 1_2",
"Solaris Temple 2_1",
"Solaris Temple 2_2",
    ]

Act4_zones = [
"Ascent",
"Belly of the Beast 1",
"Belly of the Beast 1_2",
"Belly of the Beast 2_1",
"Belly of the Beast 2_2",
"Crystal Veins",
"Crystal Veins 2",
"Dried Lake",
"Dried Lake 2",
"Harvest",
"Kaom's Dream",
"Kaom's Stronghold",
"Mines 1",
"Mines 2_1",
"Mines 2_2",

    ]
Act5_zones = [
"Chamber of Innocence",
"Control Blocks",
"Oriath Square",
"Ossuary",
"Reliquary",
"Ruined Square",
"Slave Pens",
"Templar Courts",
"Torched Courts",
    ]
Act6_zones = [
"Brine King's Reef",
"Brine King's Reef 2",
"Karui Fortress",
"Mud_Flats",
"Mud_Flats 2",
"Ridge",
"Ridge 2",
"The Cavern of Anger",
"The Coast",
"The Coast 2",
"The Lower Prison",
"The Lower Prison 2",
"The Lower Prison 3",
"The Prisoner's Gate",
"The Prisoner's Gate 2",
"The Riverways"
    ]
Act7_zones = [
"The Chamber of Sins 1",
"The Chamber of Sins 1_2",
"The Chamber of Sins 1_3",
"The Chamber of Sins 2",
"The Crossroads",
"The Crypt",
"The Crypt 2",
"The Crypt 3",
"The Crypt 2_1",
"The Crypt 2_2",
"The Crypt 2_3",
"The Den",
"The Den 2",
"The Vaal City",
    ]
Act8_zones = [
"Bath House",
"Doedre's Cesspool",
"Doedre's Cesspool 2",
"Lunaris Concourse",
"The Grain Gate",
"The Lunaris Temple 1",
"The Lunaris Temple 1_2",
"The Lunaris Temple 2_1",
"The Lunaris Temple 2_2",
"The Quay",
"The Solaris Temple 1",
"The Solaris Temple 2_1",
"The Solaris Temple 2_2",
"Toxic Conduits",
    ]
Act9_zones = [
"Oasis",
"Oasis 2",
"Quarry",
"Refinery",
"The Belly of the Beast 1",
"The Belly of the Beast 2",
"The Belly of the Beast 3",
"The Descent",
"The Foothills",
"Tunnel",
"Tunnel 2",
"Tunnel 3",
"Vastiri Desert"
    ]
Act10_zones = [
"Desecrated Chambers",
"The Control Blocks",
"The Ossuary",
"The Ravaged Square",
"The Reliquary",
"The Torched Courts",
    ]



root = Tk()
root.counter = 0
root.counter_hide = 0
b = MainApplication(root)
b.Frames()
b.Tabs()


root.mainloop()
