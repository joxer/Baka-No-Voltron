﻿image bg black = Solid((0, 0, 0, 255))
image bg meadow = "baka.jpg"
image bg waifu_1 = "waifu_1.jpg"
image bg waifu_m = "waifu_m.jpg"
image bg voltron = "voltron.jpg"
define s = Character('Harumi', color="#c8ffc8")
define m = Character('Io', color="#c8c8ff")

# Inizio del gioco
label start:
    $ pwife = False
    $ lwife = False
    $ gwife = False
    scene bg black

    play music "music.ogg" fadeout 10.0 fadein 10.0
    m "Amo la mia waifu..."
    
    menu:
     "Che tipo di waifu ti piace?"

     "Loli.":
         $ lwife = True
         m "EHEHHEHEHEH mi piacciono le loli ( ͡° ͜ʖ ͡°)"

     "Dolce calma e sincera":
         $ gwife = True
         m "Tanto bella e onesta pare la donna mia, mi pare di vivere un verso di dante con la waifu"

     "BDSM":
        m  "Alla mia waifu piace il cazzo"
        $ pwife = True
    
    m "Mi piace quando fa la brava ragazzina"
    scene bg waifu_1
    if pwife:
        m "Io l'abbraccio e si fa stuprare"
        m "Dopotutto e' una waifu, senno' a che serve"
    if gwife:
        m "Lei ama me e io amo lei, mi sembra  di vivere una fantasia di /a/"
    if lwife:
        m "Mi piace quando dice ONICHAAAAN..."
        
    scene bg waifu_m

    scene bg black
    
    m "Mi sono appena svegliato..."
    m "Sono ancora intorpidito..."
    m "Quanto e' bella mia waifu..."
    m "Quanto mi piace vivere con lei"
    
    stop music
    scene bg meadow
    play sound "oh.ogg"

    m "Um... ma cosa succede, la mia waifu..."
    play sound "onichan.ogg"
    play music "musicbox.ogg"
    m "LE MIE BRACCIA"
    
    s "Sembra che ieri sera sia successo qualcosa senpai..."
    s "Mi sono scomparsi i prolungamenti della fica"

    
    m "A me sono scomparse le braccia"
    m "Dovremmo fare un voltron"
    s "Ottima idea"
    stop music
    play music "guile.ogg"
    
    $ flash = Fade(.25, 0, .75, color="#fff")
    scene bg voltron
    with flash
    
    "TO BE CONTINUED...."
    
    return
