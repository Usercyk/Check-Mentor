# Integrated photonic quantum technologies

Jianwei Wang $^{1}$ , Fabio Sciarrino $^{2}$ , Anthony Laing $^{3}$  and Mark G. Thompson $^{3*}$

Quantum technologies comprise an emerging class of devices capable of controlling superposition and entanglement of quantum states of light or matter, to realize fundamental performance advantages over ordinary classical machines. The technology of integrated quantum photonics has enabled the generation, processing and detection of quantum states of light at a steadily increasing scale and level of complexity, progressing from few-component circuitry occupying centimetre-scale footprints and operating on two photons, to programmable devices approaching 1,000 components occupying millimetre-scale footprints with integrated generation of multiphoton states. This Review summarizes the advances in integrated photonic quantum technologies and its demonstrated applications, including quantum communications, simulations of quantum chemical and physical systems, sampling algorithms, and linear-optic quantum information processing.

Pioneering investigations of quantum science, including tests of entanglement $^{1}$ , generation of squeezed light $^{2}$ , demonstrations of quantum teleportation $^{3}$  and loophole-free tests of Bell nonlocality $^{4}$ , were possible because photons are excellent, low-noise carriers of quantum information. Weakly coupled to their environment, photons do not suffer the decoherence issues of matter-based systems, and thus do not require operation at millikelvin temperatures or in high vacuum. The translation of quantum information science to real-world technologies promises extreme advantages for certain tasks in communication $^{5}$ , computation $^{6}$  and simulation $^{7}$ . However, implementing large instances of quantum algorithms or the deployment of a global quantum communication network will require new levels of sophistication in the manufacture of quantum technologies with a large number of components. Exploiting single photons of light as quantum information carriers, together with wafer-scale fabrication processes, integrated quantum photonics (IQP) is a compelling platform for the future of quantum technologies.

While the photon-photon interactions required to realize quantum logic can be mediated through light-matter interaction in systems such as quantum dots (QDs) and colour centres, routes to scaling such systems remain challenging. In 2001, a theoretical breakthrough presented a scheme for universal quantum computation using photons in linear optics, in which photons interact non-deterministically via quantum interference and measurement-induced nonlinearities $^{9,10}$  - requiring no light-matter interactions. In the same year, a measurement-based quantum computation (MBQC) scheme was proposed, enabling a substantially more resource-efficient quantum computing model that is particularly well suited to  $\mathrm{IQP}^{11,12}$ . While realizing a universal fault-tolerant quantum computer remains challenging in any system at present, IQP provides a potentially low-resource route towards a specific but powerful quantum machine that could outperform a classical computer in a specific task, referred to as Boson sampling $^{13}$ . Photons provide the only viable technology to connect distributed quantum systems, or for quantum communication systems $^{5}$ .

In contrast to the well-established platforms of ion-trapping and superconducting systems (their first logic operation was demonstrated in the 1990s), IQP is relatively new, with the first integrated photonic quantum logic gate demonstrated in 2008<sup>14</sup>. Yet, despite its

relative immaturity, IQP can leverage commercially available tools from the complementary metal-oxide-semiconductor (CMOS) industry. Using optical waveguides to guide and route photons, IQP provides phase-stable quantum circuitry with core functionalities, including entangled state generation, quantum state manipulation and single-photon detection. While quantum photonic experiments in bulk optics continue to deliver significant results $^{15}$ , large-scale quantum information processing with hundreds or thousands of photons will almost certainly require the technological functionalities and scaling that only integrated photonics can provide.

Here we review the rapid progress that has been made, and current status, in IQP technology and applications. We first review a range of integrated photonics platforms and recent progress in integrated single-photon sources (SPSs), linear-optic quantum circuits and integrated single-photon detectors (SPDs). We then focus on applications of IQP, including chip-scale quantum communications, quantum computing and information processing, Boson sampling, and quantum simulation of chemical and physical systems. Finally, we discuss the challenges and opportunities of realizing large-scale, monolithic integrated quantum photonic circuits for future quantum applications.

# Integrated quantum photonic platforms and key devices

To give an overview, Fig. 1 summarizes the key milestones that lay the groundwork for the development of IQP technology and its quantum applications. IQP provides a versatile platform for on-chip generation, processing and detection of quantum state of light. A landmark result in IQP was the demonstration of quantum interference and the controlled-NOT (CNOT) entangling gate in silica-on-insulator optical waveguide circuits in 2008 (Fig. 2a) $^{14}$ . The achieved high fidelity demonstrated the inherent stability and controllability of IQP. Soon afterwards, on-chip state preparation and manipulation of single-qubit and two-qubit states were implemented in the same platform $^{16-18}$ , as well as in the laser-writing silica platform (Fig. 2b) $^{19-22}$ . In the decade that followed, significant process was made in materials, devices, functionality, and implementations of protocols and algorithms.

IQP platforms. A range of optical waveguide platforms have been developed for IQP applications, including silica-on-insulator

![](images/3b8f4b997878e2158f4e28357d32ed4074b1356af9f6fb9443ecdf6b234be0f9.jpg)  
Fig. 1 | Key demonstrations in IQP in the past decade. The first demonstration of on-chip quantum interference and integrated CNOT gate $^{14}$ , test of Shor's factoring algorithm $^{82}$ , laser-writing integrated quantum photonic circuits $^{19}$ , quantum walks with correlated photons $^{114}$ , near-optimal two-photon quantum interference $^{18}$ , the first re-programmable multifunctional quantum processor unit (QPU) $^{17}$ , waveguide TES detector with PNR ability $^{65}$ , Si waveguide SPSND with high efficiency $^{27}$ , observation of quantum interference in  $\mathrm{Si}^{24}$ , demonstrations of Boson sampling with multiple photons $^{97-101}$ , simulation of Anderson localizations with entangled photons $^{111}$ , near-optimal single-photon generation from a single QD $^{55}$ , the first integration of SFWM sources with quantum circuits $^{25}$ , high-efficiency QD source coupled into waveguide $^{58}$ , quantum simulation of molecular ground state $^{85}$ , demonstrations of chip-to-chip QKD and entanglement distribution $^{38,79}$ , demonstration of universal linear-optic circuit $^{83}$ , on-chip generation of six photons $^{50}$ , the first demonstration of scattershot Boson sampling $^{103}$ , test of Grover's search algorithm $^{91}$ , high-efficiency Boson sampling using a QD source $^{60}$ , test of quantum Hamiltonian learning (QHL) algorithm $^{123}$ , large-scale quantum circuits in Si with 670 components $^{44}$ , simulation of molecular vibrations $^{88}$ , demonstration of four-photon graph state $^{93}$  and on-chip generation of eight photons in  $\mathrm{Si}^{104}$ . The chronological order refers to the first date appeared in the public domain, including conference and preprint.

$(\mathrm{SiO}_2)^{14,16-18}$ , laser-writing silica $^{19-22}$ , silicon-on-insulator  $(\mathrm{Si})^{23-27}$ , silicon nitride  $(\mathrm{Si}_3\mathrm{N}_4)^{28-31}$ , lithium niobate  $(\mathrm{LN})^{32-34}$ , gallium arsenide  $(\mathrm{GaAs})^{35-37}$ , indium phosphide  $(\mathrm{InP})^{38,39}$ , silicon oxynitride (hydex) $^{40}$  and many others. For discussions on the IQP platforms, we refer to other review articles, while here we highlight a select few. For example, Si waveguides can tightly confine light, allowing direct single-photon generations in the waveguides and high-density integration (Fig. 2c,i) $^{41}$ .  $\mathrm{Si}_3\mathrm{N}_4$  provides ultralow propagation losses and can create single photons within a broad transparent window $^{28}$ . Laser-written circuits provide possibilities for investigating complex physical systems through three-dimensional circuit geometries (Fig. 2b) $^{42}$ . While the above are passive materials in general, LN (ref.  ${}^{33}$ ), GaAs (ref.  ${}^{36}$ ) and InP (ref.  ${}^{38}$ ) exhibit large electro-optical properties that allow for fast manipulations of single photons.

Qubit encoding and manipulation. A quantum state can be represented as a superposition of eigenmodes  $\sum_{i=0}^{d-1} c_i |i\rangle$ , where  $c_i$  is the complex amplitude in the  $|i\rangle$  mode and  $d$  is the size of the system. An integrated toolkit has been developed to encode, transmit and process quantum information in various degrees of freedom (DoFs) of the single photon, including location (path/rail), polarization, frequency, spatial and temporal modes. For example, the transverse electric and transverse magnetic modes in waveguides form polarization eigenstates<sup>43</sup> of a polarization encoded qubit. Engineering the birefringence of the waveguide allows the transformation of the polarized qubits, whose arbitrary operation is challenging in planar waveguides but more controllable in circular waveguides<sup>20</sup>. Photons that exist in a superposition of time bins  $|\tau\rangle$  can be initialized and measured by integrated Franson interferometers<sup>29</sup>. Photons can also exist in a superposition of frequency bins  $|\nu\rangle$ , which can be readily produced in optical resonators<sup>40</sup>. Photons simultaneously locating over dual/multiple waveguides  $|k\rangle$  form path-encoded qubit/ qudit states<sup>25,44</sup>, which can be arbitrarily prepared, manipulated and measured using re-programmable Mach-Zehnder interferometers (MZIs). Moreover, a multimode waveguide that supports more than one eigenmode enables a new DoF to encode quantum states in the high-order spatial modes  $|m\rangle$  (refs.<sup>45,46</sup>). The multidimensional nature of  $|\tau, \nu, k, m\rangle$  represents a distinguishing characteristic of photons. On-chip coherent controls of multiphoton, multidimensional and multi-DoF entangled states enable significant enhancement of information processing and communication capacities with integrated photonics.

