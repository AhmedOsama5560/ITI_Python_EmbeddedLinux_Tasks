import sys, time, os
def leftArrow (n):
    for i in range(n):
        for j in range(i,n):
            print ( ' ', end = ' ' )
        for j in range(i+1):
            print ( '*', end = ' ' )
            if i == n-1:
                for k in range(2*(i-1)):
                    print ( '*', end = ' ' )
        print ()
    for i in range (n):
        if i == 0:
            continue
        for j in range (i+1):
            print ( ' ' , end = ' ' )
        for j in range (i,n):
            print ( '*' , end = ' ' )
        print () 
        
def rightArrow (n):
    for i in range(n):
        if i == n-1:
            for j in range(9):
                print ( ' ' , end = ' ' )
            for k in range(6):
                print ( '*', end = ' ' )
        else:
            for j in range(15):
                print ( ' ' , end = ' ' )
        for j in range(i+1):
            print ( '*' , end = ' ' )
        print ()
    for i in range(n):
        if i == 0:
            continue
        for j in range(15):
            print ( ' ' , end = ' ' )
        for j in range(i,n):
            print ( '*' , end = ' ' )
        print ()
        
def downArrow ():
    for i in range (6):
        for j in range (9):
            print ( ' ' , end = ' ' )
        print ( '*' )
    for i in range (3):
        for j in range (6):
            print ( ' ' , end = ' ' )
        for j in range (i+1):
            print ( ' ' , end = ' ' )
        for j in range (i,2):
            print ( '*' , end = ' ' )
        for j in range (i,3):
            print ( '*' , end = ' ' )
        print () 

def upArrow ():
    for j in range(11):
        print ( "\033[F" , end = '' )
    # print ( "\033[D" , end = '' )
    # print ( "\033[D" , end = '' )
    for j in range(12):
            print ( "\033[C" , end = '' )
    for i in range(3):
        for j in range (i,3):
            print ( ' ' , end = ' ' )
        for j in range (i):
            print ( '*' , end = ' ' )
        for j in range (i+1):
            print ( '*' , end = ' ' )
        print()
        for j in range(12):
            print ( "\033[C" , end = '' )
    for i in range(5):
        print ( '      *' )
        for j in range(12):
            print ( "\033[C" , end = '' )
            # print ( '*' )

while True:
    os.system('cls')
    print ( '\n\n\n\n\n' )
    rightArrow(3)
    time.sleep(2)
    sys.stdout.flush()
    for j in range(5):
        print ( "\033[F" , end = '' )
    print ( '\n' )
    # print ( '\n\n\n\n\n' )
    downArrow()
    time.sleep(2)
    sys.stdout.flush()
    for j in range(11):
        print ( "\033[F" , end = '' )
    # print ( '\n\n\n\n\n' )
    leftArrow(3)
    time.sleep(2)
    sys.stdout.flush()
    upArrow()
    time.sleep(2)
