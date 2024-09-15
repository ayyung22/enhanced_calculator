# --------------------------------------------------------
# Lab 2: Getting Started with Python
# CIS 103: Building a Simple Calculator, part II
# Instructor: Md Ali
# Student Name: Annie Yung
# Date: 9/14/2024

#This code displays a basic calculator in which the user is able to choose a mathematical operation and input two numerical values.

import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # For Windows
        print("Clearing")
    else:
        os.system('TERM=xterm-256color clear')
        print("Clearing")

#Defining mathematical operations such as addition, subtraction, multiplication, exponentiation, modulus operator, and square root value

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero!."

def exponent(x,y):
    return x ** y

def mod (x,y):
    return x % y

def sqrt (x):
    return x ** (1/2)

#Defining user input for math operations
def main():
    while True:
        print("Please type in the math operation you would like to complete:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exponents")
        print("6. Remainder value")
        print("7. Square root")
        print("8. Exit")
        print("9. Clear screen")

        choice = input("Enter choice: ")

#if value == 8, then the loop will end

        if choice == '8':
            print("exiting, thank you!")
            break

        if choice == '9':
            break
            os.system('clear')

        if choice == '1':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} ** {num2} = {exponent(num1, num2)}")
        elif choice == '6':
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
            print(f"{num1} %= {num2} = {mod(num1, num2)}")
        elif choice == '7':
            num1 = float(input("Enter your number: "))
            print(f"{num1} ** (1/2) = {sqrt(num1)}")
        elif choice == '9':
            clear_screen()
        else:
            print("Invalid input, please select a math operation again")

if __name__ == "__main__":
    main()

