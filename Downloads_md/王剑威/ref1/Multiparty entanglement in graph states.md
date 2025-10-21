# Multiparty entanglement in graph states

M. Hein, $^{1,2}$  J. Eisert, $^{3,4}$  and H. J. Briegel $^{1,2,5}$

<sup>1</sup>Theoretische Physik, Ludwig-Maximilians-Universität, Theresienstraße 37, D-80333 München, Germany

$^{2}$ Institut für Theoretische Physik, Universität Innsbruck, Technikerstraße 25, A-6020 Innsbruck, Austria

$^{3}$ Institut für Physik, Universität Potsdam, Am Neuen Palais 10, D-14469 Potsdam, Germany

$^{4}$ Blackett Laboratory, Imperial College London, Prince Consort Road, London SW7 2BW, United Kingdom

$^{5}$ Institute for Quantum Optics and Quantum Information of the Austrian Academy of Sciences, A-6020 Innsbruck, Austria

(Received 19 September 2003; revised manuscript received 2 February 2004; published 9 June 2004)

Graph states are multiparticle entangled states that correspond to mathematical graphs, where the vertices of the graph take the role of quantum spin systems and edges represent Ising interactions. They are many-body spin states of distributed quantum systems that play a significant role in quantum error correction, multiparty quantum communication, and quantum computation within the framework of the one-way quantum computer. We characterize and quantify the genuine multiparticle entanglement of such graph states in terms of the Schmidt measure, to which we provide upper and lower bounds in graph theoretical terms. Several examples and classes of graphs will be discussed, where these bounds coincide. These examples include trees, cluster states of different dimensions, graphs that occur in quantum error correction, such as the concatenated [7,1,3]-CSS code, and a graph associated with the quantum Fourier transform in the one-way computer. We also present general transformation rules for graphs when local Pauli measurements are applied, and give criteria for the equivalence of two graphs up to local unitary transformations, employing the stabilizer formalism. For graphs of up to seven vertices we provide complete characterization modulo local unitary transformations and graph isomorphisms.

DOI: 10.1103/PhysRevA.69.062311

PACS number(s): 03.67.-a, 42.50.-p, 03.65.Ud

# I. INTRODUCTION

In multipartite quantum systems one can in many cases identify constituents that directly interact with each other, whereas other interactions play a minor role and can largely be neglected. For example, next-neighbor interactions in coupled systems are often by far dominant. Such quantum systems may be represented by a graph [1,2], where the vertices correspond to the physical systems and the edges represent interactions. The concept of a graph state—which abstracts from the actual realization in a physical system—is based on this intuition.

A graph state, as it is used in this paper, is a special pure multiparty quantum state of a distributed quantum system. It corresponds to a graph in that each edge represents an Ising interaction between pairs of quantum spin systems or qubits [3-6]. Special instances of graph states are codewords of various quantum error correcting codes [7], which are of central importance when protecting quantum states against decoherence in quantum computation [8]. Other examples are multiparty Greenberger-Horne-Zeilinger (GHZ) states with applications in quantum communication, or cluster states of arbitrary dimensions, which are known to serve as a universal resource for quantum computation in the one-way quantum computer [9,10]. Yet, not only the cluster state itself is a graph state, but also a pure state that is obtained from this universal resource after the appropriate steps have been taken to implement operations taken from the Clifford group. This resource is then no longer universal, but the specific resource for a particular quantum computation [3].

In this paper we address the issue of quantifying and characterizing the entanglement of these multiparticle entangled states of an arbitrary number of constituents. The aim is to

apply the quantitative theory of multiparticle entanglement to the study of correlations in graph states. The underlying measure of entanglement is taken to be the Schmidt measure [11], which is a proper multiparticle entanglement monotone that is tailored to the characterization of such states. As holds true for any known measure of multiparticle entanglement, its computation is exceedingly difficult for general states, yet for graph states this task becomes feasible to a very high extent. We start by presenting general transformation rules of graphs when local Pauli measurements are applied locally on physical systems represented by vertices. We present various upper and lower bounds for the Schmidt measure in graph theoretical terms, which largely draw from the stabilizer theory. These bounds allow for an evaluation of the Schmidt measure for a large number of graphs of practical importance. We discuss these rules for the class of 2-colorable graphs, which is of special practical importance in the context of entanglement purification [5]. For this class we give bounds to the Schmidt measure, that are particularly easy to compute. Moreover, we provide criteria for the equivalence of graph states under local unitary transformations entirely on the level of the underlying graphs. Finally, we present several examples, including trees, cluster states, states that occur in the context of quantum error correction, such as the CSS code, and the graph that is used to realize the QFT on three qubits in the one-way quantum computer. The vision behind this is to flesh out the notion of entanglement as an algorithmic resource, as it has been put forward in Ref. [3].

The paper is structured as follows. We start by introducing the notion of graph states of multiqubit systems: we set the notation concerning graph theoretical terms, and proceed by showing how graph states are in correspondence to graphs. Then, we recapitulate relevant properties of the Schmidt

measure as a measure of multiparticle entanglement. In Sec. III we then state the general upper and lower bounds that are formulated in the language of graph theory. We also investigate the equivalence class for connected graphs up to seven vertices under local unitaries and graph isomorphisms. These statements are the main results of the paper. They are proved in Sec. IV. We proceed by discussing the above mentioned examples, where we use the developed methods. Finally, we summarize what has been achieved, and sketch further interesting steps of future research.

This paper is concerned with entanglement in multipartite distributed quantum systems, with some resemblance to Refs. [13-20]. However, here we are less interested in the connection between quantum correlations and quantum phase transition, but rather in the entanglement of graph states that have definite applications in quantum information theory. Entangled states associated with graphs have also been studied in Refs. [19,21-23], where bounds on shared bipartite entanglement in multipartite quantum systems have been studied, in order to find general rules for sharing of entanglement in a multipartite setting. It should, however, be noted that the way in which we represent entangled states by mathematical graphs is entirely different from the way this is done in Refs. [19,21-23]. Furthermore, in the present paper, we are not only concerned with bipartite entanglement between two constituents or two groups of constituents, but with multipartite entanglement between many constituents. In turn, the interaction that gives rise to the entangled graph states is more specific, namely the one corresponding to an Ising interaction. Finally, as discussed above, graph states provide an interesting class of genuine multipartite entangled states that are relatively easy to survey even in the regime of many parties. Since the graph essentially encodes a preparation procedure of the state, we will mainly examine the question of how the entanglement in a graph state is related to the topology of its underlying graph.

# II. GRAPHS, GRAPH STATES, AND THE SCHMIDT MEASURE

# A. Graphs

At the basis of our analysis lies the concept of a graph [1,2]. A graph is a collection of vertices and a description of which vertices are connected by an edge. Each graph can be represented by a diagram in a plane, where each vertex is represented by a point and each edge by an arc joining two not necessarily distinct vertices. In this pictorial representation many concepts related to graphs can be visualized in a transparent manner. In the context of the present paper, physical systems will take the role of vertices, whereas edges represent an interaction.

Formally, an (undirected, finite) graph is a pair

$$
G = (V, E) \tag {1}
$$

of a finite set  $V \subset \mathbb{N}$  and a set  $E \subset [V]^2$ , the elements of which are subsets of  $V$  with two elements each [1]. The elements of  $V$  are called vertices, the elements of  $E$  edges. In the following we will only consider simple graphs, which are graphs

that contain neither loops (edges connecting vertices with itself) nor multiple edges.

When the vertices  $a, b \in V$  are the endpoints of an edge, they are referred to as being adjacent. The adjacency relation gives rise to an adjacency matrix  $\Gamma_G$  associated with a graph. If  $V = \{a_1, \ldots, a_N\}$ , then  $\Gamma_G$  is a symmetric  $N \times N$  matrix, with elements

$$
\left(\Gamma_ {G}\right) _ {i j} = \left\{ \begin{array}{l l} 1 & \text {i f} \left\{a _ {i}, a _ {j} \right\} \in E, \\ 0 & \text {o t h e r w i s e .} \end{array} \right. \tag {2}
$$

We will make repeated use of the neighborhood of a given vertex  $a \in V$ . This neighborhood  $N_a \subset V$  is defined as the set of vertices  $b$  for which  $\{a, b\} \in E$ . In other words, the neighborhood is the set of vertices adjacent to a given vertex. A vertex  $a \in V$  with an empty neighborhood will be called isolated vertex.

For the purpose of later use, we will also introduce the concept of a connected graph. An  $\{a,b\}$  path is an ordered list of vertices  $a = a_{1},a_{2},\ldots ,a_{n - 1},a_{n = b}$ , such that for all  $i$ ,  $a_{i}$  and  $a_{i + 1}$  are adjacent. A connected graph is a graph that has an  $\{a,b\}$  path for any two  $a,b\in V$ . Otherwise it is referred to as disconnected.

When a vertex  $a$  is deleted in a graph, together with the edges incident with  $a$ , one obtains a new graph. For a subset of vertices  $V' \subset V$  of a graph  $G = (V, E)$ , let us denote with  $G - V'$  the graph that is obtained from  $G$  by deleting the set  $V'$  of vertices and all edges which are incident with an element of  $V'$ . In a mild abuse of notation, we will also write  $G - E'$  for the graph that results from a deletion of all edges  $e \in E'$ , where  $E' \subset E \subset [V]^2$  is a set of edges. For a set of edges  $F \subset [V]^2$  we will write  $G + F = (V, E \cup F)$ , and  $G \Delta F = (V, E \Delta F)$ , where

$$
E \Delta F = (E \cup F) - (E \cap F) \tag {3}
$$

is the symmetric difference of  $E$  and  $F$ . Note that the symmetric difference corresponds to the addition modulo 2 or the componentwise XOR, if the sets are considered as binary vectors. Moreover, with

$$
E (A, B) = \{\{a, b \} \in E: a \in A, b \in B, a \neq b \}, \tag {4}
$$

we denote the set of edges between sets  $A, B \subset V$  of vertices.

# B. Graph states

With each graph  $G = (V, E)$  we associate a graph state. A graph state is a certain pure quantum state on a Hilbert space  $\mathcal{H}_V = (\mathbb{C}^2)^{\otimes V}$ . Hence each vertex labels a two-level quantum system or qubit—a notion that can be extended to quantum systems of finite dimension  $d$  [4]. To every vertex  $a \in V$  of the graph  $G = (V, E)$  is attached a Hermitian operator,

$$
K _ {G} ^ {(a)} = \sigma_ {x} ^ {(a)} \prod_ {b \in N _ {a}} \sigma_ {z} ^ {(b)}. \tag {5}
$$

In terms of the adjacency matrix this can be expressed as

$$
K _ {G} ^ {(a)} = \sigma_ {x} ^ {(a)} \prod_ {b \in V} \left(\sigma_ {z} ^ {(b)}\right) ^ {\Gamma_ {a b}}. \tag {6}
$$

As usual, the matrices  $\sigma_x^{(a)},\sigma_y^{(a)},\sigma_z^{(a)}$  are the Pauli matrices, where the upper index specifies the Hilbert space on which the operator acts.  $K_{G}^{(a)}$  is an observable of the qubits associated with the vertex  $a$  and all of its neighbors  $b\in N_a$ . The  $N = |V|$  operators  $\{K_G^{(a)}\}_{a\in V}$  are independent and they commute.

Using standard terminology of quantum mechanics, they define a complete set of commuting observables of the system of qubits associated with the vertex set  $V$  (that they commute can be found immediately by direct inspection, in order to demonstrate completeness the argument of Ref. [3] may be used). They thus have a common set of eigenvectors, the graph states [3,5,7], which form a basis of the Hilbert space  $\mathcal{H}_V$ . For our present purposes, it is sufficient to choose one of these eigenvectors as a representative of all graph states associated with  $G$ . We denote by  $|G\rangle$  the common eigenvector of the  $K_G^{(a)}$  associated with all eigenvalues equal to unity, i.e.,

$$
K _ {G} ^ {(a)} | G \rangle = | G \rangle \tag {7}
$$

for all  $a \in V$ . Note that any other common eigenvector of the set  $K_G^{(a)}$  with some eigenvalues being negative are obtained from  $|G\rangle$  by simply applying appropriate  $\sigma_z$  transformations at those vertices  $a$ , for which  $K_G^{(a)}$  gives a negative eigenvalue. In the context of quantum information theory, the finite Abelian group,

$$
S _ {G} = \left\langle \left\{K _ {G} ^ {(a)} \right\} _ {a \in V} \right\rangle , \tag {8}
$$

generated by the set  $\{K_G^{(a)}\}_{a\in V}$  is also called the stabilizer [8] of the graph state vector  $|G\rangle$ . If the number of independent operators in  $S_{G}$  is less than  $|V|$ , then the common eigenspaces are degenerate and can, for certain graphs  $G$ , be used as quantum error correcting codes, the so-called graph codes [7]. In this case  $G$  also describes a certain encoding procedure.

The graph state vector  $|G\rangle$  can also be obtained by applying a sequence of commuting unitary two-qubit operations  $U^{(a,b)}$  to the state vector  $|x, + \rangle^{\otimes V}$  corresponding to the empty graph:

$$
| G \rangle = \prod_ {(a, b) \in E} U ^ {\{a, b \}} | x, + \rangle^ {\otimes V}, \tag {9}
$$

where  $E$  denotes the set of edges in  $G$ , and  $|x, + \rangle$  is the eigenvector of  $\sigma_{x}$  with eigenvalue  $+1$ . The unitary two-qubit operation on the vertices  $a,b$ , which adds or removes the edge  $\{a,b\}$ , is given by

$$
U ^ {(a, b)} = P _ {z, +} ^ {(a)} \otimes 1 ^ {(b)} + P _ {z, -} ^ {(a)} \otimes \sigma_ {z} ^ {(b)} = U ^ {(a, b) \dagger}, \tag {10}
$$

and is simply a controlled  $\sigma_z$  on qubits  $a$  and  $b$ , i.e.,

$$
U ^ {(a, b)} \dot {=} \left( \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & - 1 \end{array} \right).
$$

Here,

$$
P _ {z, \pm} ^ {(a)} = \frac {1 \pm \sigma_ {z} ^ {(a)}}{2} \tag {11}
$$

denotes the projector onto the eigenvector  $|z,\pm \rangle$  of  $\sigma_z^{(a)}$  with eigenvalue  $\pm 1$  (similarly for  $\sigma_x^{(a)}$  and  $\sigma_y^{(a)}$ ).  $U^{(a,b)}$  as in Eq. (10) is the unitary two-qubit operation which removes or adds the edges. This is easily seen by noting that for  $c\in V - \{a,b\}$ ,  $K_G^{(c)}$  commutes with  $U^{(a,b)}$ , whereas

$$
U ^ {(a, b)} K _ {G} ^ {(a)} U ^ {(a, b) \dagger} = U ^ {(a, b)} \left(P _ {z, -} ^ {(a)} + P _ {z, +} ^ {(a)} \sigma_ {z} ^ {(b)}\right) K _ {G} ^ {(a)} = \sigma_ {z} ^ {(b)} K _ {G} ^ {(a)}, \tag {12}
$$

because of  $\sigma_{x}P_{z,\pm} = P_{z,\mp}\sigma_{x}$ . Since  $U^{(a,b)} = U^{(b,a)}$ , similarly

$$
U ^ {(a, b)} K _ {G} ^ {(b)} U ^ {(a, b) \dagger} = \sigma_ {z} ^ {(a)} K _ {G} ^ {(b)} \tag {13}
$$

holds, so that the transformed stabilizer corresponds to a graph  $G'$ , where the edge  $\{a, b\}$  is added modulo 2. Up to the local unitary  $\sigma_z^{(b)}$ , this corresponds to the Ising interaction.

An equivalence relation for graphs is inherited by the corresponding equivalence of state vectors. We will call two graphs  $G = (V, E)$  and  $G' = (V, E')$  LU-equivalent, if there exists a local unitary  $U$  such that

$$
| G \rangle = U | G ^ {\prime} \rangle . \tag {14}
$$

Locality here refers to the systems associated with vertices of  $G = (V, E)$  and  $G' = (V, E')$ . Note that LU equivalence is different from equivalence of graphs in the graph theoretical sense, i.e., permutations of the vertices that map neighbored vertices onto neighbored vertices.

# C. Schmidt measure

Graph states are entangled quantum states that exhibit complex structures of genuine multiparticle entanglement. It is the purpose of the present paper to characterize and quantify the entanglement present in these states that can be represented as graphs. Needless to say, despite considerable research effort there is no known computable entanglement measure that grasps all aspects of multiparticle entanglement in an appropriate manner, if there is any way to fill such a phrase with meaning. Several entanglement measures for multiparticle systems have been suggested and their properties studied [11,24-28].

