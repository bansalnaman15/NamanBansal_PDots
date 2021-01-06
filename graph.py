import database as db

agraph ="agraph.sqlite"
db.initialize(agraph)

identity = [chr(x+65) for x in range (9)]

raw = [
    [0,1,1,0,1,0,1,0,1],
    [1,0,0,0,1,1,0,1,0],
    [1,0,0,0,1,1,1,0,1],
    [1,1,1,0,1,0,1,1,0],
    [0,1,0,0,0,1,0,1,0],
    [1,0,0,0,0,0,1,1,0],
    [0,0,0,1,0,0,0,0,0],
    [1,0,1,1,1,1,0,0,1],
    [1,1,1,1,0,0,0,0,0]
]

for i,row in enumerate(raw):
    # print(identity[i])
    for j,element in enumerate(row):
        print(identity[i], f" --> {element} --> ",identity[j])



