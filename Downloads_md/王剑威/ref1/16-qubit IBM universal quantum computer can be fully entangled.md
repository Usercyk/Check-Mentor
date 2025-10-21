# ARTICLE OPEN

# 16-qubit IBM universal quantum computer can be fully entangled

Yuanhao Wang $^{1}$ , Ying Li $^{2}$ , Zhang-qi Yin $^{1}$  and Bei Zeng $^{3,4}$

Entanglement is an important evidence that a quantum device can potentially solve problems intractable for classical computers. In this paper, we prepare connected graph states involving 8 to 16 qubits on  $ibmqx5$ , a 16-qubit superconducting quantum processor accessible via IBM cloud, using low-depth circuits. We demonstrate that the prepared state is fully entangled, i.e., the state is inseparable with respect to any fixed partition.

npj Quantum Information (2018)4:46; doi:10.1038/s41534-018-0095-x

# INTRODUCTION

Quantum computation has been an active research topic since the middle 90s with the invention of the Shor's algorithm and many other important discoveries such as quantum error correction. For the last two decades, physical implementations of quantum computation have achieved significant progress. The fidelity of single and two-qubit gates exceeds  $99\%$ , reaching the threshold of fault-tolerant quantum computing. The number of qubits in both superconducting and trapped ions quantum computers are both greater than 20 now. It is projected that the number of qubits will approach 50 or more in the next few years. At that time, the quantum computer may become more powerful than the fastest classical computer for some specific tasks, into the regime of the so-called quantum supremacy.

The IBM Q is a quantum cloud service released by IBM. Its present backend devices include two processors with 5 superconducting qubits (ibmqx2 and ibmqx4), one 16-qubit processor (ibmqx5) and one 20-qubit processor (QS1_1). IBM recently announced that they have successfully built and tested a 20-qubit and a 50-qubit machine. The quantum cloud service of IBM provides high fidelity quantum gate operations and measurements. Hence, after the launch of the IBM Q, many groups tested it and performed quantum computing experiments on the cloud (for instance, see refs. 6-12).

Entanglement is considered to be the most nonclassical manifestation of quantum physics. $^{13}$  It is also a critical resource for quantum information processing. Highly entangled states such as Bell states, GHZ (Greenberger-Horne-Zeilinger) states and cluster states $^{14}$  have been applied in quantum teleportation, super-dense coding, one-way quantum computing $^{15}$  and various quantum algorithms. The ability to produce highly entangled states is, therefore, one important step to demonstrate quantumness for quantum processors like ibmqx5. This task is, however, highly non-trivial due to the error accumulation of faulty gates.

In this paper, we wish to assess the quantumness and performance of the 16-qubit ibmqx5 device via the production of highly entangled states, namely the graph states, which is an

important class of many-body entangled states that are widely used in one-way quantum computing, quantum error correction. $^{15,16}$  We generate graph states that correspond to rings involving 8 to 16 qubits via IBM Q cloud service (ibmqx5), using optimized low-depth circuits that are tailored to the universal get set on ibmqx5. We detect full entanglement up to 16 qubits, using an entanglement criterion based on reduced density matrices. Qubits are fully entangled in the sense that the state involves all physical qubits and is inseparable with respect to any fixed partition.

# RESULTS

Graph states and entanglement

Graph state<sup>17</sup> is a generalization of cluster state introduced in 2001,<sup>14</sup> which is the resource state of one-way quantum computing<sup>15</sup> and quantum error correction.<sup>16</sup> GHZ state is an example of graph state and has been demonstrated in superconducting qubit system.<sup>18</sup> However, GHZ state is fragile. Some other graph states are very robust to local operations, such as local measurements and noises. In order to disentangle the cluster state of  $N$  qubits,  $N/2$  local measurements are needed.<sup>14</sup> Because of this nice feature, we decide to generate and detect linear cluster states in the IBM cloud service ibmqx5.

$X, Y, Z$  denote the Pauli operators. An undirected graph  $G(V, E)$  includes a set of vertices  $V$  and a set of edges  $E$ . A graph state that corresponds to an undirected graph  $G(V, E)$  is a  $|V|$ -qubit state that has the form

