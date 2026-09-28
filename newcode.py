a=[]#this is used for name of book
b=[]#this ia used the borrower of book("")
while True:
    print()
    print("1. add book")
    print("2. issue a book")
    print ("3. return the book")
    print("4. show all books")
    print("0. exit")

    choice=input("enter choice:")

    if choice =="1":
         name=input("book name:")
         a.append(name)
         b.append("")
         print("book added.")

    elif choice=="2":
            name=input("book name to be issued to : ")
            if name in a:
                i=a.index(name)
                if b[i]=="":
                    b[i]=input("borrower name:")
                    print("book issued.")
                else:
                    print("book already issued")
            else:
                print("book not found")

    elif choice=="3":
         name=input ("please enter the name of the book to return: ")
         if name in a:
              i=a.index(name)
              if b[i]!="":
                    b[i]=""
                    print("book returned")
              else:
                   print("book not recieved.")
         else:
              print("book not found.")
    elif choice=="4":
         for i in range (len(b)):
              if b[i]=="":
                   print("title is available")
              else:
                   print(f"{a[i]} issued to {b[i]}")
    elif choice=="0":
         print("bye")
         break
    else:
         print("wrong choice ")
