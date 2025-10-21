# Error-protected qubits in a silicon photonic chip

Caterina Vigliar  $①$ , Stefano Paesani  $①$ , Yunhong Ding  $②, 3$ ☑, Jeremy C. Adcock  $①$ , Jianwei Wang  $④, 5$ ☑, Sam Morley-Short  $①$ , Davide Bacco  $②, 3$ , Leif K. Oxenløwe  $②, 3$ , Mark G. Thompson  $①$ , John G. Rarity  $①$  and Anthony Laing  $①$

General-purpose quantum computers can, in principle, entangle a number of noisy physical qubits to realize composite qubits protected against errors. Architectures for measurement-based quantum computing intrinsically support error-protected qubits and are the most viable approach for constructing an all-photonic quantum computer. Here we propose and demonstrate an integrated silicon photonic scheme that both entangles multiple photons, and encodes multiple physical qubits on individual photons, to produce error-protected qubits. We realize reconfigurable graph states to compare several schemes with and without error-correction encodings and implement a range of quantum information processing tasks. We observe a success rate increase from  $62.5\%$  to  $95.8\%$  when running a phase-estimation algorithm without and with error protection, respectively. Finally, we realize hypergraph states, which are a generalized class of resource states that offer protection against correlated errors. Our results show how quantum error-correction encodings can be implemented with resource-efficient photonic architectures to improve the performance of quantum algorithms.

While rudimentary quantum computers can now solve abstract tasks that are intractable to classical computers $^{1-3}$ , a general-purpose quantum computer will require error-correcting schemes to protect information as it is processed in a useful quantum algorithm $^{4,5}$ . Measurement-based quantum computing (MBQC) uses entangled states of physical qubits, namely graph states, to run an algorithm by measuring sequences of qubits and propagating information between different physical layers of the state $^{6-10}$ . As graph states are both the resource for MBQC and have a direct mapping to quantum error-correcting codes for error-protected qubits, MBQC intrinsically facilitates a fault-tolerant architecture $^{11-17}$ .

Integrated photonics is an appealing platform for architectures that build large graph states for fault-tolerant  $\mathrm{MBQC}^{18-20}$ . Thousands of optical components can be densely integrated onto a single silicon chip $^{21-24}$ , to realize the complex photonic circuitry required to generate and control entangled states of many photons. Encoding multiple qubits onto individual photons, within a multiphoton state, provides a natural resource-saving approach $^{21,25-27}$ .

In this Article we develop a scheme that combines on-chip generation of multiple pairs of entangled photons and encoding of multiple qubits on individual photons via the creation of  $d$ -level systems—qubits—to realize programmable graph states and error-protected qubits. Small clusters of qubits are encoded in single photons; multiple photons are then fused together with probabilistic entangling gates. Our scheme is modular, with the production, processing and measurement of the graph states performed by different units of the same chip.

We experimentally implement this scheme on a silicon photonic chip to realize eight-qubit reconfigurable graph states encoded in four photons. Each photonic module embeds tens of optical components, totalling more than 220 components, including eight photon-pair sources, multi-mode interferometers (MMIs),

and programmable circuitry with 48 phase shifters. We experimentally investigate different classes of graph states and demonstrate error-protected computations and teleportation schemes. In our device, the error protection of measurement-based operations is performed via a probabilistic correction of computational errors affecting physical nodes in the graph state. We run a simple version of the phase-estimation algorithm (PEA) and demonstrate the improvement in performance that results from implementing error-correction encodings. Finally, we experimentally demonstrate the generation and processing of hypergraph states—generalized graph state resources that can represent a novel approach to the MBQC paradigm.

# Scheme and device

Our silicon photonic chip, shown in Fig. 1b, can be decomposed into three different modules, as shown in Fig. 1a. First, eight coherently pumped spiral waveguides (1.5 cm long) generate two maximally entangled pairs of photons, which are spatially separated with integrated filters based on asymmetric Mach-Zehnder interferometers and waveguide crossovers[21]. Each photon encodes a pair of qubits using the spatial mode mapping  $\{|0\rangle \rightarrow |00\rangle ,|1\rangle \rightarrow |01\rangle$ $|2\rangle \rightarrow |10\rangle ,|3\rangle \rightarrow |11\rangle \}$ , as shown in Fig. 1a, to realize an eight-qubit system. Next, programmable entangling gate modules (shown in Fig. 1a) are used to realize graph states of these eight qubits implementing fusion operations between the different photon pairs[23,28]. Finally, a triangular structure of Mach-Zehnder interferometers performs arbitrary projective measurements. Photons are fibre coupled off-chip using low-loss ( $< 1\mathrm{dB}$ ) grating couplers[29], and routed to high-efficiency superconducting nanowire single-photon detectors (see Supplementary Sections 1 and 2 for further experimental details).

Different graph states can be realized from different four-photon four-dimensional states, which are obtained by pumping different

![](images/00ac3ed22f0b825fa4c09f923c7b7e70f44bb51fe948ee6a943501eeb4e8a822.jpg)  
a

![](images/2130b7b1ecf70cb1d116743f83797da7532472b26851e51a70a6a22227e21115.jpg)

