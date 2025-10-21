# Measurement-Based Quantum Computation with Trapped Ions

B. P. Lanyon, $^{1,2,*}$  P. Jurcevic, $^{1,2}$  M. Zwerger, $^{3}$  C. Hempel, $^{1,2}$  E. A. Martinez, $^{1,2}$

W. Dür,³ H. J. Briegel,¹,³ R. Blatt,¹,² and C. F. Roos¹,²

$^{1}$ Institut für Quantenoptik und Quanteninformation, Österreichische Akademie der Wissenschaften,

Technikerstraße 21A, 6020 Innsbruck, Austria

$^{2}$ Institut für Experimentalphysik, Universität Innsbruck, Technikerstraße 25, 6020 Innsbruck, Austria  
<sup>3</sup>Institut für Theoretische Physik, Universität Innsbruck, Technikerstraße 25, 6020 Innsbruck, Austria (Received 3 September 2013; revised manuscript received 21 October 2013; published 19 November 2013)

Measurement-based quantum computation represents a powerful and flexible framework for quantum information processing, based on the notion of entangled quantum states as computational resources. The most prominent application is the one-way quantum computer, with the cluster state as its universal resource. Here we demonstrate the principles of measurement-based quantum computation using deterministically generated cluster states, in a system of trapped calcium ions. First we implement a universal set of operations for quantum computing. Second we demonstrate a family of measurement-based quantum error correction codes and show their improved performance as the code length is increased. The methods presented can be directly scaled up to generate graph states of several tens of qubits.

DOI: 10.1103/PhysRevLett.111.210501

PACS numbers: 03.67.Lx, 03.67.Ac, 03.67.Bg, 37.10.Ty

The circuit model of quantum computation is conceptually similar to a classical computer: a register of two-level systems in a simple initial product state is manipulated using unitary quantum logic gates [1]. Measurement-based quantum computation (MBQC) [2] represents a conceptually and practically different approach: after preparing an entangled state of qubits [3], computation proceeds by performing measurements and feedforward. Any quantum information processing task in the circuit model can be directly mapped to MBQC. However, owing to the two-stage process of MBQC—resource creation followed by its processing—resource states can be manipulated beforehand. This offers a large degree of flexibility in optimizing and compressing measurement-based schemes for quantum information processing. As a result measurement-based entanglement purification [4] and quantum error correction [5,6] schemes have been found with very high noise thresholds, making MBQC a very promising route to fault tolerant quantum computation [7].

Several aspects of MBQC have been demonstrated experimentally using photonic qubits [8-11]. Directly scaling up the nondeterministic methods used to generate entangled states in these works is very challenging, since their success probability reduces exponentially in photon number. Very recently there has been work on generating cluster states in continuous variables of light fields [12].

In this Letter we present a comprehensive first demonstration of MBQC using trapped ions. Furthermore we make the following system-independent steps forward: our cluster state generation methods are deterministic and can be directly scaled up to tens of qubits with existing technology; we demonstrate the principles of measurement-based quantum error correction

(MBQEC)—an essential requirement for a large-scale device. The Letter is organized as follows: First MBQC is briefly reviewed and our approach to preparing cluster states is summarized. Then a universal set of operations is presented using a four-qubit cluster state. Next a MBQEC code is introduced, which can protect an encoded one-qubit state against bit-flip errors. Finally the code is implemented for increasing code word lengths and tested against various noise scenarios. We do not implement active feedforward, which has previously been demonstrated with trapped ions [13,14]. Our results are postprocessed to reproduce the action of perfect feedforward.

A mathematical graph  $G = (V, E)$  is a set of vertices  $V$  and edges  $E$ . The corresponding graph state is a physical state of  $n = |V|$  qubits, associated with the vertices of the graph  $G$ , which is defined in the following way. For every vertex one defines an operator  $K_{a} = X_{a}\prod_{b\in \mathcal{N}(a)}Z_{b}$  where  $\mathcal{N}(a)$  denotes the neighborhood of vertex  $a$  and  $X$  and  $Z$  denote Pauli spin-  $\frac{1}{2}$  operators. The graph state  $|G\rangle$  is uniquely defined as the common eigenstate of all operators  $K_{a}$  with eigenvalue  $+1$ . One approach to generating graph states is to start from an initial state with all qubits in  $|+ \rangle$ , i.e., the  $+1$  eigenstate of  $X$ , and then apply a controlled phase, CP, gate [1] between every pair of qubits connected by an edge.

