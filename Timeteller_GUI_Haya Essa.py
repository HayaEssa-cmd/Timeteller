#################Automatically install packages ###################

def install_and_import(package):
    import importlib
    try:
        importlib.import_module("remi")
        importlib.import_module("seaborn")
       
    except ImportError:
        import pip
        pip.main(['install', "remi"])
        pip.main(['install', "seaborn"])
      
    finally:
        globals()["remi"] = importlib.import_module("remi")
        globals()["seaborn"] = importlib.import_module("seaborn")
    

install_and_import('transliterate') 


#packages
##import Tkinter as tk
#import PySide2
from typing import List
from remi import start, App
#import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib 
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import matplotlib.transforms as mtransforms
from matplotlib.patches import Rectangle
import pandas as pd
import sip # can be installed : pip install sip
from datetime import datetime
# We require a canvas class
from mpldatacursor import datacursor
from PyQt5 import QtCore, QtGui, QtWidgets #works for pyqt5
from scipy.optimize import curve_fit
import matplotlib.dates


from datetime import datetime

#Framework

class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None, dpi = 120):
		fig = Figure(dpi = dpi)
		self.axes = fig.add_subplot(111)
		super(MatplotlibCanvas,self).__init__(fig)
		fig.tight_layout()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Timeteller")
        MainWindow.resize(1440, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setObjectName("comboBox_1")
        
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")

        #self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        #self.comboBox_3.setObjectName("comboBox_3")
        


        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setObjectName("radioButton")

        self.checkBox_1=QtWidgets.QCheckBox("Meals", self.centralwidget)
        self.checkBox_1.setObjectName("Check box")

        self.checkBox_2=QtWidgets.QCheckBox("Sleep", self.centralwidget)
        self.checkBox_2.setObjectName("Check box")

        self.checkBox_3=QtWidgets.QCheckBox("Exercise1", self.centralwidget)
        self.checkBox_3.setObjectName("Check box")

        self.checkBox_4=QtWidgets.QCheckBox("Exercise2", self.centralwidget)
        self.checkBox_4.setObjectName("Check box")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        
        self.horizontalLayout.addWidget(self.label_1)
        self.horizontalLayout.addWidget(self.comboBox_1)
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.radioButton_1)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.checkBox_1)
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.horizontalLayout.addWidget(self.checkBox_4)
        self.horizontalLayout.addItem(spacerItem)
        
        #self.horizontalLayout.addWidget(self.comboBox_3)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_csv_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_csv_file.setObjectName("actionOpen_csv_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_csv_file)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #self.filename = ''
        self.canv = MatplotlibCanvas(self)
        self.df = []
        
        self.toolbar = Navi(self.canv,self.centralwidget)
        self.horizontalLayout.addWidget(self.toolbar)

     #############DATA################

#different themes for the plots

        self.themes = ['seaborn','Solarize_Light2','classic','bmh', 'fast', 
        'fivethirtyeight', 'ggplot', 'seaborn-bright',
         'seaborn-colorblind', 'seaborn-dark', 
         'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
         'seaborn-paper', 'seaborn-poster', 'seaborn-talk',
         'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid'
         ]
        
        self.comboBox.addItems(self.themes)
        self.comboBox_1.addItems(['Select horizontal axis here'])
        self.comboBox_2.addItems(['Select vertical axis here'])
        #self.comboBox_3.addItems(['Displaying Attributes'])
      
        
        self.pushButton.clicked.connect(self.getFile)
        self.comboBox.currentIndexChanged['QString'].connect(self.Update)
        self.comboBox_1.currentIndexChanged['QString'].connect(self.selectXaxis)
        self.comboBox_2.currentIndexChanged['QString'].connect(self.selectYaxis)
        #self.comboBox_3.currentIndexChanged['QString'].connect(self.selectDisplayingAttribute)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionOpen_csv_file.triggered.connect(self.getFile)
        self.radioButton_1.clicked.connect(self.vsAll)

# check boxes are used for Sleep, Exercise and Meals 

        self.checkBox_1.clicked.connect(self.callUpdate)
        self.checkBox_2.clicked.connect(self.callUpdate)
        self.checkBox_3.clicked.connect(self.callUpdate)
        self.checkBox_4.clicked.connect(self.callUpdate)

        self.vsall = False
        self.dataset={}
        self.x_axis_slt=None
        self.y_axis_slt=None
        self.filename= "test_values_2022.csv" # hardcoded file into the code just so I didn't need to open a file everytime I ran it
        self.readData()


