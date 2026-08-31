A = int(input("Digite o valor do lado A:"))
B = int(input("Digite o valor do lado B:"))
C = int(input("Digite o valor do lado C:"))

if A != B and A != C:
    print("Valor A diferente dos demais")
if B != A and B != C:
    print("Valor B diferente dos demais")
if C != A and C != B:
    print("Valor C diferente dos demais")
if A == B and A == C:
    print("Todos os valores são iguais")
if B == A and B == C:
    print("Todos os valores são iguais")
if C == A and C == B:
    print("Todos os valores são iguais")



#Calcular a diferença entre dois números sem que o resultado fique negativo

A = int(input("Digite o primeiro número:"))
B = int(input("Digite o segundo número:"))

if A > B:
    print(A - B)
else:
    print(B - A)



#Pegar 3 números e colocar em números Decresentes

A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))

if A >= B and B >= C:
    print (A, B, C)
elif A >= C and C >= B:
    print (A, C, B)
elif B >= A and A >= C:
    print (B, A, C)
elif B >= C and C >= A:
    print (B, C, A)
elif C >= A and A >= B:
    print (C,A,B)
elif C >= B and B >= A:
    print (C,B,A)
else:
    print ("Todos os números são iguais")



#Leia 8 preços de produtos, somar cada preço e apresentar

