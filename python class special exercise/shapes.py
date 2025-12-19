import math
# کلاس مادر: به عنوان یک قالب کلی برای تمام شکل‌ها عمل می‌کند
class Shapes:
    def area(self):
        """متد محاسبه مساحت که در کلاس‌های فرزند بازنویسی می‌شود"""
        pass

    def perimeter(self):
        """متد محاسبه محیط که در کلاس‌های فرزند بازنویسی می‌شود"""
        pass


# --- کلاس دایره ---
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # فرمول: عدد پی ضربدر شعاع به توان دو
        return math.pi * (self.radius**2)

    def perimeter(self):
        # فرمول: دو برابر عدد پی ضربدر شعاع
        return 2 * math.pi * self.radius


# --- کلاس مربع ---
class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        # فرمول: یک ضلع ضربدر خودش
        return self.side * self.side

    def perimeter(self):
        # فرمول: چهار برابر یک ضلع
        return 4 * self.side


# --- کلاس مستطیل ---
class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # فرمول: طول ضربدر عرض
        return self.length * self.width

    def perimeter(self):
        # فرمول: دو برابرِ مجموع طول و عرض
        return 2 * (self.length + self.width)


# --- کلاس بیضی ---
class Ellipse(Shapes):
    def __init__(self, a, b):
        # a = نیم‌قطر بزرگ، b = نیم‌قطر کوچک
        self.a = a
        self.b = b

    def area(self):
        # فرمول: عدد پی ضربدر حاصلضرب نیم‌قطرها
        return math.pi * self.a * self.b

    def perimeter(self):
        # فرمول تقریبی دقیق‌تر (Ramanujan): برای محیط بیضی فرمول ساده‌ای وجود ندارد
        # در اینجا از فرمول تقریبی استاندارد استفاده شده است
        return math.pi * (
            3 * (self.a + self.b)
            - math.sqrt((3 * self.a + self.b) * (self.a + 3 * self.b))
        )


# --- کلاس لوزی ---
class Rhombus(Shapes):
    def __init__(self, diagonal1, diagonal2, side):
        self.d1 = diagonal1  # قطر اول
        self.d2 = diagonal2  # قطر دوم
        self.side = side  # ضلع (برای محاسبه محیط لوزی به ضلع نیاز داریم)

    def area(self):
        # فرمول: حاصل‌ضرب دو قطر تقسیم بر ۲
        return 0.5 * self.d1 * self.d2

    def perimeter(self):
        # فرمول: چهار برابر اندازه یک ضلع
        return 4 * self.side


# --- کلاس ذوزنقه ---
class Trapezoid(Shapes):
    def __init__(self, b1, b2, side1, side2, h):
        self.base1 = b1  # قاعده اول
        self.base2 = b2  # قاعده دوم
        self.side1 = side1  # ساق اول
        self.side2 = side2  # ساق دوم
        self.height = h  # ارتفاع

    def area(self):
        # فرمول: (مجموع دو قاعده تقسیم بر ۲) ضربدر ارتفاع
        return 0.5 * (self.base1 + self.base2) * self.height

    def perimeter(self):
        # فرمول: مجموع تمام اضلاع (دو قاعده + دو ساق)
        return self.base1 + self.base2 + self.side1 + self.side2


# --- تست عملیاتی ---
if __name__ == "__main__":
    # ساخت یک نمونه دایره
    c = Circle(5)
    print(f"Circle Area: {c.area():.2f}")

    # ساخت یک نمونه لوزی (قطرها 8 و 6، ضلع 5)
    rh = Rhombus(8, 6, 5)
    print(f"Rhombus Perimeter: {rh.perimeter()}")
