# python_course

Net4U
=====
 
Exercises: 
---------

1.  Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year they were born in. 
 
 
solutions: 
---------

1: 
.. code-block:: text

    import datetime 
    name = input("Enter your name: ") 
    age = int(input("Enter your age: ")) 
    birth = datetime.datetime.utcnow().year - age 
    print("{}; you were born in {}".format(name, birth))
 
make sure you have python 3.7+ installed.

we recommend using venv:

.. code-block:: text

    python -m venv venv
    source venv/bin/activate || venv\\Scripts\\activate
 
