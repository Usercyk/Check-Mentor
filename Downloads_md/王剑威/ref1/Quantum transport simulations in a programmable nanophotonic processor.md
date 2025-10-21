# Quantum transport simulations in a programmable nanophotonic processor

Nicholas C. Harris $^{1\star}$ , Gregory R. Steinbrecher $^{1}$ , Mihika Prabhu $^{1}$ , Yoav Lahini $^{2}$ , Jacob Mower $^{1}$ , Darius Bunandar $^{3}$ , Changchen Chen $^{4}$ , Franco N. C. Wong $^{4}$ , Tom Baehr-Jones $^{5}$ , Michael Hochberg $^{5}$ , Seth Lloyd $^{6}$  and Dirk Englund $^{1}$

Environmental noise and disorder play critical roles in quantum particle and wave transport in complex media, including solid-state and biological systems. While separately both effects are known to reduce transport, recent work predicts that in a limited region of parameter space, noise-induced dephasing can counteract localization effects, leading to enhanced quantum transport. Photonic integrated circuits are promising platforms for studying such effects, with a central goal of developing large systems providing low-loss, high-fidelity control over all parameters of the transport problem. Here, we fully map the role of disorder in quantum transport using a nanophotonic processor: a mesh of 88 generalized beamsplitters programmable on microsecond timescales. Over 64,400 experiments we observe distinct transport regimes, including environment-assisted quantum transport and the 'quantum Goldilocks' regime in statically disordered discrete-time systems. Low-loss and high-fidelity programmable transformations make this nanophotonic processor a promising platform for many-boson quantum simulation experiments.

Quantum walks (QWs), the coherent analogue of classical random walks, have emerged as useful models for experimental simulations of quantum transport (QT) phenomena in physical systems. QT experiments have been implemented in various platforms, including trapped ions $^{1,2}$ , ultracold atoms $^{3}$ , bulk optics $^{4-7}$ , integrated photonics $^{4,8-15}$ , multimode fibres $^{16}$  and scattering media $^{17}$ . Integrated photonic implementations in silicon are particularly attractive for high interferometric visibilities, phase stability, integration with single-photon sources $^{18-20}$  and detectors $^{21}$  and the promise of scaling to many active and reconfigurable components. The role of static and dynamic disorder in the transport of coherent particles has been of particular interest in the field of quantum simulation $^{22,23}$ .

Control over static (time-invariant) and dynamic (time-varying) disorder enables studies of fundamentally interesting and potentially useful quantum transport phenomena. In systems with strong dynamic disorder, a coherent particle evolving over  $T$  time steps travels a distance proportional to  $\sqrt{T}$ ; the coherent nature of the particle is effectively erased, resulting in classical, diffusive transport characteristics[24,25]. In contrast, a coherent particle (or wave) traversing an ordered system travels a distance proportional to  $T$  as a result of coherent interference between superposition amplitudes—a regime known as ballistic transport. Perhaps most notably, a coherent particle propagating through a system with strong, static disorder becomes exponentially localized in space, inhibiting transport. This phenomenon—Anderson localization[26] has been observed in several systems, including optical media[8-10,27,28]. For systems in which transport has been arrested due to Anderson localization, it has recently been predicted that adding environmental noise (dynamic disorder) over a finite range of strengths could result in enhanced transport. This

effect, known as environment-assisted quantum transport (ENAQT), is believed to play a key role in the high transport efficiencies in photosynthetic complexes $^{29,30}$ , as depicted in Fig. 1f. With such a variety of QT phenomena accessible, it is of fundamental interest to develop systems capable of fully probing the disorder space, potentially revealing new QT phenomena in the single- and multiparticle regimes.

In integrated photonic systems, static and dynamic disorder have been introduced by fabricating circuits with random parameter variations or post-processing $^{8,10}$ , rendering explorations of large parameter spaces in QT simulations possible, but cumbersome. Furthermore, single instances of disorder are not suitable for characterizing transport, as they can produce a wide range of output distributions $^{9}$ , and ensemble averages over many instances are necessary to accurately reproduce output statistics. Static and dynamic disorder have been studied separately $^{4,8-11,24}$ , but transport in a system capable of implementing both simultaneously—a requirement for the observation of ENAQT—in all combinations and strengths, with low loss and over a large number of instances, has not been demonstrated. Developing systems capable of meeting these requirements and the more stringent requirement of generating arbitrary single-particle unitary operations $^{31}$  has been the topic of several recent theoretical investigations $^{32,33}$ .

