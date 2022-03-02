#program gyak
name=input("Add meg a neved")
count=input("Hanyszor irjam ki a neved:")
for i in range(0,int(count)):
    print(str(i+1) + " " + name)