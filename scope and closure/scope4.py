def counter():
    num = 0
    def add_one():
        nonlocal num
        num += 1
        print(num)
    add_one()

counter()

# נוסף 
# nonlocal
# כדי שהפעולה += תהיה תקינה, 
# מאחר וב
# local 
# המשתנה הזה לא קיים

# global
# תהיה שגיאה פה, כי גם המשתנה מבחוץ אינו נמצא בגלובל אלא ב
# enclosing
