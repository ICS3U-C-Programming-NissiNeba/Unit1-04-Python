#!/usr/bin/env python3
# created by: Nissi
# date: Sep, 2025
# This program calculates the area and perimeter of a 6cm × 3cm rectangle.

def main():
    length = 6
    width = 3
    
    area = length * width
    perimeter = 2 * (length + width)
    
    print("Length =", length, "cm")
    print("Width =", width, "cm")
    print("Area =", area, "cm²")
    print("Perimeter =", perimeter, "cm")

if __name__ == "__main__":
    main()
