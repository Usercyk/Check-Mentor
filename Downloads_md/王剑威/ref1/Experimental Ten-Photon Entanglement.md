# Experimental Ten-Photon Entanglement

Xi-Lin Wang, Luo-Kan Chen, W. Li, H.-L. Huang, C. Liu, C. Chen, Y.-H. Luo, Z.-E. Su, D. Wu, Z.-D. Li, H. Lu, Y. Hu, X. Jiang, C.-Z. Peng, L. Li, N.-L. Liu, Yu-Ao Chen, Chao-Yang Lu, and Jian-Wei Pan  
Hefei National Laboratory for Physical Sciences at Microscale and Department of Modern Physics,  
University of Science and Technology of China, Hefei, Anhui 230026, China,  
CAS Centre for Excellence and Synergetic Innovation Centre in Quantum Information and Quantum Physics,  
Hefei, Anhui 230026, China,  
and CAS-Alibaba Quantum Computing Laboratory, Shanghai, 201315, China  
(Received 19 July 2016; published 15 November 2016)

We report the first experimental demonstration of quantum entanglement among ten spatially separated single photons. A near-optimal entangled photon-pair source was developed with simultaneously a source brightness of  $\sim 12\mathrm{MHz} / \mathrm{W}$ , a collection efficiency of  $\sim 70\%$ , and an indistinguishability of  $\sim 91\%$  between independent photons, which was used for a step-by-step engineering of multiphoton entanglement. Under a pump power of  $0.57\mathrm{W}$ , the ten-photon count rate was increased by about 2 orders of magnitude compared to previous experiments, while maintaining a state fidelity sufficiently high for proving the genuine ten-particle entanglement. Our work created a state-of-the-art platform for multiphoton experiments, and enabled technologies for challenging optical quantum information tasks, such as the realization of Shor's error correction code and high-efficiency scattershot boson sampling.

DOI: 10.1103/PhysRevLett.117.210502

Quantum entanglement [1-3] among multiple spatially separated particles is of fundamental interest, and can serve as a central resource for studies in quantum nonlocality, quantum-to-classical transition [4], quantum error correction [5], and quantum simulation [6]. The ability of generating an increasing number of entangled particles is an important benchmark for quantum information processing [7]. The largest entangled states were previously created with 14 trapped ions [8], eight photons [9], and five superconducting qubits [10].

Despite fast progress in linear optics quantum computing [11-13] in recent decades, the limiting bottleneck remains the number of experimentally controlled single photons. Even for nonuniversal quantum computation models such as boson sampling [12] that demands minimal physical resources, 20-30 single photons are required to reach quantum supremacy. The previously demonstrated eight-photon entangled state had a coincidence count rate of  $\sim 9$  per hour [9]. Based on the same technique, the ten-photon count rate would be as low as  $\sim 170$  per year.

For multiphoton experiments with spontaneous parametric down-conversion (SPDC) [13], the probability  $(p)$  of generating a single photon pair per pump pulse should be kept small (typically  $< 0.1$ ), to suppress the undesired noise contribution from double-pair emission rate  $(\sim p^2)$ . To increase the count rate of the entangled photons without compromising the single-photon purity and indistinguishability, it is most crucial to engineer the spatial and spectral properties of the pulsed SPDC to enhance the photon collection efficiency into a single spatial mode. In previous multiphoton entanglement experiments [9], however, the

collection efficiency was not sufficient to demonstrate ten-photon entanglement.

The key to our ten-photon entanglement experiment is a pulsed SPDC photon-pair source with simultaneously high brightness  $(\sim 1.2\times 10^{7}$  photon pairs generated per watt), high collection efficiency  $(\sim 70\%)$ , and high photon indistinguishability  $(\sim 91\%)$ , as shown in Fig. 1. To achieve a high coupling efficiency, we adopted beamlike type-II SPDC [14-20], where the signal-idler photon pairs are emitted as two separate circular beams in a Gaussian-like intensity distribution, confirmed by the recorded image displayed in the right-hand panel of Fig. 1(a). This is favorable for collecting the produced fluorescence into a single-mode fiber [16], a significant advantage compared to the noncollinear SPDC where the photon pairs are collected from two intersections of the down-converted rings [21]. In our experiment, using a single  $\beta$ -barium borate (BBO) crystal with  $2\mathrm{mm}$  thickness, the photon collection efficiency was measured [22] to be  $88\%$  without narrow-band filtering.

