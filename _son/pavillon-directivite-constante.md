---
title: "Pavillon à directivité constante 80° × 40°"
card_title: Un pavillon à directivité constante
headline: "Un pavillon 80°&nbsp;×&nbsp;40° imprimé en 3D"
description: >-
  Remplacer JBL 2482 et tweeters par un moteur B&C DE750 sur un pavillon
  80° × 40° coupé vers 1 kHz : calculs, simulation BEM, puissance, STL à imprimer.
lede: >-
  Pour les têtes de ma sono, je remplace le JBL 2482 et les deux tweeters par
  un seul moteur à compression, chargé par un pavillon que j'ai calculé,
  simulé et dessiné pour l'impression 3D. Voici le besoin, les calculs, le
  moteur à acheter et les fichiers à imprimer.
kicker: DIY · Acoustique · Impression 3D
card_kicker: DIY
status: En cours
date: 2026-11-17
order: 3
hero_visual: image
hero_image:
  src: /assets/img/pavillon/rendu-3-4.webp
  w: 1600
  h: 1100
  alt: "Rendu 3D du pavillon assemblé, vu de trois quarts face : une bouche en losange arrondi de 41 cm de large dans une bride rectangulaire percée de douze trous, la gorge de 2 pouces au fond"
  caption: Le pavillon assemblé, rendu du modèle à imprimer
header_cta: { label: Fichiers STL, url: "#fichiers" }
ctas:
  - { label: Fichiers STL, url: "#fichiers", icon: download }
  - { label: Le moteur, url: "#moteur", style: btn-ghost }
facts:
  - { label: Statut, value: "Conçu et simulé, prototype à imprimer" }
  - { label: Couverture simulée, value: "≈ 70° (H) de 1 à 6 kHz · ≈ 45° (V) dès 3 kHz" }
  - { label: Coupure, value: "800 Hz – 1,2 kHz au DSP 206, 1,2 kHz conseillé", url: "#coupure" }
  - { label: Moteur, value: "B&C DE750TN-8, gorge 2″", url: "#moteur" }
  - { label: Bouche, value: "410 × 237 mm (bride 438 × 265 mm)" }
  - { label: Profondeur, value: "195 mm, gorge 2″ (50,8 mm)" }
  - { label: Impression, value: "4 pièces par pavillon, sans support" }
  - { label: Niveau max, value: "≈ 128 dB à 1 m par moteur (110 W)", url: "#puissance" }
  - { label: Budget, value: "≈ 520 € les deux moteurs" }
shots:
  keele:
    src: /assets/img/pavillon/keele.webp
    kind: figure
    w: 1600
    h: 920
    alt: "Graphique de la règle de Keele : dimension de bouche nécessaire en fonction de la fréquence, pour 80° et pour 40°. À 800 Hz, il faut 40 cm de large et 79 cm de haut ; la bouche retenue, 41 cm de large et 24 cm de haut, tient 80° dès 0,8 kHz et 40° dès 2,7 kHz"
    caption: "Règle de Keele : à gauche de chaque courbe, la bouche est trop petite pour tenir l'angle"
  profils:
    src: /assets/img/pavillon/profils.webp
    kind: figure
    w: 1600
    h: 920
    alt: "Profils de paroi du pavillon retenu et du guide d'onde OS pur, en horizontal et en vertical : le retenu s'ouvre plus en horizontal et se recourbe vers la bouche en vertical"
    caption: "Profils de paroi, de la gorge (à gauche) à la bouche (à droite), proportions respectées"
  largeur:
    src: /assets/img/pavillon/largeur.webp
    kind: figure
    w: 1600
    h: 920
    alt: "Largeur de faisceau à −6 dB en fonction de la fréquence, en horizontal et en vertical, pour le pavillon retenu et le guide d'onde OS pur. Le retenu tient environ 70° en horizontal dès 1 kHz et descend à 45° en vertical vers 3 kHz"
    caption: "Largeur de faisceau à −6 dB (simulation BEM) : traits pleins, pavillon retenu ; tirets, guide d'onde OS pur"
  polaire-h:
    src: /assets/img/pavillon/polaire-h.webp
    kind: figure
    w: 1600
    h: 880
    alt: "Carte de directivité horizontale simulée : niveau relatif à l'axe en fonction de l'angle et de la fréquence ; la courbe à −6 dB reste entre ±31° et ±38° de 1 à 6 kHz, puis se resserre à ±25° à 10 kHz"
    caption: "Directivité horizontale simulée, niveau relatif à l'axe ; trait blanc : −6 dB"
  polaire-v:
    src: /assets/img/pavillon/polaire-v.webp
    kind: figure
    w: 1600
    h: 880
    alt: "Carte de directivité verticale simulée : la courbe à −6 dB part de ±65° à 800 Hz, se resserre à ±22° vers 3 kHz et reste entre ±18° et ±26° jusqu'à 10 kHz"
    caption: "Directivité verticale simulée, niveau relatif à l'axe ; trait blanc : −6 dB"
  raccord:
    src: /assets/img/pavillon/raccord.webp
    kind: figure
    w: 1600
    h: 920
    alt: "Largeur de faisceau du pavillon simulé et des deux 12 pouces superposés, en horizontal et en vertical, de 500 Hz à 5 kHz. À 1,2 kHz, le 12 pouces rayonne 101° en horizontal pour 68° au pavillon ; en vertical, la paire de 12 pouces tient 32° quand le pavillon rayonne 98°"
    caption: "Directivité autour de la coupure : traits pleins, pavillon (BEM) ; tirets, 2 × 12″ superposés à 33 cm (modèle de pistons)"
  impedance:
    src: /assets/img/pavillon/impedance.webp
    kind: figure
    w: 1600
    h: 840
    alt: "Impédance acoustique simulée à la gorge : la résistance vaut 0,63 à 800 Hz, atteint 1 vers 1 kHz puis reste autour de 1 ; la réactance tend vers zéro au-dessus de 2 kHz"
    caption: "Impédance à la gorge, normalisée à ρc/S : la charge que voit le moteur"
  plan:
    src: /assets/img/pavillon/plan.webp
    kind: figure
    w: 1600
    h: 1230
    alt: "Plan coté du pavillon : face avant avec bride de 438 × 265 mm, bouche de 410 × 237 mm, gorge de 50,8 mm et quatre trous M6 sur un cercle de 101,6 mm ; coupes verticale et horizontale de 195 mm de profondeur"
    caption: "Plan coté (mm), en projection européenne"
  arriere:
    src: /assets/img/pavillon/rendu-arriere.webp
    kind: figure
    w: 1600
    h: 1100
    alt: "Rendu du pavillon vu de l'arrière : bride ronde du moteur avec quatre trous, nervures d'assemblage le long des jonctions, bride rectangulaire de la bouche"
    caption: Côté moteur, bride de gorge et nervures
  eclate:
    src: /assets/img/pavillon/eclate.webp
    kind: figure
    w: 1600
    h: 1100
    alt: "Vue éclatée des quatre quarts du pavillon : deux quarts A en ambre en diagonale, deux quarts B en gris"
    caption: "Les quatre quarts : A en ambre, B en gris"
  impression:
    src: /assets/img/pavillon/impression.webp
    kind: figure
    w: 1600
    h: 1100
    alt: "Un quart A posé sur un plateau d'imprimante, bride de la bouche à plat, gorge en haut"
    caption: Un quart dans le sens d'impression, bouche sur le plateau
