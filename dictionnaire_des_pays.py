def texte():
    text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts 
    about the Moon and how it affects life here on Earth. On average, the
     Moon moves 4cm away from the Earth every year. This yearly drift is not 
     significant enough to cause immediate effects on Earth. The highest d
     aylight temperature of the Moon is 127 C."""
    paragraphe = text.split('. ')
    print(paragraphe)


def world():
    planet_moons = {
        'mercury': 0,
        'venus': 0,
        'earth': 1,
        'mars': 2,
        'jupiter': 79,
        'saturn': 82,
        'uranus': 27,
        'neptune': 14,
        'pluto': 5,
        'haumea': 2,
        'makemake': 1,
        'eris': 1
    }
    moons = planet_moons.values()
    sum(moons)
    total_planets = len(planet_moons.keys())
    print(moons)
    print(total_planets)


texte()
