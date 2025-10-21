# Multi-photon entanglement in high dimensions

Mehul Malik $^{1,2\star}$ , Manuel Erhard $^{1,2}$ , Marcus Huber $^{3,4,5}$ , Mario Krenn $^{1,2}$ , Robert Fickler $^{1,2\dagger}$  and Anton Zeilinger $^{1,2}$

Forming the backbone of quantum technologies today, entanglement $^{1,2}$  has been demonstrated in physical systems as diverse as photons $^{3}$ , ions $^{4}$  and superconducting circuits $^{5}$ . Although steadily pushing the boundary of the number of particles entangled, these experiments have remained in a two-dimensional space for each particle. Here we show the experimental generation of the first multi-photon entangled state where both the number of particles and dimensions are greater than two. Two photons in our state reside in a three-dimensional space, whereas the third lives in two dimensions. This asymmetric entanglement structure $^{6}$  only appears in multiparticle entangled states with  $d > 2^{6}$ . Our method relies on combining two pairs of photons, high-dimensionally entangled in their orbital angular momentum $^{7}$ . In addition, we show how this state enables a new type of 'layered' quantum communication protocol. Entangled states such as these serve as a manifestation of the complex dance of correlations that can exist within quantum mechanics.

In the recent past, big mysteries in quantum mechanics have been illuminated by taking small steps in the right direction. The phenomenon of quantum interference, for example, appeared when one considered a single quantum particle with at least two discrete levels. Moving to two particles gave us quantum entanglement and Bell's inequalities<sup>8</sup>, which allowed the conflict between quantum mechanics and local realism to be tested in a statistical manner<sup>9</sup>. Increasing the number of entangled particles to three, although seemingly a simple step, provided the first 'all-nothing' test of local realism<sup>10-12</sup>. Alongside this, increasing the dimensions of a single quantum particle from two to three provided a clear test of quantum contextuality<sup>13,14</sup>. History dictates that increasing both the number and dimensions of quantum particles in concert will lead to further interesting and fundamental phenomena. In this Letter, we discuss one such phenomenon—namely, that of asymmetric multiparticle entanglement<sup>6</sup>.

Two-dimensional entangled states are ubiquitous in quantum information today. However, the amount of information carried by a photon is potentially enormous, and harnessing this information leads to quantum communication systems with record capacities and unprecedented levels of security[15,16]. A natural space for exploring large dimensions is a photon's spatial degree of freedom[17]. The orbital angular momentum (OAM) of a photon is a spatial property that provides a discrete and unbounded state space[18]. The dimension of an OAM-carrying photon is given by the number of 'twists' in its wavefront. Recent experiments have shown the entanglement of two photons in up to  $100 \times 100$  dimensions in their spatial modes[19,20] and the teleportation of photons in a four-dimensional OAM-polarization hybrid space[21]. However,

it is not yet known how to entangle three or more photons in a high-dimensional state space.

The dimensionality of two-photon entangled states is given by the Schmidt number[22], which is the rank of the reduced single particle density matrix. This number represents the minimum number of levels one needs to faithfully represent the state and its correlations in any local basis. When one considers three entangled photons of dimensionality greater than two, the question of how many levels per photon are involved has three answers[6,23]. Consider, for example, the state

$$
| \Psi \rangle_ {3 3 2} = \frac {1}{\sqrt {3}} \left[ | 0 \rangle_ {A} | 0 \rangle_ {B} | 0 \rangle_ {C} + | 1 \rangle_ {A} | 1 \rangle_ {B} | 1 \rangle_ {C} + | 2 \rangle_ {A} | 2 \rangle_ {B} | 1 \rangle_ {C} \right] \tag {1}
$$

Notice that the first two photons,  $A$  and  $B$ , live in a three-dimensional space, whereas the third photon,  $C$ , lives in a two-dimensional space. The state's dimensionality is given by a vector of three numbers (3,3,2), which are the ordered ranks of the single particle reductions of the state density operator:

$$
\operatorname {r a n k} \left(\rho_ {A}\right) = 3, \quad \operatorname {r a n k} \left(\rho_ {B}\right) = 3, \quad \operatorname {r a n k} \left(\rho_ {C}\right) = 2 \tag {2}
$$

where  $\rho_{i} = \mathrm{Tr}_{i}|\Psi\rangle_{332}\langle\Psi|_{332}$  is the state of system  $i\in (A,B,C)$ . Only certain combinations of these three ranks are allowed, leading to a rich structure of asymmetric high-dimensional multipartite entangled states[24]. In this Letter, we demonstrate the creation and verification of one such entangled state, and discuss its application in a novel layered quantum communication protocol.

The entanglement of three photons was first achieved by combining two pairs of polarization-entangled photons in such a way that it became impossible, even in principle, to know which pair one of the detected photons belonged to. The workhorse of such experiments is the polarizing beam-splitter (PBS), which is used to mix two photons from independent polarization-entangled pairs in such a manner that information about their origin is erased, producing a four-photon, two-dimensional GHZ state. To manipulate the high-dimensional space of OAM, one would need a device akin to the PBS, but operating on a photon's spatial wavefunction as opposed to its polarization.

The Mach-Zehnder interferometer depicted in Fig. 1 was designed to sort a photon based on the parity of its OAM quantum number[25]. The interferometer has dove prisms (DP1 and DP2) in each arm, rotated by  $90^{\circ}$  with respect to one another. DP1 reflects an incoming photon, inverting its spiral phase front, whereas DP2 both inverts and rotates it by  $180^{\circ}$ . Thus, each photon interferes with a rotated version of itself, leading to constructive or destructive interference depending on its spatial mode

![](images/6e5f98531f907f7b5b057bede7c26dc778056df33e1b9fc9166ecfbe7c3843de.jpg)  
Figure 1 | Schematic of the experiment. A blue laser pulse creates two pairs of OAM-entangled photons in two nonlinear crystals (NL1 and NL2). Both pairs are spatially separated via polarising beam splitters (PBS). A moving trombone prism ensures that a photon from each pair arrives simultaneously at the OAM beam splitter. This device contains two dove-prisms (DP1 and DP2). DP1 reflects an incoming photon that inverts its spiral phase front, whereas DP2 both inverts and rotates it by  $180^{\circ}$ . This results in interference that depends on the parity (odd or even) of the spatial mode. Considered as a whole, the OAM beam splitter reflects odd components of OAM and transmits even ones, mixing the OAM components of two input photons. Depicted for clarity as a Mach-Zehnder interferometer, this was implemented in a modified Sagnac configuration for increased stability (see Supplementary Fig. 1 for an in-depth schematic). A coincidence between detectors B and C can only arise when both detected photons have the same mode parity. This projects photons at detectors (A-C) into an asymmetric three-photon entangled state that is entangled in  $3 \times 3 \times 2$  dimensions of its OAM. The detection of a trigger photon at detector T heralds the presence of this state.

