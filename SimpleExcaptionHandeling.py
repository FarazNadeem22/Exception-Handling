lst = [1,2,3,4,5,6,7]
Break = False
while True:
    try:
        item = lst.pop()
        print("Popping",item)
    except IndexError as e:
        print("From the except block: We tried to pop too many values from the list")
        print(e)
        #break
        Break = True 
    finally:
        if Break:
            break
        else:
            continue