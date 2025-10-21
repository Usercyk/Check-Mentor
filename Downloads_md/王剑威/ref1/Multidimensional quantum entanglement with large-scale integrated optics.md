# RESEARCH ARTICLE

# QUANTUM OPTICS

# Multidimensional quantum entanglement with large-scale integrated optics

Jianwei Wang, $^{1,2*}$  Stefano Paesani, $^{1*}$  Yunhong Ding, $^{3,4*}$  Raffaele Santagati, $^{1}$  Paul Skrzypczyk, $^{5}$  Alexia Salavrakos, $^{6}$  Jordi Tura, $^{7}$  Remigiusz Augusiak, $^{8}$  Laura Mančinska, $^{9}$  Davide Bacco, $^{3,4}$  Damien Bonneau, $^{1}$  Joshua W. Silverstone, $^{1}$  Qihuang Gong, $^{2}$  Antonio Acín, $^{6,10}$  Karsten Rottwitt, $^{3,4}$  Leif K. Oxenløwe, $^{3,4}$  Jeremy L. O'Brien, $^{1}$  Anthony Laing, $^{1}$  Mark G. Thompson $^{1}$

The ability to control multidimensional quantum systems is central to the development of advanced quantum technologies. We demonstrate a multidimensional integrated quantum photonic platform able to generate, control, and analyze high-dimensional entanglement. A programmable bipartite entangled system is realized with dimensions up to  $15 \times 15$  on a large-scale silicon photonics quantum circuit. The device integrates more than 550 photonic components on a single chip, including 16 identical photon-pair sources. We verify the high precision, generality, and controllability of our multidimensional technology, and further exploit these abilities to demonstrate previously unexplored quantum applications, such as quantum randomness expansion and self-testing on multidimensional states. Our work provides an experimental platform for the development of multidimensional quantum technologies.

As a generalization of two-level quantum systems (qubits), multidimensional quantum systems (qubits) exhibit distinct quantum properties and can offer improvements in particular applications. For example, qudit systems allow higher capacity and noise robustness in quantum communications (1-3), can be used to strengthen the violations of generalized Bell and Einstein-Podolsky-Rosen (EPR) steering inequalities (4-6), provide richer resources for quantum simulation (7, 8), and offer higher efficiency and flexibility in quantum computing (9, 10). Moreover, encoding and processing qubits can represent a more viable route to

$^{1}$ Quantum Engineering Technology Labs, H. H. Wills Physics Laboratory and Department of Electrical and Electronic Engineering, University of Bristol, Bristol BS8 1FD, UK.  $^{2}$ State Key Laboratory for Mesoscopic Physics, School of Physics, Collaborative Innovation Center of Quantum Matter, Peking University, Beijing 100871, China.  $^{3}$ Department of Photonics Engineering, Technical University of Denmark, 2800 Kgs. Lyngby, Denmark.  $^{4}$ Center for Silicon Photonics for Optical Communication, Technical University of Denmark, 2800 Kgs. Lyngby, Denmark.  $^{5}$ H. H. Wills Physics Laboratory, University of Bristol, Bristol BS8 1TL, UK.  $^{6}$ ICFO-Institut de Ciencies Fotoniques, Barcelona Institute of Science and Technology, 08860 Castelldefels, Spain.  $^{7}$ Max-Planck-Institut für Quantenoptik, 85748 Garching, Germany.  $^{8}$ Center for Theoretical Physics, Polish Academy of Sciences, 02-668 Warsaw, Poland.  $^{9}$ QMATH, Department of Mathematical Sciences, University of Copenhagen, 2100 Copenhagen Ø, Denmark.  $^{10}$ ICREA-Institucio Catalana de Recerca i Estudis Avancats, 08010 Barcelona, Spain. *These authors contributed equally to this work. †Corresponding author: Email: jianwei.wang@bristol.ac.uk (J.W.); yudin@fotonik.dk.tu.dk (Y.D.); anthony.laing@bristol.ac.uk (A.L.); mark.thompson@bristol.ac.uk (M.G.T.)

larger Hilbert spaces. These advantages motivate the development of multidimensional quantum technologies in a variety of systems, such as photons (11, 12), superconductors (8, 13), and atomic systems (14, 15). Unlike superconducting and atomic quuds, which cannot be encoded and manipulated without complex interaction engineering and control sequences, photons represent a promising platform able to naturally encode and process quuds in various degrees of freedom, such as orbital angular momentum (OAM) (11, 12), temporal modes (3, 16), and frequency (17, 18). Previous work on quuds includes realizations of complex entanglement (19), entanglement in ultrahigh dimensions (20), and practical applications in quantum communication (1-3) and computing (7-9). However, these approaches incur limitations in terms of controllability, precision, and universality, which represent bottlenecks for further developments of multidimensional technologies. For example, the arbitrary generation of high-dimensional entanglement is a key experimental challenge, typically relying on complex bulk-optical networks and postselection schemes (12, 16-18). In general, these approaches lack the ability to perform arbitrary multidimensional unitary operations with high fidelity (16, 19), an important factor in quantum information tasks. Integrated microring resonators able to emit multidimensional OAM (21) and frequency (18) states have been reported, but these present limited fidelity and difficulties for on-chip state control and analysis, thus not fully exploiting the high precision, scalability, and programmability of integrated optics.

We report a multidimensional integrated quantum photonic device that is able to generate, manipulate, and measure multidimensional entanglement fully on-chip with unprecedented precision, controllability, and universality. Path-encoded qudits are obtained in which each photon exists over  $d$  spatial modes simultaneously, and entanglement is produced by a coherent and controllable excitation of an array of  $d$  identical photon-pair sources. Our device allows the generation of multidimensional entangled states with an arbitrary degree of entanglement. Universal operations on path-encoded qudits are possible in linear optics for any dimension (22, 23), and our device performs arbitrary multidimensional projective measurements with high fidelity. The capabilities achieved allow us to demonstrate high-quality multidimensional quantum correlations, verified by generalized Bell and EPR steering violations, and to implement unexplored multidimensional quantum information protocols.