parity. The key to using this device for entangling two independent photons is to send a second photon into the unused input port of the first beam splitter (BS1). This seemingly simple step allows us to use this device as a two-input, two-output 'OAM beam splitter' that reflects photons with odd OAM values and transmits even ones. In this manner, an outgoing photon contains a superposition of odd and even values of OAM from two independent input photons.

Our procedure for generating the high-dimensional tripartite state uses two independent entangled photon pairs created in two non-linear crystals (NL1 and NL2). Suppose that the two pairs are in the state

$$
\begin{array}{l} \left| \Psi \right\rangle_ {A B C D} = \frac {1}{\sqrt {3}} \left(\left| 1 \right\rangle_ {A} | - 1 \rangle_ {B} + \left| 0 \right\rangle_ {A} | 0 \rangle_ {B} + | - 1 \rangle_ {A} | 1 \rangle_ {B}\right) \tag {3} \\ \otimes \frac {1}{\sqrt {3}} \left(| 1 \rangle_ {C} | - 1 \rangle_ {D} + | 0 \rangle_ {C} | 0 \rangle_ {D} + | - 1 \rangle_ {C} | 1 \rangle_ {D}\right) \\ \end{array}
$$

which is a tensor product of two OAM-entangled photon pairs  $(A, B$  and  $C, D)$  of dimension  $d = 3$  each, with OAM quantum number  $\ell \in \{-1, 0, 1\}$  (higher-order effects are discussed in the Methods). At this stage, mixing these two states results in nine possible four-photon amplitudes. Photons  $B$  and  $C$  are then incident on the two inputs of the OAM beam splitter, which reflects odd values of

![](images/fd4e8dc10250c884d79b9877ef303e771d0fe1c8e54e0f94e5ea7b03bcbfd745.jpg)  
Figure 2 | Three-photon coherent superposition. Experimental data showing the result of measuring photons A-C in superposition states  $|M\rangle_A^{0, -1}$ ,  $|M\rangle_B^{0,1}$  and  $|M\rangle_C^{0,1}$ , respectively, conditioned on measuring photon  $D$  in state  $|P_D^{0, -1}$ . The drop in coincidence counts at the position of zero delay results from interference between photons  $B$  and  $C$ . This indicates that the three-photon state from equation (4) is in a coherent superposition. A Gaussian fit is calculated based on the spectral shape of our narrowband filters and has a full-width at half-maximum of  $473\mu \mathrm{m}$  and a visibility of  $63.5\%$  (see Methods for details). Error bars indicate the Poissonian error in the photon-counting rate.

![](images/a4fc10cf076204bda098a75a9031bc26f16990ec747762eae0ecdf3174d2de96.jpg)  
a

![](images/a6ce26a386c57641e80b443187d4e5ac131401937514a666a0a24f40421c1357.jpg)  
b  
Figure 3 | Witnessing genuine multipartite entanglement in high dimensions. a, To verify that our three-photon state is entangled in  $3 \times 3 \times 2$  dimensions, we have to show that it cannot be decomposed into entangled states of a smaller dimensionality structure. First, we calculate the best achievable overlap of a  $(3,2,2)$  state  $\sigma$  with an ideal target  $(3,3,2)$  state  $|\Psi\rangle$  to be  $F_{\mathrm{max}} = 2/3$ . Next, we calculate the overlap  $F_{\mathrm{exp}}$  of our experimentally generated state  $\rho_{\mathrm{exp}}$  with the target state  $|\Psi\rangle$ . b, The 18 diagonal and 3 unique off-diagonal elements of  $\rho_{\mathrm{exp}}$  that are measured to calculate a value of  $F_{\mathrm{exp}} = 0.801 \pm 0.018$  (elements not measured are filled in with crossed lines). This is above the bound of  $F_{\mathrm{max}} = 0.667$  by 7 standard deviations and verifies that the generated state is genuinely multipartite entanglement in  $3 \times 3 \times 2$  dimensions of its OAM.  $F_{\mathrm{exp}}$  does not reach its maximal value of 1 because the state superposition is not perfectly coherent. Theoretical values are shown by empty bars.

OAM and transmits even ones. Thus, a coincidence detection between its two outputs can only arise when photons  $B$  and  $C$  are both carrying either odd or even OAM. This projects the state from equation (3) onto a subspace spanned by the five terms  $(|1\rangle_A| - 1\rangle_B|1\rangle_C| - 1\rangle_D)$ ,  $(|1\rangle_A| - 1\rangle_B| - 1\rangle_C|1\rangle_D)$ ,  $(|0\rangle_A|0\rangle_B|0\rangle_C|0\rangle_D)$ ,  $(| - 1\rangle_A|1\rangle_B|1\rangle_C| - 1\rangle_D)$  and  $(| - 1\rangle_A|1\rangle_B| - 1\rangle_C|1\rangle_D)$ . Photon  $D$  is then measured in a superposition state given by  $|P\rangle_D^{0, - 1} = (1 / \sqrt{2})(|0\rangle_D + | - 1\rangle_D)$  via a mode-projection carried out by a spatial light modulator (SLM) and a single-photon detector (T), which triggers the three-photon entangled state:

$$
\left| \Psi \right\rangle_ {\exp} = \frac {1}{\sqrt {3}} \left[ | 1 \rangle_ {A} | - 1 \rangle_ {B} | 1 \rangle_ {C} + | 0 \rangle_ {A} | 0 \rangle_ {B} | 0 \rangle_ {C} + | - 1 \rangle_ {A} | 1 \rangle_ {B} | 1 \rangle_ {C} \right] \tag {4}
$$

Note that this state has the same form as equation (1), with the quantum levels  $(0,1,2)$  replaced by the OAM quantum numbers  $(-1,0,1)$ . To ensure that these three terms are in a coherent

superposition (as opposed to an incoherent mixture), we perform superposition measurements in a two-dimensional subspace spanned by the second and third terms in equation (4). Measuring photon  $A$  in state  $|M\rangle_A^{0, - 1} = (1 / \sqrt{2})(|0\rangle_A - | - 1\rangle_A)$  projects the three-photon state into:

