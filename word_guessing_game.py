import random
name=input("Enter your name: ")
print("Good luck "+name+" please write your answers in small letters.")
words=["paper","goods","purple","sky","greeks","songs","school","math","robin","kingfisher","trees",
"orange","mango","banana","apple","window","zebra","parrot","water","computer","characters","tiger",
"lions","coconut","lime","plays","tomorrow","scale","puppet","dogs","lovely","beautiful","girls","boys"
,"tomato","sugar","salt","chocolate","sweet","pineapple","door","pets","cats","leaves","queen","kings",
"carts","silk","market","mouth","eyes","nose","balls","earth","magnet","seas","baby","rock","grandmother"
,"grandfather","grand","bells","christmas","presents","kangaroo","koala","zoo","one","two","three","four"
,"five","six","seven","eight","nine","zero","hero","fun","time","lunch","ice","cream","dance","wine",
"gas","sides","cheese","french","chips","burger","sandwich","bath","bank","motorcycle","bike","cycle","body"
,"bowl","basket","bow","drums","eat","ate","hair""buses","shirt","book","study","loose","cupboard","board"
,"type","piano","violin","pepper","sand","socks","shoes","questions","answers","mouse","keys","black","name"
,"fix","fox","bears","frame","farm","field","fire","scouts","guides","ruler","asia","snakes","ladders","cube"
,"loyal","leader","hot","cold","dress","skirt","pant","test","text","strings","pot","glass","can","prime"
,"right","wrong"]
choose=random.choice(words)
print("Guess the characters:")
guesses=' '
turns=15
while turns>0:
    failed=0
    for x in choose:
        if x in guesses:
            print(x)
        else:
            print("_")
            failed+=1
    if failed==0:
        print(name+" you win!!")
        print("The word is "+choose)
        break
    guess=input("Guess the characters:")
    guesses+=guess
    if guess not in choose:
        turns-=1
        print("Wrong!")
        print("You have ",turns," more guesses")
        if turns==0:
            print("You loose!!!")
            print("The word is " + choose)
