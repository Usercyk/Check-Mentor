# Four-qubit variational algorithms in silicon photonics with integrated entangled photon sources

Check for updates

Alessio Baldazzi $^{1}$ , Matteo Sanna $^{1,2}$ , Massimo Borghi $^{1,3}$ , Stefano Azzini & Lorenzo Pavesi $^{1}$

Variational quantum algorithms are hybrid quantum-classical approaches extensively studied for their potential to leverage near-term quantum hardware for computational advantages. In this work, we successfully execute two variational quantum algorithms on a silicon photonic integrated circuit at room temperature: a variational quantum eigensolver for the Hydrogen molecule and a variational quantum factorization for semiprime numbers. In our reconfigurable silicon photonic circuit, four identical spontaneous-four-wave-mixing-based integrated photon pair sources are used to prepare two path-entangled ququarts, whose correlation gives rise to the resource for generic trial states' preparation. This marks a first demonstration of variational quantum algorithms on a photonic quantum simulator with integrated photon pair sources.

Quantum computing  $(\mathrm{QC})^{1-5}$  is based on a new computational paradigm, that promises an exponential speed-up over classical machines for certain classes of problems<sup>6,7</sup>. However, nowadays quantum processors are typically limited in terms of the number of qubits, interconnection topology, fidelity of the entangling gates, and losses. Because of these limitations, they are termed 'Noise Intermediate Scale Quantum' (NISQ) devices<sup>8</sup>. Variational quantum algorithms (VQAs)<sup>9</sup> are investigated to achieve quantum utility<sup>10</sup> through NISQ processors. In fact, they require a modest number of qubits and a limited circuit depth. In a nutshell, the workflow of VQAs is sketched in Fig. 1. First, the problem is encoded into a collection of measurable observables,  $\{\hat{O}_k\}_k$ , based on the qubit register of the Quantum Hardware (QH). A cost function C is defined as a weighted sum of expectation values as follows

$$
C = \sum_ {k} w _ {k} \left\langle \hat {O} _ {k} \right\rangle , \tag {1}
$$

where  $\{\langle \hat{O}_k\rangle \}_{k}$  are the expectation values of the corresponding observables are evaluated on a quantum state  $|\psi (\pmb {\theta})\rangle$  , parametrized by a list of parameters  $\pmb{\theta}$  , and the classically-computed coefficients  $\{w_{k}\}_{k}$  depend on the specific problem to address. Once the problem is encoded, the reconfigurable QH starts preparing trial states, and measurements are performed. The collected raw data are sent to the classical machine for post-processing, where the cost function is evaluated. An optimization routine is executed by the classical part, and the quantum part is updated with a new setting of parameters  $\pmb{\theta}$  , accordingly to the cost function result. This procedure is repeated until the cost function converges to an extremal value. In this way,

the minimization of the cost function and the optimal setting of parameters for the trial state preparation are achieved. For a generic set  $\{\hat{O}_k\}_k$ , the observables don't commute, and the evaluation of their expectation values can be simultaneously done only within the same commuting group  $(\mathrm{CG})^{11-15}$ . With respect to Quantum Phase Estimation and Shor's algorithm $^{4,16-18}$ , VQAs are hybrid quantum-classical approaches, and they don't require a set of universal gates or quantum error-correction codes. Such algorithms show robustness against error $^{19,20}$  and can run on shallow circuits $^{21}$ . What is needed is a reconfigurable QH able to prepare states that can be mapped to the Hilbert space configurations of the addressed problem $^{22}$ . Then, the generic parametrized states can be 'trained' to minimize the desired cost function, similarly to Machine Learning processes $^{9}$ . The whole procedure shown in Fig. 1 must be tailored to a specific problem, since the coefficients  $\{w_k\}_k$  and the observables  $\{\hat{O}_k\}_k$  are determined by the addressed task and the qubit register. The problems can be classified as classical, e.g., combinatorics problems, and quantum, e.g., energy levels and scattering amplitudes. In both cases, the advantage with respect to classical algorithms could come from the information encoding and the quantum parallelization, given by the exponential scaling of the Hilbert space dimension with the number of qubits, and the use of superposition and entanglement $^{4}$ .

The first experimental implementation of a variational quantum eigensolver (VQE) has been realized on a photonic integrated circuit (PIC) with an external photon pair source $^{23}$ . Then, the whole VQE theory has been formalized in $^{11,19}$ . VQE has also been demonstrated with superconducting qubits $^{20,21,24-26}$  and trapped ions $^{27-29}$ . In these platforms, chemical accuracy of VQE has been reported $^{30-32}$ . In the same family of variational algorithms, we

$^{1}$ Department of Physics, University of Trento, Trento, Italy.  $^{2}$ Present address: Rotonium S.r.L., Padova, Italy.  $^{3}$ Present address: Department of Physics, University of Pavia, Pavia, Italy.  $\times$  e-mail: alessio.baldazzi@unitn.it

![](images/f2ae384bc8ab31b780e4fcc3611991af68ffaa12a804cc1a759f7801bcc6f67a.jpg)  
Fig. 1 | Schematic workflow of variational quantum algorithms. The procedure starts with the problem encoding: depending on the problem/task and the qubit register of the Quantum Hardware, a set of observables  $\{\hat{O}_k\}_k$  is identified and the cost function  $C$  is constructed as a weighted sum of the observables expectation values,  $\{\langle \hat{O}_k\rangle \}_{k}$ . Then, the Quantum Hardware is configured to prepare the trial states  $|\psi (\pmb {\theta})\rangle$  by starting from an initial state  $|\psi_0\rangle$  and applying the transformation  
U, which depends on the variational parameters  $\theta$ . The measurements of the trial state give the observables' expectation values. By processing the collected data, the classical machine calculates the cost function for each trial state and, after that, it sets new parameters on the quantum part. This cycle is driven by an optimization routine managed by the classical part, and it is repeated until the cost function converges to an extremal point.

can find the variational quantum factoring  $(\mathrm{VQF})^{33,34}$ , a factorization algorithm tailored to the number to factorize. Also in this case, the algorithm has been successfully performed with superconducting qubits<sup>35</sup>, and, only very recently, on a PIC with an external photon pair source<sup>36</sup>. In general, despite several experimental implementations, it is still not clear if VQAs can lead to a useful quantum advantage<sup>11,19</sup>, with major issues related to the minimization procedure of the cost function, such as the barren plateau phenomenon<sup>9</sup>. Thus, even if NISQ processors satisfy the requirements of VQAs, the desired accuracy and the duration of the specific algorithm may prevent VQAs from surpassing classical techniques. For these reasons, further theoretical and experimental investigations are needed to understand the full potential of this method for specific-purpose tasks.

Integrated quantum photonics $^{37-46}$  is a particularly promising platform, since photons are a natural choice to transfer information thanks to low decoherence and high data rates. Moreover, the use of different degrees of freedom of photons $^{47,48}$  makes it possible to encode the information with a wide variety of choices by using linear operations with high fidelity, robustness, and flexibility. For example, path encoding $^{49}$  relies on Mach-Zehnder interferometers (MZI) or MZI networks $^{50,51}$  to implement any transformations of a generic qudit, i.e.,  $d$ -dimensional qubit. Knill et al. $^{52}$  showed that linear optical quantum computing (LOQC) $^{48,52-75}$  can be realized through post-selection. This paradigm for photon entangling gates enables the existing technology to achieve photonic  $\mathrm{QC}^{42,47,76-81}$  with both approaches to quantum algorithms: measurement-based $^{82,83}$  and gate-based $^{4}$  QC. Because of the well-established photonic technology, fault-tolerant large-scale quantum photonic architectures could be achieved in the next few years, leveraging the latest achievements of integrated optics $^{84-91}$ . In particular, thanks to high-quality single photon sources and high-performing PIC, a significant improvement of photonic-based VQEs has been recently demonstrated using gate-based computation $^{92}$ : four times faster than $^{23}$  and a chemical accuracy on par with superconducting and trapped-ion qubits $^{30-32}$ . However, this latest achievement is based on a quantum-dot single photon source working at  $5\mathrm{K}$  and on integrated photonic probabilistic CNOT gates.

Quantum silicon photonics allows generating high-quality entangled photons at room temperature via spontaneous four-wave mixing (SFWM)[93-98]. These states provide an extremely valuable quantum resource without the need for cryogenic temperatures. In the low-gain regime, a pair of energy-time entangled photons is generated[99-101]. Such quantum correlation can be utilized as an entanglement resource for photonic processors.

This work aims to significantly advance the capabilities of integrated photonic VQAs by presenting a room-temperature silicon photonic integrated circuit (Si-PIC) implementing a four-qubit variational quantum eigensolver able to solve a quantum chemistry problems and factorization tasks with high accuracy. The Si-PIC uses

four spiral waveguides as sources of correlated photon pairs to create multidimensional entangled states, which serve as trial states for the implemented VQAs. For the first time, to the best of our knowledge, this work addresses proof-of-principle instances of quantum chemistry and factorization problems by means of a small-scale quantum photonic processor with integrated quantum light sources. Moreover, an interesting feature of our implementation exploits the time-energy entanglement of the photon pairs to obtain path entanglement, thus showing the possibility to avoid, at least to some extent, the use of probabilistic CNOT gates, in contrast to other photonic implementations $^{23,36,92}$ .

The paper is organized as follows. "Photonic integrated circuit for four-qubit variational algorithms" describes the Si-PIC used to implement the VQAs. Section "Discussion" shows the results of the VQE for the Hydrogen molecule and of VQF for the semiprime numbers, respectively. In "Solving the Hydrogen molecule" and "Factorizing semiprime numbers", we comment on scaling and improvement of our scheme. All the details are reported in the Supplementary Information.

