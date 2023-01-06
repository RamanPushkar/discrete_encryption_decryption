# Head Part Of Program [Decryption]___________________________________________________________________________________


#______________________________________________________________________________________________________________________
# Design of Welcome screen
from colorama import Fore, Back
from colorama import init
from termcolor import colored
init()
print(Fore.RED +'')
print(Back.BLACK + '')
print("~~  "*16,)
print("~~","                                                     ~~")
print("~~                                            ","         ~~")
print("~~        ",colored('Welcome to Encryption Technology PART 2', 'green', 'on_red'),Back.BLACK+Fore.RED +"            ~~")
print("~~                                            ","         ~~")
print("~~","                                                     ~~")
print("~~  "*15)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# take input from user
cypher_text=input ("Enter the Cypher Text/Number : ")
print("Entered Cypher Text are :",cypher_text)
print("-- "*50)
print(Fore.GREEN +"__ "*50)
# For Background Color
print("\033[1;32;40m")
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# Extend Text/DATA From Cypher text/DATA
print("Step 1: ")
print("Extend Text/DATA From Cypher Text/DATA")
print("[Perform Mathematical Operation] ")
print("\n >>"*3)
print("Derived Data [Let]: 80858372756582.0 ")
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# To Convert the Data Integer type from float type [Derived Data]
print("Step 2: ")
# After  Mathematical Operation Find derived_data=int(80858372756582.0)[Let]
derived_data=cypher_text # directly put the derived_data= cypher text
#=int(80858372756582.0)
print("To Convert the Data Integer type from float type [Derived Data] :")
print("derived Data: ",derived_data)
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# To Convert <class 'str'> from <class 'list'>
print("Step 3: ")
print("To Convert [ <class 'str'> from <class 'list'> ]")
print("Before Conversion: ",type(derived_data))
derived_data_str= str(derived_data)
print("Derived Data [Status]:",derived_data_str)
print("After Conversion: ",type(derived_data_str))
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
print("Step 4: ")
# Derived Data List with Splitting at 2 : 80858372756582 >> ['80', '85', '83', '72', '75', '65', '82']
print("Derived Data List with Splitting at 2 :",list([derived_data_str[i:i + 6] for i in range(0, len(derived_data_str), 6)]))
derived_data_str_sp_at_2=list([derived_data_str[i:i + 6] for i in range(0, len(derived_data_str), 6)])
# Transfer value  [from derived_data_str_sp_at_2 to derived_data_str_s3 ]
derived_data_str_s3 = derived_data_str_sp_at_2
print(type(derived_data_str_s3))
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
print("Step 5: ")
print("Derived Data convert string into Integer :")
for i in range(0, len(derived_data_str_s3)):
    derived_data_str_s3[i] = int(derived_data_str_s3[i])
print("Derived Data [Status]:" + str(derived_data_str_s3))
print(type(derived_data_str_s3))
print("-- "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
#Convert Integer string(ASCII CODE) to Character Decrypted File/Text [Original]:
print("Step 6: ")
print("Convert Integer string(ASCII CODE) to Character Decrypted File/Text [Original]:")
# Transfer value  [from list(derived_data_str_s3) to derived_data_str_s3_str2 ]
derived_data_str_s3_str2=list(derived_data_str_s3)
print("Derived Data [Status]:",derived_data_str_s3_str2)
# Using Naive Method
# For Remove space and Comma's fo string and convert ascii to character
res = ""
for val in derived_data_str_s3_str2:
    res = res + chr(val)
derived_data_to_decrypted_data=str(res)
print("Decrypted File/Text [Original]:")
print("````  "*50)
#______________________________________________________________________________________________________________________


#______________________________________________________________________________________________________________________
# end theme design
print(Fore.RED +'')
print(derived_data_to_decrypted_data.lower())
print(Fore.GREEN +'')
#print(type(derived_data_to_decrypted_data))
print("-- "*50)
print(Fore.RED +'')
print("        _______________________________________________________________")
print("        | Copyright © Decryption Technology | Powered by Pushkar Kumar |")
print("        ----------------------------------------------------------------")
#______________________________________________________________________________________________________________________