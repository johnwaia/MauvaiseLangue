# MauvaiseLangue

**MauvaiseLangue** est un module Python qui permet de scraper et détecter des insultes en français depuis le Wiktionnaire. Il inclut également une fonctionnalité pour obtenir les définitions des insultes détectées.

## Fonctionnalités

- **Scraping d'insultes** : Récupère la liste des insultes en français depuis la page Wiktionnaire dédiée.
- **Cache local** : Les insultes récupérées sont stockées en local pour éviter de re-scraper inutilement.
- **Détection d'insultes** : Analyse un texte pour y détecter des insultes présentes dans la base de données (scrapée ou en cache).
- **Récupération des définitions** : Accède à la page Wiktionnaire de chaque insulte pour en extraire la définition.

## Installation

Installez les dépendances requises via `pip` :

```bash
pip install MauvaiseLangue
```

## Utilisation

### 1. Afficher les insultes

Pour afficher les insultes :

```python
from MauvaiseLangue import scrape_insultes

insultes = scrape_insultes()
print(insultes)
```

### 2. Détecter des insultes dans un texte

Vous pouvez vérifier si un texte contient des insultes :

```python
from MauvaiseLangue import detect_insultes

texte = "Tu es vraiment stupide et nul."
insultes_detectees = detect_insultes(texte)
print(insultes_detectees)
```

### 3. Obtenir la définition d'une insulte

Pour obtenir la définition d'une insulte :

```python
from MauvaiseLangue import get_definition_insulte

definition = get_definition_insulte("idiot")
print(definition)
```

## Fichiers de cache

Le module utilise un fichier `insultes_cache.json` pour stocker les insultes récupérées afin d'améliorer les performances. Ce fichier est automatiquement créé et mis à jour lors du scraping.

## Contributeurs

- [johnwaia](https://github.com/votreprofil) 

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
