import time

def Now():
    t = time.localtime()

    current_time = time.strftime("%H:%M:%S", t)

    print(current_time)
    
    if(current_time > "%07:%00:%00"):
        print("It's too late")
    else:
        print("You have arrived in a goot time")

Now()