# all genes radio button definition 

    def vsAll(self):
        
        """
        This function will be called upon triggering the radio check button. If set to True, all the columsn in the csv
        will be plotted against the x-axis column. Please note that vs all means versus all, so that whatever value is 
        selected as the x-axis, it wont be plotted against itself in this mode. Moreover, the time series data will be 
        dedicated for the datetime x-axis and it wont be displayed in the vs all contents.

        """
        self.vsall = not self.vsall
        self.Update(self.themes[0]) 
        

    def selectXaxis(self,value):
        """
        This function will update the plot according to the data of x axis selected from combo box

        """
        self.x_axis_slt=value
        self.Update(self.themes[0])
        
    def selectYaxis(self,value):
        """
        This function will update the plot according to the data of y axis selected from combo box

        """
        self.y_axis_slt=value
        self.Update(self.themes[0]) #setting the things

        #Amplitude, meal times, day and night, day one and two
    
    def callUpdate(self,value):
        self.Update(self.themes[0])

    def Update(self,value):

        """
        This function will input the value of theme and accordingly plot the data, if the data is relative, i.e., x versus y-axis
        then the user can assign x and y axis from the combo box. If all data should be plotted in parallel then leave,
        the combo boxes of axis selections to their default starting location. 
            
        """
        plt.clf()
        plt.style.use(value)
        try:
            self.horizontalLayout.removeWidget(self.toolbar)
            self.verticalLayout.removeWidget(self.canv)
            
            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None
            self.verticalLayout.removeItem(self.spacerItem1)
        except Exception as e:
            print(e)
            pass
        self.canv = MatplotlibCanvas(self)
        self.toolbar = Navi(self.canv,self.centralwidget)
        
        self.horizontalLayout.addWidget(self.toolbar)
        self.verticalLayout.addWidget(self.canv)
        
        self.canv.axes.cla()

        ax = self.canv.axes
        plots = []  # intialize to empty plot 

# plots the harmonic regression of the points when you click 'all genes'

        if self.vsall:
            for k in self.dataset.keys():
                if k == "Time-Point" or k == "tHar" or not k.startswith("HarReg"):
                    continue
                if 'tHar' in self.dataset.keys():
                    plots.append(ax.plot(self.dataset['tHar'],self.dataset[k],label=k[6:],linewidth=3.5))  #plots the HarReg lines 

# plots the gene that is choosen from the y-slt - it also only plots the harmonic regression 
        else:
            if (self.x_axis_slt in self.dataset) and (self.y_axis_slt in self.dataset):
                x = np.empty((0, 0))
                values = np.empty((0, 0))
                for i in range(len(self.dataset[self.y_axis_slt])):
                    if pd.isna(self.dataset[self.y_axis_slt][i]):
                        continue
                    x = np.append(x, self.dataset["Time-Point"][i])
                    values = np.append(values, self.dataset[self.y_axis_slt][i])
                
                plots.append(ax.plot(x,values, linewidth=0))
                for k in self.dataset.keys():
                    if k == "Time-Point" or k == "tHar" or not k.startswith("HarReg"):
                        continue
               
                if 'tHar' in self.dataset.keys():
                        plots.append(ax.plot(self.dataset['tHar'],self.dataset[k],label=self.y_axis_slt,linewidth=3.5))
        
        legend = ax.legend()
        legend.set_draggable(True)
        ax.set_xlabel("Time in Hours", fontsize= 15) # make a string of "Time in Hours" 
        ax.set_xticks(range(0,50,3)) #counting from 1-50 in 3 hour steps

# makes sure the ticks are in order of the csv file because the hours are getting restarted for day 2
        current_values = ax.get_xticks()
        new_values = []
        for i in range(len(current_values)):
            tmp = current_values[i]
            while tmp >= 24:
                tmp = tmp - 24 
            new_values.append(str(tmp))
        ax.set_xticklabels(new_values)

        ax.set_ylabel('Gene Activity', fontsize= 15)
        #ax.set_yticklabels([]) #removes the labels of the y axis
        #ax.set_tick_params(left=False) #removes the ticks
        ax.set_title("Your Circadian Profile", fontsize=25, fontweight ='bold', x=0.5, y=1.01)
        #plt.setp(ax.xaxis.get_majorticklabels(), rotation=25)  # uncomment if you want the x-axis to tilt 25 degree
        
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()


