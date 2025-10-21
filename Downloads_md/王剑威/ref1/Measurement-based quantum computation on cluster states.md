# Measurement-based quantum computation on cluster states

Robert Raussendorf, Daniel E. Browne,\* and Hans J. Briegel Theoretische Physik, Ludwig-Maximilians-Universität München, München, Germany (Received 18 February 2003; published 25 August 2003)

We give a detailed account of the one-way quantum computer, a scheme of quantum computation that consists entirely of one-qubit measurements on a particular class of entangled states, the cluster states. We prove its universality, describe why its underlying computational model is different from the network model of quantum computation, and relate quantum algorithms to mathematical graphs. Further we investigate the scaling of required resources and give a number of examples for circuits of practical interest such as the circuit for quantum Fourier transformation and for the quantum adder. Finally, we describe computation with clusters of finite size.

DOI: 10.1103/PhysRevA.68.022312

PACS number(s): 03.67.Lx

# I. INTRODUCTION

Recently, we introduced the scheme of the one-way quantum computer  $(\mathrm{QC}_{\mathcal{C}})$  [1]. This scheme uses a given entangled state, the so-called cluster state [2], as its central physical resource. The entire quantum computation consists only of a sequence of one-qubit projective measurements on this entangled state. Thus, it uses measurements as the central tool to drive a computation [3-6]. We called this scheme the "one-way quantum computer" since the entanglement in the cluster state is destroyed by the one-qubit measurements and therefore it can only be used once. To emphasize the importance of the cluster state for the scheme, we use the abbreviation  $\mathrm{QC}_{\mathcal{C}}$  for "one-way quantum computer."

The  $\mathrm{QC}_{\mathcal{C}}$  is universal since any unitary quantum logic network can be simulated on it efficiently. The  $\mathrm{QC}_{\mathcal{C}}$  can thus be explained as a simulator of quantum logic networks. However, the computational model that emerges for the  $\mathrm{QC}_{\mathcal{C}}$  [7] makes no reference to the concept of unitary evolution and it shall be pointed out from the beginning that the network model does not provide the most suitable description for the  $\mathrm{QC}_{\mathcal{C}}$ . Nevertheless, the network model is the most widely used form of describing a quantum computer and therefore the relation between the network model and the  $\mathrm{QC}_{\mathcal{C}}$  must be clarified.

The purpose of this paper is threefold. First, it is to give the proof for universality of the  $\mathrm{QC}_{\mathcal{C}}$ ; second, to relate quantum algorithms to graphs; and third, to provide a number of examples for  $\mathrm{QC}_{\mathcal{C}}$  circuits, which are characteristic and of practical interest.

In Sec. II we give the universality proof for the described scheme of computation in a complete and detailed form. The proof has already been presented to a large part in Ref. [1]. What was not contained in Ref. [1] was the explanation of why and how the gate simulations on the  $\mathrm{QC}_{\mathcal{C}}$  work. This omission seemed in order since the implementation of the gates discussed there [controlled NOT (CNOT) and arbitrary rotations] requires only small clusters such that the functioning of the gates can be easily verified in a computer simul

tion. For the examples of gates and subcircuits given in Sec. IV, this is no longer the case. Generally, we want an analytic explanation for the functioning of the gate simulations on the  $\mathrm{QC}_{\mathcal{C}}$ . This explanation is given in Sec. II F and applied to the gates of a universal set in Sec. II G as well as to more complicated examples in Sec. IV.

In Sec. II H we discuss the spatial, temporal, and operational resources required in  $\mathrm{QC}_{\mathcal{C}}$  computations in relation to the resources needed for the corresponding quantum logic networks. We find that overheads are at most polynomial. But there does not always need to be overheads. For example, as shown in Sec. II I, all  $\mathrm{QC}_{\mathcal{C}}$  circuits in the Clifford group have unit logical depth.

In Sec. III we discuss non-network aspects of the  $\mathrm{QC}_{\mathcal{C}}$ . In Sec. III A we state the reasons why the network model is not adequate to describe the  $\mathrm{QC}_{\mathcal{C}}$  in every respect. The network model is abandoned and replaced by a more appropriate model [7]. This model is described very briefly.

In Sec. III B we relate algorithms to graphs. We show that from every algorithm its Clifford part can be removed. The required algorithm-specific nonuniversal quantum resource to run the remainder of the quantum algorithm on the  $\mathrm{QC}_{\mathcal{C}}$  is then a graph state [9]. All that remains of the Clifford part is a mathematical graph specifying this graph state.

In Sec. IV we give examples of larger gates and subcircuits, which may be of practical relevance, among them the  $\mathrm{QC}_{\mathcal{C}}$  circuit for quantum Fourier transformation and for the  $n$ -qubit adder.

In Sec. V we discuss the  $\mathrm{QC}_{\mathcal{C}}$  computations on finite (small) clusters and in the presence of decoherence. We describe a variant of the scheme consisting of repeated steps of (re-)entangling a cluster via the Ising interaction, alternating with rounds of one-qubit measurements. Using this modified scheme it is possible to split long computations such that they fit piecewise on a small cluster.

# II. UNIVERSALITY OF QUANTUM COMPUTATION VIA ONE-QUBIT MEASUREMENTS

In this section we prove that the  $\mathrm{QC}_{\mathcal{C}}$  is a universal quantum computer. The technique to accomplish this is to show that any quantum logic network can be simulated efficiently

![](images/734b56013ec9189036dc9f027dcc0f0442beb626e31014bf5bfb85a1b035f212.jpg)  
FIG. 1. Simulation of a quantum logic network by measuring two-state particles on a lattice. Before the measurements the qubits are in the cluster state  $|\phi \rangle_{\mathcal{C}}$  of Eq. (1). Circles  $\odot$  symbolize measurements of  $\sigma_z$ , vertical arrows are measurements of  $\sigma_x$ , while tilted arrows refer to measurements in the  $x-y$ -plane.

on the  $\mathrm{QC}_{\mathcal{C}}$ . Before we go into details, let us state the general picture.

For the one-way quantum computer, the entire resource for the quantum computation is provided initially in the form of a specific entangled state—the cluster state [2]—of a large number of qubits. Information is then written onto the cluster, processed, and read out from the cluster by one-particle measurements only. The entangled state of the cluster thereby serves as a universal "substrate" for any quantum computation. It provides in advance all entanglement that is involved in the subsequent quantum computation. Cluster states can be created efficiently in any system with a quantum Ising-type interaction (at very low temperatures) between two-state particles in a lattice configuration.

It is important to realize here that information processing is possible even though the result of every measurement in any direction of the Bloch sphere is completely random. The mathematical expression for the randomness of the measurement results is that the reduced density operator for each qubit in the cluster state is  $\frac{1}{2}\mathbb{1}$ . The individual measurement results are random but correlated, and these correlations enable quantum computation on the  $\mathrm{QC}_{\mathcal{C}}$ .

For clarity, let us emphasize that in the scheme of the  $\mathrm{QC}_{\mathcal{C}}$  we distinguish between cluster qubits on  $\mathcal{C}$ , which are measured in the process of computation, and the logical qubits. The logical qubits constitute the quantum information being processed, while the cluster qubits in the initial cluster state form an entanglement resource. Measurements of their individual one-qubit state drive the computation.

To process quantum information with this cluster, it suffices to measure its particles in a certain order and in a certain basis, as depicted in Fig. 1. Quantum information is thereby propagated through the cluster and processed. Measurements of  $\sigma_z$  observables effectively remove the respective lattice qubit from the cluster. Measurements in the  $\sigma_x$  (and  $\sigma_y$ ) eigenbasis are used for "wires," i.e., to propagate logical quantum bits through the cluster, and for the CNOT gate between two logical qubits. Observables of the form  $\cos(\varphi)\sigma_x \pm \sin(\varphi)\sigma_y$  are measured to realize arbitrary rotations of logical qubits. For these cluster qubits, the basis in which each of them is measured depends on the results of

preceding measurements. This introduces a temporal order in which the measurements have to be performed. The processing is finished once all qubits except a last one on each wire have been measured. The remaining unmeasured qubits form the quantum register which is now ready to be read out. At this point, the results of previous measurements determine in which basis these "output" qubits need to be measured for the final readout, or if the readout measurements are in the  $\sigma_{x}$ ,  $\sigma_{y}$ , or  $\sigma_{z}$  eigenbasis, how the readout measurements have to be interpreted. Without loss of generality, we assume in this paper that the readout measurements are performed in the  $\sigma_{z}$  eigenbasis.

# A. Cluster states and their quantum correlations

Cluster states are pure quantum states of two-level systems (qubits) located on a cluster  $\mathcal{C}$ . This cluster is a connected subset of a simple cubic lattice  $\mathbb{Z}^d$  in  $d\geqslant 1$  dimensions. The cluster states  $|\phi_{\{\kappa \}}\rangle_{\mathcal{C}}$  obey the set of eigenvalue equations

$$
\left. K ^ {(a)} \right| \phi_ {\{\kappa \}} \rangle_ {\mathcal {C}} = (- 1) ^ {\kappa_ {a}} \left| \phi_ {\{\kappa \}} \right\rangle_ {\mathcal {C}}, \tag {1}
$$

with the correlation operators

$$
K ^ {(a)} = \sigma_ {x} ^ {(a)} \bigotimes_ {b \in \operatorname {n g h b} (a)} \sigma_ {z} ^ {(b)}. \tag {2}
$$

Therein,  $\{\kappa\} \coloneqq \{\kappa_{a} \in \{0,1\} \mid a \in \mathcal{C}\}$  is a set of binary parameters that specify the cluster state and  $\mathrm{ngb}(a)$  is the set of all neighboring lattice sites of  $a$ .

A cluster state  $|\phi_{\{\kappa \}}\rangle_{\mathcal{C}}$  is completely specified by the eigenvalue equations (1), since  $K^{(a)}$ ,  $a \in \mathcal{C}$ , form a complete set of  $|\mathcal{C}|$  independent and commuting observables for the system of qubits on the cluster  $\mathcal{C}$ . This can most easily be seen from the fact that  $K^{(a)}$  is obtained from  $\sigma_x^{(a)}$  under conjugation with a unitary transformation, as shown below Eq. (11). For a set of eigenvalues specified by  $\{\kappa\}$  the corresponding eigenspace is thus one-dimensional, i.e.,  $|\phi_{\{\kappa\}}\rangle_{\mathcal{C}}$  is determined modulo an irrelevant phase factor. There are  $2^{|C|}$  different choices for  $\{\kappa\} \in \{0,1\}^{|C|}$ , and since  $K^{(a)}$  are Hermitian operators, the associated common eigenstates, the cluster states, are mutually orthogonal and form a basis in the Hilbert space of the cluster.

The discussion in this paper will be based entirely on eigenvalue equations (1) and we will never need to work out some cluster state in any specific basis. In fact, to write down a cluster state in its explicit form would be quite space consuming since the minimum number of required terms scales exponentially with the number of qubits [2], and for computation we will be going to consider rather large cluster states. Nevertheless, for illustration we give a few examples for cluster states of a small number of qubits. The cluster states on a chain of 2, 3, and 4 qubits, fulfilling eigenvalue equations (1) with all  $\kappa_{a} = 0$ , are

$$
\left| \phi \right\rangle_ {\mathcal {C} _ {2}} = \frac {1}{\sqrt {2}} \left(\left| 0 \right\rangle_ {1} | + \rangle_ {2} + \left| 1 \right\rangle_ {1} | - \rangle_ {2}\right),
$$

$$
\left| \phi \right\rangle_ {\mathcal {C} _ {3}} = \frac {1}{\sqrt {2}} \left(\left| + \right\rangle_ {1} \left| 0 \right\rangle_ {2} \right| + \left. \right\rangle_ {3} + \left| - \right\rangle_ {1} \left| 1 \right\rangle_ {2} | - \left. \right\rangle_ {3}), \tag {3}
$$

$$
\begin{array}{l} | \phi \rangle_ {\mathcal {C} _ {4}} = \frac {1}{2} | + \rangle_ {1} | 0 \rangle_ {2} | + \rangle_ {3} | 0 \rangle_ {4} + \frac {1}{2} | + \rangle_ {1} | 0 \rangle_ {2} | - \rangle_ {3} | 1 \rangle_ {4}, \\ + \frac {1}{2} | - \rangle_ {1} | 1 \rangle_ {2} | - \rangle_ {3} | 0 \rangle_ {4} + \frac {1}{2} | - \rangle_ {1} | 1 \rangle_ {2} | + \rangle_ {3} | 1 \rangle_ {4}, \\ \end{array}
$$

with the notation

$$
| 0 \rangle_ {a} := | 0 \rangle_ {a, z} = \sigma_ {z} ^ {(a)} | 0 \rangle_ {a, z},
$$

$$
\left| 1 \right\rangle_ {a} := \left| 1 \right\rangle_ {a, z} = - \sigma_ {z} ^ {(a)} \left| 1 \right\rangle_ {a, z}, \tag {4}
$$

$$
\left| \pm \right\rangle_ {a} := \frac {1}{\sqrt {2}} \left(\left| 0 \right\rangle_ {a} \pm \left| 1 \right\rangle_ {a}\right).
$$

The state  $|\phi \rangle_{\mathcal{C}_2}$  is local unitary equivalent to a Bell state and  $|\phi \rangle_{\mathcal{C}_3}$  to the Greenberger-Horne-Zeilinger (GHZ) state.  $|\phi \rangle_{\mathcal{C}_4}$ , however, is not equivalent to a four-particle GHZ state. In particular, the entanglement in  $|\phi \rangle_{\mathcal{C}_4}$  cannot be destroyed by a single local operation [2].

Ways to create a cluster state, in principle, are to measure all the correlation operators  $K^{(a)}$ ,  $a \in \mathcal{C}$  of Eq. (2) on an arbitrary  $|\mathcal{C}|$ -qubit state or to cool into the ground state of a Hamiltonian  $H_{K} = -\hbar g \sum_{a \in \mathcal{C}} \kappa_{a} K^{(a)}$ .

Another way—likely to be more suitable for realization in the lab—is as follows. First, a product state  $| + \rangle_{\mathcal{C}} = \otimes_{a \in \mathcal{C}} | + \rangle_{a}$  is prepared. Second, the unitary transformation  $S^{(\mathcal{C})}$ ,

$$
S ^ {(\mathcal {C})} = \prod_ {a, b \in \mathcal {C} | b - a \in \gamma_ {d}} S ^ {a b}, \tag {5}
$$

is applied to the state  $| + \rangle$ . Often we will write  $S$  in short for  $S^{(\mathcal{C})}$ . In Eq. (5), for the cases of dimension  $d = 1,2,3$ , we have  $\gamma_{1} = \{1\}$ ,  $\gamma_{2} = \{(1,0)^{T}, (0,1)^{T}\}$ , and  $\gamma_{3} = \{(1,0,0)^{T}, (0,1,0)^{T}, (0,0,1)^{T}\}$ , and the two-qubit transformation  $S^{ab}$  is such that the state  $|1\rangle_{a} \otimes |1\rangle_{b}$  acquires a phase of  $\pi$  under its action, while the remaining states  $|0\rangle_{a} \otimes |0\rangle_{b}$ ,  $|0\rangle_{a} \otimes |1\rangle_{b}$ , and  $|1\rangle_{a} \otimes |0\rangle_{b}$  acquire no phase. Thus,  $S^{ab}$  has the form

$$
S ^ {a b} = | 0 \rangle_ {a} \langle 0 | \otimes \mathbb {I} ^ {(b)} + | 1 \rangle_ {a} \langle 1 | \otimes \sigma_ {z} ^ {(b)}, \tag {6}
$$

which is a conditional phase gate between  $a$  and  $b$ . Note that all operations  $S^{ab}$  in  $S$  mutually commute and that they can therefore be carried out at the same time. Initial individual preparation of the cluster qubits in  $\left|+\right\rangle_{a\in\mathcal{C}}$  can also be done in parallel. Thus, the creation of the cluster state is a two-step process. The temporal resources to create the cluster state are constant in the size of the cluster.

The state  $| + \rangle_{\mathcal{C}}$  obviously obeys the eigenvalue equations  $\sigma_x^{(a)}| + \rangle_{\mathcal{C}} = | + \rangle_{\mathcal{C}}$ ,  $\forall a \in \mathcal{C}$  and thus the cluster state  $|\phi \rangle_{\mathcal{C}}$  generated via  $S$  obeys

$$
\left| \phi \right\rangle_ {\mathcal {C}} = S \sigma_ {x} ^ {(a)} S ^ {\dagger} | \phi \rangle_ {\mathcal {C}}, \quad \forall a \in \mathcal {C}. \tag {7}
$$

To obtain  $S\sigma_{x}^{(a)}S^{\dagger}$ , we use the evolution relations for the stabilizer of a state under the action of a phase gate [10]. We observe that

$$
S ^ {a b} \sigma_ {x} ^ {(a)} S ^ {a b \dagger} = \sigma_ {x} ^ {(a)} \otimes \sigma_ {z} ^ {(b)},
$$

$$
\left( \begin{array}{l l l l} 1 & (h) & h ^ {\prime} & (a) \\ & & & (h) \end{array} \right) \tag {8}
$$

$$
S ^ {a b} \sigma_ {x} ^ {(b)} S ^ {a b \dagger} = \sigma_ {z} ^ {(a)} \otimes \sigma_ {x} ^ {(b)},
$$

and

$$
S ^ {a b} \sigma_ {x} ^ {(c)} S ^ {a b \dagger} = \sigma_ {x} ^ {(c)}, \quad \forall c \in \mathcal {C} \backslash \{a, b \}. \tag {9}
$$

Further, the Pauli phase flip operators  $\sigma_z^{(d)}$  commute with all  $S^{ab}$ , i.e.,

$$
S ^ {a b} \sigma_ {z} ^ {(d)} S ^ {a b \dagger} = \sigma_ {z} ^ {(d)}, \forall d \in \mathcal {C}. \tag {10}
$$

Now, from Eqs. (8)-(10) it follows that

$$
S \sigma_ {x} ^ {(a)} S ^ {\dagger} = \sigma_ {x} ^ {(a)} \bigotimes_ {b \in \operatorname {n g h b} (a)} \sigma_ {z} ^ {(b)}. \tag {11}
$$

Thus, the state  $|\phi \rangle_{\mathcal{C}}$  generated from  $| + \rangle_{\mathcal{C}}$  via the transformation  $S$  as defined in Eq. (5) does indeed obey eigenvalue equations of form (1), with

$$
\kappa_ {a} = 0, \quad \forall a \in \mathcal {C}. \tag {12}
$$

As the eigenvalues are fixed in this case, we drop them in the notation for the cluster state  $|\phi \rangle_{\mathcal{C}}$ . Cluster states specified by different sets  $\{\kappa_a\}$  can be obtained by applying Pauli phase flip operators  $\sigma_z^{(a)}$ . To see this, note that

$$
\sigma_ {z} ^ {(a)} K ^ {(b)} \sigma_ {z} ^ {(a) \dagger} = (- 1) ^ {\delta_ {a, b}} K ^ {(b)}. \tag {13}
$$

Therefore,

$$
\bigotimes_ {a \in \mathcal {C}} \left(\sigma_ {z} ^ {(a)}\right) ^ {\Delta \kappa_ {a}} \left| \phi_ {\left\{\kappa_ {a} \right\}} \right\rangle_ {\mathcal {C}} = \left| \phi_ {\left\{\kappa_ {a} + \Delta \kappa_ {a} \right\}} \right\rangle_ {\mathcal {C}}, \tag {14}
$$

where the addition for  $\kappa_{a}$  is modulo 2. Cluster states with different sets  $\{\kappa\}$  are equally suited for  $\mathrm{QC}_{\mathcal{C}}$  computation.

Concerning a physical realization of the transformation  $S$  defined in Eq. (5), note that  $S$  is generated by the Hamiltonian

$$
H = \hbar g \sum_ {a, b \in \mathcal {C} | b - a \in \gamma_ {d}} \frac {1 - \sigma_ {z} ^ {(a)}}{2} \frac {1 - \sigma_ {z} ^ {(b)}}{2}. \tag {15}
$$

Now,  $S = \exp (-i\pi /\hbar gH)$  may be written in the form

$$
\begin{array}{l} S = \left[ \prod_ {a, b \in \mathcal {C} | b - a \in \gamma_ {d}} e ^ {- i (\pi / 4)} \exp \left(i \frac {\pi}{4} \sigma_ {z} ^ {(a)}\right) \exp \left(i \frac {\pi}{4} \sigma_ {z} ^ {(b)}\right) \right] \\ \times \exp \left(- i \frac {\pi}{4} \sum_ {a, b \in \mathcal {C} | b - a \in \gamma_ {d}} \sigma_ {z} ^ {(a)} \sigma_ {z} ^ {(b)}\right). \tag {16} \\ \end{array}
$$

We find that the interaction part  $H_{I}$  of the Hamiltonian  $H$  generating  $S$  is of the Ising form,

$$
H _ {I} = \hbar \frac {g}{4} \sum_ {a, b \in \mathcal {C} | b - a \in \gamma_ {d}} \sigma_ {z} ^ {(a)} \sigma_ {z} ^ {(b)}, \tag {17}
$$

and, since the local part  $H_{\mathrm{local}}$  of the Hamiltonian commutes with the Ising Hamiltonian  $H_{I}$ , the interaction  $S$  generated by  $H$  is local unitary equivalent to the unitary transformation generated by a Ising Hamiltonian.

For matter of presentation, the interaction  $S^{ab}$  in Eq. (6) and, correspondingly, the local part of the Hamiltonian  $H$  in Eq. (15) has been chosen in such a way that eigenvalue equations (1) take the particularly simple form with  $\kappa_{a} = 0$  for all  $a \in \mathcal{C}$ , irrespective of the shape of the cluster.

To create quantum states that are useful as a resource for the  $\mathrm{QC}_{\mathcal{C}}$ , i.e., cluster- or local unitary equivalent states, all systems with a tunable Ising interaction and a local  $\sigma_z$ -type Hamiltonian, i.e., with a Hamiltonian

$$
H ^ {\prime} = \sum_ {a \in \mathcal {C}} \Delta E _ {a} \sigma_ {z} ^ {(a)} + \hbar \frac {g (t)}{4} \sum_ {a, b \in \mathcal {C} | b - a \in \gamma_ {d}} \sigma_ {z} ^ {(a)} \sigma_ {z} ^ {(b)} \tag {18}
$$

are suitable, provided the coupling  $g(t)$  can be switched between zero and at least one nonzero value.

Even this condition can be relaxed. A permanent Ising interaction instead of a globally tunable one is sufficient, if the measurement process is much faster than the characteristic time scale for the Ising interaction, i.e., if the measurements are stroboscopic. If it takes the Ising interaction a time  $T_{\mathrm{Ising}}$  to create a cluster state  $|\phi\rangle_{\mathcal{C}}$  from a product state  $|+\rangle_{\mathcal{C}}$ , then the Ising interaction acting for a time  $2T_{\mathrm{Ising}}$  performs the identity operation,  $S^{(\mathcal{C})}S^{(\mathcal{C})} = \mathbb{1}^{(\mathcal{C})}$ . Therefore, starting with a product state  $|+\rangle_{\mathcal{C}}$  at time  $t = 0$  evolving under permanent Ising interaction, stroboscopic measurements may be performed at times  $(2k + 1)T_{\mathrm{Ising}}, k \in \mathbb{N}$ .

One possibility to create a cluster state in practice is via cold controlled collisions in optical lattices, as described in Ref. [2]. Cold atoms representing the qubits can be arranged on a two- or three-dimensional (3D) lattice and state-dependent interaction phases may be acquired via cold collisions between neighboring atoms [14] or via tunneling [15]. For a suitable choice of the collision phases  $\varphi$ ,  $\varphi = \pi \mod 2\pi$ , the state resulting from a product state  $| + \rangle_{\mathcal{C}}$  after interaction is a cluster state obeying eigenvalue equations (1), with the set  $\{\kappa_a,a\in \mathcal{C}\}$  specified by the filling pattern of the lattice.

Let us, at the end of this section, briefly state which techniques will be used for the explanation of measurement-based quantum computation on cluster states. First, note that the operators  $(-1)^{\kappa_a}K^{(a)}$  in Eq. (1) generate the stabilizer of the state  $|\phi_{\{\kappa \}}\rangle_{\mathcal{C}}$ . The stabilizer formalism, as developed by Gottesman [10,11] and by Calderbank et al. [12] (see also Ref. [13]), provides a compact characterization of the cluster state. It is also useful in understanding some of the working principles of the  $\mathrm{QC}_{\mathcal{C}}$ . In the subsequent sections, we frequently perform stabilizer manipulations.

Further, some basic notions of graph theory will be useful later when we discuss the relation between quantum algorithms and graphs in Sec. III B. Therefore, let us, at this point, establish a connection between quantum states such as

the cluster state of Eq. (1), and graphs. The treatment here follows that of Ref. [9], adapted to our notation.

Let us recall the definition of a graph [16]. A graph  $G(V,E)$  is a set  $V$  of vertices connected via edges  $e$  from the set  $E$ . The information of which vertex  $a \in V$  is connected to which other vertex  $b \in V$  is contained in a symmetric  $|V| \times |V|$  matrix  $\Gamma$ , the adjacency matrix. The matrix  $\Gamma$  is such that  $\Gamma_{ab} = 1$  if two vertices  $a$  and  $b$  are connected via an edge  $e \in E$ , and  $\Gamma_{ab} = 0$  otherwise. We identify the cluster  $C$  with the vertices  $V_{\mathcal{C}}$  of a graph,  $C = V_{\mathcal{C}}$ , and in this way establish a connection to the notion introduced earlier.

To relate graphs to quantum mechanics, the vertices of a graph can be identified with local quantum systems, in this case qubits, and the edges with two-particle interactions, in the present case  $\sigma_z\sigma_z$  interactions. If one initially prepares each individual qubit  $a$  in the state  $(\sigma_z^{(a)})^{\kappa_a}| + \rangle_a$  and subsequently switches on, for an appropriately chosen finite time span, the interaction

$$
H _ {G (V, E)} = \hbar g \sum_ {(a, b) \in E} \frac {1 - \sigma_ {z} ^ {(a)}}{2} \frac {1 - \sigma_ {z} ^ {(b)}}{2}, \tag {19}
$$

with  $(a,b)\in E$  denoting an edge between qubits  $a$  and  $b$ , then one obtains quantum states that are graph code words as introduced in Ref. [9]. Henceforth we will refer to these graph code words as graph states and use them in a context different from coding. The graph states  $|\phi \{\kappa \} \rangle_{G}$  are defined by a set of eigenvalue equations, which read

$$
\sigma_ {x} ^ {(a)} \otimes_ {b \in V} (\sigma_ {z} ^ {(b)}) ^ {\Gamma_ {a b}} | \phi \{\kappa \} \rangle_ {G} = (- 1) ^ {\kappa_ {a}} | \phi \{\kappa \} \rangle_ {G}, \tag {20}
$$

with  $\kappa_{a} \in \{0,1\}$ ,  $\forall a \in V$ . Here we use  $G$  instead of  $V$  as an index for the state  $|\phi\rangle$ , as the set  $E \subset V \times V$  of edges is now independent and no longer implicitly specified by  $V$  as was the case in Eq. (1).

Note that cluster states (1) are a particular case of graph states (20). The graph  $G(\mathcal{C}, E_{\mathcal{C}})$  that describes a cluster state is that of a square lattice in 2D and that of a simple cubic lattice in 3D, i.e., the set  $E_{\mathcal{C}}$  of edges is given by

$$
E _ {\mathcal {C}} = \{(a, b) | a, b \in \mathcal {C}, b \in \operatorname {n g h b} (a) \}. \tag {21}
$$

