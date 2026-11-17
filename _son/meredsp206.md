---
title: "MereDSP206 : t.racks DSP 206 sous Linux et Android"
card_title: MereDSP206
headline: Mere<span class="accent">DSP</span>206
description: >-
  Guide de MereDSP206, l'appli Linux et Android qui pilote le t.racks DSP 206
  en USB ou en réseau : installation, console, égaliseurs, filtres, presets.
lede: >-
  Piloter un t.racks DSP 206 depuis un PC Linux ou un téléphone Android, en USB
  ou en réseau. Ce guide explique ce que fait l'appli, comment l'installer et
  comment s'en servir, écran par écran.
kicker: Logiciel · Linux natif + Android
card_kicker: Logiciel
date: 2026-11-17
version: 0.1.0
order: 1
also_in: [logiciel]
image: /assets/img/og/meredsp206.png
app_icon:
  src: /assets/img/meredsp206/icon-192.png
  alt: "Icône de MereDSP206 : une courbe d'égalisation au-dessus de six vumètres"
hero_visual: dsp
header_cta: { label: Télécharger, url: "#installer" }
ctas:
  - { label: Linux, url: "#linux", icon: download }
  - { label: Android, url: "#android", icon: phone, style: btn-ghost }
facts:
  - { label: Matériel, value: "t.racks DSP 206 (2 entrées, 6 sorties)" }
  - { label: Plateformes, value: Linux (GTK 4) · Android 8.0+ }
  - { label: Connexion, value: USB · réseau (Ethernet / Wi-Fi) }
  - { label: Version, value: "0.1.0, première version" }
  - { label: Code source, value: GitHub, url: "https://github.com/FlogFr/meredsp206" }
  - { label: Accord, value: Distribution publique validée par Thomann }
# TODO: licence (see claude/docs/content-status.md)
features:
  - { label: Console, text: "Les 8 voies d'un coup d'œil : vumètres en dBu, gain, mute, polarité et source de chaque sortie." }
  - { label: Égaliseurs, text: "Paramétrique 8 bandes sur les entrées, 9 sur les sorties, avec courbe tactile. Graphique 31 bandes sur les entrées." }
  - { label: Filtrage, text: "Passe-haut et passe-bas Butterworth, Bessel ou Linkwitz-Riley, de 6 à 48 dB/octave." }
  - { label: Dynamique, text: "Noise gate sur les entrées, compresseur RMS et limiteur crête sur les sorties." }
  - { label: Délais · Routage, text: "Jusqu'à 680 ms par voie, affichés en ms, mètres ou pieds. Chaque sortie reçoit InA, InB ou les deux." }
  - { label: Presets · Fichiers, text: "Les 20 presets du DSP, et des fichiers de programme communs à Linux et Android." }
install:
  - { id: linux, name: Linux, primary: true, formats: "Code source · Debian 13+", url: "https://github.com/FlogFr/meredsp206", note: "Appli graphique et commande dsp206" }
  - { id: android, name: Android, formats: "APK de test · Android 8.0+", url: "https://github.com/FlogFr/meredsp206/actions/workflows/android.yml", note: "Google Play : publication prévue" }
terminals:
  linux_build:
    - sudo apt install build-essential pkg-config libgtk-4-dev libadwaita-1-dev cargo rustc git
    - git clone https://github.com/FlogFr/meredsp206.git
    - cd meredsp206
    - cargo build --release
    - sudo make install PREFIX=/usr/local
  linux_udev:
    - sudo install -m 644 data/udev/70-meredsp206.rules /etc/udev/rules.d/
    - sudo udevadm control --reload && sudo udevadm trigger --subsystem-match=hidraw
  linux_launch:
    - meredsp206 --usb
    - meredsp206 --connect 192.168.1.101
    - meredsp206 --demo
  cli:
    - dsp206 discover
    - dsp206 --usb info
    - dsp206 --usb meters 10
    - dsp206 --usb dump soiree.dsp206
    - dsp206 --usb set gain out1 -3 mute out6 on
    - dsp206 --host 192.168.1.101 info