An important graph state is the 2D cluster state  $|C\rangle$  [3], which has the topology of a square lattice and belongs to the class of universal resource states [15,16]. Any quantum computation can be carried out on a sufficiently large  $|C\rangle$ . In particular, any quantum logic circuit can be translated to a single-qubit-measurement pattern on  $|C\rangle$  [3]. Measurements in the computational basis can be used to remove qubits from the cluster and imprint any desired

quantum circuit structure onto the lattice. Measurements in the basis  $B(\alpha) = (| + \alpha \rangle, | - \alpha \rangle)$ , where  $| \pm \alpha \rangle = (|0\rangle \pm e^{i\alpha} |1\rangle) / \sqrt{2}$  with real  $\alpha$ , drive the computation. The value of  $\alpha$  determines, for example, the angle of single-qubit rotations. In general  $\alpha$  has to be adapted to the outcomes of previous measurements and thus introduces a temporal order and the need for feedforward [2].

Our experiments use strings of  $^{40}\mathrm{Ca}^{+}$ ions in a linear Paul trap [17,18]. Two electronic states encode a qubit  $(|D_{5/2}, m = +3/2\rangle = |0\rangle$ ,  $|S_{1/2}, m = +1/2\rangle = |1\rangle)$  and they are coupled by an electric quadrupole transition at 729 nm. We now briefly summarize how graph states are generated (for more details see the Supplemental Material [19]). Experiments begin by preparing  $n$  ionic qubits in the state  $|1\rangle^{\otimes n}$  via optical pumping, and preparing the axial center-of-mass (c.m.) and stretch (STR) vibrational modes in the ground state by resolved sideband cooling. Graph states are generated using three distinct tools. First an effective long-range qubit-qubit interaction of the form  $H_{\mathrm{MS}} = J\sum_{a < b}X_{a}X_{b}$  can be turned on for arbitrary times. This interaction is realized by off-resonantly driving the axial c.m. vibrational mode of the ion string using a bichromatic laser field from a single direction [18,20]. When applied to ionic qubits in  $|1\rangle^{\otimes n}$  this periodically generates fully connected graph states that are equivalent to GHZ states [21,22]. The second and third tools enable the selective removal of any connection in the graph [13,23]. Both use laser pulses tightly focused on individual ions. In combination these three tools allow, in principle, any cluster state to be deterministically created.

In the circuit model of quantum computation a universal set of logic gates provides the tools to implement arbitrary quantum algorithms [1]. A common universal gate set consists of the CP gate and arbitrary single-qubit rotations around two independent axes, e.g., the  $Z$  axis  $R_Z(\alpha) = e^{-i(\alpha /2)Z}$  and the  $X$  axis  $R_{X}(\alpha) = e^{-i(\alpha /2)X}$ , by angle  $\alpha$  [1]. All of these gates can be translated to carrying out specific sequences of measurements and feedforward on a four-qubit linear cluster state  $|LC_4\rangle$ , which are presented in Figs. 1(a) and 2(a) [8]. Realizing measurement patterns like these on large-scale cluster states, when combined with quantum error correction (QEC), enables arbitrary MBQC [2]. We create  $|LC_4\rangle$  using a laser pulse sequence lasting  $300~\mu \mathrm{s}$  and reconstruct the full density matrix via quantum state tomography (see the Supplemental Material [19] for details). The observed fidelity with the ideal state is  $0.841\pm 0.006$ , which is well above the threshold for witnessing multipartite entanglement of 0.5 [24].

