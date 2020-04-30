#!/usr/bin/env python3
'''
Cody Ilardo

Programming assignment #3 –Due Sat May 2nd by 11:59pm Choose either the greedy algorithm
or the edge picking algorithm presented in the graph theory part II slides and video.
Write a python program to implement the algorithm you have chosen.  Use the European
flight schedule problem (beginning on slide 32) as the test case graph to
find the “cheapest” solution to the problem.
'''

ref={
    0:"London",
    1:"Berlin",
    2:"Paris",
    3:"Rome",
    4:"Madrid",
    5:"Vienna"
}

cities=[
    [None,325,160,280,250,425],
    [325,None,415,550,675,375],
    [160,415,None,495,215,545],
    [280,550,495,None,380,480],
    [250,675,215,380,None,730],
    [425,375,545,480,730,None]
    ]

visited=[]
price=0

current=cities[0]
visited.append(0)

while len(visited) < len(cities):

    available=[x for x in current if x != None and current.index(x) not in visited]

    index=current.index(min(available))

    price=price+current[index]
    print("${:} flight to {:}".format(current[index], ref[index]))

    current=cities[index]
    visited.append(index)

#'0' hard coded becasue of hard coding a start on '0' when starting, see line 35
print("${:} flight to {:}".format(current[0], ref[0]))
price=price+current[0]

print("${:} Total".format(price))
