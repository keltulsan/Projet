from msvcrt import kbhit
import random

class chifoumi :
    """ Class qui permet de faire un chifoumi"""

    def gagner (self, joueur1_coup, joueur2_coup) :
        """Cette fonction prend en paramètre le coup des deux joueurs 
            et qui va ensuite renvoyer le gangant selon le coup jouer"""
        gagnant = 0
        if joueur1_coup == "pierre":
            if joueur2_coup == "pierre":
                gagnant = 0
            elif joueur2_coup == "papier":
                gagnant = 2
            elif joueur2_coup == "ciseaux":
                gagnant = 1
        elif joueur1_coup == "papier":
            if joueur2_coup == "pierre":
                gagnant = 1
            elif joueur2_coup == "papier":
                gagnant = 0
            elif joueur2_coup == "ciseaux":
                gagnant = 2
        elif joueur1_coup == "ciseaux":
            if joueur2_coup == "pierre":
                gagnant = 2
            elif joueur2_coup == "papier":
                gagnant = 1
            elif joueur2_coup == "ciseaux":
                gagnant = 0
        return gagnant
    
    def pierrePapierCiseaux (self, multiplayer : bool, nbRound):
        """ Fonction qui prend en paramètre multiplayer ou non 
            et le nombre de round à jouer """
        pseudoJoueur1 = str(input("Joueur 1 choississez votre pseudo : "))
        pseudoJoueur2 = "Robot"
        pointJoueur1 = 0
        pointJoueur2 = 0
        choixJoueur1 = ""
        choixJoueur2 = ""
        gagnant = 0
        tab = ["pierre", "papier", "ciseaux"]
        coup = ""
        isRègle = input("Choississez vous de voir les règles du jeu, si oui entrer 'True' sinon entrer 'False' : ")
        règlesDuJeu = "Voici les règles du jeu. Pour commencer pour joueur il faut au mininmum 2 joueurs. Ensuite vous avez le droit entre 3 actions, la première la 'pierre', la seconde le 'papier' et pour finir le 'ciseaux'.\n Pour pouvoir gagner il faut le coup étant le plus fort, pour se faire on a la 'pierre' qui bat le 'ciseaux', le 'papier' qui bat la 'pierre' et le 'ciseaux' qui bat 'papier'.\n Bonne chance à vous et que le meilleur gagne."
        cpt = 0

        for i in tab :
            coup = coup + i + ", "
        coup = coup[:-2] #retire la dernière virgule

        if isRègle == "True":
            print(règlesDuJeu) 
        

        if multiplayer :
            pseudoJoueur2 = str(input("Joueur 2 choississez votre pseudo : "))


        while cpt < nbRound :
            if multiplayer :
                print("Voici les coups Possibles " + coup )
                choixJoueur1 = str(input("Joueur 1 choississez votre coup : "))
                choixJoueur2 = str(input("Joueur 2 choississez votre coup : "))
            else :
                choixJoueur1 = str(input("Joueur 1 choississez votre coup : "))
                choixJoueur2 = random.choices(tab)
                choixJoueur2 = choixJoueur2[0]
                print(choixJoueur2)

            gagner = chifoumi().gagner(choixJoueur1, choixJoueur2)

            if gagner == 1 :
                pointJoueur1 += 1
                print("Le joueur 1 gagne avec " + choixJoueur1 + "\n")
            elif gagner == 2 :
                pointJoueur2 += 1
                print("Le joueur 2 gagne avec"  + choixJoueur2 + "\n")
            elif gagner == 0:
                print("Egalité " + "\n")
            cpt += 1


        winRateJoueur1 = pointJoueur1/nbRound
        winRateJoueur2 = pointJoueur2/nbRound

        return print("Le joueur 1 a " + str(pointJoueur1) + " point"), print("Le joueur 2 a " + str(pointJoueur2) + " point"), print("Le taux de win du joueur 1 est : " + str(winRateJoueur1)), print("Le taux de win du joueur 2 est : " + str(winRateJoueur2))

chifoumi().pierrePapierCiseaux(False,2)
