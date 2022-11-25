#Functions

def add_numbers(num1,num2=99): #if user doesn't input value to num2 then it will remain 99
    return num1 + num2

sum = add_numbers(4);  # calling function
print(sum);
print("\n")


# If statements

is_student = False
is_smart = False

if is_student and is_smart:
    print("You are a smart student")
elif is_student and not (is_smart):
    print("You are not a smart student")
else:
    print("You are not a student and not smart")

if 1<3:    #number compaisons
    print("Number comparison was true")

if "dog" == "cat":
    print("string comparison was true")
print("\n")


#Dictionaries
        #in dictionaries 'keys' and 'values' can be stored
test_grade = {
    "Andy" : "B+",
    "Stanley": "C",
    "Ryan" : "A",
    3 : 95.2
}
print( test_grade["Andy"])
print( test_grade.get("Ryan","No student Found")) #get function is use to find key if not print the given statement
print( test_grade[3])

#while loops
index = 1
while index<10:
    print(index)
    index+=1
print("\n\n")


#For loops

for index in range(5):
    print(index)
print("\n")

lucky_nums = [4,6,3,7,8,9]
for l in lucky_nums:
    print(l)
print("\n")

for letter in "forLoop":
    print(letter)