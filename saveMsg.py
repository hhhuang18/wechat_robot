import csv
import time

def saveMsg(filename,id,Msg):
	with open('./record/'+filename+'.csv', 'a', newline='') as csvout:	#加入,newline=''去除空行
		writer = csv.writer(csvout)
		now = time.strftime("%Y%m%d %H:%M:%S", time.localtime())
		writer.writerow([now,id,Msg])

# save_Msg('file','id','msg')