$$
| G \rangle = \prod_ {(a, b) \in E} U _ {a b} | + \rangle^ {\otimes V}, \tag {1}
$$

where  $U_{ab}$  is a control-Z operator acting on qubits  $a$  and  $b$ ,<sup>19</sup> and

$$
\left| \pm \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 0 \right\rangle \pm \left| 1 \right\rangle\right) \tag {2}
$$

are eigenvectors of the  $X$  operator.

<table><tr><td></td><td>Q0</td><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>Q5</td><td>Q6</td><td>Q7</td><td>Q8</td><td>Q9</td><td>Q10</td><td>Q11</td><td>Q12</td><td>Q13</td><td>Q14</td><td>Q15</td></tr><tr><td>Gate Error (10-3)</td><td>1.74</td><td>3.16</td><td>3.45</td><td>3.22</td><td>1.29</td><td>2.12</td><td>1.42</td><td>1.78</td><td>3.88</td><td>1.50</td><td>1.31</td><td>1.75</td><td>1.94</td><td>1.59</td><td>1.56</td><td>3.43</td></tr><tr><td>Readout Error (10-2)</td><td>5.52</td><td>7.99</td><td>3.17</td><td>5.66</td><td>5.41</td><td>4.25</td><td>4.29</td><td>4.48</td><td>5.02</td><td>5.27</td><td>6.65</td><td>4.82</td><td>7.57</td><td>6.00</td><td>4.90</td><td>7.95</td></tr><tr><td rowspan="6">MultiQubit Gate Error (10-2)</td><td>CX1_0</td><td>CX2_3</td><td>CX3_4</td><td></td><td>CX5_4</td><td>CX6_5</td><td>CX7_10</td><td>CX8_7</td><td>CX9_8</td><td></td><td>CX11_10</td><td>CX12_5</td><td>CX13_4</td><td></td><td>CX15_0</td><td></td></tr><tr><td>4.03</td><td>5.00</td><td>4.62</td><td></td><td>3.30</td><td>3.28</td><td>3.72</td><td>5.54</td><td>6.29</td><td></td><td>2.42</td><td>4.72</td><td>2.83</td><td></td><td>3.76</td><td></td></tr><tr><td>CX1_2</td><td></td><td>CX3_14</td><td></td><td></td><td>CX6_7</td><td></td><td></td><td>CX9_10</td><td></td><td></td><td>CX12_11</td><td>CX13_14</td><td></td><td>CX15_2</td><td></td></tr><tr><td>3.67</td><td></td><td>4.58</td><td></td><td></td><td>3.00</td><td></td><td></td><td>3.66</td><td></td><td></td><td>4.35</td><td>3.46</td><td></td><td>4.16</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>CX6_11</td><td></td><td></td><td></td><td></td><td></td><td>CX12_13</td><td></td><td></td><td>CX15_14</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>3.11</td><td></td><td></td><td></td><td></td><td></td><td>4.05</td><td></td><td></td><td>3.68</td><td></td></tr></table>

![](images/59826cec2c970ae25f63f5ae772ab4636683cda52db41a2ff997ee166bbbd0c6.jpg)  
Fig. 1 Calibration parameters of ibmqx5, archived 10 January 2018 from ref. It should be noted that these parameters are updated on a daily basis  
Fig. 2 Connectivity map of ibmqx530

![](images/dd82a4bceafa9aee599ece0c15e21971055b181367d64a9b6e5ffc12dfe3eb44.jpg)  
Fig. 3 Graph states employed in this experiment. Colored lines illustrate the graph of the 8-qubit graph state (in red), 10-qubit graph state (orange), 12-qubit graph state (yellow), 14-qubit state (blue) and 16-qubit graph state (purple)

An equivalent definition, the graph state that corresponds to  $G(V,E)$ , is the unique common eigenvector (of eigenvalue 1) of the set of independent commuting operators:

$$
K _ {a} = X ^ {a} Z ^ {N _ {a}} = X ^ {a} \prod_ {b \in N _ {a}} Z ^ {b}, \tag {3}
$$

where the eigenvalues to  $K_{a}$  are  $+1$  for all  $a \in V$ , and  $N_{a}$  denotes the set of neighbor vertices of  $a$  in  $G$ . As implied by the first definition, a  $n$ -qubit graph state can be prepared by the following steps.

1. Initialize the state to  $| + \rangle^{\otimes n}$  by applying  $n$  Hadamard gates to  $|0\rangle^{\otimes n}$ ;  
2. For every  $(a, b) \in E$ , apply a control-Z gate on qubits  $a$  and  $b$ ; the order can be arbitrary.

Entanglement of general mixed states was discussed by Werner in 1989.[20] Since then, many entanglement criteria were proposed; among them the widely used ones include the partial transpose criterion[13,21,22] and the symmetric extension criterion.[23]

A bipartite state  $\rho_{AB}$  on the Hilbert space  $\mathcal{H} = \mathcal{H}_A\otimes \mathcal{H}_B$  is said to be separable if  $\rho_{AB}$  can be written as

$$
\rho_ {A B} = \sum_ {i} p _ {i} \rho_ {A} ^ {i} \otimes \rho_ {B} ^ {i}, \tag {4}
$$

where  $\rho_A^i$  and  $\rho_B^i$  are quantum states of the system  $A$  and  $B$ , respectively, with  $p_i \geq 0$  and  $\sum_{i} p_i = 1$ . Otherwise  $\rho_{AB}$  is entangled. For a state  $\rho$  of a many-body system, for any fixed bipartition  $AB$  of the system, if  $\rho$  is entangled with respect to the partition  $AB$ , then the entanglement of the many-body state  $\rho$  can also be examined via its subsystems. That is, if the subsystems are all entangled, the whole system must be also entangled.

To be more concrete, consider a 4-qubit subsystem  $\rho_{A,B,C,D}$  in an  $n$ -qubit system. Suppose that we perform two local operations  $O_A$  and  $O_D$  on qubit  $A$  and  $D$  respectively, and then obtain the reduced density matrix of qubit  $B$  and  $C$  by tracing out qubit  $A$  and  $D$ . The reduced density matrix for qubits  $B$  and  $C$  reads

$$
\rho_ {B, C} ^ {\prime} = t r _ {A, D} \left(\frac {O _ {A} O _ {D} \rho_ {A , B , C , D} O _ {D} ^ {\dagger} O _ {A} ^ {\dagger}}{t r \left(O _ {A} O _ {D} \rho_ {A , B , C , D} O _ {D} ^ {\dagger} O _ {A} ^ {\dagger}\right)}\right). \tag {5}
$$

The entanglement of  $\rho_{B,C}^{\prime}$  can be determined by using entanglement monotones such as negativity and concurrence, which, in the 2-qubit case, has non-zero values if and only if the system is entangled.[13,22] If  $\rho_{B,C}^{\prime}$  is entangled, we can conclude that in the original system, there could not exist a separation with qubit  $B$  and  $C$  on different sides. In other words, if the original system is biseparable with respect to a fixed partition, the qubit  $B$  and  $C$  must be on the same side. Otherwise, we will be able to create entanglement between the two separable parties with only local operations, which is not possible.[13]

For an  $n$ -qubit system  $\{q_1, q_2, \ldots, q_n\}$ , if we can show that among the  $n$ -qubit pairs  $(q_1, q_2), \ldots, (q_{n-1}, q_n), (q_n, q_1), n-1$  of them must be on the same side in a separation, then we may conclude that there is no possible separation, and that the system is a  $n$ -qubit entangled state (meaning that the state is not biseparable with respect to (w.r.t.) a fixed partition, and that it involves all qubits). The (minimal) number of circuit configurations needed in this approach is  $3^4(n-1)$ , which grows linear with respect to  $n$ . This method is far more efficient compared to a full  $n$ -qubit tomography, which requires exponential number of configurations.