# Results

# Photonic integrated circuit for four-qubit variational algorithms

Figure 2 reports the scheme of the Si-PIC, whose footprint is  $1.5 \times 5 \mathrm{~mm}^2$ . The building blocks of this circuit are grating couplers<sup>102</sup>, multimode-interference-based integrated beam splitters (MMIs)<sup>103</sup>, crossing waveguides<sup>104</sup>, and thermal phase shifters (PSs)<sup>105,106</sup>. In particular, the composition of MMIs and PSs gives rise to integrated MZIs. A detailed discussion of the Si-PIC design, the description of the setup, and the characteristics of the utilized photonic components, both in terms of theoretical modeling and measured performances, are reported in the Methods and Supplementary Information Sections 1-4.

The Si-PIC has four input and eight output ports. The ports are based on grating couplers and only one input and two output ports were used in this work (label IN, OUT-1 and OUT-2 in Fig. 2). The circuit is composed of five parts: (I) pump splitting (green box of Fig. 2), (II) integrated sources (golden box of Fig. 2), (III) photon pairs' routing (purple box of Fig. 2), (IV-i) and (IV-s) linear manipulation of the idler and signal photons (blue and red boxes of Fig. 2), respectively.

Stage (I) is used to coherently pump the 1.5 cm-long spiral-waveguide-based integrated sources, present in stage (II), with arbitrary amplitudes to generate correlated photon pairs through SFWM. We utilize fundamental-TE-intramodal non-degenerate SFWM in silicon spiral waveguides, and, as usual, we denote the two generated photons as idler and signal, where the first is the photon with shorter wavelength and the latter the photon with longer wavelength. We choose spiral waveguides as photon pair sources to obtain a high degree of spectral

![](images/da419e7797c8b091a528440720062c65a0dfc9fccedc7859fe9c4ab7af598fb5.jpg)  
Fig. 2 | Layout of the silicon photonic integrated circuit. Blue lines are waveguides, solid blue components are passive integrated optical devices (grating couplers, MMIs, and crossing waveguides), and solid orange components are thermal phase shifters. IN denotes the input where light is injected, and OUT-1 and OUT-2 stand for the outputs where light is collected. The circuit is divided into five parts: (I) pump splitting in the green box, (II) integrated sources in the golden box, (III) photon pairs'  
routing (composed of AMZIs and crossing waveguides) in the purple box, and finally, (IV-i and IV-s) idler and signal manipulation in blue and red boxes, respectively. The numbers on the inputs of stage (II) and outputs of stage (III) denote the four spatial modes used to encode the two-ququart states, while the associated qubit states are reported on the left of stages (IV-i/s).

indistinguishability $^{107,108}$ , which is an important requirement for the VQAs, whose implementation is reported in "Solving the Hydrogen molecule" and "Factorizing semiprime numbers". In stage (III), asymmetric MZIs (AMZIs) $^{109}$  and crossing waveguides route idlers to stage (IV-i) and signals to stage (IV-s). In the low squeezing regime and through the coincidence basis of idlers and signals, we post-select the events where only one source emits a pair. Under this setting, the single-photon spatial modes of idler and signal can be utilized to encode ququart computational basis states,  $\{|m\rangle \}_{m = 1\dots 4}$ , and the output state of stage (III) reads as follows

$$
\left| \psi_ {\mathrm {I I I}} ^ {(4)} \right\rangle \equiv \sum_ {m = 1} ^ {4} \alpha_ {m} | m \rangle_ {i} | m \rangle_ {s}, \tag {2}
$$

where the complex parameters  $\{\alpha_{m}\}_{m}$ , normalized such that  $\sum_{m=1}^{4} |\alpha_{m}|^{2} = 1$ , depend on the setting of stage (I), and the subscripts  $i/s$  refer to idler and signal. Through the separation and the routing, the energy-time correlation of the twin photons<sup>99-101</sup> is converted into a spatial correlation. Neglecting losses, if an idler photon enters the  $m$ -th spatial mode of stage (IV-i), its twin signal photon arrives in the  $m$ -th spatial mode of stage (IV-s). For a general setting of stage (I), we can achieve any separable two-ququart computational basis states or any  $d$ -dimensional entangled state of dimension  $(2,3,4)$ , where the first ququart is encoded in the idler photon and the second in the signal photon. Then, by utilizing binary numbers, the two-ququart state can be mapped to the following four-qubit state

$$
\left| \psi_ {\mathrm {I I I}} ^ {(4)} \right\rangle = \alpha_ {1} | 0 0 \rangle_ {i} | 0 0 \rangle_ {s} + \alpha_ {2} | 0 1 \rangle_ {i} | 0 1 \rangle_ {s} + \alpha_ {3} | 1 0 \rangle_ {i} | 1 0 \rangle_ {s} + \alpha_ {4} | 1 1 \rangle_ {i} | 1 1 \rangle_ {s}. \tag {3}
$$

The labeling of the spatial modes and the two-qubit states is reported in Fig. 2 on the right and left of the blue and red boxes, respectively. The first and second qubits are encoded in the idler photon, and the third and fourth qubits in the signal photon. For the rest of the manuscript, whenever the subscripts  $i / s$  are omitted, we are following the order in the previous equation for a state  $\left|x_{1}x_{2}x_{3}x_{4}\right\rangle$ , with  $\{x_{i}\}_{i = 1\dots 4} = \{0,1\}$ , written in qubit states. Then, the final stages (IV-i) and (IV-s) perform linear transformations on each photon belonging to a given correlated photon pair. Thus, the

final state written in the ququart computational basis becomes<sup>110</sup>

$$
\left| \psi_ {\mathrm {I V}} ^ {(4)} \right\rangle = \left(U ^ {(i)} \otimes U ^ {(s)}\right) \left| \psi_ {\mathrm {I I I}} ^ {(4)} \right\rangle = \sum_ {m = 1} ^ {4} \alpha_ {m} \left| \xi_ {m} \right\rangle_ {i} \left| \xi_ {m} \right\rangle_ {s}, \quad \text {w h e r e} \left| \xi_ {\mathrm {m}} \right\rangle_ {\mathrm {i} / \mathrm {s}} \equiv \mathrm {U} ^ {\left(\mathrm {i} / \mathrm {s}\right)} | \mathrm {m} \rangle_ {\mathrm {i} / \mathrm {s}}, \tag {4}
$$

and  $U^{(i / s)}$  represents the linear transformation on the idler/signal photon implemented in stages (IV-i/s). From the previous equation, we can note that the two ququarts are independently manipulated in stages (IV-i) and (IV-s). If  $U^{(i / s)}$  is a generic SU(4)-transformation<sup>11</sup>, the state in the previous equation is exactly the well-known Schmidt decomposition of a bipartite system<sup>12</sup>. In this case, it is possible to prepare the generic trial state in the two-ququart Hilbert space. The triangular MZI scheme<sup>38,44</sup> of stages (IV-i/s) cannot implement the generic unitary transformation of ququart states, since such action can be achieved by schemes like Reck<sup>50</sup> and Clements<sup>51</sup>. Instead, what the final stages can execute are generic projections of any ququart state encoded in the idler and signal photons on OUT-1 and OUT-2, respectively. As shown in Fig. 2, these outputs correspond to the qubit state  $|01\rangle_{i / s}$ , or equivalently the ququart state  $|2\rangle_{i / s}$ <sup>38,44</sup>. Finally, the idler and signal photons are collected from OUT-1 and OUT-2, respectively and sent to two single-photon detectors (SPDs). This operation can be ideally described by the Von Neumann projector on the ququart state  $|2\rangle_i|2\rangle_s$ , or equivalently the qubit state  $|01\rangle_i|01\rangle_s$ . Within this configuration, the non-universality of ququart manipulation and the presence of one detector for each ququart is overcome by using multiple projective measurements. This choice uses the minimal number of detectors and it is achieved by executing different projectors in the final stages of the circuit given the observable to be measured. The number of linearly independent projectors is 16, i.e., a set of four projectors relative to four independent input states of stage (IV-i/s) for each ququart. The choice of 16 projectors represents the measurement setting that we want to implement, and thus, it depends on the set of CGs of observables  $\{\hat{O}_k\}_{k}$  in the cost function to be measured<sup>12-15</sup>.

The quantum resource of our photonic processor is given by the multidimensional entangled states of photon pairs. At every run of the VQAs, the two single photons are independently manipulated, and there is no multi-photon interference between independent photon pairs $^{113,114}$ . Therefore, purity $^{115-117}$  is not of concern. What matters is the