To generate polarization-entangled photon pairs, we adopted a sandwichlike geometry [19,20] where a halfwave plate (HWP) is sandwiched between two 2-mm-thick, identically cut BBOs (see Supplemental Material [23]). The polarization state of the correlated photon pairs generated from the left BBO can be written as  $|V_{1,o}\rangle |H_{2,e}\rangle$ , where  $H$  ( $V$ ) denotes horizontal (vertical) polarization and the subscripts  $1, o$  ( $2, e$ ) indicate the single photon being the downconverted ordinary (extraordinary) light in spatial mode 1 (2). The photons pass through the HWP and are rotated to its orthogonal state  $|H_{1,o}\rangle |V_{2,e}\rangle$ , which are then coherently superposed with the photon pair  $|V_{1,o}\rangle |H_{2,e}\rangle$  generated

![](images/69cf28382b7d8939056d17cfc7106f3c95b7645f19ad0e7df2c197c3766eec1f.jpg)

![](images/54cf3807d4ace59ab5f1d31c61e6d201ac52f0cbb4f141759cf719444daa3143.jpg)

![](images/d5e5b3ee7812274373b7346655c686d1a40125345809502c43d11dff42cce318.jpg)

![](images/86a7d4203417a03efdfa919179e99245a54a86892f6e7efccfca6d4d89262bc5.jpg)

![](images/e78ce54fbf95d3df9c2b525dc93ea56dabad540eceab239b75083903df4e893c.jpg)  
FIG. 1. Entangled photons from SPDC with high collection efficiency and photon indistinguishability. (a) The top panel shows a single BBO setup for generating signal-idler photon pairs in two separate circular beams, evident by the image of the photoemission profile taken using an electron multiplying charge coupled device (EMCCD). The spectra for the  $e$  and  $o$  photons are measured using a spectrometer, showing a different bandwidth of 5.2 and  $10.3\mathrm{nm}$ , respectively. The bottom panel shows a sandwich-like BBO + HWP + BBO geometry for generating entangled photons, after careful birefringent compensations. (b) Experimentally detected two-photon count rate as a function of laser pump power, with and without narrow-band filtering. (c) The entangled state fidelity at different two-photon count rates. (d) Measurement of the joint spectrum of the photon pair. (e) Test of indistinguishability between independent SPDC photons through two-photon interference at different pump power [23].

![](images/3fbe40f9e9867645860d940764aa026428e1a692cfe836734d36ccddaf253b47.jpg)

from the right BBO. The sandwichlike structure engineers the  $e$  and  $o$  photon emission to be spatially separated, allowing separate, efficient narrow-band filtering for the  $e$  and  $o$  photons [24]. By careful spatial and temporal

compensations [23], entangled photons in the state  $\left(|H_{1,o}\rangle |V_{2,e}\rangle +|V_{1,o}\rangle |H_{2,e}\rangle\right) / \sqrt{2}$  were prepared.

The observed count rate and fidelity of the two-photon entanglement as a function of pump power are summarized in Figs. 1(b) and 1(c). At a pump power of  $0.57\mathrm{W}$ , with and without narrow-band filters of  $3\mathrm{-nm}$  bandwidth for the  $e$  photon and  $8\mathrm{nm}$  for the  $o$  photon,  $1.2\times 10^{6}$  and  $3\times 10^{6}$  two-photon counts per second were detected, respectively, with a state fidelity (the overlap with an ideal two-photon entangled state) of 0.97 and 0.93. Thanks to the new source design with a high collection efficiency of  $70\%$ , we obtained an entangled-photon source  $\sim 4$  times brighter than the previous result in eight-photon entanglement [9], by using only  $65\%$  pump power (for a detailed comparison with other SPDC sources, see Supplemental Material [23]). This increases the ten-photon coincidence count rate by about 2 orders of magnitude and thus makes the experimental observation possible.

