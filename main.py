taches = []

while True:
    print("=== GESTION DES TACHES ===")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")

    choix = input("Votre choix : ")

    match choix:
        case "1":
            print("Ajouter une tâche")
            tt=""
            while (tt.strip()==""):
                tt=input("donner le  titre de la tache")
                if tt.strip()=="":
                    print("error")
            else:
                taches.append(tt)
            


        case "2":
            print("Afficher les tâches")
            if not taches:
                print("aucun elements enregistrer")
            else:
                for i in range (len(taches)):
                    print(i+1,"-",taches[i])
                
        case "3":
            print("Rechercher une tâche")
            mot=input("donner le cle ").strip()
            if mot =="":
                print("veuillez ecrire un mot")
            else:
                trouve=False
                for i in range (len(taches)):
                    if mot.lower() in taches[i].lower():
                        print (i+1,"-",taches[i])
                        trouve=True
                if trouve==False:
                    print("there nothing")
        case "0":
            print("Au revoir !")
            break

        case _:
            print("Choix invalide")