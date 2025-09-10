import random 
zodiac_fortunes = {
    "Aries": [
        "Today is a great day to start something new.",
        "Your energy will attract positive opportunities.",
        "Take the lead, but listen to advice from others."
    ],
    "Taurus": [
        "Patience will bring you great rewards.",
        "You may find comfort in familiar surroundings.",
        "Financial opportunities may come your way."
    ],
    "Gemini": [
        "Communication is key today.",
        "A new idea may inspire your next move.",
        "Keep an open mind and embrace change."
    ],
    "Cancer": [
        "Trust your intuition in personal matters.",
        "Family and friends bring unexpected joy.",
        "Your nurturing nature will be appreciated today."
    ],
    "Leo": [
        "Your confidence will shine brightly.",
        "Take pride in your accomplishments.",
        "A new adventure awaits—embrace it!"
    ],
    "Virgo": [
        "Attention to detail will pay off today.",
        "Helping others may bring unexpected rewards.",
        "Stay organized and focused on your goals."
    ],
    "Libra": [
        "Seek balance in your relationships.",
        "A harmonious day is ahead.",
        "Your diplomacy will resolve conflicts."
    ],
    "Scorpio": [
        "Embrace transformation and growth.",
        "Your passion will inspire those around you.",
        "Secrets may be revealed—stay calm."
    ],
    "Sagittarius": [
        "Adventure calls, go explore.",
        "Your optimism will attract new opportunities.",
        "Learning something new will bring joy."
    ],
    "Capricorn": [
        "Hard work leads to success.",
        "Be patient and persistent.",
        "Your ambition will inspire others."
    ],
    "Aquarius": [
        "Innovation and creativity are your allies.",
        "Connect with like-minded individuals.",
        "Your uniqueness will be celebrated today."
    ],
    "Pisces": [
        "Follow your dreams and intuition.",
        "Creativity flows easily today.",
        "Empathy and kindness will be rewarded."
    ]
}
zodiac=input("Enter your zodiac sign:")
if zodiac in zodiac_fortunes:
    print(random.choice(zodiac_fortunes[zodiac]))
else:
    print("Please enter valid zodiac sign.")