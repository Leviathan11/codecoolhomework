import sys

def sayhello(boolean):
    if boolean:
        print ("Hello", sys.argv[1], "!")
        if not sys.argv[1].isalpha():
            print ("Your name looks exotic, but hey! I am just a script, no judging!:)")
    else:
        print ("Hello World!")
    print ("")

length = len(sys.argv)

if length == 2:
    bool = "true"
else :
    bool = ""
    if length > 2:
        print ("Next time please only write one name (without space).\nNow i will welcome the World!")

sayhello(bool)
