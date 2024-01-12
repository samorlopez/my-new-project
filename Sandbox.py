#string and integer
print ("//str & int//")
x = 2
course_name = "HCDE 310"
print(x + 2)
print (str(x) + course_name)
#lists
print("//lists//")
list_1 = [0,1,2,3,4]
list_2 = ["sam", "lopez", "orendain"]
print (list_1)
print (list_2)
list_3 = [4, "sam", 5, "lopez", list_1]
print (list_3)
#indexes
print("//indexes//")
s1 = "hello 310"
l1 = [2,3,4,7,11,13,17,19,23]
print (s1[0])
print (s1[3])
print (l1[0])
print (l1[3])
location = l1.index(11)
print( )
print(location)
#len
print("//len//")
print (len(s1))
print (len(l1))
l3 = [1,2,[3,4],5]
print (len(l3))
print (l3[len(l3) - 2])
#quotes, tab and newline
print ("//quotes, tab and newline//")
quote = '"this is a quote"'
print (quote)
quote2 = '"this is line one of the quote"\n"this line two of the quote"'
print (quote2)
apostraphe_string = "their they\'re or there"
print (apostraphe_string)
tab_string = "this has a \t tab"
print (tab_string)
#location and find
print ("//location and find//")
l5 = [1,2,3,4,5]
print (l5.index(1))
mystring = "Alice in wonderland"
print (mystring[0])
print (mystring.find("wonderland"))
#split
print("//split//")
print("hello frank world".split())
print("hello, Human Centered Design Engineering, my name is Samuel Lopez".split(', '))
#slices
print("//slices//")
s = "hi there"
print(s[0:2])
print(s[3:6])
print(s[ :6])
print(s[6: ])
print(s[ : -1])
s = "H" + s[1:]
print (s)
