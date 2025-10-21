# High-dimensional one-way quantum processing implemented on  $d$ -level cluster states

Christian Reimer $^{1,2,15}$ , Stefania Sciara $^{1,3}$ , Piotr Roztocki $^{1}$ , Mehedi Islam $^{1}$ , Luis Romero Cortés $^{1}$ , Yanbing Zhang $^{1}$ , Bennet Fischer $^{1}$ , Sébastien Loranger $^{4}$ , Raman Kashyap $^{4,5}$ , Alfonso Cino $^{3}$ , Sai T. Chu $^{6}$ , Brent E. Little $^{7}$ , David J. Moss $^{8}$ , Lucia Caspani $^{9}$ , William J. Munro $^{10,11}$ , José Azaña $^{1}$ , Michael Kues $^{1,12,15*}$  and Roberto Morandotti $^{1,13,14*}$

Taking advantage of quantum mechanics for executing computational tasks faster than classical computers or performing measurements with precision exceeding the classical limit requires the generation of specific large and complex quantum states. In this context, cluster states are particularly interesting because they can enable the realization of universal quantum computers by means of a 'one-way' scheme where processing is performed through measurements. The generation of cluster states based on sub-systems that have more than two dimensions,  $d$ -level cluster states, provides increased quantum resources while keeping the number of parties constant, and also enables novel algorithms. Here, we experimentally realize, characterize and test the noise sensitivity of three-level, four-partite cluster states formed by two photons in the time and frequency domain, confirming genuine multi-partite entanglement with higher noise robustness compared to conventional two-level cluster states. We perform proof-of-concept high-dimensional one-way quantum operations, where the cluster states are transformed into orthogonal, maximally entangled  $d$ -level two-partite states by means of projection measurements. Our scalable approach is based on integrated photonic chips and optical fibre communication components, thus achieving new and deterministic functionalities.

Cluster states are a particularly important class of multi-partite states (that is, those formed by more than two parties, such as multiple atoms, photons and so on) characterized by two unique properties: maximal connectedness $^4$  (that is, any two parties of the state can be projected into a maximally entangled state through measurements on the remaining parties), as well as by the highest persistency of entanglement $^4$  (that is, cluster states require a maximal number of projection measurements to fully destroy entanglement in the system). These properties make cluster states equivalent to universal one-way (also called measurement-based) quantum computers $^5$ , where different algorithms can be implemented by performing measurements on the individual parties of the cluster

states $^{5,6}$ . This approach greatly simplifies quantum processing, since measurement settings can be usually implemented more easily than the gate operations required in other approaches $^{1,14}$ . Furthermore, cluster states have structural properties that protect the quantum information; that is, they enable topological quantum error correction $^{11}$  for minimizing computation errors. Due to the significant importance of cluster states, they have been studied in many different platforms. In particular, experimental realizations can be separated into two classes: discrete two-level $^{6,11-13}$  (that is, qubit) and continuous-variable $^{15,16}$  cluster states. Continuous-variable systems are intrinsically high-dimensional, and they can be achieved using squeezed states $^{15,16}$ . However, the quantum resource of these states relies on the level of squeezing, which is very sensitive to noise $^{17}$ . In contrast, discrete quantum states are less sensitive to noise than squeezed states $^{17}$ , and even more importantly, their individual modes can be fully accessed and individually manipulated, making their use especially appealing.

Nevertheless, increasing the number of particles to boost the computational resource comes at the price of significantly reduced coherence time and detection rates, and increased sensitivity to noise, restricting the realization of discrete cluster states to a record of eight qubits[1]. In a novel approach, the use of discrete yet  $d$ -level (that is, qudit) entangled states has the potential to address several limitations of qubit cluster states. First, the quantum resource can be increased without changing the number of particles; second,  $d$ -level quantum states enable the implementation of highly efficient computation protocols; and third, higher dimensions reduce the noise sensitivity of cluster states. The experimental realization of  $d$ -level multi-partite cluster states is the key missing piece required to exploit these important benefits for high-dimensional quantum computation[7]. Unfortunately, today's established quantum systems are ill-suited for increasing the dimensionality of discrete multipartite entangled states. For example, atomic[18] and superconducting[19] systems are mainly based on qubit schemes, and demonstrated high-dimensional photonic systems[20,21] become experimentally complex and inefficient and typically suffer from degraded state

$^{1}$ Institut National de la Recherche Scientifique (INRS-EMT), Varennes, Quebec, Canada.  $^{2}$ John A. Paulson School of Engineering and Applied Sciences, Harvard University, Cambridge, MA, USA.  $^{3}$ Department of Energy, Information Engineering and Mathematical Models, University of Palermo, Palermo, Italy.  $^{4}$ Engineering Physics Department, Polytechnique Montreal, Montreal, Quebec, Canada.  $^{5}$ Electrical Engineering Department, Polytechnique Montreal, Montreal, Quebec, Canada.  $^{6}$ Department of Physics and Material Science, City University of Hong Kong, Hong Kong, China.  $^{7}$ State Key Laboratory of Transient Optics and Photonics, Xi'an Institute of Optics and Precision Mechanics, Chinese Academy of Science, Xi'an, China.  $^{8}$ Centre for Micro Photonics, Swinburne University of Technology, Hawthorn, Victoria, Australia.  $^{9}$ Institute of Photonics, Department of Physics, University of Strathclyde, Glasgow, UK.  $^{10}$ NTT Basic Research Laboratories and NTT Research Center for Theoretical Quantum Physics, NTT Corporation, Kanagawa, Japan.  $^{11}$ National Institute of Informatics, Tokyo, Japan.  $^{12}$ School of Engineering, University of Glasgow, Glasgow, UK.  $^{13}$ Institute of Fundamental and Frontier Sciences, University of Electronic Science and Technology of China, Chengdu, China.  $^{14}$ ITMO University, St Petersburg, Russia.  $^{15}$ These authors contributed equally: Christian Reimer, Michael Kues. *e-mail: michaek.kues@glasgow.ac.uk; morandotti@emt.inrs.ca

![](images/3e9504e3db2a7cb9254740f30170cc18d60d5b2059e34c03c5cd28db4082739a.jpg)  
a

![](images/8f0301f0b39114f42a0e270e8fa24cba648ee0c81c0e9a331c3a9d632f0f562d.jpg)

![](images/b6d8062996a9adc9658b667ecfbad35a516265ba38637abaf8a819136c001bde.jpg)

![](images/e97ddae4cde0ad521a19d117cd50ca2cdebccce0050fe04d1cb257ab4efdd3d1.jpg)  
b

![](images/8726f9efaff705d91c64bc2a01cacc1400d68671e69cb1113a2feb01bba35e24.jpg)

![](images/b9d7b4852b822bca4b6430681c3dcbcda0a035b35187c6a69fc8c9008f960ae4.jpg)

![](images/fa33f61f7915383f07f5dff4e473da96b74086d5caf4048522181dfbc2b2f854.jpg)  
c

![](images/15805339362eb25ab08051584a21d51dafca82f97bd9d47cf88f6795fbfcaed3.jpg)  
Fig. 1 | Time-frequency hyper-entanglement scheme. a, An optical pulse train (composed of three pulses in this example) excites a nonlinear medium where photon pairs (signal and idler) are simultaneously generated via a nonlinear spontaneous process (NSP, here four-wave mixing), in a superposition of several time modes (here  $d = 3$ , given by the number of pulses) generating a  $d$ -level time-bin entangled two-photon state. b, A single pulse excites a nonlinear medium placed inside a cavity (composed by two semi-reflective mirrors), where photon pairs are created over a broad bandwidth in a superposition of several spectral modes (here  $d = 3$ , given by the number of selected cavity resonances per photon), leading to a  $d$ -level frequency-bin entangled state. c, An optical pulse train excites a nonlinear cavity (merging the concepts of a and b) generating a simultaneously time- and frequency-bin entangled photon pair (that is, a  $d$ -level hyper-entangled state).

![](images/5b54e68a788eca21bba36b6c3a3461d30a352eb0cacfb2db2d054d56d888012c.jpg)

purity when the number of photons used increases. The only  $d$ -level quantum states with more than two parties generated so far are three-level, three-photon states in a bulk, free-space set-up[22]. Cluster states with two and three parties are locally equivalent to Bell and Greenberger-Horne-Zeilinger (GHZ) states, respectively[4], while genuine discrete  $d$ -level cluster states require at least four parties[4]. To date, these states have not been realized, nor have their entanglement properties and their tolerance to noise been investigated.

