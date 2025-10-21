# Experimental demonstration of topological error correction

Xing-Can Yao $^{1}$ , Tian-Xiong Wang $^{1}$ , Hao-Ze Chen $^{1}$ , Wei-Bo Gao $^{1}$ , Austin G. Fowler $^{2}$ , Robert Raussendorf $^{3}$ , Zeng-Bing Chen $^{1}$ , Nai-Le Liu $^{1}$ , Chao-Yang Lu $^{1}$ , You-Jin Deng $^{1}$ , Yu-Ao Chen $^{1}$  & Jian-Wei Pan $^{1}$

Scalable quantum computing can be achieved only if quantum bits are manipulated in a fault-tolerant fashion. Topological error correction—a method that combines topological quantum computation with quantum error correction—has the highest known tolerable error rate for a local architecture. The technique makes use of cluster states with topological properties and requires only nearest-neighbour interactions. Here we report the experimental demonstration of topological error correction with an eight-photon cluster state. We show that a correlation can be protected against a single error on any quantum bit. Also, when all quantum bits are simultaneously subjected to errors with equal probability, the effective error rate can be significantly reduced. Our work demonstrates the viability of topological error correction for fault-tolerant quantum information processing.

Quantum computers exploit the laws of quantum mechanics and can solve many problems exponentially more efficiently than their classical counterparts $^{1-3}$ . However, in the laboratory the ubiquitous decoherence of quantum states makes it notoriously hard to achieve the required high degree of quantum control. To overcome this problem, quantum error correction has been invented $^{4-6}$ . The principal result in quantum error correction, the threshold theorem $^{7,8}$ , states that as long as the error rate,  $p$ , per gate in a quantum computer is smaller than a threshold value,  $p_{c}$ , arbitrarily long and accurate quantum computation is efficiently possible. However, most methods of fault-tolerant quantum computing with a high threshold error rate  $(10^{-4}-10^{-2})$  require strong and long-range interactions $^{7-9}$ , and are thus difficult to implement. Local architectures are normally associated with much lower thresholds. For traditional concatenated codes on a two-dimensional lattice of quantum bits (qubits) with nearest-neighbour gates, the highest threshold known at present $^{10}$  is  $2.02 \times 10^{-5}$ .

In such lattices, it is advantageous to use topological error correction $^{11-15}$  (TEC) in the framework of topological cluster-state quantum computing. This scheme makes use of the topological properties in three-dimensional (3D) cluster states, which form an inherently error-robust 'fabric' for computation. Local measurements drive the computation and, at the same time, implement the error correction. Active error correction and topological methods are combined, yielding a high error threshold $^{12,13}$  of  $0.7 - 1.1\%$  and tolerating loss rates $^{15}$  up to  $24.9\%$ . This allows for the unavoidable imperfections of physical devices, and makes our implementation of TEC close to the experimental state of the art. For practical quantum computation with TEC, a larger cluster state of more qubits would be needed. The 3D architecture can be further mapped onto a local setting in two spatial dimensions plus time $^{14}$ , also with nearest-neighbour interactions only. Two detailed architectures have already been proposed $^{16,17}$ . We note that a different topological scheme has been proposed in which quantum computation is driven by non-Abelian anyons $^{18,19}$  and fault tolerance is achieved through passive stabilization afforded by a ground-state energy gap.

Some simple quantum error correction codes have been experimentally demonstrated in nuclear magnetic resonance $^{20,21}$ , ion

traps $^{22,23}$  and optical systems $^{24,25}$ . However, the experimental realization of topological quantum error correction methods remains challenging. At present, multipartite cluster states can be generated with up to six photons and work is under way to create non-Abelian anyons for topological quantum computing $^{18,19}$ . Here we develop an ultrabright entangled-photon source by using an interferometric Bell-type synthesizer. With this and a noise-reduction interferometer, we generate a polarization-encoded eight-photon cluster state, which is shown to possess the required topological properties for TEC. In accordance with the TEC scheme, we measure each photon (qubit) locally. Error syndromes are constructed from the measurement outcomes, and one topological quantum correlation is protected. We demonstrate that if only one physical qubit suffers an error, the faulty qubit can be located and corrected, and that if all qubits are simultaneously subjected to errors with equal probability, the effective error rate is significantly reduced by error correction. This constitutes a proof-of-principle experiment that demonstrates the viability of TEC, a central ingredient in topological cluster-state computing.

# Cluster states and quantum computing

