def rand_name():
    import random
    first_names = ["John", "Jane", "Michael", "Emily", "Jacob", "Emma", "William", "Ava", "Olivia", "Sophia", "Mia", "Isabella", "Ethan", "Avery", "Liam", "Noah", "Mason", "Elijah", "James", "Alexander", "Daniel", "Matthew", "Samuel", "David", "Joseph", "Benjamin", "Jonathan", "Ryan", "Nicholas", "Tyler", "Jack", "William", "Adam", "Zachary", "Nathan", "Brandon", "Justin", "Luke", "Jordan", "Dylan", "Evan", "Andrew", "Gary", "Angel", "Isaiah", "Austin", "Ethan", "Jordan", "Nicholas", "Ethan", "William", "Michael", "Daniel", "Matthew", "Joshua", "Nicholas", "Andrew", "Christopher", "Alexander", "William", "Ethan", "Michael", "Daniel"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Young", "Allen", "King", "Wright", "Scott", "Green", "Baker", "Adams", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Bailey", "Bell", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross", "Henderson"]
    
    rf = random.choice(range(len(first_names)+1))
    rl = random.choice(range(len(last_names)+1))

    return first_names[rf] + " " + last_names[rl]