# plots vertical lines for Meals and Exercise 
# plots a rectangle within a range 
# automatically adds one label when you click on a check box 
       
        my_labels = {"Exercise1": "Exercise1", "Exercise2": "Exercise2" ,"Meal": "Meals", "Sleep": "Sleep"} 
        if self.checkBox_1.isChecked()==True:
            for Meal in self.meals:
                ax.axvline(Meal,ls='--',color="blue", label=my_labels["Meal"])          
                my_labels["Meal"] = "_nolegend_"    
        
        if self.checkBox_2.isChecked()==True:
            for Sleep in self.Sleep:
                ax.add_patch(Rectangle((Sleep[0], -2), Sleep[1]-Sleep[0], 7, color="grey", alpha=0.5, label=my_labels["Sleep"]))
                my_labels["Sleep"] = "_nolegend_"
                
        if self.checkBox_3.isChecked()==True:
            for Exercise1 in self.Exercise1:
                ax.axvline(Exercise1,ls='--',color="red", label=my_labels["Exercise1"])
                my_labels["Exercise1"] = "_nolegend_"

        if self.checkBox_4.isChecked()==True:
            for Exercise2 in self.Exercise2:
                ax.axvline(Exercise2,ls='--',color="green", label=my_labels["Exercise2"])
                my_labels["Exercise2"] = "_nolegend_"
        
        legend = ax.legend()
        
        ax.set_xlim(self.dataset["Time-Point"][0],self.dataset["Time-Point"][-1])
        ax.set_ylim(ylim)
        
        self.canv.draw()
            

    def getFile(self): #open button gets clicked
        """ This function will get the address of the csv file location
            also calls a readData function 
        """
        try:
            self.filename = QFileDialog.getOpenFileName(filter = "csv (*.csv)")[0]
            self.readData()
        except Exception as e:
            print(e)
            pass

# load the data set 


    def getDataset(self,csvfilename):
        
        """
        This function will convert csv file to a dictionary of dataset, with keys as the columns' names and
        values as values. The datatime format should be one of the standard datatime formats. Before plottting
        we need to convert the string of data time in the csv file values to datatime format.
        """
        df = pd.read_csv(csvfilename,encoding='utf-8') #.nanmean to find the mean value
        LIST_OF_COLUMNS = df.columns.tolist()
        LIST_OF_COLUMNS = LIST_OF_COLUMNS[:len(LIST_OF_COLUMNS) - 4] # last three columns will be handled manually 
        dataset={}
        time_format = '%H:%M%f'
# reading the HH:MM hours and minutes on the csv file as an integer 

        for i in df.index:
            HMS = [60*60, 60, 1]
            t = df["Time-Point"][i]
            dec_time = sum(a * b for a,b in zip (HMS, map(int, t.split(":"))))
            dec_time /= 3600.
            if df.loc[i, "Day"] == 1:
                df.loc[i, "Time-Point"] = dec_time
            elif df.loc[i, "Day"] == 2:
                df.loc[i, "Time-Point"] = dec_time+24
            print(df.loc[i, "Time-Point"])


#####################Meals#############################
        meals = np.empty((0, 0))
        for i in range(len(df["Meals"].iloc[0:].values)):
            if df["Meals"][i] == "x":
                meals = np.append(meals, df["Time-Point"][i])
        
        #print("Dinner's ready ",meals)
        self.meals = meals
        
#####################Exercise1#############################
        Exercise1 = np.empty((0, 0))
        for i in range(len(df["Exercise1"].iloc[0:].values)):
            if df["Exercise1"][i] == "x":
                Exercise1 = np.append(Exercise1, df["Time-Point"][i])
        
        #print("get swoll ",Exercise)
        self.Exercise1 = Exercise1

######################Exercise2#####################
        Exercise2 = np.empty((0, 0))
        for i in range(len(df["Exercise2"].iloc[0:].values)):
            if df["Exercise2"][i] == "x":
                Exercise2 = np.append(Exercise2, df["Time-Point"][i])
        
        #print("get swoll ",Exercise)
        self.Exercise2 = Exercise2    


