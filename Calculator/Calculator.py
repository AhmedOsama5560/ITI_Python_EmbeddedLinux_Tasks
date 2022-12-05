mode = 'Programmer'
mode = input ( "Please choose between Programmer Mode and Standard Mode or enter any value to exit : " )
while ( mode == 'Programmer' or mode == 'Standard' ):
    operation = 1
    if ( mode == 'Programmer' ):
        while ( operation != 0 ):
            print ( "Choose an operation :" )
            print ( "1. Convert between decimal to binary" )
            print ( "2. Convert between decimal to hexadecimal" )
            print ( "3. Convert between decimal to octal" )
            print ( "4. Convert between binary to decimal" )
            print ( "5. Convert between binary to hexadecimal" )
            print ( "6. Convert between binary to octal" )
            print ( "7. Convert between hexadecimal to decimal" )
            print ( "8. Convert between hexadecimal to binary" )
            print ( "9. Convert between hexadecimal to octal" )
            print ( "10. Convert between octal to decimal" )
            print ( "11. Convert between octal to binary" )
            print ( "12. Convert between octal to hexadecimal" )
            print ( "13. Bitwise AND" )
            print ( "14. Bitwise OR" )
            print ( "15. Bitwise NOT" )
            print ( "16. Bitwise XOR" )
            print ( "17. Bitwise Shift Right" )
            print ( "18. Bitwise Shift Left" )
            while ( operation != 0 ):
                operation = int ( input ("Enter number of operation, enter 0 to exit programmer mode : ") )
                if ( operation == 1 ):
                    num = int ( input ( "Enter number : " ) )
                    print ( "Result =", bin ( num ) )
                elif ( operation == 2 ):
                    num = int ( input ( "Enter number : " ) )
                    print ( "Result =", hex ( num ) )
                elif ( operation == 3 ):
                    num = int ( input ( "Enter number : " ) )
                    print ( "Result =", oct ( num ) )
                elif ( operation == 4 ):
                    num = int ( input ( "Enter number : " ), 2 )
                    print ( "Result =", int ( num ) )
                elif ( operation == 5 ):
                    num = int ( input ( "Enter number : " ), 2 )
                    print ( "Result =", hex ( num ) )
                elif ( operation == 6 ):
                    num = int ( input ( "Enter number : " ), 2 )
                    print ( "Result =", oct ( num ) )
                elif ( operation == 7 ):
                    num = int ( input ( "Enter number : " ), 16 )
                    print ( "Result =", int ( num ) )
                elif ( operation == 8 ):
                    num = int ( input ( "Enter number : " ), 16 )
                    print ( "Result =", bin ( num ) )
                elif ( operation == 9 ):
                    num = int ( input ( "Enter number : " ), 16 )
                    print ( "Result =", oct ( num ) )
                elif ( operation == 10 ):
                    num = int ( input ( "Enter number : " ), 8 )
                    print ( "Result =", int ( num ) )
                elif ( operation == 11 ):
                    num = int ( input ( "Enter number : " ), 8 )
                    print ( "Result =", bin ( num ) )
                elif ( operation == 12 ):
                    num = int ( input ( "Enter number : " ), 8 )
                    print ( "Result =", hex ( num ) )
                elif ( operation == 13 ):
                    num1 = int ( input ("Enter number1 : " ) )
                    num2 = int ( input ("Enter number2 : " ) )
                    print ( "Result =", num1 & num2 )
                elif ( operation == 14 ):
                    num1 = int ( input ("Enter number1 : " ) )
                    num2 = int ( input ("Enter number2 : " ) )
                    print ( "Result =", num1 | num2 )
                elif ( operation == 15 ):
                    num = int ( input ("Enter number : " ) )
                    print ( "Result =", ~num )
                elif ( operation == 16 ):
                    num1 = int ( input ("Enter number1 : " ) )
                    num2 = int ( input ("Enter number2 : " ) )
                    print ( "Result =", num1 ^ num2 )
                elif ( operation == 17 ):
                    num1 = int ( input ("Enter number1 : " ) )
                    num2 = int ( input ("Enter number2 : " ) )
                    print ( "Result =", num1 >> num2 )
                elif ( operation == 18 ):
                    num1 = int ( input ("Enter number1 : " ) )
                    num2 = int ( input ("Enter number2 : " ) )
                    print ( "Result =", num1 << num2 )
            operation = int ( input ( "Enter any key to continue in Programmer Mode, enter 0 to exit Programmer Mode : " ) )
    elif ( mode == 'Standard' ):
        while ( operation != 0 ):
            print ( "Choose an operation :" )
            print ( "1. Addition" )
            print ( "2. Subtraction" )
            print ( "3. Multiplication" )
            print ( "4. Integer Division" )
            print ( "5. Remainder of division" )
            print ( "6. Float Division" )
            while ( operation != 0 ):
                operation = int ( input ("Enter number of operation, enter 0 to exit programmer mode : ") )
                if ( operation == 1 ):
                    num1 = int ( input ( "Enter number1 : " ) )
                    num2 = int ( input ( "Enter number2 : " ) )
                    print ( "Result =", num1 + num2 )
                elif ( operation == 2 ):
                    num1 = int ( input ( "Enter number1 : " ) )
                    num2 = int ( input ( "Enter number2 : " ) )
                    print ( "Result =", num1 - num2 )
                elif ( operation == 3 ):
                    num1 = int ( input ( "Enter number1 : " ) )
                    num2 = int ( input ( "Enter number2 : " ) )
                    print ( "Result =", num1 * num2 )
                elif ( operation == 4 ):
                    num1 = int ( input ( "Enter number1 : " ) )
                    num2 = int ( input ( "Enter number2 : " ) )
                    if ( num2 != 0 ):
                        print ( "Result =", num1 // num2 )
                    else:
                        print ( "Error : number2 mustn't be zero" )
                elif ( operation == 5 ):
                    num1 = int ( input ( "Enter number1 : " ) )
                    num2 = int ( input ( "Enter number2 : " ) )
                    if ( num2 != 0 ):
                        print ( "Result =", num1 % num2 )
                    else:
                        print ( "Error : number2 mustn't be zero" )
                elif ( operation == 6 ):
                    num1 = int ( input ( "Enter number1 : " ) )
                    num2 = int ( input ( "Enter number2 : " ) )
                    if ( num2 != 0 ):
                        print ( "Result =", num1 / num2 )
                    else:
                        print ( "Error : number2 mustn't be zero" )
                operation = int ( input ( "Enter any key to continue in Standard Mode, enter 0 to exit Standard Mode : " ) )
    mode = input ( "Please choose between Programmer Mode and Standard Mode or enter any value to exit : " )            
