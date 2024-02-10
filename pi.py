text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
i = text.replace(",","").replace(".","").split()
i = list(map(len,i))
i = ''.join(map(str, i))
print(i)