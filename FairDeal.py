import csv
import re


class CustomerNotAllowedException(Exception):
    pass
class Customer(object):
    def __init__(self,title,fName,lName,flag):
        self.title = title
        self.fName=fName
        self.lName=lName
        self.flag =flag
    def getFlag(self):
        return self.flag
    def __repr__(self):
        return "{0} {1} {2} {3}".format(self.title,self.fName,self.lName, self.flag)



def main():
    customers = list()
    filename = "C:/Users/Kumar/Downloads/574_m3_datasets_v3.0/FairDealCustomerData.csv"
    with open(filename) as fp:
        csv_reader = csv.reader(fp)
        for row in csv_reader:
            name = row[1]
            flag = row[2]
            #extract title, first name and last name
            (title,fName, lName) = extractnameinfo(name)
            #create a customer object
            cust = Customer(title,fName, lName, flag)
            print(cust)
            #append to customers list
            customers.append(cust)
    
    #create order for customer 1 throws exception
    createOrder(customers[0])



def extractnameinfo(name):
    #Mr. John William
    pattern = r"([a-zA-Z]+.)\s+(\w+)\s+(\w+)?"
    match = re.search(pattern, name)
    title = match.group(1)#first bracket
    fName = match.group(2)#second bracket
    lName = match.group(3)#third bracket
    #in case no match assign a empty string
    lName = "" if lName is None else lName
    return (title, fName, lName)


def createOrder(customer):
    if customer.getFlag() == "1":
        raise CustomerNotAllowedException


main()
