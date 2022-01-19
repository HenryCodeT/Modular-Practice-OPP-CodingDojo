# Modular-Practice-OPP-CodingDojo
### Python - Fundamental - OOP 
### Goals and topics
* Get familiar with the modules
* Learn about the __name__ variable
* Practice modularizing code
### Steps
1. __name__ is not only automatically created, but also assigned a value. In your parent.py document add this line:
* modularization/parent.py
* ```{python} print ( __name__ )```
2. Run  ```padre.py``` from the command line
3. You should see ```__main__``` printed to the console 
4. In ```hijo.py``` you should have already imported the parent, if not add that line now 
5. Run  ```hijo.py``` from the command line
6. You should see parent printed to the console.
7. In ```parent.py``` add the following: 
* modularization/parent.py
* ```{python}
if  __name__  = =  "__main__" :
      print ( "the file is being executed directly" )
else :
      print ( "The file is being executed because it is imported by another file. The file is named:" , __name__ )
    ```
8. Now try to run the file directly. You should see the file being executed directly printed to the console. 
9. Run ```hijo.py``` You should see "The file is being run because it is imported by another file. The file is named: parent
10. How is this useful? We can use this conditional to prevent blocks of code from being executed unless the file is being executed directly. Why would we want to do this? Consider a situation where one class depends on another, such as mapping Users to Bank Accounts. In our product document, we could create a lot of test code to make sure we can create new products and execute methods. When we import products into the store file as a module, we don't want all those tests to run every time we run the store file, so inside our product document, we might have something like the following:
* ```{python} 
if  __name__  = =  "__main__" : 
    product =  Product ([args])
     print (product)
     print ( product.add_tax ( 0.18 )) ```
