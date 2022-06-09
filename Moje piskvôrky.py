import tkinter as tk
import random as rd
P = tk.Canvas(width=1100, height=650, bg="green")
P.pack()

P.create_text(200,80, text="Pišqvuôrky", font="Arial 50 bold", fill="white")
P.create_text(570,20, text="Pravidla:", font="Arial 10 bold", fill="white", anchor="nw")
P.create_text(625,32, text="1.) Hraje sa ľavým tlačítkom myši, na hornej časti ukazuje kto je na rade", font="Arial 10 bold", fill="white", anchor="nw")
P.create_text(625,44, text="2.) Hráči sa striedaju po každom označení políčka svojím symbolom", font="Arial 10 bold", fill="white", anchor="nw")
P.create_text(625,56, text="3.) Vyhráva ten hráč, čo spojil tri svoje symboli", font="Arial 10 bold", fill="white", anchor="nw")
P.create_text(625,68, text="4.) Po spojení symbolo si daný hráč pridá jednu mincu do svojej kapsy PTM", font="Arial 10 bold", fill="white", anchor="nw")
P.create_text(625,80, text="5.) Nové kolo sa začne stačením tlačítka: Nové Kolo", font="Arial 10 bold", fill="white", anchor="nw")
P.create_text(625,92, text="6.) Nová hra sa začne stačením tlačítka: Nové Hra", font="Arial 10 bold", fill="white", anchor="nw")

P.create_rectangle(100,625,300,425, fill="darkgoldenrod", outline="black")
P.create_rectangle(800,625,1000,425, fill="darkgoldenrod", outline="black")
P.create_line(100,225,300,425, fill="red",width=10)
P.create_line(100,425,300,225, fill="red",width=10)
P.create_oval(800,225,1000,425,fill="blue", outline="")
P.create_oval(810,235,990,415,fill="blue", outline="")

P.create_line(510,40,590,120,fill="red", width=10, tag="s5")
P.create_line(510,120,590,40,fill="red", width=10, tag="s5")

P.create_rectangle(400,200,700,500, fill="grey")

for x in range(399,701,100):
    P.create_line(x,199,x,501, width=5)
    
for y in range(199,501,100):
    P.create_line(400,y,700,y, width=5)

t=1

q=64

p1=[]
p2=[]
p3=[]
p4=[]
p5=[]
p6=[]
p7=[]
p8=[]
p9=[]

m1=11          
m2=12
m3=13
m4=14
m5=15
m6=16
m7=17
m8=18
m9=19

##    if 100<x<300 and 425<y<625:
##        P.create_oval(x+10,y+10,x-10,y-10, fill="yellow", tag="s2")
##    if 800<x<1000 and 425<y<625:
##        P.create_oval(x+10,y+10,x-10,y-10, fill="yellow", tag="s2")

def bod1(x,y):
    x=rd.randint(100,300)
    y=rd.randint(425,625)
    P.create_oval(x+10,y+10,x-10,y-10, fill="yellow", tag="s2")
    
def bod2(x,y):
    x=rd.randint(800,1000)
    y=rd.randint(425,625)
    P.create_oval(x+10,y+10,x-10,y-10, fill="yellow", tag="s2")

