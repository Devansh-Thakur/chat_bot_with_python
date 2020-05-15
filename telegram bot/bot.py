import requests
import json
from pprint import pprint
url = "https://api.telegram.org/bot1051165094:AAGso-tkLHSEY4FN8bhWDBlvW2iIDhBVIg4/"
a = url + "getUpdates" 
b = requests.get(a)
b.json()
for msg in b.json()["result"]:
   update_id = msg["update_id"]
while  True:
   b = requests.get(a)
   b.json()
   for msg in b.json()["result"]:
      update = msg["update_id"]
   if(update_id == update): 
      a = url + "getUpdates" 
      b = requests.get(a)
      b.json()
      for msg in b.json()["result"]:
         xu = msg["message"]["text"]
      if(xu.lower() == "hi"):
         xb="Hello, I am your chatbot.You can ask me about basic C programming ,basic definitions and 32 keywords used in C programming."
      elif(xu.lower() == "int"):
         xb="The int keyword declares integer type variable."
      elif(xu.lower() == "float"):
         xb = "Float is used to declare a variable having decimal."
      elif(xu.lower() == "double"):
         xb = "Double is used to declare longer variable."
      elif(xu.lower() == "char"):
         xb = "The char keyword declares a character variable."
      elif(xu.lower() == "auto"):
         xb = "The auto keyword declares automatic variables." 
      elif(xu.lower() == "break"):
         xb = "The break statement makes program jump out of the innermost enclosing loop." 
      elif(xu.lower() == "continue"):
         xb = "The continue statement skips the certain statements inside the loop." 
      elif(xu.lower() == "switch"):
         xb = "Switch is used to take an expression and run specific cases." 
      elif(xu.lower() == "case"):
         xb = "Case keyword is used to define cases under switch." 
      elif(xu.lower() == "default"):
         xb = "If none of the cases in switch is applicable then default case runs." 
      elif(xu.lower() == "const"):
         xb = "Const is used to declare any identifier as constant." 
      elif(xu.lower() == "do"):
         xb = "Do is used to run the code given body" 
      elif(xu.lower() == "while"):
         xb = "While is used to make loop,the loop continues till expresion inside () is true." 
      elif(xu.lower() == "if"):
         xb = "If is used to run a body if condition inside if() is true." 
      elif(xu.lower() == "else"):
         xb = "if condition inside if does not satisfies then body of else runs.else doesn't contain any conditions."    
      elif(xu.lower() == "enum"):
         xb = "enum is used to declare enumertion types." 
      elif(xu.lower() == "extern"):
         xb = "The extern keyword declares that a variable or a function has external linkage outside of the file it is declared."       
      elif(xu.lower() == "for"):
         xb = "for is also used to run loop, it has three parts inside it i.e. for(initiallisation ; condition ;incee/decreement)" 
      elif(xu.lower() == "goto"):
         xb = "The goto keyword is used for unconditional jump to a labeled statement inside a function." 
      elif(xu.lower() == "short"):
         xb = "It is type modifier that alters the meaning of a base data type to yield a new type.Its range is from -32768 to 32767 " 
      elif(xu.lower() == "long"):
         xb = "It is type modifier that alters the meaning of a base data type to yield a new type.Its range is from -217483648 to 217483648"
      elif(xu.lower() == "signed"):
         xb = "It is type modifier that alters the meaning of a base data type to yield a new type.Its range is from -32768 to 32767" 
      elif(xu.lower() == "unsigned"):
         xb = "It is type modifier that alters the meaning of a base data type to yield a new type.Its range is from 0 to 65535" 
      elif(xu.lower() == "return"):
         xb = "The return keyword terminates the function and returns the value." 
      elif(xu.lower() == "sizeof"):
         xb = "The sizeof keyword evaluates the size of data (a variable or a constant)." 
      elif(xu.lower() == "register"):
         xb = "The register keyword creates register variables which are much faster than normal variables." 
      elif(xu.lower() == "static"):
         xb = "The static keyword creates static variable. The value of the static variables persists until the end of the program." 
      elif(xu.lower() == "struct"):
         xb = "The struct keyword is used for declaring a structure. A structure can hold variables of different types under a single name."    
      elif(xu.lower() == "typedef"):
         xb = "The typedef keyword is used to explicitly associate a type with an identifier." 
      elif(xu.lower() == "union"):
         xb = "A Union is used for grouping different types of variable under a single name."          
      elif(xu.lower() == "void"):
         xb = "The void keyword indicates that a function doesn't return any value." 
      elif(xu.lower() == "volatile"):
         xb = "The volatile keyword is used for creating volatile objects. A volatile object can be modified in an unspecified way by the hardware." 
      elif(xu.lower() == "identifiers"):
         xb = "Identifiers are names given to various program elements such as variables, functions, and arrays." 
      elif(xu.lower() == "keywords"):
         xb = "Keywords are reserved words that have standard predefined meanings. These keywords can only be used for their intended purpose; they cannot be used as programmer defined identifiers. " 
      elif(xu.lower() == "array"):
         xb = "An array is an identifier that refers to a collection of data items of that have the same name. They must also have the same data type"    
      elif(xu.lower() == "string"):
         xb = "A string literal consists of a sequence of multibyte characters enclosed in double quotation marks." 
      elif(xu.lower() == "basic program"):
         xb =   '''#include<stdio.h>
                 int main()
                 {
                    printf("Hello world");
                 }   '''        
               
      else:
         xb="Sorry! I dont understand. Try anoter word."
      c = url + "sendMessage?text={}&chat_id=835615149".format(xb) 
      requests.get(c)
      update_id += 1