![](images/a07eb55f86528522af50ee432b407f413565e1d3695c88b765e617151940c298.jpg)

![](images/7adf2dcbedf7024bbeb8b3f84fd1dbe16f1ee6036cb1d66e72d409ff4d89ba4a.jpg)

![](images/4df2318ba4848c1902054f0cf7058934c997432e8a8a4d5bd9091686ed9fe5a7.jpg)  
b

![](images/b7d3917ec3a71e778f383297ddc740d687f4ad3d2d5965cd585112bbe9c46a7d.jpg)  
Fig. 1 | Device description and performance. a, Schematics of the silicon chip modules. Two entangled qudit-pair modules (black rectangles), each consisting of four photon-pair sources, generate two pairs of maximally entangled quitts (A-B and C-D). Each qudit, encoded in either a signal (red) or an idler (blue) photon, is mapped to a two-qubit system. Photons A-D and B-C are entangled with fusion-type gates (black circles) to produce entangled states of eight qubits among four parties. Measurement modules (blue and red squares) perform arbitrary projective measurements on each photon. b, Photograph of the silicon photonic chip. c, State characterization of a trial four-photon four-dimensional entangled state:  $\langle |0000\rangle +\mathrm{e}^{-\mathrm{i}\pi /4}|0033\rangle +\mathrm{e}^{\mathrm{i}\pi /2}|1111\rangle$ $+|1212\rangle +\mathrm{e}^{\mathrm{i}\pi /4}|2121\rangle +\mathrm{e}^{-\mathrm{i}\pi /4}|2222\rangle +\mathrm{e}^{\mathrm{i}\pi /2}|3300\rangle +\mathrm{e}^{\mathrm{i}\pi /4}|3333\rangle)$ / $2^{3/2}$ . The non-zero elements of the density matrix  $\rho$  (left) are measured to obtain fidelity of  $0.72 \pm 0.04$  with the theoretical target state (right). Column heights represent the absolute value of the non-zero entries of the complex matrix, while phases are colour coded. Error bars are obtained from Monte Carlo simulations assuming a Poissonian distribution of the measured counts.

sources and by programming both the entangling gates and the single-photon two-qubit measurement stages. The characterization of one of the initial four-photon four-dimensional resources, using partial state tomography $^{30}$ , is shown in Fig. 1c, for which we measure a fidelity of  $0.72 \pm 0.04$  against the ideal state (see Supplementary Section 3 for more details). Comparing with other post-selected entanglement generation schemes in linear optics, a larger variety of graph state topologies is available by encoding multiple qubits onto single photons than is available by encoding a single qubit per photon $^{31,32}$  (see Supplementary Section 12). In fact, local operations on individual photons, each encoding four-dimensional quuds, allow non-local operations between the two qubits encoded in that photon. Such non-local operations are deterministic and have substantially higher fidelities than gates between different photons (due to the absence of distinguishability limitations in multiphoton interference). These properties are advantageous for encoding physical qubits that make up a single logical node within an individual photon. When using codes with constant numbers of qubits, for example five-qubit codes to correct arbitrary local unitary errors $^{11}$ , the overhead of such an encoding is a constant number of additional modes per photon, which is practical for current integrated quantum photonics technologies $^{21}$ . Overall, our chip generates 21 graph

state equivalence classes with up to eight qubits (more than 120 different graphs). This is in contrast to the 4 classes (8 different graphs) with up to four qubits that are accessible with two-dimensional photonic architectures using post-selection and the same number of processed photons (for more details, see Supplementary Section 4).

Figure 2 reports fidelities for a variety of graph states with up to eight qubits. These include the eight-qubit star graph  $(| \mathrm{star}_8 \rangle)$ , the 'double-branched' graph states of seven  $(| \mathrm{B}_7 \rangle)$  and five  $(| \mathrm{B}_5 \rangle)$  qubits, the six-qubit 'crazy graph'  $(| \mathrm{crazy}_6 \rangle)^{20}$ , the five-, four- and three-qubit linear states  $(| \mathrm{L}_5 \rangle, | \mathrm{L}_4 \rangle$  and  $| \mathrm{L}_3 \rangle$ , respectively) and the four-qubit star  $(| \mathrm{star}_4 \rangle)$  and box  $(| \square_4 \rangle)$  states. States shown in Fig. 2 are all derived from  $| \mathrm{star}_8 \rangle$ , via local rotations and two-qubit (intra-qudit) operations. Our graph state verification methods (stabilizer measurements<sup>33</sup>, compressed sensing tomography<sup>34</sup> and  $\theta$ -measurements<sup>35,36</sup>) and the device configurations used to generate these states are discussed in Supplementary Section 4.

# Physical and logical MBQC

Different classes of graph states correspond to different computational tasks in the MBQC paradigm $^{7,37}$ . The ability to reprogram graph states enables us to reprogram the type of computation. As shown in Fig. 3a, we tested universal single-qubit gate operations in

