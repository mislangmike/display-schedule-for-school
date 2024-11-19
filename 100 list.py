CATEGORIES_OF_ANIMALS = ["African Bush Elephant", "Brown Rat", "Brown-Throated Sloth", "Cat", "Cheetah", "Chimpanzee",
"Common Bottlenose Dolphin", "Dog", "European Hedgehog", "Harbor Seal", "Hippopotamus", "Horse", "Human",
"Little Brown Bat", "North American Porcupine", "Northern Flying Squirrel", "Platypus", "Polar Bear", "Red Kangaroo",
"Tiger", "African Bullfrog", "Asian Common Toad", "Axolotl", "Yellow-Striped Caecilian", "Cane Toad",
"Chinese Giant Salamander", "Common Mudpuppy", "Common Toad", "Edible Frog", "European Fire Salamander",
"Goliath Frog", "Green Tree Frog", "Hellbender", "Horned Marsupial Frog", "Nauta Salamander",
"Paedophryne Amanuensis", "Poison Dart Frogs", "Taita African Caecilian", "Tomato Frog", "Tomato Frog",
"Red Eyed Tree Frog", "American Alligator", "Black Mamba", "Frilled Lizard", "African Spurred Tortoise",
"Gharial", "Gila Monster", "Green Anaconda", "Green Sea Turtle", "Inland Taipan", "Komodo Dragon",
"Leatherback Sea Turtle", "Mojave Desert Tortoise", "Nile Crocodile", "Puff Adder", "Saltwater Crocodile",
"Slow-Worm", "Spectacled Caiman", "Thorny Devi", "Tuatara", "King Cobra", 
"Sword Fish", "Atlantic Cod", "Mackerel", "Trout", "Atlantic Salmon", "Tuna", "Shark", "Red Mullet", "Mahi-Mahi",
"Anchovy", "Haddock", "Red Seabream Fish", "Gold Line Fish", "Pollack", "Ocean Sunfish", "Northern Red Snappe",
"Bonito", "Clown Fish", "Emperor Angelfish", "Bluefish", "Blue Jay", "Barn Owl", "Cardinal", "Duck",
"Downy Woodpecker", "Eagle", "Eastern Bluebird", "Falcon", "Flamingo", "Gannet", "Hawk", "Hummingbird", "Ibis",
"Indigo Bunting", "Jacana", "Junco", "Kestrel", "Kingfisher", "Lammergeier", "Macaw"]

Mamal_Names = ["African Bush Elephant", "Brown Rat", "Brown-Throated Sloth", "Cat", "Cheetah", "Chimpanzee",
                "Common Bottlenose Dolphin", "Dog", "European Hedgehog", "Harbor Seal", "Hippopotamus", "Horse",
                "Human", "Little Brown Bat", "North American Porcupine", "Northern Flying Squirrel", "Platypus",
                "Polar Bear", "Red Kangaroo", "Tiger"]
Amphibian_Names = ["African Bullfrog", "Asian Common Toad", "Axolotl", "Yellow-Striped Caecilian", "Cane Toad",
                "Chinese Giant Salamander", "Common Mudpuppy", "Common Toad", "Edible Frog",
                "European Fire Salamander", "Goliath Frog", "Green Tree Frog", "Hellbender", "Horned Marsupial Frog",
                "Nauta Salamander", "Paedophryne Amanuensis", "Poison Dart Frogs", "Taita African Caecilian",
                "Tomato Frog", "Tomato Frog", "Red Eyed Tree Frog"]
Reptiles_Names = ["American Alligator", "Black Mamba", "Frilled Lizard", "African Spurred Tortoise", "Gharial",
                "Gila Monster", "Green Anaconda", "Green Sea Turtle", "Inland Taipan", "Komodo Dragon",
                "Leatherback Sea Turtle", "Mojave Desert Tortoise", "Nile Crocodile", "Puff Adder",
                "Saltwater Crocodile", "Slow-Worm", "Spectacled Caiman", "Thorny Devi", "Tuatara", "King Cobra"]
Fish_Names = ["Sword Fish", "Atlantic Cod", "Mackerel", "Trout", "Atlantic Salmon", "Tuna", "Shark", "Red Mullet",
                "Mahi-Mahi", "Anchovy", "Haddock", "Red Seabream Fish", "Gold Line Fish", "Pollack", "Ocean Sunfish",
                "Northern Red Snappe", "Bonito", "Clown Fish", "Emperor Angelfish", "Bluefish"]
Bird_Names = ["Blue Jay", "Barn Owl", "Cardinal", "Duck", "Downy Woodpecker", "Eagle", "Eastern Bluebird",
                "Falcon", "Flamingo", "Gannet", "Hawk", "Hummingbird", "Ibis", "Indigo Bunting", "Jacana", "Junco",
                "Kestrel", "Kingfisher", "Lammergeier", "Macaw"]
