f = open("input/day07.txt").readlines()
# convert the problem to a simple string sort
key = dict(zip("A K Q J T 9 8 7 6 5 4 3 2".split(),
               "a b c d e f g h i j k l m".split()))

for useJoker in [False, True]:
    bids = {}
    if useJoker: key['J']='z' # demote J value to lowest

    for line in f:
        hand, bid = line.split()
        counts, rank = {}, 7 # default rank is lowest
        for card in hand.replace('J', '' if useJoker else 'J'):
            counts[card] = hand.count(card)
        counts = sorted(counts.values(), reverse=True)+[0] # append 0 for tricky JJJJJ case
        if useJoker: counts[0] += hand.count('J')
        if counts[0] == 5: rank = 1
        if counts[0] == 4: rank = 2
        if counts[0] == 3: rank = 3 if counts[1]==2 else 4
        if counts[0] == 2: rank = 5 if counts[1]==2 else 6
        bids[str(rank)+''.join([key[c] for c in hand])] = int(bid)

    score = 0
    for i, hand in enumerate(sorted(bids.keys(), reverse=True), 1):
        score += bids[hand]*i
    print(score)