Measurement of  $|LC_4\rangle$  in the order presented in Fig. 1 is equivalent to a circuit performing a sequence of one-qubit gates on the encoded state  $| + \rangle$ . The choice of measurement basis of qubits 1, 2, and 3  $[B_{1}(\alpha), B_{2}(\beta),$  and  $B_{3}(\gamma)]$  determines the overall rotation applied to  $| + \rangle$ . We implement a range of measurement combinations, each demonstrating a different one-qubit rotation. One approach,

![](images/62648f0994cb4a10bdaac3746381816c1861ab49779ee5cabb801a1a18af7e3d.jpg)

![](images/a194f16db375fdf1a2e42a326a4eb590ea32b400ff69fa924e460b5cb48c1d95.jpg)  
FIG. 1 (color online). Demonstration of one-qubit gates via measurement-based quantum computing. (a) Cluster state  $|LC_4\rangle$ . Qubits 1, 2, and 3 are measured consecutively in the basis  $B_{1}(\alpha)$ ,  $B_{2}(\pm \beta)$ , and  $B_{3}(\pm \gamma)$ . (b) Equivalent quantum circuit. Rotation angles  $\alpha$ ,  $\beta$ , and  $\gamma$ . Hadamard  $(H)$  [1]. (c) Ideal output states on the Bloch sphere for  $[\alpha, \beta, \gamma] = [\pi/2, 0, 0]$  (red,  $| - y \rangle$ ), [0, 0,  $-\pi/2]$  (green,  $| + y \rangle$ ),  $[\pi/2, -\pi/2, 0]$  (blue,  $| - x \rangle$ ),  $[\pi/2, 0, -\pi/2]$  (cyan,  $|0 \rangle$ ),  $[\pi/4, 0, 0]$  [magenta]. (d) Experimentally measured states; the average fidelity with the ideal cases is  $0.92 \pm 0.01$ . Gray extrapolations show nearest pure state.

![](images/c963ba6bacb6bd99ebaf87ce2889d9612d7f900411df584f5bbcef5565674d0a.jpg)

![](images/602d9791ea13045211e91e79dcf14b9eff589b3dd0b146cd0bd73d1b95785cc1.jpg)

which avoids the need for active feedforward, is to reconstruct the output state (encoded in qubit 4) postselected on the cases where the  $+1$  outcomes of the measurement of qubits 1, 2, and 3 are observed, as in Ref. [8]. More information is obtained if all outcomes are kept and postprocessed to simulate perfect feedforward. Results obtained in this way provide an upper limit for the performance that could have been achieved using feedforward. Figure 1 presents the results on the Bloch sphere: a range of rotated one-qubit output states, reconstructed via quantum state tomography. The average output state fidelity with the ideal case is  $0.92 \pm 0.01$ .

Measurement of  $|LC_4\rangle$  in the order presented in Fig. 2 is equivalent to a circuit composed of a CP gate and one-qubit rotations, which operates on the encoded state two-qubit state  $|++\rangle$ . We choose two important cases: a maximally entangled state (case 1) and a product state (case 2) are ideally created. The generated entanglement is quantified by the tangle  $\tau$  [25]. In case 1 we find that the experimentally reconstructed state is strongly entangled,  $\tau = 0.59 \pm 0.05$ , and has a fidelity of  $0.88 \pm 0.02$  with the ideal state. In case 2 the experimental state is close to being separable,  $\tau = 0.02 \pm 0.01$ , and has a fidelity of  $0.83 \pm 0.01$  with the ideal state. Experimentally reconstructed two-qubit output density matrices are presented in Fig. 2. Taken together, the results in Figs. 1 and 2 demonstrate a universal set of operations for MBQC.

In a realistic setup one cannot decouple the qubits on which the computation is performed completely from the environment, which will introduce errors on the qubits. QEC codes [1,26,27] provide a solution by encoding the states  $|0\rangle$  and  $|1\rangle$  of a qubit into the states of larger physical

![](images/46f34db324fd6c204caae13fd5a00dc687fabe74fa8d253664a071a15a7c297c.jpg)  
(a)  
(b)

