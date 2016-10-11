"""
number plate reader using openALPR
by AfterPartyLion for DigiLab
v0.5
openALPR: https://groups.google.com/forum/#!topic/openalpr/-vckIsPe618
ownCloud: https://samhobbs.co.uk/2013/10/install-owncloud-on-your-raspberry-pi
run this as a root: sudo python main.py to be able to upload the data to the ownCloud server
"""
#imports
from os import remove
from time import strftime,process_time,sleep
from openalpr import Alpr
"""
import picamera
camera = picamera.PiCamera()
#camera.hflip = True
#camera.vflip = True
"""
#functions
def motionDetect(): #motion sensor detection *needs working on
    try:
        while True:
            print('Movement Detected')
            fileName()
            #takePhoto()
            if openALPR():
                upload()
            else:
                print('image not a number plate')
            sleep(2)
    except KeyboardInterrupt:
        print('Keyboard Interrpt')
        return True

def fileName():
    print('STARTED: filename')
    global filepath,filename
    filename = strftime('%H:%M:%S %d/%m/%Y')
    filepath = ('Plates/'+strftime('%H %M %S %d %m %Y')+'.jpg')
    print('FINISHED: filename')
    return True

def takePhoto(): #taking a picture
    print('STARTED: taking picture')
    camera.start_preview()
    sleep(1)
    camera.stop_preview()
    camera.capture(filepath)
    print('FINISHED: taking picrure')
    return True

def openALPR(): #reading the picture
    print('STARTED: ALPR')
    try:
        global database
        alpr = None
        alpr = Alpr('gb','/etc/openalpr/openalpr.conf','/home/pi/openalpr/runtime_data')
        if not alpr.is_loaded():
            print("Error loading OpenALPR")
            return False
        else:
            database = []
            alpr.set_top_n(7)
            alpr.set_default_region("gb")
            alpr.set_detect_region(False)
            jpeg_bytes = open('Plates/Plate.jpg', "rb").read() #testing
            results = alpr.recognize_array(jpeg_bytes)
            i = 0
            for plate in results['results']:
                i += 1
                for candidate in plate['candidates']:
                    plate = [candidate['plate'],candidate['confidence']]
                    database.append(plate)
            if database == []:
                remove(filepath)
                print('FINISHED: ALPR unsucessful')
                return False
            else :
                print(database)
                print('FINISHED: ALPR sucessful')
                return True
    except AttributeError:
        print()
def upload(): #upload to database
    print('STARTED: upload')
    file = open('/home/pi/Desktop/NumberPlate/ownCloudData/digilab123/files/Database.txt','a') #you have to make a blank file on ownCloud and then use its location
    file.write(filename+'\n')
    for x in database:
        y = [x[0],x[1]]
        file.write(str(y))
    file.write('\n')
    file.close()
    print('FINISHED: upload')
    return True

def timeElapsed(): #time elapased *not necessary but why not
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
                elif strftime('%m') == 2:
                    if int(strftime('%Y')) % 4 == 0:
                        if int(strftime('%Y')) % 100 == 0:
                            if int(strftime('%Y')) % 400 == 0:
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
#main
print("STARTED:number plate recognition\nPress 'Ctrl + C' to stop script")
started = strftime('%H %M %S %d %m %Y')
motionDetect()
#end
timeElapsed()
print('FINISHED:number plate recognition')
quit()
