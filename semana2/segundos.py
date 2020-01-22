segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // (3600 * 24)
segundos = total_segs % (3600 * 24)
horas = segundos // 3600
segs_restantes = segundos % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print(dias,"dias,",horas,"horas,",minutos, "minutos e", segs_restantes_final, "segundos.")