# Large-scale integrated quantum photonic circuit

Entangled path-encoded qubits can be generated by coherently pumping two photon-pair sources produced by spontaneous parametric downconversion (24) or by spontaneous four-wave mixing (SFWM) (25). The approach can be generalized to qubits via the generation of photons entangled over  $d$  spatial modes by coherently pumping  $d$  sources (24). However, scaling this approach to high numbers of dimensions has been challenging because of the requirement for a stable and scalable technology able to coherently embed large arrays of identical photon sources and to precisely control qudit states in large optical interferometers.

Silicon quantum photonics offer intrinsic stability (26), high precision (27), and dense integration (28) and can therefore provide a natural solution. We devised a large-scale silicon quantum photonic circuit to implement the scheme (Fig. 1A). A total of 16 SFWM sources are coherently pumped, generating a photon pair in a superposition across the array. Because both photons must originate from the same source, the bipartite state created is  $\sum_{k=0}^{d-1} c_k |1\rangle_{i,k} |1\rangle_{s,k}$ , where  $|1\rangle_{i,k}$  and  $|1\rangle_{s,k}$  respectively indicate the Fock state of the idler and signal photon in the  $k$ th spatial mode, and  $c_k$  represents the complex amplitude in each mode (with  $\sum |c_k|^2 = 1$ ). The mapping between the Fock state of each photon and the logical state is as follows: We say that the qudit state is  $|k\rangle$  ( $k = 0$ , ...,  $d - 1$ ) if the associated photon is in its  $k$ th optical mode. This yields a multidimensional entangled state of the form

$$
| \psi \rangle_ {d} = \sum_ {k = 0} ^ {d - 1} c _ {k} | k \rangle_ {i} | k \rangle_ {s} \tag {1}
$$

where the coefficients  $c_{k}$  can be arbitrarily chosen by controlling the pump distribution over the  $d$  sources and the relative phase on each mode. This is achieved with a network consisting of Mach-Zehnder interferometers (MZIs) at

the input and phase shifters on each mode. In particular, maximally entangled states  $|\psi_d^+\rangle = \sum_{k = 0}^{d - 1}|k\rangle_i|k\rangle_s / \sqrt{d}$  can be obtained with a uniform excitation of the sources. The two nondegenerate photons are deterministically separated using asymmetric MZI filters and routed by a network of waveguide crossings, grouping the signal photon into the top modes and the idler photon into the bottom modes (Fig. 1A). We

can then locally manipulate and measure the state of each qudit. Linear optical circuits enable the implementation of any local unitary transformation  $\hat{U}_d$  in dimension  $d$  (22, 23). A triangular network of MZIs and phase shifters is used, which allows us to perform arbitrary local projective measurements, and two detectors are used to measure the outcomes. In this scheme, the measurement outcomes on a spe

cific basis are collected sequentially by rotating the qudit reference frame and using one detector per photon. The collection of the  $d^2$  outcomes thus requires  $d^2$  detections in total. For more general implementations, the simultaneous collection of all the outcomes can be achieved via universal qudit operations (23) and the detection of each photon on all the output modes with  $2d$  detectors (Fig. 1A, inset).

![](images/71f5bdc46f56fae18056b1a3989dde1aac26bf87512fea66bdb499e9d4012358.jpg)

![](images/3079f31c2268281ab7a79713511fe269f4e3e43465451e230efffdeed776df07.jpg)  
Fig. 1. Diagram and characterization of the multidimensional silicon quantum photonic circuit. (A) Circuit diagram. The device monolithically integrates 16 SFWM photon-pair sources, 93 thermo-optical phase shifters, 122 multimode interferometer (MMI) beamsplitters, 256 waveguide croscers, and 64 optical grating couplers. A photon pair is generated by SFWM in superposition across 16 optical modes, producing a tunable multidimensional bipartite entangled state. The two photons, signal and idler, are separated by an array of asymmetric MZI filters and routed by a network of croscers, allowing the local manipulation of the state by linear optical circuits. Using triangular networks of MZIs, we perform arbitrary local projective measurements. The photons are coupled off the chip into fibers by means of grating couplers and are detected by two superconducting nanowire detectors. The inset represents a general schematic for universal

![](images/5f7d87a12ecc2e7e07475fca604b58dcc3e20ab224e7ca0ade4b3f4f915ce393.jpg)  
generation and manipulation of bipartite multidimensional entangled states. (B) Framework for correlation measurements on a shared  $d$ -dimensional state  $\hat{\rho}_d$ .  $\hat{M}_{a|x}$  and  $\hat{M}_{b|y}$  represent the operators associated with local measurements  $x$  on Alice and  $y$  on Bob, with outcomes  $a$  and  $b$ , respectively. (C) Photograph of the device. Silicon waveguides and 16 SFWM sources can be observed as black spirals. Gold wires allow the electronic access of each phase shifter. (D) Visibilities for the two-photon RHOM experiments to test sources' indistinguishability. The inset shows the histogram of all 120 measured visibilities, with a mean value of  $0.984 \pm 0.025$ . (E) Statistical fidelity for  $d$ -dimensional projectors in both the computational  $\hat{Z}$ -basis and the Fourier  $\hat{F}$ -basis. The inset shows the measured distribution for the 16-dimensional projector in the  $\hat{Z}$ -basis.