# B. A universal set of quantum gates

To provide something definite to discuss right from the beginning, we now give the procedures of how to realize a CNOT gate and a general one-qubit rotation via one-qubit measurements on a cluster state. The explanation of why and how these gates work will be given in Sec. II G.

A CNOT gate can be realized on a cluster state of 15 qubits, as shown in Fig. 2. All measurements can be performed simultaneously. The procedure to realize a CNOT gate on a cluster with 15 qubits, as displayed in Fig. 2, is the following.

Procedure 1. Realization of a CNOT gate acting on a two-qubit state  $|\psi_{\mathrm{in}}\rangle$

(1) Prepare the state

$$
\left| \Psi_ {\mathrm {i n}} \right\rangle_ {\mathcal {C} _ {1 5}} = \left| \psi_ {\mathrm {i n}} \right\rangle_ {1, 9} \otimes \left( \begin{array}{c} \bigotimes \\ i \in \mathcal {C} _ {1 5 \setminus \{1. 9 \}} \end{array} \right| + \left. \right\rangle_ {i}).
$$

![](images/05390ef3f17e514b2cb097a145078145f2cf304cb4eb7d278b7c5c4094d06f8e.jpg)  
(a)

![](images/9e1d2b3339753488205e7116a58c0637b3bc9ac07d2ec82a77918e00ab756215.jpg)  
(b)

![](images/a6ef1c272d229ea2040408095809c89abc00e2b5b96463013a8e098f7c318323.jpg)  
(c)

![](images/0e3b1836ee93de7d5b087cb057286aaf1d6c9240b0225317e80cb89ea692b5be.jpg)  
(d)

![](images/458898985bfd52d63f41ee4b4af1e3f074a30e6031144e736a44ea6c590c7a0b.jpg)  
FIG. 2. Realization of elementary quantum gates on the  $\mathrm{QC}_{\mathcal{C}}$ . Each square represents a lattice qubit. The squares in the extreme left column marked with white circles denote the input qubits, those in the rightmost column denote the output qubits.  
(e)

(2) Entangle the 15 qubits of the cluster  $\mathcal{C}_{15}$  via the unitary operation  $S^{(\mathcal{C}_{15})}$ .  
(3) Measure all qubits of  $\mathcal{C}_{15}$  except for the output qubits 7, 15 (following the labeling in Fig. 2). The measurements can be performed simultaneously. Qubits 1, 9, 10, 11, 13, 14 are measured in the  $\sigma_{x}$  eigenbasis and qubits 2-6, 8, 12 in the  $\sigma_{y}$  eigenbasis.

Dependent on the measurement results, the following gate is thereby realized:

$$
U _ {\text {C N O T}} ^ {\prime} = U _ {\Sigma , \text {C N O T}} \text {C N O T} (c, t), \tag {22}
$$

where the byproduct operator  $U_{\Sigma ,\mathrm{CNOT}}$  has the form

$$
U _ {\Sigma , \mathrm {C N O T}} = \sigma_ {x} ^ {(c) \gamma_ {x} ^ {(c)}}, \sigma_ {x} ^ {(t) \gamma_ {x} ^ {(t)}} \sigma_ {z} ^ {(c) \gamma_ {z} ^ {(c)}}, \sigma_ {z} ^ {(t) \gamma_ {z} ^ {(t)}},
$$

with

$$
\gamma_ {x} ^ {(c)} = s _ {2} + s _ {3} + s _ {5} + s _ {6},
$$

$$
\gamma_ {x} ^ {(t)} = s _ {2} + s _ {3} + s _ {8} + s _ {1 0} + s _ {1 2} + s _ {1 4}, \tag {23}
$$

$$
\gamma_ {z} ^ {(c)} = s _ {1} + s _ {3} + s _ {4} + s _ {5} + s _ {8} + s _ {9} + s _ {1 1} + 1,
$$

$$
\gamma_ {z} ^ {(t)} = s _ {9} + s _ {1 1} + s _ {1 3}.
$$

Therein, the  $s_i$  represent the measurement outcomes  $s_i$  on the qubits  $i$ . Expression (23) is modified if redundant cluster qubits are present and/or if the cluster state on which the CNOT gate is realized is specified by a set  $\{\kappa_a\}$  different from Eq. (12); see Sec. II C. This concludes the presentation of the CNOT gate, the proof of its functioning is given in Sec. II G.

An arbitrary rotation  $U_{Rot} \in \mathrm{SU}(2)$  can be realized on a chain of five qubits. Consider a rotation in its Euler representation

$$
U _ {R o t} [ \xi , \eta , \zeta ] = U _ {x} [ \zeta ] U _ {z} [ \eta ] U _ {x} [ \xi ], \tag {24}
$$

where the rotations about the  $x$  and  $z$  axes are

$$
\begin{array}{l} U _ {x} [ \alpha ] = \exp \left(- i \alpha \frac {\sigma_ {x}}{2}\right), \\ U _ {z} [ \alpha ] = \exp \left(- i \alpha \frac {\sigma_ {z}}{2}\right). \tag {25} \\ \end{array}
$$

Initially, the first qubit is prepared in some state  $|\psi_{\mathrm{in}}\rangle$  , which is to be rotated, and the other qubits are prepared in  $| + \rangle$  After the five qubits are entangled by the unitary transformation  $S$  , the state  $|\psi_{\mathrm{in}}\rangle$  can be rotated by measuring qubits 1-4. At the same time, the state is also swapped to site 5. The qubits 1-4 are measured in appropriately chosen bases

$$
\mathcal {B} _ {j} (\varphi_ {j}) = \left\{\frac {\left| 0 \right\rangle_ {j} + e ^ {i \varphi_ {j}} \left| 1 \right\rangle_ {j}}{\sqrt {2}}, \frac {\left| 0 \right\rangle_ {j} - e ^ {i \varphi_ {j}} \left| 1 \right\rangle_ {j}}{\sqrt {2}} \right\}, \tag {26}
$$

whereby the measurement outcomes  $s_j \in \{0,1\}$  for  $j = 1, \dots, 4$  are obtained. Here,  $s_j = 0$  means that qubit  $j$  is projected into the first state of  $\mathcal{B}_j(\varphi_j)$ . In Eq. (26) the basis states of all possible measurement bases lie on the equator of the Bloch sphere, i.e., on the intersection of the Bloch sphere with the  $x-y$  plane. Therefore, the measurement basis for qubit  $j$  can be specified by a single parameter, the measurement angle  $\varphi_j$ . The measurement direction of qubit  $j$  is the vector on the Bloch sphere that corresponds to the first state in the measurement basis  $\mathcal{B}_j(\varphi_j)$ . Thus, the measurement angle  $\varphi_j$  is the angle between the measurement direction at qubit  $j$  and the positive  $x$  axis. In summary, the procedure to realize an arbitrary rotation  $U_{Rot}[\xi, \eta, \zeta]$ , specified by its Euler angles  $\xi, \eta, \zeta$ , is the following.

Procedure 2. Realization of general one-qubit rotations  $U_{Rot} \in \mathrm{SU}(2)$ .

(1) Prepare the state

$$
\left| \Psi_ {\mathrm {i n}} \right\rangle_ {\mathcal {C} _ {5}} = \left| \psi_ {\mathrm {i n}} \right\rangle_ {1} \otimes \left( \begin{array}{c} 5 \\ \bigotimes_ {i = 2} \end{array} \right| + \left. \right\rangle_ {i}).
$$

(2) Entangle the five qubits of the cluster  $\mathcal{C}_5$  via the unitary operation  $S^{(\mathcal{C}_5)}$ .  
(3) Measure qubits 1-4 in the following order and basis:

(3.1) measure qubit 1 in  $\mathcal{B}_1(0)$  
(3.2) measure qubit 2 in  $\mathcal{B}_2(-\xi (-1)^{s_1}t)$  (27)  
(3.3) measure qubit 3 in  $\mathcal{B}_3(-\eta (-1)^{s_2})$  
(3.4) measure qubit 4 in  $\mathcal{B}_4(-\zeta (-1)^{s_1 + s_3})$

Via Procedure 2 the rotation  $U_{Rot}^{\prime}$  is realized:

$$
U _ {R o t} ^ {\prime} [ \xi , \eta , \zeta ] = U _ {\Sigma , R o t} U _ {R o t} [ \xi , \eta , \zeta ]. \tag {28}
$$

Therein, the random byproduct operator has the form

$$
U _ {\Sigma , R o t} = \sigma_ {x} ^ {s _ {2} + s _ {4}} \sigma_ {z} ^ {s _ {1} + s _ {3}}. \tag {29}
$$

It can be corrected for at the end of the computation, as will be explained in Sec. II E.

There is a subgroup of rotations for which the realization procedure is somewhat simpler than Procedure 2. These ro

tations form the subgroup of local operations in the Clifford group. The Clifford group is the normalizer of the Pauli group.

Among these rotations are, for example, the Hadamard gate and the  $\pi /2$ -phase gate. These gates can be realized on a chain of five qubits in the following way.

Procedure 3. Realization of the Hadamard and the  $\pi /2$ -phase gates.

(1) Prepare the state

$$
\left| \Psi_ {\mathrm {i n}} \right\rangle_ {\mathcal {C} _ {5}} = \left| \psi_ {\mathrm {i n}} \right\rangle_ {1} \otimes \left( \begin{array}{c} 5 \\ \bigotimes \\ i = 2 \end{array} \right| + \left. \right\rangle_ {i}).
$$

(2) Entangle the five qubits of the cluster  $\mathcal{C}_5$  via the unitary operation  $S^{(\mathcal{C}_5)}$ .  
(3) Measure qubits 1-4. This can be done simultaneously. For the Hadamard gate, measure individually the observables  $\sigma_{x}^{(1)}$ ,  $\sigma_{y}^{(2)}$ ,  $\sigma_{y}^{(3)}$ ,  $\sigma_{y}^{(4)}$ . For the  $\pi/2$ -phase gate measure  $\sigma_{x}^{(1)}$ ,  $\sigma_{x}^{(2)}$ ,  $\sigma_{y}^{(3)}$ ,  $\sigma_{x}^{(4)}$ .

The difference with respect to Procedure 2 for general rotations is that in Procedure 2 no measurement bases need to be adjusted according to previous measurement results and, therefore, the measurements can all be performed at the same time.

As in the cases before, the Hadamard and the  $\pi /2$ -phase gates are performed only modulo a subsequent byproduct operator, which is determined by the random measurement outcomes  $s_k$

$$
\begin{array}{l} U _ {\Sigma , H} = \sigma_ {x} ^ {s _ {1} + s _ {3} + s _ {4}} \sigma_ {z} ^ {s _ {2} + s _ {3}}, \\ U _ {\Sigma , U _ {z} (\pi / 2)} = \sigma_ {x} ^ {s _ {2} + s _ {4}} \sigma_ {z} ^ {s _ {1} + s _ {2} + s _ {3} + 1}. \tag {30} \\ \end{array}
$$

Before we explain the functioning of the above gates, we would like to address the following questions: First, "How does one manage to occupy only those lattice sites with cluster qubits that are required for a particular circuit but leave the remaining ones empty?" The answer to this question is that redundant qubits will not have to be removed physically. It is sufficient to measure each of them in the  $\sigma_z$  eigenbasis, as will be described in Sec. II C.

Second, "How can the described procedures for gate simulation be concatenated such that they represent a measurement-based simulation of an entire circuit?" It seems at first sight that the described building blocks would only lead to a computational scheme consisting of repeated steps of entangling operations and measurements. This is not the case. As will be shown in Sec. II D, the three procedures stated are precisely of such a form that the described measurement-based scheme of quantum computation can be decomposed into them.

The third question is "How does one deal with the randomness of the measurement results that leads to the byproduct operators (23), (29), and (30)?" The appearance of byproduct operators may suggest that there is a need for local correction operations to counteract these unwanted extra operators. However, there is neither a possibility for such counter rotations within the described model of quantum

computation, nor is there a need. The scheme works with unit efficiency despite the randomness of the individual measurement results, as will be discussed in Sec. II E.

# C. Removing the redundant cluster qubits

A cluster state on a two-dimensional cluster of rectangular shape, say, is a resource that allows for any computation that fits on the cluster. If one realizes a certain quantum circuit on this cluster state, there will always be qubits on the cluster, which are not needed for its realization. Such cluster qubits we call redundant for this particular circuit.

In the description of the  $\mathrm{QC}_{\mathcal{C}}$  as a quantum logic network, the first step of each computation will be to remove these redundant cluster qubits. Fortunately, the situation is not such that we have to remove the qubits (or, more precisely, the carriers of the qubits) physically from the lattice. To make them ineffective to the realized circuit, it suffices to measure each of them in the  $\sigma_z$  eigenbasis. In this way, one is left with an entangled quantum state on the cluster  $\mathcal{C}_N$  of the unmeasured qubits and a product state on  $\mathcal{C} \backslash \mathcal{C}_N$ ,

$$
\left| \right. \phi_ {\{\kappa \}} \left. \right\rangle_ {\mathcal {C} \rightarrow} \left| \right. Z \left. \right\rangle_ {\mathcal {C} \backslash \mathcal {C} _ {N}} \otimes \left| \right. \phi_ {\left\{\kappa^ {\prime} \right\}} \left. \right\rangle_ {\mathcal {C} _ {N}}, \tag {31}
$$

with  $|Z\rangle_{\mathcal{C}\setminus \mathcal{C}_N} = (\otimes_{i\in \mathcal{C}\setminus \mathcal{C}_N}|s_i\rangle_{i,z})$  and  $s_i$  the results of the  $\sigma_z$  measurements. The resulting entangled state  $|\phi_{\{\kappa^{\prime}\}}\rangle_{\mathcal{C}_N}$  on the subcluster  $\mathcal{C}_N$  is again a cluster state obeying the set of Eqs. (1), and the measurement outcomes determine the sign factors therein. This can be easily seen with stabilizer methods [10,13]. Nevertheless, for completeness we give the argument here. First, by definition, we have

$$
| Z \rangle_ {\mathcal {C} \backslash \mathcal {C} _ {N}} \otimes | \phi_ {\{\kappa^ {\prime} \}} \rangle_ {\mathcal {C} _ {N}} = \left(\bigotimes_ {i \in \mathcal {C} \backslash \mathcal {C} _ {N}} \frac {1 + (- 1) ^ {s _ {i}} \sigma_ {z} ^ {(i)}}{2}\right) | \phi_ {\{\kappa \}} \rangle_ {\mathcal {C}}. \tag {32}
$$

Using eigenvalue equations (1), we now insert a correlation operator  $K^{(a)}$  with  $a \in \mathcal{C}_N$  into the right-hand side (rhs) of Eq. (32) between the projector and the state, and obtain

$$
\left| Z \right\rangle_ {\mathcal {C} \backslash \mathcal {C} _ {N}} \otimes \left| \phi_ {\left\{\kappa^ {\prime} \right\}} \right\rangle_ {\mathcal {C} _ {N}} = (- 1) ^ {\kappa_ {a} ^ {\prime}} K ^ {\prime (a)} \left| Z \right\rangle_ {\mathcal {C} \backslash \mathcal {C} _ {N}} \otimes \left| \phi_ {\left\{\kappa^ {\prime} \right\}} \right\rangle_ {\mathcal {C} _ {N}}, \tag {33}
$$

with the correlation operators

$$
K ^ {\prime (a)} = \sigma_ {x} ^ {(a)} \bigotimes_ {c \in \operatorname {n g h b} (a) \cap \mathcal {C} _ {N}} \sigma_ {z} ^ {(c)}, \tag {34}
$$

and the set  $\{\kappa_a^{\prime}\}$  specifying the eigenvalues

$$
\kappa_ {a} ^ {\prime} = \left(\kappa_ {a} + \sum_ {b \in \operatorname {n g h b} (a) \cap \left(\mathcal {C} \backslash \mathcal {C} _ {N}\right)} s _ {b}\right) \bmod 2. \tag {35}
$$

