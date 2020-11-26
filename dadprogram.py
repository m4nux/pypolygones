#Périmètre-Surface et CDG d'un polygone
#****** fonctionnel le 21-11-2020 *****
# Ce programme permet de calculer la surface,le périmetre et le centre
# de gravité d'un polygone quelconque (considéré comme une somme de triangles 
# adjacents quelconques).
# Le  point de depart est en 0,0 et les deplacements se font avec les
# fleches directionnelles. Chaque segment est validé avec la touche "enter".

from tkinter import *
from math import*

def moveR():#mouvements droite, gauche, haut, bas
    avance(10,0)
def moveL(event):
    avance(-10,0)
def moveU(event):
    avance(0,-10)
def moveD(event):
    avance(0,10)
    
def endseg(event): #traitement de la fin de chaque triangle
    global x0,y0,per,surf,pxg,pyg
    listeX0.append(x0)#stocker les coordonnées des sommets 
    listeX1.append(x1)
    listeY0.append(y0)
    listeY1.append(y1)
    x0,y0=x1,y1 # permuter les coordonnées arr/dep
    per=per+a
    surf=surf+sg*s
    pxg=surf*xg
    pyg=surf*yg

def retrace():
    i=0
    while i< len(listeX0):
        can1.create_line(listeX0[i],listeY0[i],listeX1[i],listeY1[i],fill="midnightblue")
        i=i+1
def Triangle(x0,y0,x1,y1): #calculs des éléments du triangle courant
    global a,b,c,s
    a=sqrt(((x1-x0)/2)**2+((y1-y0)/2)**2) #cotés
    b=sqrt((x0/2)**2+(y0/2)**2)
    c=sqrt((x1/2)**2+(y1/2)**2)
    p=(a+b+c)/2 #demi périmètre
    s=sqrt(p*(p-a)*(p-b)*(p-c))# srurface
    return a,b,c,s

def affiche():
    coord.configure(text="Coordonnées :  x=" + str(x1/2)+"   y="+str(y1/2))
    perim.configure(text="Périmètre =" + str(round(per+a)))
    surface.configure(text="Surface ="+str(abs(round(surf+sg*s))))
    cdg.configure(text="Centre de gravité :   XG = "+str(round(xg/2))+"     YG = "+str(round(yg/2)))
    
# procédure générale de déplacement :
def avance(gd, hb):
    global x1,y1,a,sg,xg,yg
    sg=1
    can1.create_line(x0,y0,x1,y1,fill="lightgrey")
    can1.create_line(0,0,x1,y1,fill="lightgrey")
    x1, y1 = x1 +gd, y1 +hb
    if x1>1280:
        x1=1280 #contrôle des limites de fenêtre
    if x1<0:
        x1=0
    if y1>600:
        y1=600
    if y1<0:
        y1=0
    can1.coords(rect, x1,y1, x1+2,y1+2)
    can1.create_line(0,0,x1,y1,fill="lightcoral",dash=(4,4))
    can1.create_line(x0,y0,x1,y1,fill="midnightblue")
    Triangle(x0,y0,x1,y1)
    pv=x0*(y1-y0)-y0*(x1-x0)# pv=produit vectoriel (test de convexité)
    if pv<0:#soustraction surface si polygone convexe
        sg=-1
    if (surf+sg*s)!=0:# tant que la surface vaut 0, le cdg n'est pas calculable
        xg=(sg*(x0+x1)*s/3 + pxg)/(surf+sg*s)
        yg=(sg*(y0+y1)*s/3 + pyg)/(surf+sg*s)
    can1.coords(rect, xg-1,yg-1 ,xg+1,yg+1)
    affiche() #affiche les données calculées
    retrace()# refait les lignes qui peuvent avoir été altérées (chevauchement de tracé)
    
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 0, 0 # coordonnées initiales
x0, y0 = 0, 0 # coordonnées origine
per,surf = 0,0 # perimètre et surface du polygone
a,b,c=0,0,0 #cotés triangles
s=0 #surface du triangle courant
xg,yg=0,0 #coordonnées du centre de gravité
pxg,pyg=0,0 # poids barycentriques
listeX0=[]# listes des coordonnées successives des sommets du polygone
listeX1=[]
listeY0=[]
listeY1=[]

# Création de la fenêtre principale
fen1 = Tk()
fen1.title("Détermination des périmètre, surface et centre de gravité d'un polygone")
# création des widgets "esclaves" 
can1 = Canvas(fen1,bg='lightgrey',height=600,width=1280)
rect = can1.create_rectangle(x1,y1,x1+2,y1+2,width=2,fill='red')
can1.pack(side=TOP)
Button(fen1,text='Quitter',command=fen1.quit).pack(side=RIGHT)
coord=Label(fen1)
coord.pack(side=BOTTOM)
perim=Label(fen1)
perim.pack(side=BOTTOM)
surface=Label(fen1)
surface.pack(side=BOTTOM)
cdg=Label(fen1)
cdg.pack(side=BOTTOM)
fen1.bind("<Right>",moveR)
fen1.bind("<Left>",moveL)
fen1.bind("<Up>",moveU)
fen1.bind("<Down>",moveD)
fen1.bind("<Return>",endseg)
# démarrage du réceptionnaire d’évènements (boucle principale) :
fen1.mainloop()
fen1.destroy()
