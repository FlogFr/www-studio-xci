---
title: "Pavillon à directivité constante 80° × 40°"
card_title: Un pavillon à directivité constante
headline: Un pavillon à directivité constante
description: >-
  Concevoir un pavillon à directivité constante 80° × 40° coupé à 800 Hz ou
  1 kHz pour des têtes 2 × 12″ : cahier des charges, règle de Keele et choix.
lede: >-
  Pour les futures têtes de ma sono, je dessine mon propre pavillon : 80° à
  l'horizontale, 40° à la verticale, et une coupure à 800 Hz ou 1 kHz.
kicker: DIY · Acoustique
card_kicker: DIY
status: En cours
date: 2026-11-17
order: 3
hero_visual: horn
facts:
  - { label: Statut, value: En cours }
  - { label: Couverture visée, value: 80° (H) × 40° (V) }
  - { label: Coupure, value: 800 Hz ou 1 kHz }
  - { label: Pour, value: "Têtes 2 × 12″ bi-amplifiées" }
related:
  - /son/sound-system/
  - /son/meredsp206/
schema:
  "@type": CreativeWork
  genre: Projet DIY
  about: Pavillon acoustique à directivité constante
---

## Le cahier des charges {#cahier-des-charges}

Le projet est né de l'évolution de mon [sound system](/son/sound-system/) : je
veux des têtes plus légères, avec deux 12 pouces Eminence ME-12/300 en
bas-médium et un moteur à compression pour le haut. Ce moteur a besoin d'un
pavillon, et je veux le dessiner moi-même.

| Critère | Cible |
|---------|-------|
| Directivité horizontale | 80° |
| Directivité verticale | 40° |
| Fréquence de coupure | 800 Hz ou 1 kHz |
| Grave associé | 2 × Eminence ME-12/300 |

## Pourquoi la directivité constante {#pourquoi}

Un pavillon exponentiel classique se resserre à mesure que la fréquence monte :
large dans le bas de sa bande, il devient un faisceau dans l'aigu. Hors de
l'axe, le public n'entend donc pas le même équilibre que dans l'axe.

Un pavillon à directivité constante garde à peu près le même angle de couverture
sur toute sa bande utile. Le son est le même partout dans la zone couverte, et
l'énergie envoyée hors de cette zone — au plafond, sur les murs — reste sous
contrôle.

Les deux angles ne sont pas choisis au hasard : 80° à l'horizontale pour couvrir
la piste en largeur, 40° à la verticale pour viser le public sans arroser le
plafond ni le sol devant les enceintes.

## La règle de Keele {#keele}

Pour garder un angle de couverture jusqu'à une fréquence donnée, la bouche du
pavillon doit être assez grande dans le plan considéré. La règle empirique de
Don Keele en donne l'ordre de grandeur :

`dimension de la bouche (m) ≈ 25 400 / (angle (°) × fréquence (Hz))`

Appliquée au cahier des charges :

| Coupure | Largeur (80°) | Hauteur (40°) |
|---------|---------------|---------------|
| 800 Hz | ≈ 0,40 m | ≈ 0,79 m |
| 1 kHz | ≈ 0,32 m | ≈ 0,64 m |

Deux enseignements. D'abord, c'est l'angle le plus étroit qui impose la plus
grande dimension : la bouche est plus haute que large. Ensuite, ce sont des
minimums : pour garder le contrôle un peu sous la coupure, là où le pavillon et
les 12 pouces jouent encore ensemble, il faut viser un peu plus grand.

## Les choix encore ouverts {#choix}

**800 Hz ou 1 kHz ?** Plus la coupure est basse, plus le pavillon est grand et
plus le moteur à compression travaille. Plus elle est haute, plus les 12 pouces
doivent monter, là où ils deviennent eux-mêmes directifs. La bonne réponse
dépendra du moteur choisi et des mesures.
<!-- TODO: compression driver chosen (model, throat size) -->

**La géométrie et la fabrication** restent à trancher, en fonction de ce que je
peux fabriquer proprement et reproduire à deux exemplaires.

## La suite {#la-suite}

Les prochaines étapes : choisir le moteur, simuler le pavillon, fabriquer un
prototype, puis mesurer ses polaires horizontales et verticales. Chaque étape
aura sa mise à jour ici, avec les courbes.