Box 1 summarizes the on-chip building blocks for the operations of photonic states. Flexibly controlling a photon's DoFs can enrich functionalities greatly. For example, encoding states in polarization and time bin allows robust chip-to-chip quantum information transcieving and quantum communication via optical fibre. Encoding qubits in path allows extremely low error single-qubit and two-qubit operations, which is key for on-chip quantum information processing. Silicon-based MZIs with a  $65\mathrm{dB}$  on/off ratio was recently achieved by fabricating near-perfect beamsplitters[47], equivalent to having a Pauli-Z error rate of  $< 10^{-6}$ . Remarkably, having ultrahigh-precision operations, the overhead resources for MBQC can be significantly reduced[48]. This high controllability of path-encoding states has also been confirmed by the demonstrations of two-photon quantum interference with near-unity visibility of  $100.1 \pm 0.4\%$  in  $\mathrm{SiO}_2$  (ref. [18]) and  $100.0 \pm 0.4\%$  in Si chips[25].

Integrated SPs. Harnessing the power of IQP requires on-chip generation of a large number of identical single photons. We review two types of integrated SPs: parametric photon-pair source and QD single-photon source.

Pumping nonlinear waveguides or cavities allows the generation of photon pairs, via the spontaneous four-wave mixing (SFWM) (Fig. 2c) or the spontaneous parametric down-conversion (SPDC) process (Fig. 2d). These SPSs have been demonstrated in  $\chi^3$  waveguides (for example, Si (ref.  $^{49}$ ),  $\mathrm{SiO}_2$  (ref.  $^{50}$ ) and  $\mathrm{Si}_3\mathrm{N}_4$  (ref.  $^{28}$ ), and in  $\chi^2$  waveguides (for example, GaAs (ref.  $^{35}$ ) and LN (ref.  $^{33}$ ). A notable feature of integrated parametric SPSs is that they can be made highly identical and into an array, while each is individually controllable. We give two state-of-the-art examples: an array of 18 SFWM SPSs in  $\mathrm{SiO}_2$  waveguides  $^{50}$  (and 4 SFWM SPSs in Si microresonators  $^{51}$ ) can produce heralded single photons with a  $97\%$  ( $95\%$ ) photon-number purity,  $52\%$  ( $50\%$ ) heralding efficiency and  $95\%$  ( $91\%$ ) photon indistinguishability from separated SPSs. An issue for parametric SPSs is that they produce photons nondeterministically, typically with a  $5-10\%$  probability. However, this can be significantly improved through time  $^{52}$  or spatial  $^{53}$  multiplexing techniques. In ref.  $^{52}$ , a state-of-the-art multiplexing source is demonstrated in bulk optics, achieving a  $66.7\%$  high probability of single photons collected into a fibre and high indistinguishability of  $\sim 90\%$ .

QD SPSs offer the potential for deterministic generation of single photons, and self-assembled InGaAs/GaAs QD SPSs hold the best performance[54] for QD sources. A breakthrough in 2013

![](images/1b3b13d0139894c8d24b4ed7cef6f1419421715e8bcdbd2d3bfed925dff14862.jpg)

![](images/a21ac0f20f11bded52ffcbfe112cb056bdccd803a4f0e988d780760bfc43f7b7.jpg)  
Detectors

![](images/98ba022304cd70e98b6eaa04a3d40a6e58357bc77daf1b619fb1169bb8a35aa7.jpg)  
Fig. 2 | Integrated single-photon sources, detectors and circuits. a, The first IQP circuit for CNOT entangling operation in silica-on-insulator waveguides.  $C_i$  and  $T_i$  ( $i = 1,2$ ) are the control and target qubits.  $V_{A,B}$  are ancilla qubits. In the bottom left panel, regions I and III are the cladding layer, while II is the silica core layer. b, Laser-writing quantum circuit in silica that allows complex three-dimensional integration. c, An integrated SFWM SPS in Si photonic waveguides or microresonators that allows the generation of pure and identical photons. d, An integrated SPDC SPS in GaAs waveguides that sustains two different types of eigenmodes meeting the phase matching condition. W and D are the width and height of the waveguide, respectively. e, A semiconductor InGaAs/GaAs QD SPS that can efficiently emit pure single photons from a single dot embedded in a micropillar. f, An integrated TES PNR detector that is evanescently coupled to silica waveguides. g, An integrated SNSPD atop of a Si waveguide that can absorb and detect photons with >90% efficiency. h, An integration of a QD source with two SNSPDs in the GaAs photonic-crystal waveguide system that enables the on-chip detection of QD luminescence. i, An integration of four SFWM SPSs with re-programmable quantum photonic circuits in Si that allows the on-chip preparation, manipulation and measurement of photonic qubits T and B. R i (i = x, y, z) are rotation operators implemented by the phase shifters  $(\theta, \varphi)$ . j, An integration of Si photonic circuits with SNSPDs (A1,2 and B1,2) by using the micrometre-scale flip-chip process that allows on-chip detection of non-classical light. RF, radio frequency. Panels reproduced from: a, ref. 14, AAAS; b, ref. 42, Wiley; c, ref. 49, OSA; d, ref. 35, APS; e, ref. 56, APS; f, ref. 65, APS; g, ref. 27, under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); h, ref. 133, MDPI; i, ref. 41, IOP; j, ref. 64, under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/).

![](images/f03816b6c017d2bcb2785b247942e03fbd4223ebc93fb0ab3b4930f7feeb2c80.jpg)  
Integration

![](images/00a8efd208e9e275817b873e2221db2d99b1726ba1b2a4e846a235a7d0151e92.jpg)

![](images/bdd7a58e2c9a4999b4dabbcf6bce1ed623a94b524c29f419ec33e19a63d7820b.jpg)

![](images/d85b0fc567d4fb3879d335d62d9d2231c23e4f3b44af7d0f629c5539d35b8b45.jpg)

demonstrated near-optimal single-photon emissions from a single QD, by using a resonant excitation technique $^{55}$ . A  $99.1\%$ $(99.7\%)$  single-photon purity,  $66\%$ $(65\%)$  extraction efficiency and  $98.5\%$ $(99.6\%)$  photon indistinguishability have been achieved in a single QD $^{56}$  (and several QDs samples $^{57}$ ). These micropillar-based QDs emit photons out-of-plane (Fig. 2e), presenting ease of fibre coupling but difficulty in waveguide integration. Instead, QD SPSs in photonic-crystal waveguides allow near-unity preferential emission into the waveguide $^{58}$ . A major challenge however is to create multiple, identical QD SPSs, due to the difficulty in dot-to-dot uniformity and inhomogeneous broadening. A solution is to actively de-multiplex the single photons from a single dot into different spatial modes $^{59}$ . This scheme produces multiple photons at a reduced

overall rate, and has shown a great success in recent Boson sampling implementations $^{60-62}$ . Much progress has been made towards the generation of indistinguishable photons directly from separate dots.

Integrated SPDs. On-chip detection of single-photon is required to read out the quantum information. Several SPD technologies are available $^{63}$ , including avalanche photodiodes, superconducting nanowire single-photon detectors (SNSPDs) and transition edge sensors (TESs). Fully integrated SNSPDs can be patterned on GaAs (ref.  ${}^{37}$ ), Si (ref.  ${}^{27}$ ) and  $\mathrm{Si}_3\mathrm{N}_4$  (ref.  ${}^{31}$ ) waveguides. In 2011, the first waveguide-integrated SNSPD was demonstrated in the GaAs (ref.  ${}^{37}$ ) platform, and the following year a breakthrough result demonstrated evanescently coupled Si waveguide SNSPDs with a  $91\%$

# Box 1 | Integrated building blocks for operating photonic states

Quantum interference plays a key role in photonic quantum technology. Two-photon quantum interference occurs when two indistinguishable photons meet at a balanced beamsplitter (BS), and the probability of both photons being reflected or transmitted cancel out. Inducing distinguishability no matter in which DoF yields the observation of HOM dip or interference. We take the path-encoded qubits as an example to illustrate on-chip building blocks for quantum applications.

Directional coupler and MMI are two types of integrated beamsplitters, whose unitary is represented as a Hadamard-like operator  $(\hat{H})$ . An MZI with two directional couplers/MMIs and one re-configurable phase shifter  $(\hat{P})$  can reliably perform classical and quantum interference. The relative phase is induced by changing the refractive index of one arm, for example, by thermo-optic or electro-optic effects. A combination of one MZI and two additional phases enables an arbitrary SU(2) unitary transformation. It is such a simple device that allows arbitrary but precise preparation, operation and analysis of a path-encoded single qubit as  $\alpha |0\rangle +\beta |1\rangle$ , where  $\alpha$  and  $\beta$  are complex values, and  $|0\rangle$  and  $|1\rangle$  are logical states.  $\hat{X}$  refers to the Pauli-  $X$  operator. When the two identical photons meet at an MZI, photons at outputs present a superposition of bunching state and antibunching state, dependent on the phase in the MZI. This is referred to the HOM-like or reverse-HOM interference[25]. Photonic two-qubit entangling operations are enabled by quantum interference[9]. The circuit diagrams illustrate three types of two-qubit operations for path-encoded qubits:  $\hat{\mathrm{O}}_{\mathrm{BS}}$  functions in analogy to a BS on two polarized qubits, where each qubit has a  $50\%$  probability of being found in either  $1^{\prime}$  or  $2^{\prime}$  regardless of its input;  $\hat{\mathrm{O}}_{\mathrm{PBS}}$  transmits  $|0\rangle$  and swaps  $|1\rangle$  mode in analogy to a polarization beamsplitter (PBS) transformation;  $\hat{\mathrm{O}}_{\mathrm{CZ}}$  presents the Knill-Laflamme-Milburn CZ operation, consisting of several BSs with different reflectivity. We briefly summary the basis of these operations without going into detail: they all allow measurement of qubits in the Bell basis, performing Bell analysis;  $\hat{\mathrm{O}}_{\mathrm{PBS}}$  enables the fusion operation that can be adopted to create multiphoton star-graph states; performing