$$
\frac {1}{\sqrt {3}} | M \rangle_ {A} ^ {0, - 1} \left(| P \rangle_ {B} ^ {0, 1} | M \rangle_ {C} ^ {0, 1} + | M \rangle_ {B} ^ {0, 1} | P \rangle_ {C} ^ {0, 1}\right) \tag {5}
$$

where  $|P\rangle_{B / C}^{0,1} = (1 / \sqrt{2})(|0\rangle_{B / C} + |1\rangle_{B / C})$  and  $|M\rangle_{B / C}^{0,1} = (1 / \sqrt{2})(|0\rangle_{B / C} - |1\rangle_{B / C})$ . The terms  $|P\rangle_B^{0,1}|P\rangle_C^{0,1}$  and  $|M\rangle_B^{0,1}|M\rangle_C^{0,1}$  are missing because of two-photon destructive interference at the OAM beam splitter, which only occurs when photons  $B$  and  $C$  are indistinguishable[26]. Note that this requires both two-photon and one-photon interference to occur at the OAM beam splitter. The use of narrowband interference filters (IF2) before detectors B and

![](images/eb4a222b39836238fd9fd0aa6da6efe90a5048ec7307940655099b62c0e1fc82.jpg)  
a

![](images/69e1fbe066a05d811d60c501eff96b558cbf20d2420b93e0eee8adc84a970e5a.jpg)  
b

![](images/bae24d73605b0ea5f90f98f2e2dcc8212be9c1778cc71db086b772a124ce9077.jpg)  
Figure 4 | A layered quantum communication protocol. a, When Alice, Bob, and Carol share an asymmetric (3,3,2) entangled state, all three have access to an entangled bit in the (0,1) basis. Moreover, whenever Carol has a 1, Alice and Bob share an entangled bit on the (1,2) basis. b, After sufficient data is collected, these bits can be used as a one-time pad to encrypt a secret message shared among all three parties. In addition, Alice and Bob can share a second layer of information unknown to Carol. Security is verified by checking for the presence of (3,3,2) entanglement in a randomly selected subset of photons.

![](images/2b54241901cd38a4b5f14f37926be49baa71c93002cc29ada3988678c0526c8d.jpg)

C blurs out the temporal correlations of the photons with their entangled partners, ensuring that they cannot be distinguished based on their time of arrival[27]. We look for destructive interference between photons  $B$  and  $C$  by projecting them into states  $|M\rangle_{B}^{0,1}$  and  $|M\rangle_{C}^{0,1}$ , and scanning the trombone prism (Fig. 1). At the zero-delay position, both photons arrive at the first beam splitter (BS1) at precisely the same time and interfere destructively, leading to a drop in coincidence counts between all four detectors. The characteristic dip in Fig. 2 has a width of  $473\mu \mathrm{m}$  and visibility of  $63.5\%$  that match what we expect from our experimental parameters (see Methods).

We have developed a new method for certifying multipartite and multidimensional entanglement that uses a significantly fewer number of measurements than full state tomography. This method relies on proving that the measured (3,3,2) state cannot be decomposed into entangled states of a smaller dimensionality structure[6,28]. These states form a 'Russian nesting doll' structure of concentric subsets embedded in the set of (3,3,2) states (Fig. 3a). First, we find the best achievable overlap of a (3,2,2) state  $\sigma$  with an ideal (3,3,2) state  $|\Psi\rangle$  to be  $F_{\mathrm{max}} = 2/3$  (see Methods). Next, we calculate the overlap  $F_{\mathrm{exp}}$  of our experimentally generated state  $\rho_{\mathrm{exp}} = |\Psi\rangle_{\mathrm{exp}} \langle \Psi|_{\mathrm{exp}}$  with an ideal (3,3,2) state. If  $F_{\mathrm{exp}} > F_{\mathrm{max}}$ , our state is certified to be entangled in  $3 \times 3 \times 2$  dimensions. To calculate  $F_{\mathrm{exp}}$ , it is sufficient to measure the 18 diagonal and 3 unique off-diagonal elements of  $\rho_{\mathrm{exp}}$ . These are measured via a series of 162 projective measurements of  $27\mathrm{min}$  each (Fig. 3b, numerical values in Supplementary Table 1). From these,  $F_{\mathrm{exp}}$  is calculated to be  $0.801 \pm 0.018$ , which is above the bound of  $F_{\mathrm{max}} = 0.667$  by 7 standard deviations. This certifies that our three-photon state is indeed entangled in  $3 \times 3 \times 2$  dimensions of its OAM. The error in the overlap is calculated by propagating the Poissonian error in the photon-counting rates via a Monte Carlo simulation.

Finally, this high-dimensional three-photon entangled state enables a new type of quantum cryptographic protocol where

different layers of information can be shared asymmetrically with unconditional security. When Alice, Bob, and Carol share a (3,3,2) entangled state (Fig. 4), they have access to one entangled bit in the (0,1) basis, which allows them to generate a secure string of random bits that can be used as a key[29]. However, two-thirds of the time Alice and Bob have access to an extra entangled bit in the (1,2) basis whenever Carol has a 1, allowing them to generate a second secure key. Thus, all three parties can securely share a secret message, with Alice and Bob sharing an extra layer of information that is unknown to Carol. Security can be tested by verifying the presence of (332) entanglement in a randomly selected subset of photons using the entanglement witness from above. The implementation of such a protocol would require multi-outcome measurements of orbital angular momentum, techniques for which are quite mature today[30].

We have created a three-photon entangled state and verified that it is high-dimensionally genuinely multipartite entangled in its orbital angular momentum. Our generated state displays a unique asymmetry in its entanglement structure that has not been experimentally observed before. In addition, the asymmetric entanglement structure of our state has enabled us to develop a new layered quantum communication protocol where different layers of information can be shared securely amongst multiple parties. Our experimental method can be modified to create a vast array of even more complex entangled states[31]—of which the state above is just one example. These techniques will form integral parts of any future experimental toolbox for the creation and manipulation of high-dimensional quantum states. Such asymmetric entangled states constitute a new direction in experimental studies of entanglement, and will allow the development of complex, multi-level quantum networks in the future.

# Methods

Methods and any associated references are available in the online version of the paper.

Received 20 October 2015; accepted 19 January 2016; published online 29 February 2016

# References