Entangling independent single photons requires a high mutual indistinguishability between them. For example, any spectral or temporal information that labels a photon could reveal which way it comes from, thus eliminating the quantum interference. We measure the joint spectrum of the two photons, as shown in Fig. 1(d), and observe a tilted elliptical joint spectral intensity distribution. Its long axis is about  $25^{\circ}$  with respect to the vertical direction, indicating that the  $o$  and  $e$  photons remain frequency correlated [30]. With 3- and 8-nm filtering for the  $e$  and  $o$  photon, respectively, we can expect a photon purity of 0.93. The photon indistinguishability is experimentally tested through two-photon quantum interference [see Fig. 1(e) and Supplemental Material [23]]. We observe a raw interference visibility of 0.91(1) under a low pump power of  $\sim 44\mathrm{mW}$ , where the higher-order emission rate is kept small; thus, this 0.91 visibility indicates a lower limit of photon indistinguishability. Under a high pump power of 1 W, the visibility is reduced to 0.76(1), due to the noise contributions from double-pair emission of SPDC.

The experimental setup for entangling five successive SPDC photon pairs into a ten-photon Schrödinger-cat-like state is illustrated in Fig. 2. Five  $e$  photons, each from an entangled pair, are combined on a linear optical network consisting of four polarizing beam splitters (PBSs). The time delays between different paths were finely adjusted to ensure that the photons arrived at the PBSs simultaneously. After the PBSs, the single photons are coupled into single-mode fibers and detected by silicon single-photon detectors.

As the PBSs transmit  $H$  and reflect  $V$  polarizations, it is straightforward to check that after the four PBSs, if we detect one and only one single photon in each output port (i.e., a ten-photon coincidence), the ten photons will be projected into the Schrödinger-cat-like state [2], also known as a Greenberger-Horne-Zeilinger (GHZ) state [3]:

$$
\left| \psi^ {1 0} \right\rangle = \left(\left| H \right\rangle^ {\otimes 1 0} + \left| V \right\rangle^ {\otimes 1 0}\right) / \sqrt {2}.
$$

![](images/b16e66e72d7907aa96b69c9a91ef4914469743b0e26b732160c79503d3f6b203.jpg)  
FIG. 2. Experiment setup for generating a ten-photon polarization-entangled GHZ state. (a) A pulsed ultraviolet laser was focused on five HWP-sandwiched BBO crystals to produce five entangled photon pairs in spatial modes 1-2, 3-4, 5-6, 7-8, and 9-10. Four prisms were used to adjust the time delay to ensure that the photons simultaneously arrive at the PBSs. The outputs were detected by 20 single-photon detectors where all the 1024 ten-photon coincidence events were simultaneously recorded by a coincidence counting system. (b) Graph-state representation of the process to combine the five separate photon pairs into the ten-photon entangled GHZ state. The graph states can be associated with graphs where each vertex represents a qubit prepared in the state  $(|H\rangle + |V\rangle) / \sqrt{2}$  and each edge represents a controlled phase gate having been applied between the two connected qubits. C-BBO: sandwich-like BBO + HWP + BBO combination; SC-YVO $_4$ : YVO $_4$  crystal for spatial compensation; TC-YVO $_4$ : YVO $_4$  crystal for temporal compensation. See Supplemental Material [23] for details.

This is because the ten-photon coincidence events can only originate from either the case that all the photons are  $H$  polarized or the case that all are  $V$  polarized—two possibilities quantum mechanically indistinguishable. The entangled states and their creation process can be intuitively illustrated in Fig. 2(b) using a graph-state presentation [31], where each vertex represents a qubit and each edge indicates a controlled logic gate having been applied between the two connected qubits. The combination of two single photons at a PBS can be described by the parity-check operator,  $|H\rangle |H\rangle \langle H|\langle H| + |V\rangle |V\rangle \langle V|\langle V|$ , which leads to the "fusion" of separate two-qubit graphs into a larger star-shaped graph state. Other  $N$ -photon GHZ states (e.g.,  $N = 2, 4, 6, 8$ ) in the form  $|\psi^{N}\rangle = (|H\rangle^{\otimes N} + |V\rangle^{\otimes N}) / \sqrt{2}$  can be engineered step by step using a similar method in the process of generating the ten-photon GHZ state.

