import time

def nume():
    nume.x = str(input("numele tau: "))

def meniu():
    print("                                                                          ")
    print("--------------------------------------------------------------------------")
    time.sleep(0.2)
    print("Acesta este meniul.")
    time.sleep(0.2)
    print("Tasteaza alegerea ta in linia de comanda.")
    time.sleep(0.2)
    print("Pentru a accesa cursul noastru tastati in linia de comanda < curs >.")
    time.sleep(0.2)
    print("Pentru a participa la webminar tastati in linia de comanda < web >.")
    time.sleep(0.2)
    print("Pentru datele de contact tastati in linia de comanda < contact >.")
    time.sleep(0.2)
    print("Pentru a reveni la start tastati in linia de comanda < exit >.")
    print("--------------------------------------------------------------------------")

def sageata():
    time.sleep(0.1)
    print(" | | | |")
    print(" v v v v")

def introducere():
    print(" Bine ati venit pe platforma noastra! ")
    time.sleep(0.4)
    nume()
    print(" ")
    time.sleep(0.2)
    print("Salut",nume.x,"! :)""\n Iti dedicam aceasta pagina.")
    meniu()
    sageata()
    introducere.x = nume.x

def dialog_run():
    time.sleep(0.08)
    dialog_run.intrebare = str(input("Intrebarea ta: "))
    if dialog_run.intrebare == "pa" :
        print("Chatbot: Sper sa ai zi minunata,", introducere.x, "!")
        program()
    while dialog_run.intrebare != "pa" :
        gpt2.generate(sess,
              length=50,
              temperature=1,
              prefix=dialog_run.intrebare,
              nsamples=1,
              batch_size=5,
              top_k=40,
              top_p=0.9
              )
        dialog_run()

def dialog():
    t = time.localtime()
    ora_curenta = time.strftime("%H:%M:%S", t)
    print("Cum doresti sa se numeasca acest chatbot?")
    dialog.nume = str(input("nume chatbot: "))
    time.sleep(0.1)
    print("Chatbot: Ma numesc",dialog.nume,". Si ma bucur ca discutam!")
    print("         Numele creatorului meu este",introducere.x,". Si ii multumesc pentru ca mi-a dat un scop.")
    print("         Ora curent este",ora_curenta,". Inca mai ai timp sa faci putina miscare si sa te hidratezi!")
    dialog_run()

def interactiv():
    time.sleep(0.2)
    print("Daca ai inteles ce presupune programarea unei inteligente artificiale si esti dornic sa lucrezi la propriul tau AI, atunci urmeaza urmatorii pasi. >>>")
    time.sleep(0.2)
    print("Te vom ajuta sa creezi un chatbot care va afisa raspunsul pentru orice vei scrie.")
    print("")
    time.sleep(0.1)
    print("Daca doresti sa parasesti conversatia cu chatbot-ul tau si sa te intorci la linia de comanda tasteaza < pa > .")
    print("")
    time.sleep(0.2)
    print("Pentru inceput vom introduce cativa parametrii.")
    time.sleep(0.2)
    dialog()

def program():
    print(" ")
    time.sleep(0.2)
    print("Tasteaza < meniu > pentru a afisa meniul.")
    y = str(input("Linia de comanda: "))

    if y == "web":
        print(" ")
        print("Acesta este link-ul de acces: --- momentan nu este disponibil")
    elif y == "curs":
        print(" ")
        time.sleep(0.2)
        with open("curs.txt", "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())
        print(" ")
        time.sleep(0.2)
        print("===================================================================")
        print("")
        print("Tasteaza < bot > in linia de comanda pentru a creea propriul robot.")
        print("^^^^^^^^")
    elif y == "bot":
        interactiv()
    elif y == "meniu":
        meniu()
    elif y == "exit":
        time.sleep(0.2)
        print("La revedere!")
        print(" ")
        introducere()
    elif y == "contact":
        print("Date de contact")
        print("")
    else:
        print("Verifica codul")

class site:
    introducere()
    while True:
        program()

site()