Here, we introduce a programmable nanophotonic processor (PNP), shown schematically in Fig. 1a, to explore the interaction between a particle undergoing quantum transport (on the graph depicted in Fig. 1b) and two kinds of noise: static and dynamic disorder. Over a set of 64,400 experiments, we observe a number of hallmark quantum transport regimes, including the signature of ENAQT in discrete-time systems and the 'quantum Goldilocks' regime<sup>34</sup>. The generality of the PNP Hamiltonian unlocks further

![](images/b19377920fce8658493ecc982da5ebaa84de09d06c6a11b85799da5a115f0e93.jpg)

![](images/e7eb61407f4bb3129439816eb1c5f8e3488cf9aed5b156609106c94fd51cef66.jpg)

![](images/b3f8588b74b095308af08015801bcbb1f8bc7767bcc743e2ffe499d9976db2e0.jpg)  
Figure 1 | A quantum transport simulator. a, Schematic of programmable nanophotonic processor. Dark lines are silicon nanowire waveguides; circles are programmable MZIs. Inset: thermal phase modulators control the splitting ratio and differential output phase. Time  $(\tau)$  is defined from left to right. Space  $(i)$  is defined from top to bottom. b,c, Example graphs implementable with the processor's Hamiltonian (labelled dark circles represent waveguide positions or nodes): nearest-neighbour graph implemented in this work (b), where the coupling between waveguides depends on whether the time step is even or odd; binary tree graph allowed by the processor Hamiltonian (c). d, Dynamic disorder is implemented by choosing  $\{\phi_i\}$  such that there are no spatiotemporal correlations. Disorder strength is described via the  $c_{d}$  parameter. e, Static disorder is implemented by choosing  $\{\phi_i\}$  to be constant in time, but uncorrelated in space. f, Arrested transport of a quantum particles in strong, statically disordered system to external sites can be optimized by introducing dynamic disorder.

![](images/67f8f85d2941925ddd52ec989909cfae5eeac79ffe052bc3fa6d5147756ab896.jpg)

![](images/a0c04def96c4b5ea1de2980d367653626024a831de705fd3af5910112060b322.jpg)

exploration into quantum transport on a large set of graphs including binary trees (Fig. 1c) and graphs that exhibit topological order<sup>6</sup>.

Previous photonic integrated circuits for quantum information processing have been limited to 30 individually tunable elements and 15 interferometers[35]. The present PNP is composed of 176 individually tunable phase modulators and 88 interferometers spanning a chip area of  $4.9\mathrm{mm}\times 2.4\mathrm{mm}$ . This high component density is enabled by a high silicon-to-silica index contrast, enabling the fabrication of waveguides with less than  $15\mu \mathrm{m}$  bend radius (used here) and the large thermo-optic coefficient of silicon (enabling compact phase modulators[36]).

Recent work suggests that even sampling the output distributions from linear unitary processes, including QWs, with a relatively small numbers of photons ( $n > 30$  for a circuit with  $\sim 1,000$  modes) becomes intractable for classical computers[37-39]. Furthermore, QWs augmented with feedforward control[40-42] have been proposed for universal quantum computation schemes[43].

# PNP

The PNP, shown in Fig. 2a, consists of a mesh of reconfigurable beamsplitters (RBSs, highlighted in white). Each RBS is composed of two  $50\%$  directional couplers separated by an internal  $(\theta)$  and an external  $(\phi)$  thermo-optic phase shifter[36], as shown in Fig. 2b. The RBS applies the rotation

$$
\hat {U} _ {R B S} = \left[ \begin{array}{c c} e ^ {i \phi} \sin (\theta / 2) & e ^ {i \phi} \cos (\theta / 2) \\ \cos (\theta / 2) & - \sin (\theta / 2) \end{array} \right]
$$

in the spatial-mode basis. Each RBS can implement any rotation in  $SU(2)$  by using its internal and external phase shifter and the output phase shifter of the preceding RBS; for the input RBSs in the PNP, all of the  $SU(2)$  can be accessed by choosing an input phase.

Silicon waveguides in the PNP are inverse-tapered to a mode-field diameter of  $2\mu \mathrm{m}$  with a mode spacing of  $25.4\mu \mathrm{m}$ . The 52 modes of the PNP are coupled to optical fibres using two laser-written glass photonic integrated circuits as indicated in Fig. 2c (Supplementary Section 1). Mode-field diameter mismatch between the glass chips and the PNP, and fibre connectorization, result in a transmission loss of  $3.5\mathrm{dB}$  per facet. The total loss through the PNP, including both input and output coupling, is  $8\mathrm{dB}$ . Accounting for the coupling losses of  $3.5\mathrm{dB}$  per facet, the PNP transmission is  $80\%$ . This matches the expected propagation loss for our silicon nanowire waveguides[44].

