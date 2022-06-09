# Fabbretti A., Oruche A. C.
import pygame
import math
import random

#TITOLO DEL GIOCO:
pygame.display.set_caption("Impiccato")
#----------------------

# SETUP DEL DISPLAY
pygame.init() # serve per assicurarsi che nel corso del codice
# non ci siano errori e bug
LUN, ALT = 1600, 1000
win=pygame.display.set_mode((LUN, ALT)) # sono le dimensioni del display
#--------------------------

# EFFETTI SONORI
applausi = pygame.mixer.Sound("media/APPLAU22.wav")
buuu = pygame.mixer.Sound("media/boo.wav")
vinto = pygame.mixer.Sound("media/Victorysoundeffect.wav")
perso = pygame.mixer.Sound("media/Failsoundeffect.wav")
#--------------------------

# FONT
# questo serve a dare il font, 40 è la grandezza del font: 
LETTERA_FONT = pygame.font.SysFont('comicsans', 40)
PAROLA_FONT = pygame.font.SysFont('comicsans', 80)
HAI_FONT = pygame.font.SysFont('showcard gothic', 80)
TITOLO_FONT = pygame.font.SysFont('monotype corsiva', 90)
TITOLO_FONT2 = pygame.font.SysFont('monotype corsiva', 30)
RICOMINCIA_FONT = pygame.font.SysFont('brushscript mt', 80)
CONTINUA_FONT = pygame.font.SysFont('brushscript mt', 80)
#-------------------------------

#COLORI
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(80,200,80)
BLUE=(0,0,255)
RED=(255,0,0)
PURPLE=(255, 0, 255)
CYAN=(0,255, 255)
#-------------------------------