Here, we present a general approach to prepare and coherently manipulate discrete  $d$ -level multi-partite quantum systems based on the simultaneous entanglement—that is, hyper-entanglement[23]—of two photons in time and frequency, by exploiting integrated photonic chips combined with fibre-optics telecommunications components[9,10]. Using this method, we present the first experimental realization and characterization of qudit cluster states as well as the first hyper-entangled state employing only a single degree of freedom. Further, we use these states to perform proof-of-concept high-dimensional one-way quantum processing.

As a basis for the generation of  $d$ -level cluster states, we create hyper-entangled states that support higher dimensions. Hyperentangled photon states usually employ simultaneously mul

tiple different and independent degrees of freedom, which can be described as distinct parties of the state. These states can therefore be treated as multi-partite although the number of physical photons is not increased (see Methods). Until now, such states have been realized only using combinations of fully independent degrees of freedom, described by commuting operators, such as polarization, optical paths and temporal modes[23-26]. Here we used intrinsically linked and non-commuting observables, two discrete forms of energy-time entanglement, namely time-bin and frequency-bin[10]. Time-bin entanglement refers to states where the photons are in a superposition of well-defined and distinct temporal modes, while frequency-bin entangled states are characterized by discrete and non-overlapping frequency modes. Time-bin entanglement can be generated by exciting a spontaneous parametric process in an optical nonlinear medium with multiple phase-locked pulses[9] (see Fig. 1a). On the other hand, frequency-bin entanglement can be realized when the nonlinear medium is placed within an optical resonator, where the emission bandwidth covers multiple resonances[10] (see Fig. 1b). Remarkably, if the time-frequency product corresponding to the individual modes is well above the quantum limit (see Methods), frequency-bin and time-bin entanglement become

![](images/41b2bb8524e1c172bb68b3d2c33d9dc167917da7e47fae8c4be0226fa4a7211a.jpg)  
Fig. 2 | Generation of  $d$ -level cluster states with a controlled phase gate. The two-photon  $d$ -level hyper-entangled state is simultaneously composed of three temporal modes  $\left|1\right\rangle$ ,  $\left|2\right\rangle$  and  $\left|3\right\rangle$  and three frequency modes  $\left|a\right\rangle$ ,  $\left|b\right\rangle$  and  $\left|c\right\rangle$  per signal and idler photon, given by the state wavefunction  $|\Psi_{\mathrm{H}}\rangle$  (the real part of the associated density matrix is depicted in the top left panel). A controlled phase gate gives access to the individual terms of the quantum state. This was realized by temporally dispersing the individual frequency modes into different time slots via a fibre Bragg grating array (that is, by means of frequency-to-time mapping) such that each individual state term has its own time slot (see the middle panel). An electro-optical modulator was used to change the phase of the individual state terms, here by  $\alpha /2$  and  $\beta /2$  (see the middle panel). The photons then enter the fibre Bragg grating array from the opposite end, such that the frequency-to-time mapping is coherently reversed. By choosing the phases  $\alpha = 2\pi /3$  and  $\beta = -2\pi /3$ , the hyper-entangled state is transformed into a  $d$ -level cluster state  $|\Psi_{\mathrm{C}}\rangle$ , where the two grey shading tones indicate the two opposite phase changes (the real part of the associated density matrix is shown in the top right panel).

independently controllable, allowing one to generate hyper-entangled, multi-partite states (see Methods). Such hyper-entangled states can be produced by exciting the nonlinear element, placed inside the resonator, with a coherent set of multiple pulses (see Fig. 1c), as long as the pulse separation is much larger than the photon lifetime in the resonator. In this case, the time-bin component can be fully controlled in the temporal domain, while the frequency-bin component can be completely and independently controlled in the frequency domain.

In our experimental implementation, we produced photon pairs using the nonlinear process of spontaneous four-wave mixing within a microring resonator (see Methods). By exciting the resonator with three phase-locked pulses and considering three frequency mode pairs, we generated photon states simultaneously entangled in time and frequency, described by the following expression (equation (1)):

$$
\begin{array}{l} \left| \Psi_ {\text {H y p e r}} \right\rangle = \left(\left| 1 _ {s}, 1 _ {i} \right\rangle + \left| 2 _ {s}, 2 _ {i} \right\rangle + \left| 3 _ {s}, 3 _ {i} \right\rangle\right) \\ \otimes \left(\left| a _ {s}, a _ {i} \right\rangle + \left| b _ {s}, b _ {i} \right\rangle + \left| c _ {s}, c _ {i} \right\rangle\right) \\ = \left| 1 _ {s}, 1 _ {i}, a _ {s}, a _ {i} \right\rangle + \left| 1 _ {s}, 1 _ {i}, b _ {s}, b _ {i} \right\rangle \\ + \left| 1 _ {s}, 1 _ {i}, c _ {s}, c _ {i} \right\rangle \\ + \left| 2 _ {s}, 2 _ {i}, a _ {s}, a _ {i} \right\rangle + \left| 2 _ {s}, 2 _ {i}, b _ {s}, b _ {i} \right\rangle \\ + \left| 2 _ {s}, 2 _ {i}, c _ {s}, c _ {i} \right\rangle \\ + \left| 3 _ {s}, 3 _ {i}, a _ {s}, a _ {i} \right\rangle + \left| 3 _ {s}, 3 _ {i}, b _ {s}, b _ {i} \right\rangle \\ + \left| 3 _ {s}, 3 _ {i}, c _ {s}, c _ {i} \right\rangle \\ \end{array}
$$

where numbers indicate time bins and letters indicate frequency bins, with the indices s and i referring to the signal and idler photons,

respectively (the normalization is not shown for compactness). This hyper-entangled state is bi-separable, since any projection measurement performed in, for example, the time-bin basis, does not affect the frequency-bin entangled sub-state (and vice versa). In contrast, a cluster state is characterized by the fact that a projection measurement of one party affects the remaining portion of the state. An ideal compact three-level cluster state (which is locally equivalent to a linear cluster in a one-dimensional lattice, as well as a box cluster in a two-dimensional lattice, see Methods) can be obtained by judiciously modifying the phase terms in equation (1), which then reads (equation (2)):

$$
\begin{array}{l} \mid \Psi_ {\text {C l u s t e r}} \rangle = \mid 1 _ {s}, 1 _ {i}, a _ {s}, a _ {i} \rangle + \mid 1 _ {s}, 1 _ {i}, b _ {s}, b _ {i} \rangle \\ + \left| 1 _ {s}, 1 _ {i}, c _ {s}, c _ {i} \right\rangle \\ + \left| 2 _ {s}, 2 _ {i}, a _ {s}, a _ {i} \right\rangle + e ^ {i \frac {2 \pi}{3}} \left| 2 _ {s}, 2 _ {i}, b _ {s}, b _ {i} \right\rangle \\ + e ^ {- i \frac {2 \pi}{3}} \left| 2 _ {s}, 2 _ {i}, c _ {s}, c _ {i} \right\rangle \tag {2} \\ + \left| 3 _ {s}, 3 _ {i}, a _ {s}, a _ {i} \right\rangle + e ^ {- i \frac {2 \pi}{3}} \left| 3 _ {s}, 3 _ {i}, b _ {s}, b _ {i} \right\rangle \\ + e ^ {i \frac {2 \pi}{3}} \left| 3 _ {s}, 3 _ {i}, c _ {s}, c _ {i} \right\rangle \\ \end{array}
$$

To experimentally transform the hyper-entangled state (equation (1)) into this cluster state (equation (2)), access to the individual terms of the state is necessary, while maintaining coherence. For multi-particle states, this is technically very challenging, requiring two-party quantum gates, which are usually probabilistic[27]. Since we are employing two different types of discrete energy-time entanglement associated with different timescales (that is, time-bin and frequency-bin), it is possible to fully map the entangled state into the time domain to perform coherent state manipulations using

![](images/075b0319cba6ea9ac22588054c2ab8085cccdc4fe1e38517825245fe2dd5e6ca.jpg)

![](images/028b8192c0cb2c9cdbef9c345e214c86ea79c0d33e33a5392c94f395f16bfb9b.jpg)