1. Schrödinger, E. Die gegenüber situation in der quantenmechanik. Naturwissenschaften 23, 823-828 (1935).  
2. Trimmer, J. D. The present situation in quantum mechanics: a translation of Schrödinger's "Cat Paradox" paper. Proc. Am. Phil. Soc. 124, 323-338 (1980).  
3. Yao, X.-C. et al. Observation of eight-photon entanglement. Nature Photon. 6, 225-228 (2012).  
4. Lanyon, B. P. et al. Experimental violation of multipartite bell inequalities with trapped ions. Phys. Rev. Lett. 112, 100403 (2014).  
5. Kelly, J. et al. State preservation by repetitive error detection in a superconducting quantum circuit. Nature 519, 66-69 (2015).  
6. Huber, M. & de Vicente, J. Structure of multidimensional entanglement in multipartite systems. Phys. Rev. Lett. 110, 030501 (2013).  
7. Zeilinger, A., Horne, M., Weinfurter, H. & Zukowski, M. Three-particle entanglements from two entangled pairs. Phys. Rev. Lett. 78, 3031-3034 (1997).  
8. Bell, J. On the Einstein-Podolsky-Rosen paradox. Physics 1, 195-200 (1964).  
9. Clauser, J., Horne, M., Shimony, A. & Holt, R. Proposed experiment to test local hidden-variable theories. Phys. Rev. Lett. 23, 880-884 (1969).  
10. Greenberger, D. M., Horne, M. A. & Zeilinger, A. in Bell's Theorem, Quantum Theory, and Conceptions of the Universe (ed. Kafatos, M.) 69-72 (Kluwer, 1989).  
11. Mermin, N. D. Extreme quantum entanglement in a superposition of macroscopically distinct states. Phys. Rev. Lett. 65, 1838-1840 (1990).  
12. Pan, J.-W., Bouwmeester, D., Daniell, M., Weinfurter, H. & Zeilinger, A. Experimental test of quantum nonlocality in three-photon Greenberger-Horne-Zeilinger entanglement. Nature 403, 515-519 (2000).  
13. Klyachko, A. A., Can, M. A., Binicioglu, S. & Shumovsky, A. S. Simple test for hidden variables in spin-1 systems. Phys. Rev. Lett. 101, 020403 (2008).  
14. Lapkiewicz, R. et al. Experimental non-classicality of an indivisible quantum system. Nature 474, 490-493 (2011).  
15. Cerf, N., Bouennane, M., Karlsson, A. & Gisin, N. Security of quantum key distribution using d-level systems. Phys. Rev. Lett. 88, 127902 (2002).  
16. Mirhosseini, M. et al. High-dimensional quantum cryptography with twisted light. New J. Phys. 17, 033033 (2015).

17. Malik, M. & Boyd, R. W. Quantum imaging technologies. Riv. Nuovo Cimento 37, 273-332 (2014).  
18. Molina-Terriza, G., Torres, J. P. & Torner, L. Twisted photons. Nature Phys. 3, 305-310 (2007).  
19. Dada, A. C., Leach, J., Buller, G. S., Padgett, M. J. & Andersson, E. Experimental high-dimensional two-photon entanglement and violations of generalized Bell inequalities. Nature Phys. 7, 677-680 (2011).  
20. Krenn, M. et al. Generation and confirmation of a  $(100 \times 100)$ -dimensional entangled quantum system. Proc. Natl Acad. Sci. USA 111, 6243-6247 (2014).  
21. Wang, X.-L. et al. Quantum teleportation of multiple degrees of freedom of a single photon. Nature 518, 516-519 (2015).  
22. Terhal, B. M. & Horodecki, P. Schmidt number for density matrices. Phys. Rev. A 61, 040301 (2000).  
23. Huber, M., Perarnau-Llobet, M. & de Vicente, J. I. Entropy vector formalism and the structure of multidimensional entanglement in multipartite systems. Phys. Rev. A 88, 042328 (2013).  
24. Cadney, J., Huber, M., Linden, N. & Winter, A. Inequalities for the ranks of multipartite quantum states. Linear Algebra Appl. 452, 153-171 (2014).  
25. Leach, J., Padgett, M. J., Barnett, S. M. & Franke-Arnold, S. Measuring the orbital angular momentum of a single photon. Phys. Rev. Lett. 88, 257901 (2002).  
26. Hong, C., Ou, Z. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
27. Kaltenbaek, R. Interference of Photons from Independent Sources PhD thesis, Univ. Vienna (2009).  
28. Fickler, R. et al. Interface between path and orbital angular momentum entanglement for high-dimensional photonic quantum information. Nature Commun. 5, 4502 (2014).  
29. Hillery, M., Bužek, V. & Berthiaume, A. Quantum secret sharing. Phys. Rev. A 59, 1829-1834 (1999).  
30. Mirhosseini, M., Malik, M., Shi, Z. & Boyd, R. W. Efficient separation of the orbital angular momentum eigenstates of light. Nature Commun. 4, 2781 (2013).

31. Krenn, M., Malik, M., Fickler, R., Lapkiewicz, R. & Zeilinger, A. Automated search for new quantum experiments. Phys. Rev. Lett. Preprint at http://arxiv.org/abs/1509.02749 (2015)

# Acknowledgements

We thank T. Scheidl, M. Tillman, J. Handsteiner, R. Lapkiewicz, and G.B. Lemos for helpful discussions. M.M. acknowledges funding from the European Commission through a Marie Curie fellowship (OAMGHZ). M.H. acknowledges funding from the Juan de la Cierva fellowship (JCI 2012-14155), the European Commission (STREP 'RAQUEL') and the Spanish MINECO Project No. FIS2013-40627-P, the Generalitat de Catalunya CIRIT Project No. 2014 SGR 966, the Swiss National Science Foundation (AMBIZIONE PZ00P2_161351), and fruitful discussions at LIQUID. This project was supported by the Austrian Academy of Sciences (ÖAW), the European Research Council (SIQS Grant No. 600645 EU-FP7-ICT), the Austrian Science Fund (FWF) with SFB F40 (FOQUS).

# Author contributions

M.M. devised the concept of the experiment, with assistance from M.K. and R.F. M.M and M.E. performed the experiment. M.H. developed the high-dimensional entanglement witness. M.M., M.E., M.K. and M.H. analysed the data. M.M. and M.H. developed the layered quantum communication protocol. A.Z. initiated the research and supervised the project. M.M. wrote the manuscript with contributions from all authors.

# Additional information

Supplementary information is available in the online version of the paper. Reprints and permissions information is available online at www.nature.com/reprints. Correspondence and requests for materials should be addressed to M.M.

# Competing financial interests

The authors declare no competing financial interests.

# Methods

