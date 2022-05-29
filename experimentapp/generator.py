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

valueEdge = int(input("how many edge(max, maybe less who knows :))"))
j = 0
iteratedEdge = set()
while j<int(valueEdge):
    
    
    source = str(randint(0,valueNode-1))
    destination = source
    while destination == source:
        destination = str(randint(0,valueNode-1))

    sourcedestuple = (source,destination)

    while sourcedestuple in iteratedEdge: 
        source = str(randint(0,valueNode-1))
        destination = source
        while destination == source:
            destination = str(randint(0,valueNode-1))

        sourcedestuple = (source,destination)

    iteratedEdge.add(sourcedestuple)

    # set on source vertex
    thisSourceVertex = dictio[source]
    thisSourceVertex.successor.add(destination)
    dictio[source] = thisSourceVertex

    #set on dest vertext
    thisDestVertex = dictio[destination]
    thisDestVertex.predecessor.add(source)
    dictio[destination] = thisDestVertex

    thisVertexCollection.append(j)

    edgeValues[source + "_" + destination] = randint(1,25)

    for prepredecessor in thisSourceVertex.predecessor:
        intersectionValues[prepredecessor +"_" + thisSourceVertex.name + "_" + thisDestVertex.name] = randint(0,25)

    for sucsuccessor in thisDestVertex.successor:
        intersectionValues[thisSourceVertex.name + "_" + thisDestVertex.name + "_" + sucsuccessor] = randint(0,25)


    j+=1
    
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