![](images/b64ae44920ec0c523e290247f48ee355cf1c5096a23b732b1973003fb38529db.jpg)

See (29) for more details of the device and experimental setup.

The 16 photon-pair sources are designed to be identical. Two-photon reversed Hong-Ou-Mandel (RHOM) interference is used to verify their performance, where the fringe visibility gives an estimate of the sources' indistinguishability (26). RHOM interference is tested between all the possible pairs of the 16 sources, performing  $\binom{16}{2} = 120$  quantum interference experiments and evaluating the corresponding visibilities. The pair of sources used for each interference experiment is selected each time by reconfiguring the interferometric network. The observed rate of photon-pair coincidences was approximately  $2\mathrm{kHz}$  in typical measurement conditions, from which accidents were subtracted. For the measured visibilities (Fig. 1D), in all cases we obtained a visibility greater than 0.90, and more than  $80\%$  of cases presented a visibility of  $>0.98$ . These results show a state-of-the-art degree of source indistinguishability in all 120 RHOM experiments, leading to the generation of high-quality entangled qudit states.

Each of the MZIs and phase shifters can be rapidly reconfigured (kHz rate) with high precision (26, 28). The quality of the qudit projectors is characterized by the classical statistical fidelity, which quantifies the output distribution obtained preparing and measuring a qudit on a fixed basis. We measured the fidelity of projectors in dimension  $d = 2$  to 16 in the computational basis  $\hat{Z} = |\boldsymbol{k}\rangle \langle \boldsymbol{k}|$  as well as in the Fourier-transform basis  $\hat{F} = |\ell \rangle \langle \ell|$ , where  $|\ell\rangle = \sum_{k=0}^{d-1} \exp(2\pi ik\ell / d)|k\rangle / \sqrt{d}$  and  $k, \ell = 0, \dots, d-1$  (Fig. 1E). For  $d = 8$ , we observed fidelities of

$98\%$  in the  $\hat{Z}$  -basis and  $97\%$  in the  $\hat{F}$  -basis; for  $d = 16$  ,fidelities were  $97\%$  in the  $\hat{Z}$  -basis and  $85\%$  in the  $\hat{F}$  -basis (29). The residual imperfections are mainly due to thermal cross-talk between phase shifters (higher in the  $\hat{F}$  -basis), which can be mitigated using optimized designs for the heaters (28) or ad hoc characterization techniques (23).

Because of a fabrication imperfection in the routing circuit, one of the modes (triangle label in Fig. 1A) for the idler photon presents an additional 10-dB loss. For simplicity, we exclude this lossy mode in the rest of our experiments and study multidimensional entanglement for dimensions up to 15.

Figure 1B represents the experiment in the standard framework for bipartite correlation. The correlations between two parties, Alice (A) and Bob (B)—here identified by the signal and idler photon, respectively—are quantified by joint probabilities  $p(ab|xy) = \mathrm{Tr}[\hat{\rho}_d(\hat{M}_{a|x}\otimes \hat{M}_{b|y})]$ , where  $\hat{\rho}_d$  is the shared  $d$ -dimensional state;  $x,y\in \{1,\dots,m\}$  represent the  $m$  measurement settings chosen by Alice and Bob; and  $a,b\in \{0,\dots,d - 1\}$  denote the possible outcomes with associated measurement operators  $\hat{M}_{a|x}$  and  $\hat{M}_{b|y}$ . The joint probabilities for each measurement are calculated by normalizing the coincidence counts over all the  $d^2$  outcomes in a given basis.

# Quantum state tomographies

Quantum state tomography (QST) allows us to estimate the full state of a quantum system, providing an important diagnostic tool. In general, performing a complete tomography is an expensive task both in terms of the number of

measurements and the computational time to reconstruct the density matrix from the data. For these reasons, complete QST on entangled qudit states has been achieved only up to eight-dimensional systems (30). To perform the tomographic reconstructions of larger entangled states, we use quantum compressed sensing techniques. Inspired by advanced classical methods for data analysis, these techniques reduce the experimental cost for state reconstruction (31), are general for density matrices of arbitrary dimension (32), and have been experimentally demonstrated to characterize complex quantum systems (32, 33). Compressed sensing QST was implemented to reconstruct bipartite entangled states with local dimension up to  $d = 12$ . Fidelities with ideal states  $|\psi_d^+\rangle$  are reported in Fig. 2A. For dimensions  $d = 4, 8$ , and 12, we plot the reconstructed density matrices, with fidelities of  $96\%$ ,  $87\%$ , and  $81\%$ , respectively (Fig. 2, B to D). These results show an improvement of the quality for multidimensional entanglement (18, 30). See (29) for more details.

# Certification of system dimensionality

The dimension of a quantum system quantifies its ability to store information and represents a key resource for quantum applications. Device-independent (DI) dimension witnesses enable us to set a lower bound for the dimension of a quantum system solely from the observed statistics [i.e., correlation probabilities  $p(ab|xy)$ ], making no prior assumptions on the experimental apparatus [see, e.g., (34, 35)]. Here, we adopt the approach of (35) to verify the local dimension of entangled states in a DI way in the context where

![](images/679182f3553a40a3fce5f9735f5843b5f50ed29cbb1ed29152db02baab8fb313.jpg)  
Fig. 2. Experimental quantum state tomographies. (A) Measured quantum fidelities  $\langle \psi_d^+ | \hat{\rho}_d | \psi_d^+\rangle$ , where  $\hat{\rho}_d$  represents the reconstructed states and  $|\psi_d^+\rangle$  refers to the ideal  $d$ -dimensional maximally entangled state. (B to D) Reconstructed density matrices for the entangled states in  
dimension 4 (B), 8 (C), and 12 (D) using compressed sensing techniques. Column heights represent the absolute values  $|\rho|$ ; colors represent the phases  $|\mathrm{Arg}(\rho)|$ . The phase information for matrix elements with module  $|\rho_{ij}| < 0.01$  is approximately randomly distributed but is not displayed for clarity.