Each of the 176 phase shifters can impart a phase shift of more than  $2\pi$  radians, as shown in Fig. 2c. An automated voltage scan of all 88 RBSs, without active polarization monitoring and control, gives a mean extinction ratio of  $0.9996 \pm 0.0005$ . Figure 2d shows an extinction ratio of  $0.9999998 \pm 1.3 \times 10^{-8}$  ( $\sim 66.3$  dB) for a single RBS measured when the transverse electric waveguide mode is selected using polarization filters and active polarization control, as discussed in Supplementary Section 3. To the best of our knowledge, our RBS visibility is the highest reported in literature[48]. Nearest-neighbour thermal crosstalk between adjacent phase shifters was measured to be  $1\%$ . We corrected for this by performing a linear matrix inversion for each

![](images/682f60a7fe4aa078bde0e86956a49e18535aea72bfe9fc4fa634a43359ce07ec.jpg)  
Figure 2 | Programmable nanophotonic processor. a, Processor composed of 88 MZIs, 26 input modes, 26 output modes and 176 phase shifters; gold wirebond filaments are visible. b, Zoom in of the white inset in a, showing individual interferometer and thermo-optic phase shifters  $(\theta, \phi)$ . c, Phase versus voltage curve for all internal and external phase shifters on the chip. d, Transmission spectrum for an MZI with careful input polarization filtering. The extinction ratio was measured to be  $0.9999998 \pm 1.3 \times 10^{-8}$ . e, Set-up used in this experiment. The processor accepts only transverse-electric polarized light, requiring a bank of polarization rotators to couple to the chip modes. Polarization rotator fibres are connected to the input glass photonic integrated circuit, which serves as both a waveguide pitch reducer and as a spot-size converter. The output of the PNP is sent to an array of detectors and read out using a microcontroller. The processor is electronically programmed using a 240-channel biasing system and operated using a microcontroller. f, Nonlinear optimization protocol used to generate the Massachusetts Institute of Technology logo shown in g, across the 26 output modes of the processor  $|\psi(i,11)|^2$ .

program. The thermo-optic modulators have a 3 dB bandwidth of  $130.0 \pm 5.59\mathrm{kHz}$  (ref. 36), corresponding to a limit of  $1 \times 10^{5}$  full PNP reconfigurations per second.

The PNP was fabricated in a complementary metal-oxide semiconductor (CMOS)-compatible silicon photonics process (see Methods for more detail). After fabrication, we calibrated the PNP as described in Supplementary Section 4. To program all 176 phase shifters, we developed a 240-channel, 16-bit precision electronic biasing system. To measure the PNP output mode intensities, we developed a 32-channel detector array system with 18-bit readout precision. Supplementary Section 2 gives experimental set-up details. As a demonstration of the programmability of the PNP, we used a nonlinear optimization algorithm to learn the phase settings required to generate the Massachusetts Institutue of Technology (MIT) logo across the output modes of the PNP  $(|\psi(i,11)|^2)$  as shown in Fig. 2f,g (for details see Supplementary Section 7).

# Experiment

The PNP is described by the following interaction Hamiltonian:

$$
\hat {H} _ {\mathrm {i n t}} \propto \sum_ {i} \frac {i \theta_ {i} (\tau)}{2} \left(\hat {a} _ {i} \hat {a} _ {i + 1} ^ {\dagger} - \hat {a} _ {i + 1} \hat {a} _ {i} ^ {\dagger}\right) + \phi_ {i} (\tau) \hat {a} _ {i} ^ {\dagger} \hat {a} _ {i}
$$

where  $\hat{a}$  is the mode annihilation operator,  $\tau$  (from 1 to 11) is the MZI column number (or time step) and  $i$  (between 1 and 26) is

the waveguide number (Fig. 1a). This Hamiltonian enables simulations of transport on a range of graphs including binary trees such as the one in Fig. 1c, as originally considered by Rebentrost and co-authors $^{29}$ . Here, we will explore the case  $\theta_{i}(\tau) = \pi /2$  (equal coupling between sites). The graph implemented by these settings is shown in Fig. 1b. To realize transport distributions that are symmetric about the initial site at  $i = 14$ , we program  $\phi_{14}(1)$  to  $\pi /2$  (ref. 45). To pause the evolution of the particle at some time step  $\tau_0$ , we can set  $\theta_{i}(\tau >\tau_{0}) = \pi$ .