#####################Sleep#############################
        Sleep = []
        toggle = True
        for i in range(len(df["Sleep"].iloc[0:].values)):
            if df["Sleep"][i] == "x":
                if toggle:
                    Sleep.append((df["Time-Point"][i], df["Time-Point"][i+1]))
                toggle = not toggle
        Sleep = np.array(Sleep)
        self.Sleep = Sleep

        
        for col in LIST_OF_COLUMNS:
            dataset[col]  = df[col].iloc[0:].values # takes the series corresponds to the column and starts at the first entry
          
            #print("we in col : ",col)
            #print("we read: ",dataset[col])

            if col == "Time-Point" or col == "Day":
                continue
           

            
            # replace , with . if the inputter is too , for his own good
            if isinstance(dataset[col][0],str):
                dataset[col] = np.array([float(dataset[col][i].replace(',','.')) for i in range(len(dataset[col]))]) 
            
#makes the Gene Activity values into positive numbers 

            dataset[col] = 2**(dataset[col])

#GET RID OF LINE AND KEEP HARMONIC REGRESSION, SEE IF YOU CAN DO THAT IN THIS FUNCTION -----> only take into account gene1-3 ---> more can be added 
            def HarReg(Xaxis,a,b,c):
                return a+b*np.cos((Xaxis+c)*np.pi*2/24)
            
            x = np.empty((0, 0))
            values = np.empty((0, 0))
            for i in range(len(dataset[col])):
                if pd.isna(dataset[col][i]):
                    continue
                x = np.append(x, dataset["Time-Point"][i])
                values = np.append(values, dataset[col][i])
            
            popt, pcov = curve_fit(HarReg, x, values)
            dataset["tHar"] = np.arange(df["Time-Point"].iloc[0],df["Time-Point"].iloc[-1],0.1)
            #self.canv.axes.plot(tHar, HarReg(tHar, *popt))
            dataset["HarReg"+col] = HarReg(dataset["tHar"], *popt)

#Max Point ---> probably needs to be changed
        def MaxPoint(dataset,col):
            x= dataset["Time-Point"]
            values= dataset[col]
            popt, pcov = curve_fit(HarReg, x, values)
            print('this is the max point ' + col, "popt", popt)
        #MaxPoint(dataset,col)
    
        return dataset,LIST_OF_COLUMNS

    def readData(self): #opens the data
        """ This function will read the data using pandas and call the update
            function to plot
        """
        import os
        self.dataset={}
        self.x_axis_slt=None
        self.y_axis_slt=None

        base_name = os.path.basename(self.filename)
        self.Title = os.path.splitext(base_name)[0]
        
        self.dataset, LIST_OF_COLUMNS = self.getDataset(self.filename)
        
        self.df = pd.read_csv(self.filename,encoding = 'utf-8').fillna(0)
        
        self.Update(self.themes[0]) # lets 0th theme be the default : bmh
        self.comboBox_1.clear()
        self.comboBox_2.clear()
        #self.comboBox_3.clear()
        self.comboBox_1.addItems(['Select horizontal axis here'])
        self.comboBox_2.addItems(['Select Gene'])
        #self.comboBox_3.addItems(['Select Predicted Activities'])
        self.comboBox_1.addItems(LIST_OF_COLUMNS)
        self.comboBox_2.addItems(LIST_OF_COLUMNS)
        #self.comboBox_3.addItems(LIST_OF_COLUMNS)

        self.x_axis_slt= LIST_OF_COLUMNS[0]
        self.y_axis_slt=LIST_OF_COLUMNS[1]

#labels of core GUI  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Timeteller", "Timeteller"))
        self.label.setText(_translate("Timeteller", "Select Theme"))
        self.label_1.setText(_translate("Timeteller", "X-axis"))
        self.label_2.setText(_translate("Timeteller", "Y-axis"))
        self.label_3.setText(_translate("Timeteller", "vs All Genes"))
        self.pushButton.setText(_translate("Timeteller", "Open"))
        self.menuFile.setTitle(_translate("Timeteller", "File"))
        self.actionOpen_csv_file.setText(_translate("Timeteller", "Open csv file"))
        self.actionExit.setText(_translate("Timeteller", "Exit"))
        


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	
MainWindow.show()
sys.exit(app.exec_())




  