![](images/beff8bf48056338b0bbab18885e9d98936a2c591835ea387c1242316947e569f.jpg)

![](images/260a46481ef787af729905a009a0fc75b06a4b7c9ab240b89f4a781ba6c9a64f.jpg)  
Fig. 3. Verification of system dimensionality. (A) Experimental results. Data points refer to the measured lower bounds on the local dimension of the generated entangled states; green and red points represent data for measurement scenarios I and II, respectively. The yellow line refers to ideal values. Errors are smaller than the markers and are neglected here for clarity. (B) Correlation measurements associated with optimal strategies for Magic Square and Magic Pentagram games. X, Y, and Z are Pauli operators and  $I$  is the identity. Red lines  $C_i$ ,  $R_i$ , and  $L_i$  are associated with different measurement settings. A single Magic Square game, a single Magic Pentagram game, and two copies of the Magic Square game are used in an attempt to certify the dimension for states with local dimension  $d = 4$ ,  $d = 6$  or 8, and  $d = 10$ , 12, 14, or 15, respectively. The correct dimension is certified for up to  $d = 10$  when using measurement scenario I and up to  $d = 14$  when using scenario II.

![](images/bb64a24a51ab7cff0b49c8208db1086eee99c2ddde867932b6450de915d45f52.jpg)

The lower bound on the system dimension is given by  $\lceil \mathcal{D}(p)\rceil$ , where  $\mathcal{D}(p)$  is a nonlinear function of the correlations, and  $\lceil \varepsilon \rceil$  indicates the least integer greater than or equal to  $\varepsilon$ . Whereas with  $d$  we indicate the local dimension of the qudit encoded in  $d$  modes,  $\lceil \mathcal{D}(p)\rceil$  represents the certified dimension of the quantum system—that is, the minimum dimension required to describe the observed correlations. We adopt two different DI measurement scenarios, with experimental results shown in Fig. 3A. In scenario I, we calculate the bound from the measured (partial) correlations for the Magic Square and Magic Pentagram games (36) (Fig. 3B). For example, to certify  $8\times 8$  entangled states (locally equivalent to a three-qubit system), we perform a  $\hat{Z}$ -basis measurement on Alice's system, while on Bob's system we use the  $\hat{Z}$ -basis and the one that simultaneously diagonalizes the commuting operators ZZZ, ZXX, XZX, and XXZ (Fig. 3B, lines L₃ and L₅, respectively). In the absence of noise, we would achieve  $\mathcal{D} = 8$ . Using the measured correlations, we obtain  $\mathcal{D}(p_8^{\mathrm{I}})\geq 7.22\pm 0.05$ , which yields the optimal lower bound  $\lceil \mathcal{D}(p_8^{\mathrm{I}})\rceil = 8$ . In scenario II, we compute  $\mathcal{D}(p_d^{\mathrm{II}})$  for correlations  $p_d^{\mathrm{II}}$  obtained by performing  $\hat{Z}$ -basis measurements on both sides of the maximally entangled state of local dimension  $d$ . We expect less experimental noise in this scenario (see Fig. 1D). As shown in Fig. 3A, the experimentally observed correlations  $p_d^{\mathrm{II}}$  yield  $\lceil \mathcal{D}(p_d^{\mathrm{II}})\rceil = d$  for all  $d\leq 14$ , certifying the correct dimensions. See (29) for further details.

# Multidimensional Bell correlations and state self-testing

Bell inequalities enable experimental studies of quantum nonlocality, which indicates the presence of correlations incompatible with local hidden variables (LHV) theories. Nonlocality can be demonstrated by the violation of Bell inequalities of the form  $S_{d} \leq C_{d}$ , where  $S_{d}$  is a linear function of the joint probabilities and  $C_{d}$  is the

classical bound for LHV models. Although our implementation does not represent a rigorous and loophole-free test of nonlocality, Bell inequalities are here used as an experimental tool to benchmark the quality of the multidimensional entanglement and to investigate possible future applications. We study two types of generalized Bell-type inequalities for  $d$ -dimensional bipartite systems: the SATWAP (Salavrakos-Augusiak-Tura-Wittek-Acin-Pironio) inequalities, recently introduced in (6), and the standard CGLMP (Collins-Gisin-Linden-Massar-Popescu) inequalities (5). In contrast to CGLMP inequalities, SATWAP inequalities are explicitly tailored to obtain a maximal violation for maximally entangled qudit states. Here, we test the two-input version of the SATWAP inequalities by measuring the joint probabilities to obtain the quantity

$$
\tilde {I} _ {d} = \sum_ {i = 1} ^ {2} \sum_ {l = 1} ^ {d - 1} \left\langle A _ {i} ^ {l} \tilde {B} _ {i} ^ {l} \right\rangle \tag {2}
$$

Measured CGLMP values are given with experimental errors. Values in parentheses refer to the LHV classical bound; those in braces refer to theoretical bounds for  $d$ -dimensional maximally entangled states. Errors are given by photon Poissonian noise.

Table 1. Experimental values for multidimensional CGLMP Bell correlations.  

