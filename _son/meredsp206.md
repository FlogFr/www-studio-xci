---
title: "MereDSP206 : t.racks DSP 206 sous Linux et Android"
card_title: MereDSP206
headline: Mere<span class="accent">DSP</span>206
description: >-
  MereDSP206, application native Linux et Android pour piloter le processeur
  t.racks DSP 206 de Thomann : gains, filtres, égaliseurs, délais et presets.
lede: >-
  Piloter un t.racks DSP 206 depuis un PC Linux ou un téléphone Android :
  l'histoire de l'appli, ce qu'elle fait, et comment l'installer.
kicker: Logiciel · Linux natif + Android
card_kicker: Logiciel
date: 2026-11-17
order: 1
also_in: [logiciel]
hero_visual: dsp
header_cta: { label: Télécharger, url: "#installer" }
ctas:
  - { label: Linux, url: "#linux", icon: download }
  - { label: Android, url: "#android", icon: phone, style: btn-ghost }
facts:
  - { label: Matériel, value: t.racks DSP 206 }
  - { label: Plateformes, value: Linux natif · Android }
  - { label: Accord, value: Distribution publique validée par Thomann }
# TODO: licence, source repository, version (see claude/docs/content-status.md)
features:
  - { label: Entrées · Sorties, text: "Gains, mutes et routage des 2 entrées vers les 6 sorties, avec vumètres en direct." }
  - { label: Filtrage, text: "Fréquences de coupure et pentes de chaque voie." }
  - { label: Égalisation · Délais, text: "Égaliseurs par sortie et délais pour aligner les voies." }
  - { label: Protection · Presets, text: "Limiteurs, et rappel des presets enregistrés dans le DSP." }
install:
  - { id: linux, name: Linux, primary: true }
  - { id: android, name: Android }
related:
  - /son/sound-system/
  - /son/pavillon-directivite-constante/
schema:
  "@type": SoftwareApplication
  operatingSystem: Linux, Android
  applicationCategory: MultimediaApplication
schema_name: MereDSP206
---

## Pourquoi cette appli {#pourquoi}

Le DSP 206 est le cerveau de ma sono : deux entrées, six sorties, et tout le
filtrage entre les deux. C'est un excellent processeur pour son prix. Mais pour
le régler, il faut son éditeur, et l'éditeur ne tourne pas nativement sur
Linux — le système que j'utilise tous les jours.

Il y avait un deuxième problème : on ne règle pas une sono depuis la régie. On
la règle au milieu de la piste, là où le public va l'entendre. Je voulais donc
pouvoir ajuster un gain ou un délai depuis mon téléphone, en marchant dans la
salle.

Je cherchais une solution simple et sans frais. Je ne l'ai pas trouvée, alors
je l'ai écrite.

## Ce qu'elle fait {#fonctions}

MereDSP206 donne accès aux réglages du processeur sans passer par l'éditeur
d'origine :

{% include features.html items=page.features %}

## Linux et Android {#plateformes}

Sur Linux, MereDSP206 est une vraie application native : pas d'émulation, pas de
machine virtuelle. Elle tourne sur le portable de régie à côté du reste de mes
outils.
<!-- TODO: technologies used (language, toolkit) -->

Sur Android, l'interface est pensée pour le pouce : de gros curseurs, les
réglages essentiels d'abord, et l'état du DSP toujours visible. C'est elle que
j'utilise pendant les balances.

<!-- TODO: screenshots Linux + Android (design: two captures side by side) -->

## Installer {#installer}

Choisissez votre plateforme, installez, puis branchez le DSP 206.
<!-- TODO: connection (USB / network), formats (.deb, AppImage, Flatpak, APK, F-Droid, Play Store), install commands -->

{% include install.html platforms=page.install %}

## Merci Thomann {#thomann}

Avant de publier quoi que ce soit, j'ai écrit à Thomann. Ils m'ont donné leur
accord pour partager ces applications avec le grand public — et m'ont souhaité
toute la réussite qui va avec. Merci à eux.

MereDSP206 est un projet indépendant, non affilié à Thomann. t.racks est une
marque de Thomann.
{: .note}

## La suite {#la-suite}

L'appli évolue avec ma sono. Les prochaines étapes seront annoncées ici.
<!-- TODO: upcoming features, how to report a bug (repo, e-mail) -->

Elle a été écrite pour ma sono, que je documente dans
[Le sound system](/son/sound-system/).

## In English {#english}

<div class="lang-en" lang="en" markdown="1">
**MereDSP206** is a native Linux and Android application to control the
**Thomann t.racks DSP 206** loudspeaker management processor without the
original editor: input/output gains, mutes and routing, crossover filters,
per-output EQ, delays, limiters and presets. Thomann agreed to its public
distribution. MereDSP206 is an independent project, not affiliated with Thomann.
</div>