In cluster-state quantum computing $^{26}$ , projective one-qubit measurements replace unitary evolution as the elementary process driving a quantum computation. The computation begins with a highly entangled multi-qubit state, the 'cluster state'  $|G\rangle$  (ref. 27), which is specified by an interaction graph,  $G$ , and can be created from a product state through the pairwise Ising interaction over the edges in  $G$ . For each vertex  $i \in G$ , we define a stabilizer as  $K_i \equiv X_i \otimes_{e_{ij}} Z_j$  where the product is over all the interaction edges,  $e_{ij}$ , connecting vertex  $i$  to its nearest-neighbouring vertices,  $j$ . The symbols  $X_i$  and  $Z_j$  denote the bit- and phase-flip Pauli operators, respectively, acting on qubits  $i$  and  $j$ . State  $|G\rangle$  is the unique joint eigenstate of a complete set of stabilizers  $K_i$  such that  $K_i |G\rangle = |G\rangle$  for all  $i \in G$ .

Cluster states in  $d \geq 3$  dimensions are resources for universal fault-tolerant quantum computing $^{12}$ , in which the TEC capability—shared with Kitaev's toric code $^{11,28}$  and the colour code $^{29}$ —is combined with the capability to process quantum information.

# Topological error correction

Quantum error correction and fault-tolerant quantum computing are possible with cluster states whenever the underlying interaction graph can be embedded in a 3D cell structure known as a cell complex $^{30}$ , which consists of volumes, faces, edges and vertices. Qubits are encoded on the edges and faces of a cell complex. The associated interaction graph connects the qubit on each face to the qubits on its surrounding edges through the interaction edges. Consider the elementary cell complex in Fig. 1a, shown by the dashed lines: it has one cubic volume, six square faces, twelve edges and eight vertices. The interaction edges, represented by the solid lines, form an 18-qubit cluster state,  $|G_{18}\rangle$ . There are six face stabilizers,  $K_{f}(f = 1,2,\dots,6)$ . It follows that multiplication of these stabilizers cancels out all  $Z$  operators in  $K_{f}$  and thus yields a unit expectation value:  $\langle X_1X_2\dots X_6\rangle = 1$ . This leads to the straightforward but important observation that despite the  $X$  measurement on each individual face qubit having the random outcome  $\pm 1$ , the product of all the outcomes on any closed surface,  $F$ , is  $+1$ . That is, any closed surface has the topological quantum correlation  $C_F\equiv \langle \otimes_{f\in F}X_f\rangle = 1$ , where  $f$  is a face of  $F$ .

A larger cell complex is displayed in Fig. 1b, which encodes and propagates a logical qubit. It consists of  $5 \times 5 \times T$  cells, where  $T$  specifies a span of simulated time (t). A 'defect' along the  $t$  direction (Fig. 1b, line of green dots) is first produced by performing local  $Z$  measurements. Then the topological quantum correlation,  $C_{F_D} = 1$ , on a defect-enclosing closed surface  $(F_D)$ , combined with the boundary, is used to encode a logical qubit. The evolution of the logical state from  $t_1$  to  $t_2$  is achieved by local  $X$  measurements on all other physical qubits between  $t_1$  and  $t_2$  (see ref. 31 for details). Quantum computing requires a much larger cell complex and more defects, where quantum algorithms are realized by appropriate braiding-like manipulation of defects (a sketch of the logical controlled-NOT gate is shown in Supplementary Information).

The quantum computation is possible because the topological quantum correlation  $C_{F_D} = 1$  holds on defect-enclosing closed surfaces. The TEC capability arises from the  $\mathbf{Z}_2$  homology, a topological feature, of a sufficiently large 3D cell complex (Supplementary Information). For a given  $F_{D}$ , there exist many homologically equivalent closed surfaces with the same topological correlation  $(C_{F_D} = 1)$ . This redundancy leads to the topological protection of the correlation<sup>12</sup>.

Remarkably, in TEC it is sufficient to deal with  $Z$  errors, because an  $X$  error either has no effect, if it occurs immediately before an  $X$  measurement, or is equivalent to multiple  $Z$  errors. Finally, as TEC is implemented in topological cluster-state quantum computing—a

![](images/a8eb24f7a674f45dee4a0ec95def5a6737ddb3e8b7d632ef486da3f531ceb82c.jpg)  
Figure 1 | Topological cluster states. a, Elementary lattice cell. Dashed lines represent the edges of the associated cell complex and solid lines represent the edges of the interaction graph. Qubits (spheres) are encoded on the faces and edges of the elementary cell. b, Larger topological cluster state of  $5 \times 5 \times T$  cells. Green dots represent local  $Z$  measurements, which effectively remove the measured qubits from the cluster state and thereby create a non-trivial topology capable of supporting a single correlation. Red dots represent  $Z$  errors. Red cells indicate the ends of error chains where  $C_F = -1$ . One axis of the cluster can be regarded as simulating the 'circuit time',  $t$ . The evolution of logical states from  $t_1$  to  $t_2$  is achieved by performing local  $X$  measurements on all physical qubits between  $t_1$  and  $t_2$ .

![](images/756a245d45af9dcfffb43ca948bcf041bd6cca36a7d234ab0ef8aa218f51b7b4.jpg)