![](images/0bdd94f504014dbb61e18d525d97a7457699fcce197208358b6a0300537f4217.jpg)  
Fig. 3 | Experimental demonstration of cluster state generation and related noise characteristics. a, Measured photon projections on the 81 diagonal elements of the state density matrix (Fig. 2, top right); each individual measurement had a duration of 1,200 s. b, Real (blue bars) and imaginary (red bars) parts of the measured expectation values for the individual terms of the cluster state witness operator. Note that the expectation value for each term can be complex due to the non-Hermitian properties (imaginary eigenvalues) of the generalized Pauli matrices; however, only the eight real parts contribute to the witness expectation value, measured to be  $-0.28 \pm 0.04$ , which is always real (see Methods). The error bars emerge as standard deviations from fits to the experimental data. c-e, Monte Carlo simulations for different noise contributions. The regions for which the optimal and measured witness operators confirm the existence of a cluster state for different sources of noise are indicated by blue- and orange-shaded areas, respectively. The witness bounds are shown for combinations of incoherent and amplitude noise (c), phase and incoherent noise (d), and amplitude and phase noise (e). The measurements (peaks in the respective diagrams) indicate that the largest contributor to state imperfection in our system is incoherent noise.

![](images/560f1bb82160c49d6c76e0f1df6e2a59dcda86a4b57852b88a3b204fdfa114d4.jpg)

![](images/98222c1fcb9dcb50e8e3ff8f5c8d7b037e7e9be0ac070638908f5f7bd6fa4321.jpg)

synchronized electro-optic modulation. The frequency-to-time mapping (see Fig. 2) was performed by a fibre Bragg grating array placed in a self-referenced and phase-stable loop configuration (see Methods). By choosing the appropriate phase pattern, the bi-separable hyper-entangled state was transformed into a three-level four-partite cluster state.

To confirm genuine multi-partite entanglement, we determined an optimal entanglement witness for the cluster state (see Methods). This witness detects the presence of a cluster state when its expectation value is negative (a minimum of  $-1$  is reached by a theoretically optimal cluster state; that is, in the absence of imperfection or noise contributions). This witness can be reduced to a measurable witness  $\mathcal{W}_{2S}^{(\mathcal{C}_{4,3})}$ , containing two orthogonal measurement settings represented by the generalized three-dimensional Pauli matrices  $X$  and  $Z$  (see Methods):

$$
\begin{array}{l} \langle W _ {2 S} ^ {(C _ {4, 3})} \rangle = \frac {5}{3} - \frac {1}{3} \mathrm {R e} \left(\left\langle \mathbb {I} _ {1} \mathbb {I} _ {2} Z _ {3} Z _ {4} ^ {\dagger} \right\rangle + \left\langle Z _ {1} ^ {\dagger} Z _ {2} \mathbb {I} _ {3} \mathbb {I} _ {4} \right\rangle \right. \\ + \left\langle \mathbb {I} _ {1} Z _ {2} X _ {3} X _ {4} \right\rangle + \left\langle X _ {1} X _ {2} Z _ {3} \mathbb {I} _ {4} \right\rangle \\ + \left\langle Z _ {1} \mathbb {I} _ {2} X _ {3} X _ {4} \right\rangle + \left\langle Z _ {1} ^ {\dagger} Z _ {2} ^ {\dagger} X _ {3} X _ {4} \right\rangle \\ + \left\langle X _ {1} X _ {2} \mathbb {I} _ {3} Z _ {4} \right\rangle + \left\langle X _ {1} X _ {2} Z _ {3} ^ {\dagger} Z _ {4} ^ {\dagger}\right) \\ \end{array}
$$

We measured a witness expectation value of  $\langle \mathcal{W}_{2S}^{(C_{4,3})}\rangle = -0.28\pm 0.04$  (see Fig.3a,b and Methods), confirming (within the range of 7 standard deviations) the presence of a cluster state exhibiting genuine three-level four-partite entanglement.

We then tested the impact of incoherent, phase and amplitude noise on the measured state with respect to the expectation value of the witness via Monte Carlo simulations (see Fig. 3c-e). We also calculated the threshold for which the states lose their cluster properties due to the impact of noise. We found that our  $d$ -level cluster states are highly robust towards incoherent noise (see Methods). The prepared cluster state can tolerate up to  $66.6\%$  of incoherent noise with respect to the optimal witness and  $37.5\%$  for the measured witness. In addition, they can also endure high amounts of amplitude and phase noise within the state itself; that is, as much as  $83\%$  (55% for the measurement witness) average amplitude fluctuations for the involved state components, and up to  $37\%$  (25%) error in their phase terms (see Fig. 3c-e). Most remarkably, our finding show that  $d$ -level cluster states are significantly more robust towards noise compared to two-level states. In comparison, a four-qubit cluster state can be mixed only with up to  $50\%$  of incoherent noise when employing the optimal witness and  $33\%$  when using the measurement witness to successfully detect the presence of the state. In comparison, a six-qubit cluster state (having slightly lower computational power compared to the four-qutrit state demonstrated here) can tolerate only  $50\%$  for the optimal and  $28.5\%$  for the measurement witness (see Methods).

To confirm the potential of  $d$ -level cluster states for quantum computation, we demonstrated that different and orthogonal entangled states can be generated by simply performing projection measurements on the parties of the cluster, which is the working principle of one-way quantum computers[5,7]. We here show this shaping of the cluster states and transform them into different orthogonal

![](images/247c645907f6cf2b4db98658a9e5f237c22a9ee86fccb7e1684ad1313062a0fc.jpg)

![](images/be656e9a04abd869f012067d8bb27356d7461eb610339c4267f6bce8062e772f.jpg)

![](images/8a789d8ec021db2ba23cb4d9223e83cae4bb1302672c976417e288e0606acb6c.jpg)

![](images/10fe26de53f120b8b2d5878784f58a12fc92ace3d9fc337d3a1a37deecf724ac.jpg)

![](images/f74d458daaa2e6d373ceea63c14589296a1562edffe3e0ad0aafb1aa4473fcca.jpg)  
Fig. 4 | High-dimensional one-way computation operations by measurement-based generation of orthogonal  $d$ -level two-party entangled quantum states. The cluster state was projected on specific time and frequency modes, resulting in different, orthogonal two-partite three-level entangled states in the frequency and time domains, respectively. Quantum interference measurements were performed to confirm the presence of these two-partite states, as well as their entanglement. a-c, The time-bin quantum interference, measured by selecting two temporal modes, results in different phase shifts (the relative position of the maximum with respect to the zero phase) after projecting the cluster states on the frequency modes  $\{|aa\rangle, |bb\rangle, |cc\rangle\}$ . d-f, Likewise, the frequency-bin quantum interference, measured by selecting three frequency modes, results in different phase shifts after projecting the cluster state on the temporal modes  $\{|11\rangle, |22\rangle, |33\rangle\}$ . The quantum interferences follow the expected functions for the ideal, orthogonal two-partite states (dashed line: theory, solid line: fit); furthermore, the visibilities violate the respective Bell inequalities (see Methods). The measured phase values, together with the visibility, confirm the generation of orthogonal entangled audit states through measurement-based operations, thus demonstrating high-dimensional one-way quantum computation processing.

![](images/5b36a686a45a179cce586aeb5b2cf6e0fc462d861447f4d534ef7305f9f782a4.jpg)

bi-partite states. For this, we carried out two-partite projections in either the frequency or time domain (see Fig. 4), and verified, via quantum interference measurements, that the resultant states are mutually orthogonal and entangled (see Methods). The orthogonality of these target states was confirmed by the relative phase shift in the respective quantum interference patterns (see Methods). Furthermore, all measured raw visibilities—listed in Supplementary Table 1—violated their respective two-partite Bell inequalities (see Methods). Therefore, these projection measurements performed on a cluster state represent high-dimensional one-way quantum computing operations. Universal quantum computation will require the application of  $d$ -level Hadamard gates to turn the state generated here into a linear or box cluster, necessary for algorithm implementation (see Methods). Such gates have already been achieved for time-bin qubits<sup>28</sup>, as well as frequency-bin qubits and qutrits<sup>29</sup>.

In conclusion, our work shows that integration is not, as it is often regarded, simply limited to miniaturizing devices and reducing cost (typically at the expense of lower performance), but can in fact enable novel and powerful capabilities. Furthermore, our approach has an important scaling potential and is advantageous compared to current methods based on two-level cluster states, since it can provide a better noise tolerance, as well as a significant improvement in terms of an effective quantum resource rate (EQRR).