![](images/dd921ba9e62dabb6d0e5c4d15959a7f65305d5152d80e1105b2425c66265aae5.jpg)  
Fig. 3 | Heralded single-photon interference and dimension certification. a Normalized coincidences of correlated photons measured at the outputs OUT-1 and OUT-2 in heralded single-photon interference experiments. The colors are associated with three different pairs of sources, and the sinusoidal fit is reported as a continuous line. The PSs used for the three interference patterns are:  $\phi_2^{(i)}$  (the PS in

indistinguishability of the sources present in our bipartite system, since it affects the single-photon interference visibility. Heralded single-photon interference experiments are described in Supplementary Information Section 5 and the results are shown in Fig. 3a. Moreover, measurements to certify the effective multidimensional entanglement have also been carried out as explained in Supplementary Information Section 6, and the related results are plotted in Fig. 3b. Overall, these results demonstrate a good degree of sources' indistinguishability  $(99.3 \pm 0.5$  visibility for sources 2-3) and high quality of bipartite entanglement.

Based on the Si-PIC, and given a set of binary observables  $\hat{O}_k$ , the cost function given in Eq. (1) can be rewritten in terms of the ingredients of the Si-PIC itself as follows (see Supplementary Information Section 7 for details)

$$
\left. \mathrm {C} (\boldsymbol {\alpha}) = \sum_ {k} \sum_ {\mathrm {I} \in \mathrm {C G}} w _ {k} \sum_ {m _ {1}, m _ {2} = 1} ^ {4} \pi [ k, \mathrm {I}, m _ {1}, m _ {2} ] | \langle 2 | _ {i} \langle 2 | _ {s} (U ^ {(i)} [ \mathrm {I}, m _ {1} ] \otimes U ^ {(s)} [ \mathrm {I}, m _ {2} ]) | \psi_ {\mathrm {I I I}} ^ {(4)} (\boldsymbol {\alpha}) \rangle | ^ {2}, \right. \tag {5}
$$

where  $\alpha$  are the variational parameters of our QH, the index I indicates the measurement settings associated with different CGs,  $U^{(i / s)}[\mathrm{I},m]$  is the projection of the  $m$ -th element among the four eigenstates of the  $k$ -th observable on the state  $|2\rangle_{i / s}$  within the same measurement setting and  $\pi [k,\mathrm{I},m_1,m_2]$  is the product of the eigenvalues of the corresponding eigenstates pairs. The variational parameters depend on the pump splitting performed in stage (I), while the measurement settings are set in stages (IV-i) and (IV-s). In particular, as we measure idler-signal photons coincidence events at OUT-1 and OUT-2 of the Si-PIC, we use them to estimate the probabilities contained in Eq. (5), upon normalization by the total coincidence events recorded with the same measurement setting. In this case, Eq. (5) can be rewritten as follows

$$
C (\boldsymbol {\alpha}) = \sum_ {k} \sum_ {\mathrm {I} \in \mathrm {C G}} w _ {k} \sum_ {m _ {1}, m _ {2} = 1} ^ {4} \pi [ k, \mathrm {I}, m _ {1}, m _ {2} ] \frac {\mathrm {C C} [ \boldsymbol {\alpha} , k , \mathrm {I} , m _ {1} , m _ {2} ]}{\mathrm {C C} ^ {\text {t o t}} [ \boldsymbol {\alpha} , k , \mathrm {I} ]}, \tag {6}
$$

$$
\text {w h e r e} \mathrm {C C} ^ {\mathrm {t o t}} [ \boldsymbol {\alpha}, \mathrm {k}, \mathrm {I} ] \equiv \sum_ {\mathrm {m} _ {1}, \mathrm {m} _ {2} = 1} ^ {4} \mathrm {C C} [ \boldsymbol {\alpha}, \mathrm {k}, \mathrm {I}, \mathrm {m} _ {1}, \mathrm {m} _ {2} ].
$$

Here CC refers to the coincidence counts measured with a specific setting of variational parameters  $\alpha$  and the  $(m_1, m_2)$  projective measurement associated with the I-th measurement setting, and  $\mathrm{CC}^{\mathrm{tot}}$  to the total coincidence counts of all the projective measurements within the I-th measurement setting. The evaluation of the cost function is achieved by utilizing the coincidence counts provided by our photonic processor and by the weighted sum shown in Eq. (6) on the digital computer, i.e., a PC.

Note that stages (IV-i/s) are used only to perform projective measurements, modulo fixed linear transformations, and the variational

![](images/6b057728fe33b973c09deebdd14616cdbf6c6a0d48fb257b9dedcb7fa4ef2fbe.jpg)  
the second spatial mode at the input of stage (IV-i)) for sources' pair (2-3),  $\phi_{1/4}^{(s)}$  (PS in the first/fourth spatial mode at the input of stage (IV-s)) for sources' pair (1/4-3). b Measured certified dimension of generated entangled states. Different colors and symbols represent dimensions and the utilized sources, while the light blue line refers to ideal values. Error bars are smaller than the markers.

parameters come only from the phase setting of stage (I). However, using also the phases of the last stages as variational parameters, it would be possible to explore the entire configuration space of two ququarts, as written in Eq. (4). In this case, the expressibility[22,118] of the trial state would be maximized. In the presented VQAs, the trial state with variational parameters coming only from stage (I) has enough expressibility.

# Solving the Hydrogen molecule

By utilizing the bipartite spatially-entangled system of two photons described in "Photonic integrated circuit for four-qubit variational algorithms", we address a quantum chemistry problem. In this case, the algorithm is called VQE $^{19,23}$ , and the cost function is given by the expectation value of the electronic Hamiltonian of molecules. The foundation of the algorithm is the Rayleigh-Ritz variational principle $^{119}$ . In Supplementary Information Section 8, we show more details on the encoding of quantum chemistry problems.

For our demonstration, we choose the simplest molecule, i.e., the Hydrogen molecule  $\mathrm{H}_{2}$ . Using the minimal STO-3G basis set $^{120}$ , composed of 1s orbitals of the individual H atoms with two spin values, we have a total number of atomic orbitals (AOs) equal to 4. Molecular orbitals (MOs) are given by linear combinations of AOs and represent the global and delocalized nature of the electrons in a molecule. The AOs and the MOs of  $\mathrm{H}_{2}$  are sketched in Fig. 4a-b and the 4 MOs are

