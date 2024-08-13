import cv2

# Ouvrir la capture vidéo en utilisant le premier périphérique disponible (généralement la webcam)
cap = cv2.VideoCapture(0)

# Vérifier si la capture vidéo a été ouverte avec succès
if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la capture vidéo.")
else:
    while True:
        # Lire une image de la capture vidéo
        ret, frame = cap.read()
        
        # Vérifier si l'image a été lue avec succès
        if not ret:
            print("Erreur: Impossible de lire l'image de la capture vidéo.")
            break
        
        # Afficher l'image dans une fenêtre
        cv2.imshow('Video', frame)
        
        # Attendre 1 milliseconde et vérifier si l'utilisateur appuie sur la touche 'q' pour quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer la capture vidéo et détruire toutes les fenêtres
    cap.release()
    cv2.destroyAllWindows()
