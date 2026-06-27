import random
subject = [
    "akshat",
    "anivesh",
    "gupta",
    "amit",
    "shravan",
    "himanshu",
    "alok"
]
actions = [
    "is eating",
    "is playing",
    "is sleeping",
    "is studying"
    "is coding",
    "is running",
]
place_or_thing = [
    "in the park",
    "at home",
    "in the library",
    "in the office",
    "in the gym"
    "in the cafe",
]
while True:
     subject = random.choice(subject)
     actions = random.choice(actions)
     place_or_thing = random.choice(place_or_thing)  
     headline = f"breaking news: {subject} {actions} {place_or_thing}"
     print("/n"+ headline)    
     user_input = input("do you want to generate another headline? (yes/no): ").strip()
     if user_input == "no":
        break
print("thanks for using the fake headline genrater")    



