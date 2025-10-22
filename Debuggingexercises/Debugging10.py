def down(n):
    while n > 0:
        print (n)
        return down(n - 1)
print(down(5))

# נוסף תנאי עצירה


