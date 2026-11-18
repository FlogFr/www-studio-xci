---
title: "Le sound system : deux stacks 4 voies des années 90"
headline: "Le sound system : deux stacks 4 voies nés dans les années 90"
card_title: Le sound system
description: >-
  Deux stacks quatre voies construits à Paris dans les années 90, trois amplis
  et un t.racks DSP 206 : composition, rack, chaîne du signal et réglages.
lede: >-
  Deux stacks de quatre voies, trois amplis et un DSP 206 : voici la sono qui
  m'accompagne en soirée. Elle a été construite à Paris il y a trente ans, et je
  continue de la faire évoluer.
kicker: Matériel · Documentation
card_kicker: Matériel
date: 2026-11-17
order: 2
hero_visual: stacks
hero_layout: wide
facts_style: stats
facts:
  - { label: Stacks, value: 2 }
  - { label: Voies, value: 4 }
  - { label: Amplis, value: 3 }
  - { label: Sorties DSP, value: 6 }
rack:
  - { role: Processeur, name: t.racks DSP 206 }
  - { role: Ampli 1 · Grave, name: Crest CPX 2600 }
  - { role: Ampli 2 · Bas-méd., name: Ecler APA1000 }
  - { role: Ampli 3 · Haut, name: Ecler APA1000 }
  - { role: Secours, name: Inter-M M700, spare: true }
chain:
  source: Console
  processor: DSP 206 · 2 in / 6 out
  outputs:
    - Crest CPX 2600 → W-bin 415 × 2 / côté
    - Ecler APA1000 → 2 × ME-12/300
    - Ecler APA1000 → filtre passif → JBL 2482 + HF50
  caption: Fig. 1 — trois bandes amplifiées par côté, quatre voies acoustiques.
related:
  - /son/pavillon-directivite-constante/
  - /son/meredsp206/
---

## Une sono des années 90 {#annees-90}

Ce système n'est pas sorti d'un catalogue. D'après ce que j'en sais, il a été
construit sur mesure dans les années 90, à Paris, par une boutique qui
s'appelait Master Sound — rien à voir avec la marque anglaise de mixers
rotatifs au nom presque identique.

Tout y est pensé pour la fête : des caisses larges et lourdes, du rendement
plutôt que de la compacité, et une séparation en quatre voies qui laisse à
chaque haut-parleur la bande de fréquences qu'il sait le mieux reproduire.
<!-- TODO: how and when Florian got it — an anecdote or two -->

## Un stack, quatre voies {#quatre-voies}

Chaque côté de la sono est un empilement de cinq caisses. En bas, le grave est
confié à deux W-bin 415 : des caissons à pavillon replié en forme de W, réputés
pour leur rendement. Chacun embarque un 15 pouces RCF L15-554K.

Au-dessus, le bas-médium tient dans un caisson équipé de deux Eminence
ME-12/300 — des 12 pouces de 300 W RMS sous 8 Ω, câblés en parallèle. Le
haut-médium est assuré par une chambre de compression JBL 2482 de 2 pouces sur
un pavillon large, et l'aigu par une caisse de deux tweeters Celestion HF50.

Composition d'un stack
{: .table-label}

| Voie | Caisse | Haut-parleurs |
|------|--------|---------------|
| Grave | 2 × W-bin 415 | 1 × RCF L15-554K (15″) par caisson |
| Bas-médium | 1 caisson | 2 × Eminence ME-12/300 en parallèle |
| Haut-médium | 1 caisse à pavillon | JBL 2482 (2″), filtre passif |
| Aigu | 1 caisse | 2 × Celestion HF50 |

## Le rack 10U {#rack}

Toute l'électronique tient dans un rack de 10 unités. En tête, le t.racks
DSP 206 fait le filtrage. Derrière lui, un Crest CPX 2600 est dédié aux subs, et
deux Ecler APA1000 se partagent le bas-médium et le haut du spectre. Un Inter-M
M700 reste dans le rack en secours : en soirée, on ne choisit pas le moment où
un ampli lâche.

{% include rack.html items=page.rack %}

## La chaîne du signal {#signal}

Le DSP 206 reçoit la stéréo sur ses deux entrées et la découpe en trois bandes
par côté : grave, bas-médium et haut. Trois bandes fois deux côtés, cela fait
exactement ses six sorties. La quatrième voie, l'aigu, est séparée du
haut-médium par le filtre passif d'origine, dans la caisse.

{% include signal-chain.html chain=page.chain %}

## Le réglage {#reglage}

Passer à un filtrage numérique change tout. Le DSP règle les fréquences de
coupure et les pentes au hertz près, aligne les voies dans le temps grâce aux
délais, et protège les haut-parleurs avec des limiteurs. Surtout, un réglage qui
sonne bien se garde dans un preset et se rappelle en une seconde.

Je consigne tous mes réglages dans un fichier texte, `sonorisation.dsp206.rst`,
pour pouvoir revenir en arrière et comprendre pourquoi j'ai changé quelque chose.

Sorties du DSP
{: .table-label}

| Sortie | Bande | Amplification |
|--------|-------|---------------|
| OUT 1 · 2 | Grave | Crest CPX 2600 |
| OUT 3 · 4 | Bas-médium | Ecler APA1000 |
| OUT 5 · 6 | Haut | Ecler APA1000 |

<!-- TODO: current crossover frequencies and slopes per output -->

<aside class="callout" markdown="1">
Et pour le piloter ?
{: .callout-title}

Je voulais régler le DSP depuis mon PC Linux et depuis mon téléphone, au milieu
de la piste. C'est ce qui a donné [MereDSP206](/son/meredsp206/).
</aside>

## Ce qui va changer {#evolutions}

Le système complet est impressionnant, mais il ne passe pas partout. L'idée est
de pouvoir sortir une version allégée : uniquement des têtes et des subs.

- **Des têtes 2 × 12″ bi-amplifiées.** Je garde mes deux Eminence ME-12/300 et
  j'y ajoute un seul moteur à compression, un B&C DE750TN, sur un pavillon
  80° × 40° que j'ai calculé et dessiné pour l'impression 3D — c'est le
  [projet pavillon](/son/pavillon-directivite-constante/).
- **Moins de poids, plus de rendement.** Ce moteur remplace à la fois le JBL
  2482 et les tweeters HF50 : les 2482 et leur pavillon pourraient être
  revendus pour financer les nouvelles têtes.
- **Plus d'infra.** Remplacer les 15 pouces des W-bins pour aller chercher
  encore plus bas.

Chaque étape aura son article ici, avec les mesures avant et après.
