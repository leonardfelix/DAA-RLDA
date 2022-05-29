from random import randint, random


class vertex():
    def __init__(self, name):
        self.name = name
        self.successor = set()
        self.predecessor = set()


valueNode = int(input("how many nodes"))
i = 0
dictio = {}
while i<valueNode:
    dictio[str(i)] = vertex(str(i))
    i += 1

#variables
thisVertexCollection = []
edgeValues = {}
intersectionValues = {}

for src in range(valueNode):
    for dst in range(valueNode):
        
        source = str(src)
        destination = str(dst)
        # set on source vertex
        thisSourceVertex = dictio[source]
        thisSourceVertex.successor.add(destination)
        dictio[source] = thisSourceVertex

        #set on dest vertext
        thisDestVertex = dictio[destination]
        thisDestVertex.predecessor.add(source)
        dictio[destination] = thisDestVertex


        edgeValues[source + "_" + destination] = randint(1,25)

        for prepredecessor in thisSourceVertex.predecessor:
            intersectionValues[prepredecessor +"_" + thisSourceVertex.name + "_" + thisDestVertex.name] = randint(0,25)

        for sucsuccessor in thisDestVertex.successor:
            intersectionValues[thisSourceVertex.name + "_" + thisDestVertex.name + "_" + sucsuccessor] = randint(0,25)



    
resultString = "thisVertexCollection = [" 
for key in dictio:
    successor = dictio[key].successor 
    if successor == set():
        successor = "[]"

    predecessor = dictio[key].predecessor 
    if predecessor == set():
        predecessor = "[]"

    resultString += str(f"vertex({predecessor},{successor},'{key}'),")

resultString += "]"
resultString = resultString.replace("{","[")
resultString = resultString.replace("}","]")
minimumEdgeData ={}
for key in edgeValues:
    minimumEdgeData[key] = 0


f = open("generator result.txt", "w")
f.write(resultString)
f.write("\n Edge values \n")
f.write(str(edgeValues))
f.write("\n intersection values \n")
f.write(str(intersectionValues))
f.write("\n edge data \n")
f.write(str(minimumEdgeData))
f.close()
