import math
import sys

z1 = round((int(input("z шестерни:",))),3)
z2 = round((int(input("z колеса:",))),3)
mte = round((float(input("mte:",))),3)
if 0 <= mte <= 2.5:
    print("боковой зазор (С) равен 0.1")
elif 2.6 <= mte <= 4:
    print("боковой зазор (С) равен 1.5") 
elif 4.1 <= mte <= 6:
    print("боковой зазор (С) равен 0.2")
elif 6.1 <= mte <= 8:
    print("боковой зазор (С) равен 0.25")
elif 8.1 <= mte <= 12:
    print("боковой зазор (С) равен 0.4")
elif 12.1 <= mte <= 15:
    print("боковой зазор (С) равен 0.5")
else:
    print("боковой зазор (С) на усмотрение конструктора")
    
mn = round((float(input("mn:",))),3)
b = round((float(input("b:",))),3)
alpha = 20 #tg20
alpharadians = math.radians(alpha)

tgalpharadians = round(math.tan(alpharadians),4)
beta = 35 #tg35
betaradians = math.radians(beta)
tgbetaradians = round(math.tan(betaradians),4)
d0 = round((float(input("диаметр головки(do):",))),3)
ru = d0/2
zc = round((math.sqrt(z1**2 + z2**2)),6)
print("zc:",zc)
Re = mte * (zc / 2)

R = Re - (b / 2)

Bm = int(input("средний угол наклона спирали(Bn):",))

if 30 <= Bm <= 40:
    if 0 <= Re <= 40 or 0 <= b <= 20:
        print("рекомендуемое (do) 60 или 80 ")
    elif 40 <= Re <= 60 or 21 <= b <= 30:
        print("рекомендуемое (do) 100 или 125 ")
    elif 61 <= Re <= 80 or 31 <= b <= 38:
        print("рекомендуемое (do) 125 или 160 (6 дюймов)")
    elif 81 <= Re <= 100 or 39 <= b <= 50:
        print("рекомендуемое (do) 160 или 200 (7.5 дюймов)")
    elif 101 <= Re <= 130 or 51 <= b <= 65:
        print("рекомендуемое (do) 200 или 250 (9 дюймов)")
    elif 131 <= Re <= 190 or 66 <= b <= 100:
        print("рекомендуемое (do) 250 или 315 (12 дюймов)")
    elif 191 <= Re <= 380 or 101 <= b <= 125:
        print("рекомендуемое (do) 315 или 400 (18 дюймов)")
    else:
        print("рекомендуемое (do) 400 или 500 (18 дюймов)")
else:
    if 0 <= Bm or Bm >41:
        print("(Bn) Не рекомендуемый параметр по фрезе", file=sys.stderr)
    

    
cosBm = round(math.cos(math.radians(Bm)),5)
sinBm = round(math.sin(math.radians(Bm)),4)

sumQf = math.floor((((10800*tgbetaradians)/tgalpharadians)-((((10800*tgbetaradians)/tgalpharadians) * ((sinBm/ru)*R))))/(zc *sinBm))

V0 = round((ru * cosBm), 5)
H0 = R - (ru * sinBm)
U0 = round(math.sqrt(V0**2 + H0**2),6)

q_rad = math.atan2(V0, H0)
q = math.degrees(q_rad)
q_1 = math.floor(q)
q_degrees = round((((q - q_1)/100*60) + q_1), 2)
print("q",q_degrees)
sin_q = round(math.sin(math.radians(q)), 6)
empty11 = round((U0/270), 6)
sin_e02 = empty11
degrees_sin_e0 = math.asin(sin_e02)
degrees_sin_e0_1 = round(math.degrees(degrees_sin_e0),6)
degrees_sin_e0_2 = degrees_sin_e0_1 * 2
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
degrees_sin_e0_3 = math.floor(degrees_sin_e0_2)
degrees_sin_e0_4 = round((((degrees_sin_e0_2 - degrees_sin_e0_3)/100*60) + degrees_sin_e0_3),2)
print("e0:", degrees_sin_e0_4)
degrees_sin_vip  = degrees_sin_e0_4 - 0.25
degrees_sin_vog  = degrees_sin_e0_4 - 0.1
print("e0_выпуклая:",degrees_sin_vip,"e0_вогнутая:",degrees_sin_vog)

