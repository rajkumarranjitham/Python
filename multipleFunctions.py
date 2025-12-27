import math
class multipleFunction:
    def Subfields():
        subFields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are: ")
        for temp in subFields:
            return temp
            
    def OddEven():
         number=int(input("Enter a number: "))
         result=number%2
         if(result==1):
             return number," is Odd Number"
         else:
             return number," is Even Number"
             
    def Elegible():
        person=input("Your Gender: ")
        old=int(input("Your Age: "))
        if(person.lower()=="male") & (old<21):
            print("NOT ELIGIBLE")
        elif(person.lower()=="female") & (old<18):
            return "NOT Eligible"
        else:
            return "ELIGIBLE"
            
    def percentage():
        marks={'Subject1':98,'Subject2': 87,'Subject3':95,'Subject4':95,'Subject5':93}
        total=0
        for item in marks:
            print(item)
        for mark in marks.values():
            total+=mark
        print("Total : ",total)
        percent=( total/500 ) * 100
        return "Percentage : ",percent
        
    def triangle():
        Height=32
        Breadth=34
        Area= (Height*Breadth)/2
        Height1=2
        Height2=4
        Breadth1=4
        Perimeter= Height1+Height2+Breadth1        
        print("Height=",Height,"\nBreadth=",Breadth,"\nArea formula: (Height*Breadth)/2\nArea of Triangle: ",Area,"\nHeight1=",Height1,"\nHeight2=",Height2,"\nBreadth=",Breadth1,"\nPerimeter formula: Height1+Height2+Breadth")
        return "Perimeter of Triangle: ",Perimeter