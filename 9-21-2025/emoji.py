import random,time

emojis=["😂","😎","🔥","🍕","🐍","🚀","💻","🎮","🌌","🍩"]

for _ in range(25):
    print(random.choice(emojis),end=" ",flush=True)
    time.sleep(0.2)