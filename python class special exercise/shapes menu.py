from shapes import Square, Rectangle, Circle, Rhombus, Ellipse, Trapezoid

while True:
    print("\n========= GEOMETRY CALCULATOR =========")
    print(
        "1. Square\n2. Rectangle\n3. Circle\n4. Rhombus\n5. Ellipse\n6. Trapezoid\n7. Exit"
    )
    print("=======================================")

    choice = input("Enter your choice (1-7): ")
    shape = None  # تعریف اولیه برای جلوگیری از خطا

    if choice == "1":
        side = float(input("Enter side length: "))
        shape = Square(side)
    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        shape = Rectangle(length, width)
    elif choice == "3":
        radius = float(input("Enter radius: "))
        shape = Circle(radius)
    elif choice == "4":
        d1 = float(input("Enter diagonal 1: "))
        d2 = float(input("Enter diagonal 2: "))
        side = float(input("Enter side length: "))
        shape = Rhombus(d1, d2, side)
    elif choice == "5":
        a = float(input("Enter semi-major axis (a): "))
        b = float(input("Enter semi-minor axis (b): "))
        shape = Ellipse(a, b)
    elif choice == "6":
        # برای ذوزنقه طبق کلاس جدیدت به 5 پارامتر نیاز داری
        b1 = float(input("Enter base 1: "))
        b2 = float(input("Enter base 2: "))
        s1 = float(input("Enter side 1: "))
        s2 = float(input("Enter side 2: "))
        h = float(input("Enter height: "))
        shape = Trapezoid(b1, b2, s1, s2, h)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1-7.")

    # فقط اگر شکلی ساخته شده بود، محاسبات را چاپ کن
    if shape:
        print("-" * 30)
        print(f"Result for {shape.__class__.__name__}:")  # چاپ هوشمند نام کلاس
        print(f"Area: {shape.area():.2f}")
        print(f"Perimeter: {shape.perimeter():.2f}")
        print("-" * 30)
