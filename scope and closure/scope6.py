def make_greeter(name):
    def greet():
        print("Hi", name)
    return greet

say_hi = make_greeter("Dudu")
say_hi()

# הפרמטר 'Dudu' 
# נשמר ב
# Closure 
# והפונקציה הפנימית יכולה למשוך את זה 
# למרות שהוא פרמטר שלא הוזן לה
# 