$\widehat{\mathrm{O}}_{\mathrm{CZ}}$  allows the generation of cluster states. The non-interaction nature of single photons leads to non-deterministic two-qubit operations, with a successful probability of  $1/2$  for  $\widehat{\mathrm{O}}_{\mathrm{BS}}$  and  $\widehat{\mathrm{O}}_{\mathrm{PBS}}$ , and  $1/9$  for  $\widehat{\mathrm{O}}_{\mathrm{CZ}}$ . Notably, the two-photon quantum interference that occurs at a  $2\times 2$  BS represents the most basic scenario, and can be further generalized to  $n$ -photon quantum interference in a  $m$ -mode unitary  $\widehat{\mathrm{O}}_{\mathrm{LO}}$ . A well-known example is the Boson sampling problem<sup>13</sup>, which is believed to be an intractable task for classical computers but efficiently executable in a specific quantum machine.

![](images/106ec8bc5c6810c5040b78b24e33af9b2955cf27db9ab2e13ca236d1080e43a7.jpg)

![](images/5346f1aaae06c2281c6bd488adb9dcef72803cd103fa5ff721a6c2a0bc75b2fe.jpg)

![](images/4140cb0680a04a34d81b35c044e32fd7cabdbb1454f93e2bccae34055902b631.jpg)

![](images/a3ab8dc8e7a90164fcdd1483af9ea4034232122875bdf105adac38318c081d8e.jpg)

![](images/36b66e521245ca32078dbdfe232371237b1cbe1d339929a154f0bb28a4933617.jpg)

![](images/20c975baaca3c7a1bffaa198dce162441a23cbdcdff9b8fbbe03ec09f239fe34.jpg)

![](images/160b25ad10498490f14fad7a68e51d09f374c5d0180252c1baed75159d7b3f0f.jpg)

detection efficiency, 18 ps jitter and  $50\mathrm{Hz}$  dark count (Fig. 2g) $^{27}$ . Instead of direct deposition, SNSPDs fabricated on  $\mathrm{Si}_3\mathrm{N}_4$  membrane can be flexibly transferred to other substrates (Fig. 2j) $^{64}$ . Moreover, photon-number-resolving (PNR) detection is required in many quantum protocols $^{63}$ . Such PNR TESs have been evanescently integrated on  $\mathrm{SiO}_2$  (Fig. 2f) $^{65}$  and LN waveguides $^{34}$ , with demonstrations of up to five-photon resolution. A series of integrated SNSPDs atop a GaAs waveguide allows the on-chip PNR detection of up to four photons $^{66}$ . The SNSPDs and TESs however only operate at cryogenic temperature. Recently, waveguide-coupled germanium-on-silicon avalanche photodiodes were demonstrated with a detection efficiency of  $5.27\%$  at  $1,310~\mathrm{nm}$  at  $80~\mathrm{K}$  (refs. 67,68), showing a great promise for future room-temperature chip-based quantum photonic applications.

# Chip-based quantum communications

Quantum communication aims to share encrypted keys between the transmitter and receiver based on the law of quantum mechanics, such that the achieved security is inaccessible by classical communications. The best-known example is quantum key distribution (QKD). Integrated photonics enables a robust, miniaturized and low-cost platform to realize QKD transmitters and receivers. We review recent experimental progress in chip-based QKD hardware capable of implementing superposition-based and entanglement-based protocols.

For discussions on advanced QKD protocols and physical realizations in bulk optics and fibre optics, we refer to other reviews<sup>5</sup>.

Superposition-based QKD. Integrated photonics is a well-established technology developed and deployed in the global telecommunication industry. As such, it is natural to use integrated photonics for practical QKD applications to transcendenewed keys. Pioneer studies began in 2004 with  $\mathrm{SiO}_2$ -based optical interferometers fabricated for time-bin QKD systems in fibre[69]. More recently, the first fully integrated chip-to-chip QKD system was implemented with an InP transmitter chip and a silicon oxynitride  $(\mathrm{SiO}_x\mathrm{N}_y)$  receiver chip (Fig. 3a)[38]. The InP QKD transmitter incorporates all the necessary components such as a tunable laser, attenuator and electro-optic phase modulators. The  $\mathrm{SiO}_x\mathrm{N}_y$  QKD receiver consists of thermo-optic phase shifters, which allows for digitally reconfigurable delay line and state measurement. Photons were detected by off-chip SNSPDs. These trancievers provide a complete chip-to-chip QKD solution, and could be programmed to implement multiple protocols, including BB84 at a  $560~\mathrm{MHz}$  state rate, coherent-one-way operating at a  $860~\mathrm{MHz}$  state rate, and differential phase shift at a  $1.76~\mathrm{GHz}$  state rate[38].

Silicon photonics is an appealing technology platform for QKD applications due to cost-effective manufacturing and compatibility with CMOS electronics. Fast manipulation of single photons in Si

![](images/4107dae9f8aa5818257920fff3ecec66ea64e9b63b529930abcd0103b1871854.jpg)

![](images/597d29d2c2d8aab704b8b45f4288fe758104a40cf71f9dfc4d41531afe9aaaeb.jpg)

![](images/97c0d4a6044d87232925e15c0c0e33106c8f9aeafaaf67dc49ae3fcaac547602.jpg)

![](images/4ad1f0a0e9b7704766413c771157c0645735f7090d41433687bb6d5bfa517592.jpg)  
Fig. 3 | Integrated photonic devices for quantum communications. a, A chip-to-chip QKD system between a  $2 \times 6 \mathrm{~mm}^2$  InP transmitter and a  $2 \times 32 \mathrm{~mm}^2$  SiO $_x$ N $_y$  receiver. The transmitter consists of a tunable laser, electro-optical phase modulators (EOPMs) and MZIs, allowing for pulse modulation (P.MOD), phase randomization (PH.RAND) and intensity modulation (I.M). The receiver consists of thermo-optical phase shifters (TOPSs) and reconfigurable delay lines (T-DEL), allowing for phase decoding (PH-DEC). b, A chip-to-chip entanglement distribution system between two Si chips linked by a 10 m single-mode fibre (SMF). Path-entangled states are generated on a  $1.2 \times 0.5 \mathrm{~mm}^2$  chip A, and then coherently distributed to a  $0.3 \times 0.05 \mathrm{~mm}^2$  chip B, by using path-polarization converters (PPCs) (based on two-dimensional grating coupler) on each chip. D1,2,3,4 are SNSPDs. c, An Si-based transmitter for polarization-encoded QKD. The transmitter consists of ring modulator, variable optical attenuator (VOA) and polarization modulator, all in a  $1.3 \times 3 \mathrm{~mm}^2$  area. The ring modulators generate periodic nanosecond pulse trains, while the polarization modulator prepares two sets of orthogonal polarized states for BB84 QKD. d, Si-based transmitter for a metropolitan QKD system in Massachusetts Institute of Technology (MIT). Alice is located in Cambridge and Bob is located in Lexington, connected by a 43 km dark fibre. Alice prepares the polarization states using a 10 Gbps EOPM and a PPC, while Bob measures the states using fibre-based components. BS, beamsplitter; PBS, polarization beamsplitter. e, A fully integrated QRNG in an InP chip. The device is composed of two distributed feedback (DFB) lasers, a balanced MMI beamsplitter and two photodetectors for heterodyne detection. One laser is operated in gain switching (GS) mode, while the other is in continuous wave (CW) mode. QRNG rates in the Gb s $^{-1}$  regime were obtained. Panels reproduced from: a, ref. $^{38}$ , under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); b, ref. $^{79}$ , OSA; c, ref. $^{70}$ , OSA; d, ref. $^{72}$ , OSA; e, ref. $^{39}$ , OSA.

![](images/23da0c4c7246ba0675d25ab0d2373ab59714a42b85149b4531bc1b533b3425ec.jpg)

is challenging due to the lack of efficient electro-optic modulation. However, carrier injection or depletion modulation allows sufficient state preparation for QKD with a megahertz to gigahertz rate, though loss is high. Recently, three groups have demonstrated Si-based QKD transmitters: in ref.  $^{70}$ , the transmitter prepares polarization-encoded qubits for a BB84 system over a  $5\mathrm{km}$  fibre (Fig. 3c); in ref.  $^{71}$ , two transmitters were developed, one for polarization-encoded and the other for time-bin-encoded BB84 systems; in ref.  $^{72}$ , the transmitter was tested in a real-life QKD system, in which Alice was located in Cambridge and Bob in Lexington (Fig. 3d). In these demonstrations, secret key rates of kilobits per second to megabits per second and low quantum bit error rates of  $1.0 - 5.4\%$  were obtained. Weak laser sources were coupled off-chip. A hybrid integration of Si and III/V active materials promises fully integrated QKD transmitter chips.

Multiplexing QKD. Secreted key rates can be further increased by exploiting multiplexing techniques. Taking wavelength-division multiplexing as an example, multiple keys can be co-distributed

in a single fibre but at different wavelengths. A proof-of-concept demonstration of wavelength-division multiplexing QKD system comprising two InP transmitters and a single  $\mathrm{SiO_xN_y}$  receiver achieved increased key rates by a factor of two, to  $1.11\mathrm{Mbit}s^{-1}$  over a  $20~\mathrm{km}$  emulated fibre[73]. Another example is an implementation of a multidimensional chip-to-chip QKD system on two Si chips, based on space-division multiplexing in a multicore fibre[74]. The prepare-and-measure protocol is applied for four-dimensional states by the Si transmitter and receiver. Low quantum bit error was achieved.

Measurement-device-independent QKD. QKD is rigorously secured; however, practical implementations can be imperfect, leaving loopholes that undermine the security of the system. One significant example is detector side attacks, and measurementdevice-independent (MDI) QKD was proposed and demonstrated to tackle this vulnerability. Recently, two independent studies tested the feasibility of using integrated photonics for MDI QKD, demonstrating the key part of the protocol, that is, Hong-Ou-Mandel (HOM) interference. HOM interference between weak coherent

states from two independent InP chips was observed with a high visibility of  $46.5 \pm 0.8\%$  in ref. [75], and from two Si/III-V hybrid integrated lasers with a high visibility of  $46 \pm 2\%$  in ref. [76] (note maximal achievable visibility is  $50\%$ ). Integrated photonics may provide an ideal platform for multiuser chip-based MDI QKD networks, in which users only pay for low-cost photonic chips, while the most expensive parts (for example, SNSPDs) are shared among many users in an untrusted node.

