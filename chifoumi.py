# DEBUT


# defini une fonction gagnant de paramètres joueur1_coup et joueur2_coup
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
    # initialisation du speudo du joueur1 au retoure l'éxécution de la fonction input de paramètre le nom du joueur
    # initialisation de joueur2 comme etant un Robot (un str)
    # initialisation d'un compteur de point nommé pointJoueur1 du joueur à 0
    # initialisation d'un compteur de point nommé pointJoueur2 du joueur à 0
    # initialisation du choix du joueur1 qui est un mot vide nommé choixJoueur1
    # initialisation du choix du joueur2 qui est un mot vide nommé choixJoueur2
    # initialisation gagner valant 0
    # initialisation d'un dictionnaire nommé dico qui a pour clè le nom du coup joué et la valeur de celui-ci ##{pierre:0, papier:1, ciseaux:2}
    # initialisation de isRègle valant le retoure l'éxécution de la fonction input de paramètre le choix si le joueur veut voir les règles
    # initialisation de règlesDuJeu qui est un str ##expliquant les règles du jeu
    # initialisation de cpt valant 0

    # si isRègle vaut vrai
        # alors
        # afficher règlesDuJeu grâce au retour de l'éxécution de la fontion print de paramètre règlesDuJeu 

    # tant que cpt <= nbRound
        # alors
        #Si gameMode est True 
            # alors
            # assigne du speudo du joueur2  grâce au retoure l'éxécution de la fonction input de paramètre le nom du joueur
            # afficher le choix des coups possibles grâce au retour de l'éxécution de la fontion print de paramètre les valeurs de dico ##(dico.items)
            # assigner à choixJoueur1 la valeur du retour de l'éxécution de la fonction input de paramètre le numéro de clé du dictionnaire pour choisir le coup qu'il veut jouer
            # assigner à choixJoueur2 la valeur du retour de l'éxécution de la fonction input de paramètre le numéro de clé du dictionnaire pour choisir le coup qu'il veut jouer

        # Sinon (joueur2 est un robot)
            # alors
            # afficher le choix des coups possibles grâce au retour de l'éxécution de la fontion print de paramètre les valeurs de dico ##(dico.items)
            # assigner à choixJoueur1 la valeur du retour de l'éxécution de la fonction input de paramètre le numéro de clé du dictionnaire pour choisir le coup qu'il veut jouer
            # assigner à choixJoueur2 la valeur du retour de l'éxécution de la fonction random de paramètre les valeurs de dico ##(dico.values) ### (0,1,2)

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