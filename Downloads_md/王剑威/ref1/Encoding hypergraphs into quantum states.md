# Encoding hypergraphs into quantum states

Ri Qu, Juan Wang, Zong-shang Li, and Yan-ru Bao

School of Computer Science & Technology, Tianjin University, Tianjin 300072, China and

Tianjin Key Laboratory of Cognitive Computing and Application, Tianjin 300072, China

(Received 16 November 2012; published 13 February 2013)

Ioniciou and Spiller [Phys. Rev. A 85, 062313 (2012)] have recently presented an axiomatic framework for mapping graphs to quantum states of a suitable physical system. Based on their study, we first extend the axiomatic framework to hypergraphs by means of modifying its axioms and consistency conditions. Then we use the axiomatic approach to encode hypergraphs into a different family of quantum states, called the hypergraph states. Moreover, we also try to do the following: (i) show that real equally weighted states, which occur in Grover and Deutsch-Jozsa algorithms, are equivalent to hypergraph states; (ii) describe the relations among hypergraph states, graph states, and stabilizer states; (iii) provide some transformation rules, stated in purely hypergraph theoretical terms, which completely characterize the evolution of hypergraph states under some local operations, including operators in the Pauli group and some special local Pauli measurements; and (iv) investigate some properties of multipartite entanglement of hypergraph states by hypergraph theory.

DOI: 10.1103/PhysRevA.87.022311

PACS number(s): 03.67.Mn, 03.67.Ac

# I. INTRODUCTION

It is well known that any graph state [1-4] can be constructed on the basis of a (simple and undirected) graph. Although graph states can describe a large family of entangled states including cluster states [5], GHZ states, stabilizer states [6], etc., it is clear that they cannot represent all entangled states. To go beyond graph states and still keep the appealing connection to graphs, Ref. [7] introduces an axiomatic framework for mapping graphs to quantum states of a suitable physical system and extends this framework to directed graphs and weighted graphs. Several classes of multipartite entangled states, such as qudit graph states [8], Gaussian cluster states [9], projected entangled pair states [10], and quantum random networks [11], emerge from the axiomatic framework. The main aim of this paper is to develop a different approach of encoding hypergraphs into quantum states. Therefore we generalize the above axiomatic framework to hypergraphs. We use the axiomatic approach to define a different class of quantum states of  $n$  qubits, called the hypergraph states. Any hypergraph state can be constructed by a (undirected) hypergraph as follows: Each vertex of the hypergraph labels a qubit, and each hyperedge is associated with an operator called a hyperedge gate. The hypergraph state is constructed from some initial state by successively applying the hyperedge gate corresponding to each hyperedge of the hypergraph.

A graphical interpretation of quantum states, called spin networks, is pointed out in Ref. [12]. Formally, a spin network is a (directed) graph whose edges are associated with irreducible representations of a compact Lie group and whose vertices are associated with intertwiners of the edge representations adjacent to it [13]. Clearly, it is evaluated by writing down tensors for the intertwiners at the vertices and by contracting their indices as prescribed by the edges. There exist several variations of spin networks, and they have appeared in many areas of physics. The modern form of spin networks is called tensor networks [14,15]. A quantum circuit can be naturally regarded as a tensor network: each gate is

regarded as the corresponding tensor; the qubit (qudit) lines are wires connecting the tensors, or open wires that correspond to the input and output qubits (qudits) [15]. Thus the axiomatic framework in Ref. [7] is used to map graphs into special tensor network states. Reference [15] has shown that any graph state can be simulated by a tensor network. It is clear that our extending framework can also be described by means of tensor networks.

There have been several approaches of mapping (classical) Boolean functions to quantum states which include hypergraph states. Reference [16] introduces the concept of a quantum Boolean function on  $n$  qubits, which is defined as a unitary and Hermitian operator on  $n$  qubits. Clearly, each classical Boolean function  $f: \{0,1\}^n \to \{0,1\}$  may be implemented on a quantum computer by means of the so-called phase oracle  $O_f$  as follows:

$$
O _ {f} | + \rangle^ {\otimes n} = | \psi_ {f} \rangle \equiv \frac {1}{\sqrt {2 ^ {n}}} \sum_ {x = 0} ^ {2 ^ {n} - 1} (- 1) ^ {f (x)} | x \rangle , \tag {1}
$$

where  $|x\rangle$  represents the computational basis states of  $n$  qubits. Since the phase oracle  $O_{f}$  is unitary and Hermitian, it is a quantum Boolean function corresponding to  $f$ . Note that the state  $|\psi_f\rangle$ , called a real equally weighted state in Refs. [17,18], occurs in Grover [19] and Deutsch-Jozsa [20] algorithms. In this paper, we show that real equally weighted states are equivalent to hypergraph states. Thus any real equally weighted state can be constructed by not only a Boolean function but also a hypergraph. It implies that we may investigate the properties of the real equally weighted states by means of hypergraph theory. We also show that hyperedge gates are a class of special quantum Boolean functions which are independent and commutative with each other. Thus each hypergraph can give rise to a quantum Boolean function in a natural way.

Reference [14] shows every Boolean function  $f: \{0, 1\}^n \to \{0, 1\}$  can give rise to a so-called quantum Boolean state which

is expressed (up to a global factor) in the form

$$
\sum_ {x \in \{0, 1 \} ^ {n}} | x \rangle | f (x) \rangle .
$$

Moreover, each Boolean state can be translated into a categorical (Boolean) tensor network state. Note that the state

$$
\sum_ {x \in \{0, 1 \} ^ {n}} \langle - | f (x) \rangle | x \rangle ,
$$

where  $| - \rangle \equiv \frac{1}{\sqrt{2}} (|0\rangle - |1\rangle)$ , is just (up to a global scalar factor) a real equally weighted state, i.e., a hypergraph state. Boolean tensor network states are used to study the decidability questions in Ref. [21] and to define a class of algorithms for efficiently solving some search problems in Ref. [22]. Reference [23] uses symmetries of Boolean functions to unify and extend various constructions of spin Hamiltonians embedding Boolean functions into their ground-state subspaces.

One may ask (i) whether every hypergraph state is of stabilizer states and (ii) whether every hypergraph state is of graph states. If local unitary transformations are not considered, our answers to these questions are both "no". This implies that the relations among hypergraph states, graph states, and stabilizer states are described as follows: hypergraph states include graph states; graph states constitute a subclass of the stabilizer states; and any hypergraph state, constructed by a hypergraph whose rank is more than 2, is not of stabilizer states.