Entanglement-based QKD. Fully device-independent QKD and the multinode quantum internet are examples of systems that rely on entanglement generation and distribution. In pioneering work in 2002, entangled time bins for  $\mathrm{QKD}^{32}$  were created using periodically poled lithium niobate waveguides. Recently, time-bin entangled states were generated in GaAs (ref.  $^{77}$ ), Si (ref.  $^{78}$ ) and  $\mathrm{Si}_3\mathrm{N}_4$  (ref.  $^{29}$ ) chips. Entangled time bins across the visible-telecom range were produced in a delicately engineered  $\mathrm{Si}_3\mathrm{N}_4$  microresonator and distributed over a  $20\mathrm{km}$  fibre[28]. The first chip-to-chip entanglement distribution[79] (Fig. 3b) and quantum teleportation[51] were demonstrated between two programmable Si chips that integrated all key components, including entangling photon sources and Bell measurement. These systems were stabilized by developing a path-polarization conversion technique, which were subsequently adopted in the prepare-and-measure QKD systems in refs.[70-72]. To reach longer distances or to ultimately build a quantum internet, quantum repeater and memory are required. Ground-to-satellite QKD are also being explored as an approach to extend the operating distance to the global scale.

Integrated quantum random number generator. Random number generator (RNG) is a key device in many fields of science and technology, and particularly in QKD, and quantum (Q)RNGs provide a high-entropy high-rate source of trusted random numbers. Integrated QRNGs have been demonstrated based on various nondeterministic quantum processes, such as phase fluctuation $^{39,80}$ , vacuum fluctuation $^{81}$  and non-locality $^{44}$ . For example, fully integrated QRNGs have been demonstrated in InP chips (Fig. 3e) $^{39,80}$ , in which random numbers were generated from the random phase fluctuations of two-laser interference. All these QRNGs report gigabits-per-second operations. Moreover, quantum theory allows a stronger form of certified randomness, that is, device-independent QRNG. By violating the Bell inequalities for multidimensional entangled states in a Si chip, randomness was certified in the fully device-independent scenario $^{44}$ . We expect compact, robust, fast and low-cost QRNGs in photonic chips may find intermediate applications.

# On-chip quantum information processing with photons

In the gate-based quantum computing model, interactions between photons are realized by including ancillary circuitry and photons<sup>9</sup>. The partial state collapse, which follows from detecting the ancillary photons in the ancillary modes, implements the required quantum logic. By teleporting quantum information across photonic circuitry, from gates that operated successfully, quantum computation is possible<sup>10</sup>. Yet the overheads for this scheme appear to be forbidding at a practical level. The MBQC presents a significantly more resource-efficient quantum computing model<sup>11,12</sup>. In this scheme, the challenge from requiring deterministic gates can be shifted to constructing a generic entangled cluster state, on which any quantum computation can be mapped by a sequence of measurements. Remarkably, MBQC offers tremendous advantages for photonic realizations because of its comparability with photons' probabilistic nature<sup>12</sup>.

This part summarizes the development of quantum hardware on IQP chips, for the gate-based and MBQC-based quantum information processing, and their implementations of algorithms. High re-programmability is a key feature of IQP, and it allows multifunctional processing of tasks.

Gate-based quantum information processing. The building blocks for the gate-based scheme have been demonstrated in photonic chips. For example, the CNOT gate was first demonstrated in a  $\mathrm{SiO}_2$  chip $^{14}$ , then in laser-writing  $\mathrm{SiO}_2$  (ref.  $^{22}$ ), Si (ref.  $^{41}$ ) and many others. These initial demonstrations implemented a unheralded CNOT scheme that does not include the ancillary photons required for scaling; nevertheless, it was possible to demonstrate a rudimentary version of Shor's factoring algorithm using a  $\mathrm{SiO}_2$  chip with two CNOT gates (Fig. 4a) $^{82}$ . It allows a factorization of 15 with a high fidelity of  $99 \pm 1\%$ . The first integrated heralded CNOT gate was performed using a  $\mathrm{SiO}_2$  chip able to perform universal linear-optic operations $^{83}$ . The type of teleportation required to shuttle successfully quantum information from heralded gates was also demonstrated on-chip with three photonic qubits and one CNOT gate in a laser-writing  $\mathrm{SiO}_2$  chip (Fig. 4b) $^{84}$ . It achieved the single-chip teleportation of single-qubit states with an average fidelity of  $89 \pm 3\%$ .

Programmable quantum chips for multifunctional information processing. Re-programming photonic chips allows the processing of multiple quantum tasks and algorithms in a single chip. The first fully programmable two-qubit quantum photonic processor was demonstrated in a  $\mathrm{SiO}_2$  chip in 2011 $^{17}$ . The device includes single-qubit preparation and measurement, as well as two-qubit entangling operation. It was reconfigured to perform thousands of experiments while remaining high fidelity, to study the wave-particle duality in a quantum delayed-choice experiment, and to implement a quantum algorithm that can compute the ground-state energy of molecules $^{85}$ . The first reconfigurable laser-writing device was also demonstrated recently $^{86}$ . A Si photonic quantum processor able to initialize, operate and analyse arbitrary two-qubit state and process was demonstrated by adopting a linear-combination scheme (Fig. 4c) $^{87}$ . The device was programmed to implement 98 different logic gates (for example, CNOT, CZ, CH and SWAP), and achieved an average quantum process fidelity of  $\sim 93\%$ . Multiple algorithms are implemented in the device, such as a quantum approximate optimization algorithm for a three-example constraint satisfaction problem.

Universal linear-optic (ULO) circuits able to implement all possible optical quantum protocols have been proposed and experimentally realized in re-programmable optical circuits. The first universal linear-optic circuit was realized in a single  $\mathrm{SiO}_2$  chip in 2015 (Fig. 4d) $^{83}$ , which consists of a six-mode triangularily arranged MZI network. The versatility of this universal circuit was demonstrated for several key applications, including the implementations of heralded CNOT gate, 100 different Boson sampling with verification tests, six-dimensional complex Hadamard operations $^{83}$  and quantum simulation of vibrational dynamics of molecules $^{88}$ . Recently, an eight-mode universal linear-optic circuit was also demonstrated in a  $\mathrm{Si}_3\mathrm{N}_4$  chip $^{89}$ . The above demonstrations rely on the thermo-optic phase modulation to manipulate the single-photon states at microsecond-millisecond speed, which requires fast electro-optic phase modulation at nanosecond speed.

Entanglement generation, manipulation and measurement and MBQC. The generation, manipulation and measurement (GMM) of entangled states is at the heart of MBQC. On-chip GMM of entangled states requires an integration of at least sources and circuits. For example, the first GMM of entangled two-qubit states encoded in dual paths was demonstrated in a Si chip in 2015, with the inclusion of SFWM SPSs and circuits $^{90}$ . The GMM of multidimensional entanglement in multipaths was demonstrated in a large-scale Si chip with 16 waveguide SFWM SPSs $^{44}$  and up to 15-dimensional entangled states can be GMM in an universal manner. A coherent excitation of multiple frequency bins of two photons results in multidimensional entanglement in the frequency domain $^{40}$ , in which arbitrary operations on a qudit can be performed using standard fibre components.

![](images/b803f724c6d7a0e56bedeee49868d7fde29d0f50a2ca9eb81f4b5891169f5e28.jpg)  
a

![](images/f6a0bd5723b0a59a61c9f137ce4f3044255be58dc02f87359f65e43296e07933.jpg)  
b

![](images/b90f141a4593d85b25e6513c2fd19b0543099e9e134ea434eb84500b78622d29.jpg)  
Multifunctional QIP

![](images/bc27f58c39f756082f2f0da5026b97a69bffaf7440d5d91869e33e2d8d8836b0.jpg)  
d

![](images/2e0a289c81667dbda591c05ee0a038570dbec7248b234a96d86c527ca6f8a936.jpg)  
Six-mode ULO

![](images/959009cf0c0c97cbb35c5dbecf7c47cbc8832948523b68d3e2e667bed04c85ef.jpg)  
MBQC-based QIP

![](images/d8c804a4e57be37e9fa67c8527e294f4342038ba5333a067d0c033b19ae13f96.jpg)  
Fig. 4 | Quantum information processing and computing with integrated optics. a,b, Implementations of gate-based quantum information processing (QIP). In a, a compiled version of Shor's factoring algorithm was performed in a  $\mathrm{SiO}_2$  chip that consists of two CZ gates and six Hadamard (H) gates. Four photons from SPDC bulk optic sources were coupled into the photonic chip. The  $x_{1,2}$  qubits carry the result of the algorithm;  $f_{1,2}$  are additional qubits required. QFT, quantum Fourier transform. In b, quantum teleportation of photonic qubits was performed in a silica device. A Bell state encoded on qubits [Q2,Q3] are prepared, and a Bell state measurement is performed on [Q1,Q2] qubits.  $\theta$  and  $\varphi$  indicate the rotations performed on each qubit. Z refers to the Pauli-Z gate.  $\hat{U}$  is the local rotation on the state  $\rho$ . c,d, Multifunctional quantum information processing using fully re-programmable quantum photonic chips. In c, a universal two-qubit quantum processor was realized in a re-programmable Si chip. The chip monolithically integrates 4 SFWM waveguide sources, 58 TOPSs and 82 MMIs. The device was programmed to implement 98 two-qubit [Q1,Q2] unitary operations with high fidelities. P1,2 and Q1,2 are single-qubit gates,  $\sigma_{i}(i = x,y,z)$  and I are identity and Pauli gates. U LC is a unitary operation. In d, a six-mode universal linear-optic device was realized in a fully re-programmable silica chip. The device consists of a cascade of 15 MZIs and 30 TOPSs, and up to 6 photons were injected into the chip from bulk optic SPDC SPSs. The device was re-programmed to implement multiple information tasks. In e, four-qubit linear and box cluster states were generated in a  $\mathrm{SiO}_2$  chip. This was enabled by manipulating the two-photon four-qubit hyper-entangled state and cluster state that were encoded in photon's path and polarization DoFs. IAB and  $r_{A,B}$  are the selected spatial modes. In f, four-photon star-graph  $(|S_4\rangle)$  and line-graph  $(|L_4\rangle)$  states were generated in a Si device. Four photons in two pairs were generated in four SFWM waveguide sources. Two red-coloured qubits were operated on by a reconfigurable entangling gate, performing either a fusion or CZ operation. Panels reproduced from: a, ref. 82, AAAS; b, ref. 84, Springer Nature Ltd; c, ref. 87, Springer Nature Ltd; d, ref. 83, AAAS; e, ref. 91, under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); f, ref. 93, under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/).  
f