Q_left= degrees_sin_e0_1 + q
Q_left_1 = math.floor(Q_left)
Q_left_degrees = round((((Q_left - Q_left_1)/100*60) + Q_left_1), 2)
print("Q_левое",Q_left_degrees)

Q_right = degrees_sin_e0_1 - q
Q_right_1 = math.floor(Q_right)
Q_right_degrees_1 = round((((Q_right - Q_right_1)/100*60) + Q_right_1), 2)
if Q_right_degrees_1 <= 0:
    Q_right_degrees_1 = Q_right + 360
    Q_right_degrees_2 = math.floor(Q_right_degrees_1)
    Q_right_degrees_3 = round((((Q_right_degrees_1 - Q_right_degrees_2)/ 100*60) + Q_right_degrees_2),2)#88_2
print("Q_правое:", Q_right_degrees_3)

deltacons = math.floor(sumQf)

N0 = round(((deltacons/20) * sinBm),3)
print("номер резца ",N0)

Nf = math.ceil((deltacons/20) * sinBm)
if Nf >= 12:
    print("номер резца рекомендуемый: 12")
else:    
    print("номер резца рекомендуемый:",Nf)
               
sinBm1 = round(((20*Nf)/deltacons),6)
Bm1 = math.asin(sinBm1)
asinBm1 = round(math.degrees(Bm1),6)
greesBm1 = math.floor(asinBm1)
#print("Угол наклона фактический:", greesBm1)
minutesBm1 = round(((((asinBm1) - greesBm1)/100*60) + greesBm1), 2)
cosBm1  = round((math.cos(math.radians(asinBm1))),6)

Qf = sumQf / 2
Qf1_1 = Qf / 60
tgQf2 = math.tan(math.radians(Qf1_1))
cosQf2 = round((math.cos(math.radians(Qf1_1))),4)


hm = 2.25 * mn
h = round((hm + (b * tgQf2)), 3)
print("h высота у большого модуля:",h)
               
zi = int(input("введите число не кратное ни колесу ни шестерне от 7 до 17:",))

idsh = round((2 * (zi / z1)),6)
idk = round((2 * (zi / z2)),6)