We will, for the purposes of the present paper, use a measure of entanglement that is tailored for characterizing the degree of entanglement present in graph states: this is the Schmidt measure, as introduced in Ref. [11]. Any state vector  $|\psi \rangle \in \mathcal{H}^{(1)}\otimes \dots \otimes \mathcal{H}^{(N)}$  of a composite quantum system with  $N$  components can be represented as

$$
\left| \psi \right\rangle = \sum_ {i = 1} ^ {R} \xi_ {i} \left| \psi_ {i} ^ {(1)} \right\rangle \otimes \dots \otimes \left| \psi_ {i} ^ {(N)} \right\rangle , \tag {15}
$$

where  $\xi_{i}\in \mathbb{C}$  for  $i = 1,\dots ,R$  and  $\left|\psi_i^{(n)}\right\rangle \in \mathcal{H}^{(n)}$  for  $n$ $= 1,\ldots ,N.$  The Schmidt measure associated with a state vector  $|\psi \rangle$  is then defined as

$$
E _ {S} (| \psi \rangle) = \log_ {2} (r), \tag {16}
$$

where  $r$  is the minimal number  $R$  of terms in the sum of Eq. (15) over all linear decompositions into product states. It can be extended to the entire state space (and not only the extreme points) via a convex roof extension. This paper will merely be concerned with pure states. More specifically, we will evaluate the Schmidt measure for graph states only. It should be noted, however, that the Schmidt measure is a general entanglement monotone with respect to general local operations and classical communication (LOCC), which typically leave the set of graph states.

In the multipartite case it is useful to compare the Schmidt measure according to different partitionings, where the components  $1,\ldots ,N$  are grouped into disjoint sets. Any sequence  $(A_{1},\dots ,A_{N})$  of disjoint subsets  $A_{i}\subset V$  with  $\cup_{i = 1}^{N}A_{i}$ $= \{1,\dots ,N\}$  will be called a partition of  $V$ . We will write

$$
\left(A _ {1}, \dots A _ {N}\right) \leqslant \left(B _ {1}, \dots , B _ {M}\right), \tag {17}
$$

if  $(A_{1},\ldots A_{N})$  is a finer partition than  $(B_{1},\ldots ,B_{M})$ , which means that every  $A_{i}$  is contained in some  $B_{j}$ . The latter is then a coarser partition than the former.

Among the properties that are important for the rest of the paper are the following:

(i)  $E_{S}$  vanishes on product states, i.e.,  $E_{S}(|\psi \rangle) = 0$  is equivalent to

$$
| \psi \rangle = | \psi^ {(1)} \rangle \otimes \dots \otimes | \psi^ {(N)} \rangle . \tag {18}
$$

(ii)  $E_{S}$  is nonincreasing under stochastic local operations with classical communication (SLOCC) [11,29]. Let  $L^{(1)},\ldots ,L^{(N)}$  be operators acting on the Hilbert spaces  $\mathcal{H}^{(1)},\dots,\mathcal{H}^{(N)}$  satisfying  $(L^{(i)})^{\dagger}L^{(i)}\leqslant 1$  and set  $L = L^{(1)}\otimes \dots$ $\otimes L^{(N)}$  , then

$$
E _ {S} \left(\frac {L | \psi \rangle}{\langle \psi | L ^ {\dagger} L | \psi \rangle^ {1 / 2}}\right) \leqslant E _ {S} (| \psi \rangle).
$$

This can be abbreviated as the statement that if

$$
\left| \right. \psi \left. \right\rangle_ {\text {S L O C C}} \rightarrow \left| \right. \psi^ {\prime} \left. \right\rangle , \tag {19}
$$

then  $E_{S}(|\psi^{\prime}\rangle)\leqslant E_{S}(|\psi \rangle)$  . Similarly,

$$
\left| \psi \right\rangle_ {\text {L U}} ^ {\leftrightarrow} \left| \psi^ {\prime} \right\rangle \tag {20}
$$

implies that  $E_{S}(|\psi^{\prime}\rangle) = E_{S}(|\psi \rangle)$  holds, where  $\leftrightarrow_{\mathrm{LU}}$  denotes the interconversion via local unitaries. Moreover, for any sequence of local projective measurements that finally completely disentangles the state vector  $|\psi \rangle$  in each of the measurement results, we obtain the upper bound

$$
E _ {S} (| \psi \rangle) \leqslant \log_ {2} (m), \tag {21}
$$

where  $m$  is the number of measurement results with nonzero probability.

(iii)  $E_{S}$  is nonincreasing under a coarse graining of the partitioning. If two components are merged in order to form a new component, then the Schmidt measure can only decrease. If the Schmidt measure of a state vector  $|\psi \rangle$  is evaluated with respect to a partitioning  $(A_{1},\dots ,A_{N})$ , meaning that the respective Hilbert spaces are those of the grains of the partitioning, it will be appended,

$$
E _ {S} ^ {(A _ {1}, \dots , A _ {N})} (| \psi \rangle), \tag {22}
$$

in order to avoid confusion. The nonincreasing property of the Schmidt measure then manifests as

$$
E _ {S} ^ {\left(A _ {1}, \dots , A _ {N}\right)} (\left| \psi \right\rangle) \geqslant E _ {S} ^ {\left(B _ {1}, \dots , B _ {M}\right)} (\left| \psi \right\rangle), \tag {23}
$$

if  $(A_{1},\ldots ,A_{N})\leqslant (B_{1},\ldots ,B_{M})$  . For a graph  $G = (V,E)$  , the partitioning where  $(A_{1},\dots ,A_{M}) = V$  will be referred to as finest partitioning. If no upper index is appended to the Schmidt measure, the finest partitioning will be implicitly assumed.

(iv)  $E_{S}$  is subadditive, i.e., for the partitionings  $(A_{1},\ldots ,A_{N})$  and  $(B_{1},\ldots ,B_{M})$  of two different Hilbert spaces, over which  $|\psi_1\rangle$  and  $|\psi_2\rangle$  are states,

$$
\begin{array}{l} E _ {S} ^ {(A _ {1}, \dots , A _ {N}, B _ {1}, \dots , B _ {M})} (| \psi_ {1} \rangle \otimes | \psi_ {2} \rangle) \\ \leqslant E _ {S} ^ {\left(A _ {1}, \dots , A _ {N}\right)} \left(\left| \psi_ {1} \right\rangle\right) + E _ {S} ^ {\left(B _ {1}, \dots , B _ {M}\right)} \left(\left| \psi_ {2} \right\rangle\right). \tag {24} \\ \end{array}
$$

Moreover, for any state vector  $|\phi \rangle$  that is a product state with respect to the partitioning  $(B_{1},\ldots ,B_{M})$ , we have that

$$
E _ {S} ^ {(A _ {1}, \dots , A _ {N}, B _ {1}, \dots , B _ {M})} (| \psi \rangle \otimes | \phi \rangle) = E _ {S} ^ {(A _ {1}, \dots , A _ {N})} (| \psi \rangle). \tag {25}
$$

(v) For any bipartition  $(A,B)$

$$
E _ {S} (| \psi \rangle) = \log_ {2} \left(\operatorname {r a n k} \left(\operatorname {t r} _ {A} [ | \psi \rangle \langle \psi | ]\right)\right). \tag {26}
$$

Moreover  $E_{S}$  is additive within a given bipartitioning, i.e., if  $A = A_{1} \cup A_{2}$  and  $B = B_{1} \cup B_{2}$ , then

$$
E _ {S} ^ {(A, B)} \left(\left| \psi_ {1} \right\rangle \otimes \left| \psi_ {2} \right\rangle\right) = E _ {S} ^ {\left(A _ {1}, B _ {1}\right)} \left(\left| \psi_ {1} \right\rangle\right) + E _ {S} ^ {\left(A _ {2}, B _ {2}\right)} \left(\left| \psi_ {2} \right\rangle\right). \tag {27}
$$

The Schmidt measure is a measure of entanglement that quantifies genuine multiparticle entanglement. Yet, it is a coarse measure that divides pure states into classes, each of which is associated with the logarithm of a natural number or zero. But more detailed information can be obtained by considering more than one split of the total quantum system. As stated in property (ii), the Schmidt measure is a multiparticle entanglement monotone [11]. The fact that it is a noncontinuous functional on state space is a weakness when considering bipartite entanglement (where it merely reduces to the logarithm of the Schmidt rank for pure states) and in those few-partite cases where other measures are still feasible to some extent. However, for the present purposes it turns out to be just the appropriate tool that is suitable for characterizing the multiparticle entanglement of graph states associated with potentially very many vertices.

Moreover, it should be noted that for general pure states of multipartite quantum systems the Schmidt measure is—

as any other measure of multipartite entanglement—exceedingly difficult to compute. In order to determine the Schmidt measure  $E_{S}$ , one has to show that a given decomposition in Eq. (15) with  $R$  is minimal. The minimization problem involved is, as such, not even a convex optimization problem. Since  $E_{S}$  is discrete, the minimization has to be done by ruling out that any decomposition in  $R - 1$  product terms exists. According to a fixed basis  $\{|0\rangle^{(a)}, |1\rangle^{(a)}\}$  for each of the  $N$  qubit systems, the decomposition in Eq. (15) can be written as

$$
\sum_ {i = 1} ^ {R} \xi_ {i} \left(\alpha_ {i} ^ {(1)} | 0 \rangle^ {(1)} + \beta_ {i} ^ {(1)} | 1 \rangle^ {(1)}\right) \otimes \dots \otimes \left(\alpha_ {i} ^ {(N)} | 0 \rangle^ {(N)} + \beta_ {i} ^ {(N)} | 1 \rangle^ {(N)}\right). \tag {28}
$$

Not taking normalization into account, which would increase the number of equations while decreasing the number of parameters, Eq. (15) can therefore be rewritten as a system of nonlinear equations in the variables  $\xi_{i},\alpha_{i}^{(a)},\beta_{i}^{(a)}\in \mathbb{C}$  with  $i = 1,\ldots ,R$  and  $a = 1,\dots ,N$ . In this way one would essentially arrive at testing whether a system of  $2^{N}$  polynomials in  $(2N + 1)\times 2^{Es}$  complex variables has common null spaces. This illustrates that the determination of the Schmidt measure for a general state can be a very difficult problem of numerical analysis, which scales exponentially in the number of parties  $N$  as well as in the degree of entanglement of the state itself (in terms of the Schmidt measure  $E_S$ ).

Remember, however, that the graph states themselves represent already a large class of genuine multipartite entangled states that are relatively easy to survey even in the regime of many parties. A numerical analysis [30] seems still unrealistic in this regime, at least until simpler procedures or generic arguments are found. In the following, we will provide lower and upper bounds for the Schmidt measure of graph states in graph theoretic terms, which will coincide in many cases. Because of the complexity of the numerical reformulation given above, we will omit the computation of the exact value for the Schmidt measure in those cases, where lower and upper bounds do not coincide. We will now turn to formulating general rules that can be applied when evaluating the Schmidt measure on graph states for a given graph.

# III. GENERAL RULES FOR THE EVALUATION OF THE DEGREE OF ENTANGLEMENT FOR GRAPH STATES

In this section we will present general rules that give rise to upper and lower bounds for the Schmidt measure, that render the actual evaluation of the Schmidt measure feasible in most cases. We will also present rules that reflect local changes of the graph. We will first merely state the bounds; the proofs can then be found Sec. IV. For clarity, we will state the main results in the form of propositions. In Sec. V we will then apply these rules, and calculate the Schmidt measure for a number of graphs.

# A. Local Pauli measurements

It is well known that any unitary operation or projective measurement associated with operators in the Pauli group

can be treated within the stabilizer formalism [8], and therefore be efficiently simulated on a classical computer [31]. Moreover, since any stabilizer code (over a finite field) can be written as a graphical quantum code [6,12], any measurement of operators in the Pauli group turns a given graph state into a new one. More precisely, consider a graph state vector  $|G\rangle$  which is stabilized by  $S_{G} = \langle \{K_{G}^{(a)}\}_{a\in V}\rangle$  and on which a Pauli measurement is performed. The transformed stabilizer  $S^{\prime}$  of the new graph state vector

$$
\left| G ^ {\prime} \right\rangle = P \left| G \right\rangle , \tag {29}
$$

