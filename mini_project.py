name = input("what is your name : ")

print(" good morning "+ name )

print(" how are you "+ name )

reply = input(" reply :   ")

if reply in ["good"," great","nice","excellent"]:
    print(" that's great "+ name )
elif reply in ["normal","fine","average"]:
    print("ohh "+ name )
else : 
    print("so sad to hear that "+ name)
print(" where are you from : ")

reply2 = input("reply2 : ")

if reply2 in ["warangal","hyderabad"]:
    print("you are from my state nice to meet you ")
elif reply2 in ["warangal"]:
    print("ohh your from my city nice to meet you ")
else:
    print("nice place one i will vist one day ")