![](images/a5d4c86f6182301508ee12919a8c87d0f4f5438cce0f46c8ed5f37d90a390fad.jpg)  
Fig. 2 | Graph state fidelities. State fidelities with the graph states in the associated vertical shaded regions. Estimates using stabilizer methods are shown as blue circles, while orange diamonds show the mean of only stabilizer generator measurements. Fidelity estimations using compressed sensing tomographies are indicated with yellow squares (two-photon data). A fidelity of  $0.73 \pm 0.03$  for the eight-qubit star graph, obtained via  $\theta$ -measurement methods, is shown as a black triangle. All error bars are obtained assuming a Poissonian distribution of the measured counts.

MBQC with arbitrary state initialization and measurement, using a five-qubit one-dimensional lattice. Measurements on the first and last physical qubits perform the state preparation and readout, while measurements on the three central qubits implement Euler decompositions of arbitrary single-qubit gates<sup>7</sup>. The ability to initialize and read out in arbitrary bases allows us to characterize this MBQC channel via full process tomography<sup>38</sup> (for further details see Supplementary Sections 5 and 6). Figure 3a shows single-qubit MBQC process tomography for different gates: a Hadamard gate, a rotation  $\hat{R}_{Z}(\frac{\pi}{2})$  and an  $\hat{X}$  gate. The measured fidelities for these gates are  $0.98 \pm 0.08$ ,  $0.92 \pm 0.06$  and  $0.79 \pm 0.06$ , respectively. Error bars represent the s.e.m., obtained from Monte Carlo simulations assuming a Poissonian distribution of the measured counts.

Logical states and operations can be protected in MBQC by replacing each physical qubit of the lattice with a stabilizer error-correcting code. This results in a new graph definition in which each vertex is a logical qubit, encoded in multiple physical qubits; the overall state of physical qubits can still be represented as a graph state[1]. For example, so-called 'crazy graph' structures can equip linear graph states with error correction, where a repetition code associated with each column of the two-dimensional physical lattice replaces a single physical vertex, resulting in a linear logical graph[20] (see Supplementary Section 6 for more details). Such states are suitable for photonic fault-tolerant architectures, as they can correct both computational errors and high levels of qubit loss[39]. An example of crazy graph encoding is represented in Fig. 3b for the case of a three-qubit logical linear graph state encoded in the six-qubit crazy graph physical state. In this case, each logical qubit of the linear graph is encoded in a two-qubit repetition code in the  $\hat{X}$  basis to detect phase-flip errors[38]:  $|+\rangle_{i_L} = |++\rangle_{2i-1,2i'}$ $|-\rangle_{i_L} = |--\rangle_{2i-1,2i'}$ , where  $i \in \{1,2,3\}$  indicates the column of the crazy graph. Cases such as  $|+-\rangle_{ij}$  are detected as errors and filtered out. Note that local measurements in the logical computational basis correspond to non-local measurements of physical qubits encoded in the same qudit. Using the crazy graph state we perform process tomography of single-qubit  $\hat{R}_X$  rotations in MBQC on a logical lattice. Error protection is performed throughout the whole process of the computation: state encoding, processing and readout. Tomography matrices measured for different processes are reported in Fig. 3b for both uncorrected and error-corrected cases. Crucially, for each gate analysed the fidelity with error protection exceeds that without error protection. See Supplementary Sections 6 and 8 for further details on the tomography procedures

and on how physical noises map to computational errors in the different encodings used.

More resilient error-correcting codes can be realized by using larger repetition codes $^{14,38,40}$ . We implement such codes using the branched states  $|\mathrm{B}_5\rangle$  and  $|\mathrm{B}_7\rangle$ , equivalent to a three-qubit linear graph where the middle vertex is protected against phase-flip errors via three-qubit and five-qubit repetition codes, respectively. We test the performance of these codes against the uncorrected case  $(|\mathrm{B}_3\rangle)$  by implementing state teleportation of the state  $|+i\rangle = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$  between the two outer (unprotected) qubits of the branched graphs. Figure 3c shows results for the behaviour of the graphs under different fault scenarios. In particular, we first test two different cases: the case with a single error affecting one physical qubit of the logical intermediate layer, and the case with two different physical qubits of the logical intermediate layer undergoing an error (that is two errors in total). In both cases, we test the behaviour for error probabilities  $0 \leq P \leq 1$ , which are implemented by synthetically introducing a continuous  $\hat{Z}$  rotation in the measurements $^{14}$  (Supplementary Section 6). While the repetition codes adopted for the logical qubit in  $|\mathrm{B}_5\rangle$  and  $|\mathrm{B}_7\rangle$  are able to identify and correct up to one and two errors respectively via majority voting resulting in near-unit fidelities $^{4}$ ,  $|\mathrm{B}_3\rangle$  has no way of discerning errors on the intermediate layer and thus the teleported state fidelity decreases for larger error probabilities.

A more practical scenario where all qubits of the intermediate layer are equally affected with error probability  $P$  is reported in Fig. 3d. In all cases, higher redundancies result in an enhanced fidelity of the teleported state, indicating higher tolerance to computational errors. In Supplementary Section 9 we report additional data on how these graph structures can also tolerate photon loss, even in the case where multiple qubits are encoded on each photon.

# Quantum algorithms with error-protected qubits

