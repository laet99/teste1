import random

#banco de dados dos inspermons
meus_inspermons={"Aluno": [56, 32, 100]} #poder ataque -> poder defesa -> vida
inspermons_selvagens = {"Romero": [60, 32, 100],
                        "Hage": [56, 31, 100],
                        "Fernando": [46, 33, 100],
                        "Betao": [53, 24, 100],
                        "Ferraz": [43, 28, 100], 
                        "Daniel": [40, 36, 100]}
insperdex = {"Aluno": [56, 32, 100]}


def batalha (VidaInspermon, VidaPlayer, PoderPlayer, PoderIspermon, DefesaInspermon, DefesaPlayer):
    while VidaPlayer > 0 and VidaInspermon > 0:
        VidaInspermon = VidaInspermon - (PoderPlayer - DefesaInspermon)
        if VidaInspermon <= 0:
            return "Voce venceu a batalha"
        VidaPlayer = VidaPlayer - (PoderIspermon - DefesaPlayer)
        if VidaPlayer <= 0:
            return "Voce perdeu a batalha"


laco=1
while laco:
    pergunta_inicial=input("Voce deseja 'passear', 'ver inspermons', 'ver insperdex' ou 'dormir'? ")
    if pergunta_inicial=="ver insperdex":
        print(insperdex)
    elif pergunta_inicial=="ver inspermons":
        print(meus_inspermons)
    elif pergunta_inicial=="dormir":
          print ("Até logo!")
          break
    elif pergunta_inicial=="passear":
        inspermon = str(random.choice(list(inspermons_selvagens.items())))
        inspermon = inspermon.replace("('Romero', [60, 32, 100])", "Romero")
        inspermon = inspermon.replace("('Hage', [56, 31, 100])", "Hage")
        inspermon = inspermon.replace("('Fernando', [46, 33, 100])", "Fernando")
        inspermon = inspermon.replace("('Betao', [53, 24, 100])", "Betao")
        inspermon = inspermon.replace("('Ferraz', [43, 28, 100])", "Ferraz")
        inspermon = inspermon.replace("('Daniel', [40, 36, 100])", "Daniel")
        insperdex [inspermon] = inspermons_selvagens [inspermon]
        print("Um {} selvagem acabou de aparecer!".format(inspermon))
        while True:
            luta=input("Voce deseja 'batalhar', 'fugir' ou tentar 'capturar'? ")
            if luta == "batalhar":
                inspermon_utilizado=input("Dentre os inspermons a baixo:\n"+str(meus_inspermons)+"\nqual voce deseja utilizar? ")
                if inspermon_utilizado=="Aluno" or "Hage" or "Betao" or "Fernando" or "Romero" or "Daniel" or "Ferraz":
                    print("Se prepare para a batalha!")
                    print(batalha (100, 100, meus_inspermons[inspermon_utilizado][0], inspermons_selvagens[inspermon][0], inspermons_selvagens[inspermon][1], meus_inspermons[inspermon_utilizado][1]))
                    break              
            elif luta == "fugir":
                aleatorio=random.randint(0, 9)
                if aleatorio >5:
                    print("Sua fuga foi um fracasso!")
                    inspermon_utilizado=input("Dentre os inspermons a baixo:\n"+str(meus_inspermons)+"\nqual voce deseja utilizar? ")
                    if inspermon_utilizado=="Aluno" or "Hage" or "Betao" or "Fernando" or "Romero" or "Daniel" or "Ferraz":
                        print(batalha (100, 100, meus_inspermons[inspermon_utilizado][0], inspermons_selvagens[inspermon][0], inspermons_selvagens[inspermon][1], meus_inspermons[inspermon_utilizado][1]))
                        break
                    else:
                        print("Esse inspermon não é existente na sua lista (lembre da letra maiuscula)")
                if aleatorio <=5:
                    print("Sua fuga foi um sucesso! A batalha terminou em empate.")
                    break
            elif luta == "capturar":
                inspermon_utilizado=input("Dentre os inspermons a baixo:\n"+str(meus_inspermons)+"\nqual voce deseja utilizar? ")
                aleatorio2=random.randint(0, 9)
                if meus_inspermons[inspermon_utilizado][0] > inspermons_selvagens[inspermon][0]:
                    if aleatorio2 <= 6:
                        print("Voce capturou o inspermon selvagem!") #nao esta colocando o inspermon na minha lista
                        meus_inspermons[inspermon] = inspermons_selvagens[inspermon]
                        break
                    if aleatorio2 > 6:
                        print("Voce nao conseguiu captura-lo e o " + inspermon + " selvagem conseguiu fugir")
                        break
                if meus_inspermons[inspermon_utilizado][0] < inspermons_selvagens[inspermon][0]:
                    if aleatorio2 >= 7:
                        print("Voce capturou o inspermon selvagem!") #nao esta colocando o inspermon na minha lista
                        meus_inspermons[inspermon] = inspermons_selvagens[inspermon]
                        break
                    if aleatorio2 < 7:
                        print("Voce nao conseguiu captura-lo e o " + inspermon + " selvagem conseguiu fugir")
                        break
            else:
                print("Essa opção não existe, escolha entre 'batalhar', 'fugir' ou 'capturar")
    else:
        print("Essa opção nao existe, escolha entre: passear, dormir ou ver inspermons")