# Graph states on ibmqx5

ibmqx5 is a 16-qubit superconducting quantum processor. It allows independent single-qubit operations with fidelity  $>99\%$  and control operations with fidelity  $95 - 97\%$  (see Fig. 1) marked as the edges in the connectivity map (see Fig. 2). That is, controlled NOT (CNOT) operations with qubit  $a$  as the control qubit and  $b$  as the target is allowed if and only if  $a \rightarrow b$  is an edge in the map.

In our experiment, as shown in Fig. 3, the following five graph states are employed. The first state is a 8-qubit graph state involving qubits  $q5 - q12$  that corresponds to a ring of length 8; the second one is a 10-qubit state involving qubits  $q4 - q13$  corresponding to a ring of length 10; the third one involves qubits  $q3 - q14$  and corresponds to a ring of length 12; the fourth one involves qubits  $q2 - q15$  and corresponds to a ring of length 14; the fifth one involves all the 16 qubits. We employ these particular graph states based on the following considerations. First, these states are genuinely entangled and will remain entangled after tracing out a large number of qubits. Second, research has shown that one-dimensional (1D) cluster states are robust against decoherence, meaning that it would be more likely to find entanglement in a rather large graph state close to a 1D chain, compared to GHZ states and two-dimensional (2D) graph states.[24] At last, even rings are two-edge colorable; as a result, on the 16-qubit ibmqx5, these "even-ring" states could be prepared using low-depth circuits (see Fig. 4).

To prepare the desired graph state, we start from the circuit implied by the definition of graph states (see Fig. 4a). The control-Z gates are implemented using a CNOT gate and two Hadamard gates. We then optimize this circuit by adjusting the order of commuting gates and removing redundant Hadamard gates (see Fig. 4b). The circuit that we implemented are shown in Fig. 4b and Fig. 5a-d.

# Experimental results

For each  $n$ -qubit ring state,  $n$  partial tomographies are performed for every subsystem with 4 qubits that forms a chain in the ring. For example, for the 8-qubit graph state, the 8 subsystems are (q5, q6, q7, q8), (q6, q7, q8, q9), ..., (q12, q5, q6, q7). For every state,  $3^4 n$  experimental configurations are used; 2048 measurements are taken under each configuration. The  $n$  4-qubit reduced density matrices are obtained using the maximum likelihood method proposed by Smolin et al.[25]

Due to Eq. (3), for a ring graph state, each 4-qubit density matrix of neighboring four qubits, as illustrated in Fig. 6, is given by

$$
\rho_ {A, B, C, D} = \frac {1}{4} \left(I + Z _ {A} X _ {B} Z _ {C}\right) \left(I + Z _ {B} X _ {C} Z _ {D}\right). \tag {6}
$$

![](images/9401282494ffc62ea7aa6db8789d472721e6f9e48d1a4999b152cffaec3594a6.jpg)  
Fig. 4 a The quantum circuit for preparing a 8-qubit graph state implied by the definition of graph states. b The optimized circuit that suits ibmqx5's connectivity

![](images/fa060d4fdd998812684a55cfc33010e23a7a7549e3f004c603404fa11ccf458f.jpg)

![](images/91010ab861285b68ca5de4b213f0e017f5d6178597fb9412c6f916700fd14b66.jpg)

![](images/5becd3fa93efff57ca353c3a1dc3035de3e7ae81d3180c28ef989fafb324228e.jpg)

![](images/452c6a8f8e9db409e9e4a936a9783bd034d4c66f4c52c91dc94da8d8060cfed8.jpg)  
Fig. 5 The quantum circuit implemented on ibmqx5 for the preparation of a 10-qubit graph state, b 12-qubit graph state, c 14-qubit graph state and d 16-qubit graph state

![](images/f097d7653e0ba90fc75bc56d3a420df6e9febffb9c41bf55a66d2eb1a5aa5dd1.jpg)

![](images/5092a61961604842b8f1b02cbff61de336ef7b6c50ab8ce32c4bc6ae00dabc1d.jpg)  
Fig. 6 A 4-qubit subsystem that forms a chain