MBQC relies on large entangled cluster states. The first on-chip GMM of four-qubit cluster state was realized in a  $\mathrm{SiO}_2$  chip (Fig. 4e), by manipulating both the polarization and path DoFs of two photons[91]. Four-qubit linear-cluster and box-cluster states were generated and measured. Importantly, the Grover's search algorithm for a four-element database problem was demonstrated for the first time using photonic MBQC devices. This implementation of multi-DoFs entanglement can be extended to multidimensional systems. For example, a three-level four-qubit cluster state was generated in a hydex microresonator, by independently manipulating the time and frequency DoFs of two photons[92]. A proof-of-concept qutrit MBQC was performed to show high noise robustness.

The on-chip GMM of truly four-photon four-qubit graph states was demonstrated in a Si photonic chip (Fig. 4f) $^{93}$ . The device includes waveguide SFWM SPSs creating two pairs of single photons and a reconfigurable two-qubit linear-optic operator. Performing the fusion operation or CZ operation (see Box 1) generates the line-graph or star-graph states. Recently, another state-of-the-art Si photonic quantum device with an array of nearly optimal SFWM SPSs in microresonators and high-quality reconfigurable circuits was coherently controlled to demonstrate and verify the genuine multipartite entanglement $^{51}$ .

# On-chip sampling of photons and quantum simulation

Intermediate-scale quantum photonic devices offer the possibility of demonstrating a quantum advantage over classical computers for specific tasks[94]. Boson sampling is destined for such a task and highly suited to the IQP implementation. While classical computers are fundamentally inefficient at tackling complex systems governed by the law of quantum mechanics — for example, quantum dynamics of molecules — engineering specific quantum devices that are inherently controllable to efficiently simulate quantum systems is a promising approach within different scenarios[7].

Multiphoton interference. The adoption of IQP has allowed observation of the generalization of the HOM effect (Box 1). The observation of a three-photon Bosonic coalescence via a tritter device — the extension of the beamsplitter from two to three input modes — has been demonstrated by exploiting a laser-writing technique $^{95}$ , via an integrated device containing three coupled interferometers $^{96}$ .

Boson sampling. The Boson sampling problem consists of simulating the following quantum experiment: input  $n$  bosons in different modes of an  $m$ -mode linear interferometer and sample events from the distribution of bosons at the interferometer's output modes<sup>13</sup>.

![](images/b49faa73103387961a9005c00a35547c652bcdae04f2aca874c041b19a6dbf9e.jpg)  
a  
Quantum Boson sampling

![](images/9771f5d5be6ff5c98ae5d2fd2fb68a93c28c0b4360ae20fe45d949921f1459ad.jpg)  
b  
Simulate molecular energy

![](images/6058b4faa016366a88ae9d165c8a485bf585491f34624de10d787cb8db5ac984.jpg)  
Simulate localization  
Simulate molecular vibration

![](images/8248fec91e7485117510f1154fc66feada3fde498cf8c4efc5f9558c31c5ec0c.jpg)  
d  
Simulate quantum transport  
Hamiltonian learning

![](images/d0aafc38057e31e0902a3defdfdb3e825e83486401a8c432b030b7a51f7e6139.jpg)  
e

![](images/a1425abfa977c6526cea79cf033a69fe0524170b4d608290d575a24018d988bd.jpg)

![](images/af0cc1650fb402c4d6c681dcc6ac585e7bc84421b40ad363f6fd1d1dfb3cbdd2.jpg)

![](images/577c3728fc2bcbcf68f613691146071e2b077c0e7550b905dda113c623b87953.jpg)  
f

![](images/2dcafa90c082f36cdf6069007847c682a3d11ca2255f92247195564443864f93.jpg)

