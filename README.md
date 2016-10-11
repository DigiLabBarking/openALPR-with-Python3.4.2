# openALPR on Raspberry Pi 3 with Python3.4.2 v0.5
Reading number plates with python

Requirments:
raspberry pi camera module - https://www.raspberrypi.org/products/camera-module-v2/
openALPR:https://groups.google.com/forum/#!topic/openalpr/-vckIsPe618
ownCloud:https://samhobbs.co.uk/2013/10/install-owncloud-on-your-raspberry-pi

Running:
open main.py using 'sudo python3.4 main.py' and it should start taking pictures every few seconds (I'll add in a motion sensor so that it'll only take pictures once movement has been detected) to look for number plates
if it picks up a number plate, it will save the date and the number plate in Database.txt so that it could be accesed from ownCloud