To demonstrate the  $N$ -photon coherence of the generated GHZ states, we measure the  $N$  single photons individually along the basis of  $(|H\rangle \pm e^{i\theta}|V\rangle) / \sqrt{2}$  and detect all the  $2^{N}$  combinations of  $N$ -photon output. From these measurements, we obtain the experimentally estimated expectation values of the observable  $M_{\theta}^{\otimes N} = (\cos \theta \sigma_x + \sin \theta \sigma_y)^{\otimes N}$ . The coherence of the  $N$ -qubit GHZ state, which is defined by the off-diagonal element of its density matrix and reflects the coherent superposition between the  $|H\rangle^{\otimes N}$  and  $|V\rangle^{\otimes N}$  component of the GHZ state, can be calculated by [32]

$$
C ^ {N} = \frac {1}{N} \sum_ {k = 0} ^ {N - 1} (- 1) ^ {k} \langle M _ {(k \pi / N)} ^ {\otimes N} \rangle .
$$

For the two-, four-, six-, eight-, and ten-photon GHZ states, the coherence is calculated to be 0.9305(3), 0.750(6), 0.612 (28), 0.538(29), and 0.438(27), respectively, from measurements at certain angles  $\theta = k\pi /N,k = 0,1,\dots,N - 1$

Figure 3 shows the experimentally obtained expectation values of  $\langle M_{\theta}^{\otimes N}\rangle (N = 1,2,4,6,8)$  with  $\theta$  ramping continuously from 0 to  $\pi$ . The data are fitted to sinusoidal fringes that show an  $N$  times increase of the oscillatory frequencies for the  $N$ -photon GHZ states, with a gradual reduction of fringe visibility that corresponds to the coherence of the GHZ states, as mentioned above. Ideally, for  $N = 1$ , i.e., a single-photon state  $(|H\rangle + |V\rangle) / \sqrt{2}$ , the expectation value is  $\propto \cos \theta$ . For the  $N$ -photon GHZ state  $|\psi^{N}\rangle = (|H\rangle^{\otimes N} + |V\rangle^{\otimes N}) / \sqrt{2}$ , where all the entangled photons collectively respond to the phase change, the expectation value is  $\propto \cos N\theta$ . This observed  $N\theta$  oscillation behavior highlights the potential of the GHZ states for entanglement-enhanced superresolving phase measurements [33].

For a more complete characterization of the  $N$ -photon states, we measure their state fidelities, that is, the overlap of the experimentally produced state with the ideal one:  $F(\psi^{N}) = \langle \psi^{N}|\rho_{\mathrm{expt}}|\psi^{N}\rangle = \mathrm{Tr}(\rho_{\mathrm{ideal}}\rho_{\mathrm{expt}})$  and

![](images/24d3f2448f915e3d81d69c54c9103959d45608602a336ca888e7c00d7ea5cd19.jpg)

![](images/a9ed054604ee2b3916ee8793e067b54674008f36fa00f3f8861c20a56973ea09.jpg)

![](images/23459432d64cfb899b5555e50c8a1d3652b7acb24e37ad0a00cd98394a30d13f.jpg)

![](images/7eeced66c0c4a105823e93013e151ea1dd9c458265f54e8bbb890d64b1e49791.jpg)

![](images/40858eb2c1ac2f5860ee1793d6ea44b01df3ac2b540d74a09e3e679707015f77.jpg)  
FIG. 3.  $N$ -photon coherence. The  $N$  single photons were individually measured in the basis of  $(|H\rangle \pm e^{i\theta}|V\rangle) / \sqrt{2}$  by  $2N$  single-photon detectors. (a)  $N = 1$ , (b)  $N = 2$ , (c)  $N = 4$ , (d)  $N = 6$ , and (e)  $N = 8$ . Each of the  $2^N N$ -photon events signals the observation of an eigenstate of the observable  $M_{\theta}^{\otimes N}$  with corresponding eigenvalue of  $v_{j} = +1$  or  $v_{j} = -1$ . From the relative probabilities of the  $N$ -photon detection events  $p_j$ ,  $j = 1, \dots, 2^N$ , we can then compute the expectation values of the observables by  $\langle M_{\theta}^{\otimes N}\rangle = \sum_{j=1}^{2^N} p_j v_j$ . The  $x$  axis is the phase shift  $\theta$  between  $H$  and  $V$ . The  $y$  axis is the experimentally obtained  $\langle M_{\theta}^{\otimes N}\rangle$ . The error bars represent 1 standard deviation [in (a)-(c) the error bars are smaller than the data points], calculated from Poissonian counting statistics of the raw detection events.