Then, for each 4-qubit density matrix, we apply the local operations  $O_A = \frac{Z_A + I}{2}$  and  $O_D = \frac{Z_D + I}{2}$  and calculate the negativity of the resulting 2-qubit subsystem. For instance, we may choose (q5, q6, q7, q8) as our subsystem; after applying  $O_A$  and  $O_D$  to q5 and q8 respectively, we will trace out q5 and q8, and measure the negativity of the remaining subsystem, (q6, q7). We choose  $O_A = \frac{Z_A + I}{2}$  and  $O_D = \frac{Z_D + I}{\nu}$  for the following reason. If  $\rho$  is graph state, and the 4-qubit subsystem corresponds to 4 vertices that form a chain in the graph, then the resulting 2-qubit state is a maximally entangled state

$$
| \phi \rangle = \frac {1}{\sqrt {2}} (| 0 \rangle | + \rangle + | 1 \rangle | - \rangle). \tag {7}
$$

Therefore, for a state close to this graph state, we should expect

![](images/31b6320ec498a5ceb29eefb88e1c9ce0929e2831fcf7c4a97bf8fe59e68f22bd.jpg)

![](images/8b8642ab38644d5c3212da924fc2c12619523e45858f082966d0d2351c4a8c74.jpg)

![](images/0dbedd2cfd721a373f5d249b70f8de02e5a998669eed22791a9c0b478afb7cc3.jpg)

![](images/c901c31dbc8e1e25bf875e22544f9211a0354e6497649997324dc57f466ddfd0.jpg)

![](images/735d3f12ec2ace794c3a3164ab299a4e7b4d560ddb053828c12ef1aa50723d92.jpg)  
Fig. 7 The result of a the 8-qubit graph state, b the 10-qubit graph state, c the 12-qubit graph state, d the 14-qubit graph state and e the 16-qubit graph state. The negativity of the final 2-qubit states are plotted. The  $95\%$  confidence intervals are estimated using bootstrapping techniques

the resulting 2-qubit state to have a negativity significantly greater than 0. The results are plotted in Fig. 7.

For the 8-qubit graph state, the measured negativities are all significantly greater than 0. For the 10-qubit graph state, 9 out of 10 measured negativities are significantly greater than 0. Based on our argument above, both the 8-qubit state and 10-qubit state are fully entangled.

In the 12-qubit case, as shown in Fig. 7c, 10 out of 12 measured negativites are significantly non-zero. The two zeros come from (q9, q10) and (q14, q3) pairs. Therefore, there is only one possible separation, namely {q10, q11, q12, q13, q14} | {q3, q4, q5, q6, q7, q8, q9}. Should this be true, the reduced density matrix of qubits q8, q9,q10,q11 should also be separable with the separation {q8, q9} |

$\{q10, q11\}$ . In that case, its partial transpose with respect to qubit  $q8$  and  $q9$  must be positive. However, with respect to this partial transpose,  $\rho_{q8,q9,q10,q11}$  has negativity  $0.0391 \pm 0.0039$  (standard deviation estimated via bootstrapping). Therefore, this possibility is ruled out with very high confidence. We can now conclude that the 12-qubit graph state is fully entangled.

In the 14-qubit case, as shown in Fig. 7d, 12 out of 14 measured negativites are significantly greater than 0. Here, we may apply the same trick again. The only possible separation is  $\{q2, q3, q4, q5, q6, q7, q8, q9, q12, q13, q14\} \mid \{q10, q11\}$ . In this case, subsystem  $\{q8, q9, q10, q11\}$  should have zero negativity with respect to the partial transpose on  $q8$  and  $q9$ . However, the measured negativity is  $0.0698 \pm 0.0048$  (standard deviation estimated via

bootstrapping). Hence, this possibility is ruled out with very high confidence. We may conclude that this state is fully entangled.

In the 16-qubit case, as shown in Fig. 7e, 15 out of 16 measured negativites are significantly greater than 0. As argued above, this means that this state is not biseparable w.r.t. a fixed partition, thereby showing that all 16 qubits in ibmqx5 are in full entanglement.