after the projective measurement associated with the projector  $P$ , is up to local unitaries  $U$  a stabilizer  $S_{G'}$  according to a new graph  $G'$ . Here and in the following, we will consider unit rays corresponding to state vectors only, and for simplicity of notation, we will write  $|\psi\rangle = |\psi'\rangle$  for Hilbert space vectors, if  $|\psi\rangle$  and  $|\psi'\rangle$  are identical up to a scalar complex factor, disregarding normalization. We obtain

$$
S ^ {\prime} = U S _ {G ^ {\prime}} U ^ {\dagger} = \left\langle \left\{U K _ {G} ^ {(a)} U ^ {\dagger} \right\} _ {a \in V} \right\rangle . \tag {30}
$$

It will be very helpful to specify into which graph  $G$  is mapped under such a measurement, without the need of formulating the measurement as a projection applied on Hilbert space vectors. This is the content of the following proposition:

Let  $a \in V$  denote the vertex corresponding to the qubit of which the observable  $\sigma_z^{(a)}$ ,  $\sigma_y^{(a)}$ , or  $\sigma_x^{(a)}$  is measured. Corresponding to this measurement we define unitaries  $U_{i,\pm}^{(a)}$ :

$$
U _ {z, +} ^ {(a)} = \mathbb {1}, \quad U _ {z, -} ^ {(a)} = \prod_ {b \in N _ {a}} \sigma_ {z} ^ {(b)}, \tag {31}
$$

$$
U _ {y, +} ^ {(a)} = \prod_ {b \in N _ {a}} (- i \sigma_ {z} ^ {(b)}) ^ {1 / 2}, \quad U _ {y, -} ^ {(a)} = \prod_ {b \in N _ {a}} (i \sigma_ {z} ^ {(b)}) ^ {1 / 2}, \tag {32}
$$

and, depending furthermore on a vertex  $b_{0} \in N_{a}$ ,

$$
U _ {x, +} ^ {(a)} = (+ i \sigma_ {y} ^ {(b _ {0})}) ^ {1 / 2} \prod_ {b \in N _ {a} - N _ {b _ {0}} - \{b _ {0} \}} \sigma_ {z} ^ {(b)}, \tag {33}
$$

$$
U _ {x, -} ^ {(a)} = \left(- i \sigma_ {y} ^ {\left(b _ {0}\right)}\right) ^ {1 / 2} \prod_ {b \in N _ {b _ {0}} - N _ {a} - \{a \}} \sigma_ {z} ^ {(b)}. \tag {34}
$$

Proposition 1 (Local Pauli measurements). Let  $G = (V, E)$  be a graph, and let  $|G\rangle$  be its graph state vector. If a measurement of  $\sigma_x^{(a)}$ ,  $\sigma_y^{(a)}$ , or  $\sigma_z^{(a)}$  on the qubit associated with vertex  $a \in V$  is performed, then the resulting state vector, depending on the outcome  $\pm 1$ , is given by

$$
P _ {i, \pm} ^ {(a)} | G \rangle = | i, \pm \rangle^ {(a)} \otimes U _ {i, \pm} ^ {(a)} | G ^ {\prime} \rangle , \quad i = x, y, z. \tag {35}
$$

The resulting graph is given by

$$
G ^ {\prime} = \left\{ \begin{array}{l l} G - \{a \}, & \text {f o r} \sigma_ {z} ^ {(a)}, \\ G - E \left(N _ {a}, N _ {a}\right), & \text {f o r} \sigma_ {y} ^ {(a)}, \end{array} \right. \tag {36}
$$

and for  $\sigma_x^{(a)}$  by

TABLE I. The relevant commutation relations for Pauli projections and Clifford operators.

$$
P _ {x, \pm} \sigma_ {z} = \sigma_ {z} P _ {x, \mp},
$$

$$
P _ {y, \pm} \sigma_ {z} = \sigma_ {z} P _ {y, +},
$$

$$
P _ {z, \pm} \sigma_ {z} = \sigma_ {z} P _ {z, \pm},
$$

$$
P _ {x, \pm} (- i \sigma_ {z}) ^ {1 / 2} = (- i \sigma_ {z}) ^ {1 / 2} P _ {y, \mp},
$$

$$
P _ {x, \pm} (i \sigma_ {y}) ^ {1 / 2} = (i \sigma_ {y}) ^ {1 / 2} P _ {z, \mp},
$$

$$
P _ {x, \pm} (- i \sigma_ {y}) ^ {1 / 2} = (- i \sigma_ {y}) ^ {1 / 2} P _ {z, \pm},
$$

$$
P _ {x, \pm} (i \sigma_ {z}) ^ {1 / 2} = (i \sigma_ {z}) ^ {1 / 2} P _ {y, \pm},
$$

$$
P _ {y, \pm} (- i \sigma_ {z}) ^ {1 / 2} = (- i \sigma_ {z}) ^ {1 / 2} P _ {x, \pm},
$$

$$
P _ {y, \pm} (i \sigma_ {y}) ^ {1 / 2} = (i \sigma_ {y}) ^ {1 / 2} P _ {y, \pm},
$$

$$
P _ {y, \pm} (- i \sigma_ {y}) ^ {1 / 2} = (- i \sigma_ {y}) ^ {1 / 2} P _ {y, \pm},
$$

$$
P _ {y, \pm} (i \sigma_ {z}) ^ {1 / 2} = (i \sigma_ {z}) ^ {1 / 2} P _ {x, \mp},
$$

$$
P _ {z, \pm} (- i \sigma_ {z}) ^ {1 / 2} = (- i \sigma_ {z}) ^ {1 / 2} P _ {z, \pm},
$$

$$
P _ {z, \pm} (i \sigma_ {y}) ^ {1 / 2} = (i \sigma_ {y}) ^ {1 / 2} P _ {x, \pm},
$$

$$
P _ {z, \pm} (- i \sigma_ {y}) ^ {1 / 2} = (- i \sigma_ {y}) ^ {1 / 2} P _ {x, \mp},
$$

$$
P _ {z, \pm} (i \sigma_ {z}) ^ {1 / 2} = (i \sigma_ {z}) ^ {1 / 2} P _ {z, \pm},
$$

$$
\begin{array}{l} G ^ {\prime} = G \Delta E (N _ {b _ {0}}, N _ {a}) \Delta E (N _ {b _ {0}} \cap N _ {a}, N _ {b _ {0}} \cap N _ {a}) \\ \times \Delta E \left(\left\{b _ {0} \right\}, N _ {a} - \left\{b _ {0} \right\}\right), \tag {37} \\ \end{array}
$$

for any  $b_0 \in N_a$ , if  $a \in V$  is not an isolated vertex. If  $a$  is an isolated vertex, then the outcome of the  $\sigma_x^{(a)}$  measurement is  $+1$ , and the state is left unchanged.

A similar set of rules has been found independently by Schlingemann [4].

Note that in case of a measurement of  $\sigma_y$ , the resulting graph can be produced as well by simply replacing the subgraph  $G[N_a]$  by its complement  $G[N_a]^c$ . An induced subgraph  $G[A]$  of a graph  $G = (V,E)$  with  $A \subset V$  is the graph that is obtained when deleting all vertices but those contained in  $A$ , and the edges incident to the deleted vertices. For a measurement of  $\sigma_x$ , like the resulting graph  $G'$ , the local unitary  $U_{x,\pm}$  depends on the choice of  $b_0$ . But the resulting graph states arising from different choices of  $b_0$  and  $b_0'$  will be equivalent up to the local unitary  $U_{b_0'} U_{b_0}^\dagger$  (see Sec. III E). Note also that the neighborhood of  $b_0$  in  $G'$  is simply that of  $a$  in  $G$  (except from  $b_0$ ). For a sequence of local Pauli measurements, the local unitaries have to be taken into account, if the measured qubit is affected by the unitary. For the sake of completeness, we therefore summarize the necessary commutation relations in Table I, which denote the transformation of the measurement basis, if a subsequent measurement is applied to a unitarily transformed graph state.

Figure 1 shows two subsequent applications of the rather complicated  $\sigma_{x}$  measurement. We will give a simplified version of this rule in Sec. III E. Apart from the trivial case of a  $\sigma_{x}$  measurement at an isolated vertex, both measurement results  $\pm 1$  of a local Pauli measurement are attained with probability  $1/2$  and yield locally equivalent graph state vectors  $|G^{\prime}\rangle$  and  $|G^{\prime \prime}\rangle$ . Therefore, we have

$$
E _ {S} \left(\left| G ^ {\prime} \right\rangle\right) \leqslant E _ {S} \left(\left| G \right\rangle\right) \leqslant E _ {S} \left(\left| G ^ {\prime} \right\rangle\right) + 1. \tag {38}
$$

According to Eq. (21), for any measurement sequence of  $\sigma_{x}$ ,  $\sigma_{y}$ , or  $\sigma_{z}$  that yields an empty graph, the number of local

![](images/8ee54a0174321bdef06494831945853c6f0e88cc79ef9026f054f2324db797d6.jpg)  
FIG. 1. Example for a  $\sigma_{x}$  measurement at vertex 1 in graph No. 1, which is followed by a  $\sigma_{z}$  measurement at vertex 2. In graph No. 1 a  $\sigma_{x}$  measurement is performed at the vertex 1. For the application of the rule in Eq. (37), vertex 2 was chosen as the special neighbor  $b_{0}$ , yielding graph No. 2 up to a local unitary  $U_{x,\pm}^{(1)} = (\pm i\sigma_{y}^{(2)})^{1 / 2}$ . As stated in Table I, the subsequent  $\sigma_{z}$  measurement on the new graph state is therefore essentially another  $\sigma_{x}$  measurement, now at vertex 2 with a single neighbor  $b_{0} = 5$ . The final graph is then graph No. 3.

![](images/8e159ba94af7e3db85b2741ad16cabadb0ea26f13c0abfd6c519870f7f5ea42e.jpg)

measurements in this sequence gives an upper bound on the Schmidt measure of the corresponding graph state. In the following we will call the minimal number of local Pauli measurements to disentangle a graph state its Pauli persistency (see Ref. [9]). Since each  $\sigma_z$  measurement deletes all edges incident to a vertex, any subset  $V' \subseteq V$  of vertices in a graph  $G$ , to which any edge of  $G$  is incident, allows for a disentangling sequence of local measurements. In graph theory those vertex subsets are called vertex covers.

Proposition 2 (Upper bound via persistency). The Schmidt measure of any graph state vector  $|G\rangle$  is bounded from above by the Pauli persistency. In particular, the Schmidt measure is less than or equal to the size of the minimal vertex cover of the corresponding graph  $G$ .

For graphs with many edges, a combination of  $\sigma_z$  and  $\sigma_y$  will give better bounds than restricting to  $\sigma_z$  measurements only. For example, due to Eq. (36), any complete graph (in which all vertices are adjacent) can be disentangled by just one  $\sigma_y$  measurement at any vertex. As we will show, this corresponds to the fact that these graph states are LU-equivalent to the GHZ-type graph states, in which every vertex is adjacent to the same central vertex (see Fig. 2).

# B. Schmidt measure for bipartite splits

For a bipartition  $(A,B)$  of the graph  $G = (V,E)$  let  $G_{AB} = (V,E_{AB})$  denote the subgraph of  $G$ , which is induced by the edges  $E_{AB}\equiv E(A,B)$  between  $A$  and  $B$ . Moreover,  $\Gamma_{AB}$  will denote the  $|A|\times |B|$ -off-diagonal submatrix of the adjacency matrix  $\Gamma_G$  according to  $G$ , which represents the edges between  $A$  and  $B$ :

$$
\left( \begin{array}{l l} \Gamma_ {A} & \Gamma_ {A B} ^ {T} \\ \Gamma_ {A B} & \Gamma_ {B} \end{array} \right) = \Gamma_ {G}, \tag {39}
$$

and similarly

$$
\left( \begin{array}{c c} 0 & \Gamma_ {A B} ^ {T} \\ \Gamma_ {A B} & 0 \end{array} \right) = \Gamma_ {G _ {A B}}. \tag {40}
$$

Proposition 3 (Bipartitioning). The partial trace with respect to any partition  $A$  is

![](images/7779f5857fbbaf133a7cb4109bdc45ef6145ba0515e52bcf675ade03da2013a1.jpg)  
FIG. 2. A single  $\sigma_y$  measurement at an arbitrary vertex in the complete graph No. 7 suffices to disentangle the corresponding state. Similarly, a single  $\sigma_z$  measurement at the central vertex in graph Nos. 1-6 or a single  $\sigma_x$  measurement at the noncentral vertices is a disentangling measurement. This is due to the fact that all graphs (Nos. 1-7) are locally equivalent by local unitaries, which transform the measurement basis correspondingly.

$$
\operatorname {t r} _ {A} [ | G \rangle \langle G | ] = \frac {1}{2 ^ {| A |}} \sum_ {\mathbf {z} \in \mathbb {F} _ {2} ^ {A}} U (\mathbf {z}) | G - A \rangle \langle G - A | U (\mathbf {z}) ^ {\dagger}, \tag {41}
$$

where  $\mathbb{F}_2$  denotes the integer field  $\{0,1\}$  with addition and multiplication modulo 2. The local unitaries are defined as

$$
U (\mathbf {z}) = \prod_ {a \in A} \left(\prod_ {b \in N _ {a}} \sigma_ {z} ^ {(b)}\right) ^ {z _ {a}}. \tag {42}
$$

Therefore, the Schmidt measure of a graph state vector  $|G\rangle$  with respect to an arbitrary bipartition  $(A,B)$  is given by the rank of the submatrix  $\Gamma_{AB}$  of the adjacency matrix  $\Gamma_G$ ,

$$
\begin{array}{l} E _ {S} (| G \rangle) \geqslant E _ {S} ^ {(A, B)} (| G \rangle) = \log_ {2} (\operatorname {r a n k} (\operatorname {t r} _ {A} [ | G \rangle \langle G | ])) = \operatorname {r a n k} _ {\mathrm {F} _ {2}} (\Gamma_ {A B}) \\ = \frac {1}{2} \operatorname {r a n k} _ {\mathbb {F} _ {2}} \left(\Gamma_ {G _ {A B}}\right). \tag {43} \\ \end{array}
$$

From Eq. (41) one may as well compute that the reduced entropy of  $|G\rangle$ , according to the bipartition  $(A,B)$  and the Schmidt rank, coincide if the base-2 logarithm is taken. This simply expresses the fact that, for a nonempty graph,  $|G\rangle$  is the "maximally"  $(A,B)$ -entangled state vector with  $2^{E_S^{(A,B)}}$  Schmidt coefficients. If one maximizes over all bipartitions  $(A,B)$  of a graph  $G = (V,E)$ , then according to Eq. (23) one obtains a lower bound for the Schmidt measure with respect to the finest partitioning.

Note that the Schmidt rank of a graph state is closely related to error correcting properties of a corresponding graph code. Let  $A$  be a partition, according to which  $|G\rangle$  has maximal Schmidt rank. Then, according to Ref. [7], choosing a subset  $X\subseteq A$ , the graph code, which encodes an input on vertices  $X$  in output on vertices  $Y = V - X$  according to  $G$ , detects the error configuration  $E = A - X$ , i.e., any errors occurring on only one half of the vertex set  $E$  can be corrected. In particular, all strongly error correcting graph codes in Ref. [7] must have Schmidt measure  $|V| / 2$ .

Proposition 4 (Maximal Schmidt rank). A sufficient criterion for a bipartite split  $(A,B)$  to have maximal Schmidt rank

is that the graph  $G_{AB}$  contains no cycles, and that the smaller partition contains at most one leaf with respect to the subgraph  $G_{AB}$ . If  $G_{AB}$  is not connected, then it is sufficient that the above criterion holds for every connected component of  $G_{AB}$ .

A leaf is a vertex of degree 1, i.e., a vertex to which exactly one edge is incident [1]. It is finally important to note that the maximum Schmidt measure with respect to all bipartite partitions is essentially the quantity considered in Ref. [32] in the context of an efficient simulation of a quantum algorithm on a classical computer. If this quantity has the appropriate asymptotic behavior in the number  $n$  of spin systems used in the computation, then an efficient classical algorithm simulating the quantum dynamics can be constructed.

Note finally that, as an immediate corollary of the above considerations, the degree of entanglement depends only on the area of the boundary between distinguished regions of regular cluster states, i.e., graph states where in a regular cubic lattice nearest neighbors are connected by an edge. If one considers periodic boundary conditions, one may distinguish a cuboid forming part  $A$  from the rest of the graph  $B$ , and ask for the bipartite entanglement. It follows immediately that since the interior regions may be completely disentangled, the degree of entanglement is linear in the number of vertices forming the boundary of the two regions. The corners are then counted just as one maximally entangled pair of two-spin systems.

# C. Deleting edges and vertices

For graphs with a large number of vertices or edges, it is useful to identify bounds for the Schmidt measure when local changes to the graph are applied. As an example, we give two rules that bound the changes to the Schmidt measure if an edge or a vertex is deleted or added.

Proposition 5 (Edge rule). By deleting or adding edges  $e = \{a, b\}$  between two vertices  $a, b \in V$  of a graph  $G$  the Schmidt measure of the resulting graph  $G' = G \pm \{e\}$  can at most decrease or increase by one, i.e.,

$$
\left| E _ {S} \left(\left| G ^ {\prime} \right\rangle\right) - E _ {S} \left(\left| G \right\rangle\right) \right| \leqslant 1. \tag {44}
$$

Proposition 6 (Vertex rule). If a vertex  $a$  (including all its incident edges) is deleted, the Schmidt measure of the resulting graph  $G' = G - \{a\}$  cannot increase and will at most decrease by one, i.e.,

$$
E _ {S} \left(\left| G ^ {\prime} \right\rangle\right) \leqslant E _ {S} \left(\left| G \right\rangle\right) \leqslant E _ {S} \left(\left| G ^ {\prime} \right\rangle\right) + 1. \tag {45}
$$

# D. Bounds for 2-colorable graphs

Graphs may be colorable. A proper 2-coloring of a graph is a labeling  $V \to \{1,2\}$ , such that all adjacent vertices are associated with a different element from  $\{1,2\}$ , which can be identified with two colors. In graph theory these graphs are also called "bipartite graphs," since the set of vertices can be partitioned into two disjoint sets, such that no two vertices within the same set are adjacent. It is a well-known fact in

graph theory that a graph is 2-colorable if it does not contain any cycles of odd length.

As has been shown in Ref. [5], for every graph state corresponding to a 2-colorable graph, a multiparty entanglement purification procedures exists: Given any 2-colorable graph state vector  $|G\rangle$  on  $|V|$  qubits, by means of LOCC operations a general mixed state  $\rho$  on  $|V|$  particles can be transformed into a mixed state, which is diagonal in a basis of orthogonal states that are LU-equivalent to  $|G\rangle$ . Given that the initial fidelity is sufficient, an ensemble of those states can then be purified to  $|G\rangle$ . Thus, 2-colorable graph states provide a reservoir of entangled states between a large number of particles, which can be created and maintained even in the presence of decoherence/noise. For the class of these graph states the lower and upper bounds to the Schmidt measure can be applied.

Proposition 7 (2-colorable graphs). For 2-colorable graphs  $G = (V, E)$  the Schmidt measure is bounded from below by half the rank of the adjacency matrix of the graph, i.e.,

$$
E _ {S} (| G \rangle) \geqslant \frac {1}{2} \operatorname {r a n k} _ {\mathrm {F} _ {2}} (\Gamma_ {G}), \tag {46}
$$

and from above by the size of the smaller partition of the corresponding bipartition. In particular, for a 2-colorable graph,

$$
E _ {S} (| G \rangle) \leqslant \left\lfloor \frac {| V |}{2} \right\rfloor . \tag {47}
$$

If  $\Gamma_G$  is invertible, then equality holds in Eq. (47).

Note that any graph  $G$ , which is not 2-colorable, can be turned into a 2-colorable one  $G'$  simply by deleting the appropriate vertices on cycles with odd length. Since this corresponds to  $\sigma_z$  measurements, by Eq. (38),

$$
E _ {S} (| G \rangle) \leqslant E _ {S} (| G ^ {\prime} \rangle) + M \leqslant \left\lfloor \frac {| V - M |}{2} \right\rfloor + M \leqslant \left\lfloor \frac {| V | + M}{2} \right\rfloor , \tag {48}
$$

where  $M$  denotes the number of removed vertices. Moreover, note that the number of induced cycles with odd length certainly bounds  $M$  from above.

We also note that whereas local  $\sigma_{x}$  or  $\sigma_z$  measurements in 2-colorable graphs will yield graph states according to 2-colorable graphs,  $\sigma_y$  measurements of 2-colorable graphs can lead to graph states which are not even locally equivalent to 2-colorable graphs. It is certainly true that a 2-colorable graph remains 2-colorable after application of the  $\sigma_z$  measurement rule Eq. (36), since after deletion of a vertex in a 2-colorable graph the graph still does not contain any cycles of odd length.

Now let  $G$  be a 2-colorable graph with the bipartition  $A$  of sinks and  $B$  of sources, in which the observable  $\sigma_{x}$  is measured at vertex  $a \in A$ . Then, the set  $E(N_{b_0} \cap N_a, N_{b_0} \cap N_a)$  in Eq. (37) is empty and  $E(N_{b_0}, N_a)$  only consists of edges between  $A$  and  $B$ . Moreover, after adding all edges of the last set (modulo 2) to the edge set of the graph  $G$ , the measured

![](images/63b1c175e3ad97003f2beaf89d2a57113b84e10c713343f79a0f998102bf22b0.jpg)  
FIG. 3. Whereas graph No. 1 is 2-colorable, the resulting graph No. 2 after a  $\sigma_y$  measurement at the vertex ■ is not 2-colorable. Also, none of the 132 (or 3) representatives in the corresponding equivalence class (if graph isomorphisms are included) is 2-colorable.

![](images/5d4995bb5ca62e2353113e068c901bb7ffdd15ebb13f00350658615337dba11a.jpg)

vertex  $a \in A$ , as well as its special neighbor  $b_0 \in B$ , are isolated, so that in the last step of adding  $E(\{b_0\}, N_a - \{b_0\})$  the vertex  $b_0$  simply gets all neighbors  $N_a - \{b_0\} \subset B$  in  $G$ . So after application of this rule the new graph  $G'$  has the 2-coloring with partitions  $A' = A - \{a\} \cup \{b_0\}$  and  $B' = B - \{b_0\}$ . A counterexample to a corresponding assertion for  $\sigma_y$  measurements is provided in Fig. 3. The resulting graph even has no locally equivalent representation as a 2-colorable graph. This is because the corresponding equivalence class No. 8 in Table II has no 2-colorable representative.

# E. Equivalence classes of graph states under local unitaries

Each graph state vector  $|G\rangle$  corresponds uniquely to a graph  $G$ . However, two graph states can be LU-equivalent, leading to two different graphs. Needless to say, this equivalence relation is different from the graph isomorphisms in graph theory. We have examined the graph states of all nonisomorphic (connected) graphs with up to seven vertices. More precisely, from the set of all possible graphs with seven vertices  $(2_{2}^{7}) \approx 2 \times 10^{6}$  possibilities), we have considered the subset of all connected graphs on up to seven vertices which are nonisomorphic with respect to graph isomorphisms, i.e., permutations of the vertices that map neighbored vertices onto neighbored vertices. Of the 995 isomorphism classes of corresponding graph states, 45 classes have turned out to be not invariant under local unitary operations (with respect to the finest partitioning). Moreover, within each of these classes all graph states are equivalent modulo local unitaries and additional graph isomorphisms, which corresponds to the exchange of particles. If we exclude the graph isomorphisms, as, e.g., in quantum communication scenarios, the number of inequivalent classes of graph states would even be larger. In Figs. 4 and 5 we give a list of simple representatives of each equivalence class.

To test for local equivalence we have only considered local unitaries within the corresponding local Clifford group. But, by considering the Schmidt rank with respect to all possible bipartitions, the corresponding lists of Schmidt ranks for each representative turned out to be different even if we allow arbitrary permutations of the vertices. This shows that the found sets of locally invariant graph states are maximal.

Having this enormous reduction in mind, it is desirable to find simple rules in purely graph theoretic terms, giving at

TABLE II. The number of vertices  $|V|$  and edges  $|E|$ , Schmidt measure  $E_{S}$ , rank index (see Sec. V)  $RI_{3}$  and  $RI_{2}$  (for splits with 2 or 3 vertices in the smaller partition), number of nonisomorphic but LU-equivalent graphs  $|\mathrm{LU}\text{class}|$ , and the 2-colorable property 2-col for the graph classes in Figs. 4 and 5.  

<table><tr><td>No.</td><td>|LU class|</td><td>|V|</td><td>|E|</td><td>ES</td><td>RI3</td><td>RI2</td><td>2-col</td></tr><tr><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td></td><td></td><td>yes</td></tr><tr><td>2</td><td>2</td><td>3</td><td>2</td><td>1</td><td></td><td></td><td>yes</td></tr><tr><td>3</td><td>2</td><td>4</td><td>3</td><td>1</td><td></td><td>(0,3)</td><td>yes</td></tr><tr><td>4</td><td>4</td><td>4</td><td>3</td><td>2</td><td></td><td>(2,1)</td><td>yes</td></tr><tr><td>5</td><td>2</td><td>4</td><td>4</td><td>1</td><td></td><td>(0,10)</td><td>yes</td></tr><tr><td>6</td><td>6</td><td>5</td><td>4</td><td>2</td><td></td><td>(6,4)</td><td>yes</td></tr><tr><td>7</td><td>10</td><td>5</td><td>4</td><td>2</td><td></td><td>(8,2)</td><td>yes</td></tr><tr><td>8</td><td>3</td><td>5</td><td>5</td><td>2&lt;3</td><td></td><td>(10,0)</td><td>no</td></tr><tr><td>9</td><td>2</td><td>6</td><td>5</td><td>1</td><td>(0,0,10)</td><td>(0,15)</td><td>yes</td></tr><tr><td>10</td><td>6</td><td>6</td><td>5</td><td>2</td><td>(0,6,4)</td><td>(8,7)</td><td>yes</td></tr><tr><td>11</td><td>4</td><td>6</td><td>5</td><td>2</td><td>(0,9,1)</td><td>(8,7)</td><td>yes</td></tr><tr><td>12</td><td>16</td><td>6</td><td>5</td><td>2</td><td>(0,9,1)</td><td>(11,4)</td><td>yes</td></tr><tr><td>13</td><td>10</td><td>6</td><td>5</td><td>3</td><td>(4,4,2)</td><td>(12,3)</td><td>yes</td></tr><tr><td>14</td><td>25</td><td>6</td><td>5</td><td>3</td><td>(4,5,1)</td><td>(13,2)</td><td>yes</td></tr><tr><td>15</td><td>5</td><td>6</td><td>6</td><td>2</td><td>(0,10,0)</td><td>(12,3)</td><td>yes</td></tr><tr><td>16</td><td>5</td><td>6</td><td>6</td><td>3</td><td>(4,6,0)</td><td>(12,3)</td><td>yes</td></tr><tr><td>17</td><td>21</td><td>6</td><td>6</td><td>3</td><td>(4,6,0)</td><td>(14,1)</td><td>yes</td></tr><tr><td>18</td><td>16</td><td>6</td><td>6</td><td>3</td><td>(6,4,0)</td><td>(15,0)</td><td>yes</td></tr><tr><td>19</td><td>2</td><td>6</td><td>9</td><td>3&lt;4</td><td>(10,0,0)</td><td>(15,0)</td><td>no</td></tr><tr><td>20</td><td>2</td><td>7</td><td>6</td><td>1</td><td>(0,0,35)</td><td>(0,21)</td><td>yes</td></tr><tr><td>21</td><td>6</td><td>7</td><td>6</td><td>2</td><td>(0,20,15)</td><td>(10,11)</td><td>yes</td></tr><tr><td>22</td><td>6</td><td>7</td><td>6</td><td>2</td><td>(0,30,5)</td><td>(12,9)</td><td>yes</td></tr><tr><td>23</td><td>16</td><td>7</td><td>6</td><td>2</td><td>(0,30,5)</td><td>(14,7)</td><td>yes</td></tr><tr><td>24</td><td>10</td><td>7</td><td>6</td><td>2</td><td>(0,33,2)</td><td>(15,6)</td><td>yes</td></tr><tr><td>25</td><td>10</td><td>7</td><td>6</td><td>3</td><td>(12,16,7)</td><td>(16,5)</td><td>yes</td></tr><tr><td>26</td><td>16</td><td>7</td><td>6</td><td>3</td><td>(12,20,3)</td><td>(16,5)</td><td>yes</td></tr><tr><td>27</td><td>44</td><td>7</td><td>6</td><td>3</td><td>(12,21,2)</td><td>(17,4)</td><td>yes</td></tr><tr><td>28</td><td>44</td><td>7</td><td>6</td><td>3</td><td>(16,16,3)</td><td>(18,3)</td><td>yes</td></tr><tr><td>29</td><td>14</td><td>7</td><td>6</td><td>3</td><td>(20,12,3)</td><td>(18,3)</td><td>yes</td></tr><tr><td>30</td><td>66</td><td>7</td><td>6</td><td>3</td><td>(20,13,2)</td><td>(19,2)</td><td>yes</td></tr><tr><td>31</td><td>10</td><td>7</td><td>7</td><td>2</td><td>(0,34,1)</td><td>(16,5)</td><td>yes</td></tr><tr><td>32</td><td>10</td><td>7</td><td>7</td><td>3</td><td>(12,22,1)</td><td>(16,5)</td><td>no</td></tr><tr><td>33</td><td>21</td><td>7</td><td>7</td><td>3</td><td>(12,22,1)</td><td>(18,3)</td><td>no</td></tr><tr><td>34</td><td>26</td><td>7</td><td>7</td><td>3</td><td>(16,18,1)</td><td>(18,3)</td><td>yes</td></tr><tr><td>35</td><td>36</td><td>7</td><td>7</td><td>3</td><td>(16,19,0)</td><td>(19,2)</td><td>no</td></tr><tr><td>36</td><td>28</td><td>7</td><td>7</td><td>3</td><td>(20,14,1)</td><td>(18,3)</td><td>no</td></tr><tr><td>37</td><td>72</td><td>7</td><td>7</td><td>3</td><td>(20,15,0)</td><td>(19,2)</td><td>no</td></tr><tr><td>38</td><td>114</td><td>7</td><td>7</td><td>3</td><td>(22,13,0)</td><td>(20,1)</td><td>yes</td></tr><tr><td>39</td><td>56</td><td>7</td><td>7</td><td>3&lt;4</td><td>(24,10,1)</td><td>(20,1)</td><td>no</td></tr><tr><td>40</td><td>92</td><td>7</td><td>7</td><td>3&lt;4</td><td>(28,7,0)</td><td>(21,0)</td><td>no</td></tr><tr><td>41</td><td>57</td><td>7</td><td>8</td><td>3&lt;4</td><td>(26,9,0)</td><td>(20,1)</td><td>no</td></tr><tr><td>42</td><td>33</td><td>7</td><td>8</td><td>3&lt;4</td><td>(28,7,0)</td><td>(21,0)</td><td>no</td></tr><tr><td>43</td><td>9</td><td>7</td><td>9</td><td>3</td><td>(28,7,0)</td><td>(21,0)</td><td>yes</td></tr><tr><td>44</td><td>46</td><td>7</td><td>9</td><td>3&lt;4</td><td>(32,3,0)</td><td>(21,0)</td><td>no</td></tr><tr><td>45</td><td>9</td><td>7</td><td>10</td><td>3&lt;4</td><td>(30,5,0)</td><td>(20,1)</td><td>no</td></tr></table>

![](images/468296aa0c2a5f40c225c333b9eae21157b814fb67ce9000a9aa5c5e4965c81a.jpg)  
FIG. 4. List of connected graphs with up to six vertices that are not equivalent under LU transformations and graph isomorphisms.

least sufficient conditions for two graph states to be equivalent by means of local unitaries. The subsequent rule implies such a simplification: The inversion of the subgraph  $G[N_{a}] \mapsto G[N_{a}]^{c}$ , induced by the neighborhood  $N_{a}$  of any vertex  $a \in V$ , within a given graph, gives a LU-equivalent graph state. In graph theory this transformation  $\tau_{a} \colon G \mapsto \tau_{a}(G)$ , where the edges set  $E'$  of  $\tau_{a}(G)$  is obtained from the edge set  $E$  of  $G$  by  $E' = E \Delta E(N_{a}, N_{a})$ , is known as local complementation [33]. With this notation the corresponding rule for graph states can be stated as follows:

Proposition 8 (LU equivalence). Let  $a \in V$  be an arbitrary vertex of two graphs  $G = (V, E)$ , then  $|\tau(G)\rangle = U_a(G)|G\rangle$  with local unitaries of the form

$$
U _ {a} (G) = \left(- i \sigma_ {x} ^ {(a)}\right) ^ {1 / 2} \prod_ {b \in N _ {a}} \left(i \sigma_ {z} ^ {(b)}\right) ^ {1 / 2} \propto \sqrt {K _ {G} ^ {(a)}}. \tag {49}
$$

This rule was independently found by Van den Nest, who was able to show that a successive application of this rule suffices to generate the complete orbit of any graph state under local unitary operations within the Clifford group [34]. Figure 6 shows an example of how to repeatedly apply this rule in order to obtain the whole equivalence class of a graph state. Note that the set of graphs in Fig. 6 do not exhaust the entire class associated with graph No. 4 in Fig. 4. In Fig. 7 we show another set of graphs that is a proper subset of the class No. 4 in Fig. 4. No graph in Fig. 6 is locally equivalent to any graph in the equivalence class represented in Fig. 7, though both belong to the same equivalence class when considering both, local unitary transformations and graph isomorphisms, as depicted in Fig. 4.

![](images/908d8033bf00dddc9ec8721eed183bd27da4621c944571fe686caf1093d6efe0.jpg)

![](images/cd370221f0300e2cef46d6ddbeaa726cd3b89e085dbf6147989380134d68b0b8.jpg)

![](images/224309f4593f0e40bf8a5e3da52273d80205992475f227a6788ecb3758ae7b16.jpg)

![](images/5ee6472af7f3d12b4222dddb5a70109b9057fc020d8f1959a0f6346eb9cf4c66.jpg)

![](images/51db44f890cc274ce652d48dd6ecb574e09ecccf3b413a850a891c3d9745baed.jpg)

![](images/d3056951534fa4debaebd287a56429ce80c30a71814f137448ea8a1a3f4069cc.jpg)

![](images/1fd16afb62a60896d52ad3233955a11e0e231a4551102ecbdbfee1a8ad7eabdb.jpg)

![](images/ca706eb27f2150444648f56c84fd2ccd290a314f7bdc3b408a9118102388e1b0.jpg)

![](images/885cb2364dd6fc99ac5d817e0aa5e5f7440d9a7448d72b3504eff52878e8c6a4.jpg)

![](images/4046e8d55c7b577e34363191601a894671c12ea341a3f894f6e4152b2caea6a8.jpg)

![](images/0a6c08e94188e823fcd2ce679bf7473c965f2881eecea56206c348671d27fb74.jpg)

![](images/501dd45b031338bafd9712627b8f33a042f6632a03217fe33fe8b61c929d06c7.jpg)

![](images/bf46fc1311c0fa1efd8f009017fc96f2e34aeaa87403f074f0a54b680a9ba685.jpg)

![](images/1b0244329157631734e147a1605ae2af80d5954a33f98005f1f11c0401239530.jpg)

![](images/c0591dc49be59b53a14258fa860ff321cce4ae4da7fd65d5156184b1349ee9a6.jpg)

![](images/1933cf7136e7fab3e157e389ae8387ade6332df308624138506b90cde3bbe832.jpg)  
FIG. 6. An example for an successive application of the LU rule, which exhibits the whole equivalence class associated with graph No. 1. The rule is successively applied to that vertex of the preceptor, which is written above the arrows of the following diagram:  $\begin{array}{c}3\\ \mathrm{No.1}\rightarrow \mathrm{No.2}\rightarrow \mathrm{No.3}\rightarrow \mathrm{No.4}\rightarrow \mathrm{No.5}\rightarrow \mathrm{No.6}\rightarrow \mathrm{No.7}\\ 3\\ 4\\ 1\\ 2\\ \rightarrow \mathrm{No.8}\rightarrow \mathrm{No.9}\rightarrow \mathrm{No.10}\rightarrow \mathrm{No.11}. \end{array}$

![](images/1a1cb5849c2f2da34fe1d76a23654abceec1cf228103f81e46ec6b645429bfb3.jpg)

![](images/68fc159b6f3f9cb69cc1ce8fabae3bbfd730134a0da9ff278b6cdcf98a10b01d.jpg)

![](images/f206b3792142ef09a8ae3162c46c3879ae802770a2f69ecf104afd2496b069d1.jpg)

![](images/29b1a39914e80f3cc576e1b27a94df64378905a13f5c4fd6865fcb119c4ec5e9.jpg)

![](images/96a75a801f49e63ddcac7167676451d788d59d5348bd5c9d00cad8ffb6886130.jpg)

![](images/4797f188a15f10d5ff182187e1c23a9d6f38c9856031d34a054caaab46d0486b.jpg)

![](images/3cd96260d2faa450773d63ef25f110c501ac7c4a65cd7812adc9a82bce01ac71.jpg)

![](images/127ae62747afa7788663eaa11d44fb3bc8063f8b304258e71d6545160f9a8190.jpg)

![](images/faa87563fccbc6be36969e707440348373d8a558d2f41f08500b449917e16b4e.jpg)  
FIG. 5. List of connected graphs with seven vertices that are not equivalent under LU transformations and graph isomorphisms.

![](images/466b3bd1da96e50615e2f72e1998afaee81c5b75e74b8d6065542d01d8e27b8b.jpg)

For any partition  $A$  the Schmidt rank  $E_S^{(A,A^c)}$  is an invariant under arbitrary local unitaries, which is formulated in purely graph theoretic terms. Considering the list of Schmidt ranks with respect to all partitions, one therefore obtains a set of invariants for graphs under local complementations  $\tau$ , which was already considered in graph theory, known as the connectivity function [33]. For the equivalence classes in Figs. 6 and 7, for example, the corresponding lists of Schmidt ranks or connectivity functions do not coincide, implying that the corresponding set of graph states are not equivalent either under local Clifford group operations or under general local unitaries. We note that the Schmidt rank list does not provide a complete set of invariants that would characterize all equivalence classes under local Clifford group operations. For the Petersen graph shown in Fig. 8, and the isomorphic graph, which is obtained by exchanging the labels at each end of the five "spokes," no local Clifford operation exists (i.e., sequence of local complementations) that transforms

![](images/963321db26b352319138dbae874cada7783e75bcada9e497cfea61e3d1652190.jpg)

![](images/829531aa7c0a2c4cad786ebca5d3df029ef86a8f10d403df6ad7eac8e5875aa6.jpg)

![](images/b60b7cd2b412505c4478380cffc9edf3e37b8b9c101cfd761a88aa33d1c9037a.jpg)

![](images/f0f2cc7d55c294a8b757f648d40467e819df2dad5beff844ffaaa881a2a4c4d8.jpg)

![](images/c8789ec5ea86e9e7ab9b6982b9cac6997a48cac53c4a10693f043a2b86dec7e4.jpg)

![](images/06fffe7e0d7ffc11825a6c46c0977477bf7dcc4ce487566598a2b2a3555367f6.jpg)

![](images/bda54393088472f40333f1283c09e37d80b8606acdcc77bd4d050e7c5035c698.jpg)

![](images/4ff091b55b2faa983ed1b9ad2fe0f2d2f118d6dab70d17c6978422df97919bdb.jpg)

![](images/20fcba089c524c688326ebe177384cf9102ee9aa132e9824dbbdf27d65831dcb.jpg)

![](images/92854f6e9728a2031bd57d2563febc1de5978a6521c3e5499202fd42c3c9bfc1.jpg)

![](images/5ed7fd9be01394193066938de454dc97d3c036e343170265bf1feebfe143c988.jpg)

one graph into the other, although the Schmidt rank lists for both graphs coincide. For a complete set of invariants the polynomial invariants in Ref. [35] can be considered. For example, the number of elements  $I_A(G)$  in the stabilizer of the graph state vector  $|G\rangle$ , that act nontrivially exactly on the vertices in  $A$ , corresponds to homogeneous polynomial invariants of degree 2. Moreover, one can show that

![](images/f2039d355f08591c3e58f3e065ad9330fdd61e8ed4b197d284799eaf68c3fed1.jpg)

![](images/2b523079950346d78ca7eeb8df4128904c90d1cdcf9d03a138c575299cc6cd2b.jpg)

![](images/e7a9c10bb67bcaf4c042c125a6e567eef7476d7e7bd0a19337e1986036dc37d0.jpg)

![](images/a92d7b5799f0960868000def9e8ae4532e62c6c6e34d2fc6b1053534bc3c001d.jpg)

![](images/3d4b49c4aa730ccb9661fef4911cc5ad6ff854a14a2ea26a024bb8b67b327560.jpg)

![](images/e9b84449d5871308339db7b256fc9713f9e2109e7dbfa0ec5392a08cee125893.jpg)

![](images/fad15ac39646e1bd83d8f5cdbea6d75fb2c095b0bbee05b203aea3bc60bb2e4e.jpg)

![](images/fa92ff321fb8b9f66c502c816613d6feba9e615e05c02525a09fb12cfffce522.jpg)

![](images/03699db1bf26b19d29e6c16f5dad7f6b52b6ac08335aeee34503ecb8f71d0715.jpg)  
FIG. 7. An example of an equivalence class, which is a proper subset of class No. 4 in Fig. 4.

![](images/8bf37487468b6d877ffff352aed7da0b0b05ac325b82cf3e688ab600aa332130.jpg)

![](images/33391103853e1d61f5460767691fdc732edfeb841f9ede5d99463c59b35d161c.jpg)

![](images/1b75cb299e7cf87f8da3ae270fc20ed10e403c34c15c8ceeabad64e2a2038875.jpg)  
FIG. 8. The Petersen graph. The depicted labeled graph is not LU equivalent to the graph which is obtained from it by exchanging the labels at each end of the five "spokes," i.e., the graph isomorphism which permutes the vertices  $1,2,3,4$ , and 5 with  $6,7,8,9$ , and 10, respectively.

$$
\sum_ {B \subseteq A} I _ {B} (G) = 2 ^ {\left(| A | - E _ {S} ^ {(A, A ^ {c})}\right)}. \tag {50}
$$

Therefore, the list of invariants  $I_A(G)$  with respect to all partitions  $A$  essentially contains the same information for graph states as the Schmidt rank list. But, as discussed in Refs. [35,36], by considering more invariants corresponding to homogeneous polynomials of different degrees, one can (in principle) obtain finite and complete sets of invariants for local Clifford operations, as well as for arbitrary local unitaries.

Finally, the LU rule can be used to derive the  $x$ - and  $y$ -measurement rule from the simple  $z$ -measurement rule: With commutation relations similar to those in Table I, it is easy to see that  $P_{x,\pm}^{(a)} = U_{b_0}(G)P_{y,\pm}^{(a)}U_{b_0}^{\dagger}(G)$  and  $P_{y,\pm}^{(a)} = U_a(G)P_{z,\mp}^{(a)}U_a^{\dagger}(G)$  holds, where  $b_0$  is a neighbor of  $a$ . With the notion of local complementation at hand, we can then rewrite the resulting states in Proposition 1 after the Pauli measurement in the simplified form:

$$
\left. P _ {z, \pm} ^ {(a)} | G \rangle = | z, \pm \rangle^ {(a)} \otimes U _ {z, \pm} ^ {(a)} | G - a \rangle , \right. \tag {51}
$$

$$
P _ {y, \pm} ^ {(a)} | G \rangle = | y, \pm \rangle^ {(a)} \otimes U _ {y, \pm} ^ {(a)} | \tau_ {a} (G) - a \rangle , \tag {52}
$$

$$
\left. P _ {x, \pm} ^ {(a)} | G \rangle = | x, \pm \rangle^ {(a)} \otimes U _ {x, \pm} ^ {(a)} | \tau_ {b _ {0}} \left(\tau_ {a} \circ \tau_ {b _ {0}} (G) - a\right) \rangle , \right. \tag {53}
$$

where the local unitaries  $U_{i,\pm}^{(a)}$  are defined as for Proposition 1.

# IV. PROOFS

In this section we prove the statements that, for clarity of presentation, have been summarized in the previous section without proof.

Proof of Proposition 1. As already mentioned in Sec. III E, with the LU rule at hand one could derive the graph  $G'$  after an  $x$  or  $y$  measurement from the  $z$ -measurement rule, which can be directly proven by disentangling the Ising interactions  $U^{(a,b)}$  in Eq. (9). Here, we will instead take another starting point for the proof, namely a well-known result from

stabilizer theory that we will then apply to the specific question at hand. Consider a subspace of  $\mathbb{C}^n$ , which is stabilized by

$$
\langle \left\{g _ {i} \right\} _ {i \in I} \rangle , \quad g _ {i} \in \mathcal {P} _ {n}, \tag {54}
$$

where  $\mathcal{P}_n$  denotes the Pauli group on  $n$  qubits and  $I$  is an index set. It is well known (see, e.g., Ref. [37]) that the projected subspace  $P_{g,\pm}$  corresponding to a measurement of an operator  $g\in \mathcal{P}_n$  in the Pauli group (i.e.,  $g$  is a product of Pauli matrices) with outcome  $\pm 1$  is stabilized by:

(i)  $\langle \{g_i\}_{i\in I}\rangle$  , if  $g$  commutes with all stabilizer generators  $g_{i}$  
(ii)  $\langle \{\pm g\} \cup \{g_k g_j : j \in I' - \{k\}\} \cup \{g^{(j)} | j \in I'^c\} \rangle$  for some  $k \in I'$  otherwise.  $I'$  denotes the nonempty index set of the generators  $g_i$  that do not commute with  $g$ , and  $I'^c = I \setminus I'$  is the complement of  $I'$ .

We now turn to the specific case of graph state vectors  $|G\rangle$  and measurements of  $\sigma_x^{(a)},\sigma_y^{(a)}$ , or  $\sigma_z^{(a)}$  at vertex  $a\in V$ . Then, each generator  $K_{G}^{(a)}$  is associated with an element  $a\in V$ , and for a given  $g$ , the list  $I^{\prime}$  of generators that do not commute with  $g$  is a subset of  $V$ . For the measurements considered here, only case (ii) is relevant, as long as  $\sigma_x^{(a)}$  is not measured at an isolated vertex  $a$ . In the latter situation, which corresponds to case (i),

$$
K _ {G} ^ {(a)} = \sigma_ {x} ^ {(a)}, \tag {55}
$$

and  $\sigma_z^{(a)}$  is not contained in any  $K_G^{(b)}$  for  $b\neq a$ . Then, the state is left unchanged and with probability 1 the result  $+1$  is obtained.

In case (ii), in turn, the possible measurement results  $\pm 1$  are always obtained each with probability  $1 / 2$ . Let us start with identifying the resulting state vector and graph after measuring  $\sigma_z^{(a)}$ . The index set  $I^{\prime}$  then is given by  $I^{\prime} = \{a\}$ , and the state vector  $P_{z,\pm}^{(a)}|G\rangle$  is stabilized by

$$
\langle \left\{\pm \sigma_ {z} ^ {(a)} \right\} \cup \left\{K _ {G} ^ {(b)}: b \in V - \{a \} \right\} \rangle . \tag {56}
$$

Multiplying  $\pm \sigma_z^{(a)}$  to the elements  $K_G^{(b)}$  for  $b\in V - \{a\}$ , according to the neighbors  $b\in N_{a}$  in  $G$ , yields

$$
\pm \sigma_ {z} ^ {(a)} K _ {G} ^ {(b)} = \pm \sigma_ {x} ^ {(b)} \prod_ {b ^ {\prime} \in N _ {b} - \{a \}} \sigma_ {z} ^ {(b ^ {\prime})}, \tag {57}
$$

which is up to the sign the stabilizer generator according to the vertex  $b$  in  $G - \{a\}$ . Since the stabilizer generators  $K_G^{(b)}$  corresponding to vertices  $b$  outside  $N_a \cup \{a\}$  in  $G$  coincide with those in  $G - \{a\}$ , the stabilizer may as well be seen generated by

$$
\{\pm \sigma_ {z} ^ {(a)} \} \cup \{\pm K _ {G - \{a \}} ^ {(b)}: b \in N _ {a} \}
$$

$$
\cup \left\{K _ {G - \{a \}} ^ {(b)}: b \in V - \{a \} - N _ {a} \right\}. \tag {58}
$$

Hence, we have shown the validity of Eq. (35) for the case of a positive  $\sigma_z$  measurement result. In the other case the sign can be corrected for, as the stabilizer can be written as

$$
\left\langle U _ {z, -} \left(\{- \sigma_ {z} ^ {(a)} \} \cup \left\{K _ {G - \{a \}} ^ {(b)}: b \in V _ {G - \{a \}} \right\}\right) U _ {z, -} ^ {\dagger} \right\rangle , \tag {59}
$$

which corresponds to the state vector

$$
\left| z, - \right\rangle^ {(a)} \otimes U _ {z, -} ^ {(a)} | G - \{a \} \rangle . \tag {60}
$$

Here, it has been used that  $U_{z, - }^{(a)} = \Pi_{b\in N_a}\sigma_z^{(b)}$  anticommutes exactly with the generators

$$
\left\{K _ {G - \{a \}} ^ {(b)}: b \in N _ {a} \right\}. \tag {61}
$$

In a similar manner, the case of a measurement of  $\sigma_y^{(a)}$  can be treated. The index set  $I^{\prime}$  is given by  $I^{\prime} = N_{a}\cup \{a\}$  and, if  $k = a$  is chosen, the new stabilizer is given by

$$
\left\langle \left\{\pm \sigma_ {y} ^ {(a)} \right\} \cup \mathcal {G} _ {1} \cup \mathcal {G} _ {2} \right\rangle , \tag {62}
$$

where

$$
\mathcal {G} _ {1} = \left\{K _ {G} ^ {(a)} K _ {G} ^ {(b)}: b \in N _ {a} \right\}, \tag {63}
$$

$$
\mathcal {G} _ {2} = \left\{K _ {G} ^ {(c)}: c \in V - N _ {a} - \{a \} \right\}. \tag {64}
$$

For  $\mathcal{G}_1$  one computes

$$
\begin{array}{l} K _ {G} ^ {(a)} K _ {G} ^ {(b)} = \sigma_ {y} ^ {(a)} \sigma_ {y} ^ {(b)} \prod_ {b ^ {\prime} \in N _ {b} \Delta N _ {a} - \{a, b \}} \sigma_ {z} ^ {(b ^ {\prime})} \\ = \pm \sigma_ {y} ^ {(a)} U _ {y, \pm} ^ {(a)} \left(\sigma_ {x} ^ {(b)} \prod_ {b ^ {\prime} \in N _ {b} \Delta N _ {a} - \{a, b \}} \sigma_ {z} ^ {(b ^ {\prime})}\right) U _ {y, \pm} ^ {(a) \dagger} \\ = \pm \sigma_ {y} ^ {(a)} U _ {y, \pm} ^ {(a)} K _ {G ^ {\prime}} ^ {(b)} U _ {y, \pm} ^ {(a) \dagger}, \tag {65} \\ \end{array}
$$

where  $G^{\prime}$  denotes the graph with the edge set  $E^{\prime} = E_{G}\Delta E(N_{a},N_{a})$  and the unitaries  $U_{y,\pm}^{(a)}$  are defined as in Eq. (32). Because the elements in  $\mathcal{G}_2$  commute with  $U_{y,\pm}^{(a)}$ , we arrive at the result for measurements of  $\sigma^{(a)}$ .

Finally, in the case of measurements of  $\sigma_x^{(a)}$ , we identify  $I'$  as  $I' = N_a$ . If some  $b_0 \in N_a$  is chosen, the new stabilizer is given by

$$
\langle \left\{\pm \sigma_ {x} ^ {(a)}, K _ {G} ^ {(a)} \right\} \cup \mathcal {G} _ {1} \cup \mathcal {G} _ {2} \cup \mathcal {G} _ {3} \cup \mathcal {G} _ {4} \rangle , \tag {66}
$$

where, because of the following argumentation the finer dissection is chosen,

$$
\mathcal {G} _ {1} = \left\{K _ {G} ^ {(b _ {0})} K _ {G} ^ {(b)}: b \in N _ {a} \cap N _ {b _ {0}} \right\}, \tag {67}
$$

$$
\mathcal {G} _ {2} = \left\{K _ {G} ^ {(b _ {0})} K _ {G} ^ {(b)}: b \in N _ {a} - N _ {b _ {0}} - \left\{b _ {0} \right\} \right\}, \tag {68}
$$

$$
\mathcal {G} _ {3} = \left\{K _ {G} ^ {(b)}: b \in N _ {b _ {0}} - N _ {a} - \{a \} \right\}, \tag {69}
$$

$$
\mathcal {G} _ {4} = \left\{K _ {G} ^ {(c)}: c \in V - N _ {a} - N _ {b _ {0}} \right\}. \tag {70}
$$

Instead of  $K_G^{(a)}$ , the generator

$$
\pm \sigma_ {x} ^ {(a)} K _ {G} ^ {(a)} = \pm \prod_ {b \in N _ {a}} \sigma_ {z} ^ {(b)} = U _ {x, \pm} ^ {(a)} \left(\sigma_ {x} ^ {(b _ {0})} \prod_ {b \in N _ {a} - \{b _ {0} \}} \sigma_ {z} ^ {(b)}\right) U _ {x, \pm} ^ {(a) \dagger} \tag {71}
$$

can be chosen, where  $U_{x,\pm}^{(a)}$  is defined as above. Instead of  $K_G^{(b_0)}K_G^{(b)}$  in  $\mathcal{G}_1$ , we choose, for  $b_0\in N_a$  and  $b\in N_{b_0}$

$$
\begin{array}{l} \pm \sigma_ {x} ^ {(a)} K _ {G} ^ {(a)} K _ {G} ^ {(b _ {0})} K _ {G} ^ {(b)} \\ = \mp \sigma_ {x} ^ {(b _ {0})} \sigma_ {x} ^ {(b)} \prod_ {b ^ {\prime} \in N _ {b} \Delta N _ {a} \Delta N _ {b _ {0}}} \sigma_ {z} ^ {(b ^ {\prime})} \\ = U _ {x, \pm} ^ {(a)} \left(\mp \left(\mp i \sigma_ {y} ^ {(b _ {0})}\right) \sigma_ {x} ^ {(b _ {0})} (+ \sigma_ {x} ^ {(b)}) \prod_ {b ^ {\prime} \in N _ {b} \Delta N _ {a} \Delta N _ {b _ {0}}} \sigma_ {z} ^ {(b ^ {\prime})}\right) U _ {x, \pm} ^ {(a) \dagger} \\ = U _ {x, \pm} ^ {(a)} \Bigg (\sigma_ {x} ^ {(b)} \prod_ {b ^ {\prime} \in N _ {b} \Delta N _ {a} \Delta N _ {b _ {0}} \cup \{b _ {0} \}} \sigma_ {z} ^ {(b ^ {\prime})} \Bigg) U _ {x, \pm} ^ {(a) \dagger}, \\ \end{array}
$$

where the second equality holds, because  $b_{0} \notin N_{b}\Delta N_{a}\Delta N_{b_{0}}$  and  $(\mp i\sigma_{x}^{(b_{0})})^{1 / 2}$  therefore anticommutes only with  $\sigma_{x}^{(b_{0})}$ . Moreover, the positive sign of  $+\sigma_{x}^{(b)}$  is due to  $b \notin N_{a} - N_{b_{0}} - \{b_{0}\}$ , as well as  $b \notin N_{b_{0}} - N_{a} - \{a\}$ , since in both cases  $\pm$  the term  $\sigma_{z}^{(b)}$  of  $U_{x,\pm}^{(a)}$  commutes with  $\sigma_{x}^{(b)}$ . For  $K_{G}^{(b_{0})}K_{G}^{(b)}$  of  $\mathcal{G}_2$  one computes, for  $b \notin N_{b_0}, b_0 \notin N_b\Delta N_{b_0}, b \in N_a - N_{b_0} - \{b_0\}$ ,

$$
\begin{array}{l} K _ {G} ^ {(b _ {0})} K _ {G} ^ {(b)} = \sigma_ {x} ^ {(b _ {0})} \sigma_ {x} ^ {(b)} \prod_ {{b ^ {\prime} \in N _ {b} \Delta N _ {b _ {0}}}} \sigma_ {z} ^ {(b ^ {\prime})} \\ = U _ {x, \pm} ^ {(a)} \Bigg ((\mp i \sigma_ {y} ^ {(b _ {0})}) \sigma_ {x} ^ {(b _ {0})} (\mp \sigma_ {x} ^ {(b)}) \prod_ {b ^ {\prime} \in N _ {b} \Delta N _ {b _ {0}}} \sigma_ {z} ^ {(b ^ {\prime})} \Bigg) U _ {x, \pm} ^ {(a) \dagger} \\ = U _ {x, \pm} ^ {(a)} \left(\sigma_ {x} ^ {(b)} \prod_ {b ^ {\prime} \in N _ {b} \Delta N _ {b _ {0}} \cup \{b _ {0} \}} \sigma_ {z} ^ {(b ^ {\prime})}\right) U _ {x, \pm} ^ {(a) \dagger}. \tag {72} \\ \end{array}
$$

Instead of  $K_G^{(b)}$  in  $\mathcal{G}_3$  we choose, for  $b \notin N_a$ ,  $b_0 \notin N_b\Delta N_a$ ,  $b \in N_{b_0} - N_a - \{a\}$ ,

$$
\begin{array}{l} \pm \sigma_ {x} ^ {(a)} K _ {G} ^ {(a)} K _ {G} ^ {(b)} = \pm \sigma_ {x} ^ {(b)} \prod_ {b ^ {\prime} \in N _ {b} \Delta N _ {a}} \sigma_ {z} ^ {(b ^ {\prime})} \\ = U _ {x, \pm} ^ {(a)} \Bigg (\pm (\pm \sigma_ {x} ^ {(b)}) \prod_ {b ^ {\prime} \in N _ {a} \Delta N _ {b}} \sigma_ {z} ^ {(b ^ {\prime})} \Bigg) U _ {x, \pm} ^ {(a) \dagger} \\ = U _ {x, \pm} ^ {(a)} \left(\sigma_ {x} ^ {(b)} \prod_ {b ^ {\prime} \in N _ {b} \Delta N _ {a}} \sigma_ {z} ^ {(b ^ {\prime})}\right) U _ {x, \pm} ^ {(a) \dagger}. \tag {73} \\ \end{array}
$$

Moreover, note that  $K_G^{(c)}$  in  $\mathcal{G}_4$  is not changed by  $U_{x,\pm}^{(a)}$  since  $c\in V - (N_a\cup N_{b_0})$ . To summarize, the new neighborhoods  $N_b'$  are

$$
N _ {b} ^ {\prime} = \left\{ \begin{array}{l l} N _ {a} - \left\{b _ {0} \right\} & \text {i f} b = b _ {0}, \\ N _ {b} \Delta N _ {a} \Delta N _ {b _ {0}} \cup \left\{b _ {0} \right\} & \text {i f} b \in N _ {b _ {0}} \cap N _ {a}, \\ N _ {b} \Delta N _ {b _ {0}} \cup \left\{b _ {0} \right\} & \text {i f} b \in N _ {a} - N _ {b _ {0}} - \left\{b _ {0} \right\}, \\ N _ {b} \Delta N _ {a} & \text {i f} b \in N _ {b _ {0}} - N _ {a} - \left\{a \right\}, \\ N _ {b} & \text {i f} b \in V _ {G} - N _ {a} - N _ {b _ {0}}. \end{array} \right. \tag {74}
$$

A comparison shows that these neighborhoods correspond exactly to the graph  $G'$  obtained from Eq. (37). This concludes the proof.

Proof of Proposition 2. This statement follows immediately from Eq. (21) in property (ii) of the Schmidt measure, and the fact that the different measurement results are obtained with probability  $1/2$ .

Proof of Proposition 3. To show Eq. (41), the partial trace over  $A$  can be taken according to the basis of  $A$  given by

$$
\{\left| \mathbf {z} \right\rangle = \underset {a \in A} {\otimes} \left| z, (- 1) ^ {z _ {a}} \right\rangle^ {(a)} \}. \tag {75}
$$

This corresponds to successive local  $\sigma_z$  measurements of all vertices in  $A$ , yielding measurement outcomes  $\pm 1$ . According to Sec. III A, after measurement of  $\sigma_z^{(a)}$  the state of the remaining vertices is the graph state vector  $|G - \{a\} \rangle$  in the case of the outcome  $+1$ , and

$$
\prod_ {c \in N _ {a}} \sigma_ {z} ^ {(c)} | G - \{a \} \rangle , \tag {76}
$$

if the outcome is  $-1$ . This can be summarized as

$$
\left(\prod_ {c \in N _ {a}} \sigma_ {z} ^ {(c)}\right) ^ {z _ {a}} | G - \{a \} \rangle , \tag {77}
$$

where  $z_{a} \in \{0,1\}$  denotes the measurement result  $\pm 1$ . Since the following measurements commute with the previous local unitaries, the final state vector according to the result  $\mathbf{z} = (z_{a})_{a \in A} \in \mathbb{F}_{2}^{A}$  is

$$
\begin{array}{l} \prod_ {a \in A} \prod_ {c \in N _ {a}} \left(\sigma_ {z} ^ {(c)}\right) ^ {z _ {a}} | \mathbf {z} \rangle \otimes | G - A \rangle = \prod_ {a \in A} \prod_ {c \in V} \left(\sigma_ {z} ^ {(c)}\right) ^ {\Gamma_ {c a} z _ {a}} | \mathbf {z} \rangle \otimes | G - A \rangle \\ = \prod_ {a \in A} \left(\sigma_ {z} ^ {(a)}\right) ^ {\langle \mathbf {e} ^ {a} | \Gamma_ {G - B} \mathbf {z} \rangle} | \mathbf {z} \rangle \\ \otimes \prod_ {b \in B} \left(\sigma_ {z} ^ {(b)}\right) ^ {\langle \mathbf {e} ^ {b} | \Gamma_ {A B} \mathbf {z} \rangle} | G - A \rangle , \tag {78} \\ \end{array}
$$

where the computation with respect to  $\mathbf{z}$  is done in  $\mathbb{F}_2^A$  (i.e., modulo 2) and  $\mathbf{e}_a^b = \delta_{ab}$ . Therefore, we arrive at the resulting state vector associated with the result  $\mathbf{z}$  as

$$
(- 1) ^ {\langle \mathbf {z} | \Gamma_ {G - B} \mathbf {z} \rangle} | \mathbf {z} \rangle \otimes \prod_ {b \in B} \left(\sigma_ {z} ^ {(b)}\right) ^ {\langle \mathbf {e} ^ {b} | \Gamma_ {A B} \mathbf {z} \rangle} | G - A \rangle . \tag {79}
$$

Because the possible measurement results are attained with probability  $1/2$ , this proves the validity of Eq. (41) with local unitaries as in Eq. (42), i.e.,

$$
U (\mathbf {z}) = \prod_ {a \in A} \left(\prod_ {b \in N _ {a}} \sigma_ {z} ^ {(b)}\right) ^ {z _ {a}} = \prod_ {b \in B} \left(\sigma_ {z} ^ {(b)}\right) ^ {\langle \mathbf {e} ^ {b} | \Gamma_ {A B} \mathbf {z} \rangle}. \tag {80}
$$

To show the validity of Eq. (43), note that for any  $\mathbf{z}_1, \mathbf{z}_2 \in \mathbb{F}_2^A$ , the state vectors  $U(\mathbf{z}_1) | G - A \rangle$  and  $U(\mathbf{z}_2) | G - A \rangle$  are orthogonal if and only if

$$
U \left(\mathbf {z} _ {1} - \mathbf {z} _ {2}\right) = U \left(\mathbf {z} _ {2}\right) ^ {\dagger} U \left(\mathbf {z} _ {1}\right) \neq 1, \tag {81}
$$

since  $\Pi_{c\in V^{\prime}}\sigma_{z}^{(c)}$  anticommutes with the stabilizer for any graph state and for any  $\varnothing \neq V^{\prime}\subseteq V$  , and therefore takes it into its orthogonal complement. Hence,

$$
\begin{array}{l} \log_ {2} (\operatorname {r a n k} \left(\operatorname {t r} _ {A} [ | G \rangle \langle G | ]\right)) \\ = \log_ {2} (\dim \operatorname {s p a n} \{U (\mathbf {z}) | G - A \}: \mathbf {z} \in \mathbb {F} _ {2} ^ {A}), \tag {82} \\ \end{array}
$$

as for every  $\mathbf{z} \in \mathbb{F}_2^A$  exactly those  $\mathbf{z}' \in \mathbb{F}_2^A$  yield the same  $U(\mathbf{z}') = U(\mathbf{z})$ , for which

$$
\mathbf {z} ^ {\prime} - \mathbf {z} \in \left\{\mathbf {z} \in \mathbb {F} _ {2} ^ {A}: U (\mathbf {z}) = 1 \right\} \tag {83}
$$

holds. This gives

![](images/eb2191f59ee8c915e5fe553d67e50b5964a4bfc64c911a6a7b59fd58a10cdc3d.jpg)  
FIG. 9. A sufficient condition for a graph to have maximal Schmidt rank.

$$
\begin{array}{l} \log_ {2} (\operatorname {r a n k} \left(\operatorname {t r} _ {A} [ | G \rangle \langle G | ]\right)) = | A | - \log_ {2} | \{\mathbf {z} \in \mathbb {F} _ {2} ^ {A}: \langle \mathbf {e} ^ {b} | \Gamma_ {A B} \mathbf {z} \rangle \\ = _ {\mathbb {F} _ {2}} 0 \forall b \in B \} | \\ = | A | - \dim \ker_ {\mathbb {F} _ {2}} (\Gamma_ {A B}) = \operatorname {r a n k} _ {\mathbb {F} _ {2}} (\Gamma_ {A B}). \tag {84} \\ \end{array}
$$

Proof of Proposition 4. To see this, assume to the contrary that  $G_{AB}$  contains no cycles but that the Schmidt rank is not maximal. Then, denote with  $A' \subseteq A$  any subset for which the corresponding columns  $\mathbf{n}^{(a)}$  in  $\Gamma_{AB}$  might add to 0 modulo 2,

$$
\sum_ {a \in A ^ {\prime}} \mathbf {n} ^ {(a)} = _ {\mathrm {F} _ {2}} 0. \tag {85}
$$

Obviously, every vertex  $b \in B' = \cup_{a \in A'} N_a$  must have an even number of distinct neighbors in  $A'$ . For the moment, let the single leaf  $a_1$  be contained in  $A'$  and

$$
a _ {1}, b _ {1}, a _ {2}, \dots , b _ {n - 1}, a _ {n} \tag {86}
$$

be a  $\{a_1, a_n\}$  path with maximal length that alternately crosses the sets  $A'$  and  $B'$  (starting in  $a_1$  and ending in  $A'$  as depicted in Fig. 9). Because  $a_n$  is necessarily a vertex of degree more than 1 in  $G_{AB}$  and by construction also in  $G_{A'B'}$ , it must have a neighbor  $b_n \neq b_{n-1}$  in  $B'$ . If  $b_n = b_i$  for some  $i = 1, \ldots, n-2$ , a contradiction is found. Otherwise  $b_n$  itself must have a neighbor  $a_{n+1} \neq a_n$  in  $A'$ , because  $b_n$  has even degree in  $G_{A'B'}$ . Now either  $a_{n+1} = a_i$  for some  $i = 1, \ldots, n-2$  or the path

$$
a _ {1}, b _ {1}, a _ {2}, \dots , b _ {n - 1}, a _ {n}, b _ {n}, a _ {n + 1} \tag {87}
$$

is a longer path in  $G_{A'B'}$ , both yielding to contradictions with the previous assumptions.

If the single leaf  $a_1$  is not contained in  $A'$ , or if  $A$  contains no leaves, the previous argumentation still holds, because now any  $a \in A'$  must have a degree more than one, if one allows  $a_1 \in A'$  to be arbitrary. The sufficient criterion for the connected components of  $G_{AB}$  then follows from the additivity of  $E_S$  within the given bipartition  $(A,B)$ , as formulated in Eq. (27), after deleting all edges within  $G[A]$  and  $G[B]$ , which is proper  $(A,B)$ -local unitary operation.

Proof of Proposition 5. Let  $G = (V \cup \{a_1, b_1\}, E)$  be a

![](images/2dbc939ee8e3ffb024b0847fbbad5a5f3053ca2de71fb8062b616abbad2b3ffa.jpg)

![](images/3f084be35fcea1baeb007e57073929db9191a1901305b5d10c0bb2dd260832b8.jpg)  
FIG. 10. The situation before and after the LOCC simulation for adding or deleting an edge  $\{a_1, b_1\}$ : the graph state vector  $|G\rangle$  can be transformed by  $(A, B)$ -local operations and classical communication with probability 1 into the state vector  $|G'\rangle$ , where the edge between the partitions  $A_1$  and  $B_1$  is added or deleted. This is possible if one allows for an additional maximally entangled state  $\blacksquare$  —— between  $A_2$  and  $B_2$ . After the LOCC operation the resource is consumed, i.e., the state of  $(A_2, B_2)$  is a pure product state  $\blacksquare \blacksquare$ .

graph. The set  $V$  is the set of all vertices of the graph  $G$ , except the two vertices  $a$  and  $b$  between which an edge is supposed to be deleted or added. Let  $V$  also denote the sequence of partitions in the finest partitioning of  $G$  and  $A_{1} = \{a_{1}\}$ ,  $B_{1} = \{b_{1}\}$ .  $G'$  denotes the resulting graph, which differs from  $G$  in the edge  $\{a_{1}, b_{1}\}$ . As has been shown in Refs. [38-40], the unitary operation corresponding to the Ising interaction, see Eq. (10), can be implemented with LOCC with unit probability. The necessary and sufficient resources are one maximally entangled pair of qubits and one bit of classical communication in each direction (see Fig. 10). The vertices  $a_{2}$  and  $b_{2}$  correspond to the qubits that carry the entanglement  $|\psi\rangle$  resource required to implement the Ising interaction with LOCC. With  $A_{2} = \{a_{2}\}$  and  $B_{2} = \{b_{2}\}$ , we can conclude that

$$
\begin{array}{l} E _ {S} ^ {(V, A _ {1}, B _ {1})} (| G \rangle) + 1 = E _ {S} ^ {(V, A _ {1}, B _ {1})} (| G \rangle) + E _ {S} ^ {(A _ {2}, B _ {2})} (| \psi \rangle) \\ \geqslant E _ {S} ^ {(V, A _ {1}, B _ {1}, A _ {2}, B _ {2})} (| G \rangle \otimes | \psi \rangle), \tag {88} \\ \end{array}
$$

due to subadditivity, and

$$
E _ {S} ^ {(V, A _ {1}, B _ {1}, A _ {2}, B _ {2})} (| G \rangle \otimes | \psi \rangle) \geqslant E _ {S} ^ {(V, A, B)} (| G \rangle \otimes | \psi \rangle), \tag {89}
$$

due to the nonincreasing property under coarse graining of the partition  $A = A_{1} \cup A_{2}$  and  $B = B_{1} \cup B_{2}$ . As the Schmidt measure is an entanglement monotone, LOCC simulation of the Ising interaction yields

$$
\begin{array}{l} E _ {S} ^ {(V, A _ {1}, B _ {1})} (| G \rangle) + 1 \geqslant E _ {S} ^ {(V, A, B)} (| G ^ {\prime} \rangle \otimes | \phi \rangle^ {(a _ {2})} \otimes | \omega \rangle^ {(b _ {2})}) \\ = E _ {S} ^ {(V, A _ {1}, B _ {1})} \left(| G ^ {\prime} \rangle\right), \tag {90} \\ \end{array}
$$

where it has been used that local additional systems can always be appended without change in the Schmidt measure. The state vector  $|\phi \rangle^{(a_2)}\otimes |\omega \rangle^{(b_2)}$  corresponds to the state vector of the additional system after implementation of the Ising gate. Since the Ising interaction gives rise to both a deletion or the addition of an edge, we have arrived at the above

statement. Note that the whole argumentation also holds if  $a_1$  and  $b_1$  are vertices in some coarser partitions  $A_1$  and  $B_1$  of  $G$ . In this case the same simulation with LOCC of the Ising interaction can be used, but in the estimations now with respect to coarser partitions.

Proof of Proposition 6. If a vertex  $a \in V$  is deleted from a graph  $G = (V, E)$ , the corresponding graph state vector  $|G - \{a\} \rangle$  is according to Proposition 1 up to local unitaries the graph state that is obtained from a measurement of  $\sigma_z^{(a)}$  at the vertex  $a$ . According to Eq. (19) the Schmidt measure cannot increase, and because of Eq. (38) it can at most decrease by one.

Proof of Proposition 7. To see this, we can write the adjacency matrix  $\Gamma_G$  according to the partitions of sources  $A$  and sinks  $B$ . Then, for  $\Gamma_G$  in Eq. (39),

$$
\Gamma_ {G [ A ]} = \Gamma_ {G [ B ]} = 0, \tag {91}
$$

and the number of linearly independent columns/rows in  $\Gamma_G$  is twice that of  $\Gamma_{AB}$ . Hence, a lower bound is

$$
E _ {S} ^ {(A, B)} (| G \rangle) = \left\lfloor \frac {1}{2} \operatorname {r a n k} _ {\mathrm {F} _ {2}} (\Gamma_ {G}) \right\rfloor . \tag {92}
$$

If  $\Gamma_G$  is invertible, then

$$
E _ {S} (| G \rangle) \geqslant \left\lfloor \frac {| V |}{2} \right\rfloor \tag {93}
$$

holds. On the other hand, each of the partition  $A$  and  $B$  is a vertex cover of  $G$  and  $E_{S}(|G\rangle)$  is therefore bound from above by the size of the smaller partition, which must be less than  $\lfloor |V| / 2\rfloor$

Proof of Proposition 8. Let  $c \in V - N_{a}$ , then

$$
U K _ {G} ^ {(c)} U ^ {\dagger} = K _ {G} ^ {(c)} = K _ {G ^ {\prime}} ^ {(c)}. \tag {94}
$$

For  $b \in N_{a}$ , one computes

$$
\begin{array}{l} U K _ {G} ^ {(b)} U ^ {\dagger} = (i \sigma_ {z} ^ {(b)}) \sigma_ {x} ^ {(b)} (- i \sigma_ {x} ^ {(a)}) \sigma_ {z} ^ {(a)} \prod_ {b ^ {\prime} \in N _ {b} - \{a \}} \sigma_ {z} ^ {(b ^ {\prime})} \\ = \sigma_ {x} ^ {(a)} \prod_ {b ^ {\prime} \in N _ {a}} \sigma_ {z} ^ {(b ^ {\prime})} \sigma_ {x} ^ {(b)} \prod_ {b ^ {\prime \prime} \in N _ {b} \Delta N _ {a}} \sigma_ {z} ^ {(b ^ {\prime \prime})} \\ = K _ {G ^ {\prime}} ^ {(a)} K _ {G ^ {\prime}} ^ {(b)}. \tag {95} \\ \end{array}
$$

Therefore,

$$
\langle U K _ {G} ^ {(c)} U ^ {\dagger} \rangle_ {c \in V} = \langle K _ {G ^ {\prime}} ^ {(c)} \rangle_ {c \in V}, \tag {96}
$$

which had to be shown.

# V. EXAMPLES

In this section the findings of the previous two sections will be applied to evaluating the Schmidt measure for a number of important graph states. Upper and lower bounds will be investigated, and in most of the subsequently considered cases, these bounds coincide, hence making the computation of this multiparticle entanglement measure possible.

Example 1: The Schmidt measure of a tree is the size of its smallest vertex cover.

![](images/642d4f560c2e5598bd8e5517ba0809b0d95af04cb1a2b011ff02e684d68a8f22.jpg)  
FIG. 11. Graph No. 1 represents a tree. Its bipartitioning  $(A, B)$ , for which in graph No. 2 the vertices in  $A$  are depicted by large boxes  $\blacksquare$ , is neither a minimal vertex cover nor yields maximal partial rank. Instead, the set of vertices  $A$ , represented by large boxes  $\blacksquare$  in graph No. 3, is a minimal vertex cover with maximal partial rank. Here, the edges within the set  $A$  are drawn by thin lines in order to illustrate the resulting graph  $G_{AA^c}$  between  $A$  and its complement, as considered in Sec. III B.

![](images/e0cb983fc4381cd6add2c435d25cdb614b9f218129c905328f1ef4a38938689e.jpg)

![](images/7c9d2a61d0dfa79c7e02a1cfb52a65011decea677440bd3b022e6a49b311b6bb.jpg)

Proof. A tree is a graph that has no cycles. We claim that a minimal vertex cover  $A$  of  $G$  can be chosen, such that the graph  $G_{AB}$  between  $A$  and its complement  $B = A^c$  fulfills the sufficient criterion in Proposition 4 for maximal Schmidt rank. To see this, let  $A$  be a minimal vertex cover. If a connected component  $C_1$  of  $G_{AB}$  has more than one leaf  $a$  in  $A \cap C_1$ , then this can be transferred to another (possibly new) component  $C_2$ , by simply exchanging the leaves in  $A$  with their unique neighbors  $b$  in  $B$ . One again obtains a vertex cover of the same (hence minimal) size. Note that by this exchange the new complement  $B'$  receives no inner edges with respect to  $G$ , since each of the exchanged vertex of  $A$  only had one neighbor in  $B$ .

Two distinct leaves  $a_2$  and  $a_3$  in  $A$  cannot be adjacent to the same vertex  $b \in B$ . Otherwise, taking  $b$  instead of both  $a_2$  and  $a_3$  in  $A$  would yield a vertex cover with fewer vertices. Moreover, two distinct leaves  $a_2$  and  $a_3$  of  $A \cap C_1$  are necessarily transferred to different connected components  $C_2$  and  $C_3$  of  $G_{AB}$ , because otherwise any two elements  $a_2'$  and  $a_3'$  of  $N_{a_2} \cap A$  and  $N_{a_3} \cap A$  are connected by an  $(A, B)$  path, which together with an  $(A, B)$  path between  $a_2$  and  $a_3$  and the edges  $\{a_2, a_2'\}$  and  $\{a_3, a_3'\}$  would form a cycle of  $G$ .

Starting with a component  $C_1'$  apart from one leaf  $a_1$ , all other leaves  $a_2, \ldots, a_k$  can be transferred in this way to different components  $C_2', \ldots, C_k'$ . Let us fix these vertices, including their unique neighbors  $b_1, \ldots, b_k$  for the following reduction of the number of leaves in the components  $C_2', \ldots, C_k'$  in the sense that only vertices which differ from  $a_1, \ldots, a_k, b_1, \ldots, b_k$ , are considered for a subsequent transfer. Since  $G$  is free of cycles, similar to the above argument, none of the remaining leaves is transferred to a component which was already obtained by a previous transfer. In a similar manner, for all remaining components  $C$  the minimal vertex cover can be transformed into a new one  $A'$ , for which  $C \cap A'$  contains only one leaf without affecting components which were already considered in the transfer process. That shows the validity of our claim.

Figure 11 gives an example for a tree for which the Schmidt measure does not coincide with the size of the smaller bipartition, the upper bound according to Proposition 7.

Example 2: The Schmidt measure of a  $1D-$ ,  $2D-$ , and  $3D$ -cluster state is

$$
E _ {S} (| G \rangle) = \left\lfloor \frac {| V |}{2} \right\rfloor . \tag {97}
$$

Proof. To see this, we only consider the 3D case, since the former can be reduced to this. Moreover, note that the 3D cluster does not contain any (induced) cycles of odd length. Therefore, it is 2-colorable and because of Eq. (47), we only have to provide a bipartite split with Schmidt rank  $\lfloor |V| / 2 \rfloor$ . For this we choose a cartesian numbering for the vertices starting in one corner, i.e.,  $(x,y,z)$  with  $x = 1,\dots ,X$ ,  $y = 1,\ldots ,Y$ , and  $z = 1,\ldots ,Z$ .

Let us first assume that  $X$  is an even integer. Then, let  $A = \cup_{x \text{ even}} A_x$  denote the partition consisting of vertices in planes  $A_x$  with even  $x$ , and  $y$  and  $z$  being unspecified. The graph  $G_{AA^c}$  consists of  $Y \times Z$  parallel linear chains, which alternately cross  $A$  and  $A^c$  (see Fig. 12). Since  $|A| = (X/2) \times Y \times Z$ , we have to show that for no subset  $A' \subseteq A$ , Eq. (85) holds. This can easily be done, inductively showing, that vertices in  $A_x$  cannot be contained in  $A'$  for all even  $x = 2, \ldots, X$ , if Eq. (85) shall be satisfied.

For  $x = 2$  this holds, because for every  $a \in A' \cap A_2$  there is a unique adjacent leaf  $b \in A' \cap A_1$ . Moreover, since  $b$  is a leaf,  $n_a^b = 1$  can only hold for one  $a \in A'$ . Therefore,

$$
\sum_ {a \in A ^ {\prime}} n _ {a} ^ {b} \neq_ {\mathrm {F} _ {2}} 0. \tag {98}
$$

For even  $x \geqslant 2$  note that, because  $G$  is a tree, any two  $a_1, a_2 \in A_x$  have disjoint neighborhoods in  $A_{x-1}$ , i.e.,

$$
N _ {a _ {1}} \cap N _ {a _ {2}} \cap A _ {x - 1} = \varnothing . \tag {99}
$$

In order to fulfill Eq. (85), any occurrence of  $a \in A' \cap A_x$  can therefore only be compensated by some  $a' \in A_{x-2}$ , which is impossible by the inductive presumption.

In the case where  $X, Y$ , as well as  $Z$  are odd integers, the previous construction will yield a graph  $G_{AA^c}$  consisting of separate linear chains on

$$
A = \bigcup_ {x = 1, \dots , X - 1} A _ {x} \tag {100}
$$

ending in the plane  $A_{X}$  (see Fig. 13). In this case we add every second row  $A_{Xy}$ ,  $y = 2, \ldots, Z - 1$ , to the partition  $A$ , as well as of the last row  $A_{XZ}$  every second vertex, giving the size

![](images/2508faa2c582d01e959703e7aa93f7f3f977025c8607e34b06782fa17baceb4c.jpg)

![](images/5eb7e771606680a59bac82def8fb735824ad0242bc965ed53943a8cf403040db.jpg)

![](images/b164ae29c90624e009e92f5f7ad2d42e9c6986bc67e4be795da08d9d4dfc81ad.jpg)

![](images/38758adfb2d7e03fdda033f7a9b6fc19add44ae13b9269792258679bbbfa9d8e.jpg)

![](images/a4beb0c92f0c1241e422861e8c8def61d115584c4c89e64f926630a51798990a.jpg)

![](images/6a424d7a0524a00f74cdc93abd454dc41610fd1e71b7e29e007bad353a317dca.jpg)  
FIG. 12. An example for the  $(4,5,3)$ -cluster state and its resulting graph  $G_{AA^c}$  between  $A$  and its complement as considered in Sec. III B. Here, the vertices in  $A$  are depicted by small boxes  $\blacksquare$ .

$$
\left| A \right| = \left\lfloor \frac {X}{2} \right\rfloor \times Y \times Z + \left\lfloor \frac {Y \times Z}{2} \right\rfloor = \left\lfloor \frac {X \times Y \times Z}{2} \right\rfloor . \tag {101}
$$

The inductive argument from above now still holds for all vertices in  $A$ , except from the  $y-z$  plane  $A_x$  and can be continued by a similar argument now considering the rows  $A_{Xy}$  instead of planes. Note that the results could as well be obtained by simply applying the sufficient criterion in Proposition 4 to the stated bipartitioning  $(A, B)$ . However, this

inductive proof may be of interest also for other graph classes.

Example 3: The Schmidt measure of an entangled ring with an even number  $|V|$  of vertices is given by  $|V| / 2$ .

Proof. This is a 2-colorable graph, which gives on the one hand the upper bound of  $|V| / 2$  for the Schmidt measure. On the other hand, by choosing the partitions  $A = \{1,2\}$  and  $B = \{3,4\}$  on the first four vertices, which are increased (for  $|V| > 4$ ) alternately by the rest of the vertices, yielding the partitioning with

$$
A = \{1, 2, 5, 7, \dots , 2 k + 5, \dots , | V | - 1 \} \tag {102}
$$

$$
B = \{3, 4, 6, 8, \dots , 2 k + 6, \dots , | V | \}, \tag {103}
$$

one obtains a bipartitioning  $(A,B)$ , which has maximal Schmidt rank  $E_S^{(A,B)} = |V| / 2$  according to Proposition 4 (see Fig. 14).

Example 4: All connected graphs up to seven vertices.

We have computed the lower and upper bounds to the Schmidt measure, the Pauli persistency, and the maximal partial rank, for the nonequivalent graphs in Figs. 4 and 5. They are listed in Table II, where we have also included the rank index. By the rank index, we simply compressed the information contained in the Schmidt rank list with respect to all bipartite splittings, counting how many times a certain rank occurs in splittings with either two or three vertices in the smaller partition. For example, the rank index  $RI_{3} = (20,12,3)$  of graph number 29 means that the rank 3 occurs 20 times in all possible 3-4 splits, the rank 2 twelve times, and the rank 1 only three times. (Note, that here we use  $\log_2$  of the actual Schmidt rank.) Similarly, because of  $RI_{2} = (18,3)$  the rank 2 (1) occurs 18 (3) times in all 2-5 splits of the graph number 29.

For connected graphs the Schmidt rank, 0 cannot occur for any bipartite splitting  $(A,B)$ , since this would correspond to an empty graph  $G_{AB}$ . Because the rank index is invariant under permutations of the partitions, according to graph isomorphisms, it provides information about whether two graph states are equivalent under local unitaries plus graph isomorphisms as treated in Sec. III E. But note that graph numbers 40, 42, and 44 are examples for nonequivalent graphs with the same rank index. Nevertheless, comparing the list of Schmidt ranks with respect to all bipartitions in detail shows that no permutation of the vertex set exists (especially none which is induced by a proper graph isomorphism on both sides), which would cause a permutation of the corresponding rank list, such that two of the graphs could be locally equivalent. In Table II we have also listed the sizes of the corresponding equivalence classes under LU and graph isomorphisms, as well as whether 2-colorable representatives exist. For 295 of 995 nonisomorphic graphs, the lower and upper bound differs and that in these cases the Schmidt measure also noninteger values in  $\log_2\{1,\dots,2^{|V|}\}$  are possible. As has been discussed in Sec. II C, in this paper we omit the computation of the exact value for the Schmidt measure.

Moreover, note that only graph numbers 8 and 19 have maximal partial rank with respect to all bipartite splits. Entanglement here is distributed symmetrically between all par

![](images/2c1947b6945a9a77567ace12d5928c799df2bbb9e5dd9c8cb21b2c5676100e14.jpg)

![](images/d6d7e8cd494b06233e1be3017a6bbeda29354f124a8c4774215450424c8e0c83.jpg)  
FIG. 13. An example for the  $(7,5,5)$ -cluster state and its resulting graph  $G_{AA^c}$  between  $A$  and its complement as considered in Sec. III B. Here, the vertices in  $A$  are depicted by small boxes  $\blacksquare$ . The picture gives a rotated view on the cluster considered in the proof for the case, that  $X$ ,  $Y$ , and  $Z$  are odd integers. The front plane, consisting of the vertices 1 until 35, is the  $y-z$  plane  $A_X$  in the proof.

![](images/2e1a3b2c0cc102bba4b737c493b71e9185fff7761af369d11c2fd8fcb13437c8.jpg)  
FIG. 14. Graph No. 1 is an entangled ring on 18 vertices. Graph No. 2 represents the resulting graph between the partitions  $A$ , whose vertices are depicted by boxes, and the partition  $B$ , whose vertices are depicted by discs.

![](images/d34930308730baaff3f6698addadcab5134e04a3f808883e88b27d59d305d79a.jpg)  
No.1

ties, which makes it "difficult" to disentangle the state by few measurements. From this one can understand why the gap between the lower and upper bound occurs in such cases. As discussed in Sec. III B of all graph codes with less than seven vertices only these two are candidates for strongly error detecting graph codes introduced in Ref. [7].

Example 5. Concatenated [7,1,3]-CSS code.

The graph  $G$  depicted in Fig. 15 represents an encoding procedure for the concatenated [7,1,3]-CSS code. The corresponding graph state has Schmidt measure 28. For encoding, the qubit at the vertex  $\circ$  can be in an arbitrary state. With the rest of the vertices (initially prepared in the state corresponding to  $|x, + \rangle$ ), it is then entangled by the 2-qubit unitary  $U^{(a,b)}$ , introduced in Eq. (10). Encoding the state at vertex  $\circ$  then means to perform  $\sigma_{x}$  measurements at all vertices of the inner square, yielding the corresponding encoded state on the  $7^{2} = 49$  "outer" vertices. The encoding procedure may alternatively be realized by teleporting the bare qubit, initially located on some ancillary particle, into the graph by performing a Bell measurement on the ancilla and the vertex  $\circ$  of the graph state vector  $|G^{\prime}\rangle$ . Here  $|G^{\prime}\rangle$  denotes the graph

![](images/b762a540ba51038ff4d2b02fea657fc43671a2bc086b496a49a1af75e0756b9d.jpg)  
FIG. 15. Resource graph state for the concatenated [7,1,3]-CSS code.

![](images/b09382ddc5899b71cb6ae905747ba1dfd3ad14413ff41874c0df57fdf11b97ea.jpg)  
No.2

![](images/93367c4042e6e444c15ae6251fb1fc0fd97168a4f446b52919ad164d9fcceb8d.jpg)  
FIG. 16. The graph associated with the QFT on 3 qubits in the one-way quantum computer is represented in graph No. 1, where the boxes denote the input (left) and output (right) vertices. Graph No. 3 is obtained from the first after performing all Pauli measurements according to the protocol in Ref. [3], except from the  $\sigma_{x}$  measurements at the input vertices. More precisely, it is obtained from graph No. 1 after  $\sigma_{y}$  measurements on the vertices 22, 23, 24, 26, 27, 28, 30, 31, 32 and  $\sigma_{x}$  measurements on the vertices 2, 4, 7, 9, 11, 13, 15, 18, 20 have been performed.

state vector obtained from  $|G\rangle$  by seven  $\sigma_{x}$  measurements at all vertices of the inner square except  $\circ$ . In this sense  $G'$  represents the resource for the alternative encoding procedure. It has maximal Schmidt measure 25, whereas the corresponding 0 and 1 code words have Schmidt measure 24. They can be obtained with probability  $1/2$  from  $|G'\rangle$  by a  $\sigma_{z}$  measurement at the vertex  $\circ$ .

Example 6. Quantum Fourier transform (QFT) on 3 qubits.

The graph No. 1 in Fig. 16 is a simple example of an entangled graph state as it occurs in the one-way computer of Refs. [3,10]. This specific example represents the initial resource (part of a cluster) required for the quantum Fourier

transform QFT on 3 qubits [3]. It has Schmidt measure 15, where the partition

$$
A = \{2, 4, 7, 9, 1 1, 1 3, 1 5, 1 8, 2 0, 2 2, 2 4, 2 6, 2 8, 3 0, 3 2 \}
$$

(104)

is a minimal vertex cover with maximal Schmidt rank. In the process of performing the QFT, all vertices except the output vertices 5, 16, 33, are measured locally. During this process, the entanglement of the resource state (with respect to every partitioning) can only decrease. Similar as with the graph state vector  $|G^{\prime}\rangle$  obtained from Fig. 15, graph No. 3 represents the input-independent resource needed for the essential (non-Clifford) part of the QFT protocol [3]. It has Schmidt measure 5, where the partition  $A = \{2,9,10,11,15\}$  now provides a minimal vertex cover with maximal Schmidt rank.

# VI. SUMMARY, DISCUSSION, AND OUTLINE OF FURTHER WORK

In this paper we have developed methods that allow for a qualitative and quantitative description of the multiparticle entanglement that one encounters in graph states. Such graph states capture the intuition of an interaction pattern between quantum systems, with important applications in quantum error correction, quantum communication, and quantum computation in the context of the one-way quantum computer. The Schmidt measure is tailored for a comparably detailed account on the quantum correlations grasping genuine multiparticle entanglement, yet it turns out to be computable for many graph states. We have presented a number of general rules that can be applied when approaching the problem of evaluating the Schmidt measure for general graph states, which are stated mostly in graph theoretical terms. These rules have then been applied to a number of graph states that appear in quantum computation and error correction. Also, all connected graphs with up to seven vertices have been discussed in detail. The formalism that we present here abstracts from the actual physical realization, but as has been pointed out in several instances, a number of well-controllable physical systems, such as neutral atoms in optical lattices, serve as potential candidates to realize such graph states [41,42].

In this paper, the Schmidt measure has been employed to quantify the degree of entanglement, as a generalization of the Schmidt rank in the bipartite setting. This measure is sufficiently coarse to be accessible for systems consisting of many constituents and to allow for an appropriate discussion of multiparticle entanglement in graph states. The approach of quantifying entanglement in terms of rates of asymptotic reversible state transformations, as an alternative, appears unfeasible in the many-partite setting. The question of the minimal reversible entangling generating set (MREGS) in multipartite systems remains unresolved to date, even for quantum systems consisting of three qubits, and despite considerable research effort [43,44]. These MREGS are the (not necessarily finite) sets of those pure states from which any other pure states can be asymptotically prepared in a reversible manner under local operations with classical communi-

cation (LOCC). Hence, it seems unrealistic to date to expect to be able to characterize multiparticle entanglement by the rates that can be achieved in reversible asymptotic state transformations, analogous to the entanglement cost and the distillable entanglement under LOCC operations in bipartite systems. In turn, such a description, if it was to be found, could well turn out to be too detailed to capture entanglement as an algorithmic resource in the context of error correction or the one-way quantum computer, where, needless to say, distributed quantum systems with very many constituents are encountered.

For future investigations, a more feasible characterization of LU equivalence would open up further possibilities. A step that would go significantly beyond the treatment of the present paper would be to consider measurements corresponding to observables not contained in the Pauli group. Unfortunately, in this case the stabilizer formalism is no longer available, at least not in the way we used it in this paper. Such an extension would, however, allow for a complete monitoring of the entanglement resource as it is processed during a quantum computation in the one-way computer, where also measurements in tilded bases play a role.

Finally, taking a somewhat different perspective, one could also extend the identification of edges with interactions to weighted graphs, where a real positive number associated with each edge characterizes the interaction strength (e.g., the interaction time). With such a notion at hand, one could study the quantum correlations as they emerge in more natural systems. One example is given by a Boltzmann system of particles, where each particle follows a classical trajectory but carries a quantum degree of freedom that is affected whenever two particles scatter. With techniques of random graphs, it would be interesting to investigate what kind of multiparticle correlations are being built up when the system starts from a prescribed initial state, or to study the steady state. The answer to these questions depends on the knowledge of the interaction history. A hypothetical observer who is aware of the exact distribution in classical phase space (Laplacian demon perspective) would assign a definite graph corresponding to a pure entangled state to the ensemble. An observer who lacks all or part of this classical information about the particles' trajectories would describe the state by a random mixture of graphs and corresponding quantum states. One example of this latter situation would be a Maxwell demon scenario in which one studies the bipartite entanglement as it builds up between two parts of a container.

# ACKNOWLEDGMENTS

We would like to acknowledge fruitful discussions with D. Schlingemann and M. Van den Nest, as well as with H. Aschauer, W. Dur, R. Raussendorf, and P. Aliferis. For valuable hints on connections to known results in graph theory [33] and multilinear algebra [30], we would like to thank G. Royle and K. Audenaert. This work has been supported by the Deutsche Forschungsgemeinschaft (Schwerpunkt QIV), the Alexander von Humboldt Foundation (Feodor Lynen Grant of JE), the European Commission (IST-2001-38877/-39227, IST-1999-11053), and the European Science Foundation.

[1] D. B. West, Introduction to Graph Theory (Prentice Hall, Upper Saddle River, NJ, 2001).  
[2] R. Diestel, Graph Theory (Springer, Heidelberg, 2000).  
[3] R. Raussendorf, D. E. Browne, and H. J. Briegel, Phys. Rev. A 68, 022312 (2003).  
[4] D. Schlingemann, e-print quant-ph/0305170.  
[5] W. Dür, H. Aschauer, and H. J. Briegel, Phys. Rev. Lett. 91, 107903 (2003).  
[6] M. Grassl, A. Klappenecker, and M. Rötteler, in Proceedings of the 2002 IEEE International Symposium on Information Theory, Lausanne, Switzerland, 2002, p. 45.  
[7] D. Schlingemann and R. F. Werner, Phys. Rev. A 65, 012308 (2002).  
[8] D. Gottesman, Ph.D. thesis, CalTech, Pasadena, CA, 1997.  
[9] H. J. Briegel and R. Raussendorf, Phys. Rev. Lett. 86, 910 (2001).  
[10] R. Raussendorf and H. J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[11] J. Eisert and H. J. Briegel, Phys. Rev. A 64, 022306 (2001).  
[12] D. Schlingemann, Quantum Inf. Comput. 2, 307 (2002).  
[13] T. J. Osborne and M. A. Nielsen, Phys. Rev. A 66, 032110 (2002).  
[14] A. Osterloh, L. Amico, G. Falci, and R. Fazio, Nature (London) 416, 608 (2002).  
[15] J. I. Latorre, E. Rico, and G. Vidal, Quantum Inf. Comput. 4, 048 (2004).  
[16] K. Audenaert, J. Eisert, M. B. Plenio, and R. F. Werner, Phys. Rev. A 66, 042327 (2002).  
[17] M. M. Wolf, F. Verstraete, and J. I. Cirac, Phys. Rev. Lett. 92, 087903 (2004).  
[18] J. K. Stockton, J. M. Geremia, A. C. Doherty, and H. Mabuchi, Phys. Rev. A 67, 022112 (2003).  
[19] K. M. O'Connor and W. K. Wootters, Phys. Rev. A 63, 052302 (2001).  
[20] F. Verstraete, M. Popp, and J. I. Cirac, Phys. Rev. Lett. 92, 027901 (2004).  
[21] M. Plesch and V. Buzek, Phys. Rev. A 67, 012322 (2003) 68, 012313 (2003).  
[22] P. Giorda and P. Zanardi, Phys. Rev. A 68, 062108 (2003).  
[23] M. G. Parker and V. Rijmen, e-print quant-ph/0107106.  
[24] V. Coffman, J. Kundu, and W. K. Wootters, Phys. Rev. A 61, 052306 (2000).  
[25] M. B. Plenio and V. Vedral, J. Phys. A 34, 6997 (2001).

[26] D. Meyer and N. Wallach, J. Math. Phys. 43, 4273 (2002).  
[27] T.-C. Wei and P. M. Goldbart, Phys. Rev. A 68, 042307 (2003).  
[28] H. Barnum and N. Linden, J. Phys. A 34, 6787 (2001).  
[29] W. Dur, G. Vidal, and J. I. Cirac, Phys. Rev. A 62, 062314 (2000).  
[30] For a more detailed discussion of numerical issues we refer to L. De Lathauwer, Ph.D. thesis, Dept. of Electrical Engineering, ESAT, K.U. Leuven, 1997, No. ESAT-SISTA/TR 1997-74, where the problem of finding the minimal linear decomposition of a pure state (rank- $N$  tensors) into product states (product of rank-1 tensors) is discussed in the context of the "Canonical Decomposition" or "Parallel Factors" problem.  
[31] This is the content of the so-called Gottesman-Knill theorem as it is stated in Ref. [32] (Theorem 10.7).  
[32] G. Vidal, Phys. Rev. Lett. 91, 147902 (2003).  
[33] A. Bouchet, Discrete Math. 114, 75 (1993).  
[34] M. Van den Nest, J. Dehaene, and B. De Moor, Phys. Rev. A 69, 022316 (2004); e-print quant-ph/0405023.  
[35] H. Aschauer, J. Calsamiglia, M. Hein, and H. J. Briegel, quant-ph/0306048.  
[36] M. Van den Nest, e-print quant-ph/0404106.  
[37] M. A. Nielsen and I. L. Chuang, Quantum Computation and Information (Cambridge University Press, Cambridge, 2000).  
[38] D. Gottesman, “The Heisenberg Representation of Quantum Computers,” in Proceedings of the XXII International Colloquium on Group Theoretical Methods in Physics, edited by S. P. Corney et al. (International Press, Cambridge, MA, 1999).  
[39] J. Eisert, K. Jacobs, P. Papadopoulos, and M. B. Plenio, Phys. Rev. A 62, 052317 (2000).  
[40] D. Collins, N. Linden, and S. Popescu, Phys. Rev. A 64, 032302 (2001).  
[41] D. Jaksch, H.-J. Briegel, J. I. Cirac, C. W. Gardiner, and P. Zoller, Phys. Rev. Lett. 82, 1975 (1999).  
[42] L.-M. Duan, E. Demler, and M. D. Lukin, Phys. Rev. Lett. 91, 090402 (2003).  
[43] C. H. Bennett, S. Popescu, D. Rohrlich, J. A. Smolin, and A. V. Thapliyal, Phys. Rev. A 63, 012307 (2001).  
[44] N. Linden, S. Popescu, B. Schumacher, and M. Westmoreland, quant-ph/9912039; E. F. Galvao, M. B. Plenio, and S. Virmani, J. Phys. A 33, 8809 (2000); S. Wu and Y. Zhang, Phys. Rev. A 63, 012308 (2001); A. Acin, G. Vidal, and J. I. Cirac, Quantum Inf. Comput. 3, 55 (2003).