Mamal_Names.sort()
print("Mamal_Names = ", Mamal_Names)
Amphibian_Names.sort()
print("Amphibian_Names = ", Amphibian_Names)
Reptiles_Names.sort()
print("Reptiles_Names = ", Reptiles_Names)
Fish_Names.sort()
print("Fish_Names = ", Fish_Names)
Bird_Names.sort()
print("Bird_Names = ", Bird_Names)

REPRESENTATIVE = [(Mamal_Names[3]),
(Amphibian_Names[8]),
(Reptiles_Names[12]),
(Fish_Names[15]),
(Bird_Names[19])]
print(REPRESENTATIVE)

Strengths = [(Mamal_Names[3], " = It encourages more physical activity, which means more ,calories burned, helping to keep a slender cat in shape and aiding obese cats in shedding pounds."),
            (Amphibian_Names[8], " = through its feeding habits and interaction with its surroundings, plays a crucial role in nutrient cycling and the control of invertebrate populations."),
            (Reptiles_Names[12], " = developing tools and behavioral skill sets that enabled them to forage for wild greens and flowers, fight for territory and beat the heat in a drying climate by hibernating in deep burrows fringed with creosote."),
            (Fish_Names[15], " = Temminck and Schlegel described this species as the “most common of all the Japanese species of Chrysophrys and the largest in size"),
            (Bird_Names[19], " = From their robust beaks and sharp talons for feeding and defense to their remarkable vocal mimicry and climbing abilities, these magnificent birds exemplify the resilience and adaptability of species thriving in diverse ecosystems.")]
print("Strengths = ", Strengths)

Weaknesses = [(Mamal_Names[3],
              Amphibian_Names[8],
              Reptiles_Names[12],
              Fish_Names[15],
              Bird_Names[19], " = the only weakness of these animals in my opinion is predation among predators and one of predators are humans.")]
print("Weaknesses = ",Weaknesses)
Habitat = [(Mamal_Names[3], " = are animals that do not have a specific habitat that is suited to them and their habitats can often change; they are referred to as a cosmopolitan species."),
              (Amphibian_Names[8], " = live in the forests of central Europe and are more common in hilly areas. They prefer deciduous forests since they like to hide in fallen leaves and around mossy tree trunks."),
              (Reptiles_Names[12], " = are a keystone species, which means they have a higher influence over their ecosystem than other species."),
              (Fish_Names[15], " = spawns between February and August, when they swim from deeper waters to shallower areas. Eggs and juveniles float freely in the ocean, and are not protected by parents, which makes them easy prey for larger fish."),
              (Bird_Names[19], " = use a wide range of habitats, depending on the species. Most live in forests, rainforests, or woodland, but some species prefer the more open savannah-like areas.")],
print("Habitat = ",Habitat)
Cultural_Significance = [(Mamal_Names[3], " = shaping human culture and society."),
              (Amphibian_Names[8], " = Today, the Fire Salamander is recognized not only for its beauty and ecological role but also for the challenges it faces in a rapidly changing world."),
              (Reptiles_Names[12], " = All of the Mojave tribal groups transformed tortoise shells into rattles and drums for ceremonial use."),
              (Fish_Names[15], " = Pagrus major is important in Japanese culture, where it is associated with good fortune and abundance, and eaten on special occasions."),
              (Bird_Names[19], " = Macaws are often seen as symbols of the rainforest and are deeply respected by Amazonian tribes.")]
print("Cultural_Significance = ",Cultural_Significance)
Behavior = [(Mamal_Names[3], " = are comfortable, naughty, caring and cute behavior"),
              (Amphibian_Names[8], " = is largely solitary"),
              (Reptiles_Names[12], " = are usually solitary, but sometimes they share burrows."),
              (Fish_Names[15], " = Seasonal behavior Migrating, Oceanodromous Diet and Nutrition Diet Carnivore, Planktivore Mating Habits Red seabream spawns between February and August, when they swim from deeper waters to shallower areas."),
              (Bird_Names[19], " = are intelligent as they gather in flocks of 10 to 30 individuals. Their loud calls, squawks, and screams echo through the forest canopy.")]
print("Behavior = ",Behavior)
Favorite_Food = [(Mamal_Names[3], " = Cat food, Fish and mices"),
              (Amphibian_Names[8], " = are Insects, worms, spider, snails and slugs"),
              (Reptiles_Names[12], " = Grasses, wildflowers, cacti, and other native plants"),
              (Fish_Names[15], " = Warms and small crustaceans"),
              (Bird_Names[19], " = Vegetables and Insects")]
print("Favorite_Food = ",Favorite_Food)

