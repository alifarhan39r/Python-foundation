def average(a=2,b=4):
    print("the average is:",(a+b)/2)
average(4,7)    


def name(**name):
    print("Hello",name["fname"],name["mname"],name["lname"])
    name(fname="farhan",mname="ali",lname="qadri")