shots:
  linux-mixer:
    src: /assets/img/meredsp206/linux-mixer.webp
    kind: desktop
    w: 1600
    h: 809
    alt: "MereDSP206 sous Linux, page Mixer : les huit voies côte à côte avec vumètre vert, fader de gain, boutons mute et polarité, et choix A / B des sources sur les sorties"
    caption: Linux · page Mixer (mode démo)
  console:
    src: /assets/img/meredsp206/android-console.webp
    w: 600
    h: 1205
    alt: "MereDSP206 sous Android, écran Console : InA, InB, Out1 et Out2 avec vumètre, gain, boutons Ø et Mute, et source InA ou InB des sorties"
    caption: Android · Console
  appareil:
    src: /assets/img/meredsp206/android-appareil.webp
    w: 600
    h: 1205
    alt: "Écran Appareil sous Android : état de la connexion, identité DSP206 V0105P, recherche réseau, adresse IP 192.168.1.101 et connexion USB par câble OTG"
    caption: Android · Appareil
  canal-ina:
    src: /assets/img/meredsp206/android-canal-ina.webp
    w: 600
    h: 1205
    alt: "Écran Canal sous Android, voie InA : courbe de l'égaliseur paramétrique à 8 bandes, bande 1 sélectionnée, type Peak, fréquence 50,8 Hz, gain 0 dB"
    caption: Canal · InA, 8 bandes
  canal-out1:
    src: /assets/img/meredsp206/android-canal-out1.webp
    w: 600
    h: 1205
    alt: "Écran Canal sous Android, voie Out1 : courbe de l'égaliseur paramétrique à 9 bandes, bande 1 sélectionnée, type Peak, fréquence 40,3 Hz, gain 0 dB"
    caption: Canal · Out1, 9 bandes
  linux-canal:
    src: /assets/img/meredsp206/linux-canal.webp
    kind: desktop
    w: 1600
    h: 809
    alt: "MereDSP206 sous Linux, page Channel de Out1 : courbe d'égalisation à 9 poignées, tableau des bandes (type, fréquence, gain, Q, bypass), et à droite nom, gain, délai, liaison, crossover et routage"
    caption: Linux · page Channel, voie Out1
  presets:
    src: /assets/img/meredsp206/android-presets.webp
    w: 600
    h: 1205
    alt: "Écran Presets sous Android : programme en cours Default Preset chargé depuis F00, boutons de fichier, envoi du programme, et liste F00, U01 à U05 avec Load et Store"
    caption: Android · Presets
related:
  - /son/sound-system/
  - /son/pavillon-directivite-constante/
schema:
  "@type": SoftwareApplication
  operatingSystem: Linux, Android
  applicationCategory: MultimediaApplication
  softwareVersion: 0.1.0
  image: https://studio-xci.fr/assets/img/meredsp206/icon-512.png
  screenshot:
    - https://studio-xci.fr/assets/img/meredsp206/linux-mixer.webp
    - https://studio-xci.fr/assets/img/meredsp206/android-console.webp
schema_name: MereDSP206
---

## Pourquoi cette appli {#pourquoi}

Le DSP 206 est le cerveau de ma sono : deux entrées, six sorties, et tout le
filtrage entre les deux. C'est un excellent processeur pour son prix. Mais pour
le régler, il faut son éditeur, et l'éditeur d'origine ne tourne que sous
Windows. Moi, j'utilise Linux tous les jours.

Il y avait un deuxième problème : on ne règle pas une sono depuis la régie. On
la règle au milieu de la piste, là où le public va l'entendre. Je voulais donc
pouvoir ajuster un gain ou un délai depuis mon téléphone, en marchant dans la
salle.

