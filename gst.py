print("Introduction to python programming :Rs 499.00")
print("python libraries cookbook: Rs 855.00")
print("datascience in python: Rs 645.00")
print("Delevery charges:Rs 250.00")
print("GST: 12%")
b1price=499.00
b2price=855.00
b3price=645.00
delivery=250.00
n1=int(input("enter no.of introduction to python programming books:"))
n2=int(input("enter no.of python libraries cookbook books:"))
n3=int(input("enter no.of datascience in pyhton books:"))
total=b1price*n1+b2price*n2+b3price*n3
gst=total*12/100
tamount=total+gst+delivery
print("invoice =",round(tamount,2))