As the new correlation operators  $K^{\prime (a)}$  in Eq. (33) only act on the cluster qubits in  $\mathcal{C}_N$ , the states  $|\phi_{\{\kappa '\}}\rangle_{\mathcal{C}_N}$  again obey eigenvalue equations of type (1), i.e.,

$$
\left. K ^ {\prime (a)} \right| \phi_ {\{\kappa^ {\prime} \}} \rangle_ {\mathcal {C} _ {N}} = (- 1) ^ {\kappa_ {a} ^ {\prime}} \left| \phi_ {\{\kappa^ {\prime} \}} \right\rangle_ {\mathcal {C} _ {N}}, \quad \forall a \in \mathcal {C} _ {N}. \tag {36}
$$

There are  $|\mathcal{C}_N|$  such eigenvalue equations for a state of  $|\mathcal{C}_N|$  qubits. Thus, the state  $|\phi_{\{\kappa^{\prime}\}}\rangle_{\mathcal{C}_{N}}$  is specified by Eq. (36) up to a global phase.

From Eq. (35) we find that the redundant qubits have some remaining influence on the process of computation. After they have been measured, the random measurement results enter into the eigenvalues that specify the residual cluster state  $|\phi_{\{\kappa^{\prime}\}}\rangle_{\mathcal{C}_N}$  on the cluster  $\mathcal{C}_N$ . However, from Eq. (14) it follows that  $|\phi_{\{\kappa^{\prime}\}}\rangle_{\mathcal{C}_N}$  is equivalent to  $|\phi\rangle_{\mathcal{C}_N}$  modulo local  $\sigma_z$  rotations. These can be accounted for by absorbing them into the subsequent measurements.

In this way, a  $\mathrm{QC}_{\mathcal{C}}$  computation with arbitrary  $\{\kappa_{a}^{\prime}\}$  may always be traced back to the case of  $\{\kappa_{a}^{\prime} = 0|\forall a\in \mathcal{C}_{N}\}$ , and we therefore adopt the following two rules to simplify the further discussion:

(1) The redundant cluster qubits are discarded. We only consider the subcluster  $\mathcal{C}_N$ . (37)  
(2) We assume that  $\kappa_{a}^{\prime} = 0$  for all  $a\in \mathcal{C}_N$

# D. Concatenation of gate simulations

A quantum circuit on the  $\mathrm{QC}_{\mathcal{C}}$  is a spatial and temporal pattern of measurements on individual qubits, which have previously been entangled to form a cluster state. To better understand its functioning we would like—as in the network model of quantum computation—to decompose the circuit into basic building blocks. These building blocks should be such that out of them any circuit can be assembled. In explaining the  $\mathrm{QC}_{\mathcal{C}}$  in a network language, we can relate the building blocks of a quantum logic network—the quantum gates—to building blocks of  $\mathrm{QC}_{\mathcal{C}}$  circuits. To do so, we need to prove that, in a  $\mathrm{QC}_{\mathcal{C}}$  computation, measurement patterns representing the gates can be patched together like the quantum gates themselves. This proof is given in the following.

To realize a gate  $g$  on the  $\mathrm{QC}_{\mathcal{C}}$ , consider a cluster  $\mathcal{C}(g)$ . This cluster has an input section  $\mathcal{C}_I(g)$ , a body  $\mathcal{C}_M(g)$ , and an output section  $\mathcal{C}_O(g)$ , with

$$
\mathcal {C} _ {I} (g) \cup \mathcal {C} _ {M} (g) \cup \mathcal {C} _ {O} (g) = \mathcal {C} (g),
$$

$$
\mathcal {C} _ {I} (g) \cap \mathcal {C} _ {M} (g) = \emptyset ,
$$

$$
\mathcal {C} _ {I} (g) \cap \mathcal {C} _ {O} (g) = \emptyset , \tag {38}
$$

$$
\mathcal {C} _ {M} (g) \cap \mathcal {C} _ {O} (g) = \varnothing .
$$

The measurement bases of the qubits in  $\mathcal{C}_M(g)$ , the body of the gate  $g$ , encode  $g$ . The general scheme for procedures to realize a gate  $g$  on a cluster  $\mathcal{C}(g)$ , for which examples have been given with Procedures 1-3 for the CNOT gate and the rotations, is the following.

Scheme 1. Simulation of the gate  $g$  on  $\mathcal{C}(g)$ , acting on the input state  $|\psi\rangle_{\mathrm{in}}$ .

(1) Prepare the input state  $|\psi_{\mathrm{in}}\rangle$  on  $\mathcal{C}_I(g)$  and the qubits in  $\mathcal{C}_M(g)\cup \mathcal{C}_O(g)$  individually in the state  $| + \rangle = |0\rangle_{x}$  such that the quantum state of all qubits in  $\mathcal{C}(g)$  becomes

$$
\left| \Psi_ {\text {i n}} \right\rangle_ {\mathcal {C} (g)} = \left| \psi_ {\text {i n}} \right\rangle_ {\mathcal {C} _ {I} (g)} \otimes \bigotimes_ {k \in \mathcal {C} _ {M} (g) \cup \mathcal {C} _ {O} (g)} | + \rangle_ {k}. \tag {39}
$$

(2) Entangle  $|\Psi_{\mathrm{in}}\rangle_{\mathcal{C}(g)}$  by the interaction

$$
S ^ {(\mathcal {C} (g))} = \prod_ {a, b \in \mathcal {C} (g) | b - a \in \gamma_ {d}} S ^ {a b}, \tag {40}
$$

such that the resulting quantum state is  $|\Psi_{\varepsilon}\rangle_{\mathcal{C}_N}$ $= S^{(\mathcal{C}(g))}|\Psi_{\mathrm{in}}\rangle_{\mathcal{C}(g)}$

(3) Measure the cluster qubits in  $\mathcal{C}_I(g)\cup \mathcal{C}_M(g)$ , i.e., choose measurement bases specified by  $\vec{r}_k\in S^2$ ,  $k\in \mathcal{C}_I(g)\cup \mathcal{C}_M(g)$  and obtain the random measurement results  $s_k$  such that the projector

$$
P ^ {\left(\mathcal {C} _ {I} (g) \cup \mathcal {C} _ {M} (g)\right)} = \bigotimes_ {k \in \mathcal {C} _ {I} (g) \cup \mathcal {C} _ {M} (g)} \frac {1 + (- 1) ^ {s _ {k}} \vec {r} _ {k} \cdot \vec {\sigma} ^ {(k)}}{2} \tag {41}
$$

is applied; thereby the state  $|\Psi_{\mathrm{out}}\rangle_{C(g)}$  is obtained.

Putting all three steps of Scheme 1 together, the relation between  $|\Psi_{\mathrm{in}}\rangle_{\mathcal{C}(g)}$  and  $|\Psi_{\mathrm{out}}\rangle_{\mathcal{C}(g)}$  is

$$
\left| \Psi_ {\text {o u t}} \right\rangle_ {\mathcal {C} (g)} = P ^ {\left(\mathcal {C} _ {I} (g) \cup \mathcal {C} _ {M} (g)\right)} S ^ {\left(\mathcal {C} (g)\right)} \left| \Psi_ {\text {i n}} \right\rangle_ {\mathcal {C} (g)}. \tag {42}
$$

As we will show later, the state  $|\Psi_{\mathrm{out}}\rangle_{\mathcal{C}(g)}$  has the form

$$
\left| \Psi_ {\text {o u t}} \right\rangle_ {\mathcal {C} (g)} = \left(\bigotimes_ {k \in \mathcal {C} _ {I} (g) \cup \mathcal {C} _ {M} (g)} \left| s _ {k} \right\rangle_ {k, \hat {r} _ {k}}\right) \otimes \left| \psi_ {\text {o u t}} \right\rangle_ {\mathcal {C} _ {O} (g)}, \tag {43}
$$

where  $\left| s_k \right\rangle_{k, r_k}$  denotes the state of the qubit  $k$  after the observable  $\vec{r}_k \cdot \vec{\sigma}^{(k)}$  has been measured and the measurement outcome was  $s_k$ , and

$$
\left| \psi_ {\text {o u t}} \right\rangle = U _ {\Sigma , g} U _ {g} \left| \psi_ {\text {i n}} \right\rangle . \tag {44}
$$

Therein,  $U_{g}$  is the desired unitary operation, and the byproduct operator  $U_{\Sigma ,g}$  is an extra multilocal rotation that depends on the measurement results  $\{s_k|k\in \mathcal{C}_I(g)\cup \mathcal{C}_M(g)\}$ . The byproduct operator is always in the Pauli group, i.e.,

$$
U _ {\Sigma , g} = \bigotimes_ {i = 1} ^ {n} \left(\sigma_ {x} ^ {[ i ]}\right) ^ {x _ {i}} \left(\sigma_ {z} ^ {[ i ]}\right) ^ {z _ {i}} \tag {45}
$$

modulo a possible global phase, and  $n$  is the number of logical qubits. In Eq. (45)  $\sigma^{[i]}$  denote Pauli operators acting on the logical qubit  $i$ , not cluster qubit. The values  $x_{i}, z_{i} \in \{0,1\}$  are computed from the outcomes of the measurements by which the respective gate is realized.

As will be proved in Sec. II F, each gate may be realized only modulo a subsequent byproduct operator  $U_{\Sigma,g}$ . The byproduct operator is random, but known from the outcomes of the measurements that realize the gate. This knowledge is sufficient to drive the  $\mathrm{QC}_{\mathcal{C}}$  computation deterministically, as we will demonstrate in Sec. II E.

Given a quantum circuit implemented on a cluster  $\mathcal{C}_N$  of qubits, which is divided into two consecutive circuits, suppose that circuit  $g_1$  is implemented on the subcluster  $\mathcal{C}(g_1)$  and the subsequent circuit  $g_2$  is implemented on the subcluster  $\mathcal{C}(g_2)$ , such that  $\mathcal{C}_N = \mathcal{C}(g_1) \cup \mathcal{C}(g_2)$ . There is an overlap between  $\mathcal{C}(g_1)$  and  $\mathcal{C}(g_2)$ , which consists of the output qubits of circuit 1 (identical to the input qubits of circuit 2),  $\mathcal{C}_O(g_1) = \mathcal{C}_I(g_2) = \mathcal{C}(g_1) \cap \mathcal{C}(g_2)$ . The location of the readout quantum register is  $\mathcal{C}_O(g_2) \subset \mathcal{C}(g_2)$ .

![](images/2c4922a4943e06c9b8e2e6642f0b4c035977138a0f81f4e99d1d4b426adee1c6.jpg)  
FIG. 3. Here the exchange of the order of the measurements and the entanglement operations is shown. The crosses “ $\times$ ” denote the one-qubit measurements and the horizontal lines between adjacent cluster qubits denote the unitary transformations  $S^{a,a+1}$ .

Now compare the following two strategies. Strategy (i) consists of the following steps: (1) write input and entangle all qubits of  $\mathcal{C}_N$ ; (2) measure qubits in  $\mathcal{C}_N \backslash \mathcal{C}_O(g_2)$ , to implement the circuit except the readout measurements. Strategy (ii) consists of steps (1) write input and entangle the qubits on  $\mathcal{C}(g_1)$ ; (2) measure the qubits in  $\mathcal{C}(g_1) \backslash \mathcal{C}_O(g_1)$ . This implements the first subcircuit and writes the intermediate output to  $\mathcal{C}_O(g_1) = \mathcal{C}_I(g_2)$ ; (3) entangle the qubits on  $\mathcal{C}(g_2)$ ; (4) measure all qubits in  $\mathcal{C}(g_2) \backslash \mathcal{C}_O(g_2)$ . Steps 3 and 4 implement the second subcircuit  $g_2$  on the subcluster  $\mathcal{C}(g_2)$ . The measurements on  $\mathcal{C}(g_1) \backslash \mathcal{C}_O(g_1)$ , represented by the projector  $P_1$  commute with the entanglement operation restricted to  $\mathcal{C}(g_2)$ ,  $S^{(\mathcal{C}(g_2))} = :S_2$ ,  $P_1S_2 = S_2P_1$ , because these two operations act on different subsets of particles. With  $P_2$  representing the measurements on  $\mathcal{C}(g_2) \backslash \mathcal{C}_O(g_2)$  and  $S_1 = S^{(\mathcal{C}(g_1))}$ , it follows that  $S_2S_1 = S^{(\mathcal{C}_N)}$  and  $P_2P_1 = P^{(\mathcal{C}_N \backslash \mathcal{C}_O(g_2))8}$ . Therefore,

$$
P _ {2} S _ {2} P _ {1} S _ {1} = P _ {2} P _ {1} S _ {2} S _ {1} = P ^ {\left(\mathcal {C} _ {N} \backslash \mathcal {C} _ {O} (g _ {2})\right)} S ^ {\left(\mathcal {C} _ {N}\right)}. \tag {46}
$$

Thus, the two strategies are mathematically equivalent. The above argument can be iterated. It follows that entangling the whole cluster once and subsequently performing all the measurements is equivalent to simulating a quantum logic network gate by gate. The exchange of the order of operations is illustrated in Fig. 3.

Now, we want to specialize to the case where the quantum input is known and where the quantum output is measured. This is the situation that interests us most in this paper. Examples of such a situation are Shor's factoring algorithm [17] and Grover's search algorithm [18]. In both cases, the quantum input is  $|\psi_{\mathrm{in}}\rangle = \otimes_{i = 1}^{n}| + \rangle_{i}$ .

Let us denote the input section of the whole cluster  $\mathcal{C}$ , comprising the input qubits of the network simulation, as  $I$ ; and the output section, comprising the qubits of the readout quantum register, as  $O$ . As long as the quantum input is known, it is sufficient to consider the state  $| + \rangle_{I} = \otimes_{i \in I}| + \rangle_{i}$ . For different but known input states  $|\psi_{\mathrm{in}}\rangle_{I}$  one can always find a transformation  $U_{\mathrm{in}}$  such that  $|\psi_{\mathrm{in}}\rangle_{I} = U_{\mathrm{in}}| + \rangle_{I}$  and instead of realizing some unitary transformation  $U$  on  $|\psi_{\mathrm{in}}\rangle_{I}$  one realizes  $UU_{\mathrm{in}}$  on  $| + \rangle_{I}$ .

Preparing an input state  $| + \rangle_I$  and entangling it via  $S^{(\mathcal{C})}$  with the rest of the cluster  $\mathcal{C} \backslash I$  is the same as creating a cluster state  $|\phi\rangle_{\mathcal{C}}$  on the entire cluster  $\mathcal{C} = I \cup \mathcal{C} \backslash I$ ,  $S^{(\mathcal{C})}| + \rangle_I \otimes | + \rangle_{\mathcal{C} \backslash I} = S^{(\mathcal{C})}| + \rangle_{\mathcal{C}} = |\phi\rangle_{\mathcal{C}}$ . Therefore, the entire procedure of realizing a quantum computation on the  $\mathrm{QC}_{\mathcal{C}}$  amounts to the following scheme.

Scheme 2. Performing a computation on the  $\mathrm{QC}_{\mathcal{C}}$

(1) Prepare a cluster state  $|\phi_{\{\kappa \}}\rangle_{\mathcal{C}}$  of sufficient size.  
(2) Perform a sequence of measurements on  $|\phi_{\{\kappa \}}\rangle_{\mathcal{C}}$  and obtain the result of the computation from all the measurement outcomes.

For practical realization of a  $\mathrm{QC}_{\mathcal{C}}$  computation, Scheme 2 is advantageous over the mathematically equivalent sequence of gate simulations according to Scheme 1. This sequence, in turn, may be used to explain the functioning of the  $\mathrm{QC}_{\mathcal{C}}$  in network terminology.

# E. Randomness of the measurement results

We will now show that the described scheme of quantum computation with the  $\mathrm{QC}_{\mathcal{C}}$  works with unit efficiency despite the randomness of the individual measurement results.

First note that a byproduct operator  $U_{\Sigma}$  that acts after the final unitary gate  $U_{g_{|\mathcal{N}|}}$  does not jeopardize the scheme. Its only effect is that the results of the readout measurements have to be reinterpreted. The byproduct operator  $U_{\Sigma}$  that acts upon the logical output qubits  $1, \ldots, n$  has the form

$$
U _ {\Sigma} = \prod_ {i = 1} ^ {n} \left(\sigma_ {x} ^ {[ i ]}\right) ^ {x _ {i}} \left(\sigma_ {z} ^ {[ i ]}\right) ^ {z _ {i}}, \tag {47}
$$

where  $x_{i}, z_{i} \in \{0,1\}$  for  $1 \leqslant i \leqslant n$ . Let the qubits on the cluster, which are left unmeasured, be labeled in the same way as the readout qubits of the quantum logic network.

The qubits on the cluster, which take the role of the readout qubits are, at this point, in a state  $U_{\Sigma}|\mathrm{out}\rangle$ , where  $|\mathrm{out}\rangle$  is the output state of the corresponding quantum logic network. The computation is completed by measuring each qubit in the  $\sigma_z$  eigenbasis, thereby obtaining the measurement results  $\{s_i'\}$ , say. In the  $\mathrm{QC}_{\mathcal{C}}$  scheme, one measures the state  $U_{\Sigma}|\mathrm{out}\rangle$  directly, whereby outcomes  $\{s_i\}$  are obtained and the readout qubits are projected into the state  $|\mathcal{M}\rangle = \Pi_{i=1}^{n} \{[1 + (-1)^{s_i} \sigma_z^{(i)}] / 2\} U_{\Sigma}|\mathrm{out}\rangle$ . Depending on the byproduct operator  $U_{\Sigma}$ , the set of measurement results  $\{s\}$ , in general, has a different interpretation from what the network readout  $\{s_i'\}$  would have. The measurement basis is the same. From Eq. (47) one obtains

$$
\begin{array}{l} \left| \mathcal {M} \right\rangle = \prod_ {i = 1} ^ {n} \frac {1 + (- 1) ^ {s _ {i}} \sigma_ {z} ^ {(i)}}{2} U _ {\Sigma} | \text {o u t} \rangle \\ = U _ {\Sigma} \left(U _ {\Sigma} ^ {\dagger} \prod_ {i = 1} ^ {n} \frac {1 + (- 1) ^ {s _ {i}} \sigma_ {z} ^ {(i)}}{2} U _ {\Sigma}\right) | \text {o u t} \rangle \\ = U _ {\Sigma} \prod_ {i = 1} ^ {n} \frac {1 + (- 1) ^ {s _ {i} + x _ {i}} \sigma_ {z} ^ {(i)}}{2} | \text {o u t} \rangle . \tag {48} \\ \end{array}
$$

From Eq. (48) we see that a  $\sigma_z$  measurement on the state  $U_{\Sigma}|\mathrm{out}\rangle$  with results  $\{s\}$  represents the same algorithmic output as a  $\sigma_z$  measurement of the state  $|\mathrm{out}\rangle$  with the results  $\{s_i'\}$ , where the sets  $\{s\}$  and  $\{s_i'\}$  are related by

$$
s _ {i} ^ {\prime} \equiv s _ {i} + x _ {i} \bmod 2. \tag {49}
$$

The set  $\{s_i'\}$  represents the result of the computation. It can be calculated from the results  $\{s_i\}$  of the  $\sigma_z$  measurements on the "readout" cluster qubits and the values  $\{x_i\}$  that are determined by the byproduct operator  $U_{\Sigma}$ .

Let us now discuss the sequence of the individual gate simulations. Because of Eq. (44) and the argument presented in Sec. II D, the quantum output  $|\psi_{\mathrm{out}}\rangle$  of a whole sequence of unitary gates is related to the respective input via

$$
| \psi_ {\text {o u t}} \rangle = \left(\prod_ {i = 1} ^ {| \mathcal {N} |} U _ {\Sigma , g _ {i}} U _ {g _ {i}}\right) | \psi_ {\text {i n}} \rangle , \tag {50}
$$

where the gates  $g_{i} \in \mathcal{N}$  are labeled corresponding to the order of their action.

Thus, we find that one can cope with the randomness of the measurement results provided the byproduct operators  $U_{\Sigma ,g_i}$  in Eq. (50) can be propagated forward through the subsequent gates such that they act on the cluster qubits representing the output register. This can be done. To propagate the byproduct operators we use the propagation relations

$$
\operatorname {C N O T} (c, t) \sigma_ {x} ^ {(t)} = \sigma_ {x} ^ {(t)} \operatorname {C N O T} (c, t),
$$

$$
\operatorname {C N O T} (c, t) \sigma_ {x} ^ {(c)} = \sigma_ {x} ^ {(c)} \sigma_ {x} ^ {(t)} \operatorname {C N O T} (c, t),
$$

$$
(5 1)
$$

$$
\operatorname {C N O T} (c, t) \sigma_ {z} ^ {(t)} = \sigma_ {z} ^ {(c)} \sigma_ {z} ^ {(t)} \operatorname {C N O T} (c, t),
$$

$$
\operatorname {C N O T} (c, t) \sigma_ {z} ^ {(c)} = \sigma_ {z} ^ {(c)} \operatorname {C N O T} (c, t),
$$

for the CNOT gate,

$$
\begin{array}{l} U _ {R o t} [ \xi , \eta , \zeta ] \sigma_ {x} = \sigma_ {x} U _ {R o t} [ \xi , - \eta , \zeta ], \\ \left(5 2\right) \\ \end{array}
$$

$$
U _ {R o t} [ \xi , \eta , \zeta ] \sigma_ {z} = \sigma_ {z} U _ {R o t} [ - \xi , \eta , - \zeta ],
$$

for general rotations  $U_{Rot}[\xi, \eta, \zeta]$  as defined in Eq. (24), and

$$
\begin{array}{l} H \sigma_ {x} = \sigma_ {z} H, \\ H \sigma_ {z} = \sigma_ {x} H, \\ (5 3) \\ \end{array}
$$

$$
U _ {z} [ \pi / 2 ] \sigma_ {x} = \sigma_ {y} U _ {z} [ \pi / 2 ],
$$

$$
U _ {z} [ \pi / 2 ] \sigma_ {z} = \sigma_ {z} U _ {z} [ \pi / 2 ],
$$

for the Hadamard and  $\pi /2$ -phase gates propagation relations (52) apply to general rotations realized via Procedure 2—including the Hadamard and  $\pi /2$ -phase gates—while the propagation relations (53) apply to the Hadamard and  $\pi /2$ -phase gates as realized via Procedure 3.

Note that propagation relations (51)-(53) are such that the Pauli operators are mapped onto the Pauli operators under propagation and thus the byproduct operators remain in the

Pauli group when being propagated. Further note that there is a difference between the relations for propagation through gates that are in the Clifford group and through those that are not. For CNOT, the Hadamard, and the  $\pi /2$ -phase gates, the byproduct operator changes under propagation, while the gate remains unchanged. This holds for all gates in the Clifford group because the propagation relations for the Clifford gates are of the form  $U_{g}U_{\Sigma} = (U_{g}U_{\Sigma}U_{g}^{-1})U_{g}$  as Eqs. (51) and (53), i.e., the byproduct operator  $U_{\Sigma}$  is conjugated under the gate, and the Clifford group by its definition as the normalizer of the Pauli group maps the Pauli operators onto Pauli operators under conjugation. Propagation relations (51) and (53) are identical to the propagation relations for Pauli errors given in Ref. [19]. For the gates that are not in the Clifford group, conjugation of the byproduct operator under the gate would, in general, not work and therefore, for the rotations that are not in the Clifford group, the propagation relations are different. There, the gate is conjugated under the byproduct operator, and thus the byproduct operator remains unchanged in propagation while the gate is modified. In both cases, the forward propagation leaves the byproduct operators in the Pauli group. In particular, their tensor product structure is maintained.

Let us now discuss how byproduct operator propagation affects the scheme of computation with the  $\mathrm{QC}_{\mathcal{C}}$ . Using the above propagation relations, Eq. (50) can be rewritten in the following way:

$$
\left| \psi_ {\text {o u t}} \right\rangle = \left(\prod_ {i = 1} ^ {| \mathcal {N} |} U _ {\Sigma , g _ {i}} \mid_ {\Omega}\right) \left(\prod_ {i = 1} ^ {| \mathcal {N} |} U _ {g _ {i}} ^ {\prime}\right) \left| \psi_ {\text {i n}} \right\rangle . \tag {54}
$$

Therein,  $U_{\Sigma ,g_i}|_{\Omega}$  are forward propagated byproduct operators, resulting from the byproduct operators  $U_{\Sigma ,g_i}$  of the gates  $g_{i}$ . They accumulate to the total byproduct operator  $U_{\Sigma}$  whose effect on the result of the computation is contained in Eq. (49),

$$
U _ {\Sigma} = \prod_ {i = 1} ^ {| \mathcal {N} |} U _ {\Sigma , g _ {i}} \mid_ {\Omega}. \tag {55}
$$

Further,  $U_{g_i}'$  are the gates modified under the propagation of the byproduct operators. As discussed above, for gates in the Clifford group we have

$$
U _ {g} ^ {\prime} = U _ {g}, \quad \forall g \in \text {C l i f f o r d g r o u p}, \tag {56}
$$

as can be seen from Eqs. (51) and (53).

The gates that are not in the Clifford group are modified by byproduct operator propagation. Specifically, general rotations (24) are conjugated, as can be seen from Eq. (52). From the structure of Eq. (50) we see that only the byproduct operators of gates  $g_{k}$  earlier than  $g_{i}$  in the network may have an effect on  $U_{g_i}$ , i.e., those with  $k < i$ . To give an explicit expression, let us define  $U_{\Sigma ,g_k}\big|_{\mathcal{O}_i}$ , which are byproduct operators  $U_{\Sigma ,g_k}$  propagated forward by propagation relations (51)-(53) to the vertical cut  $\mathcal{O}_i$  through the network, see Fig. 4. A vertical cut through a network is a cut that intersects

![](images/9196efd9f35fe692275d3ba31e8a58cfeb07b2de2b71d8fbbe19e8c22a1276d6.jpg)  
FIG. 4. Vertical cuts. The vertical cuts intersect each qubit line exactly once, but do not intersect gates. Thus,  $\mathcal{O}_i$ ,  $\mathcal{O}_j$ , and  $\Omega$  are vertical cuts, but  $\varnothing$  is not. The cut  $\mathcal{O}_i$  intersects the rotation  $U_x$  just before its input. For two of the rotations in the displayed network, the subclusters on which these gates are realized are symbolically displayed in gray underlay. Via the measurement of the cluster qubits  $a$  and  $b$  (displayed as black dots with white border), the rotation angles of the respective rotations  $U_x$  and  $U_z$  are set.

each qubit line exactly once and does not intersect gates. The vertical cut  $\mathcal{O}_i$  has the additional property that it intersects the network just before the input of gate  $g_{i}$ . The relation between a rotation  $U_{g_i}^{\prime}$  modified by the byproduct operators and the nonmodified rotation  $U_{g_i}$  is

$$
\begin{array}{l} U _ {g _ {i}} ^ {\prime} = \Big (\prod_ {k | k <   i} U _ {\Sigma , g _ {k}} | _ {\mathcal {O} _ {i}} \Big) U _ {g _ {i}} \Big (\prod_ {k | k <   i} U _ {\Sigma , g _ {k}} | _ {\mathcal {O} _ {i}} \Big) ^ {\dagger}, \\ \forall U _ {g _ {i}} \in S U (2). \tag {57} \\ \end{array}
$$

Now that we have investigated the effect of byproduct operator propagation on the individual gates let us return to Eq. (54). There, we find that the operations that act on the input state  $|\psi_{\mathrm{in}}\rangle$  group into two factors. The first is composed of the modified gate operations  $U_{g_i}'$  and the second is composed of the forward propagated byproduct operators. The second factor gives the accumulated byproduct operator  $U_{\Sigma}$  and is absorbed into the result of the computation via Eq. (49). It does not cause any complication.

So what remains is the first factor, and we find that the unitary evolution of the input state  $|\psi_{\mathrm{in}}\rangle$  that is realized is composed of the modified gates  $U_{g_i}'$ . The gates we will realize are thus  $U_{g_i}'$ , not  $U_{g_i}$ . However, the standard procedures (Procedures 1-3) in Sec. II B are for the operations  $U_{g_i}$ . Thus, we have to read Eq. (57) in reverse. We need to deduce  $U_{g_i}$  from  $U_{g_i}'$ . Once the gates  $g_k$  for all  $k < i$  have been realized, this can be done for each gate  $g_i$  since the byproduct operators  $U_{\Sigma,k}$  are then known for all  $k < i$ . Finally, with  $U_{g_i}$  determined from  $U_{g_i}'$ , Procedure 2 gives the measurement bases required for the realization of the gate  $g_i$ . Note that it is a sufficient criterion for the realization of the gate  $g_i$  that all gates  $g_k$  with  $k < i$  must have been realized before, but not a necessary one.

Let us, at this point, address the question of temporal ordering more explicitly. For proper discussion of the temporal ordering we have to step out of the network frame for a moment. First, note that in the case of the  $\mathrm{QC}_{\mathcal{C}}$  the basic primitive are measurements. Thus, the temporal complexity

will be determined by the temporal ordering of these measurements, unlike in quantum logic networks, where it depends on the ordering of gates. The most efficient ordering of measurements that simulates a quantum logic network is not predescribed by the temporal ordering of the gates in this network.

A temporal ordering among the measurements is inferred from the requirement to keep the computation on the  $\mathrm{QC}_{\mathcal{C}}$  deterministic in spite of the randomness introduced by the measurements. This randomness is accounted for by the byproduct operators. The key to obtain the temporal ordering of measurements is Eq. (57). There, the byproduct operators  $U_{\Sigma ,g_k}\big|_{\mathcal{O}_i}$  may modify Euler angles of the one-qubit rotations in the network and, consequently, change measurement bases. The temporal ordering thus arises due to the fact that bases for one-qubit measurements must be chosen in accordance with outcomes obtained from the measurements of other qubits.

For each cluster qubit  $q$  that needs to be measured in a nontrivial basis, i.e., not in the eigenbasis of  $\sigma_x$ ,  $\sigma_y$ , or  $\sigma_z$ , a set of cluster qubits  $p_i$  can be identified, whose measurement outcomes influence the choice of the measurement basis for qubit  $q$ . We say that  $q$  is in the forward cone [7] of  $p_i$ ,  $q \in \mathrm{FC}(p_i)$ . Each cluster qubit has a forward cone, and in no forward cone there appears a qubit that is measured in a trivial basis.

The rule is that a cluster qubit  $q$  can only be measured once all cluster qubits  $p_i$  for which  $q \in \mathrm{fc}(p_i)$  have been measured earlier. The forward cones thereby generate an antireflexive partial ordering among the measurements from which the most efficient measurement strategy can be inferred; see Ref. [7]. Gates in the Clifford group do not contribute to the temporal complexity of a  $\mathrm{QC}_{\mathcal{C}}$  algorithm, see Sec. II I.

# F. Using quantum correlations for quantum computation

In this section we give a criterion that allows us to demonstrate the functioning of the  $\mathrm{QC}_{\mathcal{C}}$  simulations of unitary gates in a compact way. Specifically, Theorem 1 given below establishes a correspondence between general quantum gates and quantum correlations of states. Using this correspondence, the explanation of  $\mathrm{QC}_{\mathcal{C}}$  gates can be reduced to stabilizer manipulations.

Before we state the theorem, let us make the notion of a measurement pattern more precise. In a  $\mathrm{QC}_{\mathcal{C}}$  computation one can only choose the measurement bases, while the measurement outcomes are random. This is sufficient for deterministic computation. Thus, one can perform measurements specified by a spatial and temporal pattern of measurement bases, but one cannot control into which of the two eigenstates the qubits are projected.

Definition 1. A measurement pattern  $\mathcal{M}^{(\mathcal{C})}$  on a cluster  $\mathcal{C}$  is a set of vectors

$$
\mathcal {M} ^ {(\mathcal {C})} = \left\{\vec {r} _ {a} \in S ^ {2} \mid a \in \mathcal {C} \right\}, \tag {58}
$$

defining the measurement bases of the one-qubit measurements on  $\mathcal{C}$ .

If this pattern  $\mathcal{M}^{(\mathcal{C})}$  of measurements is applied on an initial state  $|\Psi_{\varepsilon}\rangle_{\mathcal{C}}$  and thereby the set of measurement outcomes

$$
\{s \} _ {\mathcal {C}} = \left\{s _ {a} \in \{0, 1 \} \mid a \in \mathcal {C} \right\} \tag {59}
$$

is obtained, then the resulting state  $|\Psi_{\mathcal{M}}\rangle_{\mathcal{C}}$  is, modulo norm factor, given by  $|\Psi_{\mathcal{M}}\rangle_{\mathcal{C}} = P_{\{s\}}^{(\mathcal{C})}(\mathcal{M})|\Psi_{\mathcal{E}}\rangle_{\mathcal{C}}$ , where

$$
P _ {\{s \}} ^ {(\mathcal {C})} (\mathcal {M}) = \bigotimes_ {k \in \mathcal {C}} \frac {1 + (- 1) ^ {s _ {k}} \vec {r} _ {k} \cdot \vec {\sigma} ^ {(k)}}{2}. \tag {60}
$$

Additionally, let us introduce some conventions for labeling. Let  $\mathcal{C}_I(g)$  and  $\mathcal{C}_O(g)$  be such that  $|\mathcal{C}_I(g)| = |\mathcal{C}_O(g)| = n$ , where  $n$  is the number of logical qubits processed by  $g$ . Operators acting on qubits  $p \in \mathcal{C}_I(g)$  and  $q \in \mathcal{C}_O(g)$  are labeled by upper indices  $(\mathcal{C}_I(g), i)$  and  $(\mathcal{C}_O(g), i')$ ,  $1 \leqslant i, i' \leqslant n$ , respectively. The qubits  $p \in \mathcal{C}_I(g)$  and  $q \in \mathcal{C}_O(g)$  are ordered from 1 to  $n$  in the same way as the logical qubits that they represent.

We make a distinction between the gate  $g$  and the unitary transformation  $U$  it realizes. The gate  $g \in \mathcal{N}$  does, besides specifying the unitary transformation  $U$ , also comprise the information about the location of the gate within the network.

After these definitions and conventions we can now state the following theorem.

Theorem 1. Let  $\mathcal{C}(g) = \mathcal{C}_I(g) \cup \mathcal{C}_M(g) \cup \mathcal{C}_O(g)$  with  $\mathcal{C}_I(g) \cap \mathcal{C}_M(g) = \mathcal{C}_I(g) \cap \mathcal{C}_O(g) = \mathcal{C}_M(g) \cap \mathcal{C}_O(g) = \emptyset$  be a cluster for the simulation of a gate  $g$ , realizing the unitary transformation  $U$ , and  $|\phi\rangle_{\mathcal{C}(g)}$  the cluster state on the cluster  $\mathcal{C}(g)$ .

Suppose the state  $|\psi \rangle_{\mathcal{C}(g)} = P_{\{s\}}^{(\mathcal{C}_M(g))}(\mathcal{M})|\phi \rangle_{\mathcal{C}(g)}$  obeys the  $2n$  eigenvalue equations

$$
\sigma_ {x} ^ {\left(\mathcal {C} _ {I} (g), i\right)} \left(U \sigma_ {x} ^ {(i)} U ^ {\dagger}\right) ^ {\left(\mathcal {C} _ {O} (g)\right)} | \psi \rangle_ {\mathcal {C} (g)} = (- 1) ^ {\lambda_ {x, i}} | \psi \rangle_ {\mathcal {C} (g)}, \tag {61}
$$

$$
\sigma_ {z} ^ {\left(\mathcal {C} _ {I} (g), i\right)} \left(U \sigma_ {z} ^ {(i)} U ^ {\dagger}\right) ^ {\left(\mathcal {C} _ {O} (g)\right)} \mid \psi \rangle_ {\mathcal {C} (g)} = (- 1) ^ {\lambda_ {z, i}} \mid \psi \rangle_ {\mathcal {C} (g)},
$$

with  $\lambda_{x,i},\lambda_{z,i}\in \{0,1\}$  and  $1\leqslant i\leqslant n$

Then, on the cluster  $\mathcal{C}(g)$  the gate  $g$  acting on an arbitrary quantum input state  $|\psi_{\mathrm{in}}\rangle$  can be realized according to Scheme 1 with the measurement directions in  $\mathcal{C}_M(g)$  described by  $\mathcal{M}^{(\mathcal{C}_M(g))}$  and the measurements of the qubits in  $\mathcal{C}_I(g)$  being  $\sigma_x$  measurements. Thereby, the input and output state in the simulation of  $g$  are related via

$$
\left| \psi_ {\text {o u t}} \right\rangle = U U _ {\Sigma} \left| \psi_ {\text {i n}} \right\rangle , \tag {62}
$$

where  $U_{\Sigma}$  is a byproduct operator given by

$$
U _ {\Sigma} = \bigotimes_ {\left(\mathcal {C} _ {I} (g) \ni i\right) = 1} ^ {n} \left(\sigma_ {z} ^ {[ i ]}\right) ^ {s _ {i} + \lambda_ {x, i}} \left(\sigma_ {x} ^ {[ i ]}\right) ^ {\lambda_ {z, i}}. \tag {63}
$$

The significance of the above theorem is that it provides a comparably simple criterion for the functioning of gate simulations on the  $\mathrm{QC}_{\mathcal{C}}$ . We can now base the explanation of the gates directly on eigenvalue equations (1), which were also used to define the cluster states in a compact way. The quan

tum correlations required to explain the functioning of the gates are derived from the basic correlations (2) rather easily, and thus the use of Theorem 1 makes the explanation of the gates more transparent and compact.

In the simulation of an individual quantum gate according to Scheme 1, after reading of the input state and the entangling operation  $S^{(\mathcal{C}(g))}$ , but before the measurements that realize the gates are performed, the resulting state carries the quantum input in an encoded form. This state is, in general, not a cluster state. It is therefore not clear a priori that cluster state correlations alone are sufficient to explain the functioning of the gate. However, this is what Theorem 1 states. To prove the functioning of a gate  $g$  on the  $\mathrm{QC}_{\mathcal{C}}$  it is sufficient to demonstrate that a cluster state on  $\mathcal{C}(g)$  exhibits certain quantum correlations.

Before we turn to the proof of Theorem 1 let us note that the measurements described by  $P_{\{s\}}^{(\mathcal{C}_M(g))}(\mathcal{M}(g))$ , as they have full rank, project the initial cluster state  $|\phi \rangle_{\mathcal{C}(g)}$  into a tensor product state,  $|\psi \rangle_{\mathcal{C}(g)} = |m\rangle_{\mathcal{C}_M(g)}\otimes |\psi \rangle_{\mathcal{C}_I(g)\cup \mathcal{C}_O(g)}$ . Thereof only the second factor,  $|\psi \rangle_{\mathcal{C}_I(g)\cup \mathcal{C}_O(g)}$ , is of interest. This state alone satisfies eigenvalue equations (61) and is uniquely determined by these equations. To see this, consider the state  $|\psi^{\prime}\rangle_{\mathcal{C}_{I(g)}\cup \mathcal{C}_{O(g)}} = U^{\dagger}|\psi \rangle_{\mathcal{C}_{I(g)}\cup \mathcal{C}_{O(g)}}$ . It satisfies the  $2n$  eigenvalue equations

$$
\sigma_ {x} ^ {(i, \mathcal {C} _ {I} (g))} \sigma_ {x} ^ {(i, \mathcal {C} _ {O} (g))} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {x, i}} | \psi^ {\prime} \rangle , \tag {64}
$$

$$
\sigma_ {z} ^ {(i, \mathcal {C} _ {I} (g))} \sigma_ {z} ^ {(i, \mathcal {C} _ {O} (g))} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {z, i}} | \psi^ {\prime} \rangle ,
$$

where we have written in short  $|\psi^{\prime}\rangle$  for  $|\psi^{\prime}\rangle_{\mathcal{C}_I(g)\cup \mathcal{C}_O(g)}$  . The state  $|\psi^{\prime}\rangle_{\mathcal{C}_I(g)\cup \mathcal{C}_O(g)}$  is uniquely defined by the above set of commuting observables, it is a product of the Bell states. Therefore,  $|\psi \rangle_{\mathcal{C}_I(g)\cup \mathcal{C}_O(g)}$  is uniquely defined as well.

Proof of Theorem 1. We will discuss the functioning of the gates for two cases of inputs. First, for all input states in the computational basis. This leaves relative phases open, which have to be determined. Second, to fix them, we discuss the input state with all qubits individually in  $| + \rangle$ . As we will see, from these two cases it can be concluded that the gate simulation works for all input states of the computational basis. This is sufficient because of the linearity of the applied operations; if the gate simulations work for states of the computational basis, then they work for superpositions of such inputs as well.

Case 1. The input  $|\psi_{\mathrm{in}}\rangle$  is one of the states of the computational basis, i.e.,  $|\psi_{\mathrm{in}}\rangle = |\mathbf{z}\rangle \coloneqq \otimes_{i = 1}^{n}|z_{i}\rangle_{z,i}$  with  $z_{i}\in \{0,1\}$ ,  $i = 1,\dots ,n$ . Then the state  $|\Psi_{\mathrm{out}}(\mathbf{z})\rangle_{\mathcal{C}(g)}$  of the qubits in  $\mathcal{C}$  [after performing a procedure according to Scheme 1, using a measurement pattern  $\mathcal{M}^{(\mathcal{C}_M(g))}$  on the body  $\mathcal{C}_M(g)$  of the gate  $g$ , and applying  $\sigma_x$  measurements on  $\mathcal{C}_l(g)]$  is

$$
\begin{array}{l} n _ {O} (\mathbf {z}) \big | \Psi_ {\text {o u t}} (\mathbf {z}) \big > _ {\mathcal {C} (g)} = P _ {\{s \}} ^ {(\mathcal {C} _ {I} (g))} (X) P _ {\{s \}} ^ {(\mathcal {C} _ {M} (g))} (\mathcal {M}) S ^ {(\mathcal {C} (g))}, \big | \mathbf {z} \big > _ {\mathcal {C} _ {I} (g)} \\ \left. \otimes \right| + \rangle_ {\mathcal {C} _ {M} (g) \cup \mathcal {C} _ {O} (g)}, \tag {65} \\ \end{array}
$$

with norm factors  $n_O(\mathbf{z})$  that are nonzero for all  $\mathbf{z}$ , as we shall show later.

The input  $|\mathbf{z}\rangle$  in Eq. (65) satisfies the equation

$$
n _ {I} (\mathbf {z}) | \mathbf {z} \rangle = P _ {Z, \mathbf {z}} ^ {\left(\mathcal {C} _ {I} (g)\right)} \otimes_ {i = 1} ^ {n} | + \rangle_ {i}, \tag {66}
$$

with  $P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))} = \otimes_{i=1}^n [1 + (-1)^{z_i}\sigma_z^{[i]}/2$ , and  $n_I(\mathbf{z}) = 1/2^{n/2}$  for all  $\mathbf{z}$ . Now note that  $S^{(\mathcal{C}(g))}$  and  $P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}$ , as well as  $P_{\{s\}}^{(\mathcal{C}_M(g))}(\mathcal{M})$  and  $P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}$ , commute. Thus,  $|\Psi_{\mathrm{out}}(\mathbf{z})\rangle_{\mathcal{C}(g)}$  can be written as