<table><tr><td>Dimension</td><td>CGLMP Sd</td></tr><tr><td>2</td><td>(2) 2.810 ± 0.014 {2.828}</td></tr><tr><td>3</td><td>(2) 2.845 ± 0.012 {2.873}</td></tr><tr><td>4</td><td>(2) 2.867 ± 0.014 {2.896}</td></tr><tr><td>5</td><td>(2) 2.763 ± 0.014 {2.910}</td></tr><tr><td>6</td><td>(2) 2.629 ± 0.010 {2.920}</td></tr><tr><td>7</td><td>(2) 2.532 ± 0.013 {2.927}</td></tr><tr><td>8</td><td>(2) 2.650 ± 0.012 {2.932}</td></tr></table>

where the  $2(d - 1)$  values  $\langle A_i^l\bar{B}_i^l\rangle$  represent generalized Bell correlators, whose explicit form is given in (29). The Bell inequality here is given by  $\tilde{I}_d\leq C_d$  , where the bound for classical LHV models is  $C_d = [3\cot (\pi /4d) - \cot (3\pi /4d)] / 2 - 2.$  The maximum value of  $\tilde{I}$  obtainable with quantum states (known as the Tsirelson bound,  $Q_{d}$  ) is known analytically for arbitrary dimensions and is given by  $\tilde{I}_d\leq Q_d = 2d - 2$  . This maximal violation is achieved with maximally entangled states (6).

In Fig. 4A we show the experimental values of the generalized correlators  $\mathrm{Re}[\langle A_i^l\bar{B}_i^l\rangle ]$  . The correlation measurements are performed in the Fourier bases provided in (29). Figure 4B shows the obtained values of  $\bar{I}_d$  for dimensions 2 to 8, together with the analytical quantum and classical bounds. In all cases the classical bound is violated. In particular, in dimensions 2 to 4, a strong violation is observed, closely approaching  $Q_{d}$

We report in Table 1 the experimental values for the CGLMP inequalities. Again, strong violations of LHV models are observed. As an example, for  $d = 4$  we observe  $S_{4} = 2.867 \pm 0.014$ , which violates the classical bound (i.e.,  $C_d = 2$  for CGLMP inequalities) by  $61.9\sigma$  and is higher than the maximal value achievable by two-dimensional quantum systems  $(S_2 = 2\sqrt{2})$  by  $2.8\sigma$ , indicating stronger quantumness for higher dimensions.

The near-optimal Bell violations enable the self-testing of multidimensional entangled states. The task of self-testing represents the DI characterization of quantum devices by a classical user, based solely on the observed Bell correlations (37, 38), and thus does not require making any assumption about the devices being tested—a desirable attribute for practical quantum applications. If the maximal violation of a Bell inequality can only be achieved by a unique quantum state and set of measurements (up to local isometries), a near-optimal violation enables characterization of the experimental device. In (6) it was shown that the SATWAP inequality can be used to self-test the maximally entangled state of two qutrits  $|\psi_3^+\rangle$ ; in particular, using a numerical approach

from (39), a lower bound on the state fidelity can be obtained from the measured value of  $\tilde{I}_3$ . In (29) we generalize it also for arbitrary qutrit states of the form  $|00\rangle + \gamma |11\rangle + |22\rangle$  (up to normalization). In Fig. 4C, we report the experimental self-tested lower bounds on the fidelities for different values of  $\gamma = 1, 0.9$ , and  $(\sqrt{11} - \sqrt{3}) / 2 \approx 0.792$ . This is made possible by exploiting the capability of the device to generate multidimensional states with tunable entanglement. In particular,  $\gamma = 1$  indicates  $|\psi_3^+\rangle$ , and  $\gamma = (\sqrt{11} - \sqrt{3}) / 2$  represents the state that maximally violates the CGLMP inequality (39). We experimentally achieve self-tested lower bounds on the fidelities of  $79.9\%$ ,  $83.2\%$ , and  $68.0\%$ , respectively, for the three states. Note that the certification of high fidelities in a self-testing context is achievable only in the presence of near-ideal experimental correlations. The measured self-tested fidelities are comparable with the reported values obtained from full tomographies in other experimental approaches (18, 30). Although our device also provides high violations for dimensions higher than 3, it remains unknown whether the approach based on SATWAP inequalities can

be generalized to self-test states in arbitrary dimension (6).

# Multidimensional randomness expansion

Randomness is a key resource in many practical applications. Generating certified randomness, however, is a notoriously difficult problem. Quantum theory, being fundamentally nondeterministic, provides a natural solution. The probabilistic nature of measurements forms the basis of quantum random number generators (40). Remarkably, quantum theory can go one step further and allows a stronger form of certified randomness: Measurement statistics that exhibit nonlocal correlations are necessarily uncertain and contain randomness. This remains true even if some or all of the experimental apparatuses used to generate the nonlocal correlations are uncharacterized or untrusted (41). That is, the measurement statistics are random not only for the user of the devices but also for any other party who may have additional knowledge about the devices, such as a potential eavesdropper.

The two scenarios considered here are (i) randomness certified by Bell inequality violations,

where two untrusted measuring apparatuses are used to generate randomness, providing a fully DI certification (41), and (ii) randomness certified by EPR steering inequality violations, where one trusted and one untrusted measuring apparatus are used, with randomness generated from the untrusted device, providing a one-sided DI (1SDI) certification (42).

The protocol in either case consists of performing  $n$  runs of a Bell or steering test, using a small seed of randomness to choose the measurement settings in each run. The violation of the corresponding Bell or steering inequality is then estimated from the raw data. The randomness of the string  $\mathbf{s}$  of measurement outcomes of the untrusted apparatuses is then lower-bounded as a function of the observed violation. Because an initial seed of randomness is necessary, this process achieves randomness expansion as new private randomness is generated in the process. The randomness of the string  $\mathbf{s}$  is quantified in terms of min-entropy  $H_{\mathrm{min}} = -\log_2P_g$ , where  $P_{g}$  is the predictability of  $\mathbf{s}$  (i.e., the probability that it can be correctly guessed).

