segundos =input("Por favor, entre com numero de segundos que deseja converter: ")
total_segs =(int(segundos))

dias = total_segs // 86400
seg_restantes = total_segs % 86400 
horas = seg_restantes // 3600
seg_restantes = total_segs % 3600
minutos = seg_restantes // 60
seg_restantes_final = seg_restantes % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",seg_restantes_final,"segundos.")
