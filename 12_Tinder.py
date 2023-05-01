import random

# Define a list of men and women
men = ["Kshitij", "Giriraj", "Siddhant", "Vineet","Rachit"]
women = ["Amrutha"]

# Define the preferences of each person
#men_prefs = {"Adam": ["Beth", "Amy", "Diana", "Cathy"],
           ##  "Bob": ["Cathy", "Diana", "Amy", "Beth"],
            # "Charlie": ["Diana", "Beth", "Amy", "Cathy"],
            # "David": ["Amy", "Beth", "Cathy", "Diana"]}
men_prefs = {"Kshitij": ["Giriraj", "Siddhant", "Amrutha", "Rachit","Vineet"],
            "Giriraj": ["Vineet", "Kshitij", "Amrutha","Siddhant","Rachit" ],
            "Siddhant": [ "Kshitij", "Rachit", "Amrutha", "Giriraj","Vineet"],
            "Vineet": ["Amrutha", "Giriraj", "Kshitij","Siddhant","Rachit"],
            "Rachit": ["Siddhant",  "Kshitij", "Giriraj","Amrutha","Vineet"]
             }

#women_prefs = {"Amy": ["Bob", "David", "Adam", "Charlie"],
#               "Beth": ["Bob", "Charlie", "David", "Adam"],
#               "Cathy": ["Adam", "Charlie", "David", "Bob"],
#               "Diana": ["Charlie", "Adam", "Bob", "David"]}
women_prefs = {"Amrutha":["Giriraj","Vineet","Kshitij","Siddhant","Rachit"]}

# Define a dictionary to keep track of who is currently matched
matches = {}

# Define a function to run the Gale-Shapley algorithm
def gale_shapley(men_prefs, women_prefs):
    # Create a list of all the available men
    free_men = list(men_prefs.keys())
    # Keep running the algorithm until all men are matched
    while free_men:
        # Choose a random man from the list of free men
        man = random.choice(free_men)
        # Get the man's preferences
        prefs = men_prefs[man]
        # Go through the man's preferences until he finds a woman who is available
        for woman in prefs:
            # Check if the woman is already matched
            if woman not in matches:
                # If she isn't, match the man and woman together
                matches[woman] = man
                free_men.remove(man)
                break
            else:
                # If she is, check if she prefers the new man or her current match
                current_man = matches[woman]
                current_rank = women_prefs[woman].index(current_man)
                new_rank = women_prefs[woman].index(man)
                if new_rank < current_rank:
                    # If she prefers the new man, unmatch her from the current man and match her with the new man
                    matches[woman] = man
                    free_men.remove(man)
                    free_men.append(current_man)
                    break

# Run the algorithm to find the matches
gale_shapley(men_prefs, women_prefs)

# Print out the final matches
for woman, man in matches.items():
    print(woman + " is matched with " + man)


'''In the lines you mentioned:

makefile
Copy code
current_rank = women_prefs[woman].index(current_man)  # 0
new_rank = women_prefs[woman].index(man)  # 1
current_rank and new_rank represent the index of current_man and man in the preference list of the woman woman. The preference list is an ordered list of men ranked in order of preference by the woman.

For example, if woman's preference list is:


['Adam', 'Bob', 'Charlie']
And current_man is 'Adam', then current_rank will be 0, because 'Adam' is at the first position in the list. 
Similarly, if man is 'Charlie', then new_rank will be 2, because 'Charlie' is at the last position in the list.

The purpose of comparing these ranks is to determine whether the woman prefers the new man (man) over her current partner (current_man). 
If new_rank is smaller than current_rank, it means that the woman prefers the new man over her current partner, and the algorithm will update the matches accordingly.'''