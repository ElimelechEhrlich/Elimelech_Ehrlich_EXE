total_score = 0
def player(name):
    score = 0
    def add_points(points):
        nonlocal score
        score += points
        global total_score
        total_score += points
        print(f"{name}: {score} points (Total: {total_score})")
    return add_points

alice = player("Alice")
bob = player("Bob")

alice(10)
bob(20)
alice(15)
bob(35)