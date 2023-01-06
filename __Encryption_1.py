# Head Part Of Program [Encryption]___________________________________________________________________________________


#______________________________________________________________________________________________________________________
# Design of Welcome screen
from colorama import Fore, Back
from colorama import init
from termcolor import colored
init()
print(Fore.RED +'')
print(Back.BLACK + '')
print("~~  "*15,)
print("~~","                                                     ~~")
print("~~                                            ","         ~~")
print("~~        ",colored('Welcome to Encryption Technology PART 1', 'green', 'on_red'),Back.BLACK+Fore.RED +"            ~~")
print("~~                                            ","         ~~")
print("~~","                                                     ~~")
print("~~  "*15)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# To take input String from user
input_text = input("Enter Text to Encryption : ")
text =input_text
print("-- "*50)
# To Display the Entered String
print("Entered Original String:")
print(Fore.WHITE +"=>",text)
print(Fore.RED +'')
print("-- "*50)
print(Fore.GREEN +"__ "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# for Background color
print("\033[1;32;40m \n")
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# Convert String to lower() to Upper() [Capital Latter] :
print(" Step 1:")
print("Converted String [Capital Latter] :")
# upper() function to convert
# string to upper_case
print("==>>",text.upper(),)
convert_1=text.upper()
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
print(" Step 2:")
print("split the string into character :")
input_text=convert_1
split_string=[c for c in input_text]  # in Python, a string is just a sequence, so we can iterate over it!
print(split_string)
print(type(split_string))
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
print(" Step 3:")
split_ascii_code=[ord(c) for c in input_text]
print("split the string into ascii code :")
print(split_ascii_code)
print(type(split_string))
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# mapping
print(" Step 4:")
print("split the ascii code into ascii code string :")
list_string_ascii = map(str, split_ascii_code)
print(list(list_string_ascii))
a1=str(split_ascii_code)
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
print(" Step 6:")
print("Convert ASCII String to Integer Value :")
a2= a1.replace(',', '')
a3= a2.replace(' ', '')
a4= a3.replace('[','')
a5_data=a4.replace(']','')
#print("Value is :",a5_data)
print(type(a5_data))
a6_data=int(a5_data)
print("Data Status [Integer]:",a6_data)
print(type(a6_data))
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
print(" Step 7:") # Here a6_data is main data
print("Reduce Text/DATA From User Text/DATA")
print("[Perform Mathematical Operation] ")
print("\n >>"*3)
print("Converted Cypher Text:")
print(Fore.RED+'')
print(a6_data)
print(Fore.GREEN +'')


print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# end theme design
print(Fore.RED +'')
print("")
print("        _______________________________________________________________")
print("        | Copyright © Encryption Technology | Powered by Pushkar Kumar |")
print("        ----------------------------------------------------------------")
#______________________________________________________________________________________________________________________