![](images/516e02bcaeaa00fe12d2890b2fe370ae8f83c15bf3d97d2aa8e06063f0627793.jpg)

![](images/7129783112521bac09d4496c14ee8e43e2f7a234b4aab1bbba2897a9b120ee32.jpg)  
(c)  
(d)

![](images/37c2478cfd6c5b72e8fb7da9c81b3ed7029a043eb2a4eae964dc0c49a254b436.jpg)  
FIG. 2 (color online). Demonstration of two-qubit gates via measurement-based quantum computing. (a) Qubits 1 and 4 of cluster state  $|LC_4\rangle$  are measured in the basis  $B_{1}(\alpha)$  and  $B_{4}(\beta)$ , respectively. Qubits 2 and 3 encode the output state. (b). Equivalent quantum circuit, with angles determined by  $\alpha$  and  $\beta$ . Final element is a CP gate. (c)-(d). Experimental output state density matrices (left and right; real and imaginary parts, respectively) in two cases: (c) an entangled state for  $\alpha = \pi /2$ ,  $\beta = -\pi /2$ , with fidelity  $0.88\pm 0.02$ , and tangle  $0.59\pm 0.05$ , and (d) an ideally separable state for  $\alpha = 0$ ,  $\beta = 0$ , with fidelity  $0.83\pm 0.01$  and tangle  $0.02\pm 0.01$ .

![](images/bb93f7a1ece965bc73ad2eefbd8c8c22149f762551d67cf4545b2df0ee309f86.jpg)

![](images/dbe008b8d972fccdd7a8997ef788a18892de4ba412cf0abcde4ecd393717fb03.jpg)

systems  $|0_L\rangle$  and  $|1_L\rangle$  (called code words or logical qubits) and using correlations to protect the information. QEC consists of at least two steps after the encoding. First one measures the correlation operators which reveal the error syndrome. In this step errors, which might be unitary qubit rotations or involve entangling to the environment, are discretized. The discretization of the errors is a crucial step, as it reduces the infinite set of possible quantum errors to a finite set. Second, one applies the recovery operator to undo the error. The principles of QEC in the circuit model have been demonstrated before [28-32], including the three-qubit phase-flip code [33]. Circuit model QEC codes can be translated to MBQC in the same way as algorithms. However it is important to note that QEC codes involve only Clifford gates and Pauli measurements and these can be implemented in a very compact way in MBQC [6].

We demonstrate a MBQC phase-flip code, with code words  $|0_L\rangle = | + \rangle^{\otimes n}$  and  $|1_L\rangle = |- \rangle^{\otimes n}$ , capable of correcting full phase flips  $(Z)$  on up to  $(n - 1)/2$  of the code word qubits. The general form of the graph state employed, labeled  $|EC_n\rangle$ , and the protocol are presented in Fig. 3.  $|EC_n\rangle$  consists of  $n + 2$  qubits:  $n$  for the code word, labeled  $C_1$  to  $C_n$ , and two additional qubits  $A$  and  $B$  to read in (encode) and read out the initial and final protected one-qubit state, respectively. After preparation of  $|EC_n\rangle$ , the protocol proceeds as follows: (1) A one-qubit state  $|\psi \rangle$ , or the orthogonal state, is encoded by measuring qubit  $A$  in a basis where these are the eigenstates. The effect is to distribute either state nonlocally amongst the remaining  $(n + 1)$  qubits. (2) Each of the  $n$  central qubits  $C_n$  is measured in the  $X$  basis, yielding one of  $2^n$  possible outcomes. This simultaneously decodes the state and reveals which of up to  $(n - 1)/2$  errors have occurred on the

![](images/af285f54fa0f0fb5367cf98676030571a5e581b923ed7e98abc5b63456b7d859.jpg)  
FIG. 3 (color online). Graph state  $|EC_{n}\rangle$  and its use in measurement-based quantum error correction. (a)  $(n + 2)$ -qubit graph state  $|EC_{n}\rangle$  and protocol, which can correct for phase-flip errors  $(Z)$  occurring on up to  $(n - 1)/2$  of qubits  $C_{1}$  to  $C_{n}$ . Ideally an encoded one-qubit state is perfectly teleported across the cluster, from  $A$  to  $B$ . (b) Conceptually equivalent quantum logic circuit.