install:
  - { id: stl, name: STL, primary: true, formats: "ZIP · 4,5 Mo · quarts A et B", url: /assets/files/pavillon/pavillon-80x40-stl.zip, note: "Deux fichiers, à imprimer chacun deux fois par pavillon, déjà orientés" }
  - { id: gabarit, name: Gabarit, formats: "SVG · échelle 1:1", url: /assets/files/pavillon/gabarit-baffle.svg, note: "Découpe du baffle et position des 12 vis, avec règle de contrôle" }
related:
  - /son/sound-system/
  - /son/meredsp206/
schema:
  "@type": CreativeWork
  genre: Projet DIY
  about: Pavillon acoustique à directivité constante pour moteur à compression 2 pouces
  keywords: "pavillon, guide d'onde, directivité constante, moteur à compression, B&C DE750, BEM, impression 3D"
---

## Le besoin {#besoin}

Aujourd'hui, le haut du spectre de chaque stack de mon
[sound system](/son/sound-system/) passe par deux caisses : une chambre de
compression JBL 2482 de 2 pouces sur un pavillon large pour le haut-médium, et
deux tweeters Celestion HF50 pour l'aigu. Un filtre passif les sépare, derrière
un seul canal d'Ecler APA1000.

Je veux remplacer ces trois haut-parleurs par **un seul moteur à compression**,
chargé par **un pavillon à directivité constante** et coupé assez bas — vers
**800 Hz** — pour prendre le relais directement des deux 12 pouces Eminence
ME-12/300 de mes futures têtes.

{% include visual-horn.html %}

Ce que j'en attends :

- **Une seule source pour tout le haut du spectre.** Au-dessus de 800 Hz, le
  son sort d'un seul point. Il n'y a plus de zone où le 2482 et les HF50 jouent
  ensemble la même fréquence, côte à côte, et s'additionnent ou s'annulent
  selon l'endroit où l'on se trouve.
- **Plus de filtre passif.** La coupure, l'alignement, l'égalisation et la
  protection passent dans le DSP 206. La tête devient bi-amplifiée : OUT 3·4
  pour les 12″, OUT 5·6 pour le moteur.
- **Une couverture maîtrisée.** 80° à l'horizontale pour couvrir la piste en
  largeur, 40° à la verticale pour viser le public sans arroser le plafond ni
  le sol devant les enceintes.
- **Du rendement, et moins de poids.** Concentrer l'énergie dans un faisceau
  plus étroit, c'est plus de niveau dans l'axe pour la même puissance (le
  calcul suit). Et la seule structure magnétique du 2482 pèse 10,5 kg d'après
  sa fiche JBL ; le moteur retenu plus bas pèse 6,1 kg en tout.

Cahier des charges
{: .table-label}

| Critère | Cible |
|---------|-------|
| Couverture horizontale | 80° |
| Couverture verticale | 40° |
| Coupure basse | 800 Hz visés, 1,2 kHz possible, filtrée par le DSP 206 |
| Haut du spectre | jusqu'à l'aigu, sans tweeter |
| Moteur | un seul, gorge 2″ |
| Fabrication | imprimable en 3D, sans support |

### Le gain dans l'axe {#gain}

Un pavillon ne crée pas d'énergie : il la répartit. Le facteur de directivité
Q dit combien de fois plus d'énergie part dans l'axe que si la même puissance
rayonnait dans toutes les directions. Pour un pavillon de couverture
H × V, la formule de Molloy en donne une bonne estimation :

`Q = 180 / arcsin( sin(H/2) × sin(V/2) )`

Directivité selon la couverture
{: .table-label}