$$
\begin{array}{l} n _ {O} ^ {\prime} (\mathbf {z}) \left| \Psi_ {\text {o u t}} (\mathbf {z}) \right\rangle_ {\mathcal {C} (g)} = P _ {\{s \}} ^ {(\mathcal {C} _ {I} (g))} (X) P _ {Z, \mathbf {z}} ^ {(\mathcal {C} _ {I} (g))} P _ {\{s \}} ^ {(\mathcal {C} _ {M} (g))} (\mathcal {M}) \left| \phi \right\rangle_ {\mathcal {C} (g)} \\ = P _ {\{s \}} ^ {(\mathcal {C} _ {I} (g))} (X) P _ {Z, \mathbf {z}} ^ {(\mathcal {C} _ {I} (g))} | \psi \rangle_ {\mathcal {C} (g)}, \tag {67} \\ \end{array}
$$

where  $|\psi \rangle_{\mathcal{C}(g)}$  is specified by eigenvalue equations (61) in Theorem 1.

Let us, at this point, emphasize that the projections  $P_{\{s\}}^{(\mathcal{C}_I(g))}(X)$  and  $P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}$  in Eq. (67) are of very different origin. The projector  $P_{\{s\}}^{(\mathcal{C}_I(g))}(X)$  describes the action of the  $\sigma_x$  measurements on the qubits in  $\mathcal{C}_I(g)$ . These measurements are part of the procedure to realize some gate  $g$  on the cluster  $\mathcal{C}(g)$ . One has no control over the thereby obtained measurement outcomes  $\{s\}$  specifying  $P_{\{s\}}^{(\mathcal{C}_I(g))}(X)$ . In contrast, the projector  $P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}$  does not correspond to measurements that are performed in reality. Instead, it is introduced as an auxiliary construction that allows one to relate the processing of quantum inputs to quantum correlations in cluster states. The parameters  $\mathbf{z}$  specifying the quantum input  $|\mathbf{z}\rangle$  and thus the projector  $P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}$  in Eq. (66) can be chosen freely.

The goal is to find for the state  $\left|\Psi_{\mathrm{out}}(\mathbf{z})\right\rangle_{\mathcal{C}(g)}$  an expression involving the transformation  $U$  acting on the input  $|\mathbf{z}\rangle$ . To accomplish this, first observe that for the state on the rhs of Eq. (67) via Eq. (61), the following eigenvalue equations hold:

$$
\begin{array}{l} (U \sigma_ {z} ^ {[ i ]} U ^ {\dagger}) ^ {(\mathcal {C} _ {O})} \left[ P _ {\{s \}} ^ {(\mathcal {C} _ {I} (g))} (X) P _ {Z, \mathbf {z}} ^ {(\mathcal {C} _ {I} (g))} | \psi \rangle_ {\mathcal {C} (g)} \right] \\ = (- 1) ^ {\lambda_ {z, i} + z _ {i}} \left[ P _ {\{s \}} ^ {\left(\mathcal {C} _ {I} (g)\right)} (X) P _ {Z, \mathbf {z}} ^ {\left(\mathcal {C} _ {I} (g)\right)} \mid \psi \right\rangle_ {\mathcal {C} (g)} ], \tag {68} \\ \end{array}
$$

with  $i = 1,\dots ,n$

To make use of Eqs. (68) we need to prove that  $P_{\{s\}}^{(\mathcal{C}_I(g))}(X)P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}|\psi \rangle_{\mathcal{C}(g)}\neq 0$  for all  $\mathbf{z}$  under the assumptions of Theorem 1.

For this, we consider the scalar  $\mathcal{C}_{(g)}\langle \psi |P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}|\psi \rangle_{\mathcal{C}(g)}$  and write  $P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}$  in the form

$$
P _ {Z, \mathbf {z}} ^ {\left(\mathcal {C} _ {I} (g)\right)} = \frac {1}{2 ^ {n}} \left(1 + \sum_ {k = 1} ^ {2 ^ {n}} \bigotimes_ {i \in I _ {k}} (- 1) ^ {z _ {i}} \sigma_ {z} ^ {(i)}\right) ^ {\left(\mathcal {C} _ {I} (g)\right)}, \tag {69}
$$

where  $I_{k}\subset \mathcal{C}_{I}\neq \emptyset \forall k = 1,\ldots ,2^{n}$  . For each  $I_{k}$  we choose an  $i\in I_k$  and insert the respective eigenvalue equation from the upper line of Eq. (61) into  $\mathcal{C}(g)\langle \psi |\otimes_{j\in I_k}\sigma_z^{(j)}|\psi \rangle_{\mathcal{C}(g)}$  . Since  $\otimes_{j\in I_k}\sigma_z^{(j)}$  and  $\sigma_x^{(i,\mathcal{C}_I(g))}(U\sigma_x^{(i)}U^\dagger)^{(\mathcal{C}_O(g))}$  anticommute,  $\mathcal{C}(g)\langle \psi |\otimes_{j\in I_k}\sigma_z^{(i)}|\psi \rangle_{\mathcal{C}(g)} = 0$  for all  $I_{k}$  . Thus, with Eq. (69),

one finds  $\mathbf{\Psi}_{\mathcal{C}(g)}\langle \psi |P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}|\psi \rangle_{\mathcal{C}(g)} = 1 / 2^n$  such that  $P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}|\psi \rangle_{\mathcal{C}(g)}\neq 0$  and therefore also

$$
P _ {\{s \}} ^ {(\mathcal {C} _ {I} (g))} (X) P _ {Z, \mathbf {z}} ^ {(\mathcal {C} _ {I} (g))} | \psi \rangle_ {\mathcal {C} (g)} \neq 0, \tag {70}
$$

or, in other words,  $n_{O}^{\prime}(\mathbf{z})\neq 0$  for all  $\mathbf{z}$

Due to the fact that the projections  $P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}$  and  $P_{\{s\}}^{(\mathcal{C}_M(g))}(\mathcal{M})$  are of full rank the above state has the form

$$
\begin{array}{l} P _ {\{s \}} ^ {(\mathcal {C} _ {I} (g))} (X) P _ {Z, \mathbf {z}} ^ {(\mathcal {C} _ {I} (g))} | \psi \rangle_ {\mathcal {C} (g)} \\ = n _ {O} ^ {\prime} (\mathbf {z}) \left| \mathbf {s} \right\rangle_ {x, \mathcal {C} _ {I} (g)} \otimes \left| m \right\rangle_ {\mathcal {C} _ {M} (g)} \otimes \left| \psi_ {\text {o u t}} (\mathbf {z}) \right\rangle_ {\mathcal {C} _ {O} (g)}, \tag {71} \\ \end{array}
$$

where

$$
\left| \mathbf {s} \right\rangle_ {x, \mathcal {C} _ {I}} = \bigotimes_ {(\mathcal {C} _ {I} \ni i) = 1} ^ {n} \left| s _ {i} \right\rangle_ {x, i},
$$

and  $|m\rangle_{\mathcal{C}_M(g)}$  is some product state with  $\| |m\rangle_{\mathcal{C}_M(g)}\| = 1$ . Elaborating the argument that leads to Eq. (70) one finds that  $n_O'(z) = 1/2^n$  and  $n_O(z) = 1/2^{n/2}$ , but at this point the precise values of the normalization factors are not important as long as they are nonzero.

In Eq. (71) only the third factor of the state on the rhs is interesting, and this factor is determined by eigenvalue equations (68):

$$
| \psi_ {\text {o u t}} (\mathbf {z}) \rangle = e ^ {i \eta (\mathbf {z})} U U _ {\sum} | \mathbf {z} \rangle , \tag {72}
$$

where  $U_{\Sigma}$  is given by Eq. (63). Now, because of Eq. (67) with  $n_{O}^{\prime}(\mathbf{z}) \neq 0 \forall \mathbf{z}$ , a solution (71) with Eq. (72) for the state  $P_{\{s\}}^{(\mathcal{C}_I(g))}(X)P_{Z,\mathbf{z}}^{(\mathcal{C}_I(g))}|\psi\rangle_{\mathcal{C}(g)}$  is also a solution for the state  $|\Psi_{\mathrm{out}}(\mathbf{z})\rangle_{\mathcal{C}(g)}$ , and one finally obtains

$$
\left| \Psi_ {\text {o u t}} (\mathbf {z}) \right\rangle_ {\mathcal {C} (g)} = e ^ {i \eta (\mathbf {z})} | \mathbf {s} \rangle_ {x, \mathcal {C} _ {I} (g)} \otimes | m \rangle_ {\mathcal {C} _ {M} (g)} \otimes [ U U _ {\Sigma} | \mathbf {z} \rangle ] _ {\mathcal {C} _ {O} (g)}. \tag {73}
$$

There appear no additional norm factors in Eq. (73) because the states on the left-hand side (lhs) and the rhs are both normalized to unity.

Solution (73) still allows for one free parameter, the phase factor  $e^{i\eta(\mathbf{z})}$ . Note that, a priori, the phase factors for different  $\mathbf{z}$  can all be different.

This concludes the discussion of Case 1. We have found in Eq. (73) that the realized gate acts as

$$
\tilde {U} = U U _ {\Sigma} D, \tag {74}
$$

where the gate  $D$  is diagonal in the computational basis and contains all the phases  $e^{i\eta(\mathbf{z})}$ . What remains is to show that  $D = \mathbf{1}$  modulo a possible global phase.

Case 2. Now the same procedure is applied for the input state  $|\psi_{\mathrm{in}}\rangle = | + \rangle \coloneqq \otimes_{i = 1}^{n}| + \rangle_{i}$ . Then, the state  $|\Psi_{\mathrm{out}}(+)\rangle_{\mathcal{C}(g)}$  that results from the gate simulation is

$$
n _ {O} (+) \left| \Psi_ {\text {o u t}} (+) \right\rangle_ {\mathcal {C} (g)} = P _ {\{s \}} ^ {\left(\mathcal {C} _ {I} (g)\right)} (X) P _ {\{s \}} ^ {\left(\mathcal {C} _ {M} (g)\right)} (\mathcal {M}) | \phi \rangle_ {\mathcal {C} (g)}, \tag {75}
$$

with a nonzero norm factor  $n_O(+)$ . Using the upper line of eigenvalue equations (61), the state  $\left|\Psi_{\mathrm{out}}(+)\right\rangle_{\mathcal{C}(g)}$  is found to obey the eigenvalue equations

$$
\left. \left(U \sigma_ {x} ^ {[ i ]} U ^ {\dagger}\right) ^ {\left(\mathcal {C} _ {O (g)}\right)} \right| \Psi_ {\text {o u t}} (+) \rangle_ {\mathcal {C} (g)} = (- 1) ^ {\lambda_ {x, i} + s _ {i}} \left| \Psi_ {\text {o u t}} (+) \right\rangle_ {\mathcal {C} (g)}. \tag {76}
$$

Eigenvalue equations (76) in combination with Eq. (75) imply that

$$
\left| \Psi_ {\text {o u t}} (+) \right\rangle_ {\mathcal {C} (g)} = e ^ {i \chi} | \mathbf {s} \rangle_ {x, \mathcal {C} _ {I} (g)} \otimes | m \rangle_ {\mathcal {C} _ {M} (g)} \otimes [ U U _ {\Sigma} | + \rangle ] _ {\mathcal {C} _ {O} (g)}, \tag {77}
$$

with  $\chi$  being a free parameter. Therefore, on the input state  $| + \rangle$  the gate simulation acts as

$$
\tilde {U} = e ^ {i \chi} U U _ {\Sigma}. \tag {78}
$$

This observation concludes the discussion of Case 2.

The fact that Eqs. (73) and (77) hold simultaneously imposes stringent conditions on the phases  $\eta(\mathbf{z})$ . To see this, let us evaluate the scalar product

$$
c _ {\chi} = _ {\mathcal {C} (g)} \left\langle \Psi_ {\text {o u t}} (+) \right| U U _ {\Sigma} | \mathbf {s} \rangle_ {x, \mathcal {C} _ {I} (g)} \otimes \left| m \right\rangle_ {\mathcal {C} _ {M} (g) \otimes} + \left. \right\rangle_ {\mathcal {C} _ {O} (g)}. \tag {79}
$$

From Eq. (77) it follows immediately that

$$
c _ {\chi} = e ^ {- i \chi}. \tag {80}
$$

On the other hand, since  $| + \rangle = 1 / 2^{n / 2}\Sigma_{\mathbf{z} \in \{0,1\}^n}|\mathbf{z}\rangle$  and, by linearity,  $|\Psi_{\mathrm{out}}(+)\rangle = 1 / 2^{n / 2}\Sigma_{\mathbf{z} \in \{0,1\}^n}|\Psi_{\mathrm{out}}(\mathbf{z})\rangle$ , from Eq. (73) it follows that

$$
c _ {\chi} = \frac {1}{2 ^ {n}} \sum_ {\mathbf {z} \in \{0, 1 \} ^ {n}} e ^ {- i \eta (\mathbf {z})}. \tag {81}
$$

The sum in Eq. (81) runs over  $2^{n}$  terms. Thus, with  $\left|e^{-i\eta (\mathbf{z})}\right| = 1$  for all  $\mathbf{z}$ , it follows from the triangle inequality that  $|c_{\chi}|\leqslant 1$ . The modulus of  $c_{\chi}$  can be unity only if all  $e^{-i\eta (\mathbf{z})}$  are equal. As Eq. (80) shows,  $|c_{\chi}|$  is indeed equal to unity. Therefore, the phase factors  $e^{i\eta (\mathbf{z})}$  must all be the same, and with Eqs. (80) and (81),

$$
e ^ {i \eta (\mathbf {z})} = e ^ {i \chi}, \quad \forall \mathbf {z}. \tag {82}
$$

If we now insert Eq. (82) into Eq. (73), we find that the gate simulation acts upon every input state in the computational basis, and thus upon every input state, as  $\tilde{U}_g = e^{i\chi} U_{\Sigma}$ . Therein, the global phase factor  $e^{i\chi}$  has no effect. Thus, we find that the gate simulation indeed acts as stated in Eqs. (62) and (63).

We would like to acknowledge that a similar theorem restricted to gates in the Clifford group has been obtained in Ref. [20].

Let us conclude this section with some comments on how to use this theorem. First, note that Theorem 1 does not imply anything about the temporal order of measurements within a gate simulation. In particular, it should be understood that it

does not imply that first the measurements on the cluster qubits in  $\mathcal{C}_M(g)$  and thereafter the measurements in  $\mathcal{C}_I(g)$  are performed.

Instead, first, all those cluster qubits  $q \in \mathcal{C}_I(g) \cup \mathcal{C}_M(g)$  are measured whose measurement basis is the eigenbasis of either  $\sigma_x$  or  $\sigma_y$  (remember that, after the removal of the redundant cluster qubits, as described in Sec. II C, we are dealing with clusters  $\mathcal{C}_N$  such that, apart from the readout, no measurements in the  $\sigma_z$  eigenbasis occur). Second, possibly in several subsequent rounds, the remaining measurements are performed in bases that are chosen according to previous measurement results.

In subsequent sections we will illustrate in a number of examples how Theorem 1 is used to demonstrate the functioning of quantum gate simulations on the  $\mathrm{QC}_{\mathcal{C}}$ , and how the strategies for adapting the measurement bases are foun.

# G. Function of the CNOT gate and general one-qubit rotations

In this section, we demonstrate that the measurement patterns that we have introduced do indeed realize the desired quantum logic gates.

The basis for all our considerations is set (1) of eigenvalue equations fulfilled by the cluster states. Therefore, let us, before we turn to the realization of the gates in the universal set, describe how the eigenvalue equations can be manipulated. Equations (1) are not the only eigenvalue equations satisfied by the cluster state. Instead, a vast number of other eigenvalue equations can be derived from them.

The operators  $K^{(a)}$  may, for example, be added, multiplied by a scalar, and multiplied with each other. In this way, a large number of eigenvalue equations can be generated from Eqs. (1). Note, however, that not all operators generated in this way are correlation operators. Non-Hermitian operators can be generated, which do not represent observables, yet will prove to be useful for the construction of new correlation operators.

Furthermore, if quantum correlation operator  $K$  for state  $|\phi \rangle$  commutes with measured observable  $\vec{r_i}\cdot \vec{\sigma}^{(i)}$ , the correlation will still apply to the measured state. More specifically, if the state  $|\phi \rangle$  satisfies the eigenvalue equation  $K|\phi \rangle = \lambda |\phi \rangle$  and  $[K,\vec{r_i}\cdot \vec{\sigma}] = 0$ , then the state resulting from the measurement,  $P_{s_i}^{(i)}|\phi \rangle$ , where  $P_{s_i}^{(i)} = [1 + (-1)^{s_i}\vec{r_i}\cdot \vec{\sigma}^{(i)}] / 2$ , satisfies the same eigenvalue equation since  $\lambda [P_{s_i}^{(i)}|\phi \rangle] = [P_{s_i}^{(i)}K|\phi \rangle] = K[P_{s_i}^{(i)}|\phi \rangle]$ . Thus, the correlation  $K$  is inherited to the resultant state  $P_{s_i}^{(i)}|\phi \rangle$ .

To demonstrate and explain the measurement patterns realizing certain quantum gates, the program is as follows. First, from the set of eigenvalue equations that define the cluster state  $|\phi \rangle_{\mathcal{C}(g)}$ , we derive a set of eigenvalue equations, which is compatible with the measurement pattern on  $\mathcal{C}_M$ . Then, we use these to deduce the set of eigenvalue equations that define the state  $|\psi \rangle_{\mathcal{C}(g)}$ , where the qubits in  $\mathcal{C}_M$  have been measured. Thus, we demonstrate that the assumptions for Theorem 1, that is the set of Eqs. (61), are satisfied with the appropriate unitary transformation  $U$ . Third,  $U_{\Sigma}$  is obtained from Eq. (63) as a function of the measurement results. The order of  $U$  and  $U_{\Sigma}$  is then interchanged and, in this

way, the temporal ordering of the measurements becomes apparent.

# 1. Identity gate

As a simple example, let us first consider a gate, which realizes the identity operation  $\mathbb{1}$  on a single logical qubit.

For the identity gates  $\mathcal{C}_I$ ,  $\mathcal{C}_M$ , and  $\mathcal{C}_O$ , each consists of a single qubit, so labeling the qubits 1, 2 and 3,  $1 \in \mathcal{C}_I$ ,  $2 \in \mathcal{C}_M$ , and  $3 \in \mathcal{C}_O$ . The pattern  $\mathcal{M}(\mathbb{1})$  corresponds to a measurement of qubit 2 in the  $\sigma_x$  basis.

Let  $|\phi \rangle_{\mathcal{C}(1)}$  be the cluster state on these three qubits. The state is defined by the following set of eigenvalue equations.

$$
\left. \sigma_ {x} ^ {(1)} \sigma_ {z} ^ {(2)} \sigma_ {z} ^ {(3)} \right| \phi \rangle_ {\mathcal {C} (1)} = | \phi \rangle_ {\mathcal {C} (1)}, \tag {83a}
$$

$$
\sigma_ {z} ^ {(1)} \sigma_ {x} ^ {(2)} \sigma_ {z} ^ {(3)} | \phi \rangle_ {\mathcal {C} (1)} = | \phi \rangle_ {\mathcal {C} (1)}, \tag {83b}
$$

$$
\left. \sigma_ {z} ^ {(1)} \sigma_ {z} ^ {(2)} \sigma_ {x} ^ {(3)} \right| \phi \rangle_ {\mathcal {C} (1)} = | \phi \rangle_ {\mathcal {C} (1)}. \tag {83c}
$$

Using the stabilizer formalism [10] one obtains that after the measurement of qubit 2 in the eigenbasis of  $\sigma_{x}$  with outcome  $s_2$ , the resulting state of the cluster,  $|\psi\rangle_{\mathcal{C}(1)}$ , obeys the eigenvalue equations

$$
\sigma_ {z} ^ {(1)} \sigma_ {z} ^ {(3)} | \psi \rangle_ {\mathcal {C} (1)} = (- 1) ^ {s _ {2}} | \psi \rangle_ {\mathcal {C} (1)}, \tag {84}
$$

and

$$
\left. \sigma_ {x} ^ {(1)} \sigma_ {x} ^ {(3)} \right| \psi \rangle_ {\mathcal {C} (1)} = \left| \psi \right\rangle_ {\mathcal {C} (1)}. \tag {85}
$$

Now, since qubits 1 and 3 represent the input and output qubits, respectively, the assumption of Theorem 1, Eq. (61), is satisfied for  $U = \mathbb{1}$ . The byproduct operator  $U_{\Sigma}$  is obtained from Eq. (63), and we find that the full unitary operation realized by the gate is  $\widetilde{U} = \mathbb{1}\sigma_x^{s_2}\sigma_z^{s_1} = \sigma_x^{s_2}\sigma_z^{s_1}\mathbb{1}$ .

Also note that a wire with length one  $(\mathcal{C}_I(H) = 1, \mathcal{C}_M(H) = \emptyset, \mathcal{C}_O(H) = 2)$ , i.e., half of the above elementary wire, implements a Hadamard transformation. As in this construction the input and output qubits lie on different sublattices of  $\mathcal{C}$ , one on the even and one on the odd sublattice, we do not use it in the universal set of gates. Nevertheless, this realization of the Hadamard transformation can be a useful tool in gate construction. For example, we will use it in Sec. II G 4 to construct the realization of the  $z$  rotations out of the realization of  $x$  rotations.

# 2. Removing unnecessary measurements

In larger measurement patterns, whenever pairs of adjacent  $\sigma_{x^{-}}$  qubits in a wire are surrounded above and below by either vacant lattice sites or  $\sigma_z$  measurements, they can be removed from the pattern without changing the logical operation of the gate. This is simple to show in the case of a linear cluster. Consider six qubits, labeled  $a$  to  $f$ , which are part of a longer line of qubits, prepared in a cluster state. Four of the eigenvalue equations that define the state are

$$
\sigma_ {z} ^ {(a)} \sigma_ {x} ^ {(b)} \sigma_ {z} ^ {(c)} | \psi \rangle_ {\mathcal {C}} = | \psi \rangle_ {\mathcal {C}},
$$

$$
\sigma_ {z} ^ {(b)} \sigma_ {x} ^ {(c)} \sigma_ {z} ^ {(d)} | \psi \rangle_ {\mathcal {C}} = | \psi \rangle_ {\mathcal {C}},
$$

$$
\sigma_ {z} ^ {(c)} \sigma_ {x} ^ {(d)} \sigma_ {z} ^ {(e)} | \psi \rangle_ {\mathcal {C}} = | \psi \rangle_ {\mathcal {C}}, \tag {86}
$$

$$
\sigma_ {z} ^ {(d)} \sigma_ {x} ^ {(e)} \sigma_ {z} ^ {(f)} | \psi \rangle_ {\mathcal {C}} = | \psi \rangle_ {\mathcal {C}}.
$$

Suppose, a measurement pattern  $\mathcal{M}$  on these qubits contains measurements of the observable  $\sigma_{x}$  on qubits  $c$  and  $d$ . Measurements in the  $\sigma_{x}$  basis can be made before any other measurements in  $\mathcal{M}$ . If these two measurements alone are carried out, the new state fulfills the following eigenvalue equations, derived from Eq. (86) in the usual way,

$$
\sigma_ {z} ^ {(a)} \sigma_ {x} ^ {(b)} \sigma_ {z} ^ {(e)} | \psi \rangle_ {\mathcal {C}} = (- 1) ^ {s _ {d}} | \psi \rangle_ {\mathcal {C}}, \tag {87}
$$