Je cherchais une solution simple et sans frais. Je ne l'ai pas trouvée, alors
je l'ai écrite. MereDSP206 vise à couvrir toutes les fonctions de l'éditeur
Windows, avec une interface plus claire et plus rapide.

## Ce qu'elle fait {#fonctions}

MereDSP206 se connecte au DSP 206, lit le programme en cours, et envoie chaque
réglage au moment où vous le faites :

{% include features.html items=page.features %}

Autour de ça : annuler et rétablir, lier ou copier des voies, préparer un
réglage sans le DSP, et un mode démo pour tout essayer avec un appareil
simulé.

## Linux et Android {#plateformes}

Sur Linux, MereDSP206 est une vraie application native, écrite en Rust avec
GTK 4 et libadwaita : pas d'émulation, pas de machine virtuelle. Elle s'intègre
au bureau GNOME et tourne sur le portable de régie à côté du reste de mes
outils. Elle est livrée avec `dsp206`, son équivalent en ligne de commande.

Sur Android, l'appli est écrite en Kotlin avec Jetpack Compose. L'interface est
pensée pour le pouce : de gros curseurs, des boutons − et + pour le réglage fin,
et l'état du DSP toujours visible. C'est elle que j'utilise pendant les
balances.

{% include shots.html names="linux-mixer,console" %}

Les deux applis lisent et écrivent le même format de fichier : préparez un
réglage au calme sur le PC, ouvrez-le sur le téléphone le jour J.

Ce qui change d'une plateforme à l'autre
{: .table-label}

| | Linux | Android |
|---|---|---|
| Connexion | USB, réseau | USB (adaptateur OTG), Wi-Fi |
| Langue | anglais | français, anglais |
| En plus | raccourcis clavier, générateur de signal de test, commande `dsp206` | propose de s'ouvrir quand on branche le DSP en USB |

## Installer {#installer}

Choisissez votre plateforme. MereDSP206 en est à sa première version : pas
encore de paquet tout prêt, mais l'installation tient en quelques commandes.

{% include install.html platforms=page.install %}

### Linux {#installer-linux}

Il faut Debian 13 (trixie) ou plus récent, ou une distribution récente qui
fournit GTK 4.14 et libadwaita 1.6 au minimum. Installez les outils de
compilation, récupérez le code, compilez, puis installez :

{% include terminal.html commands=page.terminals.linux_build %}

L'appli apparaît dans le menu des applications sous le nom « Mere DSP 206 ».
La commande `meredsp206` la lance aussi, et `dsp206` donne accès à la ligne de
commande. Pour tout retirer : `sudo make uninstall PREFIX=/usr/local`.

**Accès USB.** Branché en USB, le DSP 206 apparaît comme un périphérique HID
nommé « Musicrown Dsp Process » (`0168:0821`). Linux le réserve à
l'administrateur : installez une fois la règle udev fournie, depuis le dossier
`meredsp206` :

{% include terminal.html commands=page.terminals.linux_udev %}

### Android {#installer-android}

Il faut Android 8.0 ou plus récent. La publication sur Google Play est prévue ;
en attendant, deux façons d'installer l'appli :

1. **L'APK de test.** Sur GitHub, ouvrez l'onglet *Actions* du dépôt, la
   dernière exécution réussie du workflow « Android », et téléchargez
   l'artefact `meredsp206-debug-apk` (il faut un compte GitHub). Décompressez-le,
   copiez `app-debug.apk` sur le téléphone, ouvrez-le et autorisez
   l'installation depuis cette source.
2. **Android Studio.** Activez le débogage USB sur le téléphone, ouvrez le
   dossier `android/` du dépôt dans Android Studio, branchez le téléphone et
   lancez *Run*.

L'appli s'affiche en français si le téléphone est en français, en anglais
sinon. Les captures de cette page sont en anglais.

## Se connecter au DSP {#connexion}

Le DSP 206 se relie de deux façons : par son câble USB, ou par sa prise
Ethernet branchée sur le même réseau que le PC ou le téléphone.

