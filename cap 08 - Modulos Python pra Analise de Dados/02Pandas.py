import pandas as pd

data = {
    "Estado":["SC", "SP", "PR"],
    "Ano":[2002, 2003, 2004],
    "População": [1.5, 10.5, 3.9]
}

frame = pd.DataFrame(data)

print(frame)