
# Uniform Cost Search

This program compute a route between the origin city and the destination city and will print out both the length of the route and the list of all cities that lie on that route. 

For example, command line argument, 

find_route.py input1.txt Bremen Frankfurt

prints following:

distance: 455 km
route: 
Bremen to Dortmund, 234 km
Dortmund to Frankfurt, 221 km

Arguments description:

find_route: Main python file
input1.txt: input file
Bremen: source city
Frankfurt: destination city


Main File description


```python
from sys import argv
from heapq import heappush, heappop
```

Three commandline arguments are stored.


```python
def main():                          
    filename=argv[1]
    Source=argv[2]
    Destination=argv[3]
    txt=open(filename)
```

File data are stored in the list.


```python
list=[];
while True:
    str=txt.readline()            
    str=str.replace("\n", "")
    if str.startswith("END OF INPUT"):
        break
    list.append(str)
    txt.close()
```

Appending each (source,destination,cost) string as tuple in new list.


```python
newlist=[];
for string in list:         
    element = string.split()
    atuple=tuple(element)
    newlist.append(atuple)
```


```python
distanceDictionary=Link(newlist)        # Trying to store each tuple as dictionary with in dictionary

cost=uniformCostSearch(distanceDictionary, Source, Destination)    # Uniform Cost Search function call
```


```python
if cost==None:
    print "distance: infinity \nroute: \nnone"    # Printing the final distance and route
else:
    print "distance:", cost[0],"km"
    Maya=cost[1]
    print "route:"
    for index in Maya:
        print index[0],"to",index[1],",",index[2],"km"
main()
```

Additional functions are described below:


```python
def Graph(Gap, node1, node2, path):   # function to insert each path into the dictionary with in dictionary
    if node1 not in Gap:
        Gap[node1] = {}
    (Gap[node1])[node2] = path
    if node2 not in Gap:
        Gap[node2] = {}
    (Gap[node2])[node1] = path
    return Gap
```


```python
def Link(connect):     # function to insert the (Source, destination, cost) tuple into the dictionary
    Gap = {}
    for (x,y,z) in connect:
        Graph(Gap,x,y,z)
    return Gap
```


```python
def uniformCostSearch(graph, s, g):     # Uniform cost search Algorithm implementation
    pq=[]
    visited={}
    prevNode={}
    for key in graph:           # Making the all node still to visited Making it as False
        visited[key]=False
        prevNode[key]=None
    entry=(0,s,None,0)
    heappush(pq,entry)       # creating a priority Queue
    while len(pq)!=0:
        (cost,u,pred,originalcost)=heappop(pq)    # using heappop to get the smallest cost node
        if not visited[u]:
            visited[u]=True
            prevNode[u]=[]
            prevNode[u].append(pred)
            prevNode[u].append(originalcost)     #appending visisted node and its original cost
            if u==g:                      # Condition for Goal State
                ram=ReconstructPath(prevNode,s,g)   # Reconstructing the path after goal state is reached
                ram.reverse()
                sam=[]
                sam.append(cost)
                sam.append(ram)
                return sam
            for neighbour in graph.get(u):     # looking for all the node for goal state
                if not visited[neighbour]:
                    rambo=int(graph[u][neighbour])
                    newcost=cost+ int(graph[u][neighbour])
                    entry = (newcost,neighbour, u,rambo)
                    heappush(pq,entry)
    return None
```


```python
def ReconstructPath(prevNode, start, goal):    # Reconstructing the path after reaching the Goal State
    list=[]
    sale=goal
    while (sale!=start):
        for key in prevNode:
            sambu=prevNode[key]
            mini=[]
            if sambu!=None and key==goal:   # Back tracing the path using the goal state as key
                sale=prevNode[key][0]
                cost=prevNode[key][1]
                mini.append(sale)
                mini.append(key)
                mini.append(cost)
                list.append(mini)
                prevNode[key]=None
                if sale==start:
                    return list
                    break
                goal=sale
```

INPUT FILE:
    
Luebeck Hamburg 63
Hamburg Bremen 116
Hamburg Hannover 153
Hamburg Berlin 291
Bremen Hannover 132
Bremen Dortmund 234
Hannover Magdeburg 148
Hannover Kassel 165
Magdeburg Berlin 166
Berlin Dresden 204
Dresden Leipzig 119
Leipzig Magdeburg 125
Dortmund Duesseldorf 69
Kassel Frankfurt 185
Frankfurt Dortmund 221
Frankfurt Nuremberg 222
Leipzig Nuremberg 263
Dortmund Saarbruecken 350
Saarbruecken Frankfurt 177
Saarbruecken Karlsruhe 143
Karlsruhe Stuttgart 71
Stuttgart Frankfurt 200
Stuttgart Munich 215
Stuttgart Nuremberg 207
Nuremberg Munich 171
Manchester Birmingham 84
Birmingham Bristol 85
Birmingham London 117
END OF INPUT