To study DI randomness expansion, we use violations of the above SATWAP Bell inequalities

![](images/b3f6ad8cea15df8f725dbe3580921a6d085bc69e2e34693aa0b8f1520e97a15e.jpg)

![](images/9dff05ad016092b3909ef109741416e3d45f2f71b73e77e9517795e1f36c6ded.jpg)

![](images/f3923d1cc245b18af95510f3de7b46205dfe893b4db96caf723f50458db15e76.jpg)

![](images/9e5ae8c02c8cba5e5db99ef4d13b722c54557dfdf5421f4f3d2c703838e7d1f6.jpg)

![](images/63c5007e827dfd883feb1fd9a65015ecff5649513bcbbb927e45337b66cd6259.jpg)  
Fig. 4. Bell violation and self-testing on multidimensional entangled states. (A) Measured values of the  $2(d - 1)$  correlators  $\mathrm{Re}[\langle A_i^j\tilde{B}_i^j\rangle ]$  Dashed boxes indicate theoretical values. (B) Violation of the generalized SATWAP Bell-type inequalities for  $d$  -dimensional states. Red points are experimentally measured  $\tilde{I}_d$  values. Bell inequalities of the form  $\tilde{I}_d\leq C_d$  are here violated, where  $C_d$  is the classical LHV bound (dashed line). The Tsirelson bound  $Q_{d}$  (solid line) represents the maximal violation for quantum systems. The dotted line represents the threshold above which more than

![](images/54d69688ad7d53b4443f3fa2ecd93553f78c983fcb427c7ccbc00f0833f279de.jpg)  
1 random bit can be extracted per output symbol from Bell correlations. (C) DI self-testing of entangled qutrit states  $(|00\rangle +\gamma |11\rangle +|22\rangle) / \sqrt{2 + \gamma^2}$  for  $\gamma = 1,0.9$  or 0.792. Self-tested lower bounds on the fidelities to ideal states are plotted as a function of the relative violation for more clarity. The significant uncertainty of the fidelity value is due to the general limited robustness of self-testing protocols. All errors are estimated from photon Poissonian statistics; those in (B) are smaller than markers.

(6), whereas in the ISDI case we use violations of the EPR steering inequalities tailored for maximal randomness expansion recently introduced in (29, 42):

$$
\beta_ {d} = \sum_ {\substack {a = b \\ x = y}} p (a | x) \operatorname{Tr} \left[ \hat {M} _ {b | y} \hat {\rho} _ {a | x} \right] \leq 1 + 1 / \sqrt {d} \tag{3}
$$

where  $p(a|x)$  are the probabilities of Alice's uncharacterized measurements;  $\hat{M}_{k|0} = |k\rangle \langle k|$  and  $\hat{M}_{\ell|1} = |- \ell \rangle \langle -\ell|$  are the characterized measure

![](images/cc783dbefed4d5aa082bf0ba7832d20fa8b8495615a9d04ddf9076e89b445d19.jpg)  
A

![](images/5bcdfd4729e86948419bf8c7530a0eafd6e071d6953bd05cea172802f4b15c15.jpg)  
B

![](images/39b2740559976a35ee6ca75cf505860e57c0f91045c3e22b34c26f1b807d3157.jpg)  
C  
Fig. 5. Certification of multidimensional randomness expansion. (A) Multidimension

EPR steering is certified by violating the inequality  $\beta_{d} \leq 1 + 1 / \sqrt{d}$  (dashed line). Red points are experimentally measured steering values  $\beta_{d}$ . The dotted line denotes the threshold above which more than 1 random bit is generated per round from steering correlations. (B) Randomness per round certified in a one-sided DI scenario by  $d$ -dimensional steering correlations. (C) Randomness per round certified in a fully DI scenario by  $d$ -dimensional Bell correlations. Above the dashed line in (B) and (C), more than 1 private random bit is generated per round. Error bars are given by Poissonian statistics; those in (A) are smaller than markers.

ments of Bob, with  $|k\rangle$  corresponding to the  $\hat{Z}$  -basis and  $|\ell \rangle$  to the  $\hat{F}$  -basis, defined above; and  $\hat{\rho}_{a|x}$  indicates the reduced state for Bob when the measurement  $x$  is performed on Alice and outcome  $a$  is obtained. Quantum states can violate this inequality and maximally achieve  $\beta_{d} = 2$  Figure 5A reports the experimentally measured values of  $\beta_{d}$  up to dimension 15, which display violations of the local bound in all dimensions. We note that this provides a ISDI certification of the presence of bipartite multidimensional entanglement between Alice and Bob in all cases (4).

In the DI setting, the measuring apparatuses of Alice and Bob are both untrusted, and the string of outcomes  $\mathbf{s} = (\mathbf{a},\mathbf{b})$  where  $\mathbf{a}$  and  $\mathbf{b}$  are the lists of data collected by Alice and Bob, respectively. In the ISDI setting, the measuring apparatus of Alice is untrusted, and the string of outcomes is  $\mathbf{s} = \mathbf{a}$ . [See (29) for details of how randomness is certified, as well as the maximal theoretical amount of randomness that can be certified in each case.] A particularly demanding task is the efficient generation of randomness so as to generate more than one bit of randomness per experimental run (i.e., to achieve  $H_{\mathrm{min}} > n$ ). For qubits, this is only possible using nonprojective measurements (with more than two outcomes) (43) or with sequences of measurements (44). In contrast, multidimensional entangled states provide a natural route based on projective measurements.

