import csv
import time

def saveMsg(filename,id,Msg):
	with open('./record/'+filename+'.csv', 'a') as csvout:
		writer = csv.writer(csvout)
		now = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
		writer.writerow([now,id,Msg])

# save_Msg('file','id','msg')