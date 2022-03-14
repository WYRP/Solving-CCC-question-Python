"""
Yongru Pan , 1930194
Friday , April 9th
R. Vincent , instructor
Assignment 3
"""
from bfs import BFS
from graph import digraph

ending_page = []

f=input("File name?")#prompt for file name
fp = open(f)
v_num = int(fp.readline())
G = digraph(v_num) #create a digraph object
lines = fp.readlines() #the content of the file
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

bfs = BFS(G, 0) #create the BFS object by plugging in the
#digraph object

all_path = [] 
min_path = 1000 

for i in range(1, G.V()): 
    if bfs.hasPathTo(i): #to make sure the path for
        #vertex exists
        all_path += bfs.pathTo(i) 
        if len(bfs.pathTo(i)) > 0 and bfs.pathTo(i)[-1] in ending_page and bfs.distTo(i) < min_path:
            #make sure the last element is amoung the ending pages.
            min_path = bfs.distTo(i)

print('Yes' if set(all_path) == set(range(v_num)) else 'No')
#using set to delete all of the repeated element in all_path
print(min_path + 1) #add 1, for the number of steps do not
#include the root