In Figs. 4B and 5A, the minimum values of  $\tilde{I}_d$  and  $\beta_d$  above which more than one bit of randomness per run is certified in the DI or 1SDI setting are shown as a function of dimension (yellow regions). Figure 5C shows the randomness associated with the Bell violations shown in Fig. 4A. Efficiency  $H_{\mathrm{min}} / n > 1$  is achieved for  $d = 3$  and 4. The largest amount of randomness per run is obtained for  $d = 4$ , where  $H_{\mathrm{min}} / n = 1.82 \pm 0.35$  random bits. The experimentally measured values of  $\beta_d$  are shown in Fig. 5A, and the associated randomness is reported in Fig. 5B. Here, efficiency  $H_{\mathrm{min}} / n > 1$  is preserved for the range  $4 \leq d \leq 14$ , indicating, as expected, stronger robustness in the 1SDI case.

# Conclusion

We have shown how silicon photonics quantum technologies have reached the maturity level that enables fully on-chip generation, manipulation, and analysis of multidimensional quantum systems. The achieved complexity of our integrated device represents a major step forward for large-scale quantum photonic technologies. Note that in the experimental tests performed here, the detection and locality loopholes were not closed, which was not an immediate goal of this work. However, the results demonstrate the unprecedented capabilities of multidimensional integrated quantum photonics, which will enable a wide range of practical applications. For example, high-rate, device-independent randomness generators can be realized by harnessing the abilities of efficient randomness expansion shown here, in combination with high-speed on-chip state manipulation. As a single-chip proof-of

principle demonstration of quantum key distribution, we report in (29) that Alice and Bob can share high-rate secure keys enabled by the high-fidelity control and analysis of the entangled quuds. Together with developed techniques for phase-coherent chip-to-chip qudit transmission—for example, via a multicore optical fiber (45), encoding in other degrees of freedom in free space (46), or exploiting reference frame-independent schemes (47)—our integrated platform can allow the development of high-dimensional quantum communications. All these possible applications can benefit from the monolithic integration of high-performance sources, universal operations, and detectors (26). Moreover, the scalability of silicon quantum photonics can further increase system dimensionality and allow the coherent control of multiple photons entangled over a large number of modes. Our results pave the way for the development of advanced multidimensional quantum technologies.

# REFERENCES AND NOTES

1. N. J. Cerf, M. Bourennane, A. Karlsson, N. Gisin, Phys. Rev. Lett. 88, 127902 (2002).  
2. F. Bouchard, R. Fickler, R. W. Boyd, E. Karimi, Sci. Adv. 3, e1601915 (2017).  
3. N. T. Islam, C. C. W. Lim, C. Cahall, J. Kim, D. J. Gauthier, Sci. Adv. 3, e1701491 (2017).  
4. H. M. Wiseman, S. J. Jones, A. C. Doherty, Phys. Rev. Lett. 98, 140402 (2007).  
5. D. Collins, N. Gisin, N. Linden, S. Massar, S. Popescu, Phys. Rev. Lett. 88, 040404 (2002).  
6. A. Salavrakos et al., Phys. Rev. Lett. 119, 040402 (2017).  
7. R. Kaltenbaek, J. Lavoie, B. Zeng, S. D. Bartlett, K. J. Resch, Nat. Phys. 6, 850-854 (2010).  
8. M. Neeley et al., Science 325, 722-725 (2009)  
9. B. P. Lanyon et al., Nat. Phys. 5, 134-140 (2009).  
10. A. Bocharov, M. Roetteler, K. M. Svore, Phys. Rev. A 96, 012306 (2017).  
11. A. Mair, A. Vaziri, G. Weihs, A. Zeilinger, Nature 412, 313-316 (2001).  
12. A. C. Dada, J. Leach, G. S. Buller, M. J. Padgett, E. Andersson, Nat. Phys. 7, 677-680 (2011).  
13. E. Svetitsky et al., Nat. Commun. 5, 5617 (2014).  
14. C. Senko et al., Phys. Rev. X 5, 021026 (2015).  
15. S. Choi, N. Y. Yao, M. D. Lukin, Phys. Rev. Lett. 119, 183603 (2017).  
16. A. Martin et al., Phys. Rev. Lett. 118, 110501 (2017).  
17. Z. Xie et al., Nat. Photonics 9, 536-542 (2015).  
18. M. Kues et al., Nature 546, 622-626 (2017).  
19. M. Malik et al., Nat. Photonics 10, 248-252 (2016).  
20. R. Fickler et al., Science 338, 640-643 (2012).  
21. X. Cai et al., Science 338, 363-366 (2012)  
22. M. Reck, A. Zeilinger, H. J. Bernstein, P. Bertani, Phys. Rev. Lett. 73, 58-61 (1994).  
23. J. Carolan et al., Science 349, 711-716 (2015).  
24. C. Schaeff et al., Opt. Express 20, 16145 (2012).  
25. R. Santagati et al., Sci. Adv. 4, eaap9646 (2018)  
26. D. Bonneau, J. W. Silverstone, M. G. Thompson, Silicon Quantum Photonics (Springer, 2016), pp. 41-82.  
27. J. Wang et al., Nat. Phys. 13, 551-555 (2017).  
28. N. C. Harris et al., Nat. Photonics 11, 447-452 (2017).  
29. See supplementary materials.  
30. M. Agnew, J. Leach, M. McLaren, F. S. Roux, R. W. Boyd, Phys. Rev. A 84, 062101 (2011).  
31. D. Gross, Y.-K. Liu, S. T. Flammia, S. Becker, J. Eisert, Phys. Rev. Lett. 105, 150401 (2010).  
32. E. Bolduc, G. Gariepy, J. Leach, Nat. Commun. 7, 10439 (2016).  
33. C. A. Riofrío et al., Nat. Commun. 8, 15305 (2017).  
34. M. Navascués, T. Vértesi, Phys. Rev. Lett. 115, 020501 (2015).  
35. J. Sikora, A. Varvitsiotis, Z. Wei, Phys. Rev. Lett. 117, 060401 (2016).  
36. N. D. Mermin, Phys. Rev. Lett. 65, 3373-3376 (1990).  
37. D. Meyers, A. Yao, in 39th Annual Symposium on Foundations of Computer Science (FOCS) (1998), p. 503.  
38. A. Coladangelo, K. T. Goh, V. Scarani, Nat. Commun. 8, 15485 (2017).