![](images/40bb827e4dc1b671b1c1d404336d56e0b32af3ec7cdd5b054962dfd0478a79ef.jpg)  
Fig. 5 | On-chip quantum simulation of physical and chemical systems with photons. a,b, Scattershot Boson sampling and QD-enabled Boson sampling. In a, scattershot Boson sampling with three photons was implemented using six SPDC bulk optic sources in a 13-mode  $\mathrm{SiO}_2$  chip. Scattershot reaches an exponential enhancement in sampling rate ( $k >> n$ ), by simultaneously pumping  $k$  parametric sources, and measuring  $n$  photons in a random but heralded set of input ports. b, Implementation of five-photon QD Boson sampling with a rate of  $4\mathrm{Hz}$ . Near-optimal single photons emitted from a single QD were actively de-multiplexed into five spatial modes, and the five photons were scattered in a ultralow-loss  $9\times 9$  photonic circuit. c,d, Simulations of physical quantum phenomena and processes via quantum walks. In c, Anderson localization was observed in a disordered material in a laser-writing chip that is able to perform quantum walks with 16 spatial modes and up to 8 time steps. Symmetry/antisymmetry entangled states were injected into the circuits to mimic the behaviour of bosons and fermions. Colour bar refers to the normalized probability distribution. In d, environment-assisted quantum transport is observed by controlling and mapping static and dynamic disorder in a re-programmable Si chip. The device is composed of 176 TOPSs and 88 MZIs in a  $4.9\times 2.4\mathrm{mm}^2$  area. Time (T) is defined from left to right, and space (i) is defined from top to bottom. Inset: enhanced quantum transport process from the site  $i_{t}$  to  $i_{f}$  in a disordered system ( $c_{d}$ ). e,f, Simulations of ground-state eigenenergy and vibronic modes of molecules. In e, a quantum variational eigensolver algorithm was implemented by combining a reconfigurable GPU in silica with a conventional computer. The ground-state energy and bond dissociation curve for the  $\mathrm{He - H^{+}}$  molecule were calculated.  $\varphi_{i}$  refers to the tunable TOPSs. dc are directional couplers. In f, exploiting a mapping between vibrations in molecules and photons in waveguides allows the simulation of vibrational dynamics of the atoms within molecule. Several four-atom molecules with up to six-mode vibrational modes are simulated by a  $\mathrm{SiO}_2$  chip.  $U_{L}$  refers to a unitary released by linear optics. g, An interface between a quantum simulator and target quantum system is enabled by a QHL approach. The system Hamiltonian can be efficiently learned by a quantum simulator that embeds an abstract model  $\hat{H}(x)$  where  $x$  is the parameters of Hamiltonian. A re-programmable Si photonics quantum simulator and an electron-spin system in a nitrogen-vacancy centre are interfaced, and the former was used to simulate the dynamics of the latter, obtaining its Rabi frequency  $\omega_0$ . Panels reproduced from: a, ref. 103, AAAS; b, ref. 61, APS; c, ref. 112, Springer Nature Ltd; d, ref. 47, Springer Nature Ltd; e, ref. 85, under a Creative Commons licence (https://creativecommons.org/licenses/by/4.0/); f, ref. 88, Springer Nature Ltd; g, ref. 123, Springer Nature Ltd.

![](images/7405f9b968ef2c191d5eefb5eb64dae57dfad1520c20b9eeb3217206ac61f58e.jpg)  
g

![](images/89661e60115950d1861911af5b0932ab1768f0e28cc77dc5351ea9accf1a4000.jpg)

If performed with indistinguishable bosons, this experiment results in an output distribution that is hard to sample, even approximately, on classical computers. In fact, the calculation of the probability associated with each observed Boson sampler event requires the estimation of a permanent, notoriously intractable matrix function<sup>13</sup>. The input for the classical simulation consists of the unitary matrix  $U$  describing the interferometer and the list of  $n$  input modes used. It is desirable to choose  $U$  randomly, both to avoid regularities that could simplify the classical simulation and because the main hardness-of-simulation argument holds for uniformly sampled unitaries.

The first experimental demonstrations of Boson sampling were reported with  $n = 3$  photons[97-101], mainly in integrated photonics.

Since then, several investigations have been performed to study the scalability in imperfect conditions, such as in the presence of losses, partial distinguishability $^{102}$  and generic experimental errors. To date, the highest number of photons generated in a Boson sampling experiment has been through the de-multiplexing of a single QD  $\mathrm{SPS}^{60-62}$  (Fig. 5b).

A generalized Boson sampling scheme, known as scattershot, has been proposed to overcome the limitation of probabilistic SPDC/ SFWM SPSs. It has been demonstrated first on-chip via bulk-optic SPDC  $\mathrm{SPSs}^{15,103}$  (Fig. 5a), and recently via a fully integrated chip via SFWM  $\mathrm{SPSs}^{104}$ . An alternative model known as Gaussian Boson sampling that uses squeezed light has been proposed and

![](images/cf5fdefdc59b6c9425fd442613ae9dd7df7088395c20234f549269597dae97aa.jpg)  
a  
Fig. 6 | Towards a large-scale integration of quantum photonic circuits. a, Scaling in Si quantum photonics circuits. Points in the plot refer to the number of optical components, which are respectively reported in refs. $^{24,25,44,47,90}$ . The chronological order refers to the formal publication dates. Inset shows a linear-scale plot. b, A state-of-the-art large-scale integrated quantum photonic circuit in silicon. The device fully integrates 16 waveguide SPSs (spirals), 93 reconfigurable TOPSs (orange parts), 122 MMIs, 376 crossers and 64 grating couplers, in total 671 optical components. The device was re-programmed to demonstrate the on-chip GMM of multidimensional entangled states with high controllability and universality, to certificate up to  $15 \times 15$  dimensional two-photon entangled states, and to implement multiple quantum information tasks. The two insets are photographs of the device. Silicon waveguides and 16 SFWM sources can be observed as blue lines. Gold wires allow the electronic access of each TOPS. Panel b reproduced from ref. $^{44}$ , AAAS.  
b

![](images/44565cf190fdf855f6f972a1aaffeecdff56776036d5412f427f0babac501099.jpg)

demonstrated in bulk optics $^{105}$ . Both Gaussian and scattershot Boson sampling have been implemented in the same Si photonic chip $^{104}$ .

Validation of Boson sampling. An open problem is to what extent the correctness of the outcomes of a quantum hardware can be certified. In this framework, Boson sampling represents a relevant benchmark for testing different procedures to validate the obtained calculation/simulation: could it be possible to exclude that the Boson sampling device is sampling from another specific different probability distribution, instead of the nominal one? To what extent can a validation procedure be pushed towards a full certification of the device?

A full certification of Boson sampling is believed to be not possible<sup>106</sup>; accordingly, all existing protocols aim at excluding the most plausible alternative scenarios. Currently, different protocols have been developed to validate Boson sampling, most of which have already been successfully demonstrated experimentally with integrated photonics hardware<sup>83,100,107-109</sup>.

Regime of quantum advantage. A fundamental question is which physical resources in terms of number of photons, number of modes and other relevant physical parameters are necessary to achieve the regime of quantum advantage. In the past few years, an increasing effort has been devoted to define the classical limits on the simulation of Boson sampling: experiments will need to operate with  $>20$  photons before they can start to challenge conventional computers (regime of quantum advantage) and  $>50$  photons to surpass supercomputers (regime of quantum supremacy) $^{110}$ .

Simulation via quantum walks. Quantum walks are the extension of classical random walks to a quantum framework and can be adopted as a resource structure for quantum simulations. Quantum walks can be divided in two different classes: discrete-time quantum walks, where the evolution is stroboscopic since it occurs in discrete steps; and continuous-time quantum walks, where the evolution on a given lattice is described by a Hamiltonian associated with the coupling between the different sites. Quantum walks have been implemented both in the single-particle and multiparticle regimes, where quantum interference between the different particles is occurring during the quantum dynamics.

The discrete-time quantum walk allowed the observation of single-particle and two-particle Anderson localization with Bosonic

and Fermionic statistics (Fig. 5c) $^{111,112}$ , and the entanglement growth after a spin chain quench $^{113}$ . The continuous-time quantum walk has been adopted to identify signature of Bosonic coalescence $^{114}$ , to simulate Fano resonance $^{115}$ , to shed light on the interplay between quantum coherence and noise for assist transport processes in complex networks $^{47,116,117}$  (Fig. 5d) and for quantum fast hitting on hexagonal graphs $^{118}$ . Laser-writing technology has been adopted to engineer chips with three-dimensional geometry, leading to implementation of two-dimensional quantum walks for the simulation of different physical process $^{116,119}$ .

Molecular simulation. Efficient simulation of molecular properties is fundamentally interesting in quantum chemistry $^{7}$ . Quantum phase estimation $^{120}$  and a variational eigensolver $^{85}$  were implemented in IQP chips to compute the ground-state energy of molecules such as  $\mathrm{H}_{2}$  and  $\mathrm{He - H^{+}}$  (Fig. 5e). An algorithm combining these two approaches was implemented to approximate eigenvalues for both ground and excited states $^{121}$ . Both ground and excited states are experimentally found with fidelities  $>99\%$ , and their eigenvalues are estimated with 32 bits of precision. Moreover, a modification of Boson sampling allows molecular vibronic spectra to be calculated with the inclusion of squeezed photons $^{122}$ , and an alternative scheme was proposed and realized in an universal linear-optic device (Fig. 5f) $^{88}$ . The Gaussian Boson sampling was also implemented to calculate molecular vibronic spectra of a synthetic molecule in ref. $^{104}$ . The question is how can underpinning models of the simulated systems be validated? Using a quantum Hamiltonian learning method, the fidelity of the simulation to the actual physical system can be measured by the consistency of the predictions with the obtained data. This algorithm was verified in a Si photonic simulator that can simulate the dynamics of an electron spin in a diamond nitrogen-vacancy centre (Fig. 5g) $^{123}$ .

# Challenges and outlook

Silicon photonics has been an exceptional IQP platform for quantum applications. In Fig. 6, we summarize the scaling of integrated quantum photonic components in silicon: from a single multimode interferometer (MMI) adopted for the first on-chip HOM interference experiment in  $2012^{24}$ , to a state-of-the-art large-scale quantum device with 671 optical components that was used for the GMM of multidimensional entanglement $^{44}$ . The information processing

capability has been significantly enhanced through such complex quantum devices. We anticipate that very-large-scale integration of quantum photonic circuitry containing millions of components is possible. Our optimism comes from the fact that manufacturing wafer-scale photonic circuits in silicon is compatible with 'near-zero change' of the current CMOS fabrication process. An important example is a recent demonstration of an ultralarge-scale integration of 57,600 photonic switches in a  $4 \times 4 \mathrm{~cm}^2$  Si chip, realized by our classical photonics colleagues $^{124}$ .

A state-of-the-art IQP device capable of generating and processing up to eight photons has been recently demonstrated in Si photonics[104]. In the near term, processing a large number of single photons will probably rely on the continued development of multiplexed parametric  $\mathrm{SPSs}^{52,53}$  and de-multiplexed QD  $\mathrm{SPSs}^{59,60}$ . Both approaches require a network of fast, low-loss optical switches. Recent progress in  $\mathrm{LN}^{125}$ ,  $\mathrm{Si - LN}^{126}$  and Si-barium titanate[127] switches have shown great promise for advanced switching technologies suitable for multiplexed or de-multiplexed many-photon generation. These advanced systems also promise fast manipulation of quantum light for information processing and transcieving in quantum communications systems. In general, low-loss waveguide circuits and platforms are key in quantum photonic applications, such as high-key-rate QKD, high-rate Boson sampling, efficient generation of cluster states and fault-tolerant quantum computation. Ultralow-loss waveguides have been manufactured in a range of platforms, for example,  $2.6\mathrm{dBm}^{-1}$  in Si (ref. [128]),  $2.3 - 2.7\mathrm{dBm}^{-1}$  in  $\mathrm{LN}^{129,130}$ ,  $0.1\mathrm{dBm}^{-1}$  in  $\mathrm{Si}_3\mathrm{N}_4$  (ref. [131]) and  $0.08\mathrm{dBm}^{-1}$  in  $\mathrm{SiO}_2$  (ref. [132]).

Moreover, fully integrated quantum chips with sources, circuits and detectors are yet to be realized. Much effort is focused on achieving this goal, with demonstrations of quantum circuits integrated with SNSPDs (Fig. 2j) $^{31,64}$ , and photon sources integrated with SNSPDs (Fig. 2h) $^{133,134}$ . A few existing technical challenges still need to be tackled towards full integration, such as photon manipulation at cryogenic temperatures and removal of the bright excitation light used to pump the photon sources. Cascaded mircorings $^{135}$  and MZIs $^{136}$  have achieved  $100~\mathrm{dB}$  rejection and are a promising approach towards achieving the latter challenge, and recent demonstrations of cryogenic operation of Si-barium titanate $^{137}$  optical switches are a potential approach for the former challenge.

Quantum interference with near unity visibility $^{25}$  and qubit operation with extremely low error $^{47}$  have been demonstrated. The question is how to further improve the performance for MBQC, and how to overcome the fabrication error and variability when scaling to the wafer scale. High programmability of the IQP hardware together with classical machine-learning algorithms may provide a solution that allows the compensation of fabrication imperfections, such as imperfect cross-section or waveguide non-uniformity $^{138}$ . Similar techniques could be adopted for the efficient characterization $^{123}$  and control $^{139}$  of large-scale photonic devices. In addition, machine-learning approaches could enhance the performance of quantum machines such as noise and error resistances $^{120}$ , which promises near-term, pre-fault-tolerant quantum computing and information processing $^{140}$ .

In the past decade, integrated quantum photonics has rapidly matured to become a versatile platform that is proving invaluable in the development of future quantum technologies and applications. We anticipate that over the next decade, very-large-scale integrated photonics devices and systems will be developed to enable revolutionary new applications in quantum communications, quantum information processing and quantum simulation with many photons.

Received: 10 May 2019; Accepted: 29 August 2019; Published online: 21 October 2019

# References

1. Freedman, S. J. & Clauser, J. F. Experimental test of local hidden-variable theories. Phys. Rev. Lett. 28, 938-941 (1972).  
2. Wu, L.-A., Kimble, H. J., Hall, J. L. & Wu, H. Generation of squeezed states by parametric down conversion. Phys. Rev. Lett. 57, 2520-2523 (1986).  
3. Bouwmeester, D. et al. Experimental quantum teleportation. Nature 390, 575-579 (1997).  
4. Shalm, L. K. et al. Strong loophole-free test of local realism. Phys. Rev. Lett. 115, 250402 (2015).  
5. Gisin, N., Ribordy, G., Tittel, W. & Zbinden, H. Quantum cryptography. Rev. Mod. Phys. 74, 145-195 (2002).  
6. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
7. Aspuru-Guzik, A. & Walther, P. Photonic quantum simulators. Nat. Phys. 8, 285-291 (2012).  
8. Awschalom, D. D., Hanson, R., Wrachtrup, J. & Zhou, B. B. Quantum technologies with optically interfaced solid-state spins. Nat. Photon. 12, 516-527 (2018).  
9. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2000).  
10. Gottesman, D. & Chuang, I. L. Demonstrating the viability of universal quantum computation using teleportation and single-qubit operations. Nature 402, 390-393 (1999).  
11. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
12. Nielsen, M. A. Optical quantum computation using cluster states. Phys. Rev. Lett. 93, 040503 (2004).  
13. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. In Proc. Forty-third Annual ACM Symposium on Theory of Computing 333-342 (Association for Computing Machinery, 2011).  
14. Politi, A., Cryan, M. J., rarity, J. G., Yu, S. & O'Brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
15. Zhong, H.-S. et al. 12-photon entanglement and scalable scattershot Boson sampling with optimal entangled-photon pairs from parametric downconversion. Phys. Rev. Lett. 121, 250505 (2018).  
16. Matthews, J. C. F., Politi, A., Andre, S. & O'Brien, J. L. Manipulation of multiphoton entanglement in waveguide quantum circuits. Nat. Photon. 3, 346-350 (2009).  
17. Shadbolt, P J. et al. Generating, manipulating and measuring entanglement and mixture with a reconfigurable photonic circuit. Nat. Photon. 6, 45-49 (2012).  
18. Laing, A. et al. High-fidelity operation of quantum photonic circuits. Appl. Phys. Lett. 97, 211109 (2010).  
19. Smith, B. J., Kundys, D., Thomas-Peter, N., Smith, P. G. R. & Walmsley, I. A. Phase-controlled integrated photonic quantum circuits. Opt. Express 17, 13516-13525 (2009).  
20. Corrielli, G. et al. Rotated waveplates in integrated waveguide optics. Nat. Commun. 5, 4249 (2014).  
21. Sansoni, L. et al. Polarization entangled state measurement on a chip. Phys. Rev. Lett. 105, 200503 (2010).  
22. Crespi, A. et al. Integrated photonic quantum gates for polarization qubits. Nat. Commun. 2, 566 (2011).  
23. Takesue, H. et al. Entanglement generation using silicon wire waveguide. Appl. Phys. Lett. 91, 201108 (2007).  
24. Bonneau, D. et al. Quantum interference and manipulation of entanglement in silicon wire waveguide quantum circuits. New J. Phys. 14, 045003 (2012).  
25. Silverstone, J. W. et al. On-chip quantum interference between silicon photon-pair sources. Nat. Photon. 8, 104-108 (2013).  
26. Zhang, M. et al. Generation of multiphoton quantum states on silicon. Light Sci. Appl. 8, 41 (2019).  
27. Pernice, W. H. P. et al. High-speed and high-efficiency travelling wave single-photon detectors embedded in nanophotonic circuits. Nat. Commun. 3, 1325 (2012).  
28. Lu, X. et al. Chip-integrated visible-telecom entangled photon pair source for quantum communication. Nat. Phys. 15, 373-381 (2019).  
29. Zhang, X. et al. Integrated silicon nitride time-bin entanglement circuits. Opt. Lett. 43, 3469-3472 (2018).  
30. Dutt, A. et al. On-chip optical squeezing. Phys. Rev. Appl. 3, 044005 (2015).  
31. Schuck, C. et al. Quantum interference in heterogeneous superconducting-photonic circuits on a silicon chip. Nat. Commun. 7, 10352 (2016).  
32. Tanzilli, S. et al. PPLN waveguide for quantum communication. Eur. Phys. J. D 18, 155-160 (2002).  
33. Jin, H. et al. On-chip generation and manipulation of entangled photons based on reconfigurable lithium-niobate waveguide circuits. Phys. Rev. Lett. 113, 103601 (2014).  
34. Hopker, J. P. et al. Towards integrated superconducting detectors on lithium niobate waveguides. Preprint at https://arxiv.org/abs/1708.06232 (2017).  
35. Horn, R. et al. Monolithic source of photon pairs. Phys. Rev. Lett. 108, 153605 (2012).