Down-conversion sources. As shown in Supplementary Fig. 1, a femtosecond pulsed Ti:Sapphire laser (Coherent Chameleon Ultra II) with a centre wavelength of  $808~\mathrm{nm}$  is focused by lens L1 into a  $\beta$ -Barium Borate crystal (BBO) to generate blue pump pulses at  $404~\mathrm{nm}$  via the process of second-harmonic generation. The BBO crystal is incrementally moved by a motor (M) to avoid damage to it. The generated pump pulses (average power of  $820~\mathrm{mW}$ ) are re-collimated by lens L2 and separated from the  $808~\mathrm{nm}$  light by a dichroic mirror (DM1). They are then focused with lens L3 onto two periodically poled potassium titanyl phosphate (ppKTP) crystals (NL1 and NL2)  $1\mathrm{mm} \times 2\mathrm{mm} \times 1\mathrm{mm}$  in size and with a poling period of  $9.55\mu \mathrm{m}$  for type-II phase matching. Two independent photon pairs entangled in their OAM are generated in the two crystals via spontaneous parametric down-conversion (SPDC) of photons from the same pump pulse. The crystals are spatially oriented so that down-conversion occurs when the pump pulses are vertically polarized. To conform to the phase-matching conditions for producing wavelength-degenerate photon pairs at  $808~\mathrm{nm}$ , NL1 (NL2) is heated to  $119.1^{\circ}\mathrm{C}$  ( $121.9^{\circ}\mathrm{C}$ ). A  $4f$  imaging system composed of two lenses (L4) between the two crystals ensures that the waist of the pump pulse is approximately  $240\mu \mathrm{m}$  for both crystals.

The pump waist is chosen such that generation rate of  $\ell = 0$  photons is approximately twice that of the  $\ell = \pm 1$  photons in the two OAM-entangled photon pairs. Note that the theoretical bi-photon OAM state distributions in equation (3) are maximally entangled, whereas our experimentally generated distributions are not. Interestingly, we are able to create a nearly maximally entangled three-photon state by simply unbalancing the trigger photon (T) state superposition to  $|P\rangle_D^{0 - 1} = 0.51|0\rangle_D + 0.86| - 1\rangle_D$ . This has the surprising effect of producing an almost flat state distribution, while lowering our average four-fold count rates only by  $6\%$ . Two dichroic mirrors (DM2) separate the  $404~\mathrm{nm}$  pump pulses from the entangled photon pairs. Owing to the high pump power, the Kerr-lensing effect cannot be neglected and adds an equivalent lens with  $1\mathrm{m}$  focal length into the optical path. This is compensated by carefully aligning the  $4f$  imaging system (L4). To avoid graytracking and damage due to the high pump power, the ppKTP crystals are also moved incrementally in steps of  $200\mu \mathrm{m}$  with motors (M). Movement of the BBO and ppKTP crystals shows slight variation in the count rates, which is compensated for by averaging over several periods of movement within each measurement interval. Two PBSs deterministically separate both photon pairs such that all four photons are propagating in different directions.

Higher-order effects. There are two kinds of higher-order effects that need to be addressed in our experiment. The expected output from down-conversion in the OAM basis can be written as  $\langle |0\rangle |0\rangle +| - 1\rangle |1\rangle +|1\rangle | - 1\rangle +| - 2\rangle |2\rangle +|2\rangle | - 2\rangle +$ $|-3\rangle |3\rangle +|3\rangle |-3\rangle \ldots)$ . We only use the first three terms in our experiment because they have the largest amplitudes that give us the largest count rates. If a higher-order mode  $(|e| > 1)$  is created in the first crystal NL1, the trigger T would not fire (because it only triggers for mode 0 and  $-1$ ). Thus, these higher-order modes do not contribute to the state. As we consider only the  $3\times 3$  dimensional space spanned by  $\ell \in \{-1,0,1\}$ , higher-order modes from the second crystal NL2 also do not contribute to our measured state, as in that case photon A would be outside the considered subspace.

The second type of higher-order effect concerns the generation of multiple photon pairs in one crystal. The probability of obtaining two pairs from one crystal and one pair from each crystal is essentially the same. However, the contribution from double-pair emission from one crystal is ruled out because our state is conditioned on a detection event occurring at all four detectors. Our experiment is constructed in such a way that four photons created in double-pair emission from either one of the crystals cannot, even in principle, be detected at all four detectors. An extra source of noise is the creation of three photon-pairs (two in one crystal and one in the second, or vice versa). In many multi-photon experiments, this is the main source of background that reduces visibilities[21]. The mean number of photon pairs produced per pulse in our experiment can be estimated as  $p \sim 0.0013$ , which results in a three photon-pair probability of  $0.26\%$  as compared with a double pair event. This is substantially lower than other sources of noise in our experiment and can safely be neglected.

OAM beam splitter. This is an interferometric two-input, two-output device that mixes input photons based on the parity of their OAM mode. In Fig. 1 in the main text, the OAM beam splitter is depicted for clarity in its original design[25] as a Mach-Zehnder interferometer. However, our experiment requires long-term interferometric stability, which is not easily attainable with a Mach-Zehnder interferometer. For this reason, we implement the OAM beam splitter in a zero-area, double Sagnac configuration. A similar configuration was used previously for sorting polarization-OAM modes[32]. Highlighted in green in Supplementary Fig. 1, this configuration takes a standard Sagnac loop (that is, one-input and one-output) and shifts it laterally, creating two counter-propagating Sagnac loops side-by-side that meet back up at the beam splitter. This allows us to install a dove prism (DP1 and DP2) in each loop. The interferometer is further implemented in a zero-area configuration that is rotationally invariant, minimizing the rotational dependence of the entire interferometer on the rotation of the Earth. Furthermore, a piezo-controlled mirror (P) is scanned every hour to optimize the alignment of the interferometer and ensure it is sorting OAM modes correctly. In addition to

controlling one of the mirrors actively, the interferometer is enclosed in a plastic box that reduces the air flow through the device and stabilizes the temperature to within  $\pm 0.02^{\circ}\mathrm{C}$ . All of these efforts lead to a very long stability ( $>80\mathrm{h}$ ) and at the same time achieve a very high sorting efficiency of even and odd OAM modes (99:1).

Interference of independent photons. The interference of two photons at the OAM beam splitter critically depends on the indistinguishability of the two particles involved. As the presence of the interfering photons is indicated by the trigger detection events of their respective partner photons, we effectively observe four-photon coincidence events. The interference visibility strongly depends on the physical properties of these four photons, as well as the process by which they are created. This particular phenomenon has been studied in great detail[27] and the theoretically expected visibility is calculated to have the form

