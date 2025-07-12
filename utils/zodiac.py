from datetime import datetime

ZODIAC_SIGNS = [
    ("Capricorn",  (1, 1),   (1, 19)),
    ("Aquarius",   (1, 20),  (2, 18)),
    ("Pisces",     (2, 19),  (3, 20)),
    ("Aries",      (3, 21),  (4, 19)),
    ("Taurus",     (4, 20),  (5, 20)),
    ("Gemini",     (5, 21),  (6, 20)),
    ("Cancer",     (6, 21),  (7, 22)),
    ("Leo",        (7, 23),  (8, 22)),
    ("Virgo",      (8, 23),  (9, 22)),
    ("Libra",      (9, 23),  (10, 22)),
    ("Scorpio",    (10, 23), (11, 21)),
    ("Sagittarius",(11, 22), (12, 21)),
    ("Capricorn",  (12, 22), (12, 31)),
]

ZODIAC_COMPATIBILITY = {
    "Aries":       ["Leo", "Sagittarius", "Gemini"],
    "Taurus":      ["Virgo", "Capricorn", "Cancer"],
    "Gemini":      ["Libra", "Aquarius", "Aries"],
    "Cancer":      ["Pisces", "Scorpio", "Taurus"],
    "Leo":         ["Aries", "Gemini", "Sagittarius"],
    "Virgo":       ["Taurus", "Capricorn", "Cancer"],
    "Libra":       ["Gemini", "Leo", "Aquarius"],
    "Scorpio":     ["Cancer", "Pisces", "Virgo"],
    "Sagittarius": ["Aries", "Leo", "Aquarius"],
    "Capricorn":   ["Taurus", "Virgo", "Scorpio"],
    "Aquarius":    ["Libra", "Gemini", "Sagittarius"],
    "Pisces":      ["Cancer", "Scorpio", "Capricorn"]
}

def get_zodiac_sign(day: int, month: int) -> str:
    for sign, start, end in ZODIAC_SIGNS:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            return sign
    return "Unknown"

def signs_are_compatible(sign1, sign2):
    return sign2 in ZODIAC_COMPATIBILITY.get(sign1, [])