measurement-based process—corrections suggested by TEC are not applied to the remaining cluster state but rather to the classical outcomes of  $X$  measurements.

# Simpler topological cluster state

The cell complex in Fig. 1b encodes a propagating logical qubit in terms of one topological correlation,  $C_{F_D} = 1$ , and is robust against a local  $Z$  error. However, it contains 25 elementary cells and 180 physical qubits for each layer of complex over a unit time span, which is beyond the capacity of available experimental techniques. We design a simpler graph state,  $|G_8\rangle$  (Fig. 2a), to mimic the cell complex of Fig. 1b.

The topological feature of  $|G_8\rangle$  can be seen from its association with the 3D cell complex in Fig. 2b, which consists of four elementary volumes,  $\{v,w,y,z\}$ ; six faces,  $\{f_1,f_2,f_3,f_4,f_5,f_6\}$ ; two edges,  $\{e_7,e_8\}$ ; and two vertices,  $\{s,t\}$ . All six faces have the same boundary,  $e_7\cup e_8$ , and any two of them form a closed surface,  $F$ . The centre volume is removed to resemble the defect in Fig. 1b, and the topological correlation to be protected,  $C_{F_D}$ , reads

$$
C _ {F _ {D}} \equiv \left\langle X _ {5} X _ {6} \right\rangle = 1 \tag {1}
$$

In this simple cell complex, the topological correlation  $C_{F_D} = 1$  is already multiply encoded: it is represented by any expectation  $\langle X_iX_j\rangle$  with  $i\in \{1,2,5\}$  and  $j\in \{3,4,6\}$ . Moreover, there exist four other closed surfaces, corresponding to the respective boundaries of the volumes  $\{\nu ,w,y,z\}$ , that do not enclose the defect. The 'redundant' topological correlations are

$$
\left\langle X _ {1} X _ {2} \right\rangle = \left\langle X _ {2} X _ {5} \right\rangle = \left\langle X _ {3} X _ {6} \right\rangle = \left\langle X _ {3} X _ {4} \right\rangle = 1 \tag {2}
$$

These can be used as error syndromes in TEC, which makes one or more of them equal to  $-1$ . As shown in Table 1, a single  $Z$  error on any physical qubit can be located and corrected.

Therefore, from the aspect of TEC capability, the cluster state  $|G_{8}\rangle$  is analogous to the cell complex in Fig. 1b. Each protects one topological correlation and is robust against a single  $Z$  error, despite the cell complex in Fig. 2b being too small to propagate a logical qubit (see Supplementary Information for details).

![](images/2af446d1768f49d7b97dbc783d38476f1e9a5aa4a13cd009e5aaa74bf887d25e.jpg)  
Figure 2 | Cluster state  $|G_8\rangle$  and its cell complex. a,  $G_{8}$ , the interaction graph of  $|G_8\rangle$ . b, The corresponding 3D cell complex, with volumes  $\{\nu, w, y, z\}$ , faces  $\{f_1, f_2, f_3, f_4, f_5, f_6\}$ , edges  $\{e_7, e_8\}$  and vertices  $\{s, t\}$ . The exterior and the centre volume are not in the complex. For better illustration, the cell complex is cut open and the foreground quarter is removed (silhouette view from right is shown for clarity).

Table 1  $\left| {G}_{8}\right\rangle$  and the syndromes  $\left\langle  {{X}_{i}{X}_{j}}\right\rangle$  

<table><tr><td>Qubit with Z error</td><td>(X1X2)</td><td>(X2X5)</td><td>(X3X6)</td><td>(X3X4)</td></tr><tr><td>1</td><td>-1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>-1</td><td>-1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>1</td><td>1</td><td>-1</td><td>-1</td></tr><tr><td>4</td><td>1</td><td>1</td><td>1</td><td>-1</td></tr><tr><td>5</td><td>1</td><td>-1</td><td>1</td><td>1</td></tr><tr><td>6</td><td>1</td><td>1</td><td>-1</td><td>1</td></tr></table>

# Preparation of the eight-photon cluster state

In our experiment, we create the desired eight-photon cluster state using spontaneous parametric down-conversion and linear optics. The first step is to develop an ultrabright, high-fidelity entangled-photon source. As shown in Fig. 3a, an ultraviolet mode-locked laser pulse (power,  $915\mathrm{mW}$ ) passes through a  $\beta$ -barium borate crystal, generating a pair of polarization-entangled photons in the state  $|\phi\rangle = (|HH\rangle + |VV\rangle) / \sqrt{2}$ . Using an interferometric Bell-state synthesizer<sup>32</sup>, we guide photons of different bandwidths (Fig. 3a, red and blue dots, respectively) along separate paths. This disentangles the temporal information from the polarization information. By contrast with the conventional narrowband filtering technique, this process does not result in photon loss and we thus achieve ultrahigh brightness. Four pairs of such entangled photons are prepared and labelled as 1–2, 3–4, 5–6 and 7–8 (Fig. 3b). Then we generate two graph states, each of four photons. The first is a Greenberger-Horne-Zeilinger state,  $\left(|H^{\otimes 4}\rangle_{1-4} + |V^{\otimes 4}\rangle_{1-4}\right) / \sqrt{2}$ , obtained by superposing photons 2 and 4 on a polarizing beam splitter  $(\mathrm{PBS}_1)$ , which transmits horizontal polarization ( $H$ ) and reflects vertical polarization ( $V$ ). At the same time, photons 6 and 8 are interfered on a polarization-dependent beam splitter (PDBS) and then separately pass