USB ou réseau
{: .table-label}

| | USB | Réseau |
|---|---|---|
| Câble | câble USB du DSP ; sur Android, un adaptateur USB-C OTG | prise Ethernet du DSP sur la box, le routeur ou le switch du Wi-Fi |
| Adresse | aucune | 192.168.1.101 en usine (port TCP 9761) |
| Fiabilité | chaque demande reçoit sa réponse en 20 ms environ | un seul client à la fois ; certains DSP décrochent quelques secondes après la connexion |
| Conseil | à privilégier | pratique quand le câble ne va pas jusqu'au DSP |

Les étapes :

1. Branchez le DSP 206 en USB, ou reliez sa prise Ethernet à votre réseau.
2. Ouvrez MereDSP206 sur l'écran *Appareil* (*Device*).
3. En USB, touchez *Connecter en USB* : Android demande l'autorisation la
   première fois. En réseau, touchez *Chercher sur le réseau*, ou saisissez
   l'adresse du DSP, puis *Connecter*.
4. L'appli lit le programme en cours et affiche l'identité du DSP, par exemple
   `DSP206 V0105P`.
5. Réglez : chaque modification part tout de suite vers le DSP.
{: .numbered}

Pas de DSP sous la main ? *Lancer la démo* ouvre l'appli avec un appareil
simulé : tout se règle, rien n'est envoyé.

<aside class="callout" markdown="1">
En réseau, bon à savoir
{: .callout-title}

- Le DSP n'accepte qu'un client réseau à la fois : fermez l'éditeur Windows ou
  toute autre appli connectée avant de vous connecter.
- Après une session réseau, attendez environ une minute avant de vous
  reconnecter. L'appli affiche le temps restant.
- Le DSP et le téléphone (ou le PC) doivent être sur le même sous-réseau. Le
  Wi-Fi n'a pas besoin d'accès à Internet, même si les données mobiles sont
  actives.
</aside>

## L'écran Appareil {#appareil}

{% include shots.html names="appareil" side=true %}

C'est l'écran de connexion, *Device* en anglais. Sous le nom de l'appli, une
ligne rappelle en permanence l'état du lien : *Hors ligne*, *USB*,
*Réseau* suivi de l'adresse, *Démo*, ou *ne répond plus* quand le DSP cesse de
répondre.

- **Connexion** : l'identité du DSP, le preset et le nom du programme en cours.
  *Relire* recharge le programme depuis le DSP, *Relire les pages manquantes*
  complète une lecture interrompue, *Déconnecter* ferme le lien.
- **Réseau (Wi-Fi)** : l'adresse du téléphone, la recherche des DSP du réseau,
  le champ d'adresse IP et le bouton *Connecter*.
- **USB (câble OTG)** : indique si un DSP 206 est branché, avec le bouton
  *Connecter en USB*.
- **Démo** : *Lancer la démo* avec un appareil simulé.
- **Avancé** : l'identifiant de l'appareil (de 1 à 254, 1 en usine) et le
  *Journal du protocole*, qui montre les échanges avec le DSP.

Sur Linux, la page *Device* regroupe aussi les presets (*Recall*, *Store…*),
le générateur de signal de test et l'unité d'affichage des délais. Le
générateur remplace le signal d'entrée par un bruit rose, un bruit blanc ou un
sinus réglable sur les 31 fréquences ISO, de 20 Hz à 20 kHz : repassez sur
*Analog input* une fois le test fini.

## La console {#console}

{% include shots.html names="console" side=true %}

La console (*Mixer*) montre les huit voies du DSP : InA et InB, puis Out1 à
Out6. Pour chacune :

- un vumètre et le niveau en dBu, rafraîchis toutes les 300 ms ;
- le gain, de −60 à +12 dB : faites glisser le curseur, ou utilisez − et +
  pour le réglage fin ;
