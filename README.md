-Vending Machine Simulation (OOP with Inheritance & Polymorphism)
-This project is a simulation of a vending machine implemented in Python using Object-Oriented Programming concepts such as inheritance and polymorphism.


-Features:
-Base Class:Product (name, price, display_info).
-Subclasses:
-Drink → adds volume (ml).
-Snack → adds calories.
-Candy → adds flavor.
-Each subclass overrides the display_info() method to show product-specific details.
-Products are loaded from a file (products.txt).
-The program presents a menu for users to select products and displays product details.


-##Project Structure

-VendingMachine/
-│── product.py      # Base class Product
-│── drink.py        # Drink subclass
-│── snack.py        # Snack subclass
-│── candy.py        # Candy subclass
-│── main.py         # Entry point, loads products and runs the program
-│── products.txt    # File containing product data
-│── README.md       # Project documentation


-Example products.txt
-Drink,Cola,1.50,500
-Snack,Chips,2.00,250
-Candy,Gummy Bears,1.20,Strawberry
-Drink,Water,1.00,600
-Snack,Cookies,1.75,300
-Format:
-Drink,Name,Price,Volume
-Snack,Name,Price,Calories
-Candy,Name,Price,Flavor


-How to Run
-Make sure you have Python 3 installed.
-Clone or download this repository.
-Run the main file:
-python machine.py


-OOP Concepts Used
-Inheritance → Subclasses (Drink, Snack, Candy) extend the Product class.
-Polymorphism → Each subclass overrides display_info().
-Encapsulation → Attributes are managed inside their respective classes.
-Factory Logic → Conditional logic creates the correct subclass from file input.



-Future Improvements
-Save purchase history.
-Add balance and payment simulation.
-Implement a GUI using Tkinter or a web interface with Flask.
-Made with ❤️ using Python and OOP.
