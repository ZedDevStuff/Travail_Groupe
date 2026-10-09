# **Bibliothèque Scolaire — Routes API** 

Documentation des endpoints par microservice 

## **● Service Utilisateurs** 

|**Méthode**|**Route**|**Description**|
|---|---|---|
|**POST**|/api/users/register|Inscription d'un nouvel utilisateur (étudiant, enseignant,<br>bibliothécaire)|
|**POST**|/api/users/login|Connexion — retourne un token d'authentification|
|**GET**|/api/users/profile/{id}|Consulter leprofil d'un utilisateur|
|**PUT**|/api/users/profile/{id}|Modifier les informations duprofil|



## **● Service Livres** **<mark>(</mark> Catalo** **<mark>g</mark> ue** **<mark>)</mark>** 

|**Méthode**|**Route**|**Description**|
|---|---|---|
|**GET**|/api/livres/|Récupérer la liste complète des livres du catalogue|
|**GET**|/api/livres/{id}|Consulter les détails d'un livre (auteur, genre, résumé,<br>stock)|
|**POST**|/api/livres/|Ajouter un nouveau livre au catalogue|
|**PUT**|/api/livres/{id}|Modifier les informations d'un livre existant|
|**DELETE**|/api/livres/{id}|Supprimer un livre du catalogue|



## **● Service Emprunts** 

|**Méthode**|**Route**|**Description**|
|---|---|---|
|**POST**|/api/emprunts/|Créer un nouvel empruntpour un étudiant|
|**PUT**|/api/emprunts/{id}/retour|Enregistrer le retour d'un livre emprunté|
|**GET**|/api/emprunts/{id}|Consulter les détails d'un emprunt spécifique|
|**GET**|/api/emprunts/historique|Voir l'historique complet des emprunts|
|**POST**|/api/reservations/|Créer une réservationpour un livre non disponible|
|**GET**|/api/reservations/|Consulter la liste des réservations en attente|



## **● Service Notifications** 

|**Méthode**|**Route**|**Description**|
|---|---|---|
|**GET**|/api/notifications/|Récupérer toutes les notifications d'un utilisateur|



