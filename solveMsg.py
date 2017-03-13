#将消息分类分流处理
def solveMsg(Msg):
	if 't' in Msg:
		print(1)
	elif 's' in Msg:
		print(2)
	else:
		print(3)

		
solveMsg('Msg')
pause()