39. T. H. Yang, T. Vertesi, J.-D. Bancal, V. Scarani, M. Navascués, Phys. Rev. Lett. 113, 040401 (2014).  
40. M. Herrero-Collantes, J. C. Garcia-Escartin, Rev. Mod. Phys. 89, 015004 (2017).  
41. S. Pironio et al., Nature 464, 1021-1024 (2010).  
42. P. Skrzypczyk, D. Cavalcanti, arXiv:1803.05199 (2018).  
43. A. Acin, S. Pironio, T. Vertesi, P. Wittek, Phys. Rev. A 93, 040102 (2016).  
44. F. J. Curchod et al., Phys. Rev. A 95, 020102 (2017).  
45. Y. Ding et al., npj Quantum Inform. 3, 25 (2017).  
46. R. Fickler et al., Nat. Commun. 5, 4502 (2014)  
47. A. Laing, V. Scarani, J. G. rarity, J. L. O'Brien, Phys. Rev. A 82, 012304 (2010).

# ACKNOWLEDGMENTS

We thank A. C. Dada, P. J. Shadbolt, J. Carolan, C. Sparrow, W. McCutcheon, A. A. Gentile, D. A. B. Miller, and Q. He for useful discussions, and W. A. Murray, M. Louit, and R. Collins for experimental assistance. Funding: Supported by the Engineering and Physical

Sciences Research Council (EPSRC), European Research Council (ERC), and European Commission, including PICQUE, BBOI, QuChip, QITBOX, UK Quantum Technology Hub for Quantum Communications Technologies (EP/M013472/1) and the Center of Excellence, Denmark SPOC (ref DNRF123), Bristol NSQI, the Spanish MINECO (QIBEQI FIS2016-80773-P and Severo Ochoa SEV-2015-0522), the Fundacion Cellex, the Generalitat de Catalunya (SGR875 and CERCA Program), and the AXA Chair in Quantum Information Science; and the European Union's Horizon 2020 research and innovation program under Marie Sklodowska-Curie grant agreements 705109, 748549, and 609405. Also supported by the Chinese National Young 1000 Talents Plan (J.W.); the Royal Society through a University Research Fellowship (UHQT) (P.K.); the Villum Fonden via the QMATH Centre of Excellence (no. 10059) and EPSRC grant EP/L021005/1 (L.M.); National Key R&D Program of China grant 2013CB328704 (Q.G.); a Royal Academy of Engineering Chair in Emerging Technologies (J.L.O.); EPSRC fellowship EP/N003470/1 (A.L.); and ERC starter grant ERC-2014-STG 640079 and EPSRC Early Career Fellowship EP/K033085/1 (M.G.T.). Author contributions: J.W. designed the experiment; Y.D. designed and

fabricated the device. J.W., S.P., Y.D., R.S., and J.W.S. built the setup and carried out the experiment. S.P., P.S., A.S., J.T., R.A., L.M., D.Ba., and D.Bo. performed the theoretical analysis; A.L. contributed the tomography scheme; and Q.G., A.A., K.R., L.K.O., J.L.O., A.L., and M.G.T. managed the project. All authors discussed the results and contributed to the manuscript. Competing interests: All authors declare no competing financial interests. Data and materials availability: All data are available in the manuscript or in the supplementary materials.

# SUPPLEMENTARY MATERIALS

www.sciencemag.org/content/360/6386/285/suppl/DC1

Materials and Methods

Figs. S1 to S7

Tables S1 to S9

References (48-64)

8 December 2017; accepted 27 February 2018

Published online 8 March 2018

10.1126/science.aar7053

# Multidimensional quantum entanglement with large-scale integrated optics

Jianwei Wang, Stefano Paesani, Yunhong Ding, Raffaele Santagati, Paul Skrzypczyk, Alexia Salavrakos, Jordi Tura, Remigiusz Augusiak, Laura Mancinska, Davide Bacco, Damien Bonneau, Joshua W. Silverstone, Qihuang Gong, Antonio Acin, Karsten Rottwitt, Leif K. Oxenlowe, Jeremy L. O'Brien, Anthony Laing and Mark G. Thompson

Science 360 (6386), 285-291.

DOI: 10.1126/science.aar7053originally published online March 8, 2018

# Large-scale integrated quantum optics

The ability to pattern optical circuits on-chip, along with coupling in single and entangled photon sources, provides the basis for an integrated quantum optics platform. Wang et al. demonstrate how they can expand on that platform to fabricate very large quantum optical circuitry. They integrated more than 550 quantum optical components and 16 photon sources on a state-of-the-art single silicon chip, enabling universal generation, control, and analysis of multidimensional entanglement. The results illustrate the power of an integrated quantum optics approach for developing quantum technologies.

Science, this issue p. 285

ARTICLE TOOLS

http://science.sciencemag.org/content/360/6386/285

SUPPLEMENTARY MATERIALS

http://science.sciencemag.org/content/suppl/2018/03/07/science.aar7053.DC1

REFERENCES

This article cites 59 articles, 7 of which you can access for free http://science.sciencemag.org/content/360/6386/285#BIBL

PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service