through two other PDBs. The first PDBS has transmitting probabilities  $T_{H} = 1$  and  $T_{V} = 1 / 3$ , and the second and third have  $T_{H} = 1 / 3$  and  $T_{V} = 1$ . The combination of these three PDBs acts as a controlled-phase gate $^{33,34}$ . With a success probability of one-ninth, there is twofold coincidence in paths  $6'$  and  $8'$ , yielding a four-photon cluster state $^{34}$ $[|HH\rangle_{56}(|HH\rangle_{78} + |VV\rangle_{78}) + |VV\rangle_{56}(|HH\rangle_{78} - |VV\rangle_{78})] / 2$ . Finally, photons  $4'$  and  $6'$  are superposed on PBS $_2$ . When eight photons come out of the output ports simultaneously, we obtain an entangled eight-photon cluster state:

$$
\begin{array}{l} | \psi \rangle = \\ \frac {1}{2} \left[ \left| H ^ {\otimes 6} \right\rangle_ {1 - 6} \left(| H H \rangle_ {7 8} + | V V \rangle_ {7 8}\right) + \left| V ^ {\otimes 6} \right\rangle_ {1 - 6} \left(| H H \rangle_ {7 8} - | V V \rangle_ {7 8}\right) \right] ^ {(3)} \end{array}
$$

This is exactly the cluster state  $|G_8\rangle$  shown in Fig. 2a under Hadamard operations  $H^{\otimes 8}$  on all qubits. We note that the photons, which are interfered on the PBSs or the PDBS, have the same bandwidth, and that a star topology of the eight-photon interferometer<sup>32</sup> leads to an effective noise reduction.

To ensure good spatial and temporal overlap, the photons are also spectrally filtered, with full-widths at half-maximum of  $\Delta \lambda_{\mathrm{FWHM}} = 8\mathrm{nm}$  for photons 1, 3, 5 and 7 and  $\Delta \lambda_{\mathrm{FWHM}} = 2.8\mathrm{nm}$  for photons 2, 4, 6 and 8, and are coupled by single-mode fibres. We obtain an average twofold coincidence count of  $\sim 3.4\times 10^{5}\mathrm{s}^{-1}$  and a visibility of  $\sim 94\%$  in the  $\{|H\rangle ,|V\rangle \}$  basis as well as in the  $\{|+\rangle ,$ $|\text{-}\rangle \}$  basis, where  $|\pm \rangle = (|H\rangle \pm |V\rangle) / \sqrt{2}$ . Fine adjustments of the delays between the different paths are tuned to ensure that all the interfering photons arrive at the PBSs and the PDBS simultaneously.

Measurement of each photon is made using a polarization analyser, which contains a combination of a QWP, a HWP and a PBS together

![](images/4b81a2fb200812dbed42ef02e85bdf1f0371e0f3a2bbb17c29ec1d4c8457325d.jpg)  
Figure 3 | Experimental set-up for the generation of the eight-photon cluster state and the demonstration of topological error correction.

a, Creation of ultrabright entangled-photon pairs. An ultraviolet laser pulse passes through a 2-mm, nonlinear  $\beta$ -barium borate crystal, creating an entangled photon pair  $\{\mathrm{a},\mathrm{b}\}$  with density matrix

$\rho = (|\dot{H}_{\mathrm{a}}^{o}\rangle |\dot{V}_{\mathrm{b}}^{e}\rangle \langle V_{\mathrm{b}}^{e}|\langle H_{\mathrm{a}}^{o}| + |V_{\mathrm{a}}^{e}\rangle \langle H_{\mathrm{b}}^{o}|\langle H_{\mathrm{b}}^{o}|\langle V_{\mathrm{a}}^{e}|\rangle) / 2$  by parametric down

conversion, where  $o$  and  $e$  indicate ordinary and extraordinary polarizations, respectively perpendicular and parallel relative to the  $V$ -polarized pump. After both photons pass through compensators, which include a  $45^{\circ}$  half-wave plate (HWP) and a 1-mm  $\beta$ -barium borate crystal, one of the photons' polarizations is rotated by another  $45^{\circ}$  HWP. Then we re-overlap the two photons on a PBS, creating an entangled photon pair in a state