We used our architecture and device to implement the measurement-based version of PEA, which is a core algorithm in quantum information processing[41-44]. We experimentally investigated a rudimentary form of error correction on a simple version of PEA that does not require entanglement with ancillary qubits[42]. The goal of PEA can be stated as reconstructing a phase  $2\pi \phi_0$  (with  $\phi_0 \in [0,1)$ ) acting on an input quantum state. An iterative version of PEA does so by iteratively inferring—in reverse order—the bits in the binary expansion of  $\phi_0$  using the logical circuit in Fig. 4a, where the rotation angles in the gates  $\varphi = 2\pi M\phi_0$  and  $\theta$  are adaptively chosen during the inference process[45,46].

In the MBQC implementation, the phases  $\varphi$  and  $\theta$  are realized by rotating the measurement bases on the physical qubits in the graph, as shown in Fig. 4b. The protocol can be performed on a three-qubit line graph, which can be realized with either three  $(|\mathrm{L}_3\rangle)$  or six physical qubits  $(|\mathrm{crazy}_6\rangle)$ , as described in Supplementary Section 7. The probabilities of measuring the rightmost qubit in the output 0 or 1, which implies the phase bit 0 or 1, are given by  $P = \cos^2 [\pi (M\phi_0 - \theta)]$  or  $1 - P$ , respectively. Experimental results for error-protected measurement-based PEA, applied to a range of phases with three-bit precision, are shown in Fig. 4c, together with results for physical qubits for comparison. The inference process uses majority voting over a statistical set of 17 samples[44]. While in PEA with physical qubits experimental noise results in observing an incorrect phase reconstruction in 9 of the 24 cases tested (62.5% success rate), using the logical encoding we observe only 1 incorrect phase reconstruction (95.8% success rate). The statistical confidence associated with observing an improvement in the logical case compared with the physical one is 98% (see Supplementary Section 10 for details of the data analysis). Note that, in both physical and error-protected implementations, the experimental resources used are the same (number of photons and number and performance

![](images/c0a8345fb246f2348b278adfc1fa054fea13ab65396d327a42591def1143c068.jpg)  
a

![](images/61e54146cf2e441a9e9e8fe5d071928972dfb8359ee31526a0e067934c7dd823.jpg)

![](images/d7e32c118f2e1db5711f09f8e804d56c8e32687a6f53b88b5be0cd2205c42343.jpg)

![](images/7826c8844fc4da6f16e571ea95c11be8af5477255c43e54a503b4ce50620d25c.jpg)

![](images/e083932d543ee30cf3ed0a2607388f92d3e9bb98c7bf7b0a5af3f92e7a4c724c.jpg)  
b

![](images/d2afd387034a2902ed5abe4a340f12e4d926920d6790cb8706a3eaac4c910e1f.jpg)

![](images/e510f84c3c6e934236ae08ed580bcf5a9a3fdaed23492507ad4c350aa3f48ebd.jpg)  
c, Results for measurement-based error-corrected state teleportation. Branched graph states comprising one-, three- and five-qubit repetition codes are labelled  $\left| {\mathrm{B}}_{3}\right\rangle ,\left| {\mathrm{B}}_{5}\right\rangle$  and  $\left| {\mathrm{B}}_{7}\right\rangle$  ,respectively. Fidelities are reported against increasing probability of a phase error occurring on one and two physical qubits of the code respectively, realized by detuning the measurement basis. Ideal cases are shown as dashed lines. d (as for c), Dephasing errors affecting all physical qubits in the code. Fidelity improvements when increasing the repetition code size are experimentally observed for error rates below the noise threshold  $P = {0.5}$  (up to 14% for  $P = {0.2}$  ),while no benefits are observed above this threshold. All error bars represent the s.e.m., obtained from Monte Carlo simulations assuming a Poissonian distribution of the measured counts.

![](images/8d09c71d50c2466a33e9b6add961533ba649769300daeb8fe17d3406a736dce9.jpg)

![](images/6d6e24b4d3eac9e07b2795457ee300beb540cf9fb3bf7e7d76bb1956929debe6.jpg)

![](images/f36fa733d399ee1d7b352cd174afa73d9dd7d40b45195f62e7a59d318f2f7ef7.jpg)

![](images/336feb54dfe4dbb82690cb5bc0398794439ab67da6b3899d25ab2af5b6a7b2e7.jpg)  
c

![](images/7050d9e23e05f21dd881c0c9b2d565a08347438d1bbcaf9deb8df9548ff50c55.jpg)  
d  
Fig. 3 | MBQC operations with physical and logical graph states. a, Single-qubit operations. The schematics show preparation, unitary gate and readout using a five-qubit linear cluster, together with a circuit model representation. Process tomography data for the  $\hat{X}$ , Hadamard and  $\hat{R}_Z\left(\frac{\pi}{2}\right)$  gates give respective fidelities of  $0.79 \pm 0.06$ ,  $0.98 \pm 0.08$  and  $0.92 \pm 0.06$ , with the ideal cases shown using lighter-coloured regions. Column heights represent the absolute values of the complex matrix entries and phases are colour coded. b, MBQC using physical and logical qubits. Schematics show a single-qubit process using MBQC with three physical qubits (blue frame) and three logical qubits (red frame). Each logical qubit is encoded on two physical qubits to protect against phase-flip errors. Matrices for single-qubit processes implemented with logical-qubit MBQC are shown for four operations; their fidelities  $(F_{\mathrm{L}})$  are compared against those of the same operations implemented with physical qubits  $(F_{\mathrm{p}})$ , where lighter-coloured regions represent error bars.

of gates undergone by each photon): the observed improvement is purely provided by a better way of encoding the quantum information in an error-protection code.