$$
V ^ {\prime} = \left[ 2 \frac {\sqrt {\sigma_ {T} ^ {2} + \sigma_ {P} ^ {2}} \sqrt {\sigma_ {S} ^ {2} + \sigma_ {P} ^ {2} + \sigma_ {S} ^ {2} \sigma_ {P} ^ {2} \tau_ {J} ^ {2}}}{\sigma_ {P} \sqrt {\sigma_ {S} ^ {2} + \sigma_ {T} ^ {2} + \sigma_ {P} ^ {2}}} - 1 \right] ^ {- 1} \tag {6}
$$

Here,  $\sigma_{P},\sigma_{S}$ , and  $\sigma_{T}$  are the gaussian spectral widths of the pump, signal, and trigger photons respectively (in units of frequency).  $\sigma_{S}$  and  $\sigma_{T}$  are determined by the widths of narrowband interference filters IF2 and IF1, respectively.  $\tau_{J}$  has units of time and refers to the relative timing jitter between the two crystals, which arises due to the group velocity mismatch between the  $404~\mathrm{nm}$  pump pulse and the  $808~\mathrm{nm}$  downconverted photons in the ppKTP crystals. Moreover, due to the finite pulse width of the  $404~\mathrm{nm}$  pump beam, a second relative timing jitter between the two crystals is also present. In our experiment, the sum of these two timing jitters is approximately  $1\mathrm{ps}^{33}$ .

In addition to spectral distinguishability, the spatial and temporal distinguishability of the two photons both play an important role in the interference visibility. The moving trombone system of mirrors (TB) is used to find the position of zero-delay when photons from both crystals arrive at the OAM beam splitter at the same exact time. The spatial-mode distinguishability of the two input photons at the OAM beam splitter has a further detrimental effect on the total interferometric visibility. We use a  $4f$  imaging system of lenses (L6) to compensate for the extra propagation that the photon from NL1 undergoes with respect to the photon from NL2. Nonetheless, the mode overlap of the two photons at the OAM splitter is not perfect, and reduces the two-photon interference visibility in the following way:

$$
V = \frac {\eta^ {2} V ^ {\prime}}{1 + V ^ {\prime} \left(1 - \eta^ {2}\right)} \tag {7}
$$

Here,  $\eta = \eta_{\mathrm{OAM}} \times \eta_{\mathrm{SP}}$  is the product of the sorting efficiency  $\eta_{\mathrm{OAM}}$  of the OAM beam splitter and the spatial mode overlap  $\eta_{\mathrm{SP}}$  of the two input photons. Inserting our measured/estimated experimental parameters ( $\sigma_{P} = 3.67 \mathrm{THz}$ ,  $\sigma_{T} = 588 \mathrm{GHz}$ ,  $\sigma_{S} = 184 \mathrm{GHz}$ ,  $\tau_{J} = 1 \mathrm{ps}$ ,  $\eta_{\mathrm{OAM}} = 0.99$  and  $\eta_{\mathrm{SP}} = 0.9$ ) into the above formula yields a two-photon interference visibility of  $V = 0.64$ , which is very close to the experimental visibility observed in Fig. 2. The visibility critically depends on the spectral width  $\sigma_{S}$  of the two interfering photons. A smaller  $\sigma_{S}$  greatly improves the interference visibility at the cost of lowering the four-photon count rates. It is therefore important to find an optimal value that provides both sufficiently high visibility and practical count rates. In our experiment, we found this value to be  $\sigma_{S} = 184 \mathrm{GHz}$ . Assuming a Gaussian spectral distribution, the theoretical full-width at half-maximum (FWHM) of the two-photon interference dip is then given by

$$
L _ {\mathrm {d i p}} = \frac {c}{\pi} \sqrt {\frac {2 \ln 2}{\sigma_ {P} ^ {- 2} + \sigma_ {S} ^ {- 2} + \tau_ {J} ^ {2}}} \tag {8}
$$

Inserting the corresponding values from above leads to a expected FWHM dip-width of  $624\mu \mathrm{m}$ , which is close to our experimentally observed value of  $473\mu \mathrm{m}$  in Fig. 2. It is clear from equations (6) and (7) that the spatial mode overlap  $\eta_{\mathrm{SP}}$  has a drastic effect on the interference visibility, and hence on the fidelity of our state. As the experiment was run over a long time, we suspect that the airflow in the laboratory had a direct impact on the time-averaged spatial mode overlap at the OAM-BS. We believe that this can be improved by more effectively isolating the beam paths from the laboratory environment. The OAM-BS stability can be further improved through the use of a more compact and stable design, such as one implemented with specially designed inverting prisms<sup>34</sup>.

Single photon projective measurements. Two extra  $4f$  imaging systems (L6) image the output of the OAM beam splitter onto two holographic spatial light modulators (SLMs). These are liquid-crystal devices that can impart an arbitrary 2D phase pattern onto a photon. We use these devices to perform projection measurements of OAM. These measurements are carried out by flattening the phase of incident photons such that they couple into a single-mode optical fiber $^{35}$ . The scheme is based on the fact that a single-mode fiber (SMF) only carries spatial modes with  $\ell = 0$ . To detect a photon with  $\ell = 1$ , a hologram with  $\ell = -1$  displayed on the SLM projects the photon into mode  $\ell = 0$ . The photon then couples efficiently to an SMF and is guided to a single photon avalanche photodiode (Excelitas SPCM-AQRH-14-FC). The same

procedure also applies to projective measurements of mode superpositions. Note that in our experiment, phase-only holograms are used, which take only the vortex phase structure  $e^{\ell \phi}$  of a Laguerre-Gaussian mode into account, and not its amplitude. This results in an imperfect mode overlap at the SMF $^{36}$  and leads to lowered coupling efficiencies for modes with  $\ell = \pm 1$ . This drop in efficiency can be somewhat compensated by adding a mode-dependent quadratic phase to these holograms, which changes the effective coupling mode-waist.

(332)-entanglement witness. Fully reconstructing our state via tomography would require us to measure 171 density matrix elements, which is impractical for us even with powerful modern techniques such as compressive sensing[37]. As an alternative, we have developed a new method for certifying high-dimensional multipartite entanglement that only requires us to measure the 18 diagonal and 3 unique off-diagonal density matrix elements. To prove that the state is indeed a (332)-type entangled state, we have to prove that it cannot be decomposed into states of a smaller dimensionality structure. We thus have to show that it lies outside the (322) set of states, that is the convex hull of all states that can be decomposed into 322 and 232 states. From the measured data we can extract the fidelity to the ideal state