![](images/2e2e4959e92ad557d780e646af6b43aa84266a0c50746bd5b9ba021913e9f186.jpg)

central qubits (i.e., determines the error syndrome). (3) A one-qubit correction operation, determined by the outcome in (2) is applied to the output state, stored in qubit  $B$ , recovering the encoded one-qubit state.

The temporal order of the measurements is unimportant and errors can happen to the central qubits  $C_1$  to  $C_n$  at any time before they are measured. It is useful to interpret the protocol as attempting to teleport a state across the graph, from  $A$  to  $B$ , through a noisy channel affecting the middle qubits.

We demonstrate the protocol using the  $n = 1, 3,$  and 5 cases shown in Figs. 4(a)–4(c). Equivalent experimental investigations of increasing code word lengths in the circuit model have not yet been realized, due to the complexity of the gate sequences required. The laser-pulse sequences used to generate each graph are described in the Supplemental Material [19]. For the  $n = 1$  and 3 cases we reconstruct the full  $(n + 2)$ -qubit density matrices via

![](images/717b1c787fe5922c3013055e7cbc577d8b2667471be97ede430fdf4630ab9e7e.jpg)

![](images/c0fdbee3e4fd5728fcef210239d933de9642933ceec911eb9cb99a9cb4f3c480.jpg)

![](images/4966a77b0f953532c607d58ae7494ee35f03e44af27b1acd261faec93c39afd8.jpg)

![](images/73722751b6bc84a9e5f249a27871216b604e62edcc1834182084e6dbfee77bd4.jpg)  
FIG. 4 (color online). Quantum error correction performance against errors on subsets of codeword qubits. (a) to (c). Graph states  $|EC_{n}\rangle$  for  $n = 1,3$  and 5, respectively. Errors are applied to qubits in blue. (d) Solid blue line: ideal case in (a). Experimental results for cases (a)-(c) are shown as blue diamonds, red squares and grey inverted triangles (two errors), respectively. Black circles show case (c) for only a single error applied to  $C_1$ . For more details see supplementary material. Errors are one standard deviation and derived from quantum projection noise.

quantum state tomography, yielding state fidelities of  $0.92 \pm 0.005$  and  $0.843 \pm 0.005$ , respectively.

The codes are tested against errors realized by applying one-qubit rotations  $R_{z} = \exp (-i(\theta /2)Z)$  to all or a subset of the code word qubits  $C_n$ . After measurement of  $C_n$  (and therefore discretization of the errors) this is equivalent to independent phase flips occurring incoherently and independently on those qubits to which rotations are applied, with probability  $p = \sin^2 (\theta /2)$ . For input states we choose to encode the four eigenstates of the Pauli  $X$  and  $Y$  operators, which are maximally affected by phase-flip errors. Error correction performance is quantified by the teleportation state fidelity, through the noisy channel, averaged over the four input states.

First each code is tested against errors applied to one code word qubit  $(C_1)$ . The  $n = 3$  and 5 graphs should be robust to this, whilst the average teleportation fidelity for the  $n = 1$  graph should reduce linearly with  $p$ , since it provides no error correction. The results, presented in Fig. 4, show quantitative agreement with the ideal cases, up to deviations that largely correspond to an overall fidelity drop due to imperfections in the graph state preparation. Also shown is the resistance against two errors  $(C_1$  and  $C_2)$  for the  $n = 5$  case, afforded by the increased code word length. We emphasize the quality of the results: even in the presence of a large amount of noise we are able to teleport states across a 7 ionic-qubit string with fidelities of over 0.8.

