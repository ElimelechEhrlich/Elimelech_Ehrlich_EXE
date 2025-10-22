funcs = []
for i in range(3):
    funcs.append(lambda: print(i))
    funcs[i]()

  # Expected 0,1,2; what happens?


# ה I נמצא על האינדקס האחרון בעת ההכנסה של כל פונקציה למערך, כך שתמיד זה 2.
# הפעלת הפונקציה הפנימית הוכנסה כפעולה נוספת בלולאה הראשית