- *Ø* pour inverser la polarité, *Muet* (*Mute*) pour couper la voie ;
- sur les sorties, la source (*From*) : InA, InB, ou les deux.

Touchez le nom d'une voie pour ouvrir son réglage complet. Une voie liée à
d'autres porte la mention « lié ».

Les vumètres ne tournent que lorsque la console ou l'écran *Canal* est
affiché, et que l'appli est au premier plan : le lien reste libre pour les
réglages.

Sur Linux, la page *Mixer* affiche les huit voies côte à côte, chacune avec ses
filtres et son délai en résumé, et un bouton crayon pour l'ouvrir.

## Régler une voie {#canal}

L'écran *Canal* (*Channel*) règle une voie à la fois : choisissez-la dans la
rangée InA, InB, Out1… en haut de l'écran. Les sections se suivent de haut en
bas ; certaines n'existent que sur les entrées, d'autres que sur les sorties.
Une erreur ? Les flèches en haut à droite annulent et rétablissent.

{% include shots.html names="canal-ina,canal-out1" %}

### Niveau et délai {#niveau}

Le nom de la voie (8 caractères), le gain, le mute, l'inversion de polarité et
le délai, jusqu'à 680 ms. L'unité du délai — millisecondes, mètres ou pieds —
vaut pour tout le DSP et y est enregistrée.

### Égaliseur paramétrique {#eq-parametrique}

La courbe montre la réponse de la voie de 20 Hz à 20 kHz. Touchez un point
numéroté pour choisir une bande, puis réglez son type, sa fréquence, son gain
et son Q, ou contournez-la. *À plat* (*Flat*) remet toutes les bandes à zéro,
et un interrupteur contourne tout l'égaliseur.

- 8 bandes sur les entrées, 9 sur les sorties ;
- fréquence de 19,7 Hz à 20,16 kHz, gain ±12 dB, Q de 0,4 à 128 ;
- 9 types : Peak, Low Shelf, High Shelf, passe-bas et passe-haut 6 ou
  12 dB/octave, Allpass 1 et Allpass 2.

Sur Linux, faites glisser une poignée de la courbe pour changer fréquence et
gain à la fois, et tournez la molette pour le Q. Toutes les bandes sont aussi
dans un tableau sous la courbe.

{% include shots.html names="linux-canal" %}

### Égaliseur graphique (entrées) {#eq-graphique}

31 bandes ISO de 20 Hz à 20 kHz, ±12 dB chacune : glissez le doigt sur les
barres. Un interrupteur le contourne.

### Filtrage (crossover) {#crossover}

Un passe-haut et un passe-bas par voie, de 19,7 Hz à 20,16 kHz. Vingt pentes
au choix : Butterworth et Bessel de 6 à 48 dB/octave, Linkwitz-Riley 12, 24,
36 ou 48 dB/octave.

### Noise gate (entrées) {#gate}

Seuil de −90 à 0 dB, attaque de 1 à 999 ms, maintien de 10 à 999 ms,
relâchement de 10 à 3 000 ms.

### Routage (sorties) {#routage}

Chaque sortie prend InA, InB ou les deux, avec un niveau de −60 à 0 dB pour
chaque entrée.

### Compresseur et limiteur (sorties) {#dynamique}

Le compresseur RMS a un seuil de −90 à +20 dB, un ratio de 1:1 à 1:∞, une
attaque, un relâchement et un knee de 0 à 12 dB. Le limiteur crête a les
mêmes réglages, sans ratio.

### Liaison et copie {#liaison}

Des voies liées suivent les mêmes réglages de traitement, mais gardent chacune
leur nom : pratique pour régler la gauche et la droite d'un seul geste.
*Copier vers…* recopie tous les réglages de la voie vers une autre, sauf son
nom et son routage.

Tous les réglages d'une voie
{: .table-label}

