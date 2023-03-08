import datetime
import time

def mensaje():
    return print("******Bienvenidos******\n ***veremos a continuación***\n ***si su horario de trabajo ha terminado...***")


now = datetime.datetime.now().time()
casa_time = datetime.time(19, 0, 0)
start_time = datetime.time(9, 0, 0)
current_date = datetime.date.today()
start_datetime = datetime.datetime.combine(current_date, start_time)
casa_datetime = datetime.datetime.combine(current_date, casa_time)
falta = casa_datetime - start_datetime
total_seconds = falta.total_seconds()
horas = int(total_seconds//3600)
minutos = int((total_seconds%3600)//60)

mensaje()
print("son las =", now)

if now >= casa_time:
    print("es hora de ir a casa")
else:
    print("todavía te falta")
    
    print("te quedan",falta, "de trabajo") 
#print(t.strftime("%H:%M:%S"))

#dt = datetime()
#dt()
#print(dt.strftime("%y/%B/%d %H:%M:%S"))