These diagnostic tests show that the experimentally generated graph states respond correctly to errors applied to individual code word qubits. A more realistic situation is that all code word qubits are subject to error with the same probability. Figure 5(d) shows the theoretical performance of the ideal graphs against such noise: for  $p < 0.5$ , graphs with larger  $n$  perform better, tending towards perfect correction up to  $p = 0.5$  as  $n \to \infty$ .

Errors are applied to all physical code word qubits in the experimentally generated graph states and the results are presented in Fig. 5(e). Qualitative agreement with the ideal case is observed. Even though many more qubits are exposed to errors in the larger code words, there is still a region where they perform better. That is, we are able to demonstrate that, for a range of noise levels, a better protection of quantum information is provided when using a larger error correction code. For more discussion see the Supplementary Material [19].

We have made several distinct steps forward in MBQC: the deterministic generation of graph states, together with their application as resources; the demonstration of measurement-based quantum error correction; and the observation of improved performance with increasing code word length. Both the circuit and measurement-based models of quantum computation have now been demonstrated in trapped ions. There is as yet no obvious reason to favor one over the other at this stage. In the short term,

![](images/3c022ac0150ff7bb0ac911c70c622b6178a63cd511a1ea8fe39f9fe1ac8e87cc.jpg)

![](images/63e1279b7600c0d1b8071d13e4b645832cfaee4f9cc09ef1069b4eff3b24f39b.jpg)

![](images/85adb7a3aa743ebdf6d89c7076f6f7dc9b85e3a721e9cbd00c14d6db6ba16c0f.jpg)  
FIG. 5 (color online). Quantum error correction performance against errors on all code word qubits. (a)-(c). Graph states  $|EC_{n}\rangle$  for  $n = 1,3,$  and 5, respectively. Errors are applied to qubits in blue. (d) Ideal performance for cases (a)-(c) shown as solid blue, red, and black lines, respectively. Increasing the code word length  $(n)$  improves performance for  $p < 0.5$ . (e) Experimental results for cases (a)-(c) shown as blue diamonds, red squares, and black triangles, respectively. Errors are one standard deviation and derived from quantum projection noise.

![](images/f61dd7d77a2c520651b8673f4e2ee93fcd6b4e2569623585baf3c5c7fd2eaf42.jpg)

![](images/8feb45167b4507226707722dd479bdb0e76458a3070cd888235890d6afd65bd0.jpg)

scaling up MBQC will require more emphasis on fast state detection and feedforward. MBQEC of arbitrary errors is possible using more complicated graph states.

B.P.L. acknowledges support by a Marie Curie Fellowship (PIIF-GA-2010-275477). This work was supported by the Austrian Science Fund (FWF) under Grants No. P25354-N20, No. P24273-N16, and No. SFB F40-FoQus.

*Corresponding author. ben.lanyon@uibk.ac.at

[1] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2000).  
[2] R. Raussendorf and H. J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[3] H.J. Briegel and R. Raussendorf, Phys. Rev. Lett. 86, 910 (2001).  
[4] M. Zwerger, H.J. Briegel, and W. Dür, Phys. Rev. Lett. 110, 260503 (2013).  
[5] E. Knill, Nature (London) 434, 39 (2005).  
[6] M. Zwerger, H.J. Briegel, and W. Dür, arXiv:1308.4561.  
[7] R. Raussendorf and J. Harrington, Phys. Rev. Lett. 98, 190504 (2007).  
[8] P. Walther, K.J. Resch, T. Rudolph, E. Schenck, H. Weinfurter, V. Vedral, M. Aspelmeyer, and A. Zeilinger, Nature (London) 434, 169 (2005).  
[9] R. Prevedel, P. Walther, F. Tiefenbacher, P. Bohi, R. Kaltenbaek, T. Jennewein, and A. Zeilinger, Nature (London) 445, 65 (2007).  
[10] X.-C. Yao, T.-X. Wang, H.-Z. Chen, W.-B. Gao, A.G. Fowler, R. Raussendorf, Z.-B. Chen, N.-L. Liu, C.-Y. Lu, Y.-J. Deng et al., Nature (London) 482, 489 (2012).