In particular, multi-photon states that are generated by multiple spontaneous parametric processes are hampered by a decrease in state purity with increasing photon number $^{30}$ . Moreover, in general, quantum systems suffer significant reduction in their coherence time or detection rate when the number of entangled particles becomes larger, ultimately limiting the number of physical photons to well below the number of parties required for meaningful quantum computation tasks. It is therefore important to employ large cluster states with a low photon number. As an example, the largest two-level cluster states realized to date were comprised of  $\mathrm{six}^{13}$  and  $\mathrm{eight}^{11}$  qubits. These states had Hilbert space sizes  $(H_{N,d} = d^{N})$  of  $H_{6,2} = 64$  and  $H_{8,2} = 256$ , and were featured by moderate (yet impressive for current technology) six- and eight-photon detection rates (DR) of  $\mathrm{DR}_{6,2} = 12 \mathrm{mHz}$  and  $\mathrm{DR}_{8,2} = 0.89 \mathrm{mHz}$ , resulting in effective quantum resource rates  $(\mathrm{EQRR}_{\mathrm{H}} = H \times \mathrm{DR})$  of  $\mathrm{EQRR}_{64} = 0.768 \mathrm{Hz}$  and  $\mathrm{EQRR}_{256} = 0.228 \mathrm{Hz}$ , respectively. In the multi-photon cluster state approach, the detection rate diminishes more than the gain obtained through the increase in Hilbert space size, thus reducing the EQRR. In contrast, we achieved a Hilbert space size of  $H_{4,3} = 81$  (corresponding to 6.34 qubits), yet at a much higher detection rate of  $\mathrm{DR}_{4,3} = 1 \mathrm{Hz}$ , resulting in an  $\mathrm{EQRR}_{81} = 81 \mathrm{Hz}$ . This corresponds to a one (three) hundred-fold increase with respect to the six- (eight-) photon cluster state. In addition, it has recently been shown that

multi-photon states can also carry hyper-entanglement $^{31}$ . While this GHZ-type state $^{31}$  is not practically useful for quantum computation, its realization suggests that high-dimensional cluster states based on hyper-entangled multi-photon states can become a reality (see Methods). These would enable quantum computation based on many  $d$ -level parties, yet with a manageable number of photons, and therefore high EQRRs. In this system, the computational flow could be achieved in such a way that the hyper-entangled parties are measured simultaneously, and feedforward $^{32}$  is implemented between the different photons of the state (see Methods and Supplementary Fig. 2). Our work provides an important step towards achieving powerful and noise-tolerant quantum computation in a scalable and mass-producible platform.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, statements of data availability and associated accession codes are available at https://doi.org/10.1038/s41567-018-0347-x.

Received: 21 May 2018; Accepted: 13 October 2018

Published online: 3 December 2018

# References

1. Lloyd, S. Universal quantum simulators. Science 273, 1073-1078 (1996).  
2. Israel, Y., Rosen, S. & Silberberg, Y. Supersensitive polarization microscopy using NOON states of light. Phys. Rev. Lett. 112, 103604 (2014).  
3. Hodaei, H. et al. Enhanced sensitivity at higher-order exceptional points. Nature 548, 187-191 (2017).  
4. Briegel, H. J. & Raussendorf, R. Persistent entanglement in arrays of interacting particles. Phys. Rev. Lett. 86, 910-913 (2001).  
5. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
6. Walther, P. et al. Experimental one-way quantum computing. Nature 434, 169-176 (2005).  
7. Zhou, D., Zeng, B., Xu, Z. & Sun, C. Quantum computation based on  $d$ -level cluster state. Phys. Rev. A 68, 062303 (2003).  
8. Wang, D.-S., Stephen, D. T. & Russendorf, R. Qudit quantum computation on matrix product states with global symmetry. Phys. Rev. A 95, 032312 (2017).  
9. Reimer, C. et al. Generation of multiphoton entangled quantum states by means of integrated frequency combs. Science 351, 1176-1180 (2016).  
10. Kues, M. et al. On-chip generation of high-dimensional entangled quantum states and their coherent control. Nature 546, 622-626 (2017).  
11. Yao, X.-C. et al. Experimental demonstration of topological error correction. Nature 482, 489-494 (2012).  
12. Lanyon, B. P. et al. Measurement-based quantum computation with trapped ions. Phys. Rev. Lett. 111, 210501 (2013).  
13. Lu, C. Y. et al. Experimental entanglement of six photons in graph states. Nat. Phys. 3, 91-95 (2007).  
14. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
15. Pysher, M., Miwa, Y., Shahrokhshahi, R., Bloomer, R. & Pfister, O. Parallel generation of quadripartite cluster entanglement in the optical frequency comb. Phys. Rev. Lett. 107, 030505 (2011).  
16. Yokoyama, S. et al. Ultra-large-scale continuous-variable cluster states multiplexed in the time domain. Nat. Photon. 7, 982-986 (2013).  
17. Lloyd, S. & Braunstein, S. L. Quantum computation over continuous variables. Phys. Rev. Lett. 82, 1784-1787 (1999).  
18. Blatt, R. & Wineland, D. Entangled states of trapped atomic ions. Nature 453, 1008-1015 (2008).  
19. Kandala, A. et al. Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. Nature 549, 242-246 (2017).  
20. Dada, A. C., Leach, J., Buller, G. S., Padgett, M. J. & Andersson, E. Experimental high-dimensional two-photon entanglement and violations of generalized Bell inequalities. Nat. Phys. 7, 677-680 (2011).

21. Gräfe, M. et al. On-chip generation of high-order single-photon W-states. Nat. Photon. 8, 791-795 (2014).  
22. Malik, M. et al. Multi-photon entanglement in high dimensions. Nat. Photon. 10, 248-252 (2016).  
23. Barreiro, J., Langford, N., Peters, N. & Kwiat, P. Generation of hyperentangled photon pairs. Phys. Rev. Lett. 95, 260501 (2005).  
24. Chen, K. et al. Experimental realization of one-way quantum computing with two-photon four-qubit cluster states. Phys. Rev. Lett. 99, 120503 (2007).  
25. Vallone, G., Pomarico, E., Mataloni, P., Martini, F. De & Berardi, V. Realization and characterization of a two-photon four-qubit linear cluster state. Phys. Rev. Lett. 98, 180502 (2007).  
26. Gao, W.-B. et al. Experimental demonstration of a hyper-entangled ten-qubit Schrödinger cat state. Nat. Phys. 6, 331-335 (2010).  
27. O'Brien, J. L., Pryde, G. J., White, A. G., Ralph, T. C. & Branning, D. Demonstration of an all-optical quantum controlled-NOT gate. Nature 426, 264-267 (2003).  
28. Humphreys, P. C. et al. Linear optical quantum computing in a single spatial mode. Phys. Rev. Lett. 111, 150501 (2013).  
29. Lu, H.-H. et al. Electro-optic frequency beam splitters and tritters for high-fidelity photonic quantum information processing. Phys. Rev. Lett. 120, 030502 (2018).  
30. Wang, X. L. et al. Experimental ten-photon entanglement. Phys. Rev. Lett. 117, 210502 (2016).  
31. Wang, X.-L. et al. 18-qubit entanglement with six photons' three degrees of freedom. Phys. Rev. Lett. 120, 260502 (2018).  
32. Prevedel, R. et al. High-speed linear optics quantum computing using active feed-forward. Nature 445, 65-69 (2007).

# Acknowledgements

This work was supported by the Natural Sciences and Engineering Research Council of Canada (NSERC) through the Steacie, Strategic, Discovery and Acceleration Grants Schemes, by the MESI PSR-SIIRI Initiative in Quebec, by the Canada Research Chair Program and by the Australian Research Council Discovery Projects scheme (DP150104327). C.R., P.R. and S.L. acknowledge the support of NSERC Vanier Canada Graduate Scholarships. M.K. acknowledges funding from the European Union's Horizon 2020 Research and Innovation programme under the Marie Sklodowska-Curie grant agreement number 656607. S.T.C. acknowledges support from the CityU APRC programme number 9610356. B.E.L. acknowledges support from the Strategic Priority Research Program of the Chinese Academy of Sciences (grant number XDB24030300). W.J.M. acknowledges support from the John Templeton Foundation (JTF) number 60478. R.M. acknowledges additional support by the Government of the Russian Federation through the ITMO Fellowship and Professorship Program (grant 074-U 01) and from the 1000 Talents Sichuan Program. We thank R. Helsten for technical insights; A. Tavares and K. Nemoto for discussions; P. Kung from QPS Photonics for help and the use of processing equipment; and Quantum Opus and N. Bertone of OptoElectronics Components for their support and for providing us with state-of-the-art photon detection equipment.

