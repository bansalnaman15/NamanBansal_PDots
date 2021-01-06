import database as db
import shutil,os

def getNodeNumber(row,col):
    return row+1,col+1

def addConnection(element,r,c):
    if i==j:
        return
    # print(element)
    if element==1:
        print(element,r,c)
        db.atomic(agraph,db.connect_nodes(r+1,c+1,{"connected":True}))
        print("Connected",identity[r], f" --> {element} --> ",identity[c])


if os.path.exists('agraph.sqlite'):
    os.remove("agraph.sqlite")

agraph ="agraph.sqlite"
db.initialize(agraph)

identity = [chr(x+65) for x in range (3)]

# raw = (
#     (0,1,1,0,1,0,1,0,1),
#     (1,1,0,0,1,1,0,1,0),
#     (1,0,0,0,1,1,1,0,1),
#     (1,1,1,0,1,0,1,1,0),
#     (0,1,0,0,1,1,0,1,0),
#     (1,0,0,0,0,1,1,1,0),
#     (0,0,0,1,0,0,1,0,0),
#     (1,0,1,1,1,1,0,0,1),
#     (1,1,1,1,0,0,0,0,1),
# )

# print(raw)

for i,row in enumerate(identity):
    db.atomic(agraph,db.add_node({'name':row},i+1))




# for i,row in enumerate(raw):
#     print(row)
#     for j,element in enumerate(row):
#         addConnection(element,i,j)

    

# print(db.traverse(agraph,1,neighbors_fn=db.find_neighbors))


# db.visualize(agraph, 'apple.dot', [1])