# Hypergraphs

Generalizations of MBQC have recently been proposed based on the more general class of hypergraph states $^{47-49}$ . Hypergraph resources can provide advantages in measurement-based protocols, for

example resource savings and parallelization $^{50-52}$ , protection against correlated errors $^{53}$  and improved noise robustness in quantum metrology applications $^{51}$ . The hypergraph state formalism allows for the presence of higher-order correlations, which are visually represented as loops surrounding vertices, called hyperedges $^{47-49,54}$ . More specifically, a loop around  $k$  qubits labelled  $\{i_1,i_2,\dots,i_k\}$  describes a generalized  $k$ -qubit controlled-phase (CZ) operation,  $\mathrm{C}^k\mathrm{Z}$ , where  $\mathrm{C}^k\mathrm{Z} = \hat{I} - 2|1\dots 1\rangle_{i_1\dots i_k}\langle 1\dots 1|$ . The number of vertices contained

![](images/087da11ddd9d49d4befd2837f6ecdd18bcaf61563d4500ce359017a1375c55b5.jpg)  
a

![](images/f363dc62dc2203993bb9ee7e4113a53601eee4316646077b8241e0343f078e14.jpg)  
b

![](images/518ee076f426c44deda42e6f875caede59dbad4e4560c70b983f2ef551a36ac4.jpg)  
Fig. 4 | Experimental results for MBQC PEA with physical and logical graphs. a,b, Circuit representation of the entanglement-free version of PEA (a), which can be mapped into a MBQC implementation using a three-qubit line graph of physical or logical qubits (b). c, Results for phase estimation of three-bit phases using the physical (top half, black) and logical (bottom half, blue) line graph states. The probability  $P(1)$  of measuring the rightmost logical qubit in the output 1 is plotted, from which we infer the phase bit 0 ( $P(1) < 0.5$ ) or 1 ( $P(1) > 0.5$ ). Failures in the phase estimation are highlighted as red bars, while light-blue bars show the correct bit values.

in a hyperedge defines its cardinality. As for graph states, a (non-local) stabilizer formalism can be introduced for hypergraphs $^{55}$ , which enables state characterization with the same techniques.

Our device can be programmed to generate a variety of hypergraph states of up to five qubits. We test the 'clover' five-qubit hypergraph state, represented in Fig. 5a, which contains two edges of cardinality two and four hyperedges of cardinality three (see Supplementary Section 4 for details). The measured mean of the expectation values of the state's stabilizer generators is  $0.81 \pm 0.02$ , giving an indication of its quality.

Basic working principles of MBQC using hypergraphs can be demonstrated using the clover hypergraph. In particular, we experimentally investigate the action of  $\hat{Z}$  measurements. While in standard MBQC on graph states a  $\hat{Z}$  measurement removes a physical qubit from the graph, up to probabilistic local Pauli gates on the neighbouring vertices, in hypergraphs the resulting probabilistic gates are non-local operations between the vertices sharing a hyperedge with the removed qubit[49,52]. This effect is an essential feature arising from high-order non-local correlations in hypergraphs. For hyperedges of cardinality three, for example those present in the clover hypergraph, an outcome 1 in a  $\hat{Z}$  measurement induces a CZ operation between the two remaining neighbours, while it induces an identity for outcome 0.

This working principle is demonstrated in the results of Fig. 5b,c, where the states resulting from different outcomes of  $\hat{Z}$  measurements on the clover state are characterized. Measuring the central qubit of the clover leads to biseparable states of two Bell pairs, with the connectivity given by the measurement outcome. Experimentally, these have an identical state fidelity of  $0.74 \pm 0.03$ . A three-qubit 'Toffoli' hypergraph with one single hyperedge,

measured stabilizer generators, with  $0.81 \pm 0.02$  mean expectation values.  
b, Effects of measuring the central qubit of the clover state in the  $\hat{Z}$  basis.  
A measurement outcome 1 induces a CZ operation within vertices sharing a hyperedge, resulting in two Bell pairs (1-4) and (3-2), while outcome 0 induces no operations, leaving the two Bell pairs (1-2) and (3-4).

Stabilizer expectation values for the resulting states are shown on the right, providing fidelities  $0.74 \pm 0.03$  and  $0.74 \pm 0.03$ , respectively. c, Effects of measuring two outer qubits of the clover state in the  $\hat{Z}$  basis, leading to the generation of the Toffoli and fully connected Toffoli hypergraphs. Stabilizer measurements provide fidelity estimates of  $0.83 \pm 0.05$  and  $0.80 \pm 0.05$ , respectively. All error bars are obtained assuming a Poissonian distribution of the measured counts.

or a 'fully connected Toffoli' hypergraph, with one three-qubit hyperedge and three regular edges, are obtained by measuring two outer vertices. These states have fidelities of  $0.83 \pm 0.05$  and  $0.80 \pm 0.05$ , respectively.

