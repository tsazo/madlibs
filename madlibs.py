from matplotlib.pyplot import title


title = "Fitness Tips!"
print("Theme: " + title)

adj1 = input("Adjective: ")
number = input("Number: ")
noun1 = input("Noun: ")
gerund1 = input("Verb ending in 'ing': ")
body1 = input("Part of the body: ")
celeb = input("Celebrity: ")
adj2 = input("Adjective: ")
noun2 = input("Noun: ")
body2 = input("Part of the body: ")
pn1 = input("Plural noun: ")
food1 = input("Type of food: ")
adj3 = input("Adjective: ")
body3 = input("Part of the body: ")
pn2 = input("Plural noun: ")
animal = input("Animal: ")
body4 = input("Part of the body: ")
adj4 = input("Adjective: ")
verb = input("Verb: ")
body5 = input("Part of the body: ")
place = input("A place: ")
food2 = input("Type of food: ")
color = input("Color: ")
body6 = input("Part of the body: ")

madlib = f"""
  Looking for a no-nonsense workout for those days when you're too {adj1} to
  get to the gym? We've got you covered. First, warm up with {number} minutes
  of cardio. Burpees, {noun1} climbers, or {gerund1} jacks will get your 
  {body1} pumping. Then, move on to one of these targeted workouts: \n
  \033[1m Arms: \033[0m Whether you want to get jacked like {celeb} or simply 
  look {adj2} in sleeveless dresses this summer, {noun2} training is key. For
  cut arms, try a superset of push-ups and dips. To complete a push-up, start
  in a locked-out position and lower your {body2} to the floor. If that's too
  difficult, you can keep your {pn1} on the floor for help. Either way, you're
  going to feel the burn! \n
  \033[1m Legs: \033[0m Muscular thighs and {food1}-size butts are totally in
  right now! For {adj3} resutls, add squats and lunges into your daily routine. 
  When squatting, make sure your {body3} gets below your knees for the full
  range of motion. To amp up your workout, add some weight to both movements.
  Hold a pair of {pn2} or grab the family {animal}. Then squat and lunge your
  little {body4} off! \n
  \033[1m Abs: \033[0m Abs... the unicorn of the fitness world. The {adj4}
  truth is, you can do all the crunches {verb}-ups, and {body5}-raises you 
  want.. but abs are ultimately made in (the) {place}. So put away that double
  order of {food2} and reach for a nice {color} salad instead! Your {body6}
  will thank you, even if your taste buds won't!
  """

print(madlib)