# Author contributions

C.R. and M.K. contributed equally. M.K., C.R., P.R., and S.S. developed the idea. C.R., M.K. P.R., M.I., Y.Z., L.R.C., and B.F. performed the measurements and analyzed the data. S.S., C.R., M.K., L.C., and W.J.M. performed the theoretical analysis. S.T.C. and B.E.L. designed and fabricated the microring resonator. S.L. and R.K. designed and fabricated the fibre Bragg gratings. D.J.M. and A.C. contributed to discussions. R.M. and J.A. managed the project. All authors contributed to the writing of the manuscript.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41567-018-0347-x.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to M.K. or R.M.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2018

# Methods

Experimental set-up. The full experimental set-up including all components is shown in Supplementary Fig. 1. To generate phase-locked triple pulses, we used a carrier-envelope phase stabilized mode-locked laser (Menlo Systems Inc.) operating at  $250\mathrm{MHz}$  repetition rate (that is, 4 ns pulse separation) and locked the carrier-envelope phase frequency to  $250 / 6 = 41.667\mathrm{MHz}$ . We then employed an electro-optic intensity modulator, driven by an arbitrary waveform generator (Tektronix), to temporally gate triple pulses that were separated by 24 ns (that is, taking each 6th pulse from the initial pulse train), where the set of pulses was repeated at a rate of  $10\mathrm{MHz}$  (that is, every 100 ns). The triple pulses were then spectrally filtered, amplified and coupled into the microring resonator at the resonance wavelength of  $1,555.93\mathrm{nm}$ . The microring resonator was fabricated from a high-refractive-index glass[10], with a free spectral range of  $200\mathrm{GHz}$  and a  $Q$  factor of  $235,000^{33-35}$ . The input and output waveguides were featured by mode converters and were connected to polarization-maintaining fibres, resulting in coupling losses of  $<1.6\mathrm{dB}$  per facet. The average pump power coupled through the chip was  $2.4\mathrm{mW}$ , measured at the drop port. After the microring resonator, the excitation field was removed using a high-isolation (150 dB) notch filter, and the entangled photons were coupled into the controlled phase gate (see Fig. 2). This allowed us to generate a hyper-entangled state[23,36] simultaneously exploiting the time- $\mathrm{bin}^{37}$  and frequency- $\mathrm{bin}^{38}$  approaches. The phase-gate achieved frequency-to-time mapping via a custom-made fibre Bragg grating (FBG) array, consisting of six independent FBGs matched to the photon wavelengths (1,551.08, 1,552.70, 1,554.31, 1,557.55, 1,559.17 and 1,560.80 nm) and spatially separated in the fibre to achieve a 3.96 ns temporal delay between adjacent frequency modes (that is, to introduce the frequency-time mapping). The FBGs were written into a photosensitive and deuterium-loaded polarization-maintaining fibre (Nufern) using a 213-nm-wavelength laser (fifth harmonic of a Nd:YBO laser, Xiton Photonics Inc.) by means of a continuous writing scheme, realized in a tunable Talbot interferometer with a moving fibre[39]. The FBGs were apodized using a squared cosine function, implemented by means of moving the Talbot phase mask with a piezo actuator[39]. The FBGs were then heated to  $80^{\circ}\mathrm{C}$  for  $48\mathrm{h}$  to remove the deuterium, thus decreasing losses. They were subsequently spliced to standard polarization-maintaining Panda fibres using a tapered splice to decrease mode-matching losses. To implement the optical phase modulation within the gate, we used an electro-optic phase modulator (EOSpace), which was driven by an arbitrary waveform generator (Tektronix), synchronized to the  $10\mathrm{MHz}$  reference clock of the modelocked laser. After the phase-gate, the photons were sent to a computer-controlled amplitude and phase filter with two output ports (Finisar Waveshaper). This filter was used to route the photons to different characterization set-ups. One output was connected to a stabilized fibre interferometer with 24 ns unbalance to perform temporal projection measurements[9,40], and the other output was connected to an electro-optic phase modulator, which mixes different frequency components to perform frequency projection measurements[10,41,42]. Finally, the photons were separated using spectral programmable filters and sent to superconducting single-photon detectors (Quantum Opus).

Hyper-entanglement within energy-time entangled states. Hyper-entangled states are quantum states that are entangled in two or more independent degrees of freedom $^{23,26,36,43}$ , such as polarization, optical paths or orbital angular momentum. Since these degrees of freedom can be controlled autonomously, such systems can be best described as multi-partite states, where each degree of freedom represents an independent party $^{23,36}$ . Such a system could also be mathematically mapped into a high-dimensional state representation; however, this requires a rather complex, non-intuitive description of the experimentally accessible operations. In particular, the underlying physical quantum system and the accessible operations determine which state representation should be used. For hyper-entangled systems, a multi-partite representation treats individual degrees of freedom as separate parties, where a photon is seen as a carrier of multiple parties. Past realizations of hyper-entanglement made use of independent degrees of freedom, which require very different control mechanisms for each degree of freedom $^{31}$ . In this work, we generated hyper-entanglement between two energy-time realizations (that is, a single degree of freedom). The temporal and frequency observables in energy-time entangled states are non-commuting and form Einstein-Podolsky-Rosen $^{44}$  (EPR)-type quantum correlations $^{45}$ . In the chosen discrete energy-time entanglement realization, the time-frequency product is much larger than the EPR limit, thus allowing independent control described by commuting operators and ultimately hyper-entanglement. In particular, the time- and frequency-bin mode separation were chosen to be 24 ns and 200 GHz, respectively, resulting in a time-frequency product of  $4,800 \gg 1$ , which is three orders of magnitude above the EPR limit. Remarkably, even though time- and frequency-bin entanglement are independent, they both belong to the same degree of freedom, which enabled the implementation of the controlled phase gate, where the complete state was mapped into the time domain for coherent control.

State structure and one-way quantum computation with multi-partite hyperentangled cluster states. The structure or topology of cluster states is important for useful applications. The experimentally realized cluster state was measured in its compact form, which is locally equivalent to a four-partite linear cluster in a

one-dimensional lattice (if Hadamard gates are applied to qudits 1 and 4), as well as a four-partite box cluster state in a two-dimensional lattice (if Hadamard gates are applied to all four qudits and qudits 2 and 3 are swapped). Both the linear and box cluster can be used for universal quantum computation<sup>6</sup>.

To perform meaningful algorithms, the number of parties has to be increased. This is still a significant challenge for all known quantum platforms. High-dimensional hyper-entangled multi-photon cluster states can provide a path to achieve such scalability. In particular, with current and foreseeable technology, it is not realistic to achieve, for example, a 100-qubit cluster state comprised of 100 photons, since the combination of multi-photon states is still probabilistic, which would lead to generation rates that are too low for functional processing speeds. It is therefore of paramount importance to reduce the number of physical photons, while maintaining the Hilbert space size. With the method we propose, this becomes possible through the realization of parties via hyper-entanglement and high-dimensional superposition. An important advantage of using hyper-entangled quuds in terms of scalability is that operations can be performed in a deterministic way, while multi-photon gates are commonly probabilistic. A judicious compromise between multi-photon and hyper-entangled parties is thus advantageous in terms of performing efficient operations and scalability. For efficient quantum computation, a hyper-entangled multi-photon cluster state with high-dimensional superposition can be envisioned. For example, a cluster state formed by 6 photons and hyper-entangled in 4 degrees of freedom, each in a superposition of 16 levels, would result in an equivalent 96-qubit system.

The suggested computational flow would involve a two-dimensional lattice of parties in which the hyper-entangled degrees of freedom are measured simultaneously (as they belong to the same photon), and feedforward is performed between the involved photons (see Supplementary Fig. 2). To potentially realize such a state, the  $d$ -level multi-partite cluster demonstrated here has to be extended to include more hyper-entangled parties, as well as more photons. Additional hyper-entangled parties could be obtained by making use of mutually independent energy-time entangled timescales, which could be controlled through concatenated interferometers, fast switches and spectral filters. The advantage of using multiple energy-time hyper-entangled states is that the controlled quantum gates can be used also for additional parties. Increasing the number of photons could be achieved either directly in the state generation $^{6,11,13}$ , or through state fusion gates $^{46}$ , which have already been proposed for time-bin entangled states $^{47}$ .