# Outlook

Although our implementations rely on probabilistic schemes to generate multiphoton states (post-selection and probabilistic entangling gates), the resource savings enabled by our approach could deliver advantages for both noisy intermediate-scale quantum

![](images/fc0ba6b4154a77ccd6cb95f1983dea04f0031db8aaf86c6a7a5f73ed3f0627a7.jpg)  
a

![](images/2102f28afb20f9817ef1a8cda31b2f0b40293bf062461009ee308d29cdb453d9.jpg)

![](images/0c37f9de96982ef015c36519d77d7d296ec80a75b8dc389f2c2e9221010ac099.jpg)  
Fig. 5 | Results for MBQC with hypergraphs. a, Clover hypergraph and  
b

![](images/6f890a2b9a54d89adf8e32b86857a43da0ae6dd85513e2199460d8d719ecb8ee.jpg)

![](images/e867b618e14c84fd12cc20604de9a6bf50055966859177a38ef5f5e88678d546.jpg)  
c

![](images/a94cd86a1ec15c5e0e290fff159cf67b8d69b5d83fb71ab19c2f46a82889d43c.jpg)

![](images/fc74cf97d0a26a330ff6a45ca522f828e51f7828be90c8061e9f3fb733269cba.jpg)

photonic devices in the nearer term, and general-purpose photonic quantum computing architectures over the longer term. The resource savings of high-dimensional encodings open the possibility to develop noisy intermediate-scale quantum systems with  $\geq 40$  photonic qubits, a scale impractical with previous pre-loss-tolerant photonic approaches (Supplementary Section 11). While this method enlarges the entanglement classes accessible with near-term post-selected approaches, it has to be combined with resource-expensive linear optical quantum computing architectures to be used for larger scalable fault-tolerant quantum computation $^{18,19}$ . To reach the scale required for universal photonic MBQC, the adoption of fault-tolerant architectures, in particular loss-resilient photonic schemes, is necessary. Encoding multiple qubits on individual photons allows the encoding of logical qubits that could improve tolerance to logical errors and loss (even if photon loss results in multiple qubits of information being lost) $^{56}$ . Crazy graphs are useful architectural building blocks, as they achieve a photon loss-tolerance threshold arbitrarily close to unity with sufficiently large repetition codes $^{20,39}$ . In our implementation losses are filtered out by post-selection, which precludes a direct exploitation of the loss-resilient properties of the state (Supplementary Section 9).

The bottlenecks of post-selection and probabilistic entangling gates can in principle be addressed with near-deterministic photon generation and gate multiplexing to deliver scalable architectures for photonic quantum computing[19]. While progress in circuits and sources compatible with such architectures is impressive[21,57,58], significant challenges remain. In particular, the integration of detector arrays, low-loss fast switches that are compatible with on-chip sources, and low-latency control electronics are key for developing efficient multiplexing of photon sources and gates. Recent results in thin-film barium titanate on silicon show great potential for the development of on-chip switches for multiplexing, both demonstrating losses below  $0.5\mathrm{dB}$  at speeds of tens of gigahertz[59]. Low-latency feedforward techniques used for multiplexing, possible for example via the integration or interconnection of CMOS (complementary metal-oxide-semiconductor) electronics with the photonic platform, will also enable scaling error-corrected measurement-based quantum photonic operations[19,60].

The results we report provide experimental evidence that error protection can give advantages not only for fault-tolerant machines, but also for near-term applications on pre-fault-tolerant devices. Another way of understanding our results is that we have demonstrated improved process fidelity by increasing the width of optical circuitry for error-protected qubit operation, while maintaining the same optical depth as used for physical qubit operation. Combining recent technological advances in high-dimensional encoding and multiphoton capability with integrated quantum photonics $^{21,61}$ , our architecture can readily provide reconfigurable photonic graph states with tens of qubits.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41567-021-01333-w.

Received: 30 November 2020; Accepted: 19 July 2021

Published online: 27 September 2021

# References

1. Arute, F. et al. Quantum supremacy using a programmable superconducting processor. Nature 574, 505-510 (2019).  
2. Bernien, H. et al. Probing many-body dynamics on a 51-atom quantum simulator. Nature 551, 579 (2017).