It may be noted that the subsystem of qubits  $\{q8, q9, q10, q11\}$  yields close-to-zero negativity in 3 out of 4 experiments. This can be due to relatively high readout errors or gate errors involving these qubits, which is compatible with the measured parameters provided by IBM website (see Fig. 1). For instance, the CNOT gate between  $q10$  and  $q11$  has the largest error among all possible CNOT gates, while the readout errors of  $q10$  and  $q11$  are also above the average level  $(6.5\%)$ .

# Further exploration of the 16-qubit state

The results above could be understood as an ability to generate localized entanglement on physically neighboring qubits.[26] That is, neighboring qubits can be put into entanglement by performing ideal local operations on the 16-qubit state. Using the same data obtained above, we will show that localized entanglement on qubits with distance 2 and 3 could also be generated.

Suppose  $\{E, A, B, C, D, F\}$  is a 6-qubit subsystem that forms a chain. We first apply  $O_{E} = \frac{Z_{E} \pm I}{2}$  and  $O_{F} = \frac{Z_{F} \pm I}{2}$  on  $E$  and  $F$  respectively (four possibilities). On our data, this can effectively be done by first postselecting 0s on qubits  $E$  and  $F$  before calculating the tomography of  $\{A, B, C, D\}$ . Next,  $O_{B} = \frac{X_{B} + I}{2}$  and  $O_{D} = \frac{Z_{D} + I}{2}$  are performed (see Fig. 8). At last,  $B, E, F$  and  $D$  are traced out, while the negativity in subsystem  $\{A, C\}$  is calculated. If the 16-qubit state is perfect, this resulting system would be maximum entangled.

Based on data obtained in previous experiments, we have calculated the corresponding negativity for each 6-qubit subsystem and shown them in Table 1. Using this method, we have identified localized entanglement in 13 out of 16 pairs of qubits with distance 2.

To generate localized entanglement on qubits with distance 3, we may apply the same  $O_{E}$  and  $O_{F}$ , and then apply  $O_{B}^{\prime} = \frac{X_{B} + I}{2}$  and  $O_{C}^{\prime} = \frac{X_{C} + I}{2}$  (see Fig. 9). The negativity of subsystem  $\{A, D\}$  would be calculated. Again, if the 16-qubit state is perfect, these two qubits would be maximum entangled; therefore, we should expect a non-zero negativity if the actual state is close to the theoretical one.

Among 16 pairs of qubits with distance 3, we have identified localized entanglement in 6 pairs of them. The results based on our data is presented in Table 2.

![](images/4f3abb8951bf39f4ac0d4f9cd9b2901fa049acb0bd9cdb372dc1ccd5c386074c.jpg)  
Fig. 8 Operations performed to produce entanglement on subsystem  $\{A,C\}$

<table><tr><td colspan="8">Table 1. Negativities of qubits with distance 2 in the 16-qubit state</td></tr><tr><td>(0, 2)</td><td>(1, 3)</td><td>(2, 4)</td><td>(3, 5)</td><td>(4, 6)</td><td>(5, 7)</td><td>(6, 8)</td><td>(7, 9)</td></tr><tr><td>0.023</td><td>0.027</td><td>0.088</td><td>0.145</td><td>0.143</td><td>0.156</td><td>0.134</td><td>0.105</td></tr><tr><td>(8, 10)</td><td>(9, 11)</td><td>(10, 12)</td><td>(11, 13)</td><td>(12, 14)</td><td>(13, 15)</td><td>(14, 0)</td><td>(15, 1)</td></tr><tr><td>0.178</td><td>0.000</td><td>0.114</td><td>0.079</td><td>0.040</td><td>0.028</td><td>0.000</td><td>0.000</td></tr></table>

![](images/45089493ab669beda820331bb2d96e35062e7f82965cf2d81db3c118c7c80d46.jpg)  
Fig. 9 Operations performed to produce entanglement on subsystem  $\{A, D\}$