![](images/403e235e6e3b3ba655114639018941dfd5bee8c6a0f1f83e7f5733fb1c85ed3e.jpg)

![](images/7a07ab35e71faa3784f3be47f9796c3cf49808adca75b0085ac3699ed1659313.jpg)  
FIG. 4. Experiment results for ten-photon genuine entanglement at pump power of  $0.57\mathrm{W}$ . (a) Ten-photon coincidence counts in  $|H\rangle / |V\rangle$  basis accumulated for  $35\mathrm{h}$ . (b) Expectation values of  $M_{k\pi/10}^{\otimes 10} = \cos(k\pi/10)\sigma_x + \sin(k\pi/10)\sigma_y$  ( $k=0,1,\ldots,9$ ) obtained by the measurement in the basis of  $(|H\rangle \pm e^{ik\pi/10}|V\rangle)/\sqrt{2}$ . Each setting is measured in  $\sim 26\mathrm{h}$  to accumulate  $\sim 100$  events. The error bars represent 1 standard deviation, calculated from Poissonian counting statistics of the raw detection events.

$\rho_{\mathrm{ideal}} = |\psi^N\rangle \langle \psi^N| = (P^N +C^N) / 2$  [32,34], where  $P^{N} =$ $(|H\rangle \langle H|)^{\otimes N} + (|V\rangle \langle V|)^{\otimes N}$  denotes the population of the  $|H\rangle^{\otimes N}$  and  $|V\rangle^{\otimes N}$  components of the GHZ state. The fidelity can be calculated by the expectation values of the average of the population and coherence  $F(\psi^{N}) = (\langle P^{N}\rangle +\langle C^{N}\rangle) / 2.$  The experimental data for the ten-photon state are shown in Fig. 4. Under a laser pump power of  $0.57\mathrm{W}$  impinged on the first crystal, we achieve a ten-photon count rate of  $\sim 4$  per hour, and a state fidelity of 0.573(23), which exceeds the threshold of 0.5 by 3.2 standard deviations. Thus, we can prove the presence of genuine ten-partite entanglement [34], excluding the produced state from any incompletely entangled (e.g., biseparable) state. Meanwhile, we systematically measured the state fidelities of two-, four-, six-, and eight-photon GHZ states together with their count rate following the same method, which are listed in Table I.

The main source of noise causing the imperfection of the  $N$ -photon states is from the double-pair emission of SPDC. Increasing the laser pump power can boost the photon generation probability and also the double-pair emission rate. As an example, we further tested with a laser pump power of  $0.7\mathrm{W}$ , where we detected a two-photon count rate of  $1.5\mathrm{MHz}$ . Under this condition, we detected a higher ten-photon count rate of  $\sim 11$  per hour, but a reduced state fidelity of 0.429(21) (see Fig. S1 in Supplemental Material), demonstrating the detrimental effect of high-order SPDC emission. This fidelity is below the threshold of 0.5 for proving the genuine ten-particle entanglement. A less stringent criteria, distillable entanglement [25], indicates that out of many copies of the imperfectly created states, ten-photon entanglement can be produced by local operations and classical communications. Using this criteria, our data prove ten-photon distillable entanglement

TABLE I. Summary of the measured  $N$  -photon count rate, state fidelities, and tests of  $N$  -qubit entanglement. The errors in brackets represent 1 standard deviation, deduced from propagated Poissonian counting statistics of the raw detection events.  

