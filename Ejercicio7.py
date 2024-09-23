#Los tramos impositivos para la declaración de renta en un determinado país son los
#siguientes:

#   Renta                   Tipo impositivo
#   Menos de $100,000           5%
#   Entre $100,000 y $200,000   15%
#   Entre $200,000 y $350,000   20%
#   Entre $350,000 y $600,000   30%
#   Más de $600,000             45%


renta = float(input('Renta anual que debe declarar, $'))
if (renta < 100000):
    tipo = 5
elif (renta > 100000 and renta < 200000):
    tipo = 15
elif (renta > 200000 and renta < 350000):
    tipo = 20
elif (renta > 350000 and renta < 600000):
    tipo = 30
else:
    tipo = 45

print('Usted debe cancelar $',(renta * tipo)/100, sep='')