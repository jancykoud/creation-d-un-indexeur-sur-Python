## Indexeur de Mots pour Fichiers Texte
## Aperçu
Ce projet indexe les mots contenus dans des fichiers texte d'un répertoire spécifié et de ses sous-répertoires. Il crée un index de mots (définis comme des séquences de 4 à 8 caractères incluant des lettres, des chiffres ou des traits d'union) et les chemins des fichiers contenant ces mots. Le projet est implémenté en Python et utilise les modules `json`,`os`, `re`, et `sys`.

## Structure
Le projet se compose de trois parties principales :

1. **Indexation Basée sur un Dictionnaire** : Les mots sont indexés en utilisant un dictionnaire Python.
2. **Indexation Basée sur un Arbre** : Les mots sont indexés en utilisant une structure d'arbre personnalisée.
3. **Recherche de Fichiers** : Recherche de fichiers basée sur des termes saisis par l'utilisateur et affichage des lignes pertinentes de ces fichiers.

### Scripts

### 1. Indexation Basée sur un Dictionnaire (`index_dict.py`)
- Ce script parcourt le répertoire spécifié et ses sous-répertoires.
- Il identifie les mots dans les fichiers texte (.txt) et les indexe dans un dictionnaire.
- L'index est sauvegardé dans un fichier JSON nommé dict_index.json.

### 2. Indexation Basée sur un Arbre (`index_tree.py`)
- Ce script parcourt également le répertoire spécifié et ses sous-répertoires.
- Il utilise une structure d'arbre où chaque nœud représente un caractère, et les nœuds feuilles stockent les chemins de fichiers.
- L'index est converti en dictionnaire et sauvegardé dans un fichier JSON nommé `tree_index.json`.

### 3. Recherche de Fichiers (`search_word.py`)
- Ce script désérialise l'index JSON sauvegardé.
- Il invite l'utilisateur à saisir des termes de recherche, qui peuvent inclure des mots de l'index.
- Le script trouve et affiche les fichiers correspondants à la recherche, y compris les lignes contenant les mots recherchés.
- Il permet des fonctions de méta-recherche, telles que le filtrage sur les extensions de fichiers avec le mot-clé `type:<ext>`.

### Utilisation
1. **Configuration** :

 - Modifiez la variable `home_path` dans les scripts d'indexation pour le chemin du répertoire que vous souhaitez indexer.
 - Assurez-vous que le fichier d'index JSON est dans le même répertoire que `search_word.py`.

2. **Exécution des Scripts** :

 - Exécutez `index_dict.py` ou `index_tree.py` pour créer l'index.
 - Exécutez `search_word.py` pour rechercher des termes dans les fichiers indexés.

3. **Sortie**:

 - Consultez les fichiers JSON générés (`dict_index.json` et `tree_index.json`) pour les données indexées.
 - Voir les résultats de la recherche dans la console lors de l'exécution de `search_word.py`.

## Prérequis
 - Python 3.x
 - Modules Python de base : `json`, `os`, `re`, `sys`.