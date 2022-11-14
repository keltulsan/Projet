# DEBUT


# defini une fonction gagner de paramètres joueur1_coup et joueur2_coup
    # initialisation de gagnant valant 0 ##si gaganant vaut 1 le gagnant est le joueur 1, si gagnant vaut 2 le gagnant est le joueur 2, et si gagnant vaut 0 c'est une égalité
    # si joueur1_coup vaut pierre (un str)
        # alors
        # si joueur2_coup vaut pierre (un str)
            # alors
            # assigner à gagnant la valeur 0
        # si joueur2_coup vaut papier  (un str)
            # alors
            # assigner à gagnant la valeur 2
        # si joueur2_coup vaut ciseaux (un str)
            # alors
            # assigner à gagnant la valeur 1

    # si joueur1_coup vaut papier (un str)
        # alors
        # si joueur2_coup vaut pierre (un str)
            # alors
            # assigner à gagnant la valeur 1
        # si joueur2_coup vaut papier (un str)
            # alors
            # assigner à gagnant la valeur 0
        # si joueur2_coup vaut ciseaux (un str)
            # alors
            # assigner à gagnant la valeur 2

    # si joueur1_coup vaut ciseaux(un str)
        # alors
        # si joueur2_coup vaut pierre (un str)
            # alors
            # assigner à gagnant la valeur 2
        # si joueur2_coup vaut papier (un str)
            # alors
            # assigner à gagnant la valeur 1
        # si joueur2_coup vaut ciseaux (un str)
            # alors
            # assigner à gagnant la valeur 0 
    # renvoyer gagnant (un int)




# defini la fonction pierrePapierCiseau de paramètres multiplayer qui est un booléen , nbRound qui est un int
    # initialisation du pseudo du joueur1 au retoure l'éxécution de la fonction input de paramètre le nom du joueur
    # initialisation de joueur2 comme etant un str nommé Robot
    # initialisation d'un compteur de point nommé pointJoueur1 du joueur à 0
    # initialisation d'un compteur de point nommé pointJoueur2 du joueur à 0
    # initialisation du choix du joueur1 qui est un mot vide nommé choixJoueur1
    # initialisation du choix du joueur2 qui est un mot vide nommé choixJoueur2
    # initialisation gagner valant 0
     # initialisation coup valant ""
    # initialisation d'un dictionnaire nommé tab qui a pour clè le nom du coup joué ##[pierre, papier, ciseaux]
    # initialisation de isRègle valant le retoure l'éxécution de la fonction input de paramètre le choix si le joueur veut voir les règles (True or False)
    # initialisation de règlesDuJeu qui est un str ##expliquant les règles du jeu
    # initialisation d'un compteur nommé cpt valant 0

    # pour i dans tab
        # alors 
        # coup qui est incrémenter de lui même plus de i et ensuite d'une virgule
    # modification de i où l'on retire la dernière virgule ## coup = coup[:-2]

    # si isRègle vaut vrai
        # alors
        # afficher les règlesDuJeu 


    # assigne du pseudo du joueur2  grâce au retoure l'éxécution de la fonction input de paramètre le nom du joueur
    # tant que cpt < nbRound
        # alors
        #Si multiplayer est True 
            # alors
            # afficher le choix des coups possibles ##les valeurs detab
            # assigner à choixJoueur1 la valeur du retour de l'éxécution de la fonction input de paramètre le numéro de clé du dictionnaire pour choisir le coup qu'il veut jouer
            # assigner à choixJoueur2 la valeur du retour de l'éxécution de la fonction input de paramètre le numéro de clé du dictionnaire pour choisir le coup qu'il veut jouer

        # Sinon (joueur2 est un robot)
            # alors
            # afficher le choix des coups possibles ## les valeurs de tab
            # assigner à choixJoueur1 la valeur du retour de l'éxécution de la fonction input de paramètre le numéro de clé du dictionnaire pour choisir le coup qu'il veut jouer
            # assigner à choixJoueur2 la valeur du retour de l'éxécution de la fonction random de paramètre les valeurs de tab ### ("pierre, papier, ciseaux")

        # assigner à gagner la valeur que retourne l'exécution de la fonction gagnant de paramètres choixJoueur1 et choixJoueur2

        # si gagner vaut 1 
            # alors
            # incrémenter de 1 pointJoueur1
        # si sinon gagner vaut 2
            # alors
            # incrémenter de 1 pointJoueur2

        # incrémenter de 1 cpt

    # initialisation winRateJoueur1 de valeur pointJoueur1/nbRound
    # initialisation winRateJoueur2 de valeur pointJoueur2/nbRound

    # renvoyer pointJoueur1, pointJoueur2, winRateJoueur1, winRateJoueur2

# FIN
