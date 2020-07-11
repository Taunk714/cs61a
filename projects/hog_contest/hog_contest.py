"""
Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.

Don't forget: your strategy must be deterministic and pure.
"""
from hog import roll_dice

random_sample_num = 100000

PLAYER_NAME = '' # Change this line!

# maximize probability
# if score < opponent_score:
# 	try to swap or keep low (here is a problem, if swap, then get high or low points?)
# elif score > opponent_score:
# 	try to prevent swap and get high
# all situation: best avoid 0 digits.(free_bacon)
when the point is small, roll the largest
when points over 50, try swap

def n_roll_mean(n, dice = six_sided):
	total = 0
	for i in range(1,random_sample_num):
		total += roll_dice(n, dice) 
	mean = total / (random_sample_num - 1)
	return mean
def best_num_rolls():
	max_points, max_num_rolls = 0, 0
	for i in range(1,11):
		avg_points = n_roll_mean(i)
		if avg_points > max_points:
			max_points,max_num_rolls =  avg_points,i
		elif avg_points == max_points:
		
	
		

def final_strategy(score, opponent_score):
    return 5