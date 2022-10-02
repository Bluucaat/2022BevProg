run = True
while(run):

    elsoszam = input("Enter A value: ")

    masodikszam = input("Enter B value: ")

    elsoszam = float(elsoszam)
    masodikszam = float(masodikszam)



    try:

        print(elsoszam / masodikszam)

    except ZeroDivisionError:
         print("ZeroDivisionError Ocurred and handled!")
    print("Out of try except blocks")
