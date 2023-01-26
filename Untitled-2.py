January = 0
February = 0
March = 0
April = 0
Mai = 0
June = 0
July = 0
August = 0
September = 0
October = 0
November = 0
December = 0
i1 = 0
i2 = 0
i3 = 1
i4 = 0
res1 = 0
res2 = 0
res3 = 0
res4 = 0
while i3 <= 9:
    res3 += i3
    i3+=1
while i1 <= 9:
    res1 += 1 + i1
    i1+=1
while i2 <= 9:
    res2 += 2 + i2
    if i2 == 7:
        February += res1 + res2 + res3 
    i2+=1
while i4 < 2:
    res4 += 3 + i2
    if i4 == 0:
        April += res1 + res2 + res3 + res4 
        June += res1 + res2 + res3 + res4 
        September += res1 + res2 + res3 + res4 
        November += res1 + res2 + res3 + res4 
    if i4 == 1:
        January += res1 + res2 + res3 + res4 
        March += res1 + res2 + res3 + res4 
        Mai += res1 + res2 + res3 + res4 
        July += res1 + res2 + res3 + res4 
        August += res1 + res2 + res3 + res4 
        October += res1 + res2 + res3 + res4 
        December += res1 + res2 + res3 + res4 
    i4+=1
print("Результат общий: ", February+April+June+September+November+January+March+Mai+July+August+October+December)
print("Февраль: ", February)
print("Апрель: ", April)
print("Июнь: ", June)
print("Сентябрь: ", September)
print("Ноябрь: ", November)
print("Январь: ", January)
print("Март: ", March)
print("Май: ", Mai)
print("Июль: ", July)
print("Август: ", August)
print("Октябрь: ", October)
print("Декабрь: ", December)