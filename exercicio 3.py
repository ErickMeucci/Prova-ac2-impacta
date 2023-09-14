def dia_da_semana(s):
    if(s == ('segunda')):
        x = 1
    elif(s == ('terca')):
        x = 2
    elif(s == ('quarta')):
        x = 3
    elif(s == ('quinta')):
        x = 4
    elif(s == ('sexta')):
        x = 5
    elif(s == ('sabado')):
        x = 6
    elif(s == ('domingo')):
        x = 7
    return x

def dia_da_entrega(r):
    if (r == 1):
        print('sera entregue segunda')
    elif(r == 2):
        print('sera entregue terca')
    elif(r == 3):
        print('sera entregue quarta')
    elif(r == 4):
        print('sera entregue quinta')
    elif(r == 5):
        print('sera entregue sexta')
    elif(r == 6):
        print('sera entregue sabado')
    elif(r == 7):
        print('sera entregue domingo')




s = str(input())
d = int(input())
g = dia_da_semana(s)
y = g + d
f = y - 7
if(d == 0):
    print('chega hoje!')
elif(y <= 7):
    a = dia_da_entrega(y)
else:
    b = dia_da_entrega(f)
















    