<table><tr><td>N-photon GHZ state</td><td>2a</td><td>4a</td><td>6a</td><td>8a</td><td>10a</td><td>10b</td></tr><tr><td>Fidelity</td><td>0.9720(1)</td><td>0.833(4)</td><td>0.710(16)</td><td>0.644(22)</td><td>0.573(23)</td><td>0.429(21)</td></tr><tr><td>Distillable entanglement (σ)</td><td>5215</td><td>122.3</td><td>20.8</td><td>17.7</td><td>15.2</td><td>7.2</td></tr><tr><td>Genuine entanglement (σ)</td><td>4334</td><td>84.6</td><td>13.3</td><td>6.5</td><td>3.1</td><td>-3.4</td></tr><tr><td>Count rate (Hz)</td><td>1200000</td><td>6000</td><td>39</td><td>0.2</td><td>0.0011</td><td>0.0031</td></tr></table>

aUnder a laser pump power of 0.57 W.  
bUnder a laser pump power of  $0.7\mathrm{W}$

with a statistical significance of 7.2 standard deviations [23]. Using high-efficiency photon-number-discriminating single-photon detectors [35], the noise from higher-order emission of SPDC can be eliminated. Exploiting the time-bin encoding [36], which requires only one nonlinear crystal and two detectors, the resource overhead for  $N$ -photon entanglement can be drastically reduced. Integrating the photon source, circuit, and detectors all on a chip [37] can provide a more robust approach to optical quantum technologies.

In summary, we have demonstrated the first ten-photon entanglement in experiment. The ability to control ten single photons will enable many previously challenging experiments such as realization of universal quantum error correction code [38], teleportation of three degrees of freedom in a single photon [39], and ground-to-satellite teleportation overcoming high channel loss [40,41]. The combination of high collection efficiency and high indistinguishability in pulsed SPDC [42] is of particular interest for scattershot boson sampling [43], which can significantly enhance the multiphoton count rate and may provide a route to demonstrate quantum supremacy using photonic quantum simulators.

This work was supported by the National Natural Science Foundation of China, the Chinese Academy of Sciences, and the National Fundamental Research Program.

X.-L. W. and L.-K. C. contributed equally to this work.

[1] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. 47, 777 (1935).  
[2] E. Schrödinger, Naturwissenschaften 23, 807 (1935); 23, 823 (1935); 23, 844 (1935).  
[3] D.M. Greenberger, M. Horne, A. Shimony, and A. Zeilinger, Am. J. Phys. 58, 1131 (1990).  
[4] A. J. Leggett, Rep. Prog. Phys. 71, 022001 (2008).  
[5] P. Shor, in Proceedings of the 35th Annual Symposium on the Foundations of Computer Science, edited by S. Goldwasser (IEEE Computer Society Press, Los Alamitos, 1994), pp. 124-134.  
[6] S. Lloyd, Science 273, 1073 (1996).  
[7] P. Zoller et al., Eur. Phys. J. D 36, 203 (2005).

