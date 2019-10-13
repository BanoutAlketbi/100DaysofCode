import datetime
x = datetime.datetime.now()
print(x.year)
print(x)
print(x.strftime("%B"))
print(x.strftime("%A"))

#----Extra
today = datetime.date.today()
yesterday = today - datetime.timedelta(days= 1)
tomorrow = today + datetime.timedelta(days= 1)
print("Yesterday's date: ", yesterday)
print("Tomorrow's date: ", tomorrow)