As illustrated in Fig. 1d, dynamic disorder is added to the system by sampling  $\phi_i(\tau)$  (for all  $i$  and  $\tau$ ) from the uniform distribution  $(\mathcal{U})$  with minimum and maximum values of  $-\pi$  and  $\pi$ , respectively. This disorder results in a particle phase evolution that is uncorrelated in both position and time. Static disorder, illustrated in Fig. 1e, is added to the system by sampling  $\phi_i$  (for all  $i$ ) from  $\mathcal{U}$  with minimum and maximum values of  $-\pi$  and  $\pi$ , respectively. This results in a particle phase evolution that is uncorrelated in space, but constant in time. We use the distribution weighting parameter  $c_{\mathrm{s}}(c_{\mathrm{d}})$ , with support on the interval [0, 1], to control the strength of static (dynamic) disorder. We define the disorder coordinates as  $(c_{\mathrm{d}}, c_{\mathrm{s}})$ .

Mapping the environmental interaction space. It is important to note that these photonic simulations of environmental noise produce deterministic output distributions. By generating many systems described by the same disorder coordinate, general

![](images/57e99cc1af88eb251b6ddffed102df6c677887a2313d2fe374b2b09c5e9faf21.jpg)  
a

![](images/4ab90207dd09998be3c0a36e986ce841c818c351d99db63f6316b89784e28de0.jpg)  
b  
c

![](images/32eba8e4e3a4ff636cc41c13286397b9ee089465d64a5a19288078a7a272a609.jpg)

![](images/2c372b7ea127d8f360a45dcdd33d15291ca5f622846bfc03bfcd4d660ce7b053.jpg)  
d  
Figure 3 | Convergence and the full noisy transport space. a, Programming routine for transport experiments. PNP is initialized, environmental noise is introduced, and the output distribution is measured. This process is repeated  $N$  times to develop robust statistics. b, A measurement of a single instance of disorder coordinate (0,1). With one instance, it is difficult to determine what disorder coordinate could have generated this distribution. c, Convergence of the mean output distribution with iteration number.  $N \geq 10$  is necessary to achieve a fidelity  $f$  exceeding  $98\%$ . d,  $\langle |\psi(i,11)|^2\rangle$  for 400 combinations of  $(c_d, c_s)$  with both disorder coordinates varying on [0,1]. Modes labelled  $i = 7 \rightarrow 20$  are shown;  $i < 7$  and  $i > 20$  are relatively constant for all levels of disorder, as predicted via simulation. The mean fidelity for all modes and all disorder coordinates is  $99.8 \pm 0.036\%$ . Particle-like, incoherent transport occurs on the right edge of these plots. Coherent, ballistic transport occurs in the bottom left corner. e-g. Measurements of  $\langle |\psi(i,11)|^2\rangle_{N=100}$  at disorder coordinates (0,0), (1,1) and (0,1). Fits to the Laplace and Gaussian distributions are shown in red in f and g, respectively.

transport behaviour for a system described by this coordinate can be simulated. As shown in Fig. 3a, we performed a single QT experiment by (1) initializing the PNP to  $\theta_{i}(\tau) = \pi /2$  and  $\phi_{14}(1) = \pi /2$ , (2) programming a single instance  $n$  of a given disorder coordinate and (3) making a measurement of the output distribution  $|\psi_n(i,\tau)|^2$  and then normalizing this distribution to sum to one (see Methods). To illustrate the need for averaging over many instances, we measured  $|\psi_n(i,\tau)|^2$  for one instance of a disordered system described by (0,1), as shown in Fig. 3b. With only a single instance, it is unclear what disorder coordinate could have generated this distribution or even whether the particle undergoing transport is coherent.

To benchmark the number of instances required for convergence of the mean distribution

$$
\left\langle \left| \psi (i, 1 1) \right| ^ {2} \right\rangle = \frac {1}{N} \sum_ {n} \left| \psi_ {n} (i, 1 1) \right| ^ {2}
$$

over a number of instances  $N$ , we program the PNP to implement systems with disorder coordinates  $(0, 0.6)$ ,  $(1.0, 1.0)$  and  $(0, 1.0)$  and measure output distributions for  $N = 10^{2}$  instances of each coordinate (see Supplementary Section 5 for measurements at each  $\tau$ ). Next, we use a computer to simulate the same coordinates with  $N = 2 \times 10^{4}$  instances—we call this the 'asymptotic distribution'.

For each  $n \leq N$ , we compare the fidelity (see Methods for the fidelity metric) of  $\langle \psi(i,11)|^2\rangle$  up to the  $n$ th measurement against the asymptotic distribution. The data are plotted in Fig. 3c.  $N \geq 10$  instances are required to converge to the asymptotic distribution with a fidelity exceeding  $98\%$ , and we use  $N \geq 10^2$  for all experiments.