$$
\sigma_ {z} ^ {(b)} \sigma_ {x} ^ {(e)} \sigma_ {z} ^ {(f)} | \psi \rangle_ {\mathcal {C}} {=} (- 1) ^ {s _ {c}} | \psi \rangle_ {\mathcal {C}}.
$$

The resulting state is therefore a cluster state from which qubits  $c$  and  $d$  have been removed, and  $b$  and  $e$  play the role of adjacent qubits. Thus, the two measurements have mapped a cluster state onto a cluster state and thus do not contribute to the logical operation realized by  $\mathcal{M}$ , which, in the case where both  $s_c$  and  $s_d$  equal 0, is completely equivalent to the reduced measurement pattern  $\mathcal{M}'$ , from which these adjacent  $\sigma_x$  measurements have been removed.

# 3. One-qubit rotation around  $x$  axis

A one-qubit rotation through an angle  $\alpha$  about the  $x$  axis,  $U_{x}[\alpha] = \exp[-i\alpha / 2\sigma_{x}]$ , is realized on the same three qubit layout as the identity gate. Labeling the qubits 1, 2, and 3, as in the preceding section,  $1 = \mathcal{C}_I$ ,  $2 = \mathcal{C}_M$ , and  $3 = \mathcal{C}_O$ . The measurement pattern  $\mathcal{M}(U_x)$  consists of a measurement, on qubit 2, of the observable represented by the vector  $\vec{r}_{xy}(\eta) = (\cos(\eta), \sin(\eta), 0)$ ,

$$
\vec {r} _ {x y} (\eta) \cdot \vec {\sigma} = \cos \eta \sigma_ {x} + \sin \eta \sigma_ {y} = U _ {z} [ \eta ] \sigma_ {x} U _ {z} [ - \eta ], \tag {88}
$$

whose eigenstates lie in the  $x - y$  plane of the Bloch sphere at an angle of  $\eta$  to the  $x$  axis.

The cluster state  $|\phi \rangle_{\mathcal{C}(U_x)}$  is defined by Eqs. (83). After the measurement of  $\mathcal{M}(U_x)$ , the resulting state is  $|\psi \rangle_{\mathcal{C}(U_x)} = P_{xy(\eta)}^{(2)}|\phi \rangle_{\mathcal{C}(U_x)}$ , where  $P_{xy(\eta)}^{(2)} = [1 + (-1)^{s_2}\vec{r}_{xy}(\eta)\cdot \vec{\sigma}] / 2$ . To generate an eigenvalue equation whose operator commutes with  $\vec{r}_{xy}(\eta)\cdot \vec{\sigma}$ , we manipulate Eq. (83c) in the following way:

$$
\sigma_ {z} ^ {(2)} \sigma_ {x} ^ {(3)} | \phi \rangle_ {\mathcal {C} \left(U _ {x}\right)} = | \phi \rangle_ {\mathcal {C} \left(U _ {x}\right)}, \tag {89}
$$

i.e.,

$$
\sigma_ {z} ^ {(2)} | \phi \rangle_ {\mathcal {C} (U _ {x})} = \sigma_ {x} ^ {(3)} | \phi \rangle_ {\mathcal {C} (U _ {x})},
$$

i.e.,

$$
\left. \left[ \sigma_ {z} ^ {(2)} - \sigma_ {x} ^ {(3)} \right] \mid \phi \right\rangle_ {\mathcal {C} \left(U _ {x}\right)} = 0,
$$

therefore

$$
\left. \exp \left(- i \eta / 2 \left[ \sigma_ {z} ^ {(2)} - \sigma_ {x} ^ {(3)} \right]\right) \mid \phi \right\rangle_ {\mathcal {C} \left(U _ {x}\right)} = \mid \phi \rangle_ {\mathcal {C} \left(U _ {x}\right)}, \tag {90}
$$

where the last equation is true for all  $\eta \in [0,2\pi]$ . This takes a more useful form, if we write it in terms of one-qubit rotations,

$$
U _ {z} ^ {(2)} [ \eta ] U _ {x} ^ {(3)} [ - \eta ] | \phi \rangle_ {\mathcal {C} (U _ {x})} = | \phi \rangle_ {\mathcal {C} (U _ {x})}. \tag {91}
$$

We use this, and the equation

$$
\sigma_ {z} ^ {(1)} \sigma_ {x} ^ {(2)} \sigma_ {z} ^ {(3)} \quad | \phi \rangle_ {\mathcal {C} \left(U _ {x}\right)} = | \phi \rangle_ {\mathcal {C} \left(U _ {x}\right)}, \tag {92}
$$

to construct the subsequent eigenvalue equation. Let us denote the operator on the lhs of eigenvalue equation (91) as  $A$ , and the operator on the lhs of Eq. (92) as  $B$ . With Eqs. (91) and (92) it follows that  $ABA^{-1}|\phi\rangle_{\mathcal{C}(U_x)} = |\phi\rangle_{\mathcal{C}(U_x)}$ , i.e.,

$$
\begin{array}{l} \left| \phi \right\rangle_ {\mathcal {C} \left(U _ {x}\right)} = \sigma_ {z} ^ {(1)} U _ {z} ^ {(2)} [ \eta ] \sigma_ {x} ^ {(2)} U _ {z} ^ {(2)} [ - \eta ] U _ {x} ^ {(3)} [ - \eta ] \\ \times \sigma_ {z} ^ {(3)} U _ {x} ^ {(3)} [ \eta ] | \phi \rangle_ {\mathcal {C} \left(U _ {x}\right)}. \tag {93} \\ \end{array}
$$

Note that the operators  $A$  and  $B$  do not commute.

Applying  $P_{xy(\eta),2}$  to both sides, we obtain the following eigenvalue equation for  $\left|\psi \right\rangle_{\mathcal{C}(U_x)}$

$$
\sigma_ {z} ^ {(1)} U _ {x} ^ {(3)} [ - \eta ] \sigma_ {z} ^ {(3)} U _ {x} ^ {(3)} [ \eta ] | \psi \rangle_ {\mathcal {C} (U _ {x})} = (- 1) ^ {s _ {2}} | \psi \rangle_ {\mathcal {C} (U _ {x})}. \tag {94}
$$

In the same way as for the identity gate we also apply the projector to an eigenvalue equation generated from Eqs. (83a) and (83c) to obtain

$$
\begin{array}{l} \left| \psi \right\rangle_ {\mathcal {C} \left(U _ {x}\right)} = \sigma_ {x} ^ {(1)} \sigma_ {x} ^ {(3)} \left| \psi \right\rangle_ {\mathcal {C} \left(U _ {x}\right)} \\ = \sigma_ {x} ^ {(1)} U _ {x} ^ {(3)} [ - \eta ] \sigma_ {x} ^ {(3)} U _ {x} ^ {(3)} [ \eta ] | \psi \rangle_ {\mathcal {C} (U _ {x})}, \tag {95} \\ \end{array}
$$

and thus we see that Eq. (61) is satisfied for  $U = U_{x}[-\eta]$  and  $U_{\Sigma} = \sigma_z^{s_1}\sigma_x^{s_2}$ . Interchanging the order of these operators is not as trivial here as for the identity gate. When  $\sigma_z$  is propagated through  $U_{x}[\eta]$ , the sign of the angle is reversed, so we find that the gate operation realized by this  $\mathcal{M}(U_x)$  in the  $\mathrm{QC}_{\mathcal{C}}$  is

$$
U _ {g} = U _ {x} \left[ (- 1) ^ {s _ {1}} (- \eta) \right]. \tag {96}
$$

The sign of the rotation realized by this gate is a function of  $s_1$ , the outcome of the measurement on qubit 1. This is an example of the temporal ordering of measurements in the  $\mathrm{QC}_{\mathcal{C}}$ . In order to realize  $U_{x}[\alpha]$  deterministically, the angle of the measurement,  $\eta$ , on qubit 2 must be  $\eta = (-1)^{s_1}(-\alpha)$ , thus this measurement can only be realized after the measurement of qubit 1.

# 4. Rotation around  $z$  axis

The measurement pattern for a rotation around the  $z$  axis  $U_{z}[\beta] = \exp[-i\beta / 2\sigma_{z}]$  is illustrated in Fig. 2. It requires five qubits for its realization.

The measurement layout  $\mathcal{M}(U_z)$  is similar to the rotation about the  $x$  axis, except for two additional  $\sigma_x$  measurements on either side of the central qubit. The simplest way to understand this gate is to regard it as the concatenation

![](images/cc05aee8699f17fd2b74eaadffd7468d8ec25bf52745d86fa914144dfcc43c57.jpg)  
FIG. 5. Useful identity for the realization of the rotation  $U_z[\alpha]$  as the sequence  $H U_x[\alpha]H$ .

$U_{z}[\alpha] = H U_{x}[\alpha]H$ . The Hadamard transformations may be realized as wires of length one, see Sec. II G 1. Thus, the measurement pattern of the  $z$  rotation is that of the  $x$  rotation plus one cluster qubit on either side measured in the eigenbasis of  $\sigma_{x}$ , as displayed in Fig. 5.

The explanation in terms of eigenvalue equations obeyed by cluster states is as follows. Let us label the qubits 1-5. The cluster state  $|\phi \rangle_{\mathcal{C}(U_z)}$  is defined by eigenvalue equations of the usual form. If qubits 2 and 4 are measured in the  $\sigma_x$  basis, the resulting state  $|\phi^{\prime}\rangle_{\mathcal{C}(U_z)} = P_{x,s_2}^{(2)}P_{x,s_4}^{(4)}|\phi \rangle_{\mathcal{C}(U_z)}$  fulfills the following set of eigenvalue equations:

$$
\sigma_ {x} ^ {(1)} \sigma_ {x} ^ {(3)} \sigma_ {x} ^ {(5)} | \phi^ {\prime} \rangle_ {\mathcal {C} \left(U _ {z}\right)} = | \phi^ {\prime} \rangle_ {\mathcal {C} \left(U _ {z}\right)}, \tag {97a}
$$

$$
\sigma_ {z} ^ {(1)} \sigma_ {z} ^ {(3)} \sigma_ {x} ^ {(5)} | \phi^ {\prime} \rangle_ {\mathcal {C} \left(U _ {z}\right)} = (- 1) ^ {s _ {2}} | \phi^ {\prime} \rangle_ {\mathcal {C} \left(U _ {z}\right)}, \tag {97b}
$$

$$
\sigma_ {x} ^ {(1)} \sigma_ {z} ^ {(3)} \sigma_ {z} ^ {(5)} | \phi^ {\prime} \rangle_ {\mathcal {C} (U _ {z})} = (- 1) ^ {s _ {4}} | \phi^ {\prime} \rangle_ {\mathcal {C} (U _ {z})}. \tag {97c}
$$

This set of equations is analogous to Eqs. (83), except for the different eigenvalues and that the input and output qubits  $x$  and  $z$  bases have been exchanged. From here on the analysis of the measurement pattern runs parallel to the preceding section.

One finds  $\mathcal{M}(U_z)$  realizes the operation  $U_{z}(\beta)$  if the basis of the measurement on qubit 3 is chosen to be the eigenbasis of  $\vec{r}_{xy}((-1)^{s_2}(-\beta))\cdot \vec{\sigma}$ , where  $\vec{r}_{xy}(\eta)$  is defined in Eq. (88). Qubit 2 must thus be measured prior to qubit 3. The byproduct operator for this gate is  $U_{\Sigma ,U_z} = \sigma_x^{s_2 + s_4}\sigma_z^{s_1 + s_3}$ .

# 5. Arbitrary rotation

The arbitrary Euler rotation can be realized by combining the measurement patterns of rotations around  $x$  and  $z$  axes by overlaying input and output qubits of adjacent patterns, as described in Sec. II D. This creates a measurement pattern of seven qubits plus input and output qubits, labeled as in Fig. 6, with measurements of  $\sigma_{x}$  on qubits 3, 4, 6, and 7, and measurements in the  $x - y$  plane at angles  $\alpha$ ,  $\beta$ , and  $\gamma$  on qubits 2, 5, and 8, respectively.

The unitary operation realized by these connected measurement patterns is

![](images/e47fda1c43407cdd4a136d02786be79edd062b39a14b4f84cfe9dcb8f3e9f283.jpg)  
FIG. 6. General rotation composed of two  $x$  rotations and a  $z$  rotation in between (Euler representation). In the  $\mathrm{QC}_C$  realization pairs of adjacent cluster qubits measured in the  $\sigma_x$  eigenbasis may be removed from the measurement pattern.

$$
\begin{array}{l} U _ {\Sigma} U _ {R o t} [ \xi , \eta , \zeta ] = \sigma_ {s} ^ {s 7} \sigma_ {x} ^ {s 8} U _ {x} [ (- 1) ^ {s 7} (- \gamma) ] \\ \times \sigma_ {z} ^ {s _ {3} + s _ {5}} \sigma_ {x} ^ {s _ {4} + s _ {6}} U _ {z} [ (- 1) ^ {s _ {4}} (- \beta) ] \\ \times \sigma_ {z} ^ {s _ {1}} \sigma_ {x} ^ {s _ {2}} U _ {x} [ (- 1) ^ {s _ {1}} (- \alpha) ]. \tag {98} \\ \end{array}
$$

As we have shown above, adjacent pairs of  $\sigma_{x}$  measurements can be removed from the pattern without changing the operation realized by the gate. The operation realized by this reduced measurement pattern is obtained by setting the measurement results from the removed qubits to  $0$ ,  $s_3, s_4, s_6, s_7 = 0$ . After relabelling the remaining qubits in the measurement patterns 1-5, we obtain

$$
\begin{array}{l} U _ {\Sigma} U _ {R o t} [ \xi , \eta , \zeta ] = \sigma_ {x} ^ {s _ {4}} U _ {x} [ - \gamma ] \sigma_ {z} ^ {s _ {3}} U _ {z} [ (- \beta) ] \\ \times \sigma_ {z} ^ {s _ {1}} \sigma_ {x} ^ {s _ {2}} U _ {x} [ (- 1) ^ {s _ {1}} (- \alpha) ]. \tag {99} \\ \end{array}
$$

Propagating all byproduct operators to the left-hand side, we find that the unitary operation realized by the measurement pattern is

$$
\begin{array}{l} U _ {R o t} [ \xi , \eta , \zeta ] = U _ {x} [ - (- 1) ^ {s _ {1} + s _ {3}} \gamma ] U _ {z} [ - (- 1) ^ {s _ {2}} \beta ] \\ \times U _ {x} \left[ - (- 1) ^ {s _ {1}} \alpha \right], \tag {100} \\ \end{array}
$$

with byproduct operator  $U_{\Sigma} = \sigma_x^{s_2 + s_4}\sigma_z^{s_1 + s_3}$ . One finds that, to realize a specific rotation  $U_{Rot}[\xi ,\eta ,\zeta ] = U_x[\zeta ]U_z[\eta ]U_x[\xi ]$ , the angles  $\alpha$ ,  $\beta$ ,  $\gamma$  specifying the measurement bases of the qubits 2, 3, and 4 are again dependent on the measurement results of other qubits. We see that  $\alpha = (-1)^{s_1}(-\xi)$ ,  $\beta = (-1)^{s_2}(-\eta)$ ,  $\gamma = (-1)^{s_1 + s_3}(-\zeta)$ . To realize a specific rotation deterministically, qubit 2 must thus be measured before qubits 3 and 4, and qubit 3 before qubit 4, in the bases specified in Sec. II B.

# 6. Hadamard and  $\pi /2$ -phase gates

The Hadamard and the  $\pi /2$ -phase gates have the property that under conjugation with these gates Pauli operators are mapped onto Pauli operators,

$$
H \sigma_ {x} H ^ {\dagger} = \sigma_ {z}, \tag {101}
$$

$$
H \sigma_ {z} H ^ {\dagger} = \sigma_ {x},
$$

and

$$
\begin{array}{l} U _ {z} [ \pi / 2 ] \sigma_ {x} U _ {z} [ \pi / 2 ] ^ {\dagger} = \sigma_ {y}, \tag {102} \\ U _ {z} [ \pi / 2 ] \sigma_ {z} U _ {z} [ \pi / 2 ] ^ {\dagger} = \sigma_ {z}, \\ \end{array}
$$

from which propagation relations (53) follow. Related to this property is the fact that these two special rotations may be realized via  $\sigma_{x}$  and  $\sigma_{y}$  measurements. Such measurement bases need not be adapted to previously obtained measurement results and, therefore, while these rotations might be realized in the same way as any other rotation, there is a more advantageous way to do so.

To realize either of the gates we use again a cluster state of five qubits in a chain  $\mathcal{C}(H)$ . Let the labeling of the qubits be as in Figs. 2(d) and 2(e), i.e., qubit 1 is the input and qubit 5 is the output qubit.

A cluster state  $|\phi \rangle_{\mathcal{C}(H)}$  obeys the two eigenvalue equations

$$
\begin{array}{l} \left| \phi \right\rangle_ {\mathcal {C} (H)} = K ^ {(1)} K ^ {(3)} K ^ {(4)} \left| \phi \right\rangle_ {\mathcal {C} (H)} = \sigma_ {x} ^ {(1)} \sigma_ {y} ^ {(3)} \sigma_ {y} ^ {(4)} \sigma_ {z} ^ {(5)} \left| \phi \right\rangle_ {\mathcal {C} (H)}, \tag {103} \\ \left| \phi \right\rangle_ {\mathcal {C} (H)} = K ^ {(2)} K ^ {(3)} K ^ {(5)} \left| \phi \right\rangle_ {\mathcal {C} (H)} = \sigma_ {z} ^ {(1)} \sigma_ {y} ^ {(2)} \sigma_ {y} ^ {(3)} \sigma_ {x} ^ {(5)} \left| \phi \right\rangle_ {\mathcal {C} (H)}. \\ \end{array}
$$

When qubits 2, 3, and 4 of this state are measured in the  $\sigma_{y}$  eigenbasis and thereby the measurement outcomes  $s_2$ ,  $s_3$ ,  $s_4 \in \{0,1\}$  are obtained, the resulting state  $|\psi\rangle_{\mathcal{C}(H)}$  obeys the eigenvalue equations

$$
\begin{array}{l} \left. \sigma_ {x} ^ {(1)} \sigma_ {z} ^ {(5)} \right| \phi \rangle_ {\mathcal {C} (H)} = (- 1) ^ {s _ {3} + s _ {4}} | \phi \rangle_ {\mathcal {C} (H)}, \tag {104} \\ \sigma_ {z} ^ {(1)} \sigma_ {x} ^ {(5)} | \phi \rangle_ {\mathcal {C} (H)} = (- 1) ^ {s _ {2} + s _ {3}} | \phi \rangle_ {\mathcal {C} (H)}. \\ \end{array}
$$

From Eq. (101) we see that correlations (104) are precisely those we need to explain the realization of the Hadamard gate. Using Theorem 1 we find that by Procedure 3 with measurement of the operators  $\sigma_x^{(1)}$ ,  $\sigma_y^{(2)}$ ,  $\sigma_y^{(3)}$ , and  $\sigma_y^{(4)}$  a Hadamard gate with a byproduct operator, as given in Eq. (30), is realized.

Considering the rotation  $U_{z}[\pi /2]$ , a cluster state  $|\phi \rangle_{\mathcal{C}(U_z[\pi /2])}$  of a chain of five qubits obeys the eigenvalue equations

$$
\begin{array}{l} \left| \phi \right\rangle_ {\mathcal {C} (U _ {z} [ \pi / 2 ])} = K ^ {(1)} K ^ {(3)} K ^ {(4)} K ^ {(5)} \left| \phi \right\rangle_ {\mathcal {C} (U _ {z} [ \pi / 2 ])}, \\ = - \sigma_ {x} ^ {(1)} \sigma_ {y} ^ {(3)} \sigma_ {x} ^ {(4)} \sigma_ {y} ^ {(5)} | \phi \rangle_ {\mathcal {C} (U _ {z} [ \pi / 2 ])} | \phi \rangle_ {\mathcal {C} (U _ {z} [ \pi / 2 ])} \\ = K ^ {(2)} K ^ {(4)} \mid \phi \rangle_ {\mathcal {C} (U _ {z} [ \pi / 2 ])} \\ = \sigma_ {z} ^ {(1)} \sigma_ {x} ^ {(2)} \sigma_ {x} ^ {(4)} \sigma_ {z} ^ {(5)} | \phi \rangle_ {\mathcal {C} (U _ {z} [ \pi / 2 ]).} \tag {105} \\ \end{array}
$$

When qubits 2 and 4 of this state are measured in the  $\sigma_{x}$  eigenbasis and qubit 3 is measured in the  $\sigma_{y}$  eigenbasis, with the measurement outcomes  $s_2$ ,  $s_3$ ,  $s_4 \in \{0,1\}$  obtained, the resulting state  $|\psi\rangle_{\mathcal{C}(U,[\pi/2])}$  obeys the eigenvalue equations

$$
\begin{array}{l} \sigma_ {x} ^ {(1)} \sigma_ {y} ^ {(5)} | \psi \rangle_ {\mathcal {C} \left(U _ {z} [ \pi / 2 ]\right)} = (- 1) ^ {s _ {3} + s _ {4} + 1} | \psi \rangle_ {\mathcal {C} \left(U _ {z} [ \pi / 2 ]\right)}, \tag {106} \\ \sigma_ {z} ^ {(1)} \sigma_ {z} ^ {(5)} | \psi \rangle_ {\mathcal {C} (U _ {z} [ \pi / 2 ])} = (- 1) ^ {s _ {2} + s _ {4}} | \psi \rangle_ {\mathcal {C} (U _ {z} [ \pi / 2 ]).} \\ \end{array}
$$

Using Theorem 1 we find that by Procedure 3 with measurement of the operators  $\sigma_x^{(1)}$ ,  $\sigma_x^{(2)}$ ,  $\sigma_y^{(3)}$ , and  $\sigma_x^{(4)}$  a  $\pi/2$ -phase gate is realized, where the byproduct operator is given by Eq. (30).

# 7. The CNOT gate

A measurement pattern that realizes a CNOT gate is illustrated in Fig. 2. Labeling the qubits as in Fig. 2, we use the same analysis as above to show that this measurement pattern does indeed realize a CNOT gate in the  $\mathrm{QC}_{\mathcal{C}}$ .

Of the cluster  $\mathcal{C}(\mathrm{CNOT})$  on which the gate is realized, qubits 1 and 9 belong to  $\mathcal{C}_I$ , qubits 7 and 15 belong to  $\mathcal{C}_O$  and

![](images/a49beba2e531f914f68bfa868153da26b2cc12ca67322bf39c6363a9f6845a01.jpg)  
FIG. 7. Pattern of correlation centers representing eigenvalue equation (107a).

the remaining qubits belong to  $\mathcal{C}_M$ . Let  $|\phi\rangle$  be a cluster state on  $\mathcal{C}(\mathrm{CNOT})$ , which obeys the set of eigenvalue equations (1).

From these basic eigenvalue equations there follow the equations

$$
\begin{array}{l} \left| \phi \right\rangle = K ^ {(1)} K ^ {(3)} K ^ {(4)} K ^ {(5)} K ^ {(7)} K ^ {(8)} K ^ {(1 3)} K ^ {(1 5)} \left| \phi \right\rangle \\ = - \sigma_ {x} ^ {(1)} \sigma_ {y} ^ {(3)} \sigma_ {y} ^ {(4)} \sigma_ {y} ^ {(5)} \sigma_ {x} ^ {(7)} \sigma_ {y} ^ {(8)} \sigma_ {x} ^ {(1 3)} \sigma_ {x} ^ {(1 5)} | \phi \rangle , \tag {107a} \\ \end{array}
$$

$$
\left| \phi \right\rangle = K ^ {(2)} K ^ {(3)} K ^ {(5)} K ^ {(6)} \left| \phi \right\rangle = \sigma_ {z} ^ {(1)} \sigma_ {y} ^ {(2)} \sigma_ {y} ^ {(3)} \sigma_ {y} ^ {(5)} \sigma_ {y} ^ {(6)} \sigma_ {z} ^ {(7)} \left| \phi \right\rangle , \tag {107b}
$$

$$
\left| \phi \right\rangle = K ^ {(9)} K ^ {(1 1)} K ^ {(1 3)} K ^ {(1 5)} \left| \phi \right\rangle = \sigma_ {x} ^ {(9)} \sigma_ {x} ^ {(1 1)} \sigma_ {x} ^ {(1 3)} \sigma_ {x} ^ {(1 5)} \left| \phi \right\rangle , \tag {107c}
$$

$$
\begin{array}{l} \left| \phi \right\rangle = K ^ {(5)} K ^ {(6)} K ^ {(8)} K ^ {(1 0)} K ^ {(1 2)} K ^ {(1 4)} \left| \phi \right\rangle \\ = \sigma_ {y} ^ {(5)} \sigma_ {y} ^ {(6)} \sigma_ {z} ^ {(7)} \sigma_ {y} ^ {(8)} \sigma_ {z} ^ {(9)} \sigma_ {x} ^ {(1 0)} \sigma_ {y} ^ {(1 2)} \sigma_ {x} ^ {(1 4)} \sigma_ {z} ^ {(1 5)} | \phi \rangle . \tag {107d} \\ \end{array}
$$

Subsequently, we will often use a graphic representation of eigenvalue equations such as (107a)-(107d). Each of these equations is specified by the set of correlation centers  $q$  for which the basic correlation operators  $K^{(q)}$  (2) enter the rhs of the equation. While the information content is the same, it is often more illustrative to display the pattern of correlation centers than to write down the corresponding cluster state eigenvalue equation. As an example, the pattern of correlation centers, which represents the eigenvalue equation (107a) is given in Fig. 7.

If the qubits 10, 11, 13, and 14 are measured in the  $\sigma_{x}$  eigenbasis and the qubits 2, 3, 4, 5, 6, 8, and 12 are measured in the  $\sigma_{y}$  eigenbasis, whereby the measurement results  $s_2 - s_6$ ,  $s_8$ ,  $s_{10} - s_{14}$  are obtained, then the cluster state eigenvalue equations (107a)-(107d) induce the following eigenvalue equations for the projected state  $|\psi \rangle$

$$
\begin{array}{l} \left. \sigma_ {x} ^ {(1)} \sigma_ {x} ^ {(7)} \sigma_ {x} ^ {(1 5)} \right| \psi \rangle = (- 1) ^ {1 + s _ {3} + s _ {4} + s _ {5} + s _ {8} + s _ {1 3}} \left| \psi \right\rangle , (108a) \\ \left. \sigma_ {z} ^ {(1)} \sigma_ {z} ^ {(7)} \right| \psi \rangle = (- 1) ^ {s _ {2} + s _ {3} + s _ {5} + s _ {6}} | \psi \rangle , (108b) \\ \left. \sigma_ {x} ^ {(9)} \sigma_ {x} ^ {(1 5)} | \psi \rangle = (- 1) ^ {s _ {1 1} + s _ {1 3}} | \psi \rangle , \right. (108c) \\ \sigma_ {z} ^ {(9)} \sigma_ {z} ^ {(7)} \sigma_ {z} ^ {(1 5)} | \psi \rangle = (- 1) ^ {s _ {5} + s _ {6} + s _ {8} + s _ {1 0} + s _ {1 2} + s _ {1 4}} | \psi \rangle . (108d) \\ \end{array}
$$

Therein, qubits 1 and 7 represent the input and output for the control qubit and qubits 9 and 15 represent the input and output for the target qubit. Writing the CNOT unitary operation on control and target qubits  $\mathrm{CNOT}(c,t)$ , we find

$$
\operatorname {C N O T} (c, t) \sigma_ {x} ^ {(c)} \operatorname {C N O T} (c, t) = \sigma_ {x} ^ {(c)} \sigma_ {x} ^ {(t)}, \tag {109a}
$$

