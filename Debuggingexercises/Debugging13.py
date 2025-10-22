funcs = []
for i in range(3):
    funcs.append(lambda : print(i)))
    funcs[i]()

  # Expected 0,1,2; what happens?


# ה I הוא עם הערך מהספירה האחרונה בעת ההפעלה של כל פונקציה במערך, כך שתמיד זה 2 
# הפעלת הפונקציה הוכנסה כפעולה נוספת בלולאה הראשית בכל ריצה 
# דרך נוספת להכניס את הפונקציה למערך ביחד עם ההפעלה שלה , כלומר להכניס את הקריאה לפונקציה וכך הפונקציה תפעל בזמן הריצה הנוכחי. כך:

funcs = []
for i in range(3):
    funcs.append((lambda i: print(i))(i))

# או:

funcs = []
for i in range(3):
    f = lambda i: print(i)
    funcs.append(f(i))

