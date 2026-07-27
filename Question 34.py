# Write a lambda function using reduce() which accepts list of strings and returns list of strings having lenght greater than 5

from functools import reduce 

Lenght = lambda x, y: x + [y] if len(y) > 5 else x

def main():

    n = int(input("How many no of elements you want to enter in list : "))

    Data = []

    for i in range(n):
        element = input(f"Enter element {i+1} :")
        Data.append(element)

    print("List Before reduce is : ",Data)

    rData = reduce(Lenght, Data,[])

    print("List after reduce : ",rData)

if __name__ == "__main__":
    main()


# Step by step Explaination


            # Step 1: Import reduce

            # What is reduce()?

            # reduce() takes all items from a list and combines them one by one.

            # Think of it as a robot that processes the list item by item.

            # It keeps an accumulated result and updates it at every step.

            # Step 2: Start the program

            # This creates a function named main().The program will start executing from here.

            # Step 3: Ask how many elements

            # Example:

            # User enters: 5

            # Now:

            # n = 5

            # Step 4: Create an empty list

            # Currently:

            # Data = []

            # Think of this as an empty basket waiting for items.

            # Step 5: Take inputs one by one

            # Suppose the user enters:

            # Apple

            # Cat

            # Elephant

            # Banana

            # Hi

            # Iteration 1:

            # Data becomes:

            # ['Apple']

            # Iteration 2:

            # Data becomes:

            # ['Apple', 'Cat']

            # Iteration 3:

            # Data becomes:

            # ['Apple', 'Cat', 'Elephant']

            # Iteration 4:

            # Data becomes:

            # ['Apple', 'Cat', 'Elephant', 'Banana']

            # Iteration 5:

            # Final list:

            # Data = ['Apple', 'Cat', 'Elephant', 'Banana', 'Hi']

            # Step 6: Print the original list

            # Output:

            # List Before reduce is : ['Apple', 'Cat', 'Elephant', 'Banana', 'Hi']

            # Step 7: The Important Part - reduce()

            # This is the heart of the program.

            # General syntax:

            # function → lambda x, y: ...

            # iterable → Data

            # initial_value → []

            # So reduce starts with:

            # x = []

            # Now it processes each item one by one.

            # Understanding the Lambda Function

            # Equivalent normal function:

            # Meaning:

            # x = accumulated result so far

            # y = current element from the list

            # If current string length is greater than 5, add it to x.

            # Otherwise, keep x unchanged.

            # Dry Run (Most Important)

            # Initial value:

            # x = []

            # Current item y = 'Apple'

            # Condition:

            # Return:

            # Result:

            # []

            # Current item y = 'Cat'

            # Condition is False.Result remains:

            # []

            # Current item y = 'Elephant'

            # Condition:

            # Return:

            # Result:

            # ['Elephant']

            # Current item y = 'Banana'

            # Condition is True.Return:

            # Result:

            # ['Elephant', 'Banana']

            # Current item y = 'Hi'

            # Condition is False.Result stays:

            # ['Elephant', 'Banana']

            # Final value stored in rData
            # Step 8: Print the result

            # Output:

            # List after reduce : ['Elephant', 'Banana']

            # Visual Memory Trick

            # Imagine a basket:

            # Start with an empty basket []

            # Check 'Apple' → too short → don't put it in

            # Check 'Cat' → too short → don't put it in

            # Check 'Elephant' → long enough → put it in

            # Check 'Banana' → long enough → put it in

            # Check 'Hi' → too short → don't put it in

            # Basket at the end:

            # ['Elephant', 'Banana']

            # One Important Interview Point

            # Although this works with reduce(), Python programmers would usually use filter() for this task because we are filtering elements, not combining them.Using filter():

            # Both produce the same result:

            # ['Elephant', 'Banana']

            # But for your assignment, the reduce() solution you wrote is correct and demonstrates how an accumulator works in reduce(). 🎉