[8] T. Monz, P. Schindler, J. T. Barreiro, M. Chwalla, D. Nigg, W. A. Coish, M. Harlander, W. Hänsel, M. Hennrich, and R. Blatt, Phys. Rev. Lett. 106, 130506 (2011).  
[9] X.-C. Yao, T.-X. Wang, P. Xu, H. Lu, G.-S. Pan, X.-H. Bao, C.-Z. Peng, C.-Y. Lu, Y.-A. Chen, and J.-W. Pan, Nat. Photonics 6, 225 (2012).  
[10] R. Barends et al., Nature (London) 508, 500 (2014).  
[11] P. Kok, W. J. Munro, K. Nemoto, T. C. Ralph, J. P. Dowling, and G. J. Milburn, Rev. Mod. Phys. 79, 135 (2007).  
[12] S. Aaronson and A. Arkhipov, in Proceedings of the 43rd Annual ACM Symposium on Theory of Computing, San Jose (ACM Press, 2011), pp. 333-342.  
[13] J.-W. Pan, Z.-B. Chen, C.-Y. Lu, H. Weinfurter, A. Zeilinger, and M. Zukowski, Rev. Mod. Phys. 84, 777 (2012).  
[14] S. Takeuchi, Opt. Lett. 26, 843 (2001).  
[15] C. Kurtsiefer, M. Oberparleiter, and H. Weinfurter, J. Mod. Opt. 48, 1997 (2001).  
[16] O. Kwon, Y.-W. Cho, and Y.-H. Kim, Phys. Rev. A 78, 053825 (2008).  
[17] Y.-H. Kim, Phys. Rev. A 68, 013804 (2003).  
[18] X.-L. Niu, Y.-F. Huang, G.-Y. Xiang, G.-C. Guo, and Z. Y. Ou, Opt. Lett. 33, 968 (2008).  
[19] S. Takeuchi, U.S. Patent No. 20,050,094,142 (2005).  
[20] C. Zhang, Y.-F. Huang, Z. Wang, B.-H. Liu, C.-F. Li, and G.-C. Guo, Phys. Rev. Lett. 115, 260402 (2015).  
[21] P. G. Kwiat, K. Mattle, H. Weinfurter, A. Zeilinger, A. V. Sergienko, and Yanhua Shih, Phys. Rev. Lett. 75, 4337 (1995).  
[22] M. Giustina et al., Phys. Rev. Lett. 115, 250401 (2015); L. K. Shalm et al., Phys. Rev. Lett. 115, 250402 (2015).  
[23] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.117.210502 for more information about the generation methods of the near-optimal entangled photon pair, the experiment results for ten-photon distillable entanglement, and the raw data for the  $N$ -qubit entanglement, which includes Refs. [9,20,22,24-29].  
[24] Y.-H. Kim, S. P. Kulik, M. V. Chekhova, W. P. Grice, and Y. Shih, Phys. Rev. A 67, 010301 (2003).  
[25] W. Dur and J. I. Cirac, J. Phys. A 34, 6837 (2001).  
[26] T. Guerreiro, A. Martin, B. Sanguinetti, N. Bruno, H. Zbinden, and R. T. Thew, Opt. Express 21, 27641 (2013).  
[27] N. Bruno, A. Martin, T. Guerreiro, B. Sanguinetti, and R. T. Thew, Opt. Express 22, 17246 (2014).  
[28] B.G. Christensen et al., Phys. Rev. Lett. 111, 130406 (2013).  
[29] F. Kaneda et al., Opt. Express 24, 10733 (2016).

[30] P. J. Mosley, J. S. Lundeen, B. J. Smith, P. Wasylczyk, A. B. U'Ren, C. Silberhorn, and I. A. Walmsley, Phys. Rev. Lett. 100, 133601 (2008).  
[31] M. Hein, J. Eisert, and H.-J. Briegel, Phys. Rev. A 69, 062311 (2004).  
[32] C. A. Sackett, D. Kielpinski, B. E. King, C. Langer, V. Meyer, C. J. Myatt, M. Rowe, Q. A. Turchette, W. M. Itano, D. J. Wineland, and C. Monroe, Nature (London) 404, 256 (2000).  
[33] V. Giovannetti, S. Lloyd, and L. Maccone, Nat. Photonics 5, 222 (2011).  
[34] O. Gühne and G. Toth, Phys. Rep. 474, 1 (2009).  
[35] R. H. Hadfield, Nat. Photonics 3, 696 (2009); B. Calkins et al., Opt. Express 21, 22657 (2013).

[36] E. Megidish, T. Shacham, A. Halevy, L. Dovrat, and H. S. Eisenberg, Phys. Rev. Lett. 109, 080504 (2012).  
[37] F. Najafi et al., Nat. Commun. 6, 5873 (2015).  
[38] P. W. Shor, Phys. Rev. A 52, R2493 (1995).  
[39] X.-L. Wang, X.-D. Cai, Z.-E. Su, M.-C. Chen, D. Wu, L. Li, N.-L. Liu, C.-Y. Lu, and J.-W. Pan, Nature (London) 518, 516 (2015).  
[40] J. Yin et al., Nature (London) 488, 185 (2012).  
[41] X.-S. Ma et al., Nature (London) 489, 269 (2012).  
[42] L. K. Shalm, http://spdcalc.org/.  
[43] A. P. Lund, A. Laing, S. Rahimi-Keshari, T. Rudolph, J. L. O'Brien, and T. C. Ralph, Phys. Rev. Lett. 113, 100502 (2014).