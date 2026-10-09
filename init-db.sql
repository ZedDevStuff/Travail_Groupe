-- Script exécuté automatiquement au premier démarrage de PostgreSQL
-- Crée les 4 bases de données des microservices

-- service_livres est déjà créée via POSTGRES_DB dans le compose

CREATE DATABASE service_utilisateurs;
CREATE DATABASE service_emprunts;
CREATE DATABASE service_notifications;

-- Donner tous les droits à l'admin sur chaque base
GRANT ALL PRIVILEGES ON DATABASE service_livres       TO admin;
GRANT ALL PRIVILEGES ON DATABASE service_utilisateurs TO admin;
GRANT ALL PRIVILEGES ON DATABASE service_emprunts     TO admin;
GRANT ALL PRIVILEGES ON DATABASE service_notifications TO admin;