3. Preskill, J. Quantum computing in the NISQ era and beyond. Quantum 2, 79 (2018).  
4. Gottesman, D. Stabilizer Codes and Quantum Error Correction. PhD thesis, Californian Institute of Technology (1997).  
5. Aharonov, D. & Ben-Or, M. Fault-tolerant quantum computation with constant error rate. Preprint at https://arxiv.org/abs/quant-ph/9906129 (1999).  
6. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188 (2001).  
7. Raussendorf, R., Browne, D. E. & Briegel, H. J. Measurement-based quantum computation on cluster states. Phys. Rev. A 68, 022312 (2003).  
8. Walther, P. et al. Experimental one-way quantum computing. Nature 434, 169 (2005).  
9. Vallone, G., Pomarico, E., De Martini, F. & Mataloni, P. Active one-way quantum computation with two-photon four-qubit cluster states. Phys. Rev. Lett. 100, 160502 (2008).  
10. Wang, Y., Li, Y., Yin, Z. & Zeng, B. 16-qubit IBM universal quantum computer can be fully entangled. npj Quantum Inf. 4, 1 (2018).  
11. Zwerger, M., Briegel, H. J. & Dür, W. Hybrid architecture for encoded measurement-based quantum computation. Sci. Rep. 4, 5364 (2014).  
12. Raussendorf, R., Harrington, J. & Goyal, K. Topological fault-tolerance in cluster state quantum computation. New J. Phys. 9, 199 (2007).  
13. Schlingemann, D. & Werner, R. F. Quantum error-correcting codes associated with graphs. Phys. Rev. A 65, 012308 (2001).  
14. Lanyon, B. P. et al. Measurement-based quantum computation with trapped ions. Phys. Rev. Lett. 111, 210501 (2013).  
15. Barz, S. et al. Demonstrating elements of measurement-based quantum error correction. Phys. Rev. A 90, 042302 (2014).  
16. Yao, X.-C. et al. Experimental demonstration of topological error correction. Nature 482, 489 (2012).  
17. Bell, B. et al. Experimental demonstration of a graph state quantum error-correction code. Nat. Commun. 5, 1 (2014).  
18. Varnava, M., Browne, D. E. & Rudolph, T. How good must single photon sources and detectors be for efficient linear optical quantum computation? Phys. Rev. Lett. 100, 060502 (2008).  
19. Gimeno-Segovia, M., Shadbolt, P., Browne, D. E. & Rudolph, T. From three-photon Greenberger-Horne-Zeilinger states to ballistic universal quantum computation. Phys. Rev. Lett. 115, 020502 (2015).  
20. Rudolph, T. Why I am optimistic about the silicon-photonic route to quantum computing. *APL Photon.* 2, 030901 (2017).  
21. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285 (2018).  
22. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photon. 11, 447 (2017).  
23. Adcock, J. C., Vigliar, C., Santagati, R., Silverstone, J. W. & Thompson, M. G. Programmable four-photon graph states on a silicon chip. Nat. Commun. 10, 3528 (2019).  
24. Llewellyn, D. et al. Chip-to-chip quantum teleportation and multi-photon entanglement in silicon. Nat. Phys. 16, 1 (2019).  
25. Barreiro, J. T., Langford, N. K., Peters, N. A. & Kwiat, P. G. Generation of hyperentangled photon pairs. Phys. Rev. Lett. 95, 260501 (2005).  
26. Vallone, G., Pomarico, E., Mataloni, P., De Martini, F. & Berardi, V. Realization and characterization of a two-photon four-qubit linear cluster state. Phys. Rev. Lett. 98, 180502 (2007).  
27. Reimer, C. et al. High-dimensional one-way quantum processing implemented on  $d$ -level cluster states. Nat. Phys. 15, 148 (2019).  
28. Zhang, Q. et al. Demonstration of a scheme for the generation of 'event-ready' entangled photon pairs from a single-photon source. Phys. Rev. A 77, 062316 (2008).  
29. Ding, Y., Peucheret, C., Ou, H. & Yvind, K. Fully etched apodized grating coupler on the SOI platform with  $-0.58\mathrm{db}$  coupling efficiency. Opt. Lett. 39, 5348 (2014).  
30. Malik, M. et al. Multi-photon entanglement in high dimensions. Nat. Photon. 10, 248 (2016).  
31. Adcock, J. C., Morley-Short, S., Silverstone, J. W. & Thompson, M. G. Hard limits on the postselectability of optical graph states. Quantum Sci. Technol. 4, 015010 (2018).  
32. Gu, X., Erhard, M., Zeilinger, A. & Krenn, M. Quantum experiments and graphs II: quantum interference, computation, and state generation. Proc. Natl Acad. Sci. USA 116, 4147 (2019).  
33. Gühne, O. & Toth, G. Entanglement detection. Phys. Rep. 474, 1 (2009).  
34. Gross, D., Liu, Y.-K., Flammia, S. T., Becker, S. & Eisert, J. Quantum state tomography via compressed sensing. Phys. Rev. Lett. 105, 150401 (2010).  
35. Sackett, C. A. et al. Experimental entanglement of four particles. Nature 404, 256 (2000).  
36. Wang, X.-L. et al. Experimental ten-photon entanglement. Phys. Rev. Lett. 117, 210502 (2016).  
37. Hein, M., Eisert, J. & Briegel, H. J. Multiparty entanglement in graph states. Phys. Rev. A 69, 062311 (2004).  
38. Nielsen, M. A. & Chuang, I. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2002).

