import random
import time

class Introduce:
    Bleeps = ["&","#","$","-","*","+","@","_"]

    def MyselfAs (name):
        print("Hi! I'm " + str(name))
        time.sleep(2)
        print("I am a self taught programmer, who's only goal is to get better")
        time.sleep(2)
        print("I have made a few projects, and am great at python (for being self taught :P)")
        time.sleep(2)
        print("but I want to learn some web design, c++, c# for unity, and alot more!")
        time.sleep(2)
        print("enjoy your day, and remember:")
        time.sleep(3)
        while True:
            G = ""
            for I in range(0,4):
                G = G + Introduce.Bleeps[random.randint(0,len(Introduce.Bleeps)-1)]
            print(G + " programming")
            time.sleep(0.2)

Introduce.MyselfAs("kenny")