#VARIABILI DEI BOTTONI
raggio=30
distanza=15
lettere=[]
startx= round((LUN - (raggio * 2 + distanza) * 13) /2)
starty= 700
A = 65
for i in range(26):
# la variabile i mi indica quale bottone sto premendo: 
    x = startx + distanza * 2 + (raggio * 2 + distanza) * (i % 13)
    # (i % 13) manda un promemoria della i dopo aver fatto il modulo di 13
    # (raggio * 2 + distanza) è quanto dista ogni bottone uno dall'altro
    y = starty  + ((i // 13) * (distanza + raggio * 2))
    lettere.append([x,y, chr(A+i), True]) #chr mi converte il num in lettere
                                          # True mi dirà se il bottone sarà visibile oppure no  
#----------------------------
    
# LOAD IMAGES
images=[]
for i in range(2,8):
    image=pygame.image.load("media/disegno" + str(i) + ".png")
    images.append(image)

#-------------------------------
    
# VARIABILI DEL GIOCO
impiccato_status=0 #si riferisce al numero dell'immagine
parole=["CTRL","SCIENTIFICO", "EVVIVA", "GATTO", "CASA", "ANIMALE", "AMORE", "SOLE", "CUFFIE", "COMPUTER", "PALLONE", "ALBERO", "FRAGOLA", "CARCIOFI", "VESPA", "ASSORBIMENTO", "CAPELLI", "DORMIRE", "LINGUAGGIO","PAPPAGALLO", "SOLEGGIATO", "MONITOR", "MONOPOLI", "APE", "MARE", "ERASMUS", "OCEANO","BUONGIORNO", "CENA", "REALTÀ", "MUCCA", "SOFISTICAT", "SPIAGGIA", "TORINO", "AQUILA", "CACAO", "RISPONDI", "PERCHE'", "COSCIENZA"]
parola = random.choice(parole)
indovina=[parola[0]]

#-------------------------------

#DEF DEL GIOCO 
def disegno():
    win.fill(WHITE) # fill = colora tutto il display
    
    # disegna titolo & nome
    titolo = TITOLO_FONT.render("Impiccato 3AS", 1, BLUE)
    nomi = TITOLO_FONT2.render("by Alicia & Amala", 1, BLUE)
    win.blit(titolo, (LUN/2 - titolo.get_width()/2, 40))# blit = mi permette di visualizzare un'immagine o una superficie grafica sopra un'altra
    win.blit(nomi, (1390, 960)) 
    #disegna parola
    display_parola=""
    
    for lettera in parola:
        if lettera in indovina:
            display_parola += lettera + " "
        else:
            display_parola+="-"
    testo=PAROLA_FONT.render(display_parola, 1, BLACK)
    win.blit(testo,(600,400))
            
    
    #disegno bottoni
    for lettera in lettere:
        x,y, ltr, visibile =lettera # (x,y) = coordinate lettera
                                            #ltr=lettera
                                           # visibile = visibilità del bottone
        if visibile:
            pygame.draw.circle(win, BLACK, (x,y), raggio, 4) # 4 è lo spessore del cerchio
            text = LETTERA_FONT.render(ltr, 1, BLACK) # da il colore alla lettera
            # (get_heigh /widht) / da le coordinate del centro della circonferenza
            win.blit(text, (x- text.get_width()/2, y- text.get_height()/2)) 
        
    #blit = disegna l'immagine; (150,100) = coordinate da cui parte il disegno
    if impiccato_status<len(images):
        win.blit(images[impiccato_status],(150,100)) 
        pygame.display.update()  
#-------------------------------

# DEF HAI VINTO/PERSO
def display_messaggio(messaggio):
        pygame.time.delay(1000)# tempo che passa prima di far vedere il messaggio
        win.fill(WHITE)
        if messaggio == "HAI VINTOOOO! :)":
            text = HAI_FONT.render(messaggio, 1 , GREEN)
            vinto.play()
        if messaggio =="HAI PERSO :(":
            text = HAI_FONT.render(messaggio, 1 , RED)
            perso.play()
        win.blit(text, (LUN/2 - text.get_width()/2, ALT/2- text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)# il tempo che passa dopo il messaggio prima che  appare il menu
#-------------------------------
        
# DEF DELLA PAAROLA NN INDOVINATA
def last_word():
    win.fill(BLACK)
    text = PAROLA_FONT.render(F'La Parola era: {parola}', 1, WHITE)
    win.blit(text, (int(LUN/2 - int(text.get_width()/2)), int(ALT/2) - int(text.get_height()/2)))
    pygame.display.update() 
#-------------------------------
 
 # DEF PER RICOMINCIARE IL GIOCO
def ricomincia_gioco():
    global hangman_status # global: mi lascia usare le variabili al di fuori della funzione
    global word
    global guessed
    global letters
    global i
    global x
    global y
    hangman_status = 0
    parola = random.choice(parole)
    indovina = []
    lettere = []
    for i in range(26):
        x = startx + distanza * 2 + (raggio * 2 + distanza) * (i % 13)
        y = starty  + ((i // 13) * (distanza + raggio * 2))
        lettere.append([x,y, chr(A+i), True])
        main()

#-------------------------------
# CICLO DEL GIOCO     
def main():
    gameover = False
    gameclose= False
    global impiccato_status # global : mi consente di accedere alle variabili anche se non c'è nella funzione 
    # FPS frame per second la velocità del gioco per secondo
    FPS= 60
    Clock=pygame.time.Clock() #si assicura che venga rispettato l'FPS
    run=True #controlla che il loop sia sempre vero
    
    while run:
        Clock.tick(FPS) #si assicura che il while rispetti cio che abbiamo scritto prima con FPS
        
        for evento in pygame.event.get(): #controlla gli eventi del gioco
            if evento.type == pygame.QUIT: #chiude il gioco
                run= False
                
            if evento.type == pygame.MOUSEBUTTONDOWN: #controlla i movimenti del mouse
                m_x , m_y =pygame.mouse.get_pos() # coordinate della lettera
                for lettera in lettere:
                    x, y, ltr, visibile = lettera
                    applausi.play
                    if visibile:
                        dist = math.sqrt ((x - m_x)**2 + (y- m_y)**2) # è la radice quadrata delle coordinate della posizione del mouse
                        #applausi.play()
                        if dist < raggio:
                            lettera[3] = False # mi toglie il bottone dalla riga
                            indovina.append(ltr)# mi aggiunge la lettera sui spazi vuoti
                            #applausi.play()
                            if ltr not in parola:
                                impiccato_status+=1 # aggiunge un pezzo di immagine in più ad ogni lettrea sbagliata
                                buuu.play()
        disegno()
        
        won =True 
        for lettera in parola:
            if lettera not in indovina:
                won = False
                break
        
        # HAI VINTO O PERSO?
        if won:
            display_messaggio("HAI VINTOOOO! :)")
            win.fill(CYAN)
            frase = CONTINUA_FONT.render("Clicca <<SPAZIO>> per continuare", 1 , BLACK)
            win.blit(frase, (LUN/2 - frase.get_width()/2, ALT/2- frase.get_height()/2))
            for event in pygame.event.get():
                # Condition becomes true when keyboard is pressed   
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("ciao")
                        main()
                        
            pygame.display.update()
            pygame.time.delay(10000)
                
        if impiccato_status==6:
            last_word()
            pygame.time.delay(4000)            
            perso = display_messaggio("HAI PERSO :(")
            break
main()
#-------------------------------

# VUOI RICOMINCIARE IL GIOCO?
while True:
    run = True
    win.fill(PURPLE)
    frase = RICOMINCIA_FONT.render("Clicca <<INVIO>> per ricominciare", 1 , BLACK)
    win.blit(frase, (LUN/2 - frase.get_width()/2, ALT/2- frase.get_height()/2))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                  main()
                  
    pygame.display.update()
    pygame.time.delay(10000)
    
pygame.quit()