39. Morley-Short, S., Gimeno-Segovia, M., Rudolph, T. & Cable, H. Loss-tolerant teleportation on large stabilizer states. Quantum Sci. Technol. 4, 025014 (2019).  
40. Schindler, P. et al. Experimental repetitive quantum error correction. Science 332, 1059 (2011).  
41. O'Malley, P. J. J. et al. Scalable quantum simulation of molecular energies. Phys. Rev. X 6, 031007 (2016).  
42. Higgins, B. L., Berry, D. W., Bartlett, S. D., Wiseman, H. M. & Pryde, G. J. Entanglement-free Heisenberg-limited phase estimation. Nature 450, 393 (2007).  
43. Friis, N. et al. Flexible resources for quantum metrology. New J. Phys. 19, 063044 (2017).  
44. Paesani, S. et al. Experimental Bayesian quantum phase estimation on a silicon photonic chip. Phys. Rev. Lett. 118, 100503 (2017).  
45. Dobsicek, M., Johansson, G., Shumeiko, V. & Wendin, G. Arbitrary accuracy iterative quantum phase estimation algorithm using a single ancillary qubit: a two-qubit benchmark. Phys. Rev. A 76, 030306 (2007).  
46. Kitaev, A. Y. Quantum measurements and the Abelian stabilizer problem. Preprint at https://arxiv.org/abs/quant-ph/9511026 (1995).  
47. Qu, R., Wang, J., Li, Z.-S. & Bao, Y.-R. Encoding hypergraphs into quantum states. Phys. Rev. A 87, 022311 (2013).  
48. Rossi, M., Huber, M., Bruß, D. & Macchiavello, C. Quantum hypergraph states. New J. Phys. 15, 113022 (2013).  
49. Gühne, O. et al. Entanglement and nonclassical properties of hypergraph states. J. Phys. A 47, 335303 (2014).  
50. Miller, J. & Miyake, A. Hierarchy of universal entanglement in 2D measurement-based quantum computation. npj Quantum Inf. 2, 16036 (2016).  
51. Gachechiladze, M., Budroni, C. & Gühne, O. Extreme violation of local realism in quantum hypergraph states. Phys. Rev. Lett. 116, 070401 (2016).

52. Gachechiladze, M., Gühne, O. & Miyake, A. Changing the circuit-depth complexity of measurement-based quantum computation with hypergraph states. Phys. Rev. A 99, 052304 (2019).  
53. Lyons, D. W. et al. Local Pauli stabilizers of symmetric hypergraph states. J. Phys. A 50, 245303 (2017).  
54. Gachechiladze, M., Tsimakuridze, N. & Gühne, O. Graphical description of unitary transformations on hypergraph states. J. Phys. A 50, 19LT01 (2017).  
55. Morimae, T., Takeuchi, Y. & Hayashi, M. Verification of hypergraph states. Phys. Rev. A 96, 062321 (2017).  
56. LoPiparo, N., Hanks, M., Gravel, C., Nemoto, K. & Munro, W. J. Resource reduction for distributed quantum information processing using quantum multiplexed photons. Phys. Rev. Lett. 124, 210503 (2020).  
57. Wang, H. et al. Towards optimal single-photon sources from polarized microcavities. Nat. Photon. 13, 770 (2019).  
58. Paesani, S. et al. Near-ideal spontaneous photon sources in silicon quantum photonics. Nat. Commun. 11, 1 (2020).  
59. Eltes, F. et al. An integrated cryogenic optical modulator. Preprint at https://arxiv.org/abs/1904.10902 (2019).  
60. Atabaki, A. H. et al. Integrating photonics with silicon nanoelectronics for the next generation of systems on a chip. Nature 556, 349 (2018).  
61. Paesani, S. et al. Generation and sampling of quantum states of light in a silicon chip. Nat. Phys. 15, 925 (2019).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2021

# Data availability

The data that support the plots within this paper and other findings of this study are available at https://doi.org/10.6084/m9.figshare.11903427.

# Acknowledgements

We thank R. Santagati, A. E. Jones, J. F. Bulmer, R. Shaw, D. D. Roberts, J. F. Tasker, N. Maraviglia, J. W. Silverstone, W. A. Murray, Z. Raissi, C. Gogolin and P. Skrzypczyk for useful discussions and technical assistance. We acknowledge support from the Engineering and Physical Sciences Research Council (EPSRC), European Research Council (ERC) and European Commission (EC) funded grants PICQUE, BBOI, QUCHIP, QuPIC, QITBOX, VILLUM FONDEN, QUANPIC (ref. 00025298), the Center of Excellence, Denmark SPOC (ref DNRF123) and ERA-NET cofund initiatives QuantERA within the European Union's Horizon 2020 research and innovation programme grant agreement 731473 (project SQUARE). We acknowledge support from the EPSRC Hubs in Quantum Computing and Simulation (EP/T001062/1) and Networked Quantum Information Technologies (EP/N509711/1). Fellowship support from EPSRC is acknowledged by A.L. (EP/N003470/1).

# Author contributions

C.V., S.P., Y.D., J.W., D.B., M.G.T. and A.L. designed the experiment. J.W. and S.P. designed the integrated circuit. Y.D. fabricated the silicon photonics device. C.V. and S.P. performed the experiment and analysed the data, with theoretical support from J.C.A. and S.M.-S. C.V., S.P., J.C.A. and A.L. wrote the manuscript with feedback from all authors. L.K.O., M.G.T., J.G.R. and A.L. managed the project.

# Competing interests

M.G.T. is involved in developing quantum photonic technologies at PsiQuantum Corporation. The remaining authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41567-021-01333-w.

Correspondence and requests for materials should be addressed to Yunhong Ding, Jianwei Wang or Anthony Laing.

Peer review information Nature Physics thanks the anonymous reviewers for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.