RESTAURANTS = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30)
]
def by_rating(r):
    return (-r[1], r[2])
def by_time(r):
    return (r[2], -r[1])
choice=input("sort by (rating/time): ").lower()
if choice=="rating":
    result=sorted(RESTAURANTS, key=by_rating)
elif choice=="time":
    result=sorted(RESTAURANTS, key=by_time)
else:
    print("Unknown option")
    result=[]
for i in range(len(result)):
    name=result[i][0]
    rating=result[i][1]
    minutes=result[i][2]
    print(f"{i + 1}. {name}, {rating} star, {minutes} min")