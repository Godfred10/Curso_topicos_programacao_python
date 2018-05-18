frequencia=float(input("a frequencia do aluno:"))
if frequencia >= 75:
    notaMd = float(input("a media de p1 e p2:"))
    if notaMd >= 7:
        print("aprovado")
    elif notaMd < 3:
        print("reprovado")
    elif notaMd < 7:
        print("prova final")
        notaPf = float(input("a nota da prova final: "))
        mediaFinal = notaPf + notaMd/2
        if mediaFinal < 5:
            print("reprovado")
        else:
            print("aprovado")
else:
    print("reprovado")