It is clear that one can characterize hypergraph states by means of hypergraph theory. In this paper we show how to translate the action of some local operations (including operators in the Pauli group and some special local Pauli measurements) on hypergraph states into the transformations on their corresponding hypergraphs; that is, to derive some transformation rules, stated in purely hypergraph theoretical terms, which completely characterize the evolution of hypergraph states under these local operations. Moreover, we also study some properties of multipartite entanglement [24] of hypergraph states by hypergraph theory.

This paper is organized as follows: In Sec. II we recall some notations of hypergraphs, Boolean functions, and the Pauli group. We show how to encode hypergraphs into quantum states by an axiomatic framework in Sec. III. In Sec. IV we define hypergraph states by means of the framework given in Sec. III. In Sec. V we show that real equally weighted states are equivalent to hypergraph states. We show how any operator in the Pauli group on a hypergraph state is translated into the operation of adding some specified hyperedges to its corresponding hypergraph in Sec. VI. In Sec. VII we describe the relationships among hypergraph states, graph states, and stabilizer states. We show how some special local Pauli measurements are translated into the operations of deleting the vertices in Sec. VIII. We investigate some properties of multipartite entanglement of hypergraph states in Sec. IX. We summarize our conclusions in Sec. X.

![](images/a17524fa9e7a14485a86c509b0aafe72b95494581edbbbfb51cedc267f3cccaa.jpg)  
(a)  $g_{a}$

![](images/8cc538a653284007eedf64c418a64a297d4e07e79662968d9fa2d02e60f531f3.jpg)  
(b)  $g_{b}$

![](images/28dc081e4437bbc3b55b4fececa2e1da64cc516859f7ed97458f4cb7f5181509.jpg)  
(c)  $g_{c}$

![](images/21f249473173ecbc7075454e61db7bf25a86f52c31b173f128d9e10a32083943.jpg)  
FIG. 1. Examples of hypergraphs. The hypergraphs (a)-(d) have the same vertex set  $\{1,2,3,4\}$ . The hypergraph  $g_{a}$  in (a) has 4 hyperedges:  $\{1\}, \{2,3\}, \{3,4\}$  and  $\{1,2,3\}$ . In (b), the hypergraph  $g_{b}$  also has 4 hyperedges:  $\{\Phi\}, \{1\}, \{3,4\}$  and  $\{1,2,3\}$ . Two hyperedges, i.e.,  $\{2,3\}$  and  $\{3,4\}$ , constitute the hyperedge set of  $g_{c}$  in (c). The hypergraph  $g_{d}$  in (d) has 2 hyperedges:  $\{\Phi\}$  and  $\{3,4\}$ . The hypergraphs  $g_{c}$  and  $g_{d}$  are respectively corresponding to  $g_{a} -_{+} \{1\}$  and  $g_{b} -_{-} \{1\}$  while  $g_{b} = g_{a} + \{\{\Phi\}, \{2,3\}\}$ .  
(d)  $g_{d}$

# II. PRELIMINARIES

Formally, a hypergraph is a pair  $(V,E)$ , where  $V$  is the set of vertices,  $E \subseteq \wp(V)$  is the set of hyperedges and  $\wp(S)$  denotes the power set of the set  $S$ . The set of all hypergraphs of  $n$  vertices is denoted by  $\Theta_n$ . The empty hypergraph is defined as  $(V,\Phi)$ . If a hypergraph only contains the empty hyperedge  $\Phi$  or one-vertex hyperedges (called loops), it is trivial. The rank of a hypergraph  $g$ , denoted by  $\operatorname{ran}(g)$ , is the maximum cardinality of a hyperedge in  $g$ . Moreover, a hypergraph can be depicted by the visual form as shown in Fig. 1. Each vertex is represented as a dot while each hyperedge is represented as a closed curve which encloses the dots corresponding to vertices incident with the hyperedge.

A hypergraph  $(V', E')$  is called a subhypergraph of  $(V, E)$  if  $V' \subseteq V$  and  $E' \subseteq E$ . Two hypergraphs  $(V, E)$  and  $(V', E')$  are isomorphic if there exists a permutation  $P$  on  $V$ ; that is, a 1-1 mapping  $P: V \to V'$ , such that  $V' = P(V)$  and  $E' = \cup_{e \in E} \{P(v) | v \in e\}$ . The vertices incident with the same hyperedge are referred to as being adjacent. A sequence of vertices  $v_1, v_2, \ldots, v_p$  such that  $v_k$  and  $v_{k+1}$  are adjacent for all  $1 \leqslant k \leqslant p-1$  is called a path joining  $v_1$  to  $v_p$ . A hypergraph is connected if any two vertices are joined by a path. Otherwise, it is disconnected. A component of a hypergraph  $g$  is a connected subhypergraph contained in no other connected subhypergraph. The number of components of a hypergraph  $g$  is denoted by  $\operatorname{con}(g)$ .

We define the sum of  $g = (V,E)$  and  $g^{\prime} = (V^{\prime},E^{\prime})$  as  $g\Delta g^{\prime}\equiv (V\cup V^{\prime},E\Delta E^{\prime})$  where  $E\Delta E^{\prime}$  denotes the symmetric difference of  $E$  and  $E^{\prime}$ ; that is,  $E\Delta E^{\prime} = E\cup E^{\prime} - E\cap E^{\prime}$ . Given a hypergraph  $g = (V,E)$ , there are two ways of deleting vertex  $k$  to obtain a new hypergraph  $g^{\prime} = (V^{\prime},E^{\prime})$ : (i) Delete vertex  $k$  in  $V$ , together with all hyperedges incident with  $k$ , which means that  $V^{\prime} = V - \{k\}$  and  $E^{\prime} = E\Delta \{e|k\in e\wedge e\in E\}$ . Denote the obtained hypergraph  $g^{\prime}$  by  $g_{- + }\{k\}$ . (ii) At first delete vertex  $k$  in  $V$  and replace each hyperedge  $e$  incident with  $k$  to  $e - \{k\}$ . Then delete all repeated hyperedges. This implies  $V^{\prime} = V - k$  and  $E^{\prime} = E\Delta \{e|k\in e\wedge e\in E\} \Delta \{e - \{k\} |k\in e\wedge e\in E\}$ . Denote the obtained hypergraph  $g^{\prime}$  by  $g_{- - }\{k\}$ . In Fig. 1, the hypergraphs  $g_{c}$  and  $g_{d}$  are respectively corresponding to  $g_{a} - _{+}\{1\}$  and  $g_{a} - _{-}\{1\}$ . Similar to graph

