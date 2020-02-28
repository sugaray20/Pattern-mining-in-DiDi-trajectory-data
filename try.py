# -*- coding: utf-8 -*-

import time
import copy

def timmer(func):
    def warpper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('the func run time is %s' %(stop_time-start_time))
    return warpper

@timmer

def nodeToNode(filename): 
    with open(filename) as f:
        line = f.readline()
        count = 0

        while count<=296709:
            line = f.readline()
            line=line.split('\t')
            nodeID.append(line[0])
            latitude.append(float(line[2]))
            longitude.append(float(line[3]))
            neibour_node_number.append(int(line[5]))
            neibour_node.append(line[6:6+2*int(line[5]):2])
            neibour_node_length.append(line[7:6+2*int(line[5]):2])
            count+=1
    f.close()

            
# with open('beijingRoadNewMap') as h:
#     count = 0
#     a={}
#     while count<=387587:
#         road=h.readline()
#         road=road.split('\t',)
#         road1=road[1].split('\n')[0]
#         a[str(road[0])]=str(road1)
#
#         a['-'+road[0]]='-'+str(road1)
#         count+=1
#     h.close()
#
    
def node_start(node):
    index=int(node)
    ready_node[node]=0
    unready.remove(node)
    for i in range(len(neibour_node[index])):
        ready_neighbour[neibour_node[index][i]]=int(neibour_node_length[index][i])

@timmer   
def nodeToNodeCount():
    count=0
    for count in range(219302):
        try:
            min_node=min(ready_neighbour.items(), key=lambda x: x[1])
        except ValueError:
            return ready_neighbour, ready_node
        min_dis=min_node[1]
        min_node=min_node[0]
        ready_node[min_node]=min_dis
        del ready_neighbour[min_node]
        unready.remove(min_node)
        index=int(min_node)
        for i in range(len(neibour_node[index])):
            if neibour_node[index][i] in ready_neighbour:
                try:
                    ready_neighbour[neibour_node[index][i]]=min(int(neibour_node_length[index][i])+min_dis,ready_neighbour[neibour_node[index][i]])
                except ValueError :
                    return ready_neighbour, ready_node
            elif neibour_node[index][i] not in ready_node:
                ready_neighbour[neibour_node[index][i]]=int(neibour_node_length[index][i])+min_dis
    return ready_neighbour, ready_node
    
    

nodeID=[]  
latitude=[]
longitude=[]
neibour_node_number=[]
neibour_node=[]
neibour_node_length=[]


nodeToNode('beijingNodeNew')
unready=copy.copy(nodeID)
unready = { i  for i in unready }

ready_node={}


ready_neighbour={}

node_start('0')

nodeToNodeCount()