To probe whether ENAQT can be observed in discrete-time systems, we measure 400 disorder coordinates with  $c_{\mathrm{d}}$  and  $c_{\mathrm{s}}$  each spanning all strengths from 0 to 1 in increments of 0.05 and  $N = 100$ , totalling  $4 \times 10^{4}$  experiments. The ensemble average probability distributions at the output of the PNP for modes 7-20 are plotted in Fig. 3d; modes 1-6 and 21-26 are not plotted, because transport to these extremal modes is nearly uniform for all disorder levels, as predicted by simulation. The measured data in Fig. 3 are in excellent agreement with simulation, as shown in Table 1. This highlights one of the key benefits of the PNP:

Table1 | Fidelities for experimental data shown in Fig. 3.  

<table><tr><td></td><td>Fidelity</td><td>Uncertainty</td></tr><tr><td>Fig. 3b</td><td>0.9990</td><td>±0.0024</td></tr><tr><td>Fig. 3d</td><td>0.9976</td><td>±0.0004</td></tr><tr><td>Fig. 3e</td><td>0.9988</td><td>±0.0030</td></tr><tr><td>Fig. 3f</td><td>0.9987</td><td>±0.0035</td></tr><tr><td>Fig. 3g</td><td>0.9989</td><td>±0.0035</td></tr></table>

![](images/5ba83f60879d388524211cafefbf81561e21fd4a203642eb87288d80876ceb6e.jpg)  
a

![](images/56fbd3ac16db3a931cc112790a5209a76665585c81d48c1d3f60085ac1397772.jpg)  
Figure 4 | Environment-assisted quantum transport and the Goldilocks regime. a, Conceptual drawing of the phase landscape for a strong, statically disordered system where particle is localized to initial site at  $i_{14}$ . By adding dynamic disorder (shown as red vibrations), it is possible to optimize transport of the particle to sites further away. b, Slice through  $c_{\mathrm{s}} = 0.6$  and all  $c_{\mathrm{d}}$ , corresponding to a randomized phase span of  $1.2\pi$ . The  $y$  axis represents quantum transport efficiency  $\eta$  and the  $x$  axis is dynamic disorder strength. Red and blue lines are experimental data and simulation data for the phase configuration used in the experiment, respectively. The green line represents simulation with  $N = 2 \times 10^{4}$  —the asymptotic distribution. These data show environment-assisted quantum transport in a discrete-time system. Standard errors are plotted as a transparent band around the mean.

it can be calibrated post fabrication to implement high-fidelity transformations without physical modification.

To gain intuition for the disorder space in Fig. 3d, we plotted  $\langle |\psi (i,11)|^2\rangle$  for disorder coordinates  $(0,0)$ ,  $(1,1)$  and  $(0,1)$  in Fig.  $3\mathrm{e - g}$ , respectively. The lower left coordinates in Fig. 3d correspond to ballistic transport (Fig. 3e), the right edge corresponds to diffusive, incoherent transport (Fig. 3f) and the upper left coordinates correspond to Anderson localization (Fig. 3g) (indicated by arrows).

Environment-assisted quantum transport. Of particular interest in these data is the behaviour of mode 18 in Fig. 3d. We examine a cross-section through  $c_{\mathrm{d}}$  between 0 and 1, with  $c_{\mathrm{s}} = 0.6$ , corresponding to a strong, statically disordered system with  $\phi_{i}$  sampled uniformly between  $\pm 0.6\pi$ . In this case, a coherent particle localized at the starting point  $i_{14}$  is able to escape its initial position through the introduction of dynamic disorder. This process is depicted schematically in Fig. 4a. The cut through this transport space is plotted in Fig. 4b. The experimental and simulated data are in close agreement, with a fidelity of  $0.9998 \pm 0.0157$ . The trend of increasing transport efficiency for  $c_{\mathrm{d}} < 0.4$  may lead one to expect that introducing further dynamic disorder would enhance transport to site  $i_{18}$ . The data indicate that this is not the case. Instead, there is a 'quantum Goldilocks' regime in which adding additional dynamic disorder inhibits transport. The maximum efficiency improvement gained through ENAQT in this system after 11 time steps  $(\Delta \eta = (\eta_{\max} - \eta_{\min}) / \eta_{\max})$  is measured to be  $42\%$ .

# Discussion

ENAQT occurs in (statically) disordered systems in which transport has been arrested due to Anderson localization. Through interactions with a fluctuating environment (simulated by dynamic disorder), the transport efficiency of the coherent particle may be enhanced. Rebentrost et al.[29] predicted the existence of such an effect in systems that evolve in continuous time. We have shown evidence for ENAQT on discrete-time graphs as well as a 'quantum Goldilocks'[34] regime in which there is an optimal transport efficiency for all levels of dynamic noise. We note that the general Hamiltonian of this processor enables a range of quantum transport experiments on a variety of graphs.

