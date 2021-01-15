#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2021/1/14


"""
chapter 7 图及其算法

Lecture notes of Artificial intellengence

1. what's is a graph?

A data structure that consist of a set of nodes(vertices顶点) and set of edges that relate the nodes to each other

The set of edges describes relationships among the vertices

2. Mathematical defination:

G = (V,E)   V(G): a finite, nonempty set of vertices E(G): a set of edges(pairs of vertices)

System Objects Interactions

3.
Node degree Ki:  the number of edges adjacent to node i, also the total degree of a node is the sum of in-
and out degree.

4. 有向图 vs 无向图

directed versus undirected graphs

if the graph is directed, the order of the vertices in each edge is important.

5.
Tree vs graph: trees are special cases of graphs, further, trees are special directed graphs.

树与图的关系： 树是一种特殊的有向图

6. terminology of graphs:

Adjacent nodes: two nodes are adjacent if they are connected by an edge

Path: a sequence of vertices that connect two nodes in a graph

Complete graph: a graph in which every vertex is directly connected to every other vertex

7.
The number of edges in a complete undirected graph with N vertices:

N*(N-1)/2  算法复杂度

8.
Weighted graph: a graph in which each edge carries a value

Array-based representation:
A 1D array is used to represent the vertices
A 2D array (adjacency matrix) is used to represent the edges（矩阵不一定是symmetirc的，有点vertices之间是单向的）



9.
链表可用于representation vertices
Linked-list implementation
A 1D array is used to represent the vertices
A list is used for each vertex v which contains the vertices which are adjacent from v (adjacency list)


10.
Graph is topological: it has no shape.

11.
Adjacency matrix vs. adjacency list representation

Adjacency matrix
Good for dense graphs --|E|~O(|V|2)
Memory requirements: O(|V| + |E| ) = O(|V|2 )
Connectivity between two vertices can be tested quickly

Adjacency list
Good for sparse graphs -- |E|~O(|V|)
Memory requirements: O(|V| + |E|)=O(|V|)
Vertices adjacent to another vertex can be found quickly

12. Graph searching:

Problem: find a path between two nodes of the graph (e.g., Austin  and Washington)
Methods: Depth-First-Search (DFS) or Breadth-First-Search (BFS)

-- Depth-First-Search DFS

What is the idea behind DFS?
Travel as far as you can down a path Back up as little as possible when you reach a "dead end"
(i.e.,  next vertex has been "marked" or there is no next vertex)
DFS can be implemented efficiently using a stack

-- Breadth-First-Search BFS

What is the idea behind BFS?
Look at all possible paths at the same depth before you go at a deeper level
Back up as far as possible when you reach a "dead end" (i.e.,  next vertex has been "marked" or there is no next vertex)



13. 算法与数据结构中的

顶点 边 权重
V = [V0,V1,V2,...]
E = [(VO,V1,2),()] 元组，一般是二元组，代表两个adjacent vertices，可以再添加weight，（v1,v2,weight）

path 路径: 是由边连接的顶点组成的序列

环 : 环是有向图中的一条起点和终点为同一个顶点的路径 The start and the final vertices are same.

无环图
有向无环图 DAG

"""

# Python实现图