36. Wang, J. et al. Gallium arsenide (GaAs) quantum photonic waveguide circuits. Opt. Commun. 327, 49-55 (2014).  
37. Sprengers, J. P. et al. Waveguide superconducting single photon detectors for integrated quantum photonic circuits. Appl. Phys. Lett. 99, 181110 (2011).  
38. Sibson, P. et al. Chip-based quantum key distribution. Nat. Commun. 8, 13984 (2017).  
39. Abellan, C. et al. Quantum entropy source on an InP photonic integrated circuit for random number generation. Optica 3, 989-994 (2016).  
40. Kues, M. et al. On-chip generation of high-dimensional entangled quantum states and their coherent control. Nature 546, 622-626 (2017).  
41. Santagati, R. et al. Silicon photonic processor of two-qubit entangling quantum logic. J. Opt. 19, 114006 (2017).  
42. Meany, T. et al. Laser written circuits for quantum photonics. *Laser Photon. Rev.* 9, 363-384 (2015).  
43. Matsuda, N. et al. A monolithically integrated polarization entangled photon pair source on a silicon chip. Sci. Rep. 2, 817 (2012).  
44. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
45. Feng, L.-T. et al. On-chip coherent conversion of photonic quantum entanglement between different degrees of freedom. Nat. Commun. 7, 11985 (2016).  
46. Mohanty, A. et al. Quantum interference between transverse spatial waveguide modes. Nat. Commun. 8, 14010 (2017).  
47. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photon. 11, 447-452 (2017).  
48. Rudolph, T. Why I am optimistic about the silicon-photonic route to quantum computing. APL Photon. 2, 030901 (2017).  
49. Engin, E. et al. Photon pair generation in a silicon micro-ring resonator with reverse bias enhancement. Opt. Express 21, 27826-27834 (2013).  
50. Spring, J. B. et al. Chip-based array of near-identical, pure, heralded single-photon sources. Optica 4, 90-96 (2017).  
51. Llewellyn, D. et al. Demonstration of chip-to-chip quantum teleportation. In Conference on Lasers Electro-Optics (CLEO) JTh5C.4 (Optical Society of America, 2019).  
52. Kaneda, F. & Kwiat, P. G. High-efficiency single-photon generation via large-scale active time multiplexing. Sci. Adv. 5, eaaw8586 (2019).  
53. Collins, M. J. et al. Integrated spatial multiplexing of heralded single-photon sources. Nat. Commun. 4, 2582 (2014).  
54. Senellart, P., Solomon, G. & White, A. High-performance semiconductor quantum-dot single-photon sources. Nat. Nanotechnol. 12, 1026-1039 (2017).  
55. He, Y.-M. et al. On-demand semiconductor single-photon source with near-unity indistinguishability. Nat. Nanotechnol. 8, 213-217 (2013).  
56. Ding, X. et al. On-demand single photons with high extraction efficiency and near-unity indistinguishability from a resonantly driven quantum dot in a micropillar. Phys. Rev. Lett. 116, 020401 (2016).  
57. Somaschi, N. et al. Near-optimal single-photon sources in the solid state. Nat. Photon. 10, 340-345 (2016).  
58. Arcari, M. et al. Near-unity coupling efficiency of a quantum emitter to a photonic crystal waveguide. Phys. Rev. Lett. 113, 093603 (2014).  
59. Lenzini, F. et al. Active demultiplexing of single photons from a solid-state source. *Laser. Rev.* **11**, 1600297 (2017).  
60. Wang, H. et al. High-efficiency multiphoton boson sampling. Nat. Photon. 11, 361-365 (2017).  
61. Wang, H. et al. Toward scalable boson sampling with photon loss. Phys. Rev. Lett. 120, 230502 (2018).  
62. Loredo, J. C. et al. Boson sampling with single-photon Fock states from a bright solid-state source. Phys. Rev. Lett. 118, 130503 (2017).  
63. Hadfield, R. H. Single-photon detectors for optical quantum information applications. Nat. Photon. 3, 696-705 (2009).  
64. Najafi, F. et al. On-chip detection of non-classical light by scalable integration of single-photon detectors. Nat. Commun. 6, 5873 (2015).  
65. Gerrits, T. et al. On-chip, photon-number-resolving, telecommunication-band detectors for scalable photonic information processing. Phys. Rev. A 84, 060301 (2011).  
66. Sahin, D. et al. Waveguide photon-number-resolving detectors for quantum photonic integrated circuits. Appl. Phys. Lett. 103, 111116 (2013).  
67. Martinez, N. J. D. et al. Single photon detection in a waveguide coupled Ge-on-Si lateral avalanche photodiode. Opt. Express 25, 16130-16139 (2017).  
68. Vines, P. et al. High performance planar germanium-on-silicon single-photon avalanche diode detectors. Nat. Commun. 10, 1086 (2019).  
69. Honjo, T., Inoue, K. & Takahashi, H. Differential-phase-shift quantum key distribution experiment with a planar light-wave circuit Mach-Zehnder interferometer. Opt. Lett. 29, 2797-2799 (2004).  
70. Ma, C. et al. Silicon photonic transmitter for polarization-encoded quantum key distribution. Optica 3, 1274-1278 (2016).

