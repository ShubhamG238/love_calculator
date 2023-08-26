print("welcome to love calculator")
n1=input('what is ur name ?\n' ).lower()
n2=input('what is the name of ur love?\n').lower()
nn=n1+n2
l1=(nn.count("t") +nn.count("r")+nn.count("u")+nn.count("e"))
l2=(nn.count("l")+nn.count('o')+nn.count('v')+nn.count('e'))
l3=str(l1)+str(l2)
l4=float(l3)
if l4<=10 and l4>=90:
    print(f"your score is {l3}, u go together like coke and mentos") 
elif l4>=40 and l4<=50:
    print(f"ur score is {l3}, u r alright together")
elif l4>50:
    print(f"ur love score is {l3}, damn u r amazing together")
else:
    print(f"ur love score is {l3}")