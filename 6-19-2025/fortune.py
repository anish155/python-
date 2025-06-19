import random

high = ['light', 'sun', 'fire', 'beam', 'gale']
mid = ['wave', 'enigma', 'lava', 'jolt', 'flare']
low = ['thunder', 'void', 'venom', 'snake', 'leech']

# Combine all into one pool
all_words = high + mid + low

# Pick 3 random words
reading = random.sample(all_words, 3)

# Count how many are from each category
high_count = sum(1 for word in reading if word in high)
mid_count = sum(1 for word in reading if word in mid)
low_count = sum(1 for word in reading if word in low)

# Determine fortune
if high_count == 3:
    fortune = "🌟 Ultimate Fortune! Everything will align for you."
elif high_count == 2:
    fortune = "✨ Great Fortune! Success is very likely."
elif high_count == 1:
    if mid_count == 2:
        fortune = "🙂 Balanced Path. Moderate luck with opportunities."
    else:
        fortune = "👍 Fortune. A spark of greatness is with you."
elif mid_count == 3:
    fortune = "🌀 Uncertain Tide. You may face confusion, but not failure."
elif mid_count == 2:
    fortune = "🌫️ Cloudy Vision. Things are unclear—take care."
elif mid_count == 1:
    fortune = "⚠️ Shaky Grounds. Tread carefully today."
else:  # low_count == 3
    fortune = "☠️ Dire Omen. Be cautious in all that you do."

# Show reading and fortune
print("Your reading:")
print(" - " + ", ".join(reading))
print("Interpretation:")
print(fortune)