| Réglage | Voies | Plage |
|---|---|---|
| Gain | toutes | −60 à +12 dB |
| Délai | toutes | 0 à 680 ms |
| Égaliseur paramétrique | entrées : 8 bandes · sorties : 9 bandes | 19,7 Hz – 20,16 kHz, ±12 dB, Q 0,4 à 128 |
| Égaliseur graphique | entrées | 31 bandes ISO, ±12 dB |
| Passe-haut, passe-bas | toutes | 19,7 Hz – 20,16 kHz, 6 à 48 dB/octave |
| Noise gate | entrées | seuil −90 à 0 dB |
| Routage | sorties | InA et/ou InB, −60 à 0 dB |
| Compresseur RMS | sorties | seuil −90 à +20 dB, ratio 1:1 à 1:∞ |
| Limiteur crête | sorties | seuil −90 à +20 dB |
| Nom | toutes | 8 caractères |

## Presets et fichiers {#presets}

{% include shots.html names="presets" side=true %}

Le DSP 206 garde le programme en cours, le preset d'usine F00 et 20 presets
utilisateur, de U01 à U20. L'écran *Presets* les liste, le preset actif en
surbrillance.

- *Charger* (*Load*) remplace les réglages du DSP par ceux du preset. Le son
  change immédiatement : l'appli demande confirmation.
- *Enregistrer* (*Store*) sauve les réglages actuels dans un emplacement U01 à
  U20, sous un nom de 14 caractères au plus, sans accents. Confirmation aussi.

En haut de l'écran, le programme en cours :

- *Enregistrer dans un fichier* sauve le programme dans un fichier `.dsp206`,
  *Ouvrir un fichier* le recharge dans l'appli ;
- *Envoyer tout le programme à l'appareil* applique d'un coup tous les
  réglages affichés au DSP, après confirmation.

Sans connexion, l'appli travaille sur un programme local. Préparez votre
réglage chez vous, enregistrez-le dans un fichier, puis envoyez-le au DSP une
fois sur place.

## Linux : clavier et terminal {#linux-avance}

### Raccourcis clavier {#raccourcis}

| Raccourci | Action |
|---|---|
| <kbd>Ctrl</kbd> + <kbd>Z</kbd> | annuler |
| <kbd>Ctrl</kbd> + <kbd>Maj</kbd> + <kbd>Z</kbd> ou <kbd>Ctrl</kbd> + <kbd>Y</kbd> | rétablir |
| <kbd>Ctrl</kbd> + <kbd>O</kbd> · <kbd>Ctrl</kbd> + <kbd>S</kbd> | ouvrir · enregistrer un fichier de programme |
| <kbd>Ctrl</kbd> + <kbd>R</kbd> | relire le programme depuis le DSP |
| <kbd>Alt</kbd> + <kbd>1</kbd> à <kbd>4</kbd> | pages Mixer, Channel, Device, Log |
| <kbd>Ctrl</kbd> + <kbd>?</kbd> | liste des raccourcis |
| <kbd>Ctrl</kbd> + <kbd>Q</kbd> | quitter |

### Options de lancement {#lancement}

`meredsp206` peut se connecter dès le démarrage, en USB, à une adresse IP, ou
lancer la démo. `--page` et `--channel` ouvrent directement une page et une
voie, par exemple `--page channel --channel out1`.

{% include terminal.html commands=page.terminals.linux_launch %}

### La commande dsp206 {#dsp206}

`dsp206` fait la même chose depuis un terminal, pratique pour un script ou un
diagnostic. Les voies s'appellent `ina`, `inb`, `out1` à `out6`.

{% include terminal.html commands=page.terminals.cli %}

- `discover` liste les DSP trouvés en USB et sur le réseau ;
- `info` lit l'identité, les presets et le programme en cours ;
- `meters` affiche des relevés de vumètres (20 par défaut) ;
- `dump` enregistre le programme en cours dans un fichier `.dsp206`, `load`
  envoie un fichier au DSP ;
- `set` change le gain, le mute, la polarité, le délai ou le nom d'une voie,
  rappelle un preset (`recall 3`) ou lance le signal de test (`tone pink`) ;
