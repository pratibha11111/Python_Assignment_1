# -*- coding: utf-8 -*-
"""Let's Code Data Structures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YQcLt_kr-bPRPkS8GdwQe47LTJBg1U-U

Write a python program which accepts the radius of a circle from the user and computes area.
"""

pi= 3.14159265
radius= float(input("Enter the radius of the circle:"))
area= pi*(radius)**2
print("The area of the circle is:", area)

"""Write a python program to accept a filename from the user and print the extension of that."""

file_name= input("Enter the name of the file:")
ext= file_name.split(".")
print("The extension of the file which you have entered is:", ext[-1])