| Couverture | Q | Indice de directivité |
|------------|---|-----------------------|
| 90° × 90° | 6,0 | 7,8 dB |
| 80° × 40° | 14,2 | 11,5 dB |

Passer de 90° × 90° à 80° × 40° fait gagner environ **3,7 dB dans l'axe** à
puissance égale, autant que si l'on multipliait la puissance de l'ampli par
2,3. Ce gain-là ne chauffe pas le moteur.

## La règle de Keele {#keele}

Pour garder un angle de couverture jusqu'à une fréquence donnée, la bouche du
pavillon doit être assez grande dans le plan considéré. En dessous, le pavillon
ne tient plus son angle : le faisceau s'élargit. La règle empirique de Don
Keele donne la dimension minimale :

`dimension de la bouche (m) ≈ 25 400 / (angle (°) × fréquence (Hz))`

Appliquée au cahier des charges :

| Coupure | Largeur (80°) | Hauteur (40°) |
|---------|---------------|---------------|
| 800 Hz | ≈ 0,40 m | ≈ 0,79 m |
| 1 kHz | ≈ 0,32 m | ≈ 0,64 m |
| 1,2 kHz | ≈ 0,26 m | ≈ 0,53 m |

{% include shots.html names="keele" %}

La largeur tombe bien : **40 cm**, c'est à peu près la largeur d'un caisson de 12 pouces, et
quatre quarts d'impression d'une vingtaine de centimètres.

La hauteur, elle, pose problème. Tenir 40° en vertical jusqu'à 800 Hz demande
une bouche de **79 cm de haut**, plus haute que large. Avec des parois à ±20°
partant d'une gorge de 5 cm, il faudrait près d'**un mètre de profondeur** pour
l'atteindre. C'est un pavillon de cinéma, pas une tête de sono légère.

La vraie question devient donc : dans un format compact et imprimable, jusqu'où
le pavillon tient-il ses 40° en vertical ? C'est le travail de la simulation.

## Le moteur : B&C DE750TN {#moteur}

Un seul moteur doit couvrir de 800 Hz jusqu'à l'aigu, puisqu'il remplace aussi
les tweeters. Mes critères :

- une **coupure conseillée par le fabricant à 800 Hz ou moins** : en dessous de
  sa zone de travail, la membrane se déplace trop et le moteur souffre ;
- une **gorge de 2 pouces** (50 mm) : c'est la plus grande, celle qui charge
  le mieux le bas de la bande, et le pavillon est dessiné pour elle ;
- une bande qui monte vers **18 kHz** ;
- un prix raisonnable, puisqu'il en faut deux.

Moteurs comparés
{: .table-label}

| Moteur | Gorge | Coupure conseillée | Sensibilité (1 W, 1 m) | Puissance | Prix relevé |
|--------|-------|--------------------|------------------------|-----------|-------------|
| **B&C DE750TN-8** | 2″ | 800 Hz | 107,5 dB | 110 W nominal, 220 W continus | ≈ 260 € |
| B&C DE950TN-8 | 2″ | 800 Hz | 108,5 dB | 220 W | ≈ 420 €, en rupture |
| FaitalPRO HF201 | 2″ | non trouvée (bande dès 500 ou 900 Hz selon les revendeurs) | 108 dB | 100 W nominal | ≈ 315 € |
| Eminence N314T-8 | 1,4″ | 800 Hz | — | 100 W | ≈ 240 € |

