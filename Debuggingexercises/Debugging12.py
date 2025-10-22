def add_item(item, bucket=None):
    if bucket == None:
        bucket = []
    bucket.append(item)
    return bucket

print(add_item("a"))
print(add_item("b"))


# שונה ברירת המחדל של המשתנה עבור הרשימה לNone כדי שיצור רשימה חדשה עבור כל הרצה חדשה - אם 