For multiphoton experiments, loss is important. Coupling loss in our set-up could be reduced to less than  $5\%$  using grating couplers[46]. With improved fabrication, waveguide losses can also be lowered considerably; indeed, values as low as  $0.3\mathrm{dBcm}^{-1}$  have been reported[47]. With these improvements, the transmission loss of a photonic system of the complexity used here could be reduced to  $9\%$  using current technology. In this demonstration, on-chip loss is dominated by scattering associated with waveguide roughness,

and reducing this loss will become increasingly important as the PNP architecture is scaled. To the best of our knowledge, our MZI visibility (over 66 dB) is the highest reported in the literature[48].

For these experiments, we modelled and calibrated the PNP to maximize fidelities for single-particle experiments, enabling future high-fidelity, multiphoton quantum transport experiments (see Supplementary Section 6 for two-photon quantum interference experiments using the PNP). Transport simulations exceeding several tens of photons[49] become intractable[37] for classical computers. Although we have demonstrated one-dimensional quantum transport here, it is possible to simulate unitary processes in higher dimensions (for example, two and three dimensions) by programming universal unitary circuits[35] into the PNP interferometer mesh. Entangled photon sources[19,36,50] and single-photon detectors[21,51] have recently been integrated into the silicon photonics platform, providing a path towards high-photon-number experiments. In addition, recently demonstrated low-latency superconducting logic devices[52] may provide fast on-chip feedforward operations on quantum optical states. Together with programmable nanophotonic processors, these chip-integrated technologies provide a promising platform for future quantum simulation and computing tasks.

# Methods

Methods and any associated references are available in the online version of the paper.

Received 21 March 2017; accepted 12 May 2017; published online 19 June 2017

# References

1. Schmitz, H. et al. Quantum walk of a trapped ion in phase space. Phys. Rev. Lett. 103, 090504 (2009).  
2. Zahringer, F. et al. Realization of a quantum walk with one and two trapped ions. Phys. Rev. Lett. 104, 100503 (2010).  
3. Preiss, P. M. et al. Strongly correlated quantum walks in optical lattices. Science 347, 1229-1233 (2015).  
4. Broome, M. A. et al. Discrete single-photon quantum walks with tunable decoherence. Phys. Rev. Lett. 104, 153602 (2010).  
5. Vozilik, J., Leon-Montiel, R. d. J. & Torres, J. P. Implementation of a spatial two-dimensional quantum random walk with tunable decoherence. Phys. Rev. A 86, 052327 (2012).  
6. Kitagawa, T. et al. Observation of topologically protected bound states in photonic quantum walks. Nat. Commun. 3, 882 (2012).  
7. Schreiber, A. et al. Photons walking the line: a quantum walk with adjustable coin operations. Phys. Rev. Lett. 104, 050502 (2010).  
8. Crespi, A. et al. Anderson localization of entangled photons in an integrated quantum walk. Nat. Photon. 7, 322-328 (2013).  
9. Schwartz, T., Bartal, G., Fishman, S. & Segev, M. Transport and Anderson localization in disordered two-dimensional photonic lattices. Nature 446, 52-55 (2007).