theory, one can define the vertex cover of a hypergraph  $g = (V,E)$ . If a trivial hypergraph is obtained by deleting all vertices in a subset of  $V$ , then the subset is called a vertex cover of  $g$ . In Fig. 1, the sets  $\{3\}$  and  $\{1,4\}$  are two different vertex covers of the hypergraphs  $g_{a}$ . Moreover, for a set of the hyperedges  $F \subseteq \wp(V)$ , adding all hyperedges of  $F$  to a hypergraph  $g = (V,E)$  will obtain a new hypergraph  $g + F \equiv (V,E\Delta F)$ . The hypergraph  $g_{b} = g_{a} + \{\{\Phi\}, \{2,3\}\}$  is shown in Fig. 1.

Let  $[n] \equiv \{1, 2, \dots, n\}$ . Define a mapping on  $\wp([n])$  as

$$
\forall e \subseteq [ n ], \quad c (e) = \left\{ \begin{array}{l l} 1, & e = \Phi \\ \prod_ {k \in e} x _ {k}, & e \neq \Phi . \end{array} \right. \tag {2}
$$

Then an  $n$ -variable Boolean function  $f(x) \equiv f(x_{1}, x_{2}, \ldots, x_{n})$  can be written as the so-called algebraic normal form as follows:

$$
\bigoplus_ {e \subseteq [ n ]} a _ {e} c (e), \tag {3}
$$

where the coefficients  $a_{e} \in \{0,1\}$  and  $\oplus$  denotes the addition operator over  $\mathbb{Z}_2$ . The algebraic degree and codegree of  $f$  are respectively defined as

$$
\deg (f) \equiv \max  _ {e \in [ n ] \wedge a _ {e} \neq 0} | e |
$$

and

$$
\operatorname {c o d e g} (f) \equiv \min  _ {e \in [ n ] \wedge a _ {e} \neq 0} | e |,
$$

where  $|e|$  denotes the cardinality of the set  $e$ . The quadratic functions are the Boolean functions with algebraic degree at most two. The set of all  $n$ -variable quadratic functions is denoted by  $Q_{n}$ . The set of all  $n$ -variable Boolean functions is denoted by  $\Omega_{n}$ .

For convenience, let  $[n]$  be the set of  $n$  vertices. Then we can construct a 1-1 mapping  $u: \Theta_n \to \Omega_n$  which satisfies  $\forall g = ([n], E) \in \Theta_n$ ,

$$
u (g) = \bigoplus_ {e \in E} c (e). \tag {4}
$$

Moreover, it is clear that  $\forall g,g^{\prime}\in \Theta_{n},u(g\Delta g^{\prime}) = u(g)\oplus u(g^{\prime})$ , which implies that  $(\Theta_n,\Delta)$  is isomorphic with  $(\Omega_n,\oplus)$ . Thus every  $n$ -variable Boolean function can be uniquely represented as a hypergraph of  $n$  vertices.

Denote the 2 by 2 identity matrix by  $I$  and let

$$
\sigma_ {x} \equiv \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right], \quad \sigma_ {y} \equiv \left[ \begin{array}{c c} 0 & - i \\ i & 0 \end{array} \right], \quad \sigma_ {z} \equiv \left[ \begin{array}{l l} 1 & 0 \\ 0 & - 1 \end{array} \right]. \tag {5}
$$

Define  $G_{n}$ , the Pauli group on  $n$  qubits, as  $2^{n}$  by  $2^{n}$  matrices of the form  $\alpha p_{1} \otimes p_{2} \otimes \dots \otimes p_{n}$  for some  $\alpha \in \{1, -1, i, -i\}$  and  $p_{k} \in \{I, \sigma_{x}, \sigma_{y}, \sigma_{z}\}$ . Define  $\sigma_{x}^{(k)}$  as  $\sigma_{x}$  acting on the  $k$ th qubit, i.e.,  $I^{\otimes k-1} \otimes \sigma_{x} \otimes I^{\otimes n-k}$  and similarly for  $\sigma_{y}^{(k)}$  and  $\sigma_{z}^{(k)}$ .

# III. AXIOMATIC FRAMEWORK AND HYPERGRAPHS

Reference [7] has presented an axiomatic framework for encoding graphs into quantum states. The framework defines a class of theories characterized by a triplet  $(H,|\phi\rangle, U)$  where  $H$  is the Hilbert space associated to a vertex,  $|\phi\rangle \in H$  is an initial state, and  $U$  is an edge operator acting on

$H \otimes H$ . A graph  $g$  is mapped to the corresponding state  $|g\rangle$  constructed from the initial state  $|\phi\rangle^{\otimes n}$  by successively applying the edge operator corresponding to each edge in  $g$ . Let  $|+ \rangle \equiv \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$  and  $Z_2 \equiv \mathrm{diag}(1, 1, 1, -1)$ . Then  $(\mathbb{C}^2, |+ \rangle, Z_2)$  is the simplest case and it is used to encode simple graphs into graph states. The framework has been extended to multiple graphs, random graphs, directed graphs, and weighted graphs [7]. In this section, we extend the framework to hypergraphs. We first modify the axioms A1-A3 in Ref. [7] into the following axioms A1' - A3' in order to fit to hypergraphs.

Axiom  $A1'$ : Separability. Suppose two hypergraphs  $g = (V, E)$ ,  $g' = (V', E')$  have no same vertex, i.e.,  $V \cap V' = \Phi$ . Then we have

$$
\left| g \Delta g ^ {\prime} \right\rangle = \left| g \right\rangle \otimes \left| g ^ {\prime} \right\rangle . \tag {6}
$$

Axiom  $A2'$ : Hypergraph isomorphism. If two hypergraphs  $g = (V, E)$ ,  $g' = (V', E')$  are isomorphic, the corresponding density operators  $\rho = |g\rangle \langle g|$  and  $\rho' = |g'\rangle \langle g'|$  satisfy

$$
\rho^ {\prime} = D (P) \rho D (P) ^ {- 1}, \tag {7}
$$

where  $D(P)$  is a matrix representation of the permutation  $P$  on  $V$  mapping  $g$  to  $g'$ .

According to the above two axioms, we can obtain the following proposition:

Proposition 1. Given a hypergraph  $g = (V, E)$  of  $n$  vertices, the corresponding quantum state  $|g\rangle$  belongs to a Hilbert space  $H^{\otimes n}$  of  $n$  identical quantum systems where  $H$  is the Hilbert space associated to a single vertex. Moreover, the empty hypergraph is mapped to  $|\phi\rangle^{\otimes n}$  where  $|\phi\rangle \in H$ .

Proof. It is the same as proposition 1 in Ref. [7].

