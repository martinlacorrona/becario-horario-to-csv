# becario-horario-to-csv
Convierte el horario descargado de la pagina a un CSV para importar a distintos calendarios (Google Calendar).

# Steps
# Version 3.7 de Python
Descarga e instala pip para instalar paquetes:
py -m pip install requests

# Using
py .\timetable.py USER PASSWORD FILETOEXPORT.csv False(isNextWeek?)
py .\timetable.py userPrueba passwordPrueba horarioExportar.csv True
Sacara el horario de la semana que viene usando True.