$$
\left| \Psi \right\rangle = \frac {1}{\sqrt {3}} \left(\left| 0, 0, 0 \right\rangle + \left| 1, - 1, 1 \right\rangle + \left| - 1, 1, 1 \right\rangle\right) \tag {9}
$$

which we will denote as  $F_{\mathrm{exp}} \coloneqq \mathrm{Tr}(\rho_{\mathrm{exp}}|\Psi\rangle \langle \Psi|)$ . We thus need to compare the experimental fidelity with the best achievable fidelity of a (322)-state, that is,

$$
F _ {\max } := \max  _ {\sigma \in (3 2 2)} \operatorname {T r} (\sigma | \Psi) \langle \Psi |) \tag {10}
$$

If  $F_{\mathrm{exp}} > F_{\mathrm{max}}$ , we can conclude that the experimentally certified fidelity cannot be explained by any state in (322) and thus the underlying state is certified to have an entangled dimensionality structure of (332). To calculate  $F_{\mathrm{max}}$  it is useful to observe that it is convex in the set of states, that is, the maximum will always also be reachable by a pure state. Furthermore, as the set (322) is the convex hull of 322 and 232, we can write the following

$$
\begin{array}{l} F _ {\max } = \max  _ {| \Phi | \in (3 2 2)} \left| \langle \Psi | \Phi \rangle \right| ^ {2} \\ = \max  \left[ \max  _ {| \Phi \rangle \in 3 2 2} | \langle \Psi | \Phi \rangle | ^ {2}, \max  _ {| \Phi \rangle \in 2 3 2} | \langle \Psi | \Phi \rangle | ^ {2} \right] \tag {11} \\ \end{array}
$$

Now for a fixed rank vector  $xyz$ , these fidelities can be bounded by noticing that

$$
\begin{array}{l} \max  _ {| \Phi \rangle \in x y z} | \langle \Psi | \Phi \rangle | ^ {2} \leq \min  \left[ \max  _ {\operatorname {r a n k} (\operatorname {T r} _ {2 3} | \Phi \rangle \langle \Phi |) = x} | \langle \Psi | \Phi \rangle | ^ {2}, \right. \\ \max  _ {\operatorname {r a n k} \left(\operatorname {T r} _ {1 3} | \Phi \rangle \langle \Phi |\right) = y} \left| \langle \Psi | \Phi \rangle \right| ^ {2}, \max  _ {\operatorname {r a n k} \left(\operatorname {T r} _ {1 2} | \Phi \rangle \langle \Phi |\right) = z} \left| \langle \Psi | \Phi \rangle \right| ^ {2} ] \tag {12} \\ \end{array}
$$

Now inserting (12) in (11) we can compute each of the appearing terms using a previously published theorem[28]. It states that if a state has a Schmidt decomposition across a cut  $A|\overline{A}$  given by  $|\Psi \rangle = \sum_{i_0}^{r-1} \lambda_i |\nu_A^i \rangle \otimes |\nu_{\overline{A}}^i \rangle$ , we can compute the maximal overlap with a state of bounded rank across this partition as

$$
\max  _ {\operatorname {r a n k} \left(\mathrm {T r} _ {\lambda} | \Phi \rangle \langle \Phi |\right) = x} \left| \left\langle \Psi | \Phi \right\rangle \right| ^ {2} = \sum_ {i = 0} ^ {x - 1} \lambda_ {i} ^ {2} \tag {13}
$$

where we assumed ordered Schmidt coefficients, that is,  $\lambda_{i}\geq \lambda_{i + 1}$ . Now all we need are the coefficients for the Schmidt decompositions for our target state for all three partitions. For  $3|12$  they are  $\{(\sqrt{2} /\sqrt{3}),(1 / \sqrt{3})\}$  and for  $2|13$  and  $1|23$  we get  $\{(1 / \sqrt{3}),(1 / \sqrt{3}),(1 / \sqrt{3})\}$ . Inserting these numbers we find that the maximum overlap of the target state (9) with a (322) state is given by

$$
F _ {\max } = \frac {2}{3} \tag {14}
$$

In contrast to this, entanglement can also be certified with asymmetric assumptions about the observables used<sup>38</sup>. Intrinsically asymmetric states such as ours may be good candidates for such asymmetric certification schemes.

Witness measurements. The experimental fidelity  $F_{\mathrm{exp}} \coloneqq \mathrm{Tr}(\rho_{\mathrm{exp}}|\Psi \rangle \langle \Psi |)$  determines which measurements are required. The projector  $|\Psi \rangle \langle \Psi |$  projects only onto the nonzero diagonal and off-diagonal elements contained in the density matrix  $\rho_{\mathrm{exp}}$ .

Moreover, for the purpose of normalization, it is necessary to measure all other diagonal elements in  $\rho_{\mathrm{exp}}$ . This results in 18 diagonal and 3 unique off-diagonal elements that need to be measured to calculate  $F_{\mathrm{exp}}$ . In our experiment, we can only perform projective measurements with SLMs. A diagonal element is given by one single projection  $(ijk|\rho |ijk) = (C(ijk) / C_T)$ , with  $C_T\coloneqq \sum_{i = -1,0,1}\sum_{j = -1,0,1}\sum_{k = 0,1}C(ijk)$  containing all diagonal elements for normalization. Out of the six off-diagonal elements, only three are unique and need to be measured:  $\langle 000|\rho |1 - 11\rangle$ ,  $\langle 000|\rho$ $| - 111\rangle$  and  $\langle -111|\rho |1 - 11\rangle$ . Note that the last off-diagonal element is only in a two-particle superposition. Hence, it can be measured in the standard way that two-particle two-dimensional states are usually measured. To measure the other two off-diagonal elements with projective measurements, we decompose them into  $\sigma_{\mathrm{x}}$  and  $\sigma_{\mathrm{y}}$  measurements. The real and imaginary part of each element can be written as

$$
\begin{array}{l} \Re [ \langle i j k | \rho | l m n \rangle ] = \langle \sigma_ {x} ^ {\mathrm {i}, \mathrm {l}} \otimes \sigma_ {x} ^ {\mathrm {j}, \mathrm {m}} \otimes \sigma_ {x} ^ {\mathrm {k}, \mathrm {n}} \rangle - \langle \sigma_ {y} ^ {\mathrm {i}, \mathrm {l}} \otimes \sigma_ {y} ^ {\mathrm {j}, \mathrm {m}} \otimes \sigma_ {x} ^ {\mathrm {k}, \mathrm {n}} \rangle \\ - \left\langle \sigma_ {\mathrm {y}} ^ {\mathrm {l}, \mathrm {i}} \otimes \sigma_ {\mathrm {x}} ^ {\mathrm {j}, \mathrm {m}} \otimes \sigma_ {\mathrm {y}} ^ {\mathrm {k}, \mathrm {n}} \right\rangle - \left\langle \sigma_ {\mathrm {x}} ^ {\mathrm {l}, \mathrm {i}} \otimes \sigma_ {\mathrm {y}} ^ {\mathrm {j}, \mathrm {m}} \otimes \sigma_ {\mathrm {y}} ^ {\mathrm {k}, \mathrm {n}} \right\rangle \\ \end{array}
$$