<table><tr><td colspan="8">Table 2. Negativities of qubits with distance 3 in the 16-qubit state</td></tr><tr><td>(0, 3)</td><td>(1, 4)</td><td>(2, 5)</td><td>(3, 6)</td><td>(4, 7)</td><td>(5, 8)</td><td>(6, 9)</td><td>(7, 10)</td></tr><tr><td>0.000</td><td>0.000</td><td>0.085</td><td>0.093</td><td>0.110</td><td>0.097</td><td>0.061</td><td>0.000</td></tr><tr><td>(8, 11)</td><td>(9, 12)</td><td>(10, 13)</td><td>(11, 14)</td><td>(12, 15)</td><td>(13, 0)</td><td>(14, 1)</td><td>(15, 2)</td></tr><tr><td>0.012</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td></tr></table>

# DISCUSSION

We have prepared graph states of 8, 10, 12, 14 and 16 qubits on the 16-qubit ibmqx5 processor and demonstrated that these graph states are not biseparable w.r.t. any fixed partition. In particular, we have realized full entanglement using all 16 qubits. Moreover, we have demonstrated the ability to create localized entanglement on qubit pairs with distance 3 and 4 from this 16-qubit entangled state. In our approach of detecting nonseparability, we only have to measure the reduced density matrix of up to 4 qubits, and the size of reduced density matrix does not scale with the total qubit number, i.e., our method is efficient and scalable. In our experiments, graph states do not have high fidelity because of the large number of qubits, e.g., the fidelity of the 12-qubit graph state is lower than 0.44. (This upperbound is obtained by computing the fidelity between each 4-qubit subsystem and the theoretical result and taking the minimum.) However, the negativity of 4-qubit reduced density matrix decays gently with respect to the qubit number, which implies that the error per qubit weakly depends on the qubit number. It is a strong evidence that ibmqx5 is capable of generating highly entangled states and demonstrates the computer's quantumness. In computational tasks such as one-way quantum computing, graph state with decaying fidelity is acceptable, and the computing is fault tolerant as long as the error per qubit is lower than a threshold.[27,28]

# DATA AVAILABILITY

The experimental data that support the findings of this study29 are available in figshare with the identifier https://doi.org/10.6084/m9.figshare.6790781.

# ACKNOWLEDGEMENTS

We gratefully acknowledge the IBM Q team for providing us access to their 16-qubit platform. The views expressed are those of the authors and do not reflect the official policy or position of IBM or the IBM Quantum Experience team. Y.L. is supported by NSAF (Grant No. U1730449). Z.-Q.Y. is supported by the National Natural Science Foundation of China Grants 61771278, 11574176 and 11474177. B.Z. is supported by NSERC and CIFAR.

# AUTHOR CONTRIBUTIONS

Y.L., Z.-Q.Y. and B.Z. designed and conceived the study. Y.W. designed quantum circuits and performed the experiments. All authors wrote the manuscript.

# ADDITIONAL INFORMATION

Competing interests: The authors declare no competing interests.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

# REFERENCES