Entanglement witness for cluster states of qutrits. Multi-partite entangled quantum systems provide powerful resources for the implementation and advancement of many applications $^{48}$ . The presence of a genuine pure multi-partite quantum state  $|\psi \rangle$ , and those states close to them (for example, states degraded by noise), can be identified by measuring the expectation value of an entanglement witness operator $^{49}$ :

$$
\widehat {\mathcal {W}} = \delta \times \mathbb {I} - | \psi \rangle \langle \psi |
$$

with  $\mathbb{I}$  being the identity. The factor  $\delta$  has to be chosen in such a way to exclude all bi-separable quantum states $^{49}$ . This witness detects the presence of the target state if the expectation value of the witness is negative. For convention, we normalize this witness such that the optimal state results in an expectation value of minus one:

$$
\mathcal {W} = \frac {1}{1 - \delta} (\delta \times \mathbb {I} - | \psi \rangle \langle \psi |)
$$

The factor  $\delta$  is given by the square of the largest Schmidt coefficient of all singlet states between any combination of qutrits $^{49,50}$ . Determining this for cluster states is straightforward, since a cluster state can be projected under local operations on maximally entangled singlet states between any combination of qutrits. This immediately leads to the fact that the maximal Schmidt coefficient of a three-level cluster state when performing Schmidt-mode decomposition with respect to an arbitrary bipartite split does not exceed the maximal Schmidt coefficient of the singlet $^{51}$ , which is given by  $1 / \sqrt{3}$  for three-level cluster states. This means that  $\delta = \frac{1}{3}$  for a four-qutrit cluster state. The optimal witness operator for a four-partite, three-level cluster state  $|C_{4,3}\rangle$  is therefore given by:

$$
\mathcal {W} _ {\text {o p t}} ^ {(C _ {4, 3})} = \frac {1}{2} \mathbb {I} - \frac {3}{2} | C _ {4, 3} \rangle \langle C _ {4, 3} |
$$

Measuring the optimal witness would require full state tomography, which is experimentally very demanding. For this reason, the optimal witness is usually reduced to a witness that includes only two orthogonal measurement settings $^{50}$ , which can be achieved for cluster states using the stabilizer formalism $^{50}$ . Stabilizers are operators that are expressed as products of (generalized) Pauli matrices and are thus locally measurable by means of single-qudit projection measurements. Following the stabilizer formalism for  $d$ -level cluster states, developed in ref. $^{7}$ , we determined the stabilizers of the generated three-level, four-partite cluster state. In general, a cluster state  $|C_{N,d}\rangle$  can be uniquely defined by a set of main eigenvalue equations, where  $N$  is the number of parties and  $d$  is the number of levels. These equations are:

$$
\begin{array}{c c c} X _ {a} & \otimes & Z _ {b}   | \mathcal {C} _ {N, d} \rangle = | \mathcal {C} _ {N, d} \rangle \\ & b \in \mathcal {N} (a) \end{array}
$$

where  $a$  denotes the qudit and

$$
\mathcal {N} (a) = \left\{ \begin{array}{l l} \{2 \}, & a = 1 \\ \{N - 1 \}, & a = N \\ \{a - 1, a + 1 \}, & a \notin \{1, N \} \end{array} \right.
$$

denotes the neighbours of the qudit  $a$ . In the case of four qutrits, there is a set of four main eigenvalue equations that uniquely describe the cluster state  $|C_{4,3}\rangle$  generated here; that is,

$$
S _ {i} ^ {(C _ {4, 3})} | C _ {4, 3} \rangle = | C _ {4, 3} \rangle
$$

with

$$
S _ {1} ^ {(C _ {4, 3})} = Z _ {1} ^ {\dagger} Z _ {2} \mathbb {I} _ {3} \mathbb {I} _ {4},
$$

$$
S _ {2} ^ {(C _ {4}, 3)} = X _ {1} X _ {2} Z _ {3} \mathbb {I} _ {4},
$$

$$
S _ {3} ^ {(C _ {4}, 3)} = \mathbb {I} _ {1} Z _ {2} X _ {3} X _ {4}.
$$

$$
S _ {4} ^ {(C _ {4}, 3)} = \mathbb {I} _ {1} \mathbb {I} _ {2} Z _ {2} Z _ {4} ^ {\dagger}
$$

where  $X$  and  $Z$  are the generalized Pauli matrices,  $\mathbb{I}$  is the identity and  $\dagger$  denotes the transpose conjugate. In particular,

$$
Z = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & q & 0 \\ 0 & 0 & q ^ {2} \end{array} \right), X = \left( \begin{array}{c c c} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right), \mathbb {I} = \left( \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right)
$$

with  $q = \mathrm{e}^{i2\pi /3}$ . The matrices composing the stabilizers belong to the orthonormal Pauli group  $P = \{\mathbb{I},X,X^{\dagger},Z,Z^{\dagger},Y,Y^{\dagger},V,V^{\dagger}\}$ , with  $Y = XZ, V = XZ^{\dagger}$ .

Using the stabilizers, the density matrix of the cluster state can be written as

$$
\left| C _ {4, 3} \right\rangle \left\langle C _ {4, 3} \right| = \prod_ {k = 1} ^ {4} \frac {S _ {k} ^ {(C _ {4 , 3})} + S _ {k} ^ {\dagger (C _ {4 , 3})} + \mathbb {I}}{3}
$$

We can separate the stabilizers into two orthogonal sets that include only  $X$  and  $Z^{50}$ , which leads to a witness operator that contains only two measurement settings:

$$
\begin{array}{l} \mathcal {W} _ {2 S} ^ {(C _ {4, 3})} = 2 \mathbb {I} - \frac {3}{2} \prod_ {\text {e v e n}} ^ {4} \frac {S _ {k} ^ {(C _ {4 , 3})} + S _ {k} ^ {\dagger (C _ {4 , 3})} + \mathbb {I}}{3} \\ - \frac {3}{2} \prod_ {\mathrm {o d d}} ^ {4} \frac {S _ {k} ^ {(C _ {4 , 3})} + S _ {k} ^ {\dagger (C _ {4 , 3})} + \mathbb {I}}{3} \\ \end{array}
$$

Considering the stabilizers listed above, this witness has an expectation value of:

$$
\begin{array}{l} \langle \mathcal {W} _ {2 S} ^ {\left(\mathcal {C} _ {4, 3}\right)} \rangle = \frac {5}{3} - \frac {1}{3} \operatorname {R e} \left(\left\langle \mathbb {I} _ {1} \mathbb {I} _ {2} Z _ {3} Z _ {4} ^ {\dagger} \right\rangle + \left\langle Z _ {1} ^ {\dagger} Z _ {2} \mathbb {I} _ {3} \mathbb {I} _ {4} \right\rangle + \left\langle \mathbb {I} _ {1} Z _ {2} X _ {3} X _ {4} \right\rangle \right. \\ + \left\langle X _ {1} X _ {2} Z _ {3} \mathbb {I} _ {4} \right\rangle + \left\langle Z _ {1} \mathbb {I} _ {2} X _ {3} X _ {4} \right\rangle + \left\langle Z _ {1} ^ {\dagger} Z _ {2} ^ {\dagger} X _ {3} X _ {4} \right\rangle \\ + \left\langle X _ {1} X _ {2} \mathbb {I} _ {3} Z _ {4} \right\rangle + \left\langle X _ {1} X _ {2} Z _ {3} ^ {\dagger} Z _ {4} ^ {\dagger}) \right\rangle \\ \end{array}
$$

where  $\operatorname{Re}()$  refers to the real part of the operators, also considering that the real part of an imaginary number  $C$  is given by  $\mathrm{Re}(C) = \frac{C + C^{\dagger}}{2}$ . The witness operator therefore always has a real expectation value, as required for a measurable value with physical meaning. Note that the generalized Pauli matrices (that is, for  $d$ -level systems) are non-Hermitian and have complex eigenvalues, and therefore the expectation values of the individual stabilizers can have imaginary components.

In a similar way as described above, witnesses were previously derived for cluster states of qubits<sup>50</sup>. The optimal witness for all cluster states of qubits is given by

$$
\mathcal {W} _ {\mathrm {o p t}} ^ {(C _ {N, 2})} = \mathbb {I} - 2 | C _ {N, 2} \rangle \langle C _ {N, 2} |
$$

