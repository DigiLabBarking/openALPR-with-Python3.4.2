"""
number plate reader using openALPR
by AfterPartyLion for DigiLab
v0.1
"""
#imports
from os import remove
from time import strftime,process_time,sleep
from openalpr import Alpr
#functions
def motionDetect(): #motion sensor detection
    return True
def createFilename(): #filename generator
    global filenameTEST,filename
    filename = str(strftime('%H:%M:%S %d/%m/%Y'))
    filepath = ('Plates/'+str(strftime('%H.%M.%S_%d.%m.%Y'))+'.jpg')
    filenameTEST = ('Plates/notPlate.jpg') ###
    return True
def takePhoto(): #taking a picture
    return True
def openALPR(): #reading the picture
    alpr = None
    try:
        alpr = Alpr('gb','/etc/openalpr/openalpr.conf','/home/pi/openalpr/runtime_data')

        if not alpr.is_loaded():
            print("Error loading OpenALPR")
            return False
        else:
            database = []
            alpr.set_top_n(7)
            alpr.set_default_region("gb")
            alpr.set_detect_region(False)
            jpeg_bytes = open('Plates/Plate.jpg', "rb").read() ###
            results = alpr.recognize_array(jpeg_bytes)
            i = 0
            for plate in results['results']:
                i += 1
                for candidate in plate['candidates']:
                    plate = [candidate['plate'],candidate['confidence']]
                    database.append(plate)
            if database == []:
                remove('Plates/Plate.jpg') ###
                return False
            print(database)
    finally:
        if alpr:
            alpr.unload()
            return True
def upload(): #upload to database
    file = open('Database.txt','a')
    file.write(filename+'\n')
    for x in database:
        y = [x[0],x[1]]
        file.write(str(y))
    file.write('\n')
    file.close()
    return True
def timeElapsed(): #time elapased
    global started
    finished = strftime('%H %M %S %d %m %Y')
    finished = finished.split(' ')
    started = started.split(' ')
    timer = []
    for counter in range(6):
        x = int(finished[counter])-int(started[counter])
        timer.append(x)
    sen = ("The program has been on for ")
    x = [' hour(s) ',' minute(s) ',' second(s) ',' day(s) ',' month(s) ',' year(s) ']
    for counter in range(6):    
        if timer[counter] > 0:
            sen = sen+str(timer[counter])+x[counter]
        elif timer[counter] < 0:
            if counter == 0:
                timer[counter] += 24
                sen = sen+str(timer[counter])+x[counter]
            elif counter == 1:
                timer[counter] += 60
                sen = sen+str(timer[counter])+x[counter]
            elif counter == 2:
                timer[counter] += 60
                sen = sen+str(timer[counter])+x[counter]
            elif counter == 3:
                if strftime('%m') == 1:
                    timer[counter] += 31
                elif strftime('%m') == 2: #Febuary
                    if int(strftime('%Y')) % 4 == 0: #Divisable by 4
                        if int(strftime('%Y')) % 100 == 0: #Divisable by 100
                            if int(strftime('%Y')) % 400 == 0: #Divisable by 400
                                timer[counter] += 29
                            else:
                                timer[counter] += 28
                        else:
                            timer[counter] += 28
                    else:
                        timer[counter] += 28
                elif strftime('%m') == 3:
                    timer[counter] += 31
                elif strftime('%m') == 4:
                    timer[counter] += 30
                elif strftime('%m') == 5:
                    timer[counter] += 31
                elif strftime('%m') == 6:
                    timer[counter] += 30
                elif strftime('%m') == 7:
                    timer[counter] += 31
                elif strftime('%m') == 8:
                    timer[counter] += 31
                elif strftime('%m') == 9:
                    timer[counter] += 30
                elif strftime('%m') == 10:
                    timer[counter] += 31
                elif strftime('%m') == 11:
                    timer[counter] += 30
                elif strftime('%m') == 12:
                    timer[counter] += 31
                sen = sen+str(timer[counter])+x[counter]
            elif counter == 4:
                timer[counter] += 12
                sen = sen+str(timer[counter])+x[counter]        
    print(sen)
#maim
print('STARTED:number plate recognition')
started = strftime('%H %M %S %d %M %Y')
#end
timeElapsed()
print('FINISHED:number plate recognition')
quit()
