items =      [ 'Banana', 'Apple', 'Pineapple', 'Peach' ]
quantities = [ 50, 45, 52, 98]
costs =      [ 1.25, 2.56, 5.75, 4.51 ]
cart_items = []
cart_quantities = []
cart_costs = []
while True:
    print ( items )
    print ( quantities )
    print ( costs )
    mode = input ( "Choose between owner mode and customer mode or enter 0 to exit : " )
    if mode == 'owner':
        while True:
            print ( "Enter 1 to add new products" )
            print ( "Enter 2 to modify names of existing products" )
            print ( "Enter 3 to modify quantities of existing products" )
            print ( "Enter 4 to modify cost of existing products" )
            print ( "Enter 5 to show products" )
            print ( "Enter 6 to delete products" )
            print ( "Enter 7 to exit" )
            operation = int ( input ( "Operation : " ) )
            if operation < 5:
                print ( "Enter 0 in product name field to exit this operation" )
            if operation == 1:
                while True:
                    inputVar = input ( "Enter product name : " )
                    if inputVar == '0':
                        break
                    elif inputVar in items:
                        print ( "Item already exists" )
                    else:
                        items.append(inputVar)
                        inputVar = int ( input ( "Enter product quantity : " ) )
                        quantities.append(inputVar)
                        inputVar = float ( input ( "Enter product cost : " ) )
                        costs.append(inputVar)
                        print ( "New product has been added\n " )
            elif operation == 2:
                while True:
                    inputVar = input ( "Enter product name : " )
                    if inputVar == '0':
                        break
                    elif inputVar not in items:
                        print ( "Item doesn't exist" )
                    else:
                        index = items.index( inputVar )
                        items[index] = input ( "Enter new name : " )
                        print ( "Product name has been modified\n" )
            elif operation == 3:
                while True:
                    inputVar = input ( "Enter product name : " )
                    if inputVar == '0':
                        break
                    elif inputVar not in items:
                        print ( "Item doesn't exist" )
                    else:
                        index = items.index( inputVar ) 
                        quantities[index] = int ( input ( "Enter quantity : " ) )
                        print ( "Product quantity has been modified\n" )
            elif operation == 4:
                while True:
                    inputVar = input ( "Enter product name : " )
                    if inputVar == '0':
                        break
                    elif inputVar not in items:
                        print ( "Item doesn't exist" )
                    else:
                        index = items.index( inputVar ) 
                        costs[index] = float ( input ( "Enter cost : " ) )
                        print ( "Product cost has been modified\n" )
            elif operation == 5:
                i = 0
                while i < len(items):
                    print ( 'Item :', items[i], ', Quantity :', quantities[i], ', Cost :', costs[i] )
                    i = i + 1
                print ()
            elif operation == 6:
                while True:
                    inputVar = input ( "Enter product name : " )
                    if inputVar == '0':
                        break
                    elif inputVar not in items:
                        print ( "Item doesn't exist" )
                    else:
                        index = items.index( inputVar )
                        items.pop ( index )
                        quantities.pop ( index )
                        costs.pop ( index )
                        print ( "Product has been deleted\n" )
            elif operation == 7:
                break
            else:
                print ( "Invalid choice" )
    elif mode == 'customer':
        while True:
            print ( "Enter 1 to show available products" )
            print ( "Enter 2 to show your cart" )
            print ( "Enter 3 to add products to your cart" )
            print ( "Enter 4 to remove products from your cart" )
            print ( "Enter 5 to clear your cart" )
            print ( "Enter 6 to confirm your purchase" )
            print ( "Enter 7 to exit" )
            operation = int ( input ( "Operation : " ) )
            if operation == 1:
                i = 0
                while i < len(items):
                    print ( 'Item :', items[i], ', Quantity :', quantities[i], ', Cost :', costs[i] )
                    i = i + 1
                print ()
            elif operation == 2:
                i = 0
                while i < len(cart_items):
                    print ( 'Item :', cart_items[i], ', Quantity :', cart_quantities[i], ', Cost :', cart_costs[i] )
                    i = i + 1
                print ( 'Total cost :', sum ( cart_costs ) )
                print ()
            elif operation == 3:
                while True:
                    inputVar = input ( "Enter product name : " )
                    if inputVar == '0':
                        break
                    elif inputVar not in items:
                        print ( "Product doesn't exist" )
                    elif inputVar in cart_items:
                        owner_index= items.index ( inputVar )
                        cart_index = cart_items.index ( inputVar )
                        inputVar = int ( input ( "Enter quantity : " ) )
                        if inputVar > quantities[owner_index]:
                            print ( "Not enough quantity in store\n" )
                        else:
                            quantities[owner_index] -= inputVar
                            cart_quantities[cart_index] += inputVar
                            cart_costs[cart_index] += costs[owner_index] * inputVar
                            print ( "Products have been added to your cart\n" )
                    elif inputVar not in cart_items:
                        owner_index= items.index ( inputVar )
                        inputQuantity = int ( input ( "Enter quantity : " ) )
                        if inputQuantity > quantities[owner_index]:
                            print ( "Not enough quantity in store\n" )
                        else:
                            cart_items.append(inputVar)
                            quantities[owner_index] -= inputQuantity
                            cart_quantities.append(inputQuantity)
                            cart_costs.append( costs[owner_index] * inputQuantity )
                            print ( "Products have been added to your cart\n" )
            elif operation == 4:
                while True:
                    inputProduct = input ( "Enter product name : " )
                    if inputProduct == '0':
                        break
                    elif inputProduct not in cart_items:
                        print ( "Product doesn't exist" )
                    elif inputProduct in cart_items:
                        owner_index= items.index ( inputProduct )
                        cart_index = cart_items.index ( inputProduct )
                        inputQuantity = int ( input ( "Enter quantity : " ) )
                        if inputQuantity > cart_quantities[cart_index]:
                            print ( "Not enough quantity in your cart\n" )
                        else:
                            quantities[owner_index] += inputQuantity
                            cart_quantities[cart_index] -= inputQuantity
                            cart_costs[cart_index] -= costs[owner_index] * inputQuantity
                            if cart_quantities[cart_index] == 0:
                                cart_items.pop(cart_index)
                                cart_quantities.pop(cart_index)
                                cart_costs.pop(cart_index)
                            print ( "Products have been removed from your cart\n" )
            elif operation == 5:
                cart_index = 0
                for item in cart_items:
                    owner_index = items.index(item)
                    quantities[owner_index] += cart_quantities[cart_index]
                    cart_index = cart_index + 1
                cart_items.clear()
                cart_quantities.clear()
                cart_costs.clear()
                print ( "Your cart has been cleared\n" )
            elif operation == 6:
                i = 0
                while i < len(items):
                    if quantities[i] == 0:
                        items.pop(i)
                        quantities.pop(i)
                        costs.pop(i)
                    i = i + 1
                cart_items.clear()
                cart_quantities.clear()
                cart_costs.clear()
                print ( "Thank you for purchasing our products\n" )
            elif operation == 7:
                break
            else:
                print ( "Invalid choice" )
    elif mode == '0':
        break