which results in a noise tolerance for a cluster state of qubits mixed with linear incoherent noise of  $50\%$ . The reduced witness for cluster states of qubits was derived in ref. [50], and reads:

$$
\mathcal {W} _ {2 S} ^ {(C _ {N, 2})} = 3 \mathbb {I} - 2 \prod_ {\text {e v e n}} ^ {N} \frac {S _ {k} ^ {(C _ {N , 2})} + \mathbb {I}}{2} - 2 \prod_ {\text {o d d}} ^ {N} \frac {S _ {k} ^ {(C _ {N , 2})} + \mathbb {I}}{2}
$$

This witness for qubits has a tolerance with respect to incoherent linear noise of  $33.33\%$  for four qubits, and  $28.57\%$  for six qubits<sup>50</sup>.

Measurement of the witness expectation value. To measure the expectation value of the entanglement witness, the individual expectation values for eight stabilizers have to be measured separately. Each stabilizer expectation value can be extracted by means of 81 separate measurements, which can be performed by projecting the state on the respective combinations of stabilizer eigenvectors. In particular, the witness terms  $Z_{1}^{\dagger}Z_{2}\mathbb{I}_{3}\mathbb{I}_{4}$  and  $\mathbb{I}_1\mathbb{I}_2Z_3Z_4^\dagger$  have eigenvectors  $|1\rangle ,|2\rangle ,|3\rangle ,|a\rangle ,|b\rangle$  and  $|c\rangle$ ;

while  $\mathbb{I}_1Z_2X_3X_4, Z_1\mathbb{I}_2X_3X_4$  and  $Z_{1}^{\dagger}Z_{2}^{\dagger}X_{3}X_{4}$  have eigenvectors  $|1\rangle, |2\rangle, |3\rangle, |f1\rangle, |f2\rangle$  and  $|f3\rangle$ , with  $|f1\rangle = |a\rangle + |b\rangle + |c\rangle, |f2\rangle = |a\rangle + \mathrm{e}^{i2\pi / 3} |b\rangle + \mathrm{e}^{-i2\pi / 3} |c\rangle$  and  $|f3\rangle = |a\rangle + \mathrm{e}^{-i2\pi / 3} |b\rangle + \mathrm{e}^{i2\pi / 3} |c\rangle$ ; finally,  $X_1X_2Z_3I_4, X_1X_2I_3Z_4$  and

$X_{1}X_{2}Z_{3}^{\dagger}Z_{4}^{\dagger}$  have eigenvectors  $|t1\rangle$ $|t2\rangle$ $|t3\rangle$ $|a\rangle$ $|b\rangle$  and  $|c\rangle$

with  $|t1\rangle = |1\rangle + |2\rangle + |3\rangle$ ,  $|t2\rangle = |1\rangle + \mathrm{e}^{i2\pi / 3} |2\rangle + \mathrm{e}^{-i2\pi / 3} |3\rangle$  and

$|t3\rangle = |1\rangle + \mathrm{e}^{-i2\pi / 3} |2\rangle + \mathrm{e}^{i2\pi / 3} |3\rangle$ . To extract all projection values,  $3 \times 81 = 243$  parameters, which can take real values between 0 and 1, have to be experimentally determined. From these 243 measurement outcomes, the expectation values of the individual witness terms (stabilizers) can be calculated, which are complex numbers with an absolute value smaller than one. The witness is then calculated from the real parts of the eight stabilizer terms. Projections on time and frequency modes  $(|1\rangle, |a\rangle$  and so on), as well as frequency-bin superpositions  $(|f1\rangle$ , and so on), can be immediately obtained with the experimental set-up. Projections on time-bin superpositions were achieved as follows: we assessed the state phases through simultaneous projection measurements on the superposition of two time bins each, implemented by unbalanced two-arm interferometers. The time-bin projections  $|t1\rangle$ ,  $|t2\rangle$  and  $|t3\rangle$  were then reconstructed considering the measured interference patterns.

Extraction of the wavefunction's amplitude and phase terms and orthogonality of the bi-partite states after projection. The quantum interference measurements shown in Fig. 4 can be used to extract the amplitude and phase terms of the four-partite cluster state, which can then be used to confirm that the bi-partite states that remain after projection measurements are orthogonal. The most generic wavefunction to express the four-qutrit hyper-entangled states is

$$
\begin{array}{l} \left| \Psi \right\rangle = m _ {1, a} \left| 1, 1, a, a \right\rangle + m _ {1, b} \left| 1, 1, b, b \right\rangle + m _ {1, c} \left| 1, 1, c, c \right\rangle \\ + m _ {2, a} | 2, 2, a, a \rangle + m _ {2, b} | 2, 2, b, b \rangle + m _ {2, c} | 2, 2, c, c \rangle \\ + m _ {3, a} | 3, 3, a, a \rangle + m _ {3, b} | 3, 3, b, b \rangle + m _ {3, c} | 3, 3, c, c \rangle \\ \end{array}
$$

where  $m_{t,f} = |m_{t,f}|\mathrm{e}^{i\phi_{t,f}}$  are complex numbers with amplitude  $|m_{t,f}|$  and phase  $\phi_{t,f}$ . Here,  $t = 1,2,3$  and  $f = a,b,c$ . We determined the amplitudes by performing 81 coincidence measurements between all combinations of temporal and frequency modes, and confirmed that, as expected, the wavefunction has only the above-stated nine non-zero elements (see Fig. 3a). To extract the phases  $\phi_{t,f}$  we used the nine quantum interference measurements shown in Fig. 4. In particular, we projected onto time- or frequency-bin bases by means of temporal gating (in the detection) or optical filtering. The remaining two-partite states were then measured in superpositions. For time-bin measurements, we employed a two-arm interferometer, which simultaneously projects on time-bin superpositions; that is  $|1\rangle +\mathrm{e}^{-i\theta}|2\rangle$ , as well as  $|2\rangle +\mathrm{e}^{-i\theta}|3\rangle$  for each photon. The relative phase offset between the quantum interference measurements can be used to extract the relative phase between the coefficients of the wavefunction. For the frequency-bin projections, we first added spectral phases, and then mixed the three frequency components using electro-optic modulation. The spectral phase was adjusted to perform projection measurements of the form  $|a\rangle +\mathrm{e}^{-i\theta}|b\rangle +\mathrm{e}^{i2\theta}|c\rangle$ . We then fitted the predicted functions to the quantum interference patterns to extract the individual phases of the wavefunction (listed in Supplementary Table 1), including the estimated error for these values. Note that all measured visibilities exceed the threshold (also shown in Supplementary Table 1) required to violate two-partite Bell inequalities[53].

The extracted phase parameters can then be used to confirm that the individual two-partite states are orthogonal. In particular, the quantum interference measurements witness the generation of the following bi-partite states:

$$
\begin{array}{l} \left| \psi_ {\mathrm {a}, \mathrm {a}} \right\rangle = 0. 5 8 1 1 1, 1 \rangle + 0. 5 7 7 \mathrm {e} ^ {\mathrm {i} 0. 0 6 \pi} | 2, 2 \rangle + 0. 5 7 4 \mathrm {e} ^ {- \mathrm {i} - 0. 0 6 \pi} | 3, 3 \rangle \\ \left| \psi_ {\mathrm {b}, \mathrm {b}} \right\rangle = 0. 5 8 8 | 1, 1 \rangle + 0. 5 6 3 \mathrm {e} ^ {\mathrm {i} 0. 6 5 \pi} | 2, 2 \rangle + 0. 5 8 1 \mathrm {e} ^ {- \mathrm {i} 0. 7 2 \pi} | 3, 3 \rangle \\ \left| \psi_ {c, c} ^ {\prime} \right\rangle = 0. 5 9 6 | 1, 1 \rangle + 0. 5 7 4 e ^ {- i 0. 6 7 \pi} | 2, 2 \rangle + 0. 5 6 2 e ^ {i 0. 6 9 \pi} | 3, 3 \rangle \\ \left| \psi_ {1, 1} \right\rangle = 0. 5 7 4 | a, a \rangle + 0. 5 7 7 e ^ {i 0. 0 8 7 \pi} | b, b \rangle + 0. 5 8 1 e ^ {i 0. 0 0 1 \pi} | c, c \rangle \\ \left| \psi_ {2, 2} ^ {\prime} \right\rangle = 0. 5 8 6 \left| a, a \right\rangle + 0. 5 6 9 e ^ {i 0. 5 9 4 \pi} \left| b, b \right\rangle + 0. 5 7 6 e ^ {- i 0. 6 6 7 \pi} \left| c, c \right\rangle \\ \left| \psi_ {3, 3} \right\rangle = 0. 5 8 2 \left| a, a \right\rangle + 0. 5 8 6 e ^ {- i 0. 6 3 8 \pi} \left| b, b \right\rangle + 0. 5 6 4 e ^ {i 0. 6 2 8 \pi} \left| c, c \right\rangle \\ \end{array}
$$