$$
\operatorname {C N O T} (c, t) \sigma_ {z} ^ {(c)} \operatorname {C N O T} (c, t) = \sigma_ {z} ^ {(c)}, \tag {109b}
$$

$$
\operatorname {C N O T} (c, t) \sigma_ {x} ^ {(t)} \operatorname {C N O T} (c, t) = \sigma_ {x} ^ {(t)}, \tag {109c}
$$

$$
\operatorname {C N O T} (c, t) \sigma_ {z} ^ {(t)} \operatorname {C N O T} (c, t) = \sigma_ {z} ^ {(c)} \sigma_ {z} ^ {(t)}. \tag {109d}
$$

Comparing these equations to eigenvalue equations (108a)-(108d), one sees that  $\mathcal{M}$  does indeed realize a CNOT gate. Furthermore, after reading off the operator  $U_{\Sigma}$  using Eqs. (61) and (63) and propagating the byproduct operators through the output side of the CNOT gate, one finds the expressions for the byproduct operators, reported in Eq. (23).

# H. Upper bounds on resource consumption

Here we discuss the spatial, temporal, and operational resources required for the  $\mathrm{QC}_{\mathcal{C}}$  and compare with resource requirements of a network quantum computer.

To run a specific quantum algorithm, the  $\mathrm{QC}_{\mathcal{C}}$  requires a cluster of a certain size. Therefore, the  $\mathrm{QC}_{\mathcal{C}}$ -spatial resources  $S$  are the number of cluster qubits in the required cluster state  $|\phi\rangle_{\mathcal{C}}$ , i.e.,  $S = |\mathcal{C}|$ . The computation is driven by one-qubit measurement only. Thus, a single one-qubit measurement is one unit of operational resources, and the  $\mathrm{QC}_{\mathcal{C}}$ -operational resources  $O$  are defined as the total number of one-qubit measurements involved. The operational resources  $O$  are always smaller or equal to the spatial resources  $S$ ,

$$
O \leqslant S, \tag {110}
$$

since each cluster qubit is measured at most once. As for the temporal resources, the  $\mathrm{QC}_C$ -logical depth  $T$  is the minimum number of measurement rounds to which the measurements can be parallelized.

Let us briefly recall the definition of these resources in the network model. The temporal resources are specified by the network logical depth  $T_{\mathrm{qln}}$ , which is the minimal number of steps to which quantum gates and readout measurements can be parallelized. The spatial resources  $S_{\mathrm{qln}}$  count the number of logical qubits on which an algorithm runs. Finally, the operational resources  $O_{\mathrm{qln}}$  are the number of elementary operations required to carry out an algorithm, i.e., the number of gates and measurements.

The construction kit for the simulation of quantum logic networks on the  $\mathrm{QC}_{\mathcal{C}}$  shall contain a universal set of gates, in our case the CNOT gate between arbitrary qubits and the one qubit rotations. Already the next-neighbor CNOT with general rotations is universal since a general CNOT can be assembled of a next-neighbor CNOT and swap gates, which can themselves be composed of next-neighbor CNOTs. However, in the following we would like to use for the general CNOT the less cumbersome construction described in Sec. IV B. For this gate, the distance between logical qubits, i.e., between paral

Ie 1. The virtue of this gate is that it can always be realized on a vertical slice of width 6 on the cluster, no matter how far control and target qubit are separated. A slice of width 6 means that the distance between an input qubit of the gate and the corresponding input of the consecutive gate is six lattice spacings. This general CNOT gate determines the spatial dimensions of a unit cell in the measurement patterns. The size of this unit cell is  $4\times 6$ . The other elementary gates, the next-neighbor CNOT and the rotations are smaller than a unit cell and therefore have to be stretched. This is easily accomplished. The next-neighbor CNOT, as displayed in Fig. 2(a) has a size of  $2\times 6$  and is extended to size  $4\times 6$  by inserting two adjacent cluster qubits into the vertical bridge connecting the horizontal qubit lines. The general rotation as in Fig. 2(b) has width 4 and is stretched to width 6 by inserting two cluster qubits just before the output.

Concerning the temporal resources we first observe that we can realize the gates in the same temporal order as in the network model. To realize a general CNOT on the  $\mathrm{QC}_{\mathcal{C}}$  takes one step of measurements, to realize a general rotation takes at most three. For the network model we do not assume that a general rotation has to be Euler-decomposed. Rather we assume that in the network model a rotation can be realized in a single step. Thus, the temporal resources of the  $\mathrm{QC}_{\mathcal{C}}$  and in the network model are related via

$$
T \leqslant 3 T _ {\mathrm {q l n}}. \tag {111}
$$

As for the spatial resources, let us consider a rectangular cluster of height  $h$  and width  $w$  on which the qubit wires are oriented horizontally, with the network register state propagating from left to right. As the logical qubits have distance 4, the height of the cluster has to be  $h = 4S_{\mathrm{qln}} - 3$ , where  $S_{\mathrm{qln}}$  is equal to the number  $n$  of logical qubits. Further, the number of gates in the circuit is at most  $S_{\mathrm{qln}}T_{\mathrm{qln}}$  because, in the network model, in each step at most  $S_{\mathrm{qln}}$  gates can be realized. On each vertical slice of width 6 on the cluster there fits at least one gate such that—taking into account an extra slice of width 1 for the readout cluster qubits—for the width holds  $w \leqslant 6S_{\mathrm{qln}}T_{\mathrm{qln}} + 1$ . With  $S = h w$  one finds that

$$
S \leqslant 2 4 S _ {\mathrm {q l n}} ^ {2} T _ {\mathrm {q l n}}. \tag {112}
$$

In a similar way, a bound involving the network operational resources can be obtained. The spatial overhead  $S$  and the operational overhead  $O$  per elementary network operation is  $\leqslant 24S_{\mathrm{qln}}$  if this operation is a unitary gate from the universal set described before, and is equal to 1 if this operation is a readout measurement. Thus, we also have

$$
S \leqslant 2 4 O _ {\mathrm {q l n}} S _ {\mathrm {q l n}},
$$

$$
O \leqslant 2 4 O _ {\mathrm {q l n}} S _ {\mathrm {q l n}}. \tag {113}
$$

The purpose of this section was to demonstrate that the scaling of spatial and temporal resources is at worst polynomial as compared to the network model. In Ref. [7] it has been shown, as stated in Sec. III A, that the required classical processing increases the computation time only marginally

(logarithmically in the number  $n$  of logical qubits), and thus there is no exponential overhead in either classical or quantum resources.

The upper bounds in Eqs. (111)-(113) should not be taken for estimates. For algorithms of practical interest the required resources usually scale much more favorably and there do not even have to be overheads at all. This is illustrated for the temporal complexity of Clifford circuits in Sec. II I and in the examples of Sec. IV. A spatial overhead always exists. However, this is compensated by the fact that the operational effort to create a cluster state is independent of the cluster size.

# I. Quantum circuits in the Clifford group can be realized in a single step

The measurement bases to realize the Hadamard and the  $\pi /2$ -phase gates need not be adapted since only operators  $\sigma_{x}$  and  $\sigma_{y}$  are measured. The same holds for the realization of the CNOT gate, see Fig. 2. Thus, all the Hadamard,  $\pi /2$ -phase, and CNOT gates of a quantum circuit can be realized simultaneously in the first measurement round, regardless of their location in the network. In particular, quantum circuits that consist only of such gates, i.e., circuits in the Clifford group, can be realized in a single time step. As an example, many circuits for coding and decoding are in the Clifford group.

The fact that quantum circuits in the Clifford group can be realized in a single time step has previously not been known for networks. The best upper bound on the logical depth that was known previously scales logarithmically with the number of logical qubits [21].

Note that, as stated by the Gottesman-Knill theorem [22], there is no need for fast Clifford circuits if the quantum output is measured in a Pauli basis because these circuits can be simulated efficiently classically. However, the purpose of this section is to point out that the whole Clifford part of any quantum circuit can be performed in a single time step. We will discuss this point further in Sec. III B.

Here we find a first aspect of  $\mathrm{QC}_{\mathcal{C}}$  computation, which is not adequately described within the network model, and with this observation we conclude the discussion of the  $\mathrm{QC}_{\mathcal{C}}$  as a simulator of quantum logic networks.

# III. COMPUTATIONAL MODEL UNDERLYING THE  $\mathbf{Q}\mathbf{C}_{\mathcal{C}}$

# A. Processing of information

In the network model of quantum computation one usually regards a quantum register as the carrier of information. The quantum register is prepared in some input state and processed to some output state by applying a suitable unitary transformation composed of quantum gates. Finally, the output state of the quantum register is measured by which the classical readout is obtained.

For the  $\mathrm{QC}_{\mathcal{C}}$  the notions of "quantum input" and "quantum output" have no genuine meaning if we restrict ourselves to the situation where the input state is known. As stated before, Shor's factoring algorithm [17] and Grover's search algorithm [18] are both examples of such a situation.

In these cases the final result of any computation -including quantum computations--is a classical number. In a  $\mathrm{QC}_{\mathcal{C}}$  computation this number is extracted from the outcomes of all the one-qubit measurements. The entire computation amounts to just measurements of the cluster qubits in a certain order and basis.

We have divided the set  $\mathcal{C}$  of cluster qubits into subsets  $I$ ,  $M$ , and  $O$  to describe the  $\mathrm{QC}_{\mathcal{C}}$  in terms of the network model. Such a terminology is not required for the  $\mathrm{QC}_{\mathcal{C}}$  a priori. It is true that when a quantum logic network is realized on a cluster state there is a subset of cluster qubits that play the role of the output register. However, these qubits are not the final ones to be measured, but among the first (!). The measurement outcomes from all the cluster qubits contribute to the result of the computation. The qubits of  $O \subset \mathcal{C}$  simulate the output state of the quantum register and thus contribute obviously to the computational result. The cluster qubits in the set  $I \subset \mathcal{C}$  simulate the fiducial input state of the quantum register and their measurement contributes via the accumulated byproduct operator on  $O$ . Finally, the qubits in the section  $M \subset \mathcal{C}$  of the cluster whose measurements simulate the quantum gates also contribute via the byproduct operator.

Naturally there arises the question whether there is any difference in the way how measurements of cluster qubits in  $I$ ,  $O$ , or  $M$  contribute to the final result of the computation. As shown in Ref. [7], it turns out that there is none. This is why we can abandon the notions of quantum input, quantum output, and quantum register, altogether from the description of the  $\mathrm{QC}_{\mathcal{C}}$ .

Furthermore, quantum gates are not constitutive elements of the  $\mathrm{QC}_{\mathcal{C}}$ ; these are instead one-qubit measurements performed in a certain temporal order and in a spatial pattern of adaptive measurement bases. In fact, the most efficient temporal order of the measurements does not follow from the temporal order of the simulated gates in the network model.

The general view of a  $\mathrm{QC}_{\mathcal{C}}$  computation is as follows. The cluster  $\mathcal{C}$  is divided into disjoint subsets  $Q_{t} \subset \mathcal{C}$  with  $0 \leqslant t \leqslant t_{\max}$ , i.e.,  $\sum_{t=0}^{t_{\max}} Q_{t} = \mathcal{C}$  and  $Q_{s} \cap Q_{t} = \emptyset$  for all  $s \neq t$ . The cluster qubits within each set  $Q_{t}$  can be measured simultaneously and the sets are measured one after another. The set  $Q_{0}$  consists of all those qubits for which no measurement bases have to be adjusted, i.e., those of which the operator  $\sigma_{x}, \sigma_{y}$ , or  $\sigma_{z}$  is measured. In the subsequent measurement rounds only operators of the form  $\cos \varphi \sigma_{x} \pm \sin \varphi \sigma_{y}$  are measured where  $|\varphi| < \pi/2$ ,  $\varphi \neq 0$ . The measurement bases are adaptive in these rounds, i.e., they are adapted to measurement results obtained in previous rounds. The measurement outcomes from the qubits in  $Q_{0}$  determine the measurement bases for the qubits in  $Q_{1}$ , which are measured in the second round, those from  $Q_{0}$  and  $Q_{1}$  together determine the bases for the measurements of the qubits in  $Q_{2}$ , which are measured in the third round, and so on. Finally, the result of the computation is calculated from the measurement outcomes obtained in all the measurement rounds (Fig. 8).

Now there arises the question of how complex the required classical processing is. In principle, it could be that all the obtained measurement results had to be stored separately and the functions to compute the measurement bases were so

![](images/feaaf963134bdadcf6054d96bc791d678b1ebc0bede7db094abcb91fb0d9235a.jpg)  
FIG. 8. General scheme of the quantum computer via one-qubit measurements. The sets  $Q_{t}$  of lattice qubits are measured one after the other. The results of earlier measurements determine the measurement bases of later ones. All classical information from the measurement results needed to steer the  $\mathrm{QC}_{\mathcal{C}}$  is contained in the information flow vector  $\mathbf{I}(t)$ . After the last measurement round  $t_{\max}$ ,  $\mathbf{I}(t_{\max})$  contains the result of the computation.

complicated that one would gain no advantage over the classical algorithm for the considered problem. This is not at all the case. If the network algorithm runs on  $n$  qubits, then the classical data that the  $\mathrm{QC}_{\mathcal{C}}$  has to keep track of is entirely contained in a  $2n$ -component binary valued vector, which we have called the information flow vector  $\mathbf{I}(t)$  [7]. The update of  $\mathbf{I}(t)$  is a classical computation that is needed to adapt the measurement bases of cluster qubits according to previous measurement outcomes. These updates and the final identification of the computational result from  $\mathbf{I}(t_{\max})$  are all elementary.

Concerning the resources for the classical processing of the measurement outcomes in a  $\mathrm{QC}_{\mathcal{C}}$  computation, we point out that this processing increases the total time of computation only marginally [7].

In summary, the formal description of the  $\mathrm{QC}_{\mathcal{C}}$  is based on primitive quantities of which the most important ones are the sets  $Q_{t} \subset \mathcal{C}$  of cluster qubits, defining the temporal ordering of measurements on the cluster state and the binary-valued information flow vector  $\mathbf{I}(t)$ , which is the carrier of the algorithmic information. The reader who is interested in how this computational model arises and in its detailed description is referred to Ref. [7], or, for concepts and summary, to Ref. [8].

# B. Quantum algorithms and graphs

In this section we relate  $\mathrm{QC}_{\mathcal{C}}$  algorithms to graphs. We do this by considering non-universal graph states suited for the specific algorithm in question. For the  $\mathrm{QC}_{\mathcal{C}}$ , the Clifford part of each algorithm can be removed. We show that a mathematical graph comprises all the information that needs to be kept of the Clifford part.

While the network formulation of a quantum algorithm is given as a sequence of quantum gates applied to a fiducial input state, the  $\mathrm{QC}_{\mathcal{C}}$  version of a quantum algorithm is speci

fied by a measurement pattern on the universal cluster state plus the structure [7] for the processing of the measurement outcomes.

To motivate the considerations of this section, note that the measurement pattern is, in the simplest case, just a copy of the network layout to the substrate cluster state, imprinted by the measurements. As such it contains information about the precise location of the gate simulations and about the way the "wires" connecting the gates are bent around. These are all details of the realization of an algorithm but do not belong to the description of the algorithm itself. Thus, the measurement pattern introduces a large amount of redundancy into the description of a  $\mathrm{QC}_{\mathcal{C}}$  algorithm. This redundancy may be reduced to a large extent by allowing for non-universal, algorithm-specific quantum resources.

Clearly, at this point one has to specify how special the algorithm-specific resource is allowed to be. Obviously it would make no sense to take the quantum output of the entire network as the required quantum resource and to regard the subsequent readout measurements as the algorithm. Here, we allow for any graph state [9], Eq. (20) as the quantum resource. Graph states are easy to create, e.g., via unitary networks or from cluster states via measurements.

To allow for an algorithm-specific graph state as the quantum resource of a  $\mathrm{QC}_{\mathcal{C}}$  computation reduces the redundancy of both the description and the realization of a quantum algorithm. This can easily be seen from the material presented in Sec. II C. All the cluster qubits  $q \in \mathcal{C} \setminus \mathcal{C}_N$  can be get rid of either by measuring them in the  $\sigma_z$  eigenbasis or equivalently by not placing them initially into their positions at all. The remaining state on the subcluster  $\mathcal{C}_N$  is again a cluster state. Hence, it is also a graph state. It is less redundant and no longer universal.

But we can go further. Not only the qubits measured in the  $\sigma_z$  eigenbasis may be removed from the cluster but instead all those qubits of which one of the Pauli operators  $\sigma_x$ ,  $\sigma_y$  or  $\sigma_z$  is measured, i.e., all the qubits which form the set  $Q_0$ . The state of the unmeasured qubits that emerges after the measurement of the cluster qubits in  $Q_0$  is again (local equivalent to) a graph state.

This may be seen as follows. First note that the operators  $\sigma_x^{(a)}\otimes_{b\in V}(\sigma_z^{(b)})^{\Gamma_{ab}}$  , which appear in Eq. (20) form a stabilizer of the state  $|\phi \{\kappa \} \rangle_G$  . The generator of the stabilizer contains  $|\mathcal{C}|$  elements for a state of  $|\mathcal{C}|$  qubits. After all the qubits  $q\in Q_0$  have been measured, the resulting state  $\left|\Psi \right\rangle_{\mathcal{C}\setminus Q_0}$  of the  $|\mathcal{C}\setminus Q_0|$  unmeasured qubits is again described by a stabilizer of the form

$$
\begin{array}{c}\stackrel {\left|\mathcal{C}\setminus Q_{0}\right|}{\bigotimes}\\ i = 1 \end{array} (\sigma_{x}^{(i)})^{X_{a,i}}(\sigma_{z}^{(i)})^{Z_{a,i}}|\Psi \rangle_{\mathcal{C}\setminus Q_{0}} = \pm \left|\Psi \right\rangle_{\mathcal{C}\setminus Q_{0}}
$$

$$
\forall a = 1, \dots , | \mathcal {C} \backslash Q _ {0} |, \tag {114}
$$

with two  $|\mathcal{C} \setminus Q_0| \times |\mathcal{C} \setminus Q_0|$  matrices  $X$  and  $Z$ , for which  $X_{a,i}, Z_{a,i} \in \{0,1\}$ . The  $|\mathcal{C} \setminus Q_0| \times 2|\mathcal{C} \setminus Q_0|$ -compound matrix  $(X|Z)$  [12] is called the generator matrix of the stabilizer for  $|\Psi\rangle_{\mathcal{C} \setminus Q_0}$ . The state  $|\Psi\rangle_{\mathcal{C} \setminus Q_0}$  is uniquely determined by the generator of its stabilizer.

The state  $|\Psi \rangle_{\mathcal{C} \setminus Q_0}$  can thus be regarded as a  $[|\mathcal{C} \setminus Q_0|, 0, d]$ -stabilizer code, with the distance  $d$  not specified. This state fulfills the assumptions of Theorem 1 in Ref. [23]. The cited theorem states that any stabilizer code over the alphabet  $A = \mathbb{F}_{p^m}$  is [local unitary] equivalent to a graph code.

We now specialize to the case of our interest,  $A = \mathbb{F}_{2^2}$ . It follows from the above-mentioned theorem that the state  $|\Psi\rangle_{\mathcal{C} \setminus Q_0}$  specified in Eq. (114) is local unitary equivalent to a graph state  $|\phi\{\kappa\}\rangle_{G(\mathcal{C} \setminus Q_0, E_{\mathcal{C} \setminus Q_0})}$  Eq. (20). That is, the state  $|\Psi\rangle_{\mathcal{C} \setminus Q_0}$  obtained in a  $\mathrm{QC}_{\mathcal{C}}$  computation after the first round of measurements may as well be obtained from a graph state  $|\phi\{\kappa\}\rangle_{G(\mathcal{C} \setminus Q_0, E_{\mathcal{C} \setminus Q_0})}$  via local unitary transformations; and the subsequent measurements may be performed as usual. Alternatively, one may use the graph state  $|\phi\{\kappa\}\rangle_{G(\mathcal{C} \setminus Q_0, E_{\mathcal{C} \setminus Q_0})}$  directly, only modifying the measurement bases instead of performing the local rotations prior to the measurements. Thus, in a  $\mathrm{QC}_{\mathcal{C}}$  computation with a special graph state as the quantum resource and the first measurement round omitted, the way of processing the classical information is the same as in a  $\mathrm{QC}_{\mathcal{C}}$  computation with a universal resource and the first measurement round performed.

The graphs associated with states (114) are, in general, not unique [23]. A constructive way to obtain graphs on  $\mathcal{C} \setminus Q_0$  from  $G(\mathcal{C}, E_{\mathcal{C}})$  and the measurement bases of the qubits in  $Q_0$  has been described in Ref. [24].

Now note that the measurement of the qubits in  $Q_{0}$  realize the Clifford part of a quantum circuit. The fact that we can reduce the quantum resource by these qubits means that we can remove from each quantum algorithm its Clifford part. This represents, in a way, an extension to the Knill-Gottesman theorem [22], stating that a quantum computation that consists only of quantum input state preparation in the computational basis, unitary gates in the Clifford group, measurement of observables in the Pauli group, and gates in the Clifford group conditioned on the outcomes of such measurements, may be simulated efficiently classically and thus requires no quantum resources at all.

With only a single non-Clifford operation in the circuit, such as a one-qubit rotation about most axes and angles, the efficient classical formalism on which the Gottesman-Knill theorem rests can no longer be applied. The  $\mathrm{QC}_{\mathcal{C}}$  construction, on the other hand, is not affected by this. Each quantum network algorithm in question may be reduced by its Clifford part. Only the non-Clifford gates require quantum resources. The price is that the universal quantum resource, the cluster state, is changed into a nonuniversal, algorithm-specific resource—a graph state (20)—on fewer qubits. The Clifford part of the network algorithm specifies the corresponding graph.

In conclusion, instead of describing a quantum algorithm as a network of gates applied to some fiducial input state, a quantum algorithm may (arguably more effectively) be characterized by a graph specifying the quantum resource and the structure [7] for the processing of the measurement outcomes.

![](images/2b328370fca61a992a49d484cb32d4f297f5939f110a2c75d3997622ed4635ee.jpg)

![](images/372d39cca903e3f83e3c1fd96b893d56b1311e41198a658e1f284dbf166c5884.jpg)  
FIG. 9. Simulation of the Hamiltonian  $H_{4}$  as specified in Eq. (115). (a) Measurement pattern. (b) Correlation centers for additional correlation. Shaded squares [in (b)] represent cluster qubits measured in adaptive bases.

# IV. EXAMPLES OF PRACTICAL INTEREST

# A. Simulating multiqubit Hamiltonians

Here we display a gate that simulates the unitary evolution with  $U = \exp (-iH_4t)$  of the quantum input for the multiparticle Hamiltonian

$$
H _ {4} = g \sigma_ {z} ^ {(1)} \sigma_ {z} ^ {(2)} \sigma_ {z} ^ {(3)} \sigma_ {z} ^ {(4)} \tag {115}
$$

and arbitrary times  $t$ . In addition, the gate performs a SWAP-gate, i.e., the order if the logical qubits is reversed.

The procedure to realize the measurement pattern  $\mathcal{M}$  for Hamiltonian simulation, as shown in Fig. 9, requires two rounds of measurements. In the first round all the  $\sigma_{x}$  measurements are performed. In the second measurement round, of the qubit (3,4) the operator

$$
\vec {r} _ {(3, 4)} \cdot \vec {\sigma} = U _ {z} [ (- 1) ^ {\lambda_ {M}} 2 \varphi ] \sigma_ {x} U _ {z} ^ {\dagger} [ (- 1) ^ {\lambda_ {M}} 2 \varphi ] \tag {116}
$$

is measured, where  $U_{z}[\alpha] = \exp(-i\alpha \sigma_{z}/2)$ . Therein, the angle  $\varphi$  is given by

$$
\varphi = g t, \tag {117}
$$

and  $\lambda_{M}\in \{0,1\}$ , which depends linearly on outcomes of measurements in the first round, will be specified below.

To understand the functioning of the Hamiltonian simulator, let us first discuss the state  $|\psi^{\prime}\rangle$  on the cluster  $\mathcal{C}(\mathrm{sim})$  after the first round of measurements. By the techniques for stabilizer manipulation described in Ref. [10], the state  $|\psi^{\prime}\rangle$  obeys the following eigenvalue equations:

$$
\sigma_ {x} ^ {(3, 4)} \sigma_ {x} ^ {(I, 1)} \sigma_ {x} ^ {(O, 4)} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {x, 1}} | \psi^ {\prime} \rangle ,
$$

$$
\sigma_ {x} ^ {(3, 4)} \sigma_ {x} ^ {(I, 2)} \sigma_ {x} ^ {(O, 3)} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {x, 2}} | \psi^ {\prime} \rangle ,
$$

$$
\sigma_ {x} ^ {(3, 4)} \sigma_ {x} ^ {(I, 3)} \sigma_ {x} ^ {(O, 2)} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {x, 3}} | \psi^ {\prime} \rangle ,
$$

$$
\sigma_ {x} ^ {(3, 4)} \sigma_ {x} ^ {(I, 4)} \sigma_ {x} ^ {(O, 1)} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {x, 4}} | \psi^ {\prime} \rangle , \tag {118}
$$

$$
\sigma_ {z} ^ {(I, 1)} \sigma_ {z} ^ {(O, 4)} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {z, 1}} | \psi^ {\prime} \rangle ,
$$

$$
\sigma_ {z} ^ {(I, 2)} \sigma_ {z} ^ {(O, 3)} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {z, 2}} | \psi^ {\prime} \rangle ,
$$

$$
\sigma_ {z} ^ {(I, 3)} \sigma_ {z} ^ {(O, 2)} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {z, 3}} | \psi^ {\prime} \rangle ,
$$

$$
\sigma_ {z} ^ {(I, 4)} \sigma_ {z} ^ {(O, 1)} | \psi^ {\prime} \rangle = (- 1) ^ {\lambda_ {z, 4}} | \psi^ {\prime} \rangle .
$$

Further, the state  $|\psi^{\prime}\rangle$  obeys the eigenvalue equation

$$
\left. \sigma_ {z} ^ {(3, 4)} \sigma_ {z} ^ {(O, 1)} \sigma_ {z} ^ {(O, 2)} \sigma_ {z} ^ {(O, 3)} \sigma_ {z} ^ {(O, 4)} \right| \psi^ {\prime} \rangle = (- 1) ^ {\lambda} | \psi^ {\prime} \rangle , \tag {119}
$$

with  $\lambda \in \{0,1\}$  linear in the measurement outcomes of the first round. Equation (119) can be easily verified with the pattern of correlation centers displayed in Fig. 9(b). From (119) it follows that

$$
\exp (i \theta \sigma_ {z} ^ {(3, 4)}) U _ {4} [ (- 1) ^ {\lambda} \theta ] | \psi^ {\prime} \rangle = | \psi^ {\prime} \rangle \tag {120}
$$

for arbitrary angles  $\theta$ , with

$$
U _ {4} [ \alpha ] = \exp (- i \alpha \sigma_ {z} ^ {(O, 1)} \sigma_ {z} ^ {(O, 2)} \sigma_ {z} ^ {(O, 3)} \sigma_ {z} ^ {(O, 4)}). \tag {121}
$$

Equation (120) is now inserted in both the lhs and the rhs of Eqs. (118). For example, with the first equation from Eq. (118), one obtains

