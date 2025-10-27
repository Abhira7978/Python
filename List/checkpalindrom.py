list1=[1,2,3]

list1_cpy=list1.copy()
list1_cpy.reverse()

if(list1_cpy==list1):
    print("It is a palindrome")
else:
    print("It Is Not A Palindrome")