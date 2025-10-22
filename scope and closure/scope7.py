def discount_factory(percent):
    def apply(price):
        return price - (price * percent / 100)
    return apply
student = discount_factory(10)
print(student(100))

vip = discount_factory(25)
print (vip(100))

# ההדפסה תהיה המחיר (הפרמטר בפעולת הפרינט) פחות האחוז (הפרמטר בפונקציה המרכזית)