Note that these measurements do not present full quantum state tomography, but are based on the realistic assumption that only the considered elements of the quantum state contribute to the wavefunction, and that the final actual state is an incoherent mixture of a pure state with linear noise. These assumptions are justified since we have an accurate experimental control over the generation

process as well as the projection measurements, and the measured interference agrees well with the fitted curves (see Fig. 4). From the estimated wavefunctions, it is possible to confirm that the generated states are orthogonal within the measurement uncertainties:

$$
| \langle \psi_ {\mathrm {a}, \mathrm {a}} | \psi_ {\mathrm {b}, \mathrm {b}} \rangle | ^ {2} = 0. 0 0 9 \pm 0. 0 2 \approx 0
$$

$$
\left| \langle \psi_ {\mathrm {a}, \mathrm {a}} | \psi_ {\mathrm {c}, \mathrm {c}} \rangle \right| ^ {2} = 0. 0 1 1 \pm 0. 0 2 \approx 0
$$

$$
| \langle \psi_ {\mathrm {b}, \mathrm {b}} | \psi_ {\mathrm {c}, \mathrm {c}} \rangle | ^ {2} = 0. 0 0 9 \pm 0. 0 2 \approx 0
$$

$$
\left| \right.\left\langle \right. \psi_ {1, 1} \left. \right| \psi_ {2, 2} \left. \right\rangle\left. \right| ^ {2} = 0. 0 2 7 \pm 0. 0 2 \approx 0
$$

$$
| \langle \psi_ {1, 1} | \psi_ {3, 3} \rangle | ^ {2} = 0. 0 0 2 \pm 0. 0 2 \approx 0
$$

$$
\left| \langle \Psi_ {2, 2} | \Psi_ {3, 3} \rangle \right| ^ {2} = 0. 0 1 2 \pm 0. 0 2 \approx 0
$$

Witness distribution and noise characterization via Monte Carlo simulations. We performed Monte Carlo simulations to infer the distribution of the witness expectation value. For all noise calculations, we used a linear noise model[50,53], where the pure quantum state is incoherently mixed with linear, uncorrelated classical noise:

$$
\rho_ {\text {n o i s e}} = \varepsilon \frac {\mathbb {I}}{d ^ {N}} + (1 - \varepsilon) | \psi \rangle \langle \psi |
$$

Here,  $\rho_{\mathrm{noise}}$  is the density matrix of the state after the incoherent mixture with noise,  $\varepsilon$  measures the quantity of mixed noise and  $|\psi\rangle$  is the wavefunction of the pure quantum state. The linear noise model is very useful for this analysis, as it allows one to separate different noise sources. The incoherent noise term is commonly used to describe the impact of state impurities such as losses and detection noise. Other sources such as amplitude and phase noise do not affect the purity of the state, and can be incorporated into the wavefunction of the pure state by adjusting the amplitude and phase terms within the wavefunction. Starting from the measured input values and their determined experimental errors (Supplementary Table 1), we assumed a Gaussian error distribution for each individual input parameter and calculated the witness expectation value one million times. These calculations were then summarized in normalized histograms (see Fig. 3). To determine the witness bound for different sources of input noise (that is, incoherent, amplitude and phase noise), we calculated the associated operator for input parameters with different noise sources and average strengths. In each calculation, only two noise sources were considered at a time, while the remaining noise source was kept at zero. For diagrams involving incoherent noise, a fixed value for this term was first set and ten million random input values for either the phases or amplitudes were generated (then the incoherent noise value was changed for different rounds of simulations). For the diagrams where both amplitude and phase noise were open parameters, we generated one billion random input settings. For each simulation input, we calculated the witness expectation value. The outcomes were then sorted according to positive and negative witness values as well as their average noise. We defined the amplitude noise as the average over the absolute deviations from the ideal value, normalized by the latter:  $\sigma_{\mathrm{ampl.}} = 3\times \frac{1}{9}\sum |a_i - 1 / 3|$ , where  $a_i$  are the nine different amplitude values in the wavefunction and  $1/3$  is the ideal value. We define the phase noise as the average over the absolute phase deviation from the ideal value, normalized by the optimal phase terms:  $\sigma_{\mathrm{ampl.}} = \frac{3}{2\pi}\times \frac{1}{9}\sum |\theta_i - \varphi_{\mathrm{ideal}}|$ , where  $\varphi_{\mathrm{ideal}} = \left[0,\frac{2\pi}{3},\frac{-2\pi}{3}\right]$  are the ideal phase settings, and  $\theta_i$  are the nine different determined phase values in

the wavefunction. The stated bound for the witness was determined as the points where over  $95\%$  of all calculated witness values were negative.

# Data availability

The data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.

# References

33. Moss, D. J., Morandotti, R., Gaeta, A. L. & Lipson, M. New CMOS-compatible platforms based on silicon nitride and Hydex for nonlinear optics. Nat. Photon. 7, 597-607 (2013).  
34. Pasquazi, A. et al. Micro-combs: A novel generation of optical sources. Phys. Rep. 729, 1-81 (2017).  
35. Caspani, L. et al. Integrated sources of photon quantum states based on nonlinear optics. Light Sci. Appl. 6, e17100 (2017).  
36. Kwiat, P. G. Hyper-entangled states. J. Mod. Opt. 44, 2173-2184 (1997).  
37. Brendel, J., Gisin, N., Tittel, W. & Zbinden, H. Pulsed energy-time entangled twin-photon source for quantum communication. Phys. Rev. Lett. 82, 2594-2597 (1999).  
38. Olislager, L. et al. Frequency-bin entangled photons. Phys. Rev. A 82, 013804 (2010).  
39. Loranger, S., Karpov, V., Schinn, G. W. & Kashyap, R. Single-frequency low-threshold linearly polarized DFB Raman fiber lasers. Opt. Lett. 42, 3864-3867 (2017).  
40. Xiong, C. et al. Compact and reconfigurable silicon nitride time-bin entanglement circuit. Optica 2, 724-727 (2015).  
41. Lukens, J. M. & Lougovski, P. Frequency-encoded photonic qubits for scalable quantum information processing. Optica 4, 8-16 (2017).  
42. Imany, P. et al. 50-GHz-spaced comb of high-dimensional frequency-bin entangled photons from an on-chip silicon nitride microresonator. Opt. Lett. 26, 1825-1840 (2018).  
43. Li, X.-H. & Ghose, S. Complete hyperentangled Bell state analysis for polarization and time-bin hyperentanglement. Opt. Express 24, 18388-18398 (2016).  
44. Einstein, A., Podolsky, B. & Rosen, N. Can quantum-mechanical description of physical reality be considered complete? Phys. Rev. 47, 777-780 (1935).  
45. Franson, J. D. Bell inequality for position and time. Phys. Rev. Lett. 62, 2205-2208 (1989).  
46. Browne, D. E. & Rudolph, T. Resource-efficient linear optical quantum computation. Phys. Rev. Lett. 95, 010501 (2005).  
47. Soudagar, Y. et al. Cluster-state quantum computing in optical fibers. J. Opt. Soc. Am. B 24, 226-230 (2007).  
48. Hein, M., Eisert, J. & Briegel, H. J. Multiparty entanglement in graph states. Phys. Rev. A 69, 062311 (2004).  
49. Bourennane, M. et al. Experimental detection of multipartite entanglement using witness operators. Phys. Rev. Lett. 92, 087902 (2004).  
50. Toth, G. & Guehne, O. Entanglement detection in the stabilizer formalism. Phys. Rev. A 72, 022340 (2005).  
51. Nielsen, M. A. Conditions for a class of entanglement transformations. Phys. Rev. Lett. 83, 436-439 (1999).  
52. Lawrence, J. Mutually unbiased bases and trinary operator sets for N qutrits. Phys. Rev. A 70, 012302 (2004).  
53. Collins, D., Gisin, N., Linden, N., Massar, S. & Popescu, S. Bell inequalities for arbitrarily high-dimensional systems. Phys. Rev. Lett. 88, 040404 (2002).