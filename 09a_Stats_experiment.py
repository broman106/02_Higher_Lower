# HL component 9a - get game stats to display nicely....

game_stats =[3, 1, 6, 3, 4]

# print game outcomes
print("*** Socre for each round... ***")
list_count = 1
for item in game_stats:
    print("round {}: {}". format(list_count, item))
    list_count += 1

# calculate statistics
game_stats.sort()
best = game_stats[0]
worst = game_stats[-1]
average = sum(game_stats)/len(game_stats)

print()
print("*** summary statistics ***")
print("best: {}".format(best))
print("worst: {}".format(worst))
print("average: {}".format(average))