- `dsp206 help` donne la liste complète.

Sans `--usb`, `dsp206` passe par le réseau, à l'adresse d'usine
192.168.1.101 ou à celle donnée par `--host`.

## En cas de souci {#depannage}

**« Aucun DSP 206 trouvé en USB » sur Linux.** La règle udev manque : installez-la
(voir [Installer](#installer-linux)), puis débranchez et rebranchez le DSP.

**« L'accès USB a été refusé » sur Android.** L'autorisation a été refusée à la
première connexion. Touchez à nouveau *Connecter en USB* et acceptez.

**La recherche réseau ne trouve rien.** Le DSP et le téléphone doivent être sur
le même sous-réseau. Un DSP réglé d'usine répond à 192.168.1.101 : il faut donc
un réseau en 192.168.1.x. Vous pouvez aussi saisir l'adresse à la main.

**« Ne répond plus » en réseau.** Sur certains DSP, le module réseau cesse de
répondre une ou deux secondes après la connexion. L'appli continue d'envoyer
les réglages mais ne peut plus les confirmer : l'écran *Appareil* compte les
réglages non confirmés. Passez en USB, c'est la solution la plus sûre.

**Connexion impossible juste après une session réseau.** Le DSP reste muet
environ une minute après la fin d'une session. Attendez la fin du décompte, et
vérifiez qu'aucune autre appli n'est connectée.

**Des pages du programme manquent.** La lecture a été interrompue :
*Relire les pages manquantes*, sur l'écran *Appareil*, la complète.

## Merci Thomann {#thomann}

Avant de publier quoi que ce soit, j'ai écrit à Thomann. Ils m'ont donné leur
accord pour partager ces applications avec le grand public — et m'ont souhaité
toute la réussite qui va avec. Merci à eux.

Le protocole du DSP a été étudié pour l'interopérabilité. Aucun code ni aucun
élément de l'éditeur d'origine n'est inclus dans MereDSP206.

MereDSP206 est un projet indépendant, non affilié à Thomann ni au fabricant du
DSP 206. t.racks est une marque de Thomann.
{: .note}

## La suite {#la-suite}

MereDSP206 en est à sa version 0.1.0. Le protocole du DSP 206 a été décodé et
testé sur mon appareil ; les deux applis sont jeunes et vont continuer
d'évoluer avec ma sono. Prochaines étapes :

- la publication sur Google Play ;
- des essais plus poussés sur le matériel, en USB comme en réseau ;
- les fonctions de l'éditeur d'origine qui manquent encore : verrouillage par
  mot de passe, réglage de l'identifiant et de l'adresse IP du DSP,
  contournement des filtres passe-haut et passe-bas.

Le code source est public sur
[GitHub](https://github.com/FlogFr/meredsp206) : c'est là que le projet avance.
<!-- TODO: how to report a bug or contact Florian (issues, e-mail) -->

L'appli a été écrite pour ma sono, que je documente dans
[Le sound system](/son/sound-system/).

## In English {#english}

<div class="lang-en" lang="en" markdown="1">
**MereDSP206** is a native Linux (GTK 4) and Android application to control the
**Thomann t.racks DSP 206** loudspeaker management processor over USB or the
network, without the Windows-only original editor. It covers the mixer with
level meters, gains, mutes, polarity and routing, parametric EQ (8 bands on
inputs, 9 on outputs), a 31-band graphic EQ on inputs, high-pass and low-pass
filters up to 48 dB/octave, noise gate, RMS compressor, peak limiter, delays,
channel linking, the unit's presets and program files, plus a demo mode with a
simulated unit. A `dsp206` command-line tool comes with the Linux app. The
source code is on [GitHub](https://github.com/FlogFr/meredsp206). Thomann agreed
to its public distribution. MereDSP206 is an independent project, not
affiliated with Thomann.
</div>
