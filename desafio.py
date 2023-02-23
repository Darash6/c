Conversor de segundos:

segundos = input("Por favor, qual a quantidade de segunods que deseja converter?: ")
total_s = int(segundos)

dias=total_s//86400
segs_restantes=total_s%86400
horas=segs_restantes//3600
segs_restantes_2=segs_restantes%3600
minutos=segs_restantes2//60
segs_restantes_final=segs_restantes_2%60

print(dias, "dias", horas, "horas", minutos, "minutos e", segs_restantes_final, "segundos.")