def k(j):
    global t
    global q
    x=j.x
    x=(x//100*100+50)
    y=j.y
    y=(y//100*100+50)
    global m1,m2,m3,m4,m5,m6,m7,m8,m9
    global s5,s3,s4
    P.delete("s5")
    q=q
    if q==64:
        if x==450 and y==250 and [x,y] not in p1:
            p1.append([x,y])
            t = t+1
            if t %2 == 0:
                P.create_line(x+40,y-40,x-40,y+40, width=5, fill="red", tag="s1")
                P.create_line(x+40,y+40,x-40,y-40, width=5, fill="red", tag="s1")
                m1=10
            else:
                P.create_oval(x+40,y-40,x-40,y+40, fill="blue", tag="s1")
                P.create_oval(x+36,y+36,x-36,y-36, fill="grey", tag="s1")
                m1=5
            if m1==m2==m3:
                P.create_line(450,250,650,250, fill="white", width=7, tag="s1")
                q=32
                if m1%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                  
            if m1==m4==m7:
                P.create_line(450,250,450,450, fill="white", width=7, tag="s1")
                q=32
                if m1%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                   
            if m1==m5==m9:
                P.create_line(450,250,650,450, fill="white", width=7, tag="s1")
                q=32
                if m1%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))   

        if x==550 and y==250 and [x,y] not in p2:
            p2.append([x,y])
            t = t+1
            if t %2 == 0:
                P.create_line(x+40,y-40,x-40,y+40, width=5, fill="red", tag="s1")
                P.create_line(x+40,y+40,x-40,y-40, width=5, fill="red", tag="s1")
                m2=10
            else:
                P.create_oval(x+40,y-40,x-40,y+40, fill="blue", tag="s1")
                P.create_oval(x+36,y+36,x-36,y-36, fill="grey", tag="s1")
                m2=5
            if m1==m2==m3:
                P.create_line(450,250,650,250, fill="white", width=7, tag="s1")
                q=32
                if m2%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                    
            if m2==m5==m8:
                P.create_line(550,250,550,450, fill="white", width=7, tag="s1")
                q=32
                if m2%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                   
            
        if x==650 and y==250 and [x,y] not in p3:
            p3.append([x,y])
            t=t+1
            if t%2==0:
                P.create_line(x+40,y-40,x-40,y+40, width=5, fill="red", tag="s1")
                P.create_line(x+40,y+40,x-40,y-40, width=5, fill="red", tag="s1")
                m3=10
            else:
                P.create_oval(x+40,y-40,x-40,y+40, fill="blue", tag="s1")
                P.create_oval(x+36,y+36,x-36,y-36, fill="grey", tag="s1")
                m3=5
            if m1==m2==m3:
                P.create_line(450,250,650,250, fill="white", width=7, tag="s1")
                q=32
                if m3%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                    
            if m3==m6==m9:
                P.create_line(650,250,650,450, fill="white", width=7, tag="s1")
                q=32
                if m3%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                        
            if m3==m5==m7:
                P.create_line(650,250,450,450, fill="white", width=7, tag="s1")
                q=32
                if m3%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                    

        if x==450 and y==350 and [x,y] not in p4:
            p4.append([x,y])
            t=t+1
            if t%2==0:
                P.create_line(x+40,y-40,x-40,y+40, width=5, fill="red", tag="s1")
                P.create_line(x+40,y+40,x-40,y-40, width=5, fill="red", tag="s1")
                m4=10
            else:
                P.create_oval(x+40,y-40,x-40,y+40, fill="blue", tag="s1")
                P.create_oval(x+36,y+36,x-36,y-36, fill="grey", tag="s1")
                m4=5
            if m4==m5==m6:
                P.create_line(450,350,650,350, fill="white", width=7, tag="s1")
                q=32
                if m4%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                        
            if m1==m4==m7:
                P.create_line(450,250,450,450, fill="white", width=7, tag="s1")
                q=32
                if m4%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                       

        if x==550 and y==350 and [x,y] not in p5:
            p5.append([x,y])
            t=t+1
            if t%2==0:
                P.create_line(x+40,y-40,x-40,y+40, width=5, fill="red", tag="s1")
                P.create_line(x+40,y+40,x-40,y-40, width=5, fill="red", tag="s1")
                m5=10
            else:
                P.create_oval(x+40,y-40,x-40,y+40, fill="blue", tag="s1")
                P.create_oval(x+36,y+36,x-36,y-36, fill="grey", tag="s1")
                m5=5
            if m4==m5==m6:
                P.create_line(450,350,650,350, fill="white", width=7, tag="s1")
                q=32
                if m5%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                        
            if m2==m5==m8:
                P.create_line(550,250,550,450, fill="white", width=7, tag="s1")
                q=32
                if m5%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                      
            if m1==m5==m9:
                P.create_line(450,250,650,450, fill="white", width=7, tag="s1")
                q=32
                if m5%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                  
            if m3==m5==m7:
                P.create_line(650,250,450,450, fill="white", width=7, tag="s1")
                q=32
                if m5%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))      
            
        if x==650 and y==350 and [x,y] not in p6:
            p6.append([x,y])
            t=t+1
            if t%2==0:
                P.create_line(x+40,y-40,x-40,y+40, width=5, fill="red", tag="s1")
                P.create_line(x+40,y+40,x-40,y-40, width=5, fill="red", tag="s1")
                m6=10
            else:
                P.create_oval(x+40,y-40,x-40,y+40, fill="blue", tag="s1")
                P.create_oval(x+36,y+36,x-36,y-36, fill="grey", tag="s1")
                m6=5
            if m4==m5==m6:
                P.create_line(450,350,650,350, fill="white", width=7, tag="s1")
                q=32
                if m6%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                     
            if m3==m6==m9:
                P.create_line(650,250,650,450, fill="white", width=7, tag="s1")
                q=32
                if m6%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))              

        if x==450 and y==450 and [x,y] not in p7:
            p7.append([x,y])
            t=t+1
            if t%2==0:
                P.create_line(x+40,y-40,x-40,y+40, width=5, fill="red", tag="s1")
                P.create_line(x+40,y+40,x-40,y-40, width=5, fill="red", tag="s1")
                m7=10
            else:
                P.create_oval(x+40,y-40,x-40,y+40, fill="blue", tag="s1")
                P.create_oval(x+36,y+36,x-36,y-36, fill="grey", tag="s1")
                m7=5
            if m7==m8==m9:
                P.create_line(450,450,650,450, fill="white", width=7, tag="s1")
                q=32
                if m7%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                      
            if m1==m4==m7:
                P.create_line(450,250,450,450, fill="white", width=7, tag="s1")
                q=32
                if m7%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                    
            if m3==m5==m7:
                P.create_line(650,250,450,450, fill="white", width=7, tag="s1")
                q=32
                if m7%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                  

        if x==550 and y==450 and [x,y] not in p8:
            p8.append([x,y])
            t=t+1
            if t%2==0:
                P.create_line(x+40,y-40,x-40,y+40, width=5, fill="red", tag="s1")
                P.create_line(x+40,y+40,x-40,y-40, width=5, fill="red", tag="s1")
                m8=10
            else:
                P.create_oval(x+40,y-40,x-40,y+40, fill="blue", tag="s1")
                P.create_oval(x+36,y+36,x-36,y-36, fill="grey", tag="s1")
                m8=5
            if m7==m8==m9:
                P.create_line(450,450,650,450, fill="white", width=7, tag="s1")
                q=32
                if m8%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                    
            if m2==m5==m8:
                P.create_line(550,250,550,450, fill="white", width=7, tag="s1")
                q=32
                if m8%2==0:
                    bod1(    rd.randint(100,300),rd.randint(425,625))
                else:
                    bod2  (rd.randint(800,1000),rd.randint(425,625))                      
                
        if x==650 and y==450 and [x,y] not in p9:    
            p9.append([x,y])
            t=t+1
            if t %2==0:
                P.create_line(x+40,y-40,x-40,y+40, width=5, fill="red", tag="s1")
                P.create_line(x+40,y+40,x-40,y-40, width=5, fill="red", tag="s1")
                m9=10
            else:
                P.create_oval(x+40,y-40,x-40,y+40, fill="blue", tag="s1")
                P.create_oval(x+36,y+36,x-36,y-36, fill="grey", tag="s1")
                m9=5
            if m7==m8==m9:
                P.create_line(450,450,650,450, fill="white", width=7, tag="s1")
                q=32
                if m9%2==0:
                    bod1
                else:
                    bod2                        
            if m3==m6==m9:
                P.create_line(650,250,650,450, fill="white", width=7, tag="s1")
                q=32
                if m9%2==0:
                    bod1
                else:
                    bod2                        
            if m1==m5==m9:
                P.create_line(450,250,650,450, fill="white", width=7, tag="s1")
                q=32
                if m9%2==0:
                    bod1
                else:
                    bod2                        
                
        if t%2==0:
            P.delete("s4")
            P.delete("s5")
            P.create_oval(510,40,590,120, fill="blue", tag="s3")
            P.create_oval(520,50,580,110, fill="green", tag="s3")
        else:
            P.delete("s3")
            P.delete("s5")
            P.create_line(510,40,590,120,fill="red", width=10, tag="s4")
            P.create_line(510,120,590,40,fill="red", width=10, tag="s4")
        