print("гитара деления для шестерни", idsh)
"""
for gear_1 in range(34, 91):
    for gear_2 in range(34, 91):
        variant_2gears = gear_1 / gear_2
        variant_2gears = round((variant_2gears), 7)
        diff_1 = idsh - 0.000001
        diff_2 = idsh + 0.000001
        if diff_1 < variant_2gears < diff_2:
            print(gear_1, "/", gear_2, "=", variant_2gears)
            break
        else:
            variant_4gears_1 = gear_1 * gear_2
            for gear_3 in range(34,91):
                for gear_4 in range(34,91):
                    variant_4gears_2 = gear_3 * gear_4
                    variant_4gears = round((variant_4gears_1 / variant_4gears_2), 7)
                    if diff_1 <= variant_4gears <= diff_2:
                        break
                        print()
                        print(gear_1, "*", gear_2,)
                        print("--    --", "=", variant_4gears)
                        print(gear_3, "*", gear_4,)
                        print()
                        
"""         
print("гитара деления для колеса",idk)
"""
for gear_1 in range(34, 91):
    for gear_2 in range(34, 91):
        variant_2gears = gear_1 / gear_2
        variant_2gears = round((variant_2gears), 7)
        diff_1 = idk - 0.000001
        diff_2 = idk + 0.000001
        if diff_1 < variant_2gears < diff_2:
            print(gear_1, "/", gear_2, "=", variant_2gears)
            break
        else:
            variant_4gears_1 = gear_1 * gear_2
            for gear_3 in range(34,91):
                for gear_4 in range(34,91):
                    variant_4gears_2 = gear_3 * gear_4
                    variant_4gears = round((variant_4gears_1 / variant_4gears_2), 7)
                    if diff_1 <= variant_4gears <= diff_2:
                        break
                        print()
                        print(gear_1, "*", gear_2,)
                        print("--    --", "=", variant_4gears)
                        print(gear_3, "*", gear_4,)
                        print()
"""
i_exemple_0 = round((3.5 * (zi/zc)),6)
print("обкат для колеса:", i_exemple_0)
"""


for gear_1 in range(34, 91):
    for gear_2 in range(34, 91):
        variant_2gears = gear_1 / gear_2
        variant_2gears = round((variant_2gears), 7)
        diff_1 = i_exemple_0 - 0.000001
        diff_2 = i_exemple_0 + 0.000001
        if diff_1 < variant_2gears < diff_2:
            print(gear_1, "/", gear_2, "=", variant_2gears)
            break
        else:
            variant_4gears_1 = gear_1 * gear_2
            for gear_3 in range(34,91):
                for gear_4 in range(34,91):
                    variant_4gears_2 = gear_3 * gear_4
                    variant_4gears = round((variant_4gears_1 / variant_4gears_2), 7)
                    if diff_1 <= variant_4gears <= diff_2:
                        print()
                        print(gear_1, "*", gear_2,)
                        print("--   --", "=", variant_4gears)
                        print(gear_3, "*", gear_4,)
                        print()

"""
i_exemple_1 = round(((3.5 * zi)/(zc - 0.25)),6)
print("обкат для выпуклой:", i_exemple_1)
"""
for gear_1 in range(34, 91):
    for gear_2 in range(34, 91):
        variant_2gears = gear_1 / gear_2
        variant_2gears = round((variant_2gears), 7)
        diff_1 = i_exemple_1 - 0.000001
        diff_2 = i_exemple_1 + 0.000001
        if diff_1 < variant_2gears < diff_2:
            print(gear_1, "/", gear_2, "=", variant_2gears)
            break
        else:
            variant_4gears_1 = gear_1 * gear_2
            for gear_3 in range(34,91):
                for gear_4 in range(34,91):
                    variant_4gears_2 = gear_3 * gear_4
                    variant_4gears = round((variant_4gears_1 / variant_4gears_2), 7)
                    if diff_1 <= variant_4gears <= diff_2:
                        print()
                        print(gear_1, "*", gear_2,)
                        print("--   --", "=", variant_4gears)
                        print(gear_3, "*", gear_4,)
                        print()

"""
i_exemple_2 = round(((3.5 * zi)/(zc + 0.2)),6)
print("обкат для вогнутой:", i_exemple_2)

"""
for gear_1 in range(34, 91):
    for gear_2 in range(34, 91):
        variant_2gears = gear_1 / gear_2
        variant_2gears = round((variant_2gears), 7)
        diff_1 = i_exemple_2 - 0.000001
        diff_2 = i_exemple_2 + 0.000001
        if diff_1 < variant_2gears < diff_2:
            print(gear_1, "/", gear_2, "=", variant_2gears)
            break
        else:
            variant_4gears_1 = gear_1 * gear_2
            for gear_3 in range(34,91):
                for gear_4 in range(34,91):
                    variant_4gears_2 = gear_3 * gear_4
                    variant_4gears = round((variant_4gears_1 / variant_4gears_2), 7)
                    if diff_1 <= variant_4gears <= diff_2:
                        print()
                        print(gear_1, "*", gear_2,)
                        print("--   --", "=", variant_4gears)
                        print(gear_3, "*", gear_4,)
                        print()                        
"""
    
input("Нажмите для выхода...")