$$
\begin{array}{l} \left\{\left| \sigma , \uparrow \right\rangle_ {[ e _ {1}} \left| \sigma , \downarrow \right\rangle_ {e _ {2} ]}, \left| \sigma^ {*}, \uparrow \right\rangle_ {[ e _ {1}} \left| \sigma^ {*}, \downarrow \right\rangle_ {e _ {2} ]}, \left| \sigma , \uparrow \right\rangle_ {[ e _ {1}} \left| \sigma^ {*}, \downarrow \right\rangle_ {e _ {2} ]}, \left| \sigma , \downarrow \right\rangle_ {[ e _ {1}} \left| \sigma^ {*}, \uparrow \right\rangle_ {e _ {2} ]} \right\} \\ \text {w h e r e} \quad \left\{ \begin{array}{l} | \sigma , \uparrow / \downarrow \rangle_ {e} \equiv \frac {1}{\sqrt {N _ {+}}} (| A, \uparrow / \downarrow \rangle + | B, \uparrow / \downarrow \rangle), \\ | \sigma^ {*}, \uparrow / \downarrow \rangle_ {e} \equiv \frac {1}{\sqrt {N _ {+}}} (| A, \uparrow / \downarrow \rangle - | B, \uparrow / \downarrow \rangle), \end{array} \right. \tag {7} \\ \end{array}
$$

the square parenthesis denote anti-symmetrization,  $N_{\pm}$  are normalization factors,  $|\mathrm{A} / \mathrm{B},\uparrow /\downarrow \rangle$  denotes the AO 1s are associated with the atom A/B and the spin state  $\uparrow/\downarrow$ . The state  $|\sigma\rangle$  is called bonding molecular orbital (BMO), while the state  $|\sigma^{*}\rangle$  is anti-bonding molecular orbital (AMO). The system of two electrons in  $\mathrm{H}_{2}$  has 4 possible configurations made of combinations of the bonding and anti-bonding orbitals, reported in the left part of Fig. 4b. We utilize the Jordan-Wigner mapping[121] to translate the occupation number states  $|f\rangle$  of each MO involved in the ground state of  $\mathrm{H}_{2}$  into qubit states. The qubit encoding dictionary is given in Fig. 4b, where each qubit represents the occupation number of MOs with the following order:  $\{f_{|\sigma,\uparrow\rangle},f_{|\sigma^{*},\uparrow\rangle},f_{|\sigma,\downarrow\rangle},f_{|\sigma^{*},\downarrow\rangle}\}$ . Moreover, the electronic Hamiltonian is mapped to the equivalent bosonic Hamiltonian given by a linear combination of binary operators made of the identity and Pauli operators,  $\{\mathbf{1},\hat{X},\hat{Y},\hat{Z}\}$ . Then, these operators can be organized into two CGs, which implies two different sets of basis states and their corresponding

![](images/f575be97613850c5d7a113a0147ab60594c872719be1cfa6e0833fc09dea84a5.jpg)

![](images/2fb983a9c4b59ff2e35596e8b1f1a4d8a5beb1ce83f6552a455c736e7c524ac4.jpg)  
Fig. 4 | Hydrogen molecule problem and UCC ansatz. a Graphical representation of atomic orbitals (AOs) and molecular orbitals (MOs) for the Hydrogen molecule  $\mathrm{H}_2$  together with the list of single-electron molecular spin orbitals. The two MOs states  $|\sigma\rangle$  and  $|\sigma^{*}\rangle$  are the bonding and anti-bonding orbital states. b Slater determinants associated with the four configurations of the two electrons in  $\mathrm{H}_2$  mapped to the occupation number states. c Experimental and theoretical values of the  $\mathrm{H}_2$  ground state energy, measured in Hartree, as a function of the variational parameter  $\theta$ , which controls the amount of contribution of the anti-bonding orbital to the

measurement settings for stages (IV-i) and (IV-s) of our Si-PIC. The observables and parameters $^{122}$  composing the  $\mathrm{H}_{2}$  Hamiltonian are given in Supplementary Information Section 8.

Under the Unitary Coupled Cluster (UCC) ansatz $^{123-125}$ , the trial state for  $\mathrm{H}_{2}$  is given by a linear combination of BMO-BMO and AMO-AMO states. In our register, the UCC trial state is parameterized as

$$
| \psi (\boldsymbol {\theta}) \rangle = \cos \boldsymbol {\theta} | 1 0 1 0 \rangle - \sin \boldsymbol {\theta} | 0 1 0 1 \rangle \quad \leftrightarrow \quad | \psi (\boldsymbol {\theta}) \rangle = \cos \boldsymbol {\theta} | 3 \rangle_ {i} | 3 \rangle_ {s} - \sin \boldsymbol {\theta} | 2 \rangle_ {i} | 2 \rangle_ {s}, \tag {8}
$$

where the variational parameter  $\theta$  controls the amount of contribution of AMO-AMO states to the equilibrium configuration, and we present the state written in terms of qubits as well as ququarts. Using the path encoding shown in "Photonic integrated circuit for four-qubit variational algorithms", we realize the state in Eq. (8) by exciting two sources through stage (I) of the Si-PIC. In particular, as it is shown in Eq. (3), we can prepare the desired state by setting to zero two  $\alpha$  parameters, corresponding to routing all the optical input power to only two output paths of stage (I). We chose sources (2,3), because of the high indistinguishability, as shown in Fig. 3a, and we utilized the leftmost MZI of stage (I) to control the optical power ratio between sources (2,3). Thus, the relative phase  $\theta$  between the two arms of the MZI represents the variational parameter  $\theta$  of the UCC ansatz, Eq. (8). Regarding the measurement settings, we have to calculate the expectation values of two CGs of observables. The first CG is composed of projectors associated with the computational basis, while for the second group, the rotated projectors are constructed starting from the eigenvectors of operators  $\hat{X} \otimes \hat{Y}$  and  $\hat{Y} \otimes \hat{X}$ . Supplementary Information Section 8 contains the details of the two measurement settings.

![](images/39a526f0bcb613f5c92c8abf28507898bb22bc75459256fe1f9aeacaf143f4fc.jpg)

![](images/aab814a8c1044fb03ae8dc6abb470c2cb8c7517e3a85a0fe804570d2d77003ac.jpg)  
equilibrium configuration. The energy is calculated within the UCC ansatz, reported above the graph, and using the coefficients  $\{w_k\}_k$  associated with an atomic distance R equal to  $0.736\AA^{122}$ . The red-border inset shows additional data points obtained during the optimization procedure assessing the minimum energy value. d Experimental and theoretical values of the  $\mathrm{H}_{2}$  ground state energy, measured in Hartree, as a function of the atomic distance. Each point is the minimum energy for a fixed atomic distance within the UCC ansatz. The red-border inset shows a zoomed version of the data around the energy minimum.

After setting the problem, we explore the configurations of BMO-BMO and AMO-AMO states in Eq. (8) by varying the variational parameter  $\theta$ . In other words, we are looking at all the Hilbert space of  $\mathrm{H}_2$  within the minimal STO-3G basis set and the UCC ansatz. The experimental results, together with the theoretical ones, are reported in Fig. 4c, d. In Fig. 4c we show the estimated and theoretical values of the  $\mathrm{H}_2$  energy as a function of the variational parameter  $\theta$ , calculated using the coefficients,  $\{w_k\}_k$  in Eq. (1) $^{122}$ , associated with an atomic distance R equal to  $0.736\AA$ . For each distance, i.e., for different weights  $\{w_k\}_k$  in the evaluation of the ground state energy, we fit the data and identify a minimum energy value. Figure 4d summarizes the collection of estimated  $\mathrm{H}_2$  ground state energies as a function of the atomic distance, together with the theoretical values. The analysis of all the Hilbert spaces allows to calculate the ground state energy for all the distances by the classical post-processing of the raw coincidences' data. From this analysis, we found the experimental equilibrium ground energy expectation value of  $-1.1340 \pm 0.0124\mathrm{Ha}$  for  $\theta = 0.11 \pm 0.01$  and  $\mathrm{R} = 0.736\AA$ , which is compatible with the theoretical result of  $-1.1373\mathrm{Ha}^{126}$ .

Once the photonic processor has been tested in preparing all the trial states described by Eq. (8) and performing the two measurement settings associated with the two CGs, the VQA needs a classical optimization routine. We implemented two methods, one based on gradient descent $^{127}$  and another one based on Bayesian optimization $^{128,129}$ . In both cases, we start from the trial state with  $\theta = 0$ , i.e., the BMO-BMO configuration, and we choose the coefficients  $\{w_k\}_k$  associated with an atomic distance equal to  $0.736\mathring{\mathrm{A}}$ . This state is exactly the Hartree-Fock (HF) state of  $\mathrm{H}_{2}$  and in our encoding is represented by the separable two-ququart state  $|3\rangle_i|3\rangle_s$  or equivalently  $|1010\rangle$  in the qubit basis. We observed that the convergence of the gradient-based method is strongly limited by the statistical error and the

![](images/a13d11f28f9828f95478a102d24ec5d39b72b557fb79919debc3b89eef225af0.jpg)  
Fig. 5 | VQE with Bayesian optimization for the Hydrogen molecule. On the left, the evolution of the minimum Bayesian search for the Hydrogen molecule within the minimal STO-3G basis set and the UCC ansatz, and using the coefficients associated with an atomic distance R equal to  $0.736\AA^{122}$ , as reported below the graph. Blue stars are the experimental samples of the expectation value of the Hamiltonian, measured in Hartree, evaluated during the Bayesian optimization, and the light blue line indicates the theoretical value of the ground state energy of the Hydrogen molecule within the minimal STO-3G basis set and the UCC ansatz. Close to every data point, the associated value of the set variational parameter is reported. The red-border inset shows a zoom of the last datum. On the right, the probability amplitudes associated with the first (Hartree-Fock state) and the last steps of the algorithm.  
$|\psi_t\rangle = \cos (\theta)|1010\rangle -\sin (\theta)|0101\rangle$ $\mathrm{R} = 0.736\AA$

![](images/a0dcf05c8f8d067badd408f5d4059be0cbc348f8932b6b52aebbab50c50adee5.jpg)

![](images/24c0af698cb2fe4b26bd203b7b4b42329ce71e2a0952d4d12a0a13f1fefe571b.jpg)

Table 1 | VQE results for the Hydrogen molecule  

<table><tr><td rowspan="2"></td><td colspan="2">θ</td><td colspan="2">{H}</td></tr><tr><td>UCC theory</td><td>Experiment</td><td>UCC theory</td><td>Experiment</td></tr><tr><td>Hartree-Fock ansatz</td><td>0</td><td>0 ± 0.01</td><td>-1.1168 Ha</td><td>-1.1149 ± 0.0055 Ha</td></tr><tr><td>Minimum</td><td>0.11</td><td>0.12 ± 0.01</td><td>-1.1373 Ha</td><td>-1.1343 ± 0.0062 Ha</td></tr></table>

Theoretical and experimental values of energy expectation value and the variational parameter for the initial ansatz, i.e., Hartree-Fock state, and the last trial state of the Bayesian search, shown in Fig. 5.

long measurement time in the gradient evaluation. This limit is well known in the literature, and it is fundamentally due to the quantum projection noise $^{130}$ , manifested through the large number of measurement shots required by the hybrid quantum-classical nature of these algorithms $^{11,131}$ . This aspect is a subject of very active research in the field of variational quantum circuits, which recently brought about a new solution known as the parameter shift rule $^{132,133}$ . Very recently, this technique has also been reported for VQAs implemented on PICs $^{134-136}$ .

Given the known limits of classical gradient-based methods that we also observed, we decided to opt for Bayesian optimization $^{137}$ , a gradient-free method. Our acquisition function is given by the lower confidence bound equal to  $2.5\%$ . The details on the Gaussian Process $^{128,129,138}$  are given in Supplementary Information Section 8. The robustness of this method relies on its gradient-free nature: a small number of evaluations for the cost function and, consequently, a lower machine time. Moreover, the outcome of this algorithm gives global information about the behavior of the cost function and generally needs fewer trials for the variational parameter to converge. Figure 5 summarizes the outcome achieved with the Bayesian optimization. With a good degree of reproducibility and 6-to-13 numbers of iterations, we obtained a very good agreement between the theory and the experiments, with an average value featuring an accuracy of  $0.003\mathrm{Ha}$  with respect to the UCC ansatz. The desired chemical accuracy is approximately  $1.59\mathrm{10}^{-3}\mathrm{Ha}$  per particle, compatible with our results. These results are presented in Table 1, where the first and last steps associated with the Bayesian search shown in Fig. 5 are summarized. We point out that the choice of the HF ansatz does not affect the number of iterations in the case of the Bayesian optimization, contrary to the gradient-descent case.

# Factorizing semiprime numbers

In this section, we address the factorization problem using the VQF algorithm $^{33,34}$ . Given a semiprime number  $N$ , the goal consists of finding the two prime numbers  $(p,q)$  such that  $N = p \cdot q$ . As before, the algorithm starts with the definition of a cost function, whose construction is based on the

following Hamiltonian35

$$
\mathrm {H} _ {\text {f a c t}} = (N - p q) ^ {2}, \quad \text {w h e r e} \quad \left\{ \begin{array}{l} p = 1 + \sum_ {i = 1} ^ {m _ {x}} x _ {i} 2 ^ {i}, \\ q = 1 + \sum_ {i = 1} ^ {m _ {y}} y _ {i} 2 ^ {i}. \end{array} \right. \tag {9}
$$

Here,  $m_{x/y}$  is a number between 1 and  $\lceil \log_2N\rceil -1$  and  $\{x_i,y_i\}_i$  are either 0 or 1. Note that  $(p,q)$  are assumed to be odd numbers different from one, and they are expressed in binary numbers.  $\mathrm{H}_{\mathrm{fact}}$  can be expanded and rewritten as a weighted sum of monomials of the variables  $\{x_i\}_i$  and it is exactly zero for the factorization solution. After inserting the ansatz for  $(p,q)$  in  $\mathrm{H}_{\mathrm{fact}}$ , we encode possible solutions in a string of qubits, i.e.,  $\left|x_1\ldots x_{[\log_2N]}\right\rangle$ , and promote the classical variables to quantum binary operators as follows:  $x_{i}\rightarrow (\mathbb{1} - \hat{Z}_{i}) / 2$ , where  $\hat{Z}_i$  is the Z-Pauli applied to the  $i$ -th qubit. Finally, we obtain the weighted sum of operators containing only the identity and Z-Pauli operators,

$$
\mathrm {H} _ {\text {f a c t}} = \sum_ {k} w _ {k} \hat {O} _ {k}, \quad \text {w h e r e} \hat {O} _ {k} \equiv \bigotimes_ {\hat {\sigma} _ {j} \in \{1, \hat {Z} \}} \hat {\sigma} _ {j}. \tag {10}
$$

The coefficients  $\{w_k\}_k$  depend on  $N$  and on the ansatz in Eq. (9) for  $p$  and  $q$ . Like in VQE, these coefficients can be efficiently calculated with a classical machine. Note that we need only the measurement setting associated with the computational basis.

We chose three different numbers to factorize,  $N = (15, 21, 35)$ , and the ansatz  $p = 4x_{1} + 2x_{2} + 1$  and  $q = 4x_{3} + 2x_{4} + 1$ . Among the 16 possibilities for the variables  $\{x_{i}\}_{i}$ , we exclude the trivial choices with one factor equal to one or  $p = q$  (square numbers) and the options that are symmetric in the exchange of  $p \leftrightarrow q$ . After this fast cleaning, we maintain only one exception among the squares and we end up with four possibilities:  $\{0110 \rightarrow (3, 5), 0101 \rightarrow (3, 3), 1101 \rightarrow (7, 3), 1110 \rightarrow (7, 5)\}$ . In Fig. 6a, we present the problem encoding for this factorization and all the possible solutions, where

![](images/db91de7c960ba852dd98f3740f6dd3d47ea6eee486d68c368999fd84c78f9492.jpg)  
Fig. 6 | VQF results. a The problem encoding in our qubit register for the factorization of (15, 21, 35), followed by the 16 possible solutions where we cross out impossible, trivial choices. b On the left, the evolution of the minimum gradient

![](images/dea6b4a9da0e9f5e25b8cf05c5e2b49f0465a30a67a56939625afb306e8d8c08.jpg)  
descent search for the factorization of (15, 21, 35) using the trial state reported below the graph. On the right, the probability amplitudes associated with the "democratic" initial guess and the final configuration for the factorization of (15, 21, 35).

![](images/3d9a16cd689e519a62d80708c19aa5e8398a677c2feae96eb94d067a2857884c.jpg)

we cross out the excluded ones. Then trial state has the following form

$$
\left| \psi (\alpha) \right\rangle = \alpha_ {1} | 0 1 1 0 \rangle + \alpha_ {2} | 0 1 0 1 \rangle + \alpha_ {3} | 1 1 0 1 \rangle + \alpha_ {4} | 1 1 1 0 \rangle , \tag {11}
$$

where  $\sum_{i=1}^{4} |\alpha_i|^2 = 1$  and the parameters  $\{\alpha_i\}_{i \in 1..4}$  depend on three phases corresponding to the PSs of stage (I). Modulo a linear transformation, the previous state has the same form as the state in Eq. (3). For the minimization of the expectation value of the Hamiltonian in Eq. (10), we have implemented only the gradient descent algorithm. The list of projectors, parameters  $\{w_k\}_k$  and the details on the optimization method are given in Supplementary Information Section 9. The initial guess is given by a "democratic" choice of the  $\alpha$  parameters,  $\alpha_1 = \alpha_2 = \alpha_3 = \alpha_4 = 1/2$ , so we are assigning  $25\%$  probability to the four selected options. In Fig. 6b, we report the evolution of the cost functions during the variational algorithm and the initial and last values of the probability amplitudes of the four selected possible solutions for  $N = (15, 21, 35)$ . At the end of the procedure, almost all the optical power is driven to one source, the (first, third, fourth) one for (15, 21, 35), and the final separable trial state is  $(|0110\rangle, |1101\rangle, |1110\rangle$ , respectively. The convergence reported in Fig. 6b demonstrates the successful factorization of (15, 21, 35) by utilizing our Si-PIC. The same machinery can be used to factorize all odd semiprime numbers up to 49 by suitable choices of the starting ansatz and weights  $\{w_k\}_k$  in Eq. (10). The semiprime numbers up to 49 are (4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49). Our ansatz excludes all even numbers. Even and square numbers are not interesting since their factorization can be done efficiently with classical algorithms. Thus, the remaining numbers up to 49 are (15, 21, 33, 35, 39). If one wants to find the factorization of (33, 39) with our SiPIC, the following ansatz must be used:  $p = 8x_1 + 4x_2 + 2x_3 + 1$  and  $q = 2x_4 + 1$ . Indeed, if  $(x_1, x_2, x_3, x_4)$  is  $(1,0,1,1)$  and  $(1,1,0,1)$ , we obtain  $33 = 11 \cdot 3$  and  $39 = 13 \cdot 3$ , respectively. The expressibility of the ansatz in a generic VQA[22,118] is crucial: the ansatz parametrizing the generic trial state must span a subset of the Hilbert space containing the problem solution.

Contrary to the previous case, the gradient descent algorithm shows more robustness in the result convergence, and we didn't implement the Bayesian optimization. The main reason can be found in the smaller evaluation time needed to evaluate the cost function for one trial, since there is only one CG.

As pointed out in "Photonic integrated circuit for four-qubit variational algorithms", our variational parameters come only from stage (I), while stages (IV-i/s) are used just to execute the projective measurements. By utilizing also those phases as variational parameters, we can explore the most generic state of two ququarts and create an ansatz more generic than the one reported in Eq. (11).

# Discussion

Integrated photonics represents a promising platform for VQAs, since generating and detecting entangled photons, a potentially relevant resource, can be achieved using room temperature technology, contrary to e.g., superconducting and trapped-ion qubits, which require ultra-low temperatures and vacuum conditions. Our experiments, showing VQAs based on on-chip generation and manipulation of single photons at room temperature, mark a significant step along the path to realize a fully-integrated photonic quantum processor. Indeed, due to e.g., the well-established silicon photonics technology and the high fidelity of the operations, larger-scale integrated photonic circuits such as the one reported in ref. 139 can already be utilized to tackle larger problems on a room-temperature and compact device, thus witnessing both relevance and impact of our results.

In Sections "Solving the Hydrogen molecule" and "Factorizing semiprime numbers", we have presented the implementation of two different proof-of-principle VQAs relying on the use of path-entangled ququarts. These have been executed in silicon photonics exploiting on-chip photon pair sources. In quantum silicon photonics, the integration of up to 32 on-chip photon pair sources based on spiral waveguides has already been demonstrated $^{139}$ . Therefore, silicon photonics VQA-based processors able to address large molecules such as water or large semiprime numbers are already within reach of current technology. However, preparing  $d$ -dimensional entangled states in bipartite structures, like the one presented in this work, requires  $(d - 1)$  MZIs in stage (I),  $d$  photon pair sources in stage (II),  $d$  AMZIs in stage (III),  $(d - 1)$  MZIs and an array of  $d$  PSs in both stages (IV-i) and (IV-s), and two SPDs connected to outputs  $|\Gamma \frac{d}{2}\rangle_{i / s}$ . The simplicity of having two SPDs is paid with  $d^2$  measurement setting to retrieve all the various output correlations. In this case, the time required for the implemented VQAs scales quadratically with the dimension  $d^{38,44}$ . If the projections and the multiple projective measurements are substituted with a generic  $\mathrm{SU}(d)$  transformation, the resources in the final stages are  $d(d - 1)$  in

terms of  $\mathrm{MZIs}^{50,51}$ ,  $2d$  in terms of SPDs, and the computational time does not depend on  $d$ . In both cases, if we use the fact that for  $d = 2^n$  we can encode  $n$  qubits, the scaling of the spatial and/or time resources grows manifestly as an exponential of the qubit register dimension.

To explore higher-dimensional Hilbert spaces and tackle larger problems, an alternative strategy to simply increasing the number of paths is required. In particular, two points must be modified: the initialization and the measurement stages. First, to prepare the initial entanglement resource, more Si-PICs could be combined to generate multidimensional entangled states. Each one of these Si-PIC will become a building block of a modular architecture $^{140-142}$ . The Si-PIC, composed of stages (I)-(II)-(III) reported in Fig. 2, can create qudit entangled bipartite states. Without increasing the dimension of the qudit structure too much, e.g., 4- or 8-dimensional, we exploit the advantages of qudit with respect to qubits $^{143,144}$  and avoid the exponential scaling of spatial resources. Then, one can consider fusion-based  $\mathrm{LOQC}^{145}$  manipulation schemes where fusion gates $^{62}$  can be used to entangle different pairs of photons. Second, the multiple projective measurement stage with one detector must be substituted by a stage with generic rotation followed by an array of detectors, one per path. Future investigations about this modular approach are necessary and deserve the appropriate space to be discussed.

# Methods

# The experimental setup and the Si-PIC

The pump light comes from a TUNICS-BT NetTest Wavelength Tunable CW Laser Diode Source, followed by Thorlabs' EDFA100x core-pumped erbium-doped fiber amplifier. The Dense Wavelength Division Multiplexing modules (OpNeti and Precision Micro optics) have 200 GHz bandwidth and 100 GHz FWHM: among the sixteen channels from 21 to 51, we used channels 35, 27 and 41, whose spectral responses are reported in Supplementary Information Section 3.

The SOI photonic chip was fabricated using e-beam lithography based on nano-fabrication by SiPhotonic Technologies ApS via a commercial MPW service. The photonic circuit for the VQAs fits within a size of  $1.5 \times 5$ $\mathrm{mm}^2$ . The silicon waveguide core is  $220~\mathrm{nm}$ -thick and  $500~\mathrm{nm}$ -wide. We used the foundry's PDKs for grating couplers, MMIs, and crossing waveguides. The thermal phase shifters are made of titanium,  $100\mu \mathrm{m}$ -long, and have a tuning efficiency of around  $0.14\mathrm{rad / mA}^2$ . The experiments are performed by using the fundamental electric-transverse mode, and, in order to set the correct polarization, the transmission is maximized through manual fiber polarization controllers based on the different insertion losses of the waveguide modes. In order to improve the visibility of the camera and have an easier coupling, we used a lidless fiber array (Meisu Optics). The fiber array is put on Thorlabs' 6-Axis NanoMax Stage, whose (X, Y, Z) are connected to Thorlabs'  $150\mathrm{V}$  USB Closed-Loop 3-channel piezo-controller.

The detection of the residual pump is done with Thorlabs' PM100USB and Thorlabs' PDA20CS-EC (InGaAs amplified detector). The single photons are detected through two ID-Quantique single photon detector modules, respectively id210 for idler photons and id201 for signal photons. Both single-photon detectors have  $15\%$  efficiency, 20 ns gate width, and 80  $\mu$ s deadtime. Id201 is set in external gating mode, and it is triggered at 500 kHz by id210, which is set in internal gating mode. The output counts of the detectors are collected by time-tagging electronics (Swabian Instruments) connected to a PC.

# Active control and computational times

The photonic chip is glued to a printed board circuit, designed by the electronic workshop of the University of Trento. Current modules (National Instruments) are attached to a power supply (E3631A 80W Triple Output Power Supply) and provide the currents for the thermal phase shifters of the PIC through the printed board circuit. We used MATLAB on our PC to run the self-alignment routine for the piezo-controller, to acquire the data coming from the time-tagging electronics, the power meters, and to set the current at the thermal phase shifters. In particular, in order to maintain the temperature change locally confined, the counts associated with each phase

shifter' setting are collected in two/four intervals of  $30~\mathrm{s}$  until the total number of counts is approximately 2000/4000 twofold events, which directly determines the statistical error. The overall time to calculate the energy expectation value associated with one trial state is given by the time to acquire enough statistics times the number of commuting groups associated with the desired cost function, times 16, i.e., the number of projectors.

We used an on-chip power equal to  $2\mathrm{mW}$  per excited source, which means  $4\mathrm{mW}$  on-chip power for the VQE and  $8\mathrm{mW}$  on-chip power for the VQF. This choice is based on the non-linear characterization results. The overall run time of the analysis summarized in Fig. 4 is around 17 hours, and the overall time of the Bayesian optimization shown in Fig. 5 is around 12 hours. Finally, the overall time of each optimization summarized in Fig. 6 is around 21 hours.

# Data availability

Data underlying the results presented in this paper are not publicly available, but may be obtained from the authors upon reasonable request.

# Code availability

Not applicable.

Received: 10 January 2025; Accepted: 9 June 2025

Published online: 01 July 2025

# References

1. Feynman, R. P. Simulating physics with computers. Int. J. Theor. Phys. 21, 467-488 (1982).  
2. DiVincenzo, D. P. The physical implementation of quantum computation. Fortschr. der Phys. 48, 771-783 (2000).  
3. Bennett, C. H. & DiVincenzo, D. P. Quantum information and computation. Nature 404, 247-255 (2000).  
4. Nielsen, M. A. & Chuang, I. L.Quantum Computation and Quantum Information: 10th Anniversary Edition (Cambridge University, 2010).  
5. Johnson, T. H., Clark, S. R. & Jaksch, D. What is a quantum simulator? EPJ Quantum Technol. 1, 1-12 (2014).  
6. Lloyd, S. Universal quantum simulators. Science 273, 1073-1078 (1996).  
7. Ronnow, T. F. et al. Defining and detecting quantum speedup. Science 345, 420-424 (2014).  
8. Preskill, J. Quantum computing in the NISQ era and beyond. Quantum 2, 79 (2018).  
9. Cerezo, M. et al. Variational quantum algorithms. Nat. Rev. Phys. 3, 625-644 (2021).  
10. Davis, R. What is quantum utility? In IBM Quantum blog https://www.ibm.com/quantum/blog/what-is-quantum-utility (2023).  
11. Tilly, J. et al. The variational quantum eigensolver: A review of methods and best practices. Phys. Rep. 986, 1-128 (2022).  
12. Jozsa, R. Fidelity for mixed quantum states. J. Mod. Opt. 41, 2315-2323 (1994).  
13. James, D. F. V., Kwiat, P. G., Munro, W. J. & White, A. G. Mesurement of qubits. Phys. Rev. A 64, 1-15 (2001).  
14. D'Ariano, G. M., Paris, M. G. & Sacchi, M. F. Quantum tomography. Adv. Imaging Electron Phys. 128, 205-308 (2003).  
15. Altepeter, J. B., James, D. F. & Kwiat, P. G. 4 qubit quantum state tomography. In Paris, M. & R^{\wedge}eháček, J. (eds.) Quantum State Estimation, 113-145 (Springer Berlin Heidelberg, Berlin, Heidelberg, 2004).  
16. Shor, P. Algorithms for quantum computation: discrete logarithms and factoring. In Proceedings 35th Annual Symposium on Foundations of Computer Science, 124-134 (1994).  
17. Kitaev, A. Y. Quantum measurements and the abelian stabilizer problem (1995). https://arxiv.org/abs/quant-ph/9511026.  
18. Cleve, R., Ekert, A., Macchiavello, C. & Mosca, M. Quantum algorithms revisited. Proc. R. Soc. Lond. Ser. A: Math., Phys. Eng. Sci. 454, 339-354 (1998).

19. McClean, J. R., Romero, J., Babbush, R. & Aspuru-Guzik, A. The theory of variational hybrid quantum-classical algorithms. N. J. Phys. 18, 023023 (2016).  
20. O'Malley, P. et al. Scalable quantum simulation of molecular energies. Phys. Rev. X 6 https://doi.org/10.1103/PhysRevX.6.031007 (2016).  
21. Kandala, A. et al. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. Nature 549, 242-246 (2017).  
22. Holmes, Z., Sharma, K., Cerezo, M. & Coles, P. J. Connecting ansatz expressibility to gradient magnitudes and barren plateaus. PRX Quantum 3 https://doi.org/10.1103/PRXQuantum.3.010313 (2022).  
23. Peruzzo, A. et al. A variational eigenvalue solver on a photonic quantum processor. Nat. Commun. 5 https://doi.org/10.1038/ncomms5213 (2014).  
24. Colless, J. et al. Computation of molecular spectra on a quantum processor with an error-resilient algorithm. Phys, Rev, X 8 https://doi.org/10.1103/PhysRevX.8.011021 (2018).  
25. Qing, M. & Xie, W. Use VQE to calculate the ground energy of hydrogen molecules on IBM Quantum (2023).  
26. Bentellis, A., Matic-Flierl, A., Mendl, C. B. & Lorenz, J. M. Benchmarking the variational quantum eigensolver using different quantum hardware. In 2023 IEEE International Conference on Quantum Computing and Engineering (QCE), vol. 01, 518-523 (2023).  
27. Shen, Y. et al. Quantum implementation of the unitary coupled cluster for simulating molecular electronic structure. Physi. Rev. A 95 https://doi.org/10.1103/PhysRevA.95.020501 (2017).  
28. Hempel, C. et al. Quantum chemistry calculations on a trapped-ion quantum simulator. Phys. Rev. X 8, 031022 (2018).  
29. Kokail, C. et al. Self-verifying variational quantum simulation of lattice models. Nature 569, 355-360 (2019).  
30. Zhang, Y. et al. Variational quantum eigensolver with reduced circuit complexity. npj Quantum Inf. 8 (2022).  
31. Kandala, A. et al. Error mitigation extends the computational reach of a noisy quantum processor. Nature 567, 491-495 (2019).  
32. Nam, Y. et al. Ground-state energy estimation of the water molecule on a trapped-ion quantum computer. npj Quantum Inf. 6, 33 (2020).  
33. Anschuetz, E., Olson, J., Aspuru-Guzik, A. & Cao, Y. Variational quantum factoring. In Feld, S. & Linnhoff-Popien, C. (eds.) Quantum Technology and Optimization Problems, 74-85 (Springer International Publishing, Cham, 2019).  
34. Zhang, X. & Zhang, F. Variational quantum computation integer factorization algorithm. Int. J. Theor. Phys. 62, 245 (2023).  
35. Selvarajan, R., Dixit, V., Cui, X., Humble, T. S. & Kais, S. Prime factorization using quantum variational imaginary time evolution. Sci. Rep. 11, 20835 (2021).  
36. Agresti, I. et al. Demonstration of hardware efficient photonic variational quantum algorithm (2024).  
37. Hamilton, C. S. et al. Gaussian boson sampling. Phys. Rev. Lett. 119, 170501 (2017).  
38. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
39. Adcock, J. C., Vigliar, C., Santagati, R., Silverstone, J. W. & Thompson, M. G. Programmable four-photon graph states on a silicon chip. Nat. Commun. 10, 3528 (2019).  
40. Wang, H. et al. Boson sampling with 20 input photons and a 60-mode interferometer in a  $10^{14}$ -dimensional Hilbert space. Phys. Rev. Lett. 123, 250503 (2019).  
41. Llewellyn, D. et al. Chip-to-chip quantum teleportation and multiphoton entanglement in silicon. Nat. Phys. 16, 148-153 (2019).  
42. Bartlett, B. & Fan, S. Universal programmable photonic architecture for quantum information processing. Phys. Rev. A 101, 042319 (2020).

43. Wang, J., Sciarrino, F., Laing, A. & Thompson, M. G. Integrated photonic quantum technologies. Nat. Photonics 14, 273-284 (2020).  
44. Vigliar, C. et al. Error-protected qubits in a silicon photonic chip. Nat. Phys. 17, 1137-1143 (2021).  
45. Adcock, J. C. et al. Advances in silicon quantum photonics. IEEE J. Sel. Top. Quantum Electron. 27, 1-24 (2021).  
46. Lee, J.-M. et al. Quantum states generation and manipulation in a programmable silicon-photonic four-qubit system with high-fidelity and purity. APL Photonics 9, 076110 (2024).  
47. O'Brien, J. L. Optical quantum computing. Science 318, 1567-1570 (2007).  
48. Tan, S.-H. & Rohde, P. P. The resurgence of the linear optics quantum interferometer - recent advances & applications. Rev. Phys. 4, 100030 (2019).  
49. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
50. Reck, M., Zeilinger, A., Bernstein, H. J. & Bertani, P. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58-61 (1994).  
51. Clements, W. R., Humphreys, P. C., Metcalf, B. J., Kolthammer, W. S. & Walmsley, I. A. Optimal design for universal multiport interferometers. Optica 3, 1460-1465 (2016).  
52. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
53. Cerf, N. J., Adami, C. & Kwiat, P. G. Optical simulation of quantum logic. Phys. Rev. A 57, R1477-R1480 (1998).  
54. Pittman, T., Jacobs, B. & Franson, J. Probabilistic quantum logic operations using polarizing beam splitters. Phys. Rev. A 64, 062311 (2001).  
55. Ralph, T. C., White, A. G., Munro, W. J. & Milburn, G. J. Simple scheme for efficient linear optics quantum gates. Phys. Rev. A 65, 012314 (2001).  
56. Pittman, T., Jacobs, B. & Franson, J. Demonstration of nondeterministic quantum logic operations using linear optical elements. Phys. Rev. Lett. 88, 257902 (2002).  
57. Hofmann, H. F. & Takeuchi, S. Quantum phase gate for photonic qubits using only beam splitters and postselection. Phys. Rev. A 66, 024308 (2002).  
58. Ralph, T. C., Langford, N. K., Bell, T. B. & White, A. G. Linear optical controlled-not gate in the coincidence basis. Phys. Rev. A 65, 062324 (2002).  
59. O'Brien, J. L., Pryde, G. J., White, A. G., Ralph, T. C. & Branning, D. Demonstration of an all-optical quantum controlled-NOT gate. Nature 426, 264-267 (2003).  
60. Gasparoni, S., Pan, J.-W., Walther, P., Rudolph, T. & Zeilinger, A. Realization of a photonic controlled-not gate sufficient for quantum computation. Phys. Rev. Lett. 93, 020504 (2004).  
61. Zhao, Z. et al. Experimental demonstration of a nondestructive controlled-not quantum gate for two independent photon qubits. Phys. Rev. Lett. 94, 030501 (2005).  
62. Browne, D. E. & Rudolph, T. Resource-efficient linear optical quantum computation. Phys. Rev. Lett. 95, 010501 (2005).  
63. Fiurášek, J. Linear-optics quantum Toffoli and Fredkin gates. Phys. Rev. A 73, 062313 (2006).  
64. Bao, X.-H. et al. Optical nondestructive controlled-not gate without using entangled photons. Phys. Rev. Lett. 98, 170502 (2007).  
65. Okamoto, R., O'Brien, J. L., Hofmann, H. F. & Takeuchi, S. Realization of a Knill-Laflamme-Milburn controlled-not photonic quantum circuit combining effective optical nonlinearities. Proc. Natl Acad. Sci. 108, 10067-10071 (2011).  
66. Li, H. et al. Reconfigurable controlled two-qubit operation on a quantum photonic chip. N. J. Phys. 13, 115009 (2011).  
67. Li, J.-P. et al. Heralded nondestructive quantum entangling gate with single-photon sources. Phys. Rev. Lett. 126, 140501 (2021).

68. Lee, J.-M. et al. Controlled-not operation of sin-photonic circuit using photon pairs from silicon-photonic circuit. Opt. Commun. 509, 127863 (2022).  
69. Liu, W.-Q., Wei, H.-R. & Kwek, L.-C. Universal quantum multi-qubit entangling gates with auxiliary spaces. Adv. Quantum Technol. 5, 2100136 (2022).  
70. Li, Y. et al. Quantum Fredkin and Toffoli gates on a versatile programmable silicon photonic chip. npj Quantum Inf. 8, 112 (2022).  
71. Li, M. et al. On-chip path encoded photonic quantum Toffoli gate. Photonics Res. 10, 1533-1542 (2022).  
72. Liu, W.-Q. & Wei, H.-R. Linear optical universal quantum gates with higher success probabilities. Adv. Quantum Technol. 6, 2300009 (2023).  
73. Kwon, Y., Baldazzi, A., Pavesi, L. & Choi, B.-S. Quantum circuit mapping for universal and scalable computing in mzi-based integrated photonics. Opt. Express 32, 12852-12881 (2024).  
74. Baldazzi, A. & Pavesi, L. Universal multiport interferometers for post-selected multi-photon gates. Adv. Quant. Technol. 2400418 (2024).  
75. Liu, W.-Q. & Wei, H.-R. Quantum gate teleportation with the superposition of causal order. Phys. Rev. Appl. 23, 014064 (2025).  
76. O'Brien, J. L., Furusawa, A. & Vučković, J. Photonic quantum technologies. Nat. Photonics 3, 687-695 (2009).  
77. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
78. Laing, A. et al. High-fidelity operation of quantum photonic circuits. Appl. Phys. Lett. 97, 211109 (2010).  
79. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
80. Zhong, H.-S. et al. Quantum computational advantage using photons. Science 370, 1460-1463 (2020).  
81. Alexander, K. et al. A manufacturable platform for photonic quantum computing. Nature 641, 876-883 (2025).  
82. Briegel, H. J. & Raussendorf, R. Persistent entanglement in arrays of interacting particles. Phys. Rev. Lett. 86, 910-913 (2001).  
83. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
84. Harris, N. C. et al. Large-scale quantum photonic circuits in silicon. Nanophotonics 5, 456-468 (2016).  
85. Qiang, X. et al. Large-scale silicon quantum photonics implementing arbitrary two-qubit processing. Nat. photonics 12, 534-539 (2018).  
86. Bogaerts, W. & Chrostowski, L. Silicon photonics circuit design: methods, tools and challenges. *Laser Photonics* Rev. **12**, 1700237 (2018).  
87. Bogaerts, W. et al. Programmable photonic circuits. Nature 586, 207-216 (2020).  
88. Moody, G. et al. 2022 roadmap on integrated quantum photonics. J. Phys.: Photonics 4, 012501 (2022).  
89. Luo, W. et al. Recent progress in quantum photonic chips for quantum communication and the internet. Light Sci. Appl. 12, 175 (2023).  
90. Yu, Y. et al. Programmable silicon-photonic quantum simulator based on a linear combination of unitaries. Photonics Res. 12, 1760-1767 (2024).  
91. Huang, J. et al. Demonstration of hypergraph-state quantum information processing. Nat. Commun. 15, 2601 (2024).  
92. Maring, N. et al. A versatile single-photon-based quantum computing platform. Nat. Photonics 18, 603-609 (2024).  
93. Fukuda, H. et al. Four-wave mixing in silicon wire waveguides. Opt. Express 13, 4629-4637 (2005).  
94. Clemmen, S. et al. Continuous wave photon pair generation in silicon-on-insulator waveguides and ring resonators. Opt. Express 17, 16558-16570 (2009).  
95. Helt, L. G., Yang, Z., Liscidini, M. & Sipe, J. E. Spontaneous four-wave mixing in microring resonators. Opt. Lett. 35, 3006-3008 (2010).

96. Azzini, S. et al. Ultra-low power generation of twin photons in a compact silicon ring resonator. Opt. Express 20, 23100-23107 (2012).  
97. Engin, E. et al. Photon pair generation in a silicon micro-ring resonator with reverse bias enhancement. Opt. Express 21, 27826-27834 (2013).  
98. Schmittberger Marlow, B. L. Degenerate four-wave-mixing as a low-power source of squeezed light. Opt. Express 28, 38169 (2020).  
99. Mancini, S., Giovannetti, V., Vitali, D. & Tombesi, P. Entangling macroscopic oscillators exploiting radiation pressure. Phys. Rev. Lett. 88 https://doi.org/10.1103/PhysRevLett.88.120401 (2002).  
100. Howell, J. C., Bennink, R. S., Bentley, S. J. & Boyd, R. W. Realization of the Einstein-Podolsky-Rosen paradox using momentum- and position-entangled photons from spontaneous parametric down conversion. Phys. Rev. Lett. 92, 210403 (2004).  
101. Ali Khan, I. & Howell, J. C. Experimental demonstration of high two-photon time-energy entanglement. Phys. Rev. A 73, 031801 (2006).  
102. Cheng, L., Mao, S., Li, Z., Han, Y. & FU, H. Y. Grating couplers on silicon photonics: Design principles, emerging trends and practical issues. Micromachines 11, 666 (2020).  
103. Soldano, L. & Pennings, E. C. M. Optical multi-mode interference devices based on self-imaging: principles and applications. J. Lightw. Technol. 13, 615-627 (1995).  
104. Chen, H. & Poon, A. W. Low-loss multimode-interference-based crossings for silicon wire waveguides. IEEE photonics Technol. Lett. 18, 2260-2262 (2006).  
105. Harris, N. C. et al. Efficient, compact and low-loss thermo-optic phase shifter in silicon. Opt. Express 22, 10487-10493 (2014).  
106. Jacques, M. et al. Optimization of thermo-optic phase-shifter design and mitigation of thermal crosstalk on the SOI platform. Opt. Express 27, 10456-10471 (2019).  
107. Lal, N., Mishra, S. & Singh, R. P. Indistinguishable photons. AVS Quantum Sci. 4, 021701 (2022).  
108. Lee, J.-M. et al. Do different kinds of photon-pair sources have the same indistinguishability in quantum silicon photonics? Photonics Res. 11, 1820 (2023).  
109. El Shamy, R. S., Afifi, A. E., Badr, M. M. & Swillam, M. A. Modelling, characterization, and applications of silicon on insulator loop terminated asymmetric Mach-Zehnder interferometer. Sci. Rep. 12, 3598 (2022).  
110. Plesch, M. & Brukner, C. Quantum-state preparation with universal gate decompositions. Phys. Rev. A 83 https://doi.org/10.1103/PhysRevA.83.032302 (2011).  
111. Vidal, G. & Dawson, C. M. Universal quantum circuit for two-qubit transformations with three controlled-not gates. Phys. Rev. A 69 https://doi.org/10.1103/PhysRevA.69.010301 (2004).  
112. Huber, M. & de Vicente, J. I. Structure of multidimensional entanglement in multipartite systems. Phys.Rev. Lett. 110 https://doi.org/10.1103/PhysRevLett.110.030501 (2013).  
113. Silverstone, J. W. et al. On-chip quantum interference between silicon photon-pair sources. Nat. Photonics 8, 104-108 (2013).  
114. Faruque, I. I., Sinclair, G. F., Bonneau, D., rarity, J. G. & Thompson, M. G. On-chip quantum interference with heralded photons from two independent micro-ring resonator sources in silicon photonics. Opt. Express 26, 20379 (2018).  
115. Vernon, Z. et al. Truly unentangled photon pairs without spectral filtering. Opt. Lett. 42, 3638 (2017).  
116. Signorini, S. & Pavesi, L. On-chip heralded single photon sources. AVS Quantum Sci. 2, 041701 (2020).  
117. Paesani, S. et al. Near-ideal spontaneous photon sources in silicon quantum photonics. Nat. Commun. 11 https://doi.org/10.1038/s41467-020-16187-8 (2020).  
118. Tangpanitanon, J., Thanasilp, S., Dangniam, N., Lemonde, M.-A. & Angelakis, D. G. Expressibility and trainability of parametrized analog quantum systems for machine learning applications. Phys.

Revi Res. 2 https://doi.org/10.1103/PhysRevResearch.2.043364 (2020).  
119. Helgaker, T., Jorgensen, P. & Olsen, J. Molecular Electronic-Structure Theory (Wiley, 2014).  
120. Stewart, R. F. Small Gaussian expansions of Slater-type orbitals. J. Chem. Phys. 52, 431-438 (1970).  
121. McArdle, S., Endo, S., Aspuru-Guzik, A., Benjamin, S. C. & Yuan, X. Quantum computational chemistry. Rev. Mod. Phys. 92 https://doi.org/10.1103/RevModPhys.92.015003 (2020).  
122. Smith, D. G. A. et al. PSI4 1.4: Open-source software for high-throughput quantum chemistry. J. Chem. Phys. 152, 184108 (2020).  
123. Hoffmann, M. R. & Simons, J. A unitary multiconfigurational coupled-cluster method: Theory and applications. J. Chem. Phys. 88, 993-1002 (1988).  
124. Bartlett, R. J., Kucharski, S. A. & Noga, J. Alternative coupled-cluster ansätze ii. The unitary coupled-cluster method. Chem. Phys. Lett. 155, 133-140 (1989).  
125. Romero, J. et al. Strategies for quantum computing molecular energies using the unitary coupled cluster ansatz. Quantum Sci. Technol. 4, 014008 (2018).  
126. Graves, V., Sunderhauf, C., Blunt, N. S., Izsák, R. & Szöri, M. The electronic structure of the hydrogen molecule: A tutorial exercise in classical and quantum computation (2023).  
127. Boyd, S. & Vandenberghe, L. Convex optimization (Cambridge University Press, 2004).  
128. MacKay, D. J. C. Information Theory, Inference & Learning Algorithms (Cambridge University Press, USA, 2002).  
129. Garnett, R. Bayesian Optimization (Cambridge University Press, 2023).  
130. Itano, W. M. et al. Quantum projection noise: Population fluctuations in two-level systems. Phys. Rev. A 47, 3554-3570 (1993).  
131. Scriva, G., Astrakhantsev, N., Pilati, S. & Mazzola, G. Challenges of variational quantum optimization with measurement shot noise. Phys. Rev. A 109 https://doi.org/10.1103/PhysRevA.109.032408 (2024).  
132. Schuld, M., Bergholm, V., Gogolin, C., Izaac, J. & Killoran, N. Evaluating analytic gradients on quantum hardware. Phys. Rev. A 99, 032331 (2019).  
133. Li, J., Yang, X., Peng, X. & Sun, C.-P. Hybrid quantum-classical approach to quantum optimal control. Phys. Rev. Lett. 118, 150503 (2017).  
134. Cimini, V. et al. Variational quantum algorithm for experimental photonic multiparameter estimation. npj Quant. Inf. 10 https://doi.org/10.1038/s41534-024-00821-0 (2024).  
135. Hoch, F. et al. Variational approach to photonic quantum circuits via the parameter shift rule (2024).  
136. Pappalardo, A. et al. Photonic parameter-shift rule: Enabling gradient computation for photonic quantum computers. Phys. Rev. A 111, 032429 (2025).  
137. Iannelli, G. & Jansen, K. Noisy Bayesian optimization for variational quantum eigensolvers. In Proceedings of The 38th International Symposium on Lattice Field Theory - PoS (LATTICE2021), vol. 396, 251 (2022).  
138. Mockus, J. The Bayesian approach to global optimization. In Springer (ed.) System Modeling and Optimization: Proceedings of the 10th IFIP Conference, New York City, USA, August 31–September 4, 1981, 473–481 (2005).  
139. Bao, J. et al. Very-large-scale integrated quantum graph photonics. Nat. Photon. https://doi.org/10.1038/s41566-023-01187-z (2023).  
140. Monroe, C. et al. Large-scale modular quantum-computer architecture with atomic memory and photonic interconnects. Phys. Rev. A 89, 022317 (2014).  
141. Pirker, A., Wallnofer, J. & Dur, W. Modular architectures for quantum networks. N. J. Phys. 20, 053054 (2018).

142. Aghaee Rad, H. et al. Scaling and networking a modular photonic quantum computer. Nature 1-8 https://doi.org/10.1038/s41586-024-08406-9 (2025).  
143. Wang, Y., Hu, Z., Sanders, B. C. & Kais, S. Qudits and high-dimensional quantum computing. Front. Phy. 8 https://doi.org/10.3389/fphy.2020.589504 (2020).  
144. Meth, M. et al. Simulating two-dimensional lattice gauge theories on a qudit quantum computer. Nat. Phys. 1-7 https://doi.org/10.1038/s41567-025-02797-w (2025).  
145. Bartolucci, S. et al. Fusion-based quantum computation. Nat. Commun. 14, 912 (2023).

# Acknowledgements

The work was supported by the Horizon 2020 Framework Program (899368), Horizon Widera 2023 (101160101), and by the Provincia Autonoma di Trento through the Q@TN joint laboratory. We acknowledge the work of Nicola Furlan (University of Trento) for the PCB design, Sara Ferrari (Fondazione Bruno Kessler) for the wire-bonding service, and the master students Nicolò Broseghini and Leonardo Cattarin for the self-alignment code and for the initial work on the setup, respectively.

# Author contributions

M.B. conceived the idea of the PIC. A.B. simulated the PIC's components and designed the PIC. A.B. and M.S. created the setup. A.B. carried out the experiments and the analysis of the results. A.B. took the lead in writing the manuscript. All authors provided critical feedback and helped shape the research, analysis, and manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41534-025-01061-6.

Correspondence and requests for materials should be addressed to Alessio Baldazzi.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025