10. Lahini, Y. et al. Anderson localization and nonlinearity in one-dimensional disordered photonic lattices. Phys. Rev. Lett. 100, 013906 (2008).  
11. Schreiber, A. et al. Decoherence and disorder in quantum walks: from ballistic spread to localization. Phys. Rev. Lett. 106, 180403 (2011).  
12. Bromberg, Y., Lahini, Y., Morandotti, R. & Silberberg, Y. Quantum and classical correlations in waveguide lattices. Phys. Rev. Lett. 102, 253904 (2009).  
13. Peruzzo, A. et al. Quantum walks of correlated photons. Science 329, 1500-1503 (2010).  
14. Sansoni, L. et al. Two-particle bosonic-fermionic quantum walk via integrated photonics. Phys. Rev. Lett. 108, 010502 (2012).  
15. Liu, C. et al. Enhanced energy storage in chaotic optical resonators. Nat. Photon. 7, 473-478 (2013).  
16. Defienne, H., Barbieri, M., Walmsley, I. A., Smith, B. J. & Gigan, S. Two-photon quantum walk in a multimode fiber. Sci. Adv. 2, e1501054 (2016).  
17. Wolterink, T. A. et al. Programmable two-photon quantum interference in  $10^{3}$  channels in opaque scattering media. Phys. Rev. A 93, 053817 (2016).  
18. Harris, N. C. et al. Integrated source of spectrally filtered correlated photons for large-scale quantum photonic systems. Phys. Rev. X 4, 041047 (2014).  
19. Collins, M. et al. Integrated spatial multiplexing of heralded single-photon sources. Nat. Commun. 4, 2582 (2013).  
20. Silverstone, J. W. et al. On-chip quantum interference between silicon photon-pair sources. Nat. Photon. 8, 104-108 (2014).  
21. Najafi, F. et al. On-chip detection of non-classical light by scalable integration of single-photon detectors. Nat. Commun. 6, 5873 (2015).  
22. Aspuru-Guzik, A. & Walther, P. Photonic quantum simulators. Nat. Phys. 8, 285-291 (2012).  
23. Huh, J., Guerreschi, G. G., Peropadre, B., McClean, J. R. & Aspuru-Guzik, A. Boson sampling for molecular vibronic spectra. Nat. Photon. 9, 615-620 (2015).  
24. Levi, L., Krivolapov, Y., Fishman, S. & Segev, M. Hyper-transport of light and stochastic acceleration by evolving disorder. Nat. Phys. 8, 912-917 (2012).  
25. Amir, A., Lahini, Y. & Perets, H. B. Classical diffusion of a quantum particle in a noisy environment. Phys. Rev. E 79, 050105 (2009).  
26. Anderson, P. W. Absence of diffusion in certain random lattices. Phys. Rev. 109, 1492-1505 (1958).  
27. Lahini, Y., Bromberg, Y., Christodoulides, D. N. & Silberberg, Y. Quantum correlations in two-particle Anderson localization. Phys. Rev. Lett. 105, 163905 (2010).  
28. Segev, M., Silberberg, Y. & Christodoulides, D. N. Anderson localization of light. Nat. Photon. 7, 197-204 (2013).  
29. Rebentrost, P., Mohseni, M., Kassal, I., Lloyd, S. & Aspuru-Guzik, A. Environment-assisted quantum transport. New J. Phys. 11, 033003 (2009).  
30. Mohseni, M., Rebentrost, P., Lloyd, S. & Aspuru-Guzik, A. Environment-assisted quantum walks in photosynthetic energy transfer. J. Chem. Phys. 129, 174106 (2008).  
31. Reck, M. & Zeilinger, A. Experimental realization of any discrete unitary operator. Phys. Rev. Lett. 73, 58-61 (1994).  
32. Miller, D. A. B. Self-configuring universal linear optical component. Photon. Res. 1, 1-15 (2013).  
33. Mower, J., Harris, N. C., Steinbrecher, G. R., Lahini, Y. & Englund, D. High-fidelity quantum state evolution in imperfect photonic integrated circuits. Phys. Rev. A 92, 032322 (2015).  
34. Lloyd, S., Mohseni, M., Shabani, A. & Rabitz, H. The quantum Goldilocks effect: on the convergence of timescales in quantum transport. Preprint at http://arxiv.org/abs/1111.4982 (2011).  
35. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
36. Harris, N. C. et al. Efficient, compact and low loss thermo-optic phase shifter in silicon. Opt. Express 22, 10487-10493 (2014).  
37. Aaronson, S. & Arkhipov, A. in Proc. 43rd Annual ACM Symposium on Theory of Computing (eds Fortnow, L. & Vadhan, S.) 333-342 (ACM, 2011).  
38. Spring, J. B. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2012).  
39. Broome, M. A. et al. Photonic boson sampling in a tunable circuit. Science 339, 794-798 (2012).

40. Prevedel, R. et al. High-speed linear optics quantum computing using active feed-forward. Nature 445, 65-69 (2007).  
41. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
42. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
43. Childs, A. M. Universal computation by quantum walk. Phys. Rev. Lett. 102, 180501 (2009).  
44. Baehr-Jones, T. et al. A 25 Gb/s silicon photonics platform. Preprint at http:// arxiv.org/abs/1203.0767 (2012).  
45. Kempe, J. Quantum random walks: an introductory overview. Contemp. Phys. 44, 307-327 (2003).  
46. Notaros, J. et al. in Optical Fiber Communications Conference and Exhibition (OFC), 1-3 (IEEE, 2016).  
47. Cardenas, J. et al. Low loss etchless silicon photonic waveguides. Opt. Express 17, 4752-4757 (2009).  
48. Wilkes, C. M. et al. 60 dB high-extinction auto-configured Mach-Zehnder interferometer. Opt. Lett. 41, 5318-5321 (2016).  
49. Yao, X.-C. et al. Observation of eight-photon entanglement. Nat. Photon. 6, 225-228 (2012).  
50. Silverstone, J. W. et al. Qubit entanglement between ring-resonator photon-pair sources on a silicon chip. Nat. Commun. 6, 7948 (2015).  
51. Gerrits, T. et al. On-chip, photon-number-resolving, telecommunication-band detectors for scalable photonic information processing. Phys. Rev. A 84, 060301 (2011).  
52. McCaughan, A. N. & Berggren, K. K. A superconducting-nanowire three-terminal electrothermal device. Nano Lett. 14, 5748-5753 (2014).