P.bind("<Button-1>", k )


def bod(j):
    x=j.x
    y=j.y
    if 100<x<300 and 425<y<625:
        P.create_oval(x+10,y+10,x-10,y-10, fill="yellow", tag="s2")
    if 800<x<1000 and 425<y<625:
        P.create_oval(x+10,y+10,x-10,y-10, fill="yellow", tag="s2")

P.bind("<Button-3>",bod)

def z():
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    P.delete("s1")
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    p5=[]
    p6=[]
    p7=[]
    p8=[]
    p9=[]
    global m1
    global m2
    global m3
    global m4
    global m5
    global m6
    global m7
    global m8
    global m9
    m1="11"
    m2="12"
    m3="13"
    m4="14"
    m5="15"
    m6="16"
    m7="17"
    m8="18"
    m9="19"
    P.delete("s2")
    global q
    q=64

def u ():
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    P.delete("s1")
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    p5=[]
    p6=[]
    p7=[]
    p8=[]
    p9=[]
    global m1
    global m2
    global m3
    global m4
    global m5
    global m6
    global m7
    global m8
    global m9
    m1="11"
    m2="12"
    m3="13"
    m4="14"
    m5="15"
    m6="16"
    m7="17"
    m8="18"
    m9="19"
    global q
    q=64

but = tk.Button(text="Nové Kolo", command=u)
but.pack()
but = tk.Button(text="Nová Hra", command=z)
but.pack()

P.mainloop