from subprocess import call

archivo="/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Desktop/BD.txt Bd.txt"
call ([archivo],shell=True)

#archivo2="/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Desktop/BD.txt Bd.txt"
#call ([archivo2],shell=True)