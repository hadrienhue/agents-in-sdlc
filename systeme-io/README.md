# Tunnel systeme.io – BioConnect × Spengler

Tunnel en 3 pages : **capture → merci → vente**. Chaque fichier `.html` se colle tel quel dans un élément **Code HTML** (Raw HTML) de systeme.io.

| Page systeme.io | Contenu de la page (dans l'ordre) |
|---|---|
| 1. Capture | `1-capture-bloc-A.html` → **formulaire natif systeme.io** → `1-capture-bloc-B.html` |
| 2. Merci | `2-merci.html` |
| 3. Vente | `3-vente.html` (le bouton mène à votre page de commande systeme.io) |

## Réglages dans systeme.io

1. Pour chaque section : **pleine largeur**, marges intérieures (padding) à 0.
2. Formulaire de la page 1 : champs Prénom et E-mail (+ champ facultatif « Vous êtes : particulier / professionnel de santé / pharmacie »), case **non obligatoire et non pré-cochée** « J'accepte de recevoir des informations sur les produits BioConnect », bouton « JE REÇOIS LE GUIDE » (couleur `#F26B1D`, arrondi max), section en fond `#111111`. Après l'envoi, il redirige vers la page 2.
3. E-mail automatique (règle d'automatisation) : il envoie le lien du guide (`LIEN_DRIVE_PDF`).
4. Le bloc Code HTML **n'apparaît pas dans l'aperçu** de l'éditeur : vérifiez le rendu sur la page publiée.

## À remplacer (recherchez chaque code du tableau avec Ctrl+F ; les repères `A_REMPLACER` signalent les principaux)

| Code | À mettre à la place |
|---|---|
| `LIEN_DRIVE_PDF` | Lien de partage Google Drive du guide (accès « Tous les utilisateurs disposant du lien ») |
| `LIEN_PAGE_3` | URL de la page 3 (vente) |
| `LIEN_COMMANDE` | URL de la page de commande systeme.io |
| `XX,XX €` | Prix. Un prix barré doit être le prix le plus bas des 30 derniers jours (art. L112-1-1 Code de la consommation), sinon supprimez-le |
| `CONTACT_EMAIL`, `EXPEDITEUR_EMAIL` | E-mail de contact, adresse d'expédition des e-mails |
| `LIEN_FACEBOOK`, `LIEN_INSTAGRAM`, `LIEN_LINKEDIN` | Réseaux sociaux (supprimez la ligne si inutile) |
| `LIEN_MENTIONS_LEGALES`, `LIEN_CONFIDENTIALITE`, `LIEN_CGV` | Pages légales |
| `IMG_FAMILLE` | URL de la photo de mise en situation (médiathèque systeme.io → copier le lien) |

## Design system (commun aux 4 blocs)

- Tout le style est préfixé par `.bcf` : il ne déborde ni sur l'éditeur ni sur le thème.
- Variables CSS sur `.bcf` : `--or #F26B1D`, `--noir #111111`, `--cream`, `--gris`, `--line`, etc.
- Logo BioConnect en **SVG base64** (léger, environ 1 Ko). Il ne demande aucun téléversement.
- Photos produits et couverture du guide **intégrées en base64** (WebP compressé, de 5 à 26 Ko chacune, sources dans `img/`). Chaque photo n'est déclarée qu'une fois par bloc, sous forme de classe CSS `.pic-…`, même si elle apparaît plusieurs fois. Poids des blocs : capture A environ 48 Ko, merci environ 39 Ko, vente environ 86 Ko.
- Pour changer une photo : remplacez le fichier dans `img/` (même nom), puis relancez `python3 build_funnel.py`.
- Responsive : **container queries à 700 px** sur `.bcf`. La mise en page s'adapte à la largeur du bloc, pas seulement à celle de l'écran.
- Compatibilité systeme.io : aucune balise `<!DOCTYPE>`, `<html>`, `<head>` ou `<body>`, polices chargées par `@import`, z-index ≤ 19.
- Barre « Commander » fixe sur mobile (page 3) : elle est placée **hors** de `.bcf`, parce que `container-type` empêcherait `position:fixed` de fonctionner.

## Modifier

Les blocs sont générés par `build_funnel.py`. Modifiez ce script, puis lancez `python3 build_funnel.py` : les 4 fichiers sont régénérés, et des aperçus sont créés dans `_apercu/` (non versionné).
