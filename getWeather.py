#coding:utf-8
import urllib.parse
import urllib.request
from xml.dom.minidom import parseString

def getWeather(city):

	if city:
		pass
	else:
		city="武汉"	
		
	url = "http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName"
	values = {"theCityName":city}
	data = urllib.parse.urlencode(values).encode(encoding='UTF8')
	req = urllib.request.Request(url, data)
	response = urllib.request.urlopen(req)
	the_page = response.read().decode("utf8")
	dom = parseString(the_page)
	string = dom.getElementsByTagName("string")
	
	try:
		my_city = string[1].childNodes[0].data
		today = string[6].childNodes[0].data
		today_tem = string[5].childNodes[0].data
		tom1 = string[13].childNodes[0].data
		tom1_tem = string[12].childNodes[0].data
		tom2 = string[18].childNodes[0].data
		tom2_tem = string[17].childNodes[0].data
		weather_message=my_city+' : '+today+today_tem+'---'+tom1+tom1_tem+'---'+tom2+tom2_tem

	except IndexError as e:
		next
		
	if weather_message:
		pass
	else:
		weather_message="Error"
		
	return weather_message