Je retiens le **[B&C DE750TN-8](https://www.bcspeakers.com/en/products/hf-driver/2/8/DE750TN)** :
c'est le moins cher des 2 pouces, et B&C le donne pour une coupure
conseillée de 800 Hz, exactement ma cible. Sa bande annoncée va de 500 Hz à
18 kHz, avec une bobine de 75 mm sur une membrane en titane. Il se fixe par
quatre vis M6 à 90° sur un cercle de 102 mm (4 pouces), que le pavillon
reprend.

Fiche du B&C DE750TN-8
{: .table-label}

| Caractéristique | Valeur (B&C) |
|-----------------|--------------|
| Gorge | 50 mm (2″) |
| Impédance | 8 Ω nominal, 7,8 Ω minimum |
| Puissance | 110 W nominal, 220 W continus |
| Sensibilité | 107,5 dB (1 W, 1 m) |
| Bande | 0,5 – 18 kHz |
| Coupure conseillée | 0,8 kHz |
| Bobine | 75 mm |
| Fixation | 4 × M6 à 90° sur Ø 102 mm |
| Encombrement | Ø 180 mm, profondeur 87 mm |
| Poids | 6,1 kg |

### À acheter {#achats}

Pour les deux têtes, la liste des courses tient en une ligne :

| Pièce | Quantité | Prix unitaire | Total |
|-------|----------|---------------|-------|
| B&C DE750TN-8 (8 Ω) | 2 | ≈ 260 € | **≈ 520 €** |

Prix relevés en novembre 2026 : 259 € chez
[Thomann](https://www.thomann.fr/bc_de750.htm) (B-Stock à partir de 206 €),
261 € chez [SonoVente](https://www.sonovente.com/b-and-c-de-750-tn-p8916.html).
Ils bougent : à vérifier avant de commander. Le reste — filament, visserie,
joint — est du consommable courant, détaillé dans la
[partie fabrication](#fabrication).

## Le profil : un guide d'onde OS-SE {#profil}

Un pavillon exponentiel charge bien le moteur, mais il se resserre dans
l'aigu. Les pavillons à directivité constante classiques tiennent leur angle,
au prix d'arêtes et de fentes qui diffractent. J'ai choisi un **guide d'onde à
sphéroïde aplati** (OS, *oblate spheroid*), le profil popularisé par Earl
Geddes : il part de la gorge dans l'axe du moteur, sans cassure, puis s'ouvre
progressivement vers un angle constant. Le front d'onde reste propre jusqu'à
la bouche.

À la bouche, une **terminaison en super-ellipse** (SE) recourbe la paroi vers
le baffle, comme le font les outils de conception de guides d'onde récents :
la sortie est plus douce, et la bouche gagne de la hauteur sans allonger le
pavillon. Le rayon de la paroi, à la profondeur *z* et pour une direction
donnée autour de l'axe, vaut :

```
r(z) = √( r0² + z² · tan²α )  +  s · L · ( 1 − (1 − (q·z/L)ⁿ)^(1/n) ) / q
       └─ sphéroïde aplati ─┘    └────────── terminaison ──────────┘
```

L'angle α et la force de terminaison *s* varient autour de l'axe, entre leur
valeur horizontale et leur valeur verticale : la gorge est ronde, la bouche en
losange arrondi.

Paramètres du pavillon retenu
{: .table-label}

| Paramètre | Valeur | Rôle |
|-----------|--------|------|
| r0 | 25,4 mm | rayon de la gorge, celui du moteur 2″ |
| L | 195 mm | profondeur, de la gorge à la bouche |
| α horizontal | 45° | parois ouvertes à 90° : le faisceau sort à 63 – 76° |
| α vertical | 20° | parois à 40° |
| s horizontal · vertical | 0,1 · 0,6 | terminaison discrète en largeur, marquée en hauteur |
| n · q | 4 · 0,995 | forme et troncature de la terminaison |
| Pente maximale | 50° | limite d'impression sans support |

Deux choix méritent une explication. **Les parois horizontales sont ouvertes à
90°**, pas à 80° : un guide d'onde OS rayonne un faisceau un peu plus étroit
que ses parois, et la simulation d'un profil à 80° donnait de 56 à 79°.
**La pente des parois est plafonnée à 50°** : au-delà, l'intérieur du pavillon
ne s'imprime plus bouche vers le bas sans supports, et des supports laisseraient
des traces sur la surface qui guide le son.

{% include shots.html names="profils" %}

## La simulation {#simulation}

### La méthode {#methode}

J'ai simulé les pavillons par la **méthode des éléments de frontière** (BEM),
celle des logiciels de conception d'enceintes, avec la bibliothèque libre
bempp-cl. Le pavillon est monté dans une boîte un peu plus grande que sa
bouche ; la gorge vibre comme un piston plat, tout le reste est rigide. Le
calcul donne la pression rayonnée dans toutes les directions, de 500 Hz à
10 kHz, et l'impédance que le pavillon présente au moteur.

Avant de lui faire confiance, je l'ai vérifié sur un cas dont on connaît la
solution exacte, la sphère pulsante (erreur inférieure à 0,2 %), puis j'ai
refait un calcul avec des mailles deux fois plus fines (écart inférieur à
0,1 dB). Les scripts, les résultats bruts et la géométrie sont publiés avec
le site, dans
[`scripts/pavillon`](https://github.com/FlogFr/www-studio-xci/tree/main/scripts/pavillon).

### Trois pavillons comparés {#candidats}

Pour trouver le bon compromis, j'ai simulé plusieurs profils de même
profondeur. Trois résument ce que j'ai appris :

Candidats simulés
{: .table-label}

| Pavillon | Bouche | Ce qu'il montre |
|----------|--------|-----------------|
| OS pur, parois 80° × 40° | 339 × 154 mm | la référence, sans terminaison |
| Terminaison verticale forte | 393 × 420 mm | une bouche haute, obtenue en ouvrant les parois verticales jusqu'à 50° |
| **Retenu** | **410 × 237 mm** | parois horizontales à 90°, terminaison modérée |

Largeur de faisceau à −6 dB, simulée
{: .table-label}

| Fréquence | OS pur H · V | Terminaison forte H · V | **Retenu H · V** |
|-----------|--------------|-------------------------|------------------|
| 800 Hz | 101° · 150° | 91° · 86° | **89° · 130°** |
| 1 kHz | 79° · 139° | 76° · 71° | **74° · 108°** |
| 2 kHz | 72° · 86° | 48° · 79° | **69° · 73°** |
| 3,15 kHz | 56° · 48° | 79° · 95° | **63° · 45°** |
| 4 kHz | 58° · 41° | 88° · 96° | **70° · 44°** |

{% include shots.html names="largeur" %}

Ce que disent ces chiffres :

- **La règle de Keele se vérifie.** Le guide d'onde OS pur, haut de 154 mm,
  devrait tenir 40° à partir de 4,1 kHz d'après Keele : la simulation donne 41°
  à 4 kHz. En horizontal, ses 339 mm promettent 80° dès 940 Hz : la simulation
  donne 79° à 1 kHz.
- **Une bouche haute ne suffit pas.** La terminaison forte agrandit la bouche à
  42 cm de haut et tient mieux la verticale vers 1 kHz, mais ses parois
  verticales, ouvertes à 50° dès 8 cm de la gorge, élargissent tout le
  haut du spectre : 96° à 4 kHz, avec un creux dans l'axe. Pour un faisceau de
  40°, les parois doivent rester à ±20° presque jusqu'à la bouche.
- **Le retenu est le meilleur compromis dans ce format.** Il gagne 10 à 30° en
  vertical entre 800 Hz et 1,6 kHz par rapport à l'OS pur, sans rien perdre dans
  l'aigu, et son horizontal reste entre 63 et 76° de 1 à 5 kHz.

### Le pavillon retenu, plan par plan {#directivite}

Les cartes ci-dessous se lisent comme une vue de dessus du faisceau : en
abscisse la fréquence, en ordonnée l'angle, et la couleur donne le niveau par
rapport à l'axe. Le trait blanc suit le contour à −6 dB, les tirets bleus la
cible.

{% include shots.html names="polaire-h" %}

{% include shots.html names="polaire-v" %}

Largeur de faisceau et indice de directivité du pavillon retenu
{: .table-label}

| Fréquence | Horizontal (−6 dB) | Vertical (−6 dB) | Indice de directivité |
|-----------|--------------------|------------------|-----------------------|
| 630 Hz | 103° | 136° | 6,9 dB |
| 800 Hz | 89° | 130° | 7,8 dB |
| 1 kHz | 74° | 108° | 9,3 dB |
| 1,25 kHz | 68° | 96° | 10,2 dB |
| 1,6 kHz | 76° | 89° | 10,6 dB |
| 2 kHz | 69° | 73° | 11,2 dB |
| 2,5 kHz | 64° | 54° | 11,9 dB |
| 3,15 kHz | 63° | 45° | 12,5 dB |
| 4 kHz | 70° | 44° | 12,5 dB |
| 5 kHz | 73° | 52° | 12,7 dB |
| 6,3 kHz | 73° | 43° | 13,3 dB |
| 8 kHz | 62° | 36° | 14,5 dB |
| 10 kHz | 50° | 40° | 15,9 dB |

De 3 à 6 kHz, le pavillon tient à peu près son cahier des charges : 63 à 73°
en horizontal, 43 à 52° en vertical, et un indice de directivité de 12,5 à
13,3 dB, plus que les 11,5 dB promis par la formule de Molloy. Entre 800 Hz et
3 kHz, la verticale s'ouvre : c'est la règle de Keele, et le prix d'une bouche
de 24 cm de haut.

Au-delà de 6 kHz, c'est l'horizontal qui se resserre : 62° à 8 kHz, 50° à
10 kHz. La gorge de 5 cm devient grande devant la longueur d'onde (3,4 cm à
10 kHz) et le faisceau se concentre dans l'axe. L'égalisation rétablit
l'équilibre dans l'axe ; sur les côtés de la piste, l'extrême aigu sera un peu
plus discret.

### La charge du moteur {#charge}

L'impédance à la gorge dit si le pavillon « tient » la membrane du moteur. Une
résistance proche de 1 signifie que le moteur transmet efficacement son énergie
à l'air ; une résistance faible, qu'il pousse dans le vide et que sa membrane
se déplace davantage pour le même niveau.

{% include shots.html names="impedance" %}

Au-dessus de 1 kHz, la résistance oscille autour de 1 : la charge est bonne. À
800 Hz, elle tombe à 0,63, et la réactance (la part de l'air qui ne fait que
faire ressort) domine. Le pavillon arrive là au bas de sa bande : 800 Hz est la
coupure la plus basse raisonnable, filtrée raide, et il ne faut pas descendre
plus bas. C'est aussi le mieux chargé des trois candidats à 800 Hz.

### Ce que la simulation ne dit pas {#limites}

- Le moteur est remplacé par un piston plat : son propre comportement, ses
  résonances et sa chambre de compression ne sont pas modélisés. Les niveaux
  sont relatifs à l'axe.
- La boîte autour du pavillon n'est pas la future caisse : sous 1 kHz, la
  vraie caisse, avec les deux 12″ en dessous, changera la verticale.
- Au-delà de 5 kHz, la boîte est maillée plus grossièrement que le pavillon,
  pour garder des calculs raisonnables : les points à 6,3, 8 et 10 kHz sont
  moins précis, surtout hors axe.
- Les marches d'impression, les jonctions et la rigidité des parois ne sont
  pas simulées.

Tout cela se vérifiera à la mesure, sur le prototype.

## Le pavillon retenu {#pavillon}

{% include shots.html names="plan" %}

En chiffres
{: .table-label}

| Caractéristique | Valeur |
|-----------------|--------|
| Bouche | 410 × 237 mm |
| Bride de la bouche | 438 × 265 mm, 8 mm d'épaisseur, 12 trous Ø 4,6 |
| Profondeur | 195 mm, bride du moteur comprise |
| Gorge | Ø 50,8 mm, bride ronde Ø 136 mm, 4 trous M6 à 45° sur Ø 101,6 mm |
| Paroi | 4 mm, 7 mm à la gorge |
| Volume imprimé | 1 706 cm³ par pavillon, quatre quarts de 427 cm³ |
| Masse | au plus ~2,2 kg de PETG par pavillon, moins avec un remplissage partiel |

{% include shots.html names="arriere" %}

**70° plutôt que 80° en horizontal.** À −6 dB, le faisceau horizontal simulé
tourne autour de 70°, un peu plus étroit que la cible. Pour viser 80° pile, il
faudrait ouvrir encore les parois horizontales ; la bouche dépasserait alors
42 cm, et les quarts ne tiendraient plus sur un plateau de 22 cm. J'ai préféré
un pavillon imprimable partout, et le vérifier à la mesure.

**Le compromis vertical, assumé.** La tête complète ne s'arrête pas au
pavillon : sous la coupure, ce sont les deux 12″ qui jouent. Superposés à
33 cm d'entraxe, deux haut-parleurs forment une petite colonne qui se resserre
en vertical : un calcul simple à deux sources donne environ 50° à 800 Hz et
40° à 1 kHz. En dessous de la coupure, la verticale est donc tenue par les
12″ ; au-dessus de 3 kHz, par le pavillon. Entre les deux, la tête rayonne plus
large en hauteur, comme la plupart des enceintes deux voies compactes.

## 800 Hz ou 1,2 kHz ? {#coupure}

Couper plus haut ne demande ni un autre moteur ni un autre pavillon : c'est un
réglage du DSP. La question est de savoir où le passage entre les 12″ et le
pavillon se fait le mieux.

### Une coupure plus haute ne donne pas 40° plus bas {#quarante}

La règle de Keele ne bouge pas : pour tenir 40° jusqu'à 1,2 kHz, il faudrait
encore une bouche de 53 cm de haut, plus du double de la nôtre. À 1,2 kHz, le
pavillon simulé rayonne 68° × 98°. Il tient ses 40° à partir de 3 kHz, quelle
que soit la coupure.

Ce qui change, c'est qui joue entre 800 Hz et 1,2 kHz : le pavillon, ou les
deux 12″. Et les deux 12″ superposés ont leur propre directivité.

{% include shots.html names="raccord" %}

Directivité à la coupure
{: .table-label}

| Coupure | Pavillon H · V (BEM) | 2 × 12″ superposés H · V (modèle) |
|---------|----------------------|-----------------------------------|
| 800 Hz | 89° · 129° | plus de 180° · 49° |
| 1,2 kHz | 68° · 98° | 101° · 32° |

- **En horizontal, le raccord est bien meilleur à 1,2 kHz.** Un 12″ s'y est
  déjà resserré à une centaine de degrés, proche des 68° du pavillon. À
  800 Hz, il rayonne encore sur tout le demi-espace devant lui, pour 89° côté
  pavillon : sur les côtés de la piste, le médium change de couleur au
  passage d'une voie à l'autre.
- **En vertical, les 12″ tiennent la verticale plus longtemps.** Superposés,
  ils forment une petite colonne qui donne 49° à 800 Hz, 39° à 1 kHz et 32° à
  1,2 kHz. Couper à 1,2 kHz laisse cette colonne travailler une demi-octave de
  plus : la zone où la tête rayonne large en hauteur se réduit à
  1,2 – 3 kHz, au lieu de 0,8 – 3 kHz.
- **Le passage reste brusque en vertical** dans les deux cas : de 30 à 50° côté
  12″ à 100° et plus côté pavillon. C'est le compromis d'une tête deux voies
  compacte ; le garder court, c'est aussi coller le pavillon au 12″ du haut.

Le modèle des 12″ est simple — deux pistons de 26 cm dans un baffle infini, à
33 cm d'entraxe — mais il suffit pour comparer les tendances. Les vraies
valeurs viendront de la mesure de la tête.

### Le moteur respire {#marge}

Le DE750TN est donné pour 800 Hz : il tient les deux coupures. Mais à 800 Hz,
pour le même niveau, sa membrane bouge **environ deux fois plus** qu'à
1,2 kHz : une fois et demie parce que la fréquence est plus basse (le
déplacement varie comme 1/f), et encore 1,4 fois parce que le pavillon la
charge moins bien (résistance de 0,64 au lieu de 1,19, et la vitesse varie
comme 1/√R). Couper à 1,2 kHz, c'est 6 dB de marge sur le déplacement de la
membrane, et le gros de l'énergie des voix laissé aux 12″.

### Et le prix ? {#prix}

Un moteur fait pour une coupure plus haute peut être plus petit et moins cher,
mais il faut alors redessiner le pavillon pour sa gorge.

Moteurs selon la coupure
{: .table-label}

| Coupure | Moteur | Gorge | Sensibilité | Puissance | Prix relevé |
|---------|--------|-------|-------------|-----------|-------------|
| 800 Hz | **B&C DE750TN-8** (retenu) | 2″ | 107,5 dB | 110 W | ≈ 260 € |
| 1,2 kHz | B&C DE780TN-16 | 1,4″ | 109 dB | 110 W (fiche 8 Ω) | ≈ 230 – 240 € |
| 1,6 kHz | B&C DE250-8 | 1″ | 108,5 dB | 60 W | ≈ 92 – 99 € |

Le DE780TN, donné pour 1,2 kHz minimum, n'économise que 20 à 30 € par
moteur, au prix d'un nouveau pavillon. La vraie économie, c'est un moteur
1 pouce comme le DE250 : près de trois fois moins cher, mais coupé à 1,6 kHz, avec
presque deux fois moins de puissance, et des 12″ qui devraient monter
proprement jusqu'à 3 kHz. Pour un système qui doit envoyer, ce n'est pas le
bon calcul.

Prix relevés en novembre 2026 : DE780TN 16 Ω à 192,44 € HT chez
[Thomann](https://www.thomann.co.uk/bc_de780tn_16_ohms.htm) et 238 € TTC chez
[SonoVente](https://www.sonovente.com/b-and-c-de-780-tn-16-ohms-p92174.html) ;
DE250 à 92 € chez [Thomann](https://www.thomann.de/be/bc_de_250.htm) et
99 € chez Muziker. Ils bougent : à vérifier avant de commander.

### Ce que je retiens {#choix-coupure}

Je garde le DE750TN et ce pavillon, et je pars d'une **coupure à 1,2 kHz**
(Linkwitz-Riley 24 dB/octave). Je redescendrai vers 1 kHz ou 800 Hz si les 12″
ne restent pas propres jusqu'à 2,4 kHz, ou si le raccord mesuré est meilleur
plus bas. Rien à racheter : tout se règle dans
[MereDSP206](/son/meredsp206/).

## Avec les deux 12″ {#douze-pouces}

Le but de tout ce projet : remplacer l'empilement du haut de la sono — 2482,
tweeters, filtre passif — par une seule voie plus simple, sans perdre en
qualité ni en niveau. Il faut donc que le moteur et les 12″ arrivent au même
niveau maximal : sinon, c'est la voie la plus faible qui fixe la limite.

### Sensibilité et puissance {#puissance}

La sensibilité est le niveau mesuré à 1 m pour 1 W. Doubler la puissance
ajoute 3 dB ; deux haut-parleurs identiques qui jouent ensemble ajoutent 6 dB
à puissance égale par haut-parleur. D'où des niveaux maximaux, à 1 m dans
l'axe, en ordre de grandeur :

Niveau maximal par tête
{: .table-label}

| Voie | Sensibilité (1 W, 1 m) | Puissance | Niveau max à 1 m |
|------|------------------------|-----------|------------------|
| Moteur B&C DE750TN | 107,5 dB | 110 W nominal (220 W en programme) | ≈ 128 dB (≈ 131 dB) |
| 2 × Eminence ME-12/300 actuels | non trouvée | 2 × 300 W | sensibilité + 31 dB |
| 2 × B&C 12NDL76 | 100 dB | 2 × 400 W | ≈ 132 dB |
| 2 × FaitalPRO 12PR320 | 97 dB | 2 × 300 W | ≈ 128 dB |

Le moteur plafonne vers **128 dB à 1 m**. Pour le suivre, la paire de 12″ doit
avoir une sensibilité d'au moins 97 dB avec 2 × 300 W. À 10 m, en champ libre,
il faut retirer 20 dB : environ 108 dB par tête, avant de compter la
deuxième tête et le sol.

Deux réserves. La sensibilité du moteur est celle de la fiche B&C, mesurée sur
son propre pavillon : sur celui-ci, elle sera à mesurer, à quelques décibels
près. Et la remontée d'aigu propre aux pavillons à directivité constante mange
une partie de la marge au-dessus de 5 kHz, là où la musique a peu d'énergie.

À tension égale, le moteur (107,5 dB à 2,83 V sous 8 Ω) est un peu plus
sensible que la paire de 12″ (sensibilité d'un 12″ + 6 dB à 2,83 V sous 4 Ω,
soit 103 à 106 dB) : sa sortie sera atténuée de quelques décibels dans le DSP,
ce qui lui laisse de la réserve. L'Ecler APA1000 doit fournir 110 W sous 8 Ω
sur une voie et 600 W sous 4 Ω sur l'autre : c'est à vérifier sur sa fiche.

### Ce qu'il faut aux 12″ {#compatibilite}

| Critère | Coupure à 800 Hz | Coupure à 1,2 kHz |
|---------|------------------|-------------------|
| Réponse propre jusqu'à | ~1,6 kHz | ~2,4 kHz |
| Sensibilité | 97 dB ou plus | 97 dB ou plus |
| Puissance | 2 × 300 W ou plus | 2 × 300 W ou plus |
| Montage | superposés, pavillon au-dessus, au plus près | idem |

Une octave au-dessus de la coupure, le filtre Linkwitz-Riley n'a retiré que
24 dB : ce que le 12″ fait là s'entend encore, d'où la colonne « réponse propre
jusqu'à ».

Je n'ai pas trouvé de fiche publique des Eminence ME-12/300 : leur
sensibilité et leur limite haute sont à mesurer, ou à retrouver sur leur
étiquette. S'ils atteignent 97 dB et montent proprement à 2,4 kHz, ils
restent. Sinon, deux 12″ du commerce collent à ce cahier des charges :

12″ compatibles
{: .table-label}

| 12″ | Sensibilité | Bande | Puissance | Prix relevé | Coupure possible |
|-----|-------------|-------|-----------|-------------|------------------|
| B&C 12NDL76-8 | 100 dB | 50 Hz – 2 kHz | 400 W (800 W en programme) | ≈ 199 € | 800 Hz – 1 kHz |
| FaitalPRO 12PR320-8 | 97 dB | 45 Hz – 5 kHz | 300 W | ≈ 193 – 235 € | jusqu'à 1,2 kHz |

Le B&C est le plus sensible, mais sa bande annoncée s'arrête à 2 kHz : il va
avec une coupure vers 1 kHz. Le Faital monte plus haut et accepte 1,2 kHz,
pour 3 dB de sensibilité en moins. Prix relevés en novembre 2026 : 199 € chez
[Thomann](https://www.thomann.de/gb/bc_12_ndl_76.htm) pour le 12NDL76 ;
193 € en promotion et 229 € au prix normal chez
[Masori](https://masori.de/en/products/12pr320), 234,95 € chez Soundimports
pour le 12PR320. À vérifier avant de commander.

## Imprimer et assembler {#fabrication}

Le pavillon est coupé en quatre quarts, le long de ses deux plans de symétrie.
Il n'y a que **deux fichiers** : le quart A et son symétrique, le quart B. Un
quart A tourné d'un demi-tour devient le quart en bas à gauche ; il faut donc
imprimer **deux A et deux B par pavillon**.

{% include shots.html names="eclate" %}

### Les fichiers {#fichiers}

{% include install.html platforms=page.install %}

### Les réglages d'impression {#impression}

Chaque quart s'imprime **bouche vers le bas**, la bride à plat sur le plateau,
**sans aucun support** : l'intérieur du pavillon ne penche jamais plus de 50°,
tout l'extérieur regarde vers le haut, et la bride du moteur repose sur un
collier à 45°. Seuls le plafond des quatre encoches et le haut des trous de
boulons se font en pont.

{% include shots.html names="impression" %}

Réglages conseillés
{: .table-label}

| Réglage | Valeur |
|---------|--------|
| Plateau minimum | 220 × 135 mm, 195 mm de haut |
| Matière | PETG (tient jusqu'à ~70 °C) ; PLA pour un prototype d'intérieur |
| Buse · couches | 0,4 ou 0,6 mm · 0,2 à 0,28 mm |
| Parois | 4 périmètres minimum : la paroi de 4 mm sort pleine |
| Remplissage | 30 % gyroïde (colliers, brides, nervures) |
| Supports | aucun |
| Matière par quart | 427 cm³, au plus ~540 g de PETG |

Les marches laissées par les couches, quelques dixièmes de millimètre, sont
sans effet acoustique : la plus courte longueur d'onde jouée, à 18 kHz, fait
19 mm. Un ponçage léger de l'intérieur suffit, surtout aux jonctions.

### La visserie {#visserie}

Par pavillon
{: .table-label}

| Pièce | Quantité | Rôle |
|-------|----------|------|
| Vis M4 × 20, écrou, 2 rondelles | 12 | assembler les quarts par les nervures |
| Vis M6, rondelle | 4 | fixer le moteur (longueur : 12 mm de bride + 8 à 10 mm de filet dans le moteur) |
| Vis à bois Ø 4 × 25 | 12 | fixer la bride derrière le baffle |
| Colle époxy ou polyuréthane | — | coller les jonctions |
| Joint fin (1 mm) ou cordon de silicone | — | étancher moteur et pavillon |

### L'assemblage {#assemblage}

1. Ébavurer les quarts et poncer légèrement les faces de jonction. Assembler
   une première fois à blanc avec les vis M4 pour vérifier l'alignement,
   surtout à la gorge.
2. Coller les quarts deux par deux (haut et bas), visser, puis réunir les
   deux moitiés. Essuyer la colle qui déborde à l'intérieur : la paroi doit
   rester lisse, sans marche, en particulier dans les premiers centimètres.
3. Poser le joint, présenter le moteur et le fixer par ses quatre vis M6,
   accessibles par les encoches du collier. Serrer en croix, sans forcer :
   c'est du plastique.
4. Découper le baffle de la caisse au contour exact de la bouche — le gabarit
   SVG s'imprime à l'échelle 1:1, avec une règle de 100 mm pour le contrôler —
   puis visser la bride par l'arrière, bouche affleurante.
5. **Soutenir le moteur.** Il pèse 6,1 kg : il ne doit pas pendre au bout de
   la gorge imprimée. Une cale ou une sangle vers une traverse de la caisse
   reprend son poids, surtout pendant le transport.
{: .numbered}

## Le réglage dans le DSP 206 {#reglage}

Le moteur se branche sur les sorties OUT 5·6 du DSP 206, à travers l'Ecler
APA1000 qui alimentait jusqu'ici le filtre passif. Tout se règle depuis
[MereDSP206](/son/meredsp206/). Les valeurs ci-dessous sont des points de
départ ; les vraies se trouvent à la mesure.

Réglages de départ
{: .table-label}

| Réglage | OUT 3·4 (2 × 12″) | OUT 5·6 (moteur) |
|---------|-------------------|------------------|
| Filtre | passe-bas Linkwitz-Riley 24 dB/oct, 1,2 kHz (800 Hz à 1,2 kHz selon les 12″) | passe-haut Linkwitz-Riley 24 dB/oct, même fréquence |
| Délai | à régler : la membrane du moteur est à plus de 20 cm derrière le baffle | 0 |
| Niveau | référence | atténué de quelques dB : le moteur est plus sensible que les 12″ ([détail](#puissance)) |
| Égalisation | selon mesure | remontée progressive de l'aigu, typique d'un pavillon à directivité constante |
| Limiteur | selon les 12″ | seuil vers 30 V efficaces en sortie d'ampli (110 W sous 8 Ω) |

Deux précautions. Le passe-haut doit être en place **avant** de brancher le
moteur : une seule note grave à pleine puissance suffit à le détruire. Et le
filtre de 24 dB/octave n'est pas un luxe : B&C conseille de couper à 800 Hz,
c'est un minimum, et une pente raide garde le moteur à l'abri de ce qui se
passe en dessous, là où le pavillon le charge mal.

Le seuil du limiteur se déduit de la puissance nominale : 110 W sous 8 Ω, c'est
√(110 × 8) ≈ 30 V efficaces aux bornes du moteur. Il reste à mesurer quel
niveau de sortie du DSP donne 30 V à la sortie de l'ampli, avec son gain réglé.

## La suite {#la-suite}

1. Imprimer un premier pavillon et vérifier l'ajustement du moteur.
2. Mesurer ses polaires horizontales et verticales (micro de mesure et REW), et
   les comparer à la simulation.
3. Mesurer les 12″ jusqu'à 2,4 kHz, choisir la coupure entre 800 Hz et 1,2 kHz,
   régler l'alignement à la mesure, puis dessiner la caisse de la tête autour.
4. Si la verticale doit être tenue plus bas, étudier une version plus profonde
   à fente de diffraction, imprimée en plus de morceaux.
{: .numbered}

Chaque étape aura sa mise à jour ici, avec les courbes mesurées.
