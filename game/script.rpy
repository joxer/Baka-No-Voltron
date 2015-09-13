image bg black = Solid((0, 0, 0, 255))
image bg meadow = "baka.jpg"
image bg intro = "intro.jpg"
image bg waifu_1 = "waifu_1.jpg"
image bg waifu_m = "waifu_m.jpg"
image bg voltron = "voltron.jpg"
image bg limbs = "limbs.png"
image bg porta = "porta.jpg"
define d = Character("Diprè", image="dipre")
image d ask = "dipre.png"
define s = Character('Harumi', color="#c8ffc8")
define m = Character('Io', color="#c8c8ff")

# Inizio del gioco
label start:
    $ bwife = False
    $ mwife = False
    $ twife = False
    scene bg intro

    play music "music.ogg" fadeout 10.0 fadein 10.0
    
    "Questo gioco è frutto della testa di tre dementi, se ti senti offeso, abbattuto o prossimo a fare qualche cazzata, siamo esenti dalle responsabilità"
    
    menu:
        "Questo gioco analizza il tuo profilo psicologico e da' risposte in base alla tua personalità\n
        Che tipo di persona sei?"

        "Amo il moe":
            $ mwife = True
         
        "Amo Tsunedere":
             $ twife = True
        
        "Amo Bishojo":
            $ bwife = True
    
    scene bg waifu_1
    
    if mwife:
       m "Questa è mia moglie, è cosi' carina e simpatica, si diverte anche a fare il cosplay, proprio ieri eravamo andati a una fiera giu' in citta'"
    if twife:
       m "Mia moglie è una adorabile scassacazzi, rompe il cazzo ogni volta che puo', pero' poi è dolce e gentile, arrossisce pure"
    if bwife:
       m "Mia moglie fa ancora le superiori, ma ci siamo sposati presto, io frequentavo /a/, lei /b/ e ci siamo conosciuti online"
        
    scene bg waifu_m

    scene bg intro
    m "Amo la mia waifu..."
    m "Mi sono appena svegliato..."
    m "Sono ancora intorpidito..."
    m "Quanto e' bella mia waifu..."
    m "Quanto mi piace vivere con lei"
    
    stop music
    scene bg meadow
    play sound "oh.ogg"

    m "Um... ma cosa succede, la mia waifu..."
    play music "musicbox.ogg"
    m "LE MIE BRACCIA"
    
    if mwife or bwife :
        s "Sembra che ieri sera sia successo qualcosa senpai..."
        s "Mi sono scomparsi i prolungamenti della fica"
    if twife:
        s "A COGLIONE, CHE CAZZO AMO FATTO IERI, STO NCORA SBRONZA"
        s "IO TE DENUNCIO A PER MALTRATTAMENTI ALLA WAIFU"
    m "A me sono scomparse le braccia"
    
    if twife:
        s "BEN TE STA"
    
    scene bg porta

    show d ask
    d "Speriamo sia il campanello giusto"
    play sound "bell.ogg"
    
    if mwife:
        s "SUONANO ALLA PORTA SENPAI!!!"
        play sound "onichan.ogg"

    if twife:
        s "TESTA DE CAZZO, TE STANNO A SUONA'"
    if bwife:
        s "Io devo andare a scuola!!! e stanno suonando, vai tu senpai?"
    
    scene bg waifu_m
    
    if mwife:
        m "è cosi' carina, devo inventarmi qualcosa, potrebbe essere il dottore con la medicina per la sua varicella"
    if twife:
        m "Qua si mette male, se je trovano il livido dell'altra notte finisce che me cacciano a rebibbia"
    if bwife:
        m "La waifu oggi ha il compito di Kanji, non posso farglielo perdere!"
        
    menu:
     "Vuoi che la fusione funzioni?"

     "Sì":
          stop sound

          m "Dovremmo fare un voltron"
          s "Ottima idea"
          stop music
          play music "guile.ogg"
    
          $ flash = Fade(.25, 0, .75, color="#fff")
          scene bg voltron
          with flash

     "No":
        stop sound

        m "mi metto sopra, vediamo che succede"
        s "s-senpai ho paura"
        m "non avere paura"
        m "POTERE DEL CRISTALLO DI LUNA"
        play sound "luna.ogg"
        $ flash = Fade(.25, 0, .75, color="#fff")
        scene bg limbs
        with flash
        
        m "Si e' rotto tutto aiuto"
        s "Ora siamo un limbo solo, nessuno aprirà piu' la porta"
        m "Moriremo di inedia e varicella"
        s "Per l'eternità"
        
        if twife:
            s "TE AVEVO DETTO IO CHE SEI NTESTA DE CAZZO NO?"
            
        show d ask
        d "Siamo ancora qui con andrea diprè a intervistare l'opera d'arte mobile di oggi"
   
        stop sound

    "TO BE CONTINUED...."
    
    return
