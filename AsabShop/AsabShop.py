from tkinter import *
import csv

def viewCost():
    cost = int ( smallSizeSpinbox.get() ) * 5 + int ( mediumSizeSpinbox.get() ) * 7 + int ( largeSizeSpinbox.get() ) * 10 
    costLabel.configure ( text = str(cost) + " EGP" )
    return cost

def purchase():
    data = []
    data.append ( smallSizeSpinbox.get() )
    data.append ( mediumSizeSpinbox.get() )
    data.append ( largeSizeSpinbox.get() )
    data.append ( str ( viewCost() ) )
    
    smallSizeSpinbox.delete(0,'end')
    mediumSizeSpinbox.delete(0,'end')
    largeSizeSpinbox.delete(0,'end')
    
    smallSizeSpinbox.insert(0,'0')
    mediumSizeSpinbox.insert(0,'0')
    largeSizeSpinbox.insert(0,'0')
    
    with open( "Asab.csv" , "a+" , newline = '' ) as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)        

mainWindow = Tk()

mainWindow.configure ( bg = '#C3DB79')
mainWindow.title("Asab Shop")
mainWindow.geometry('1000x500')
mainWindow.resizable(0,0)

welcomeLabel = Label(mainWindow, text="Welcome to Hussien Asab Shop" , bd = '10' , bg= '#C3DB79' , font = ( 'Calibre' , 20 , 'bold') )

smallSizeLabel = Label ( mainWindow , text = "Small" , bg = '#C3DB79' ,font = ( 'Calibre' , 20 , 'bold' ) )
mediumSizeLabel = Label ( mainWindow , text = "Medium" , bg = '#C3DB79' , font = ( 'Calibre' , 20 , 'bold' ) )
largeSizeLabel = Label ( mainWindow , text = "Large" , bg = '#C3DB79' , font = ( 'Calibre' , 20 , 'bold' ) )

smallSizePhoto = PhotoImage ( file = 'SmallSize.png' ).subsample(2,2)
smallSizePhotoLabel = Label ( mainWindow , image = smallSizePhoto )

mediumSizePhoto = PhotoImage ( file = 'MediumSize.png' ).subsample(2,2)
mediumSizePhotoLabel = Label ( mainWindow , image = mediumSizePhoto )

largeSizePhoto = PhotoImage ( file = 'LargeSize.png' ).subsample(2,2)
largeSizePhotoLabel = Label ( mainWindow , image = largeSizePhoto )

smallSizeSpinbox = Spinbox ( mainWindow , from_ = 0 , to = 10 , width = 5 , font = ( 'Calibre' , 15 , 'bold' ))

mediumSizeSpinbox = Spinbox ( mainWindow , from_ = 0 , to = 10 , width = 5 , font = ( 'Calibre' , 15 , 'bold' ))

largeSizeSpinbox = Spinbox ( mainWindow , from_ = 0 , to = 10 , width = 5 , font = ( 'Calibre' , 15 , 'bold' ))

viewCostButton = Button ( mainWindow , text = "View Cost" , font = ( 'Calibre' , 15 , 'bold' ) , command = viewCost )
purchaseButton = Button ( mainWindow , text = "Purchase" , font = ( 'Calibre' , 15 , 'bold' ) , command = purchase )

costLabel = Label ( mainWindow , text = "0 EGP" , font = ( 'Calibre' , 15 , 'bold' ) , bg = '#C3DB79' )

welcomeLabel.place ( x = 270 , y = 0 )

smallSizeLabel.place ( x = 157 , y = 60 )
mediumSizeLabel.place ( x = 447 , y = 60 )
largeSizeLabel.place ( x = 757 , y = 60 )

smallSizePhotoLabel.place ( x = 100 , y = 100 )
mediumSizePhotoLabel.place ( x = 400 , y = 100 )
largeSizePhotoLabel.place ( x = 700 , y = 100 )

smallSizeSpinbox.place ( x = 165 , y = 300 )
mediumSizeSpinbox.place ( x = 465 , y = 300 )
largeSizeSpinbox.place ( x = 765 , y = 300 )

viewCostButton.place ( x = 390 , y = 350 )
costLabel.place ( x = 510 , y = 356 ) 
purchaseButton.place ( x = 450 , y = 420 )



mainWindow.mainloop()