# Acknowledgements

N.C.H. and M.P. acknowledge support from the National Science Foundation Graduate Research Fellowship Program grants 1122374 and 1122374, respectively. G.S. acknowledges support from the Department of Defense National Science and Engineering Graduate Fellowship. Y.L. acknowledges support from the Pappalardo Fellowship in Physics. This work was supported in part by the Air Force Office of Scientific Research (AFOSR) Multidisciplinary University Research Initiative (FA9550-14-1-0052) and the Air Force Research Laboratory programme (FA8750-14-2-0120). M.H. acknowledges support from the AFOSR Small Business Technology Transfer programme (FA9550-12-C-0079 and FA9550-12-C-0038) and G. Pomrenke, of AFOSR, for his support of the optoelectronic systems integration in silicon (OpSIS) effort, through a Presidential Early Career Award in Science and Engineering award (FA9550-13-1-0027) and funding for OpSIS (FA9550-10-1-0439). D.E. acknowledges support by Excitonics, an Energy Frontier Research Center funded by the US Department of Energy, Office of Science, Office of Basic Energy Sciences under award no. desc0001088. The authors thank C. Galland for his discussions about the result.

# Author contributions

N.C.H. designed the photonic integrated circuit and experimental set-up and performed the experiments. N.C.H. laid out the design mask, with assistance from G.S. on metal routing. N.C.H. and M.P. calibrated the system. N.C.H., Y.L., G.S., S.L. and D.E. conceived the experiment. D.B. assisted with the theory. C.C. and F.N.C.W. assisted with multiphoton experiments. T.B.-J. and M.H. fabricated the system. All authors contributed to writing the paper.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. Correspondence and requests for materials should be addressed to N.C.H.

# Competing financial interests

The authors declare no competing financial interests.

# Methods

Fabrication of photonic circuit. We fabricated the PNP on a silicon-on-insulator wafer with  $2\mu \mathrm{m}$  of buried  $\mathrm{SiO}_2$  in the Optoelectronic Systems Integration in Silicon foundry. Device regions were defined using partial and full etches in the silicon device layer, resulting in 90-nm- and 220-nm-thick structures, respectively. A silica cladding  $2\mu \mathrm{m}$  thick was thermally grown on top of the device layer to achieve transverse symmetry for the optical modes. Input and output optical coupling was achieved with an inverse taper (from  $500~\mathrm{nm}$  wide to  $200~\mathrm{nm}$  over a distance of 300  $\mu \mathrm{m}$ ). Light was guided in  $500\mathrm{nm}\times 220\mathrm{nm}$  silicon ridge waveguides with a single transverse-electric mode  $(\mathrm{TE}_0)$  near  $1,550~\mathrm{nm}$  and an effective index of 2.57. Thermo-optic phase shifters<sup>36</sup> were defined by full and partial etches and two boron implants with concentrations of  $7\times 10^{17}\mathrm{cm}^{-3}$  and  $1.7\times 10^{20}\mathrm{cm}^{-3}$ . Due to the high active element densities, two aluminium layers and two via layers were required to simplify the phase shifter electrical signal routing.

Measurement description. Continuous-wave laser light  $(100\mu \mathrm{W}$  at  $1,570~\mathrm{nm}$  wavelength) was launched into input 14, and the intensity at outputs 1-26 was measured using an array of calibrated photodiodes. Loss and coupling were independently measured for each input and output channel to accurately estimate the resultant output intensity distributions. The measured intensity distributions were normalized to give the probability distributions presented.

Fidelity calculations. To evaluate the closeness between one-dimensional distributions, we used the metric  $\sum_{i}\sqrt{P_{i}q_{i}}$ , where  $p$  and  $q$  are probability-normalized distributions (that is,  $\sum_{i}p_{i} = 1$ ). For two-dimensional distributions, we used the metric  $\sum_{ij}\sqrt{P_{ij}Q_{ij}}$  where the distributions were normalized to unity as  $\sum_{ij}P_{ij} = 1$ .

Data availability. The data that support the plots within this paper and other findings of this study are available from the corresponding author upon reasonable request.