$$
\begin{array}{l} \Im [ \langle i j k | \rho | l m n \rangle ] = \langle \sigma_ {y} ^ {\mathrm {i}, \mathrm {l}} \otimes \sigma_ {y} ^ {\mathrm {j}, \mathrm {i m}} \otimes \sigma_ {y} ^ {\mathrm {k}, \mathrm {n}} \rangle - \langle \sigma_ {x} ^ {\mathrm {i}, \mathrm {l}} \otimes \sigma_ {x} ^ {\mathrm {j}, \mathrm {i m}} \otimes \sigma_ {y} ^ {\mathrm {k}, \mathrm {n}} \rangle \\ - \left\langle \sigma_ {x} ^ {\mathrm {l}, \mathrm {I}} \otimes \sigma_ {y} ^ {\mathrm {j}, \mathrm {m}} \otimes \sigma_ {x} ^ {\mathrm {k}, \mathrm {n}} \right\rangle - \left\langle \sigma_ {y} ^ {\mathrm {l}, \mathrm {I}} \otimes \sigma_ {x} ^ {\mathrm {j}, \mathrm {m}} \otimes \sigma_ {x} ^ {\mathrm {k}, \mathrm {n}} \right\rangle \\ \end{array}
$$

where  $\sigma_{\mathrm{x}}^{\mathrm{a,b}} = |a\rangle \langle b| + |b\rangle \langle a|$  and  $\sigma_{\mathrm{y}}^{\mathrm{a,b}} = i|a\rangle \langle b| - i|b\rangle \langle a|$ . The  $\sigma_{x,y}$  operators are also not measurable directly with SLMs and are therefore rewritten using the following operators:

$$
\begin{array}{l} \widehat {\mathcal {P}} _ {+} (a, b) = | + \rangle \langle + | _ {(a, b)} = | a \rangle \langle a | + | b \rangle \langle b | + | a \rangle \langle b | + | b \rangle \langle a | \\ \widehat {\mathcal {P}} _ {-} (a, b) = | - \rangle \langle - | _ {(a, b)} = | a \rangle \langle a | + | b \rangle \langle b | - | a \rangle \langle b | - | b \rangle \langle a | \tag {16} \\ \end{array}
$$

$$
\widehat {\mathcal {P}} _ {+ i} (a, b) = | + i \rangle \langle + i | _ {(a, b)} = | a \rangle \langle a | + | b \rangle \langle b | - i | a \rangle \langle b | + i | b \rangle \langle a |
$$

$$
\widehat {\mathcal {P}} _ {- i} (a, b) = | - i \rangle \langle - i | _ {(a, b)} = | a \rangle \langle a | + | b \rangle \langle b | + i | a \rangle \langle b | - i | b \rangle \langle a |,
$$

where  $| + \rangle_{(a,b)} = |a\rangle + |b\rangle$ ,  $| - \rangle_{(a,b)} = |a\rangle - |b\rangle$ ,  $| + i\rangle_{(a,b)} = |a\rangle + i|b\rangle$  and  $|-i\rangle_{(a,b)} = |a\rangle - i|b\rangle$ . These superposition states can be measured with SLMs in our experiment. Thus the  $\sigma$  operators from equation 15 can be written in the following manner:

$$
\begin{array}{l} \sigma_ {\mathrm {x}} ^ {\mathrm {a}, \mathrm {b}} = \frac {1}{2} \left(\widehat {\mathcal {P}} _ {+} (a, b) - \widehat {\mathcal {P}} _ {-} (a, b)\right) \tag {17} \\ \sigma_ {y} ^ {\mathrm {a}, \mathrm {b}} = \frac {1}{2} (\widehat {\mathcal {P}} _ {- i} (a, b) - \widehat {\mathcal {P}} _ {+ i} (a, b)) \\ \end{array}
$$

This leads to 64 projection measurements required for measuring each of the two off-diagonal elements  $\langle 000|\rho |1 - 11\rangle$  and  $\langle 000|\rho | - 111\rangle$ . Only 16 projection measurements are required for the off-diagonal element  $\langle -111|\rho |1 - 11\rangle$  as it involves only one dimension for photon  $C$ . Summing up these measurements as well as the 18 diagonal elements leads to 162 total measurements. The results of these are given in Supplementary Table 1. From these measurements, the overlap between the generated state  $\rho_{\mathrm{exp}}$  and the ideal (332) state  $|\Psi \rangle$  is calculated to be  $F_{\mathrm{exp}} = 0.801\pm 0.018$ . The error in the overlap is calculated by propagating the Poissonian error in the photon-counting rates by performing a Monte Carlo simulation of the experiment.

# References

32. Vieira, A. R., Hor-Myell, M. & Khoury, A. Z. Spin-orbit mode selection with a modified Sagnac interferometer. J. Opt. Soc. Am. B 30, 1623–1626 (2013).  
33. Scheidl, T. et al. Crossed-crystal scheme for femtosecond-pulsed entangled photon generation in periodically poled potassium titanyl phosphate. Phys. Rev. A 89, 042324 (2014).  
34. Lavery, M. et al. Robust interferometer for the routing of light beams carrying orbital angular momentum. New J. Phys. 13, 093014 (2011).  
35. Mair, A., Vaziri, A., Weihs, G. & Zeilinger, A. Entanglement of the orbital angular momentum states of photons. Nature 412, 313-316 (2001).  
36. Qassim, H. et al. Limitations to the determination of a Laguerre-Gauss spectrum via projective, phase-flattening measurement. J. Opt. Soc. Am. B 31, A20-A23 (2014).  
37. Tonolini, F., Chan, S., Agnew, M., Lindsay, A. & Leach, J. Reconstructing high-dimensional two-photon entangled states via compressive sensing. Sci. Rep. 4, 6542 (2014).  
38. Händchen, V. et al. Observation of one-way Einstein-Podolsky-Rosen steering. Nature Photon. 6, 596-599 (2012).