$$
\begin{array}{l} (- 1) ^ {\lambda_ {x, 1}} \left| \psi^ {\prime} \right\rangle = \left(U _ {z} [ 2 \theta ] \sigma_ {x} U _ {z} ^ {\dagger} [ 2 \theta ]\right) ^ {(3, 4)} \sigma_ {x} ^ {(I, 1)} \\ \times (U _ {4} [ - (- 1) ^ {\lambda} \theta ] \sigma_ {x} ^ {[ 4 ]} \\ \times U _ {4} ^ {\dagger} [ - (- 1) ^ {\lambda} \theta ] ^ {(O)} | \psi^ {\prime} \rangle . \tag {122} \\ \end{array}
$$

In the second measurement round the qubit (3,4) is the only one left to be measured. As can be seen from Eq. (122), if the operator  $U_{z}[2\theta ]\sigma_{x}U_{z}^{\dagger}[2\theta ]$  of qubit (3,4) is measured, then

the state  $|\psi \rangle$ , into which the cluster qubits are projected after the second measurement round, obeys the eigenvalue equation

$$
\begin{array}{l} \left. (- 1) ^ {\lambda_ {x, 1} + s _ {(3, 4)}} \right| \psi \rangle = \sigma_ {x} ^ {(I, 1)} \left(U _ {4} [ - (- 1) ^ {\lambda} \theta ] \sigma_ {x} ^ {[ 4 ]} \right. \\ \times U _ {4} ^ {\dagger} [ - (- 1) ^ {\lambda} \theta ]) ^ {(O)} | \psi \rangle . \tag {123} \\ \end{array}
$$

If we carry out this procedure for all equations in Eq. (118), we find that the state  $|\psi \rangle$  that emerges after the second measurement round obeys the eigenvalue equations

$$
\begin{array}{l} \sigma_ {x} ^ {(I, i)} \left(U _ {4} U _ {\text {s w a p}} \sigma_ {x} ^ {[ i ]} U _ {\text {s w a p}} ^ {\dagger} U _ {4} ^ {\dagger}\right) ^ {(O)} | \psi \rangle = (- 1) ^ {\lambda_ {x, i} + s _ {(3, 4)}} | \psi \rangle , \tag {124} \\ \sigma_ {z} ^ {(I, i)} \left(U _ {4} U _ {\text {s w a p}} \sigma_ {z} ^ {[ i ]} U _ {\text {s w a p}} ^ {\dagger} U _ {4} ^ {\dagger}\right) ^ {(O)} | \psi \rangle = (- 1) ^ {\lambda_ {z, i}} | \psi \rangle , \\ \end{array}
$$

for  $i = 1,\ldots ,4$  and with  $U_{4}$  written in short for  $U_{4}[-(-1)^{\lambda}\theta ]$

With the set of Eqs. (124) assumptions (61) of Theorem 1 are fulfilled. With Theorem 1 it follows that the measurement pattern displayed in Fig. 9 realizes a unitary transformation

$$
U _ {\text {s i m}} = U _ {4} [ - (- 1) ^ {\lambda} \theta ] U _ {\text {s w a p}} U _ {\Sigma}, \tag {125}
$$

where the byproduct operator is given by

$$
U _ {\Sigma} = \bigotimes_ {i = 1} ^ {} 4 (\sigma_ {z} ^ {[ i ]}) ^ {s _ {(I, i)} + \lambda_ {x, i} + s _ {(3, 4)}} (\sigma_ {x} ^ {[ i ]}) ^ {\lambda_ {z, i}}. \tag {126}
$$

Finally, the order of the operators has to be exchanged. Note that  $U_{\mathrm{swap}}$  and  $U_4$  commute. From Eq. (125) one finds

$$
U _ {\text {s i m}} = U _ {\Sigma} ^ {\prime} U _ {\text {s w a p}} U _ {4} \left[ - (- 1) ^ {\lambda + \sum_ {i = 1} ^ {4} \lambda_ {z, i}} \theta \right], \tag {127}
$$

with

$$
U _ {\Sigma} ^ {\prime} = U _ {\text {s w a p}} U _ {\Sigma} U _ {\text {s w a p}} ^ {\dagger}. \tag {128}
$$

Thus, in order to realize  $U_4[\varphi]$  with  $\varphi$  specified in Eq. (117) we must choose

$$
\theta = (- 1) ^ {1 + \lambda + \sum_ {i = 1} ^ {4} \lambda z, i} \varphi . \tag {129}
$$

That is, in the second measurement round we measure on the qubit (3,4) the operator given in Eq. (116), where

$$
\lambda_ {M} = \left(1 + \lambda + \sum_ {i = 1} ^ {4} \lambda_ {z, i}\right) \bmod 2. \tag {130}
$$

$\{\lambda_{x,ij}\}$ ,  $\{\lambda_{z,ij}\}$ , and  $\lambda$  depend linearly on the measurement outcomes  $\{s_{(i,j)}\}$  obtained in the first measurement round.

The subcircuit we have described in this section simulates the unitary evolution according to a particular four-particle Hamiltonian in a two-step process of measurements. The time for which the simulated Hamiltonian acts is encoded in the basis of the measurement in the second round.

The generalization of the simulation of the four-particle Hamiltonian  $H_{4}$ , shown in Fig. 9, to an arbitrary number  $n$  of

![](images/de0f8a65bf2171bc8e5c04d5ed537819f2177bdd35d26c7a2a95a2486b2a55ae.jpg)  
FIG. 10. Measurement pattern that realizes the multiquubit SWAP gate.

qubits, i.e., the simulation of the Hamiltonian  $H_{n} = \otimes_{i=1}^{n} \sigma_{z}^{[i]}$ , is straightforward.

If the "interaction time" is set to zero,  $\varphi = 0$ , i.e., when the qubit (3,4) is measured in the  $\sigma_{x}$  eigenbasis as well, then one obtains a multiqubit SWAP gate, which reverses the order of the logical qubits. In this case, only a single measurement round is required. The multiqubit SWAP gate is displayed in Fig. 10.

# B. CNOT between non- neighboring qubits

The CNOT gate described in Sec. II G 7 operates on two logical qubits whose input qubits are adjacent to each other on the cluster. However, for universal quantum computation, one must be able to realize a CNOT gate between any two logical qubits. While this could be achieved using a combination of the CNOT gate, introduced above, and the SWAP gate, the width of the measurement pattern needed to realize this would grow linearly with the separation of the two logical qubits. There is, however, an alternative measurement pattern, which, at the cost of doubling the spacing between the input qubits on the cluster, has a fixed width.

The measurement pattern is illustrated in Fig. 11 for qubits separated by an odd and even number of logical qubits, respectively.

This layout can be understood within the quantum logic network model. The "wires" for the logical qubits in between the target and the control qubits are crossed, using the measurement subpattern, illustrated in Fig. 12(a). However, as well as swapping the qubits, this pattern also realizes a controlled  $\pi$ -phase gate, also known as a controlled  $\sigma_z$  gate, illustrated in Fig. 12(b).

The quantum logic circuit realized by the whole measurement pattern, illustrated on the left-hand side of Fig. 13 uses these subpatterns to swap the positions of adjacent qubits. This brings non- neighboring qubits together so that a CNOT operation may be performed on them.

![](images/a2b6aeabf572263723a301813710fc0f71a9b6a3f86e6a26c153e7576f89f3cf.jpg)  
(a)  
FIG. 11. Measurement pattern for a CNOT gate between two logical qubits whose input and output qubits are not neighbors. Squares in light gray denote cluster qubits measured in the eigenbasis of  $\sigma_{x}$ , in dark gray of  $\sigma_{y}$ . Pattern (a) is for the case where the two qubits are separated by an odd number of logical qubits. Pattern (b) is for an even-numbered separation. The patterns can be adapted to any separation by repeating the section enclosed by the dashed line. The width of the pattern remains the same for all separations.

![](images/55ff55ae477d5c91a884e5ed3524add845323a4d9c4af18cd159de3f04498c2a.jpg)  
(b)

The networks on the left and on the right of Fig. 13 act identically, and thus the measurement pattern displayed in Fig. 11 realizes a distant CNOT gate.

# C. Controlled phase gate

Here, we give an example of another two-qubit gate, which can be realized without decomposing it into CNOTs and rotations, the controlled phase gate  $U_{\mathrm{CPG}}(\theta)$ . This gate realizes the unitary operation

$$
U _ {\mathrm {C P G}} [ \theta ] = 1 ^ {(a b)} + (e ^ {i \theta} - 1) | 1 1 \rangle_ {a b} \langle 1 1 | \tag {131}
$$

applied to the two qubits  $a$  and  $b$ .

![](images/b0955e6dd17239479abd29de2b1c3757cc0043190671e73830caae6df4b06032.jpg)  
FIG. 12. This measurement pattern is one of the key components of the measurement pattern in Fig. 11. It performs a conditional  $\pi$ -phase gate and a SWAP gate.

![](images/196c7ece83d75fabccfbf317c94f2f8f69e7cf4c6115db9c8f7eab72e4b940b0.jpg)  
FIG. 13. The measurement pattern in Fig. 11 realizes the quantum logic circuit on the left-hand side of this figure. This network is equivalent to that on the right-hand side, where the only gate realized is the CNOT between the two desired nonadjacent qubits.

We can write this in terms of the following one- and two-qubit rotations:

$$
U _ {\mathrm {C P G}} [ \theta ] = e ^ {i (\theta / 4)} U _ {z z} ^ {(a b)} [ - \theta / 2 ] U _ {z} ^ {(a)} [ \theta / 2 ] U _ {z} ^ {(b)} [ \theta / 2 ], \tag {132}
$$

where the two-qubit rotation is

$$
U _ {z z} ^ {(a b)} [ \theta ] = \exp (- i \theta / 2 \sigma_ {z} ^ {(a)} \sigma_ {z} ^ {(b)}). \tag {133}
$$

This representation is particularly convenient for finding the measurement pattern that realizes the gate, since rotations  $U_{z}[\theta /2]$  and  $U_{zz}[-\theta /2]$  are realized on the  $\mathrm{QC}_{\mathcal{C}}$  in a simple natural way. The measurement pattern is illustrated in Fig. 14, in which the labelling of the qubits is also defined.

We follow the same method as above, beginning with the eigenvalue equations of the cluster state  $|\phi \rangle_{\mathcal{C}}$  on the qubits shown. The  $\sigma_{x}$  measurements can be considered first, using the methods already illustrated in this paper. The resultant state of the remaining qubits,  $|\psi^{\prime}\rangle$ , after this subset of the measurements has been carried out, is defined by the following set of eigenvalue equations:

$$
\sigma_ {x} ^ {(I, a)} \sigma_ {x} ^ {(1, 2)} \sigma_ {x} ^ {(2, 3)} \sigma_ {x} ^ {(O, b)} | \psi^ {\prime} \rangle = | \psi^ {\prime} \rangle , \tag {134a}
$$

$$
\left. \sigma_ {x} ^ {(I, b)} \sigma_ {x} ^ {(1, 2)} \sigma_ {x} ^ {(2, 1)} \sigma_ {x} ^ {(O, a)} \right| \psi^ {\prime} \rangle = | \psi^ {\prime} \rangle , \tag {134b}
$$

![](images/fe60ed83bfa3423662c2bc4337bb36f0ee75c2eb8ec82895efe04ebc8fbf1227.jpg)  
FIG. 14. Controlled phase gate with additional swap.

$$
\left. \sigma_ {z} ^ {(I, a)} \sigma_ {z} ^ {(O, b)} \right| \psi^ {\prime} \rangle = (- 1) ^ {s _ {(1, 1)} + s _ {(2, 2)} + s _ {(3, 3)}} \left| \psi^ {\prime} \right\rangle , \tag {134c}
$$

$$
\left. \sigma_ {z} ^ {(I, b)} \sigma_ {z} ^ {(O, a)} \right| \psi^ {\prime} \rangle = (- 1) ^ {s _ {(1, 3)} + s _ {(2, 2)} + s _ {(3, 1)}} \left| \psi^ {\prime} \right\rangle , \tag {134d}
$$

and

$$
\sigma_ {z} ^ {(2, 1)} \sigma_ {z} ^ {(O, a)} | \psi^ {\prime} \rangle = (- 1) ^ {s (3, 1)} | \psi^ {\prime} \rangle , \tag {135a}
$$

$$
\left. \sigma_ {z} ^ {(2, 3)} \sigma_ {z} ^ {(O, b)} \right| \psi^ {\prime} \rangle = (- 1) ^ {s (3, 3)} | \psi^ {\prime} \rangle , \tag {135b}
$$

$$
\left. \sigma_ {z} ^ {(1, 2)} \sigma_ {z} ^ {(O, a)} \sigma_ {z} ^ {(O, b)} \right| \psi^ {\prime} \rangle = (- 1) ^ {s _ {(3, 1)} + s _ {(2, 2)} + s _ {(3, 3)}} \left| \psi^ {\prime} \right\rangle . \tag {135c}
$$

As in Sec. II G 3, eigenvalue equations are now generated, which commute with the remaining measurements in  $\mathcal{M}$ , namely the measurements of  $\sigma_{xy}^{(i)}(\alpha_i)$  on qubits  $i \in \{(2,1),(1,2),(2,3)\}$ . First, we manipulate Eqs. (135) such that, for example, eigenvalue equation (135c) attains the form

$$
U _ {z} ^ {(1, 2)} [ \xi ] U _ {z z} ^ {\left((O, a), (O, b)\right)} [ - (- 1) ^ {s _ {(3, 1)} + s _ {(2, 2)} + s _ {(3, 3)}} \xi ] | \psi^ {\prime} \rangle = | \psi^ {\prime} \rangle . \tag {136}
$$

Similar equations containing one-qubit rotations on qubits (2,1) and  $(O,a)$ , and (2,3) and  $(O,b)$  are derived from the other equations of Eqs. (135) in the same way. These equations are inserted into both sides of eigenvalue equations (134) so that, using the method introduced above, we obtain a set of four eigenvalue equations for  $|\psi^{\prime}\rangle$ , which induce a set of four eigenvalue equations for the state  $|\psi\rangle$  that one obtains after the remaining measurements have been carried out.

Specifically, in the second measurement round the qubits (1,2), (2,1), and (2,3) are measured. Of these qubits one measures the observables

$$
\vec {r} _ {a} \cdot \vec {\sigma} ^ {(a)} = (U _ {z} [ \alpha_ {a} ] \sigma_ {x} U _ {z} [ \alpha_ {a} ] ^ {\dagger}) ^ {(a)}, \tag {137}
$$

for  $a \in \{(1,2),(2,1),(2,3)\}$  and  $\{\alpha_{a}\}$  specified below.

The induced eigenvalue equations for the state  $|\psi \rangle$  are of the form of Eq. (61), and the unitary operation realized by the gate can be read off from them, using Theorem 1. The full unitary operation realized by the measurement pattern is

$$
\begin{array}{l} U ^ {\prime} U _ {\Sigma} ^ {\prime} = U _ {z z} ^ {(a, b)} \left[ - (- 1) ^ {s _ {(3, 1)} + s _ {(2, 2)} + s _ {(3, 3)}} \alpha_ {(1, 2)} \right] \\ \times U _ {z} ^ {(a)} \left[ - (- 1) ^ {s (3, 1)} \alpha_ {(2, 1)} \right] U _ {z} ^ {(b)} \left[ - (- 1) ^ {s (3, 3)} \alpha_ {(2, 3)} \right] \\ \times U _ {\text {s w a p}} ^ {(a, b)} \left(\sigma_ {x} ^ {(a)}\right) ^ {s _ {(1, 1)} + s _ {(2, 2)} + s _ {(3, 3)}} \\ \times \left(\sigma_ {x} ^ {(b)}\right) ^ {s _ {(1, 3)} + s _ {(2, 2)} + s _ {(3, 1)}} \left(\sigma_ {z} ^ {(a)}\right) ^ {s _ {(I, a)} + s _ {(1, 2)} + s _ {(2, 3)}} \\ \times \left(\sigma_ {z} ^ {(b)}\right) ^ {s _ {(I, b)} + s _ {(2, 1)} + s _ {(1, 2)}}, \tag {138} \\ \end{array}
$$

such that after the order of the gate and the byproduct operator is reversed,  $U^{\prime}U_{\Sigma}^{\prime} = U_{\Sigma}U$ , one obtains

$$
\begin{array}{l} U _ {\Sigma} U = \left(\sigma_ {x} ^ {(a)}\right) ^ {s _ {(1, 3)} + s _ {(2, 2)} + s _ {(3, 1)}} \left(\sigma_ {x} ^ {(b)}\right) ^ {s _ {(1, 1)} + s _ {(2, 2)} + s _ {(3, 3)}} \\ \times \left(\sigma_ {z} ^ {(a)}\right) ^ {s _ {(2, 1)} + s _ {(1, 2)} + s _ {(I, b)}} \left(\sigma_ {z} ^ {(b)}\right) ^ {s _ {(I, a)} + s _ {(1, 2)} + s _ {(2, 3)}} \\ \times U _ {z z} ^ {(a, b)} \left[ - (- 1) ^ {s _ {(1, 1)} + s _ {(2, 2)} + s _ {(1, 3)}} \alpha_ {(1, 2)} \right] \\ \end{array}
$$

![](images/2ad7a09d786aa5dc0fb79ad6404787a5865162540f6b909fac29320197eb69ed.jpg)

![](images/cb1dd26c7ec4317ab20f425b8f37071e52ae5ee70b0389fec3415194d6f19625.jpg)  
FIG. 15. Quantum Fourier transformation. (a) Network for quantum Fourier transformation on four qubits, taken from Ref. [25]. (b) Component of the network shown in (a), which performs a conditional phase and a SWAP gate. Specifically, the gate shown is  $U_{CPG}[2\pi /2^m]$ , i.e.,  $U_{m} = |0\rangle \langle 0| + e^{i2\pi /2^m}|1\rangle \langle 1|$ .

$$
\begin{array}{l} \times U _ {z} ^ {(a)} \left[ - (- 1) ^ {s _ {(2, 2)} + s _ {(1, 3)}} \alpha_ {(2, 1)} \right] \\ \times U _ {z} ^ {(b)} \left[ - (- 1) ^ {s _ {(1, 1)} + s _ {(2, 2)}} \alpha_ {(2, 3)} \right] U _ {\text {S W A P}} ^ {(a, b)}. \tag {139} \\ \end{array}
$$

Using Eq. (139) one finds the following result: To realize the controlled phase gate (131) together with a SWAP gate, observables (137) measured in the second round have to be chosen with the angles  $\alpha_{(2,1)} = (-1)^{1 + s_{(2,2)} + s_{(1,3)}}\theta /2$ ,  $\alpha_{(1,2)} = (-1)^{s_{(1,1)} + s_{(2,2)} + s_{(1,3)}}\theta /2$  and  $\alpha_{(2,3)} = (-1)^{s_{(1,1)} + s_{(2,2)} + 1}\theta /2$ . This realizes the gate  $U_{\Sigma}U_{CPG}[\theta]$ , where the byproduct operator  $U_{\Sigma}$  generated by the measurements may be read off from Eq. (139).

# D. Quantum Fourier transformation

To realize the quantum Fourier transform we simulate the quantum logic network given in Fig. 15(a). The arrangement of the gates in this network is taken from Ref. [25]. Note that in Ref. [25] it was demonstrated that the setup to perform a quantum Fourier transformation simplifies considerably in a situation where the output state is measured right after the transformation. Here, however, the quantum Fourier transformation may constitute part of a larger quantum circuit and we do not measure its output state.

As can be seen from Fig. 15, the quantum Fourier transform consists of the Hadamard gates and combined gates that perform a conditional phase shift and a swap. These gates have been discussed in Secs. II B and IV C. All that remains to do is to put the measurement patterns simulating these gates together, using the networklike composition principle described in Sec. II D.

In this way we obtain a measurement pattern in which there are adjacent cluster qubits in "wires" that are measured in the  $\sigma_{x}$  eigenbasis. As described in Sec. II G 2, such pairs of cluster qubits may be removed from the measurement pattern. Note that by removing adjacent pairs of  $\sigma_{x}$ -measured cluster qubits, we have moved the  $\sigma_{y}$  measurements of the Hadamard transformations "into" the subsequent conditional phase gates, i.e., we removed a cluster qubit that was not from a wire. It can be easily verified that this is an allowed

![](images/e71b13e0c4b678a3ba8445f7f4504382425bb44693b6b3c4bf2c4ff1ac4ca144.jpg)  
FIG. 16.  $\mathrm{QC}_{\mathcal{C}}$  realization of a quantum Fourier transformation on four qubits. The cluster qubits displayed as framed squares are measured in adapted bases. For the labels see text.

extension of the method described in Sec. II G 2. Finally, one obtains the  $\mathrm{QC}_{\mathcal{C}}$  circuit displayed in Fig. 16.

In this circuit, as in all the others, the adaptive measurements are of observables

$$
U _ {z} [ \pm \eta ] \sigma_ {x} U _ {z} [ \pm \eta ] ^ {\dagger}, \tag {140}
$$

with  $\eta = \pi /4$  for cluster qubits marked with "2" in Fig. 16,  $\eta = \pi /8$  for qubits marked with "3," and  $\eta = \pi /16$  for the qubits marked with "4." The sign factors of the angles in Eq. (140) depend on the results of previous measurements.

The  $\mathrm{QC}_{\mathcal{C}}$  circuit, shown in Fig. 16 for the case of four qubits, is straightforwardly generalized to an arbitrary number  $n$  of logical qubits. The temporal spatial and operational resources  $T$ ,  $S$ , and  $O$  are, to leading order

$$
T = n, \quad S, O = 2 n ^ {2}. \tag {141}
$$

The corresponding network resources are  $T_{\mathrm{qln}} = 2n$ ,  $S_{\mathrm{qln}} = n$ , and  $O_{\mathrm{qln}} = n^2 / 2$ . Thus, the scaling of the QC<sub>c</sub> spatial resources is worse than in the network model, but the temporal and operational resources scale in the same way as the corresponding resources for the network. The QC<sub>c</sub> simulation of the network displayed in Fig. 15 requires half as many time steps and four times as many operations, albeit only one-qubit operations.

# E. Multiqubit controlled gates

In this section we describe the realization of the Toffoli phase gate and the three-qubit controlled gate CARRY, which we will both need for the construction of the  $\mathrm{QC}_{\mathcal{C}}$  -adder circuit described in Sec. IV F.

![](images/e29299ac7ac56a05ca26cfe011c516dde40c2c052edd164f45328465a67347ec.jpg)  
FIG. 17. A measurement layout to realize a Toffoli phase gate with phase  $\phi$ . The qubits marked by black boxes are simultaneously measured in adapted bases, depending on previous measurement outcomes.

![](images/cce123ca6edd1174431c1f7e70aeaf73ed287def7c541cd6259161e842b981dd.jpg)  
FIG. 18. Cluster state quantum correlations for the realization of  $U_{zz}^{(c_1,c_2)}[\phi /4]$ , used in the Toffoli phase gate.

The Toffoli phase gate is a three-qubit generalization of the two-qubit controlled phase gate. If all three qubits are in the state  $|1\rangle$ , the state gains a phase of  $\exp (i\phi)$ , while all other logical basis states remain unchanged by the gate:

$$
U _ {\text {T o f f o l i}} ^ {(c _ {1}, c _ {2}, t)} [ \phi ] = \left. \right\lceil^ {(c _ {1}, c _ {2}, t)} + (e ^ {i \phi} - 1) \left| 1 1 1 \right\rangle_ {c _ {1}, c _ {2}, t} \langle 1 1 1 |. \tag {142}
$$

Like the controlled phase gate it can be represented as a product of multiquubit rotations,

$$
\begin{array}{l} U _ {\text {T o f f o l i}} ^ {(c _ {1}, c _ {2}, t)} [ \phi ] = U _ {z z z} ^ {(c _ {1}, c _ {2}, t)} \left[ \frac {\phi}{4} \right] U _ {z z} ^ {(c _ {1}, c _ {2})} \left[ - \frac {\phi}{4} \right] U _ {z z} ^ {(c _ {1}, t)} \left[ - \frac {\phi}{4} \right] \\ \times U _ {z z} ^ {(c _ {2}, t)} \left[ - \frac {\phi}{4} \right] U _ {z} ^ {(c _ {1})} \left[ \frac {\phi}{4} \right] U _ {z} ^ {(c _ {2})} \left[ \frac {\phi}{4} \right] U _ {z} ^ {(t)} \left[ \frac {\phi}{4} \right], \tag {143} \\ \end{array}
$$

where we have dropped the global phase, and  $U_{zz}^{(c_1,c_2,t)}[\alpha] = \exp(-i\alpha / 2\sigma_z^{(c_1)}\sigma_z^{(c_2)}\sigma_z^{(t)})$  is a three-qubit generalized rotation. The two-qubit rotations  $U_{zz}$  are as defined in Eq. (133).

The way to convert sequence (143) of generalized rotations into a measurement pattern is as in the examples be

![](images/a713607fd21e4230afb0ef403a786eb57b6c501cbae8c5c19f538315f96e0965.jpg)  
FIG. 19. The three-qubit controlled gate. Qubits displayed as squares in light gray are measured in the  $\sigma_{x}$  eigenbasis, the qubit displayed in dark gray is measured in the  $\sigma_{y}$  eigenbasis, and the measurement bases of the qubits displayed as framed squares are adaptive.

fore. The measurement layout for the Toffoli phase gate is illustrated in Fig. 17. Each of the generalized rotations that make up the gate is directly associated with one of the measurements made in the eigenbasis of  $U_z[\pm \phi /4]\sigma_xU_z[\pm \phi /4]^{\dagger}$ . An initial cluster-state correlation, which is used for the realization of a generalized rotation, is shown in Fig. 18; the rotation  $U_{zz}^{(c_1,c_2)}[\phi /4]$  is realized via the measurement of the cluster qubit at the lattice site (3,1) in the appropriate basis.

The sign factors of the angles that specify the measurement bases depend on the outcome of  $\sigma_{x}$  measurements only. Thus, after all  $\sigma_{x}$  measurements have been performed, the measurement bases for the remaining qubits can be deduced and the Toffoli phase gate is realized in a single further time step. The measurement pattern realizes the generalized rota

tions directly and is not derived from a quantum logic network.

Now we describe the realization of a four-qubit gate CARRY, which has one target and three control qubits. It performs a phase-flip  $\sigma_z$  on the target if at least two of the control qubits are in state  $|1\rangle$  and otherwise does nothing, i.e.,

$$
U _ {\text {C A R R Y}} = \exp \left(- i \pi \sum_ {i = 0 0 0 _ {d} | w (i) \geqslant 2} ^ {1 1 1 _ {d}} | i \rangle_ {c _ {1} c _ {2} c _ {3}} \langle i | \otimes | 1 \rangle_ {t} \langle 1 |\right), \tag {144}
$$

Expanding the projectors on the control qubits into products of the Pauli operators one obtains

$$
\begin{array}{l} U _ {\mathrm {C A R R Y}} = e ^ {- i (\pi / 4)} \underbrace {\exp \left(- i \frac {\pi}{8} \sigma_ {z} ^ {(t)} \sigma_ {z} ^ {(c _ {3})}\right)} _ {U _ {i}} \underbrace {\exp \left(- i \frac {\pi}{8} \sigma_ {z} ^ {(t)} \sigma_ {z} ^ {(c _ {2})}\right)} _ {U _ {h}} \underbrace {\exp \left(i \frac {\pi}{8} \sigma_ {z} ^ {(c _ {3})}\right)} _ {U _ {g}} \underbrace {\exp \left(i \frac {\pi}{8} \sigma_ {z} ^ {(c _ {2})}\right)} _ {U _ {f}} \underbrace {\exp \left(i \frac {\pi}{8} \sigma_ {z} ^ {(c _ {1})}\right)} _ {U _ {e}} \\ \times \underbrace {\exp \left(i \frac {\pi}{4} \sigma_ {z} ^ {(t)}\right)} _ {U _ {d}} \underbrace {\exp \left(- i \frac {\pi}{8} \sigma_ {z} ^ {(t)} \sigma_ {z} ^ {(c _ {1})}\right)} _ {U _ {c}} \underbrace {\exp \left(- i \frac {\pi}{8} \sigma_ {z} ^ {(c _ {1})} \sigma_ {z} ^ {(c _ {2})} \sigma_ {z} ^ {(c _ {3})}\right)} _ {U _ {b}} \underbrace {\exp \left(i \frac {\pi}{8} \sigma_ {z} ^ {(t)} \sigma_ {z} ^ {(c _ {1})} \sigma_ {z} ^ {(c _ {2})} \sigma_ {z} ^ {(c _ {3})}\right)} _ {U _ {a}}. \tag {145} \\ \end{array}
$$

The global phase is henceforth discarded.

The unitary transformation is now subdivided into two parts:

$$
U _ {\text {C A R R Y}} = U _ {h, i} U _ {a - g}, \tag {146}
$$

with  $U_{a - g} = U_gU_fU_eU_dU_cU_bU_a$  and  $U_{h,i} = U_iU_h$ . Correspondingly, the cluster on which  $U_{\mathrm{CARRY}}$  is realized is divided into two subclusters. On the first subcluster the transformations  $U_{a}$  to  $U_{g}$  are realized, on the second subcluster  $U_{h,i}$ . The measurement pattern to realize  $U_{\mathrm{CARRY}}$  is displayed in Fig. 19. The first subcluster stretches from  $x = 0$  to  $x = 8$ , with the input at  $x = 0$  and the intermediate output at  $x = 8$ . The qubits with  $8 \leqslant x \leqslant 16$  belong to the second subcluster.

Let us now explain the subgate  $U_{a - g}$ . The conversion of sequence (145) of generalized rotations is as in the previous examples. For each generalized rotation there is one cluster qubit in  $C_M(U_{a - g})$  whose measurement basis specifies the respective rotation angle. Specifically, the measurement of the cluster qubit (3,4) sets the rotation angle of  $U_{a}$ , the measurement of qubit (4,3) sets the angle for  $U_{b}$ , (5,6) sets  $U_{c}$ , (6,7) sets  $U_{d}$ , (6,5) sets  $U_{e}$ , (6,3) sets  $U_{f}$ , and qubit (6,1) sets  $U_{g}$ . The quantum correlations of the initial cluster state, which induce via the measurements of the cluster qubits in  $C_M(U_{a - g})$  the quantum correlations associated with the generalized rotations are displayed in Fig. 20.

The realization of the gate requires two measurement rounds. In the first round the standard measurements of  $\sigma_{x}$  and  $\sigma_{y}$  are performed. Note that the rotation angle of  $U_{d}$  is twice as big as for the other rotations. To realize  $U_{d}$  of the cluster qubit (6,7) the observable

$$
U _ {z} \left[ \pm \frac {\pi}{2} \right] \sigma_ {x} U _ {z} \left[ \mp \frac {\pi}{2} \right] = \pm \sigma_ {y} \tag {147}
$$

is measured. Thus, the realization of  $U_{d}$  belongs to the first round of measurements. Strictly speaking, this measurement round does not belong to the gate but to the circuit as a whole since all standard measurements are performed simultaneously.

In the second measurement round, of the remaining qubits in  $\mathcal{C}_M(U_{a - g})$  one measures the observables

$$
U _ {z} \left[ \pm \frac {\pi}{4} \right] \sigma_ {x} U _ {z} \left[ \mp \frac {\pi}{4} \right]. \tag {148}
$$

The procedure to infer the sign factors in Eqs. (148) and (147) is explained in Sec. II F.

The reason why the measurements in the tilted bases may all be performed simultaneously in the second round can be seen as follows. Let  $Q_{\nearrow}$  be the set of qubits measured in tilted bases. The contribution  $U_{\Sigma, Q_{\nearrow}}$  of the cluster qubits

![](images/c027e1b7312af3a92024b850d2bcfb800e0bacffeffced5c86f1604c92e9d016.jpg)

![](images/d4891be9357d8ca9901daca1a9e9a919046a31e8f5bfb8d9d77c355880c55e02.jpg)

![](images/05040adbfcef939cb00ddefc6e641681d67808fa63e9cb01c3e6e64a24c230aa.jpg)  
FIG. 20. Quantum correlations of the initial cluster state  $|\phi \rangle_{\mathcal{C}(U_{a - g})}$  on the cluster  $\mathcal{C}(U_{a - g})$ . These correlations induce, via the  $\sigma_x$  measurements, the quantum correlations for the state  $|\psi^{\prime}\rangle$ , which act only on the output qubits and one cluster qubit in  $\mathcal{C}_M(U_{a - g})$ . The pattern of correlation centers in (a) displays the correlation required to realize  $U_{a}$ ; (b), (c), and (d) display the correlations for  $U_{b}$ ,  $U_{c}$ , and  $U_{e}$ , respectively. The correlations used for the realization of  $U_{d}$ ,  $U_{f}$ , and  $U_{g}$  are not shown. They are analogous to that in (d) used for the realization of  $U_{e}$ .

![](images/c866dd6291c200d1e1823b4908ed0a0def9233436b4e1dd6cf9f63662753933e.jpg)

measured in tilted bases to the byproduct operator  $U_{\Sigma}$  in Eq. (63) contains only a  $z$  part but no  $x$  part. That is, it has the form

$$
U _ {\Sigma , Q _ {\nearrow}} = \bigotimes_ {i \in I \subset \{t, c _ {1}, c _ {2}, c _ {3} \}} \sigma_ {z} ^ {[ i ]}. \tag {149}
$$

In Eq. (62) the byproduct operator appears "on the wrong side" of  $U_{a - g}$  as does the contribution  $U_{\Sigma, Q_{\nearrow}}$ . When the

order of the gate and the byproduct operator is exchanged, the byproduct operator may modify the gate. While this is, not surprisingly, indeed the case for the whole  $U_{\Sigma}$ , it is not so for the contribution  $U_{\Sigma, Q_{\nearrow}}$  coming from the measurements in the tilted bases. Because  $U_{\Sigma, Q_{\nearrow}}$  has only a  $z$  part, it commutes with  $U_{a - g}$ . Therefore, the results of measurements in a tilted basis do not mutually affect the choice of their measurement bases.

![](images/904dd80eaf03470e9f8fe58125245436a17483de5b31789c4d315ad7ea865d83.jpg)  
FIG. 21. Quantum correlations of the initial cluster states on  $\mathcal{C}(U_h)$  and  $\mathcal{C}(U_i)$ . These correlations induce, via the  $\sigma_x$  measurements, the quantum correlations for the states  $|\psi^{\prime}\rangle_{\mathcal{C}(U_h)}$  and  $|\psi^{\prime}\rangle_{\mathcal{C}(U_i)}$  that involve only the respective output qubits and one qubit in the gate body. The pattern of correlation centers in (a) displays the correlation required to realize  $U_h$  and (b) the correlation for  $U_i$ .

![](images/9b486af879adf78a9ff6495e2106a453940738ce4ca633cba1ee311a35a20abd.jpg)

![](images/3593919465d6f4141ae4caf32a41cf90bc0a2737fce3ff664ec466a35082bcdd.jpg)  
FIG. 22. In the three-qubit controlled gate CARRY, the target qubit may travel either back or forth.

The fact that the byproduct operator  $U_{\Sigma, Q}$  is indeed of form (149), we do not show here explicitly. For the byproduct operator created in the measurement of qubit (3,4), realizing the transformation  $U_{a}$  it may be verified from Eq. (126) in Sec. IV A.

The explanation of the second subgate  $U_{h,i}$  is analogous. Figure 21 displays the quantum correlations of the initial cluster state, which, via the measurements in  $\mathcal{C}_M(U_{h,i})$ , induce the required quantum correlations associated with  $U_{h}$  and  $U_{i}$ .

Two further points we would like to address in this section. The first is to note that the whole gate  $U_{\mathrm{CARRY}}$  can be performed on the  $\mathrm{QC}_{\mathcal{C}}$  in two measurement rounds. The first measurement round is that of the  $\sigma_x$ ,  $\sigma_y$ , and  $\sigma_z$  measurements, which, strictly speaking, does not belong to the gate but to the circuit as a whole. The second measurement round is that of the simultaneous measurements in tilted measurement bases.

We have already seen that the measurements that realize the unitary transformations  $U_{a}, \ldots, U_{g}$  may be realized simultaneously, and this argument may be extended to the entire gate  $U_{\mathrm{CARRY}}$ . All the byproduct operators created with the measurements in tilted bases have only a  $z$  but no  $x$  part. Therefore, they all commute with  $U_{\mathrm{CARRY}}$ . Thus, to choose the right measurement bases neither of the measurements in a tilted basis that realizes one of the rotations  $U_{a}, \ldots, U_{i}$  needs to wait for another measurement in a tilted basis.

Second, note that for  $U_{\mathrm{CARRY}}$  the target input and the target output can be interchanged, see Fig. 22. This holds

because the (conditional) phase flip on the target qubit is its own inverse. Thus, the target qubit may travel through the gate backwards. This property also holds for the Toffoli phase gate. We will make use of it in the construction of the quantum adder in the following section.

# F. Circuit for addition

The  $\mathrm{QC}_{\mathcal{C}}$  version of the quantum adder corresponds to the quantum logic network as given in Ref. [26], see Fig. 23. In this paper we use the three-qubit controlled phase gate CARRY together with a prior and subsequent Hadamard gate on the target qubit while in Ref. [26] the equivalent three-qubit controlled spin-flip gate is used directly.

At first sight it appears as if the horizontal dimension of the cluster to realize the adder circuit would grow linearly with the number of logical qubits  $n$ . This is, however, not the case. The  $\mathrm{QC}_{\mathcal{C}}$  circuit may be formed in such a way that the horizontal size of the required cluster is constant such that the cluster size increases only linearly with the number  $n$  of logical qubits. To see what the  $\mathrm{QC}_{\mathcal{C}}$  realization of the quantum adder will look like, the network displayed in Fig. 23 may be bent in a way displayed in Fig. 24.

To "bend a network" is a rather informal notion. We therefore now specify what we mean by this. If a quantum circuit is displayed as a quantum logic network, the vertical axis usually denotes some spatial dimension, i.e., the location of the qubit carriers, and the horizontal axis corresponds to the sequence of steps of a quantum computation, i.e., a logical time. As the basic blocks of quantum computation in the network model, the universal gates, are unitary transformations generated by suitably chosen Hamiltonians, the logical time becomes associated with physical time. This is, however, a peculiarity of the network model. If on the  $\mathrm{QC}_{\mathcal{C}}$  a quantum logic network is simulated, the temporal axis is converted into an additional spatial axis. The temporal axis in a  $\mathrm{QC}_{\mathcal{C}}$  computation emerges anew. It has no counterpart in the network model. If we modify a quantum logic network in such a way that qubits travel from right to left, as done in Fig. 24, it does not mean that we propose to use particles that

![](images/148c5587be23af2cc7659b2fc7f742c6f3e5b9d383fdcd0bfa9318925475d221.jpg)  
FIG. 23. Quantum logic network for four-qubit adder,  $c = a + b \mod 2^4$ . The adder network is taken from Ref. [26]. The two-qubit controlled gate in this network is the Tofolli phase gate, as discussed in Sec. IV E. A straightforward simulation of this network on the  $\mathrm{QC}_C$  would result in a quadratic scaling of spatial resources. However, the more compact realization discussed below requires only a linear overhead.

![](images/945ff58dd5882ba1ad36f37e7a696920df6255214518fe7086fb6be6e75f40f7.jpg)  
FIG. 24. Quantum logic network for four-qubit adder, bent.

travel backwards in time because we do not need to respect the temporal axis implied by the network model. If one wants a seminetwork picture that accounts for this, one may imagine the logical qubits as traveling through pipes on a two-dimensional surface.

The reason why we may let the auxiliary qubits travel "backwards" is the identity displayed in Fig. 22. This arrangement of gates makes the circuit more compact. To complete the description of components from which the  $\mathrm{QC}_{\mathcal{C}}$  version of the quantum adder is built, a compact measurement pattern for the two combined CNOT gates is displayed in Fig. 25.

The realization of the quantum adder in the network layout of Fig. 24 directly leads to the  $\mathrm{QC}_{\mathcal{C}}$  circuit for the quantum adder displayed in Fig. 26. Note that the displayed  $\mathrm{QC}_{\mathcal{C}}$  adder is for eight qubits, while the networks in Figs. 23 and 24 are only for four qubits.

![](images/0ef6c10bb0b6709d4a948133ba0064d41552338064a0427be49e04d9bc128b72.jpg)  
a)