Axiom  $A3'$ : Universal hyperedge operator. If two hypergraphs  $g = (V, E)$ ,  $g' = (V, E')$  differ by a single hyperedge, i.e.,  $E' = E \cup \{e\}$  where  $e \subseteq V$ , then

$$
\left| g ^ {\prime} \right\rangle = U _ {e} | g \rangle . \tag {8}
$$

The hyperedge operator  $U_{e}$  is independent of  $g$  and  $g^{\prime}$  and depends only on the hyperedge  $e$ .

Given a hypergraph  $g = (V, E)$  of  $n$  vertices, the axioms  $\mathrm{A}1' - \mathrm{A}3'$  provide a constructive way to obtain the corresponding quantum state  $|g\rangle$ : starting from the empty hypergraph  $|\phi\rangle^{\otimes n}$  we apply the hyperedge operator corresponding to each hyperedge in  $E$ ; that is,

$$
| g \rangle = \prod_ {e \in E} U _ {e} | \phi \rangle^ {\otimes n}. \tag {9}
$$

This construction is consistent if the hyperedge operator satisfies the following conditions  $\mathrm{C1}^{\prime} - \mathrm{C3}^{\prime}$  which are a generalization of three consistency conditions in Ref. [7]. Since there are  $n + 1$  types of hyperedges according to the cardinality of a hyperedge, we give the first condition.

Condition  $C1'$ : Variety. There are  $n + 1$  basic operators  $U_0, U_1, \ldots, U_n$  where the operator  $U_k$  acts on  $H^{\otimes k}$  for all  $1 \leqslant k \leqslant n$  and  $U_0 \in \mathbb{C}$  is a constant.

In this paper, we only discuss the undirected hypergraphs. Hence we combine the conditions C2-C3 shown in Ref. [7] into the following condition:

Condition  $C2'$ : Locality and symmetry. The hyperedge operator  $U_{e}$  acts nontrivially only on  $H^{\otimes |e|}$  associated with

vertices in  $e$

$$
U _ {e} = U _ {| e |} \otimes I ^ {\otimes n - | e |}, \tag {10}
$$

with  $I$  the identify acting on the rest. In particular,  $U_{\Phi} = U_0 I^{\otimes n}$ .

Condition  $C3'$ : Commutability. Any two hyperedge operators commute.

We denote the above framework for hypergraphs by a triple  $(H, |\phi\rangle, \{U_k | 0 \leqslant k \leqslant n\})$ . In the following section, we will identify  $H, |\phi\rangle$ , and  $\{U_k | 0 \leqslant k \leqslant n\}$  to construct hypergraph states.

# IV. HYPERGRAPH STATES

We first define some special gates called the hyperedge gates and discuss their properties. Let  $Z_{k}$  be the  $2^{k}$  by  $2^{k}$  diagonal matrix which satisfies

$$
\left(Z _ {k}\right) _ {j j} = \left\{ \begin{array}{l l} - 1, & j = 2 ^ {k} \\ 1 & \text {o t h e r s .} \end{array} \right. \tag {11}
$$

Clearly,  $Z_0$  is equal to  $-1$  and  $Z_1$  is just the Pauli matrix  $\sigma_z$ . If  $k \geqslant 2$ , then  $Z_k$  is a controlled phase operator acting on  $k$  qubits with  $k - 1$  control qubits and one target qubit. Note that  $Z_k$  does not depend on which of  $k$  qubits is the target one.

Suppose  $e \subseteq [n]$ . If  $e = \{i_1, i_2, \ldots, i_k\}$ , define the operator  $Z_e$  as  $Z_k \otimes I^{\otimes n - k}$  which means that  $Z_k$  acts on the  $i_1$ th,  $i_2$ th, ..., and  $i_k$ th qubits while  $I$  acts on the rest, respectively. We call  $Z_e$  a hyperedge gate on  $n$  qubits. Moreover, define the operator  $Z_\Phi$  as  $-I^{\otimes n}$ . Note that  $Z_{\{j\}}$  implies  $Z_1$  acting on the  $j$ th qubit, i.e.,  $Z_{\{j\}} = \sigma_z^{(j)} \in G_n$ .

Clearly, hyperedge gates have the following properties:  $\forall e, e' \subseteq [n]$ , (i)  $Z_{e}$  is Hermitian and unitary, thus  $Z_{e}^{2} = I^{\otimes n}$ ; (ii)  $Z_{e}Z_{e'} = Z_{e'}Z_{e}$ ; (iii)  $Z_{e}$  is independent with the other hyperedge gates, i.e.,  $Z_{e}$  cannot be written by a product expression of the other hyperedge gates. Note that hyperedge gates are a class of special quantum Boolean functions which are independent and commutative with each other. This implies that any hypergraph  $([n], E)$  can give rise to a quantum Boolean function  $\prod_{e \in E} Z_{e}$ .

Given a hypergraph  $g = ([n],E)$ , an  $n$ -qubit state  $|g\rangle$  can be constructed by  $g$  as follows: Each vertex labels a qubit (i.e.,  $H = \mathbb{C}^2$ ) initialized in  $|\phi \rangle = | + \rangle$ . The basic operators are  $Z_{k}$  for all  $0\leqslant k\leqslant n$ . The state  $|g\rangle$  is obtained from the initial state  $| + \rangle^{\otimes n}$  by applying the hyperedge operator  $Z_{e}$  for each hyperedge  $e\in E$ ; that is,

$$
| g \rangle = \prod_ {e \in E} Z _ {e} | + \rangle^ {\otimes n}. \tag {12}
$$

This construction is consistent since the basic operators  $\{Z_k|0\leqslant k\leqslant n\}$  and the hyperedge gates satisfy the conditions  $\mathrm{C1^{\prime} - C3^{\prime}}$  . The state  $|g\rangle$  is called an  $n$  -qubit hypergraph state. Thus hypergraph states correspond to  $(\mathbb{C}^2,| + \rangle ,\{Z_k|0\leqslant k\leqslant n\})$

# V. REAL EQUALLY WEIGHTED STATES AND HYPERGRAPH STATES

It is known that real equally weighted states, which are of the form  $|\psi_f\rangle$  in Eq. (1), occur in Grover and Deutsch-Jozsa algorithms. In this section we discuss the relationship between real equally weighted states and hypergraph states.

We can construct a 1-1 correspondence between  $\{|g\rangle |g\in$ $\Theta_{n}\}$  and  $\{|\psi_f\rangle |f\in \Omega_n\}$  . In fact, it is clear that  $\forall e,e^{\prime}\subseteq [n],$

$$
Z _ {e} | + \rangle^ {\otimes n} = \frac {1}{\sqrt {2 ^ {n}}} \sum_ {x = 0} ^ {2 ^ {n} - 1} (- 1) ^ {c (e)} | x \rangle \tag {13}
$$

and

$$
Z _ {e} Z _ {e ^ {\prime}} | + \rangle^ {\otimes n} = \frac {1}{\sqrt {2 ^ {n}}} \sum_ {x = 0} ^ {2 ^ {n} - 1} (- 1) ^ {c (e) \oplus c \left(e ^ {\prime}\right)} | x \rangle . \tag {14}
$$

By Eqs. (4) and (12), we have  $\forall g = ([n],E)\in \Theta_{n}$

$$
| g \rangle = \prod_ {e \in E} Z _ {e} | + \rangle^ {\otimes n} = \frac {1}{\sqrt {2 ^ {n}}} \sum_ {x = 0} ^ {2 ^ {n} - 1} (- 1) ^ {\oplus c (e)} | x \rangle = | \psi_ {u (g)} \rangle . \tag {15}
$$

Hence this implies that real equally weighted states are equivalent to hypergraph states. In particular, the set of all graph states is just the set  $\{|\psi_f\rangle |f\in Q_n\wedge \mathrm{codeg}(f) = 2\}$ . This implies that hypergraph states include graph states.

# VI. OPERATORS IN PAULI GROUP AND ADDING HYPEREDGES

In this section we show that any operator in the Pauli group on a hypergraph state can be translated into the operation of adding some specified hyperedges to the corresponding hypergraph.

Proposition 2. Let  $g = ([n], E)$  be a hypergraph, and let  $U \in \{\sigma_x^{(k)}, \sigma_z^{(k)}\}$  where  $k \in [n]$ . Then the state  $|g'\rangle = U|g\rangle$  is corresponding to the hypergraph  $g' = ([n], E')$  where

$$
E ^ {\prime} = \left\{ \begin{array}{l l} E \Delta \{e - \{k \} | k \in e \wedge e \in E \}, & U = \sigma_ {x} ^ {(k)} \\ E \Delta \{\{k \} \}, & U = \sigma_ {z} ^ {(k)}. \end{array} \right. \tag {16}
$$

It implies that  $\sigma_x^{(k)}$  responds to adding all hyperedges of  $\{e - \{k\} | k \in e \wedge e \in E\}$  to  $g$  while  $\sigma_z^{(k)}$  is corresponding to adding the hyperedge  $\{k\}$  to  $g$ . In Fig. 1, the hypergraph  $g_a$  is transformed into  $g_b$  by applying  $\sigma_x^{(1)}$  on the hypergraph state  $|g_a\rangle$ .

Proof. From Eq. (15), we have  $|g\rangle = |\psi_{u(g)}\rangle$  and  $u(g)(x) = \oplus_{e\in E}c(e)$ . It is well known that each  $f\in \Omega_n$  can be written as

$$
\begin{array}{l} f (x) = \left(1 - x _ {k}\right) f \left(x _ {1}, \dots , x _ {k - 1}, 0, x _ {k + 1}, \dots , x _ {n}\right) \\ + x _ {k} f \left(x _ {1}, \dots , x _ {k - 1}, 1, x _ {k + 1}, \dots , x _ {n}\right). \tag {17} \\ \end{array}
$$

Thus we can obtain

$$
\begin{array}{l} | g \rangle = \frac {1}{\sqrt {2 ^ {n}}} \sum_ {x _ {1} = 0} ^ {1} \dots \sum_ {x _ {k - 1} = 0} ^ {1} \sum_ {x _ {k + 1} = 0} ^ {1} \dots \sum_ {x _ {n} = 0} ^ {1} (- 1) ^ {u (g) \left(x _ {1}, \dots , x _ {k - 1}, 0, x _ {k + 1}, \dots , x _ {n}\right)} | x _ {1} \dots x _ {k - 1} x _ {k + 1} \dots x _ {n} \rangle | 0 \rangle^ {(k)} \\ + \frac {1}{\sqrt {2 ^ {n}}} \sum_ {x _ {1} = 0} ^ {1} \dots \sum_ {x _ {k - 1} = 0} ^ {1} \sum_ {x _ {k + 1} = 0} ^ {1} \dots \sum_ {x _ {n} = 0} ^ {1} (- 1) ^ {u (g) \left(x _ {1}, \dots , x _ {k - 1}, 1, x _ {k + 1}, \dots , x _ {n}\right)} | x _ {1} \dots x _ {k - 1} x _ {k + 1} \dots x _ {n} \rangle | 1 \rangle^ {(k)}. \tag {18} \\ \end{array}
$$

When  $U = \sigma_{x}^{(k)}$ , we have

$$
\begin{array}{l} | g ^ {\prime} \rangle = \sigma_ {x} ^ {(k)} | g \rangle = \frac {1}{\sqrt {2 ^ {n}}} \sum_ {x _ {1} = 0} ^ {1} \dots \sum_ {x _ {k - 1} = 0} ^ {1} \sum_ {x _ {k + 1} = 0} ^ {1} \dots \sum_ {x _ {n} = 0} ^ {1} (- 1) ^ {u (g) (x _ {1}, \dots , x _ {k - 1}, 0, x _ {k + 1}, \dots , x _ {n})} | x _ {1} \dots x _ {k - 1} x _ {k + 1} \dots x _ {n} \rangle | 1 \rangle^ {(k)} \\ + \frac {1}{\sqrt {2 ^ {n}}} \sum_ {x _ {1} = 0} ^ {1} \dots \sum_ {x _ {k - 1} = 0} ^ {1} \sum_ {x _ {k + 1} = 0} ^ {1} \dots \sum_ {x _ {n} = 0} ^ {1} (- 1) ^ {u (g) \left(x _ {1}, \dots , x _ {k - 1}, 1, x _ {k + 1}, \dots , x _ {n}\right)} | x _ {1} \dots x _ {k - 1} x _ {k + 1} \dots x _ {n} \rangle | 0 \rangle^ {(k)} \\ = \frac {1}{\sqrt {2 ^ {n}}} \sum_ {x _ {1} = 0} ^ {1} \sum_ {x _ {2} = 0} ^ {1} \dots \sum_ {x _ {n} = 0} ^ {1} (- 1) ^ {u (g) \left(x _ {1}, \dots , x _ {k - 1}, 1 \oplus x _ {k}, x _ {k + 1}, \dots , x _ {n}\right)} | x _ {1} x _ {2} \dots x _ {n} \rangle . \tag {19} \\ \end{array}
$$

It is clear that  $u(g)(x_1, \ldots, x_{k-1}, 1 \oplus x_k, x_{k+1}, \ldots, x_n) = \oplus_{e' \in E} \Delta\{e - \{k\} | k \in e \wedge e \in E\} c(e')$ . Thus we can get  $E' = E \Delta\{e - \{k\} | k \in e \wedge e \in E\}$ . When  $U = \sigma_z^{(k)}$ , we have  $E' = E \Delta\{\{k\}\}$  in that  $\sigma_z^{(k)} = Z_{\{k\}}$ .

It is well known that the Pauli group  $G_{n}$  can be generated by the set  $\{iI^{\otimes n}\} \cup \{\sigma_x^{(k)},\sigma_z^{(k)}|k\in [n]\}$ . This means that any operator  $U\in G_{n}$  transforms a hypergraph into a new one (up to the global phase  $i$ ) according to the above proposition. Moreover,  $U$  is translated into the operation of adding the associated hyperedges.

# VII. HYPERGRAPH STATES, GRAPH STATES, AND STABILIZER STATES

In this section we answer the following questions: (i) whether every hypergraph state is of stabilizer states and (ii) whether every hypergraph state is of graph states. Thereby, we describe the relations among stabilizer states, graph states, and hypergraph states. Note that local unitary transformations are not considered in this section.

An  $n$ -qubit stabilizer state  $|\varphi \rangle$  is defined as a simultaneous eigenstate with eigenvalue  $1$  of  $n$  commuting and independent operators in the Pauli group  $G_{n}$ . The set  $\{M|M|\varphi \rangle = |\varphi \rangle \wedge M \in G_{n}\}$  is called the stabilizer of  $|\varphi \rangle$ . We first answer the question (i) as follows:

Proposition 3. If the rank of a hypergraph  $g = ([n], E)$  is more than 2, then the corresponding hypergraph state  $|g\rangle$  is not any stabilizer state.

Proof. According to the definition of the hypergraph states, we can obtain  $|g\rangle = \prod_{e\in E}Z_e| + \rangle^{\otimes n}$ . Clearly, the state  $| + \rangle^{\otimes n}$  is of stabilizer states, and its stabilizer is generated by the set  $\{\sigma_x^{(k)}|k\in [n]\}$ . Assume that  $|g\rangle$  is a stabilizer state. It would be true that

$$
\left(\prod_ {e \in E} Z _ {e}\right) \sigma_ {x} ^ {(k)} \left(\prod_ {e \in E} Z _ {e}\right) ^ {\dagger} \in G _ {n}
$$

for all  $k \in [n]$ . Since  $\mathrm{ran}(g) > 2$ , there exist a hyperedge  $e_r$  and an integer  $j$  such that  $|e_r| = \mathrm{ran}(g) > 2$  and  $j \in e_r$ . According to proposition 2, we have

$$
\begin{array}{l} \left(\prod_ {e \in E} Z _ {e}\right) \sigma_ {x} ^ {(j)} \left(\prod_ {e \in E} Z _ {e}\right) ^ {\dagger} | + \rangle^ {\otimes n} \\ = \prod_ {e \in E} Z _ {e} \cdot \prod_ {e \in E \Delta \{e ^ {\prime} - \{j \} | j \in e ^ {\prime} \wedge e ^ {\prime} \in E \}} Z _ {e} | + \rangle^ {\otimes n} \\ = \prod_ {e \in \{e ^ {\prime} - \{j \} | j \in e ^ {\prime} \wedge e ^ {\prime} \in E \}} Z _ {e} | + \rangle^ {\otimes n}. \tag {20} \\ \end{array}
$$

Clearly,  $e_r - \{j\} \in \{e' - \{j\}|j \in e' \land e' \in E\}$  and  $|e_r - \{j\}| \geqslant 2$ . Thus

$$
\prod_ {e \in \{e ^ {\prime} - \{j \} | j \in e ^ {\prime} \wedge e ^ {\prime} \in E \}} Z _ {e} \notin G _ {n},
$$

which is contradictory with

$$
\left(\prod_ {e \in E} Z _ {e}\right) \sigma_ {x} ^ {(j)} \left(\prod_ {e \in E} Z _ {e}\right) ^ {\dagger} \in G _ {n}.
$$

As all graph states constitute a subclass of stabilizer states, the above hypergraph state is also not of graph states. Thus we can describe the relations among hypergraph states, graph states, and stabilizer states: hypergraph states include graph states; graph states constitute a subclass of the stabilizer states; and any hypergraph state, constructed by a hypergraph whose rank is more than 2, is not of stabilizer states. This is shown in Fig. 2.

# VIII. LOCAL PAULI MEASUREMENTS AND DELETING VERTICES

It is well known that any projective measurement associated with operators in the Pauli group can be treated within the stabilizer formalism [6]. Since any stabilizer state is local equivalent to a graph state [25], any measurement of operators in the Pauli group turns a given graph state into a new one (up to local unitaries). It cannot be directly generalized to hypergraph states because some hypergraph states are not of stabilizer states according to the above section. However, we find the Pauli measurement of  $\sigma_z^{(k)}$  can turn a given hypergraph state into another one.

Proposition 4. Let  $g = ([n], E)$  be a hypergraph, and let  $|g\rangle$  be its hypergraph state. If a local measurement of  $\sigma_z^{(k)}$  on

![](images/18d7812d2415e661f6d7b75ba8548020a2e5b6d40c8d9f4075cc0fdc64b523b0.jpg)  
FIG. 2. The relations among hypergraph states, graph states and stabilizer states. Graph states constitute a subclass of hypergraph states or stabilizer states. The intersection of hypergraph states and stabilizer states of  $n$  qubits is the set  $\{|g\rangle |g\in \Theta_n\land ran(g)\leqslant 2\}$ .

the qubit associated with vertex  $k \in [n]$  is performed, then the resulting state, depending on the outcome  $j \in \{1, -1\}$ , is given by

$$
| 0 \rangle^ {(k)} \langle 0 | g \rangle = | g - _ {+} \{k \} \rangle \otimes | 0 \rangle^ {(k)}, \quad j = 1 \tag {21}
$$

$$
| 1 \rangle^ {(k)} \langle 1 | g \rangle = | g - _ {-} \{k \} \rangle \otimes | 1 \rangle^ {(k)}, \quad j = - 1.
$$

It implies that two possible resulting states are respectively corresponding to two ways of deleting the vertex  $k$ .

Proof. According to Eq. (15),  $|g\rangle = |\psi_{u(g)}\rangle$  and  $u(g)(x) = \oplus_{e\in E}c(e)$ . Clearly, we also obtain the expression (18). It is known that

$$
u (g) \left(x _ {1}, \dots , x _ {k - 1}, 0, x _ {k + 1}, \dots , x _ {n}\right) = \underset {e ^ {\prime} \in E \Delta \{e | k \in e \wedge e \in E \}} {\oplus} c \left(e ^ {\prime}\right) \tag {22}
$$

and

$$
\begin{array}{l} u (g) \left(x _ {1}, \dots , x _ {k - 1}, 1, x _ {k + 1}, \dots , x _ {n}\right) \\ = \underset {e ^ {\prime} \in E \Delta \{e | k \in e \wedge e \in E \}} {\oplus} \Delta \left\{e - \{k \mid k \in e \wedge e \in E \right\} c \left(e ^ {\prime}\right), \tag {23} \\ \end{array}
$$

which combined with Eq. (18) gives Eq. (21).

Figure 1 shows that the hypergraph  $g_{a}$  is transformed into one of  $g_{c}$  (when the outcome is 1) and  $g_{d}$  (when the outcome is -1) by performing a local measurement of  $\sigma_{z}^{(1)}$  on the state  $|g_{a}\rangle$ . Note that there exists a relation between  $|g - _{+}\{k\} \rangle$  and  $|g - _{-}\{k\} \rangle$ : let  $|g^{\prime}\rangle = \delta_{x}^{(k)}|g\rangle$ , then  $|g - _{-}\{k\} \rangle = |g^{\prime} - _{+}\{k\} \rangle$ . By the above proposition, it is known that any measurement of the set generated by  $\{\sigma_z^{(k)}|k\in [n]\} \cup \{-I^{\otimes n}\}$  can turn a given hypergraph state into another one.

# IX. ENTANGLEMENT

Entanglement is a major resource in quantum information processing. In this section, we first investigate the entanglement structure of hypergraph states. Then we quantify the entanglement in hypergraph states by the Schmidt measure [26] and give some properties.

A pure state is  $m$ -separable if it can be written as tensor products of pure states of  $m$  subsystems [24]. An  $n$ -qubit pure state is fully separable if it is  $n$ -separable. Otherwise, it is entangled. If an  $n$ -qubit pure state is not biseparable, it is completely entangled. The entanglement structure of real equally weighted states has been investigated in Refs. [17,18]. In this section, we study the entanglement structure of hypergraph states by hypergraph theoretical terms.

Proposition 5. Let  $g = ([n], E)$  be a hypergraph. Then the state  $|g\rangle$  is  $m$ -separable if and only if there are  $m$  subhypergraphs  $g_1 = (V_1, E_1)$ ,  $g_2 = (V_2, E_2)$ , ...,  $g_m = (V_m, E_m)$  such that  $\{V_1, V_2, \ldots, V_m\}$  is a partition of  $[n]$ ,  $E = \cup_{1 \leqslant k \leqslant m} E_k$  and  $|g\rangle = \otimes_{1 \leqslant k \leqslant m} |g_k\rangle$ .

Proof: (i) "if". It is clear that  $E_{j} \cap E_{k} = \Phi$  for all  $j \neq k$ . Thus we have

$$
\begin{array}{l} | g \rangle = \prod_ {e \in E} Z _ {e} | + \rangle^ {\otimes n} \\ = \prod_ {e \in E _ {1}} Z _ {e} | + \rangle^ {\otimes | V _ {1} |} \otimes \prod_ {e \in E _ {2}} Z _ {e} | + \rangle^ {\otimes | V _ {2} |} \\ \otimes \dots \otimes \prod_ {e \in E _ {m}} Z _ {e} | + \rangle^ {\otimes | V _ {m} |}. \tag {24} \\ \end{array}
$$

(ii) "only if". Since  $|g\rangle$  is  $m$  separable, the state  $|g\rangle$  can be written as  $|\varphi_1\rangle \otimes |\varphi_2\rangle \otimes \dots \otimes |\varphi_m\rangle$  where  $|\varphi_1\rangle$ ,  $|\varphi_2\rangle$ , ...,  $|\varphi_m\rangle$  are the real equally weighted states [18]. The states  $|\varphi_1\rangle$ ,  $|\varphi_2\rangle$ , ...,  $|\varphi_m\rangle$  are also of hypergraph states according to Sec. V.

From the above proposition, one can glimpse the entanglement structure of any hypergraph state by merely looking at its corresponding hypergraph. This is shown in the following corollary.

Corollary 6. Let  $g = ([n], E)$  be a hypergraph. Then (i) the state  $|g\rangle$  is fully separable if and only if the hypergraph  $g$  is trivial; (ii) if the state  $|g\rangle$  is completely entangled if and only if the hypergraph  $g$  is connected; (iii) if the state  $|g\rangle$  is  $m$ -separable, then  $m \leqslant \mathrm{con}(g)$ ; (iv) if the state  $|g\rangle$  is  $m$ -separable, then  $m \leqslant \min\{n - \mathrm{ran}(g) + 1, n\}$ ; (v) if  $E$  contains the hyperedge  $[n]$ , then the state  $|g\rangle$  is completely entangled.

From (v) in the above corollary, the number of completely entangled states in  $\{|g\rangle |g\in \Theta_n\}$  is at least  $2^{2^n -1}$  since the number of hypergraphs containing the hyperedge  $[n]$  is  $2^{2^{n} - 1}$ . Moreover, when  $n\to \infty$  the states in  $\{|g\rangle |g\in \Theta_n\}$  are nearly completely entangled; that is, the hypergraphs of  $\Theta_{n}$  are almost connected. In fact, the number of disconnected hypergraphs of  $\Theta_{n}$ , denoted by  $N_{\mathrm{discon}}$ , satisfies

$$
\begin{array}{l} N _ {\text {d i s c o n}} \leqslant \sum_ {k = 1} ^ {n - 1} B (n, k) 2 ^ {2 ^ {k}} 2 ^ {2 ^ {n - k}} \\ \leqslant \sum_ {k = 1} ^ {n - 1} B (n, k) 2 ^ {2 ^ {n - 1} + 2} = (2 ^ {n} - 2) 2 ^ {2 ^ {n - 1} + 2}, \tag {25} \\ \end{array}
$$

where  $B$  denotes the binomial coefficient. It is known that  $|\Theta_n| = 2^{2^n}$ . Thus we have

$$
\lim  _ {n \rightarrow \infty} \frac {N _ {\text {d i s c o n}}}{2 ^ {2 ^ {n}}} \leqslant \lim  _ {n \rightarrow \infty} \frac {(2 ^ {n} - 2) 2 ^ {2 ^ {n - 1} + 2}}{2 ^ {2 ^ {n}}} = 0. \tag {26}
$$

It means that for large  $n$  some quantum algorithms (e.g., the Grover search algorithm) typically employ complete entanglement.

Reference [1] has characterized and quantified the multipartite entanglement of graph states in terms of the Schmidt measure. The Schmidt measure  $E_{S}$  has the following properties [1,26]: (i)  $E_{S}(|\varphi \rangle) = 0$  if and only if  $|\varphi \rangle$  is a product (i.e., fully separable) state; (ii)  $E_{S}$  is an entanglement monotone that does not increase under stochastic local operations with classical communications (SLOCC). In particular,  $E_{S}$  is invariable under local unitaries; (iii)  $E_{S}(|\varphi \rangle + |\phi \rangle) \leqslant \max \{E_{S}(|\varphi \rangle), E_{S}(|\phi \rangle)\} + 1$ ; (iv)  $E_{S}(|\varphi \rangle \otimes |\phi \rangle) = E_{S}(|\varphi \rangle)$  if  $|\phi \rangle$  is fully separable.

Let  $g = ([n], E)$  be a hypergraph. Then we can obtain the following propositions according to these properties of the Schmidt measure.

Proposition 7. Let  $F = \{e - \{k\} | k \in e \land e \in E\}$  where  $k \in [n]$ . Then we have  $E_{s}(|g\rangle) = E_{s}[|g^{\prime}\rangle]$  where  $g^{\prime} = ([n],E\Delta F)$ .

Proof. It is known that  $|g^{\prime}\rangle = \sigma_{x}^{(k)}|g\rangle$  by proposition 2. Thus  $E_{s}(|g\rangle) = E_{s}[|g^{\prime}\rangle ]$ .

Proposition 8. Let  $E_{s}^{k} = \max \{E_{s}(|g| - _{+}\{k\})\}$ ,  $E_{s}(|g| - _{-}\{k\})$  where  $k \in [n]$ . Then we have  $E_{s}^{k} \leqslant E_{s}(|g\rangle) \leqslant E_{s}^{k} + 1$ .

Proof. Clearly,  $E_{s}(|g -_{+}\{k\}) \leqslant E_{s}(|g\rangle)$  and  $E_{s}(|g -_{-}\{k\}) \leqslant E_{s}(|g\rangle)$  by proposition 4. Thus  $E_{s}^{k} \leqslant E_{s}(|g\rangle)$ . It is known that  $|g\rangle = \frac{1}{\sqrt{2}} (|g -_{+}\{k\}) \otimes$

$|0\rangle^{(k)} + |g - _{-}\{k\} \rangle \otimes |1\rangle^{(k)})$  , which implies  $E_{s}(|g\rangle)\leqslant$ $E_{s}^{k} + 1$  
According to the above proposition and the definition of vertex cover, the following proposition can be easily obtained.  
Proposition 9. The Schmidt measure of the hypergraph state  $|g\rangle$  is less than or equal to the cardinality of minimal vertex cover of the hypergraph  $g$ .

# X. CONCLUSION

In this paper we develop an axiomatic framework for encoding hypergraphs into quantum states, which implies that hypergraphs will play an important role in characterizing several families of multipartite quantum states. To see this, we use the axiomatic framework to define the hypergraph states which are equivalent to real equally weighted states.

Therefore one can investigate the properties of real equally weighted states by hypergraph theory. For instance, we provide some transformation rules, stated in purely hypergraph theoretical terms, which completely characterize the evolution of hypergraph states under some local operations, including operators in the Pauli group and some special local Pauli measurements. Moreover, we also investigate some properties of multipartite entanglement of hypergraph states by means of hypergraph theory.

# ACKNOWLEDGMENTS

This work was financially supported by the National Natural Science Foundation of China under Grant No. 61170178. The authors would like to thank the anonymous referee whose comments improved the quality of this paper.

[1] M. Hein, J. Eisert, and H. J. Briegel, Phys. Rev. A 69, 062311 (2004).  
[2] H. Aschauer, W. Dur, and H. J. Briegel, Phys. Rev. A 71, 012319 (2005).  
[3] R. Raussendorf, D. E. Browne, and H. J. Briegel, Phys. Rev. A 68, 022312 (2003).  
[4] R. Raussendorf and H. J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[5] H. J. Briegel and R. Raussendorf, Phys. Rev. Lett. 86, 910 (2001).  
[6] D. Gottesman, Phys. Rev. A 54, 1862 (1996); 57, 127 (1998).  
[7] R. Ioniciou and T. P. Spiller, Phys. Rev. A 85, 062313 (2012).  
[8] S. Y. Looi et al., Phys. Rev. A 78, 042303 (2008).  
[9] N. C. Menicucci, S. T. Flammia, and P. van Loock, Phys. Rev. A 83, 042335 (2011).  
[10] F. Verstraete et al., Phys. Rev. Lett. 96, 220601 (2006); D. Pérez-García et al., Quantum Inf. Comput. 8, 650 (2008); N. Schuch et al., Phys. Rev. Lett. 98, 140506 (2007).  
[11] S. Perseguers et al., Nat. Phys. 6, 539 (2010).  
[12] R. Penrose, in Quantum Theory and Beyond: Essays and Discussions Arising from a Colloquium, edited by T. Bastin (Cambridge University Press, Cambridge, 1971), p. 151.

[13] J. C. Baez, Adv. Math. 117, 253 (1996); H. Pfeiffer, Adv. Theor. Math. Phys. 6(6), 827 (2002), also see arXiv:gr-qc/0211106.  
[14] J. D. Biamonte, S. R. Clark, and D. Jaksch, AIP Adv. 1, 042172 (2011).  
[15] Igor L. Markov and Yaoyun Shi, SIAM J. Comput. 38, 963 (2008).  
[16] A. Montanaro and T. J. Osborne, Chicago J. Theor. Computer Science 2010, 1 (2010), http://cjtcs.cs.uchicago.edu/, also see arXiv:0810.2435 [quant-ph].  
[17] D. Bruß and C. Macchiavello, Phys. Rev. A 83, 052313 (2011).  
[18] Ri Qu and Yanru Bao, arXiv:1207.2518 [quant-ph].  
[19] L. Grover, Proceedings of the 28th Annual ACM Symposium on the Theory of Computing (ACM Press, New York, 1996), p. 212.  
[20] D. Deutsch and R. Jozsa, Proc. R. Soc. London A 439, 553 (1992).  
[21] J. Morton and J. Biamonte, Phys. Rev. A 86, 030301(R) (2012).  
[22] T. H. Johnson et al., Sci. Rep. 3, 1235 (2013).  
[23] J. D. Whitfield, M. Faccin, and J. D. Biamonte, Europhys. Lett. 99, 57004 (2012).  
[24] R. Horodecki et al., Rev. Mod. Phys. 81, 865 (2009).  
[25] M. Nest, J. Dehaene, and B. Moor, Phys. Rev. A 69, 022316 (2004); D. Schlingemann, Quantum Inf. Comput. 2, 307 (2002).  
[26] J. Eisert and H. J. Briiegel, Phys. Rev. A 64, 022306 (2001).