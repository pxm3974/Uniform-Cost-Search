from sys import argv
from heapq import heappush, heappop

def Graph(Gap, node1, node2, path):   # function to insert each path into the dictionary with in dictionary
    if node1 not in Gap:
        Gap[node1] = {}
    (Gap[node1])[node2] = path
    if node2 not in Gap:
        Gap[node2] = {}
    (Gap[node2])[node1] = path
    return Gap

def Link(connect):     # function to insert the (Source, destination, cost) tuple into the dictionary
    Gap = {}
    for (x,y,z) in connect:
        Graph(Gap,x,y,z)
    return Gap

def uniformCostSearch(graph, s, g):     # Uniform cost search Algorithm implementation
	pq=[]
	#path="distance: infinity \nroute: \nnone"
	visited={}
	prevNode={}
	for key in graph:           # Making the all node still to visited Making it as False
		visited[key]=False
		prevNode[key]=None
	#print visited
	#print prevNode
	entry=(0,s,None,0)
	heappush(pq,entry)       # creating a priority Queue
	while len(pq)!=0:
		(cost,u,pred,originalcost)=heappop(pq)    # using heappop to get the smallest cost node
		if not visited[u]:
			visited[u]=True
			#prevNode[u]={}
			prevNode[u]=[]
			prevNode[u].append(pred)
			prevNode[u].append(originalcost)     #appending visisted node and its original cost
			#(prevNode[u])[pred]=originalcost
			#print prevNode
			if u==g:							    # Condition for Goal State
				ram=ReconstructPath(prevNode,s,g)   # Reconstructing the path after goal state is reached
				#print ram
				ram.reverse()
				sam=[]
				sam.append(cost)
				sam.append(ram)
				return sam
			for neighbour in graph.get(u):     # looking for all the node for goal state
				if not visited[neighbour]:
					#print cost
					rambo=int(graph[u][neighbour])
					#print rambo
					newcost=cost+ int(graph[u][neighbour])
					#print newcost
					entry = (newcost,neighbour, u,rambo)
					#print entry
					heappush(pq,entry)
	return None
				
def ReconstructPath(prevNode, start, goal):    # Reconstructing the path after reaching the Goal State
	#print start, goal
	#print prevNode
	list=[]
	sale=goal
	while (sale!=start):
		for key in prevNode:
				sambu=prevNode[key]
				mini=[]
				#print sambu
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

def main():                          # Main function
	filename=argv[1]
	Source=argv[2]
	Destination=argv[3]
	txt=open(filename)
	#fo = open("input1.txt", "r+")
	list=[];
	while True:
		str=txt.readline()            # Appending entire file into the list
		str=str.replace("\n", "")
		if str.startswith("END OF INPUT"):
			break
		list.append(str)
		#print str
	#print list
	txt.close()

	newlist=[];
	for string in list:         # Appending each (source,destination,cost) string as tuple in new list
		element = string.split()
		atuple=tuple(element)
		newlist.append(atuple)
	#print newlist
	distanceDictionary=Link(newlist)        # Trying to store each tuple as dictionary with in dictionary
	
	cost=uniformCostSearch(distanceDictionary, Source, Destination)    # Uniform Cost Search function call
	
	if cost==None:
		print "distance: infinity \nroute: \nnone"    # Printing the final distance and route
	else:
		print "distance:", cost[0],"km"
		Maya=cost[1]
		print "route:"
		for index in Maya:
			print index[0],"to",index[1],",",index[2],"km"
main()