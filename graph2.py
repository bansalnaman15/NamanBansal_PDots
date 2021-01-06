import database as db
import random,string

res = ''.join(random.choices(string.ascii_uppercase+string.digits, k = 4)) 
agraph =f"{res}.sqlite"

db.initialize(agraph)

identity = ['A','B','C','D']

for i,row in enumerate(identity):
    db.atomic(agraph,db.add_node({'name':row},i+1))

db.atomic(agraph, db.connect_nodes(2, 1, {'connected': 'True'}))
db.atomic(agraph, db.connect_nodes(2, 3, {'connected': 'True'}))
db.atomic(agraph, db.connect_nodes(3, 4, {'connected': 'True'}))


print(db.traverse(agraph,2,neighbors_fn=db.find_outbound_neighbors))



