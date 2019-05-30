from sentence_formula import action_sent
from Sent_selection import get_scores

for sent in action_sent("He hit me with a bat"):
    print(sent ,get_score(sent))


# Prints
# hit Him with a bat  :  10.84556671893511
# hit Him  :  2302.3264182193057
# hit Him with a bat  :  10.84556671893511