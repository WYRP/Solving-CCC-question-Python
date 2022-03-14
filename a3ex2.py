"""
Yongru Pan , 1930194
Friday , April 9th
R. Vincent , instructor
Assignment 3
"""


from bfs import BFS
from graph import digraph

ending_page = []

f=input("File name?") #prompt for file name
fp = open(f) 
v_num = int(fp.readline()) #create a digraph object
G = digraph(v_num) #the content of the file
lines = fp.readlines()
for i in range(len(lines)):
    line_str = lines[i].strip()
    if line_str == '0': #find pages with an outdegree of zero
        ending_page.append(i)
    else:
        for w in line_str.split():
            w = (int(w) - 1) #to make file content
            #fit the format of digraph
            if w != i:
                G.addEdge(i, w)



bfs = BFS(G, 0)#create the BFS object by plugging in the
#digraph object

all_path = []
min_path = 1000
num_min_path = 0

for i in range(1, G.V()):
    if bfs.hasPathTo(i): #to make sure the path for
        #vertex exists
        all_path += bfs.pathTo(i)
        if len(bfs.pathTo(i)) > 0 and bfs.pathTo(i)[-1] in ending_page and bfs.distTo(i) < min_path:
            #make sure the last element is amoung the ending pages.
            min_path = bfs.distTo(i)

for i in range(1, G.V()):
    if bfs.hasPathTo(i):
        if len(bfs.pathTo(i)) == min_path + 1 and bfs.pathTo(i)[-1] in ending_page:
            num_min_path += 1
            #The number of paths of length equal to the shortest path 

print('Y' if set(all_path) == set(range(v_num)) else 'N')
#using set to delete all of the repeated element in all_path
print(min_path + 1) #add 1, for the number of steps do not
#include the root
print(num_min_path) 

max_indegree = -1
max_indegree_index = -1
G = G.reverse() #reverse so that indegree becomes outdegree
#the one with the most outdegree means it has the highest
#indegree in the original function
for i in range(v_num):
    print(G.adj(i))
    if len(G.adj(i)) > max_indegree:
        max_indegree = len(G.adj(i))
        max_indegree_index = i + 1

print(max_indegree_index, max_indegree)