1. Nielsen, M. A. & Chuang, I. Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, 2002).  
2. Barends, R. et al. Superconducting quantum circuits at the surface code threshold for fault tolerance. Nature 508, 500-503 (2014).  
3. Friis, N. et al. Observation of entangled states of a fully controlled 20-qubit system. Phys. Rev. X 8, 021012 (2018).  
4. IBM Q experience. https://quantumexperience.ng.bluemix.net/qx/devices. Accessed 27 December 2017.  
5. Preskill, J. Quantum computing and the entanglement frontier. arXiv preprint arXiv:1203.5813 (2012).  
6. Alsina, D. & Latorre, J. I. Experimental test of mermin inequalities on a five-qubit quantum computer. Phys. Rev. A 94, 012314 (2016).  
7. Devitt, S. J. Performing quantum computing experiments in the cloud. Phys. Rev. A 94, 032329 (2016).  
8. Berta, M., Wehner, S. & Wilde, M. M. Entropic uncertainty and measurement reversibility. New J. Phys. 18, 073004 (2016).  
9. Rundle, R. P., Mills, P. W., Tilma, T., Samson, J. H. & Everitt, M. J. Simple procedure for phase-space measurement and entanglement validation. Phys. Rev. A 96, 022117 (2017).  
10. Huffman, E. & Mizel, A. Violation of noninvasive macrorealism by a superconducting qubit: Implementation of a leggett-garg test that addresses the clumsiness loophole. Phys. Rev. A 95, 032131 (2017).  
11. Hebenstreit, M., Alsina, D., Latorre, J. I. & Kraus, B. Compressed quantum computation using a remote five-qubit quantum computer. Phys. Rev. A 95, 052339 (2017).  
12. Ferrari, D. & Amoretti, M. Demonstration of envariance and parity learning on the IBM 16 qubit processor. *ArXiv e-prints* (2018). 1801.02363.  
13. Horodecki, R., Horodecki, P., Horodecki, M. & Horodecki, K. Quantum entanglement. Rev. Mod. Phys. 81, 865 (2009).  
14. Briegel, H. J. & Raussendorf, R. Persistent entanglement in arrays of interacting particles. Phys. Rev. Lett. 86, 910 (2001).  
15. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188 (2001).  
16. Raussendorf, R. & Harrington, J. Fault-tolerant quantum computation with high threshold in two dimensions. Phys. Rev. Lett. 98, 190504 (2007).  
17. Hein, M., Eisert, J. & Briegel, H. J. Multiparty entanglement in graph states. Phys. Rev. A 69, 062311 (2004).  
18. Song, C. et al. 10-qubit entanglement and parallel logic operations with a superconducting circuit. Phys. Rev. Lett. 119, 180511 (2017).  
19. Hein, M. et al. Entanglement in graph states and its applications (2006). quant-ph/ 0602096.

20. Werner, R. F. Quantum states with einstein-podolsky-rosen correlations admitting a hidden-variable model. Phys. Rev. A 40, 4277 (1989).  
21. Peres, A. Separability criterion for density matrices. Phys. Rev. Lett. 77, 1413 (1996).  
22. Horodecki, M., Horodecki, P. & Horodecki, R. Separability of mixed states: necessary and sufficient conditions. Phys. Lett. A 223, 1-8 (1996).  
23. Doherty, A. C., Parrilo, P. A. & Spedalieri, F. M. Distinguishing separable and entangled states. Phys. Rev. Lett. 88, 187904 (2002).  
24. Hein, M., Dur, W. & Briegel, H.-J. Entanglement properties of multipartite entangled states under the influence of decoherence. Phys. Rev. A 71, 032350 (2005).  
25. Smolin, J. A., Gambetta, J. M. & Smith, G. Efficient method for computing the maximum-likelihood quantum state from measurements with additive gaussian noise. Phys. Rev. Lett. 108, 070502 (2012).  
26. Popp, M., Verstraete, F., Martin-Delgado, M. A. & Cirac, J. I. Localizable entanglement. Phys. Rev. A 71, 042306 (2005).  
27. Nielsen, M. A. & Dawson, C. M. Fault-tolerant quantum computation with cluster states. Phys. Rev. A 71, 042323 (2005).  
28. Raussendorf, R., Harrington, J. & Goyal, K. A fault-tolerant one-way quantum computer. Ann. Phys. 321, 2242-2270 (2006).  
29. Wang, Y., Li, Y., Yin, Z. & Zeng, B. 16-qubit ibm quantum processor entanglement (2018). https://figshare.com/articles/16-qubit_IBM_quantum Processor_ entanglement/6790781/1.  
30. The IBM Q experience ibmqx5 backend. https://github.com/QISKit/ibmqx5-backend-information/tree/master/backends/ibmqx5. Accessed 27 December 2017.

![](images/04ebac5f0f58b30d9fcea1ad2a3ef4c86cf6d4b46df1983e454e87b1b4ba7c93.jpg)

Open Access This article is licensed under a Creative Commons

Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2018