$|\phi_{\mathrm{ab}}\rangle = (|H\rangle |H\rangle +e^{i\varphi}|V\rangle |V\rangle)\otimes |e_{\mathrm{a}}\rangle |o_{\mathrm{b}}\rangle /\sqrt{2}$ , where  $|e_{\mathrm{a}}\rangle$  is a state in which all photons in path a have extraordinary polarization and  $|o_{\mathrm{b}}\rangle$  is a state in which all photons in path b have ordinary polarization.  $\mathbf{b}$ . To create the desired cluster state, we combine photons from paths 6 and 8 at the first PDBS and let each photon pass through another PDBS (PDBS'), resulting a controlled-phase operation between the two photons. At the same time, photons 2 and 4 are interfered on  $\mathrm{PBS}_1$ . Then photons  $4^{\prime}$  and  $6^{\prime}$  are overlapped on  $\mathrm{PBS}_2$ . On coincidence detection, we create the eight-photon cluster state (equation (3)) for topological error correction. c, Polarization analyser for each individual photon, containing a quarter-wave plate (QWP), a HwP, a PBS and two single-mode, fibre-coupled single-photon detectors.

with a single-mode, fibre-coupled single-photon detectors in each output of the PBS (Fig. 3c). The complete set of all 256 possible combinations of eight-photon coincidence events is registered by a home-made programmable coincidence logic unit based on a field-programmable gate array. We obtain an eightfold coincidence rate of 3.2 per hour. On the basis of the measurements for the 256 possible polarization combinations in the  $\{|H\rangle ,|V\rangle \}$  basis (Fig. 4a), we obtain a signal-to-noise ratio, defined as the ratio of the average number of desired components to that of non-desired components, of about 200:1. This indicates that we have been successful in preparing the desired eight-photon cluster state.

To characterize the cluster state more precisely, we use the entanglement witness method to determine its fidelity. For this purpose, we construct a witness that allows for the lower bound on the state fidelity and requires only eight measurement settings (Supplementary Information):

$$
\begin{array}{l} \mathcal {W} _ {8} = \frac {1}{2} - (| \psi \rangle \langle \psi | - | \psi^ {\prime} \rangle \langle \psi^ {\prime} |) \\ = \frac {1}{2} - \left[ \frac {1}{4} \left(| H \rangle \langle H | ^ {\otimes 6} - | V \rangle \langle V | ^ {\otimes 6}\right) _ {1 - 6} \otimes \left(X _ {7} X _ {8} - Y _ {7} Y _ {8}\right) \right. \\ \left. + \frac {1}{1 2} \left(\sum_ {k = 0} ^ {5} (- 1) ^ {k} M _ {k} ^ {\otimes 6}\right) _ {1 - 6} \otimes \left(| H \rangle \langle H | ^ {\otimes 2} - | V \rangle \langle V | ^ {\otimes 2}\right) _ {7 8} \right] \\ \end{array}
$$

Here  $\langle \psi'|\psi\rangle = 0$  and  $M_{k} = \cos (k\pi /6)X + \sin (k\pi /6)Y$ . The measured expectation value of each measurement setting in  $\mathcal{W}_8$  is shown in Fig. 4b. These yield the witness  $\langle \mathcal{W}_8\rangle = -0.105\pm 0.023$ , which is negative by 4.5 s.d. The state fidelity is  $F > 0.5 - \langle \mathcal{W}_8\rangle = 0.605\pm 0.023$ . This confirmed the presence of genuine eight-photon entanglement.

# Experimental topological error correction

Given such a cluster state, topological error correction is implemented using a series of single-qubit measurements and classical correction operations. In the laboratory, operations are performed on state  $|\psi \rangle$  (equation (3)), which differs from  $|G_8\rangle$  in Fig. 2a by the Hadamard operation  $H^{\otimes 8}$ . Therefore, the correlation to be protected in equation (1),  $\langle X_5X_6\rangle$ , corresponds to  $\langle Z_5Z_6\rangle$  in the experiment; similarly, each  $\langle X_iX_j\rangle$  in equation (2) corresponds to  $\langle Z_iZ_j\rangle$ . Furthermore,  $X$  errors are simulated instead of  $Z$  errors.

In the experiment, the noisy quantum channels on polarization qubits are simulated by one HwP positioned between two QWPs, which are set at  $90^{\circ}$  relative to the horizontal. By randomly setting the HwP axis to be oriented at  $\pm \theta$  with respect to the horizontal direction, the noisy quantum channel can be simulated with a bit-flip error probability of  $p = \sin^2 (2\theta)$ .

We first study the case in which only a single  $X$  error occurs on one of the six photons  $\{1, \dots, 6\}$ . The syndrome correlations are measured (Fig. 5). For comparison, in Fig. 4c we plot the correlations without any simulated error. This comparison, together with Table 1, makes it possible to locate precisely the physical qubit undergoing an  $X$  error.

We then consider the case in which all six photons are simultaneously subject to a random  $X$  error with equal probability  $0 < p < 1$  and study the rate of errors,  $\langle Z_5Z_6\rangle = -1$ , for the topological quantum correlation  $\langle Z_5Z_6\rangle$ . Without error correction, the error rate of correlation  $\langle Z_5Z_6\rangle$  is  $P = 1 - (1 - p)^2 -p^2$ . With error correction, the residual error becomes

$$
\begin{array}{l} P = 1 - \left[ (1 - p) ^ {6} + p ^ {6} \right] - \left[ 6 p (1 - p) ^ {5} + 6 (1 - p) p ^ {5} \right] \\ - \left[ 9 p ^ {2} (1 - p) ^ {4} + 9 (1 - p) ^ {2} p ^ {4} \right] \\ \end{array}
$$

For small  $p$ , the residual error rate after error correction is significantly reduced relative to the unprotected case. As shown in Fig. 6, the experimental results are in good agreement with these theoretical predictions. Considerable improvement of the robustness of the correlation  $\langle Z_5Z_6\rangle$  can be seen both in theory and in practice.

In the experiment, the whole measurement takes about 80 days. This requires our set-up to be extremely stable. The imperfections in the experiment are mainly due to the undesired components in the  $\{|H\rangle ,|V\rangle \}$  basis, which arise from higher-order emissions of entangled photons, and the imperfect photon overlapping at the PBSs and the PDBS. In spite of these issues, the viability of TEC is successfully demonstrated in the experiment.

# Discussion

In this work, we have experimentally demonstrated TEC with an eight-photon cluster state. This state represents the current state of the art for preparation of cluster states in qubit systems and is of particular interest in studying multipartite entanglement and quantum information processing. The scalable construction of cluster

![](images/5fb6adb4233fa505abc91240da26026b06da12dec41eef90baa2eb9f2305e97c.jpg)  
a

![](images/274449f476b277036f7dfdf40506b26d6958de40bc6ffcdbaabea1a3f7749e65.jpg)  
b

![](images/2bf59f5bf9e56c2e3f83ef4a62ac704904874a07a172e881c751a87ae6bff196.jpg)  
Figure 4 | Experimental results for the created eight-photon cluster state. a, Measured eightfold coincidence in the  $\{|H\rangle ,|V\rangle$  basis. b, The expectation values for different witness measurement settings. The measurement settings are  $A_0 = (|H\rangle \langle H|^{\otimes 6} - |V\rangle \langle V|^{\otimes 6})_{1 - 6}X_7X_8$ ,  $A_{1} = (|H\rangle \langle H|^{\otimes 6} - |V\rangle \langle V|^{\otimes 6})_{1 - 6}$ $Y_{7}Y_{8}$  and  $B_{i} = M_{i}^{\otimes 6}(|H\rangle \langle H|^{\otimes 2} - |V\rangle \langle V|^{\otimes 2})_{78}$  with  $i = 0,\ldots ,5$ . The  
c  
measurement of each setting takes  $50\mathrm{h}$  for the first two settings and  $30\mathrm{h}$  for the remaining settings. c, Correlations for the initial state without any simulated error. Error bars, 1 s.d., deduced from propagated Poissonian counting statistics of the raw detection events.

![](images/37e72b98dbdf0a03fd27f9ae6c638cb9fc28ad1e276d595c7f3730f98a0cf1cc.jpg)

![](images/93eee7ff23e9025847ecdd1bba73dbc216ebdaef1c40c1a4ea2336d943c57037.jpg)

![](images/52d684e556991448c64b94d70b732b5171c519cef0d4b9a968125fd30bf49b7a.jpg)

![](images/8bbfb064da3b7b32d6ffd539b57072341889cf1a5ca5e0cbe8df4165248be057.jpg)  
Correlation setting

![](images/bb00b5c4cb4017216ce6705d9ad60a9cb83708fad7cfeacc84c9d38aa9acdf4c.jpg)  
Figure 5 | Experimental results of syndrome correlations for topological error correction. Only one qubit is subjected to an  $X$  error in each plot. The measurement for each error setting takes about  $80\mathrm{h}$ . Error bars, 1 s.d., deduced from propagated Poissonian counting statistics of the raw detection events.  
Correlation setting

![](images/1aa28255d585a8d8ee8ce0bcdfea7114e06a137c2154c5f9b39b8c09c78c8b55.jpg)  
Correlation setting

states in future will require further development of high-efficiency entanglement sources and single-photon detectors $^{35}$ . Recent results have shown that if the product of the number-resolving detector efficiency and the source efficiency is greater than two-thirds, efficient linear optical quantum computation is possible $^{36}$ . There has been technical progress towards this goal, such as deterministic, storable, single-photon sources $^{37}$  and photon-number-resolving detectors $^{38}$ . Our demonstration of TEC is a further step towards fault-tolerant quantum computation. In the scheme, given sufficient qubits and physical error rates below  $0.7 - 1.1\%$ , arbitrary quantum computations can be performed arbitrarily reliably. The high threshold error rate is especially remarkable given that only nearest-neighbour interactions are required. Owing to these advantages, TEC is especially well suited for physical systems geometrically constrained to nearest-neighbour interactions, such as quantum dots $^{39}$ , Josephson junction qubits $^{40}$ , ion traps $^{41}$ , cold atoms in optical lattices $^{42}$  and photonic modules $^{17}$ . A quantum gate with an error rate below the threshold required in TEC is within reach of present technology $^{43}$ . It would be interesting in future work to exploit cluster states of the maximum achievable size, to implement topologically error-protected quantum algorithms using local measurements.

![](images/7d4bd9cb74572ee0da1ef8236fcf9da37c05be269ad71a8414bd89091a0152c6.jpg)  
Figure 6 | Experimental results of topological error correction. All physical qubits are simultaneously subject to an  $X$  error with equal probability ranging from 0 to 1. The blue circles and blue lines represent the experimental and, respectively, theoretical values of the error rate for the protected correlation without TEC, and the red squares and red lines similarly represent the error rate with TEC. The agreement between the experimental and the theoretical results demonstrates the viability of TEC. The measurement of each data point takes  $80\mathrm{h}$ . Error bars, 1 s.d., deduced from propagated Poissonian counting statistics of the raw detection events.

# Received 26 October; accepted 7 December 2011.

1. Shor, P. W. in Proc. 35th Annu. Symp. Foundations Computer Sci. 124-134 (IEEE, 1994).  
2. Grover, L. K. Quantum mechanics helps in searching for a needle in a haystack. Phys. Rev. Lett. 79, 325-328 (1997).  
3. Feynman, R. P. Simulating physics with computers. Int. J. Theor. Phys. 21, 467-488 (1982).  
4. Calderbank, A. R. & Shor, P. W. Good quantum error-correcting codes exist. Phys. Rev. A 54, 1098-1105 (1996).  
5. Steane, A. M. Error correcting codes in quantum theory. Phys. Rev. Lett 77, 793-797 (1996).  
6. Gottesman, D. Theory of fault-tolerant quantum computation. Phys. Rev. A 57, 127-137 (1998).  
7. Knill, E. Quantum computing with realistically noisy devices. Nature 434, 39-44 (2005).  
8. Aliferis, P., Gottesman, D. & Preskill, J. Quantum accuracy threshold for concatenated distance-3 code. Quantum Inf. Comput. 6, 97-165 (2006).  
9. Kitaev, A. Y. Quantum computations: algorithms and error correction. Russ. Math. Surv. 52, 1191-1249 (1997).  
10. Spedalieri, F. & Roychowdhury, V. P. Latency in local, two-dimensional, fault-tolerant quantum computing. Quantum Inf. Comput. 9, 666-682 (2009).  
11. Dennis, E., Landahl, A., Kitaev, A. & Preskill, J. Topological quantum memory. J. Math. Phys. 43, 4452-4505 (2002).  
12. Raussendorf, R., Harrington, J. & Goyal, K. A fault-tolerant one-way quantum computer. Ann. Phys. 321, 2242-2270 (2006).  
13. Wang, D. S., Austin, A. G. & Hollenberg, L. C. L. Quantum computing with nearest neighbor interactions and error rates over  $1\%$ . Phys. Rev. A 83, 020302(R) (2011).  
14. Rassendorf, R. & Harrington, J. Fault-tolerant quantum computation with high threshold in two dimensions. Phys. Rev. Lett. 98, 190504 (2007).  
15. Barrett, S. D. & Stace, T. M. Fault tolerant quantum computation with very high threshold for loss errors. Phys. Rev. Lett. 105, 200502 (2010).  
16. Stock, R. & James, D. F. V. A scalable, high-speed measurement-based quantum computer using trapped ions. Phys. Rev. Lett. 102, 170501 (2009).  
17. Devitt, S.J. et al. Topological cluster state computation with photons. N.J. Phys. 11, 083032 (2009).  
18. Nayak, C., Simon, S. H., Stern, A., Freedman, M. & Sarma, S. D. Non-abelian anyons and topological quantum computation. Rev. Mod. Phys. 80, 1083-1159 (2008).  
19. Wilczek, F. Fractional Statistics and Anyon Superconductivity (World Scientific, 1990).  
20. Cory, D. G. et al. Experimental quantum error correction. Phys. Rev. Lett 81, 2152-2155 (1998).  
21. Knill, E., Laflamme, R., Martinez, R. & Negrevergne, C. Benchmarking quantum computers: the five-qubit error correcting code. Phys. Rev. Lett. 86, 5811-5814 (2001).  
22. Chiaverini, J. et al. Realization of quantum error correction. Nature 432, 602-605 (2004).  
23. Schindler, P. et al. Experimental repetitive quantum error correction. Science 332, 1059-1061 (2011).  
24. Lu, C.-Y. et al. Experimental quantum coding against qubit loss error. Proc. Natl Acad. Sci. USA 105, 11050-11054 (2008).  
25. Aoki, T. et al. Quantum error correction beyond qubits. Nature Phys. 5, 541-546 (2009).  
26. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
27. Schlingemann, D. & Werner, R. F. Quantum error-correcting codes associated with graphs. Phys. Rev. A 65, 012308 (2001).  
28. Kitaev, A. Y. Fault-tolerant quantum computation by anyons. Ann. Phys. 303, 2-30 (2003).  
29. Bombin, H. & Martin-Delgado, M. A. Topological quantum distillation. Phys. Rev. Lett. 97, 180501 (2006).  
30. Hatcher, A. Algebraic Topology (Cambridge Univ. Press, 2002).

31. Fowler, A. G. & Goyal, K. Topological cluster state quantum computing. Quantum Inf. Comput. 9, 727-738 (2009).  
32. Yao, X.-C. et al. Observation of eight-photon entanglement. Nature Photon. (in the press); preprint at <http://arxiv.org/abs/1105.6318> (2011).  
33. Hofmann, H. F. & Takeuchi, S. Quantum phase gate for photonic qubits using only beam splitters and postselection. Phys. Rev. A 66, 024308 (2002).  
34. Kiesel, N. et al. Experimental analysis of a four-qubit photon cluster state. Phys. Rev. Lett. 95, 210502 (2005).  
35. O'Brien, J. L. Optical quantum computing. Science 318, 1567-1570 (2007).  
36. Varnava, M., Browne, D. E. & Rudolph, T. How good must single photon sources and detectors be for efficient linear optical quantum computation? Phys. Rev. Lett. 100, 060502 (2008).  
37. Chen, S. et al. Deterministic and storable single-photon source based on quantum memory. Phys. Rev. Lett. 97, 173004 (2006).  
38. Kardynal, B.E., Yuan, Z.L. & Shields, A.J. An avalanche-photodiode-based photon-number-resolving detector. Nature Phys. 2, 425-428 (2008).  
39. Press, D. et al. Complete quantum control of a single quantum dot spin using ultrafast optical pulses. Nature 456, 218-221 (2008).  
40. Hime, T. et al. Solid-state qubits with current-controlled coupling. Science 314, 1427-1429 (2006).  
41. Hensinger, W. K. et al. T-junction ion trap array for two-dimensional ion shuttling, storage, and manipulation. Appl. Phys. Lett. 88, 034101 (2006).  
42. Jaksch, D. et al. Entanglement of atoms via cold controlled collisions. Phys. Rev. Lett. 82, 1975-1978 (1999).

43. Benhelm, J., Kirchmair, G., Roos, C. F., & Blatt, R. Towards fault-tolerant quantum computing with trapped ions. Nature Phys. 4, 463-466 (2008).

Supplementary Information is linked to the online version of the paper at www.nature.com/nature.

Acknowledgements We acknowledge discussions with M. A. Martin-Delgado and O. Gühne. We are grateful to X.-H. Bao for his original idea of the ultrabright entanglement and to C.-Z. Peng for his idea of reducing high-order emission. We would also like to thank C. Liu and S. Fölling for their help in designing the figures. This work has been supported by the NNSF of China, the CAS, the National Fundamental Research Program (under grant no. 2011CB921300) and NSERC.

Author Contributions W.-B.G., A.G.F., R.R., Z.-B.C., Y.-J.D. and J.-W.P. had the idea for and initiated the experiment. A.G.F., R.R. and Y.-J.D. contributed to the general theoretical work. X.-C.Y., C.-Y.L., Y.-A.C. and J.-W.P. designed the experiment. X.-C.Y., T.-X.W. and H.-Z.C. carried out the experiment. X.-C.Y. and Y.-A.C. analysed the data. X.-C.Y., A.G.F., R.R., N.-LL., C.-Y.L., Y.-J.D., Y.-A.C. and J.-W.P. wrote the manuscript. N.-LL., Y.-A.C. and J.-W.P. supervised the whole project.

Author Information Reprints and permissions information is available at www.nature.com/reprints. The authors declare no competing financial interests. Readers are welcome to comment on the online version of this article at www.nature.com/nature. Correspondence and requests for materials should be addressed to Y.-A.C. (yuaochen@ustc.edu.cn) or J.-W.P. (pan@ustc.edu.cn).