71. Sibson, P. et al. Integrated silicon photonics for high-speed quantum key distribution. Optica 4, 172-177 (2017).  
72. Bunandar, D. et al. Metropolitan quantum key distribution with silicon photonics. Phys. Rev. X 8, 021009 (2018).  
73. Thompson, M. G. Large-scale integrated quantum photonic technologies for communications and computation. In Optical Fiber Communication Conference (OFC) W3D.3 (Optical Society of America, 2019).  
74. Ding, Y. et al. High-dimensional quantum key distribution based on multicore fiber using silicon photonic integrated circuits. npj Quantum Inf. 3, 25 (2017).  
75. Semenenko, H., Sibson, P., Thompson, M. G. & Erven, C. Interference between independent photonic integrated devices for quantum key distribution. Opt. Lett. 44, 275-278 (2019).  
76. Agnesi, C. et al. Hong-Ou-Mandel interference between independent III-V on silicon waveguide integrated lasers. Opt. Lett. 44, 271-274 (2019).  
77. Autebert, C. et al. Integrated AlGaAs source of highly indistinguishable and energy-time entangled photons. Optica 3, 143-146 (2016).  
78. Grassani, D. et al. Micrometer-scale integrated silicon source of time-energy entangled photons. Optica 2, 88-94 (2015).  
79. Wang, J. et al. Chip-to-chip quantum photonic interconnect by path-polarization interconversion. Optica 3, 407-413 (2016).  
80. Roger, T. et al. Real-time interferometric quantum random number generation on chip. J. Opt. Soc. Am. B 36, B137-B142 (2019).  
81. Raffaelli, F. et al. A homodyne detector integrated onto a photonic chip for measuring quantum states and generating random numbers. Quantum Sci. Technol. 3, 025003 (2018).  
82. Politi, A., Matthews, J. C. F. & O'Brien, J. L. Shor's quantum factoring algorithm on a photonic chip. Science 325, 1221 (2009).  
83. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
84. Metcalf, B. J. et al. Quantum teleportation on a photonic chip. Nat. Photon. 8, 770-774 (2014).  
85. Peruzzo, A. et al. A variational eigenvalue solver on a photonic quantum processor. Nat. Commun. 5, 4213 (2013).  
86. Flamini, F. et al. Thermally reconfigurable quantum photonic circuits at telecom wavelength by femtosecond laser micromachining. Light Sci. Appl. 4, e354 (2015).  
87. Qiang, X. et al. Large-scale silicon quantum photonics implementing arbitrary two-qubit processing. Nat. Photon. 12, 534-539 (2018).  
88. Sparrow, C. et al. Simulating the vibrational quantum dynamics of molecules using photonics. Nature 557, 660-667 (2018).  
89. Taballione, C. et al. 8x8 reconfigurable quantum photonic processor based on silicon nitride waveguides. Opt. Express 19, 26842-26857 (2019).  
90. Silverstone, J. W. et al. Qubit entanglement between ring-resonator photon-pair sources on a silicon chip. Nat. Commun. 6, 7948 (2015).  
91. Ciampini, M. A. et al. Path-polarization hyperentangled and cluster states of photons on a chip. Light Sci. Appl. 5, e16064 (2016).  
92. Reimer, C. et al. High-dimensional one-way quantum processing implemented on  $d$ -level cluster states. Nat. Phys. 15, 148-153 (2019).  
93. Adcock, J. C., Vigliar, C., Santagati, R., Silverstone, J. W. & Thompson, M. G. Programmable four-photon graph states on a silicon chip. Nat. Commun. 10, 3528 (2019).  
94. Harrow, A. W. & Montanaro, A. Quantum computational supremacy. Nature 549, 203-209 (2017).  
95. Spagnolo, N. et al. Three-photon bosonic coalescence in an integrated titter. Nat. Commun. 4, 1606 (2013).  
96. Metcalf, B. J. et al. Multiphoton quantum interference in a multiport integrated photonic device. Nat. Commun. 4, 1356 (2013).  
97. Crespi, A. et al. Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nat. Photon. 7, 545-549 (2013)  
98. Tillmann, M. et al. Experimental boson sampling. Nat. Photon. 7, 540-544 (2013).  
99. Spring, J. B. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2013).  
100. Carolan, J. et al. On the experimental verification of quantum complexity in linear optics. Nat. Photon. 8, 621-626 (2014).  
101. Broome, M. A. et al. Photonic boson sampling in a tunable circuit. Science 339, 794-798 (2013).  
102. Tillmann, M. et al. Generalized multiphoton quantum interference. Phys. Rev. X 5, 041015 (2015).  
103. Bentivegna, M. et al. Experimental scattershot boson sampling. Sci. Adv. 1, e1400255 (2015).  
104. Paesani, S. et al. Generation and sampling of quantum states of light in a silicon chip. Nat. Phys. 15, 925-929 (2019).  
105. Zhong, H.-S. et al. Experimental Gaussian Boson sampling. Sci. Bull. 64, 511-515 (2019).  
106. Aaronson, S. & Arkhipov, A. Boson sampling is far from uniform. Quantum Inf. Comput. 14, 1383-1423 (2014).  
107. Spagnolo, N. et al. Experimental validation of photonic boson sampling. Nat. Photon. 8, 615-620 (2014).

108. Giordani, T. et al. Experimental statistical signature of many-body quantum interference. Nat. Photon. 12, 173-178 (2018).  
109. Agresti, I. et al. Pattern recognition techniques for Boson sampling validation. Phys. Rev. X 9, 011013 (2019).  
110. Neville, A. et al. Classical boson sampling algorithms with superior performance to near-term experiments. Nat. Phys. 13, 1153-1157 (2017).  
111. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
112. Crespi, A. et al. Anderson localization of entangled photons in an integrated quantum walk. Nat. Photon. 7, 322-328 (2013).  
113. Pitsios, I. et al. Photonic simulation of entanglement growth and engineering after a spin chain quench. Nat. Commun. 8, 1569 (2017).  
114. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500-1503 (2010).  
115. Crespi, A. et al. Particle statistics affects quantum decay and Fano interference. Phys. Rev. Lett. 114, 090201 (2015).  
116. Caruso, F., Crespi, A., Ciriolo, A. G., Sciarrino, F. & Osellame, R. Fast escape of a quantum walker from an integrated photonic maze. Nat. Commun. 7, 1682 (2016).  
117. Biggerstaff, D. N. et al. Enhancing coherent transport in a photonic network using controllable decoherence. Nat. Commun. 7, 11282 (2016).  
118. Tang, H. et al. Experimental quantum fast hitting on hexagonal graphs. Nat. Photon. 12, 754-758 (2018).  
119. Poulios, K. et al. Quantum walks of correlated photon pairs in two-dimensional waveguide arrays. Phys. Rev. Lett. 112, 143604 (2014).  
120. Paesani, S. et al. Experimental Bayesian quantum phase estimation on a silicon photonic chip. Phys. Rev. Lett. 118, 100503 (2017).  
121. Santagati, R. et al. Witnessing eigenstates for quantum simulation of Hamiltonian spectra. Sci. Adv. 4, eaap9646 (2018).  
122. Huh, J., Guerreschi, G. G., Peropadre, B., McClean, J. R. & Aspuru-Guzik, A. Boson sampling for molecular vibronic spectra. Nat. Photon. 9, 615-620 (2015).  
123. Wang, J. et al. Experimental quantum Hamiltonian learning. Nat. Phys. 13, 551-555 (2017).  
124. Seok, T. J., Kwon, K., Henriksson, J., Luo, J. & Wu, M. C.  $240 \times 240$  wafer-scale silicon photonic switches. In Optical Fiber Communication Conference (OFC) 2019 Th1E.5 (Optical Society of America, 2019).  
125. Wang, C. et al. Integrated lithium niobate electro-optic modulators operating at CMOS-compatible voltages. Nature 562, 101-104 (2018).  
126. He, M. et al. High-performance hybrid silicon and lithium niobite Mach-Zehnder modulators for 100 Gbit s $^{-1}$  and beyond. Nat. Photon. 13, 359-364 (2019).  
127. Abel, S. et al. Large Pockels effect in micro- and nanostructured barium titanate integrated on silicon. Nat. Mater. 18, 42-47 (2019).  
128. Li, G. et al. Ultralow-loss, high-density SOI optical waveguide routing for macrochip interconnects. Opt. Express 20, 12035-12039 (2012).  
129. Zhang, M., Wang, C., Cheng, R., Shams-Ansari, A. & Loncar, M. Monolithic ultra-high-  $Q$  lithium niobate microring resonator. Optica 4, 1536-1537 (2017).

130. Wu, R. et al. Long low-loss-lithium niobate on insulator waveguides with sub-nanometer surface roughness. *Nanomaterials* 8, 910 (2018).  
131. Bauters, J. F. et al. Planar waveguides with less than  $0.1\mathrm{dB / m}$  propagation loss fabricated with wafer bonding. Opt. Express 19, 24090-24101 (2011).  
132. Lee, H., Chen, T., Li, J., Painter, O. & Vahala, K. J. Ultra-low-loss optical delay line on a silicon chip. Nat. Commun. 3, 867 (2012).  
133. Digeronimo, G. E. et al. Integration of single-photon sources and detectors on GaAs. Photonics 3, 55 (2016).  
134. Khasminskaya, S. et al. Fully integrated quantum photonic circuit with an electrically driven light source. Nat. Photon. 10, 727-732 (2016).  
135. Ong, J., Kumar, R. & Mookherjea, S. Ultra-high-contrast and tunable-bandwidth filter using cascaded high-order silicon microring filters. IEEE Photon. Technol. Lett. 25, 1543-1546 (2013).  
136. Piekarek, M. et al. High-extinction ratio integrated photonic filters for silicon quantum photonics. Opt. Lett. 42, 815-818 (2017).  
137. Eltes, F. et al. An integrated cryogenic optical modulator. Preprint at https://arxiv.org/abs/1904.10902 (2019).  
138. Miller, D. A. B. Perfect optics with imperfect components. Optica 2, 747-750 (2015).  
139. Carolan, J. et al. Scalable feedback control of single photon sources for photonic quantum technologies. Optica 6, 335-340 (2019).  
140. Biamonte, J. et al. Quantum machine learning. Nature 549, 195-202 (2017).

# Acknowledgements

We thank C.-Y. Lu for discussions on quantum dot sources and J. Bulmer for discussions on photonic quantum information processing. J.W. acknowledges support from the Natural Science Foundation of China (61975001), National Key Research & Development (R&D) Program of China (2018YFB1107205), Beijing Natural Science Foundation (Z190005), Beijing Academy of Quantum Information Sciences (Y18G21) and the Key R&D Program of Guangdong Province (2018B030329001). F.S. acknowledges support from the H2020-FETPROACT-2014 Grant QUCHIP (Quantum Simulation on a Photonic Chip; grant agreement no. 641039). A.L. acknowledges support from an EPSRC (Engineering and Physical Sciences Research Council) Early Career Fellowship EP/N003470/1. M.G.T. acknowledges support from an ERC (European Research Council) starter grant (ERC-2014-STG 640079) and an EPSRC Early Career Fellowship (EP/K033085/1).

# Competing interests

M.T. is involved in developing quantum photonic technologies at PsiQuantum Corporation.

# Additional information

Correspondence should be addressed to M.G.T.

Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

$\odot$  Springer Nature Limited 2019