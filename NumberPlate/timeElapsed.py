from time import strftime
def timeElapsed(): #time elapased
    global started
    #finished = strftime('%H %M %S %d %m %Y')
    finished = ('23 32 21 06 02 2016')
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


#started = strftime('%H %M %S %d %M %Y')
started = ('23 32 21 07 02 2016')
timeElapsed()