[11] S. Barz, E. Kashefi, A. Broadbent, J.F. Fitzsimons, A. Zeilinger, and P. Walther, Science 335, 303 (2012).  
[12] S. Yokoyama, R. Ukai, S.C. Armstrong, C. Sornphiphatphong, T. Kaji, S. Suzuki, J.-i. Yoshikawa, H. Yonezawa, N.C. Menicucci, and A. Furusawa, arXiv:1306.3366.  
[13] M. Riebe, H. Häffner, C. F. Roos, W. Hänsel, J. Benhelm, G. P. T. Lancaster, T. W. Körber, C. Becher, F. Schmidt-Kaler, D. F. V. James et al., Nature (London) 429, 734 (2004).  
[14] M. Riebe, T. Monz, K. Kim, A. S. Villar, P. Schindler, M. Chwalla, M. Hennrich, and R. Blatt, Nat. Phys. 4, 839 (2008).  
[15] M. Van den Nest, A. Miyake, W. Dur, and H.J. Briegel, Phys. Rev. Lett. 97, 150504 (2006).  
[16] M. V. den Nest, W. Dur, A. Miyake, and H. J. Briegel, New J. Phys. 9, 204 (2007).  
[17] P. Schindler, D. Nigg, T. Monz, J. T. Barreiro, E. Martinez, S. X. Wang, S. Quint, M. F. Brandl, V. Nebendahl, C. F. Roos, M. Chwalla et al., arXiv:1308.3096.  
[18] G. Kirchmair, J. Benhelm, F. Zähringer, R. Gerritsma, C.F. Roos, and R. Blatt, New J. Phys. 11, 023002 (2009).  
[19] See the Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevLett.111.210501 for experimental details including: laser pulse sequences, experimental techniques, and data analysis techniques. Additional results and analysis including: experimentally reconstructed graph state density matrices.  
[20] A. Sørensen and K. Mølmer, Phys. Rev. Lett. 82, 1971 (1999).

[21] T. Monz, P. Schindler, J. T. Barreiro, M. Chwalla, D. Nigg, W. A. Coish, M. Harlander, W. Hänsel, M. Hennrich, and R. Blatt, Phys. Rev. Lett. 106, 130506 (2011).  
[22] K. Mølmer and A. Sørensen, Phys. Rev. Lett. 82, 1835 (1999).  
[23] V. Nebendahl, H. Häffner, and C. F. Roos, Phys. Rev. A 79, 012312 (2009).  
[24] G. Toth and O. Gühne, Phys. Rev. Lett. 94, 060501 (2005).  
[25] V. Coffman, J. Kundu, and W. K. Wootters, Phys. Rev. A 61, 052306 (2000).  
[26] A.R. Calderbank and P.W. Shor, Phys. Rev. A 54, 1098 (1996).  
[27] A. Steane, Proc. R. Soc. A 452, 2551 (1996).  
[28] D.G. Cory, M.D. Price, W. Maas, E. Knill, R. Laflamme, W.H. Zurek, T.F. Havel, and S.S. Somaroo, Phys. Rev. Lett. 81, 2152 (1998).  
[29] J. Chiaverini, D. Leibfried, T. Schaetz, M.D. Barrett, R.B. Blakestad, J. Britton, W.M. Itano, J.D. Jost, E. Knill, C. Langer et al., Nature (London) 432, 602 (2004).  
[30] T. B. Pittman, B.C. Jacobs, and J. D. Franson, Phys. Rev. A 71, 052332 (2005).  
[31] M.D. Reed, L. DiCarlo, S.E. Nigg, L. Sun, L. Frunzio, S.M. Girvin, and R.J. Schoelkopf, Nature (London) 482, 382 (2012).  
[32] J. Zhang, R. Laflamme, and D. Suter, Phys. Rev. Lett. 109, 100503 (2012).  
[33] P. Schindler, J.T. Barreiro, T. Monz, V. Nebendahl, D. Nigg, M. Chwalla, M. Hennrich, and R. Blatt, Science 332, 1059 (2011).