![](images/31fed143c8d545058733c1522669f08e594b166185fa14a7945b9c0bb78efc10.jpg)  
FIG. 25. Combination of two CNOT gates (a) and its  $\mathrm{QC}_{\mathcal{C}}$  realization (b).  
b)

![](images/32a424385d35111c17f431dadf8426b0468887bed4c23ab77a9cd6082f41d8cb.jpg)  
FIG. 26. Quantum adding circuit for two eight-qubit states. As in all figures displaying  $\mathrm{QC}_{\mathcal{C}}$  circuits, squares in light and dark gray represent cluster qubits measured in the  $\sigma_{x}$  and  $\sigma_{y}$  eigenbasis, respectively. The measurement bases of qubits displayed as framed squares are adaptive.

For the quantum adder circuit in Fig. 26 we have made two further minor simplifications. The first concerns the ancilla preparation. To prepare an ancilla qubit on the cluster in the state  $| + \rangle$  means to measure the respective cluster qubit in the  $\sigma_{x}$  eigenbasis (the randomness of the measurement outcome does not jeopardize the deterministic character of the circuit). As can be seen from the Toffoli gate and the three-qubit controlled gate, displayed in Figs. 17 and 19, the ancilla qubits are located on cluster qubits that have only one next neighbor. As can be verified from eigenvalue equations (1), to measure a qubit of a cluster state that only has one next neighbor in the eigenbasis of  $\sigma_{x}$  also has the effect of projecting this neighboring cluster qubit into an eigenstate of  $\sigma_{z}$ . Such cluster qubits may be removed from the cluster as explained in Sec. II C. With these neighboring qubits removed, the cluster qubits on which the initial ancilla qubits were located become disconnected from the remaining cluster and may thus be removed as well. With the same argument, the cluster qubits carrying the ancillas in their output state, and their next neighbors may also be removed.

Second, between the  $\mathrm{QC}_{\mathcal{C}}$  realization of the CARRY gates on the left and the subsequent blocks of CNOT gates we have

removed pairs of adjacent cluster qubits that would be measured in the eigenbasis of  $\sigma_{x}$ . Why this can be done has been explained for adjacent qubits in wires in Sec. II G 2. Here the situation is little more involved since, like in the case of the circuit for the Fourier transformation displayed in Sec. IV D, one of the removed qubits in each pair has more than two neighbors. But the method still works as can be easily verified.

Let us now briefly discuss the resources required for the  $\mathrm{QC}_{\mathcal{C}}$  realization of an  $n$ -qubit adder. As can be seen directly from the circuit displayed in Fig. 26 and the underlying network shown in Fig. 24 with its repeating sub-structure, the adder requires a cluster of height  $8n - 5$  and of constant width 38. Thus, the spatial and operational resources are, to leading order,

$$
S = O = 3 0 4 n. \tag {150}
$$

Concerning the temporal resources note that each pair of three-qubit controlled phase gates using the same control qubits and the pair of the Toffoli phase gates may be completed at one time instant but that one pair of gates is completed after another. The reason why the measurements in the tilted bases that complete each pair of gates may be performed simultaneously is the same as that given previously for the measurements in tilted bases of a single three-qubit controlled gate. The propagation of byproduct operators is most easily followed in the network of Fig. 23. The temporal complexity  $T$  of an  $n$ -qubit  $\mathrm{QC}_{\mathcal{C}}$  adder is

$$
T = n, \tag {151}
$$

plus one step of  $\sigma_x$ ,  $\sigma_y$ , and  $\sigma_z$  measurements for the entire circuit.

The corresponding network resources are, to leading order,  $S_{\mathrm{qln}} = 3n$  and  $O_{\mathrm{qln}} = T_{\mathrm{qln}} = 8n$ . For the counting of the operational and temporal network resources, we have assumed that the three-qubit controlled spin-flip gate used in the addition circuit is composed of two Toffoli gates and one CNOT gate, as described in Ref. [26], and that the CNOT and the Toffoli gates are regarded as elementary.

Thus, we find for both the network and the  $\mathrm{QC}_{\mathcal{C}}$  realization of the quantum adder that the spatial, temporal, and operational resources scale linearly with  $n$ . Therefore, the resource overheads in one realization as compared to the other one are only constants. For the  $\mathrm{QC}_{\mathcal{C}}$  this is much better than what is indicated by bounds (111)-(113), in particular, for the spatial and operational resources. Equation (112) yields an upper bound on  $S$ , which is  $\sim n^3$ , and Eq. (113) gives bounds on  $O$  and  $S$ , which are  $\sim n^2$ . Thus, the quantum adder is an example for which these bounds are very loose. In general, they should not be mistaken as estimates.

If the prefactors are compared, one finds that for the realization of a quantum adder the  $\mathrm{QC}_{\mathcal{C}}$  requires about 100 times more spatial and 38 times more operational resources, while it is eight times faster. However, since we compare different objects, these ratios do not mean much apart from the fact that they are constants. It may be argued that in the case of the  $\mathrm{QC}_{\mathcal{C}}$  spatial resources are not as precious as they usually are, to create cluster states one needs a system with nonse

lective uniform interaction only while for quantum logic networks one generally requires a system with selective interactions among the qubits. Concerning the operational and temporal resources, the  $\mathrm{QC}_{\mathcal{C}}$  only uses one-qubit measurements, while the corresponding network uses two- and three-qubit gates as elementary operations.

# G. Remarks

We would like to add two remarks, one with regard to the elementary constituents of the  $\mathrm{QC}_{\mathcal{C}}$  and the other with regard to their composition principle.

For the particular set of gate simulations used in the  $\mathrm{QC}_{\mathcal{C}}$  universality proof in Sec. II, the CNOT gate and arbitrary one-qubit rotations, there is only a single instance where one of these gates has been used as part of a more complicated gate in all examples of this section. Namely, the next-neighbor CNOT gate has been used as part of the long-distance CNOT, described in Sec. IV B. Of universal gate simulations one might expect that any circuit is composed of them rather than they occur almost not at all. One could say, though, that the used set of gates is not a good choice for the universal set. In fact, in realizations of network quantum computers it is often the physics of the specific implementation that determines which gates are elementary. For the  $\mathrm{QC}_{\mathcal{C}}$  this is not so. The  $\mathrm{QC}_{\mathcal{C}}$  may simulate, for example, general one-qubit rotations and the Toffoli gates alike. Any gate simulation may be called "elementary" with the same right as any other, but they cannot be all elementary. The elementary constituents of the  $\mathrm{QC}_{\mathcal{C}}$  are not gate simulations.

As a consequence, the composition principle for these elements will be different from gate composition. At first sight, if we go through the examples of this section, we find that this is not yet reflected in the larger and more complicated constructions. For the quantum Fourier transform and the addition circuit we have, though playing with some tricks, ultimately imitated network composition.

However, in the smaller gates and subcircuits, such as the controlled phase gate, the Toffoli phase gate and the gate CARRY we find something that might give rise to a more appropriate composition principle. First, for the  $\mathrm{QC}_{\mathcal{C}}$  it is not the one-qubit and two-qubit operations that are particularly simple. In the Hamiltonian simulation circuit of Sec. IV A we found that it is easy to realize generalized rotations  $\exp (i\varphi \sigma^{(J)})$  where  $\sigma^{(J)}$  is a composite Pauli operator,  $\sigma^{(J)} = \otimes_{a\in J}\sigma_{k_a}^{(a)}$ ,  $k_{a} = x,y,z$ . Furthermore, in the subsequent examples of the multiqubit gates in Secs. IV C and IV E we have decomposed the gates into such generalized rotations rather than into known standard gates on fewer qubits.

Any unitary transformation may be decomposed into a unitary transformation in the Clifford group followed by generalized rotations. So, is this a new composition principle? With our present state of knowledge, the answer must be "Not yet." First, though any transformation may be rewritten in this form, it is presently not clear how to design quantum algorithms with these elements directly. Second, the construction uses the very concept of applying unitary transformations to the state of a quantum register. However, as we have explained in Ref. [7] and also briefly sketched in Sec.

III A, the  $\mathrm{QC}_{\mathcal{C}}$  has no quantum register. So, the generalized rotations and their concatenation at least have to be reformulated to fit the description of the  $\mathrm{QC}_{\mathcal{C}}$ . In particular, they have to be made compatible with the graph states identified in Sec. III B as characteristic quantum resource to represent algorithms. Nevertheless, it appears that the generalized rotations should be reflected in what may emerge as elementary constituents and composition principle for the  $\mathrm{QC}_{\mathcal{C}}$ .

# V. COMPUTATION WITH LIMITED SPATIAL RESOURCES AND IN THE PRESENCE OF DECOHERENCE

In this section we describe how to perform  $\mathrm{QC}_{\mathcal{C}}$  computation on finite and possibly small clusters. If the cluster that may be provided by a specific device is too small for a certain measurement pattern, it does not mean that the respective  $\mathrm{QC}_{\mathcal{C}}$  algorithm cannot be run on this device. Instead, the  $\mathrm{QC}_{\mathcal{C}}$  computation may be split into several parts such that each of those parts fits on the cluster.

To see this, consider Scheme 1 for the realization of gates. Scheme 1 is applicable to any gate or subcircuit. It is thus possible to divide the circuit into subcircuits, each of which fits onto the cluster. The adapted scheme is a process of repetitive reentangling steps alternating with rounds of measurements.

Specifically, one starts with the realization of the first subcircuit acting on the fiducial input state located at  $I_{1} \subset \mathcal{C}$ . The fiducial input is, while being processed, teleported to some subset  $O_{1}$  of the cluster  $\mathcal{C}$ . The set  $O_{1}$  of qubits forms the intermediate output of the first subcircuit. These qubits remain unmeasured, while all the other qubits are measured to realize the first subcircuit. Now the realization of the second subcircuit begins. Its input state has already been prepared,  $I_{2} = O_{1}$ . The cluster qubits  $a \in \mathcal{C} \setminus O_{1}$ , which have been measured in the realization of the first subcircuit, are now prepared individually in the state  $| + \rangle_{a}$ . This completes Step 1 of Scheme 1 to realize the second subcircuit. Step 2 is to entangle the whole cluster via the Ising interaction. In the third step all cluster qubits except those of the intermediate output  $O_{2}$  are measured whereby the realization of the second subcircuit is completed. The intermediate output is now located at  $O_{2}$ . For the realization of the subsequent subcircuits one proceeds accordingly.

An advantage of this modified procedure is that one gets with smaller clusters. A disadvantage is that the Clifford part of the circuit may no longer be performed in a single time step.

Perhaps the most important advantage of the above con

striction is that in this way a basic requirement to make the  $\mathrm{QC}_{\mathcal{C}}$  fault tolerant can be fulfilled. Namely, decoherence can be controlled. If a single large cluster is used, the computation might reach certain cluster qubits only after a long time such that the cluster would have already decohered significantly and it is not clear how error correction could help in such a situation. This might, for any error rate, limit the duration of a computation. On the contrary, if the computation is split then the size of the subcircuits may be adjusted such that each of them can be performed within a fixed time  $T$  and in this way, each cluster qubit is, before being measured, exposed to a bounded amount of decoherence specified by  $T$ . Thus, "fresh" qubits for computation are always provided.

# VI. CONCLUSION

In this paper we have given a detailed account of the one-way quantum computer. We have shown that the  $\mathrm{QC}_{\mathcal{C}}$  can be regarded as a simulator of quantum logic networks. This way, we clarified the relation of the  $\mathrm{QC}_{\mathcal{C}}$  to the network model of quantum computation and gave the universality proof.

We have based our description on the correlations exhibited by cluster states and states that can be created from them under one-qubit measurements. For this purpose, Theorem 1 of Sec. II F is an important tool. It relates unitary transformations to quantum correlations exhibited by certain pure states.

In Sec. IV we have presented a number of example circuits such as the circuit for quantum Fourier transformation and for addition. In this way, hopefully, we also have acquainted the reader with a number of construction principles for  $\mathrm{QC}_{\mathcal{C}}$  circuits. Note that the simulations of the universal gates required in the universality proof are hardly used. Instead, more compact measurement patterns have been found.

The main purpose of this paper is to provide a comprehensive description of the  $\mathrm{QC}_{\mathcal{C}}$  from the network perspective. Beyond that, we have pointed out the non-network aspects of the  $\mathrm{QC}_{\mathcal{C}}$ , such as the different nature of information processing [7,8], and the connection to mathematical graphs.

# ACKNOWLEDGMENTS

This work was supported by the Deutsche Forschungsgemeinschaft (DFG) and in part by IST-1999-13021. We would like to thank D. Schlingemann, M. Grassl, M. Hein, H. Aschauer, B. Neuburger, and H. Wagner for valuable discussions.

[1] R. Raussendorf and H.J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[2] H.J. Briegel and R. Raussendorf, Phys. Rev. Lett. 86, 910 (2001).  
[3] M.A. Nielsen and I.L. Chuang, Phys. Rev. Lett. 79, 321 (1997).

[4] D. Gottesman and I.L. Chuang, Nature (London) 402, 390 (1999).  
[5] E. Knill, R. Laflamme, and G.J. Milburn, Nature (London) 409, 46 (2001).  
[6] M.A. Nielsen, e-print quant-ph/0108020; D.W. Leung, e-print quant-ph/0111122.

[7] R. Raussendorf and H.J. Briegel, Quantum Inf. Comput. 6, 443 (2002).  
[8] R. Raussendorf and H.J. Briegel, e-print quant-ph/0207183.  
[9] D. Schlingemann and R.F. Werner, Phys. Rev. A 65, 012308 (2001).  
[10] D. Gottesman, e-print quant-ph/9705052.  
[11] D. Gottesman, Phys. Rev. A 57, 127 (1998).  
[12] A.R. Calderbank, E.M. Rains, P.W. Shor, and N.J.A. Sloane, Phys. Rev. Lett. 78, 405 (1997).  
[13] M.A. Nielsen and I.L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2000).  
[14] D. Jaksch et al., Phys. Rev. Lett. 82, 1975 (1999).  
[15] L.-M. Duan, E. Demler, and M.D. Lukin, e-print cond-mat/0210564.

[16] R. Diestel, Graphentheorie (Springer-Verlag, Heidelberg, 2000).  
[17] P.W. Shor, SIAM J. Sci. Statist. Comput. 26, 1484 (1997).  
[18] L.K. Grover, Phys. Rev. Lett. 79, 325 (1997).  
[19] E. Knill, R. Laflamme, and W.H. Zurek, e-print quant-ph/9702058.  
[20] S. Perdrix (unpublished).  
[21] C. Moore and M. Nilsson, e-print quant-ph/9808027.  
[22] Theorem 10.7 in Quantum Computation and Quantum Information (Ref. [13]).  
[23] M. Grassl, A. Klappenecker, and M. Rötteler, in IEEE International Symposium on Information Theory, Lausanne, 2002 (unpublished), p. 45.  
[24] D. Schlingemann (private communication).  
[25] R.B. Griffiths and C.-S. Niu, Phys. Rev. Lett. 76, 3228 (1996).  
[26] V. Vedral, A. Barenco, and A. Ekert, e-print quant-ph/9511018.