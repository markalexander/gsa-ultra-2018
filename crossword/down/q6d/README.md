
# 6d. "Alan and Ada"

Ada is excited about directed acyclic graphs (DAGs). Today, she's learning how
to topologically sort a DAG. She has written her own version of the algorithm
(in pseudocode) as follows:

```
 1 // Notes:
 2 // "n" is the number of nodes in the DAG
 3 // "edges" is a tuple denoting the edges in the DAG
 4 // the nodes are indexed 1, 2, ... n.
 5 // "[]" denotes an empty array.
 6 // "{}" denotes an empty set.
 7 // "x.append(v)" appends "v" at the end of array "x".
 8
 9 def TopoSort(n, edges):
10     ans = []        // array which will contain the output
11     in_deg = []     // in_deg[i] denotes the number of incoming edges at node i
12     open_nodes = {} // a set of nodes
13
14     // initialize "in_deg"
15     for i = 0 to n-1:
16         in_deg.append(0)
17
18     for each edge (u -> v) in edges:
19         in_deg[v]++
20
21     // add nodes with indegree 0 to the set
22     for i = 0 to n-1:
23         if in_deg[i] == 0:
24             open_nodes.add(i)
25
26     while open_nodes is not empty:
27         u = random value from set open_nodes
28         remove u from open_nodes
29
30         ans.append(u)
31
32         for each edge (u -> v) that begins at node u:
33             in_deg[v]--
34             if in_deg[v] == 0:
35                 open_nodes.add(v)
36
37     return ans
```

The above algorithm is a randomised algorithm, since in line 27 we introduce
randomness by picking a random element from the set. Because of this, the value
of the `open_nodes` set can be different across different runs of the algorithm
on the same input graph.

Ada's colleague Alan comes along and gives to her a DAG and a set of integers
V = {v_1, v_2, ..., v_k}. He says that he'll run the randomised algorithm once.
Now, he asks Ada to tell him the probability of the `open_nodes` set being equal
to V at any point in the algorithm's execution. Ada argues that calculating this
probability is very difficult, but she can instead tell Alan if the probability
is zero or non-zero.

Write a function that takes a tuple of T test cases as input. Each test case is
a tuple of:

  - An integer N denoting the number of nodes in the graph (1 ≤ N ≤ 10^5)
  - A tuple of M tuples of integers (U, V), each denoting that a directed edge
    from node U to node V exists in the graph (M ≤ 2 × 10^5 and 1 ≤ U,V ≤ N)
  - A tuple of K integers V_1, V_2, ..., V_K denoting the nodes in the set Alan
    has given

Your function should output the integer ∑_{i=0}^{t-1} 2^i * f(i), where f(i) is
1 if the required probability for the i-th index test case is non-zero, else
f(i) is 0. Since the value could be very large, return it modulo 10^9 + 7.

For example, the output of

```
solution((
    (5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 5)),
    (5, ((1, 3), (2, 3), (3, 4), (2, 5), (5, 4)), (1, 2, 5))
))
```

is 2^0 × 1 + 2^1 × 0 = 1. In both test cases the graph has 5 nodes and 5 edges.

For the first test case, the initial value of `open_nodes` is {1, 2}. If node 2
is chosen to be removed, the value of `open_nodes` would be {1, 5}. Hence,
there is a non-zero probability of achieving Alan's value.

For the second test case, the initial value of `open_nodes` is again {1, 2}. The
test case necessitates that nodes 5 and 2 be simultaneously present in
`open_nodes` at some point in the algorithm's execution. But in order for node 5
to be present in `open_nodes`, node 2 would have to be removed. Hence, it's
never possible to achieve Alan's value.
