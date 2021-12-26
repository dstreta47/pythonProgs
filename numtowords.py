
words = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
         7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"tewelve",
         13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",
         18:"eighteen", 19:"ninteen", 20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty",
         60:"sixty", 70:"seventy", 80:"eighty", 90:"ninty", 100:"Hundred"}

number = input("enter number [0-100] : ")

strToNumbr = eval(number)

if strToNumbr >=0 and strToNumbr <=100:

    if strToNumbr in words:
        print(words.get(strToNumbr))

    else:
        remainder = strToNumbr % 10
        coefficiant = int(strToNumbr / 10) * 10
        print(words.get(coefficiant), words.get(remainder))
else:
    print("value should be [0-100] only")
