# Generation of Hyperentangled Photon Pairs

Julio T. Barreiro, $^{1}$  Nathan K. Langford, $^{2}$  Nicholas A. Peters, $^{1}$  and Paul G. Kwiat $^{1}$

$^{1}$ Department of Physics, University of Illinois at Urbana-Champaign, Urbana, Illinois 61801-3080, USA

$^{2}$ Department of Physics, University of Queensland, Brisbane, Queensland 4072, Australia

(Received 13 July 2005; published 19 December 2005)

We experimentally demonstrate the first quantum system entangled in every degree of freedom (hyperentangled). Using pairs of photons produced in spontaneous parametric down-conversion, we verify entanglement by observing a Bell-type inequality violation in each degree of freedom: polarization, spatial mode, and time energy. We also produce and characterize maximally hyperentangled states and novel states simultaneously exhibiting both quantum and classical correlations. Finally, we report the tomography of a  $2 \times 2 \times 3 \times 3$  system (36-dimensional Hilbert space), which we believe is the first reported photonic entangled system of this size to be so characterized.

DOI: 10.1103/PhysRevLett.95.260501

Entanglement, the quintessential quantum mechanical correlations that can exist between quantum systems, plays a critical role in many important applications in quantum information processing, including the revolutionary one-way quantum computer [1], quantum cryptography [2], dense coding [3], and teleportation [4]. As a result, the ability to create, control, and manipulate entanglement has been a defining experimental goal in recent years. Higher-order entanglement has been realized in multiparticle [5] and multidimensional [6-9] systems. Furthermore, two-component quantum systems can be entangled in every degree of freedom (DOF), or hyperentangled [10]. These systems enable the implementation of  $100\%$  -efficient complete Bell-state analysis with only linear elements [11] and techniques for state purification [12]. In addition, hyperentanglement can also be interpreted as entanglement between two higher-dimensional quantum systems, offering significant advantages in quantum communication protocols (e.g., secure superdense coding [13] and cryptography [14]).

Photon pairs produced via the nonlinear optical process of spontaneous parametric down-conversion have many accessible DOF that can be exploited for the production of entanglement. This was first demonstrated using polarization [15,16], but the list expanded rapidly to include momentum (linear [17], orbital [6], and transverse [18] spatial modes), energy time [19] and time bin [20], simultaneous polarization and energy time [21], and recently, simultaneous polarization and 2-level linear momentum [22]. In this work, we produce and characterize pairs of single photons simultaneously entangled in every DOF—polarization, spatial mode, and energy time. As observed previously [6], photon pairs from a single nonlinear crystal are entangled in orbital angular momentum (OAM). Moreover, polarization entangled states can be created by coherently pumping two contiguous thin crystals [23], provided the spatial modes emitted from each crystal are indistinguishable. Finally, the pump distributes energy to the daughter photons in many ways, entangling each pair in energy; equivalently, each pair is coherently emitted over a

PACS numbers: 03.65.Ud, 03.67.Mn, 42.50.Dv, 42.65.Lm

range of times (within the coherence of the continuous wave pump). We show our two-crystal source can generate a  $(2\times 2\times 3\times 3\times 2\times 2)$ -dimensional hyperentangled state [10], approximately

$$
\underbrace {\left(| H H \rangle + | V V \rangle\right)} _ {\text {p o l a r i z a t i o n}} \otimes \underbrace {\left(| r l \rangle + \alpha | g g \rangle + | l r \rangle\right)} _ {\text {s p a t i a l m o d e s}} \otimes \underbrace {\left(| s s \rangle + | f f \rangle\right)} _ {\text {e n e r g y t i m e}}. \tag {1}
$$

Here  $H(V)$  represents the horizontal (vertical) photon polarization;  $|l\rangle$ ,  $|g\rangle$ , and  $|r\rangle$  represent the paraxial spatial modes (Laguerre-Gauss) carrying  $-\hbar$ , 0, and  $+\hbar$  OAM, respectively [24];  $\alpha$  describes the OAM spatial-mode balance prescribed by the source [25] and selected via the mode-matching conditions; and  $|s\rangle$  and  $|f\rangle$ , respectively, represent the relative early and late emission times of a pair of energy anticorrelated photons [19].

The most common maximally entangled states are the 2-qubit Bell states:  $\Phi^{\pm} = (|00\rangle \pm |11\rangle) / \sqrt{2}$  and  $\Psi^{\pm} = (|01\rangle \pm |10\rangle) / \sqrt{2}$ , in the logical basis  $|0\rangle$  and  $|1\rangle$ . By collecting only the  $\pm \hbar$  OAM state of the spatial subspace, the state (1) becomes a tensor product of three Bell states  $\Phi_{\mathrm{poln}}^{+} \otimes \Phi_{\mathrm{spa}}^{+} \otimes \Phi_{\mathrm{t - e}}^{+}$ . As a preliminary test of the hyperentanglement, we characterized the polarization and spatial-mode subspaces by measuring the entanglement (characterized by tangle  $T$  [26]), the mixture (characterized by linear entropy  $S_{L}(\rho) = \frac{4}{3}[1 - \mathrm{Tr}(\rho^{2})]$  [27]), and the fidelity  $F(\rho, \rho_{t}) \equiv (\mathrm{Tr}(\sqrt{\rho_{t}}\rho\sqrt{\rho_{t}}))^{2}$  of the measured state  $\rho$  with the target state  $\rho_{t} = |\psi_{t}\rangle \langle \psi_{t}|$ . We consistently measured high-quality states with tangles, linear entropies, and fidelities with  $\Phi^{+}$ of  $T = 0.99(1)$ ,  $S_{L} = 0.01(1)$ , and  $F = 0.99(1)$  for polarization; and  $T = 0.96(1)$ ,  $S_{L} = 0.03(1)$ , and  $F = 0.95(1)$  for spatial mode, significantly higher than earlier results [18].

The experiment is illustrated in Fig. 1. A  $120\mathrm{mW}$ $351\mathrm{nmAr^{+}}$  laser pumps two contiguous  $\beta$ -barium borate (BBO) nonlinear crystals with optic axes aligned in perpendicular planes [23]. Each  $0.6\mathrm{mm}$  thick crystal is phase matched to produce type-I degenerate photons at  $702\mathrm{nm}$

into a cone of  $3.0^{\circ}$  half-opening angle. The first (second) crystal produces pairs of horizontally (vertically) polarized photons, and these two possible down-conversion processes are coherent, provided the spatial modes emitted from each crystal are indistinguishable. With the pump focused to a waist at the crystals, this constraint can be satisfied by using thin crystals and "large" beam waists (large relative to the mismatch in the overlap of the down-conversion cones from each crystal [23]). However, the OAM entanglement is maximized by balancing the relative populations of the low-valued OAM eigenstates [25], which requires smaller beam waists to image a large area of the down-conversion cones. Here we compromise by employing an intermediate waist size ( $\sim 90~\mu \mathrm{m}$ ) at the crystal. Mode-matching lenses are then used to optimize the coupling of the rapidly diverging down-conversion modes into single-mode collection fibers.

The measurement process consists of three stages of local state projection, one for each DOF. At each stage, the target state is transformed into a state that can be discriminated from the other states with high accuracy. Specifically, computer-generated phase holograms [28] transform the target spatial mode into the pure Gaussian (or 0-OAM) mode, which is then filtered by the single-mode fiber [6] [Fig. 1(b)]. After a polarization controller to compensate for the fiber birefringence, wave plates transform the target polarization state into horizontal, which is filtered by a polarizer [Fig. 1(d)]. The analysis of the energy-time state is realized by a Franson-type [19] polarization interferometer without detection postselection [21]. The matched unbalanced interferometers give each photon a fast  $|f\rangle$  and slow  $|s\rangle$  route to its detector. Our interferometers consisted of  $L \sim 11\mathrm{mm}$  quartz birefringent elements, which longitudinally separated the horizontal and vertical polarization components by  $\Delta n_{\mathrm{quartz}} L \sim 100 \mu \mathrm{m}$ , more than the single-photon coherence length ( $\lambda^2 / \Delta \lambda \sim 50 \mu \mathrm{m}$  with  $\Delta \lambda = 10 \mathrm{~nm}$  from the interference filters) but much less than the pump-photon coherence length

![](images/ee4eb5b0258dd6ce6406794f196863e5329959000bf4dc02480befcc1b920afa.jpg)  
FIG. 1. Experimental setup for the creation and analysis of hyperentangled photons. (a) The photons, produced using adjacent nonlinear crystals (BBO), pass through a state filtration process for each DOF before coincidence detection. The measurement insets show the filtration processes as a transformation of the target state (dashed box) and a filtering step to discard the other components of the state (dotted box). (b) Spatial filtration (spa): hologram (holo) and single-mode fiber (smf). (c) Energy-time transformation  $(e - t)$ : thick quartz decoherer (dec) and liquid crystal (LC). (d) Polarization filtration (poln): quarter-wave plate (qwp), half-wave plate (hwp), and polarizer (pol).

$(\sim 10~\mathrm{cm})$  . We rely on the photons' polarization entanglement  $|HH\rangle +|VV\rangle$  to thus project onto a two-time state  $(|Hs,Hs\rangle +e^{i(\delta_1 + \delta_2)}|Vf,Vf\rangle)$  , where  $\delta_{1}$  and  $\delta_{2}$  are controlled by birefringent elements (liquid crystals and quarter-wave plates) in the path of each photon [21]. Finally, by analyzing the polarization in the  $\pm 45^{\circ}$  basis, we erase the distinguishing polarization labels and can directly measure the coherence between the  $|ss\rangle$  and  $|ff\rangle$  terms, arising from the energy-time entanglement.

To verify quantum mechanical correlations, we tested every DOF against a Clauser-Horne-Shimony-Holt (CHSH) Bell inequality [29]. The CHSH inequality places constraints  $(S \leq 2)$  on the value of the Bell parameter  $S$ , a combination of four two-particle correlation probabilities using two possible analysis settings for each photon. If  $S > 2$ , no separable quantum system (or local hidden variable theory) can explain the correlations; in this sense, a Bell inequality acts as an "entanglement witness" [30]. To measure the strongest violation for the polarization and spatial-mode DOFs, we determined the optimal measurement settings by first tomographically reconstructing the 2-qubit subspace of interest; we employ a maximum likelihood technique to identify the density matrix most consistent with the data [27].

Table I shows the Bell parameters measured for the polarization, spatial-mode, and energy-time subspaces, with various projections in the complementary DOF. We see that for every subspace, the Bell parameter exceeded the classical limit of  $S = 2$  by more than 20 standard deviations  $(\sigma)$ , verifying the hyperentanglement. For both the polarization and spatial-mode measurements, we traced over the energy-time DOF by not projecting in this subspace. We measured the polarization correlations while projecting the spatial modes into the orthogonal basis states  $(|l\rangle, |g\rangle,$  and  $|r\rangle$ ), as well as the superpositions  $|h\rangle \equiv (|l\rangle + |r\rangle) / \sqrt{2}$  and  $|v\rangle \equiv (|l\rangle - |r\rangle) / \sqrt{2}$ . The measured Bell parameters agreed (within  $\sim 2\sigma$ ) with predictions from tomographic reconstruction and violated the inequality by more than  $30\sigma$ . In the spatial-mode DOF, the corre

TABLE I. Bell parameter  $S$  showing CHSH-Bell inequality violations in every degree of freedom. The local realistic limit  $\left( {S \leq  2}\right)$  is violated by the number of standard deviations shown in brackets,determined by counting statistics.  

<table><tr><td rowspan="2">DOF</td><td rowspan="2">|gg&gt;&lt;gg|</td><td colspan="4">Spatial-mode projected subspaces</td></tr><tr><td>|rl&gt;&lt;rl|</td><td>|lr&gt;&lt;lr|</td><td>|hh&gt;&lt;hh|</td><td>|vv&gt;&lt;vv|</td></tr><tr><td>Φ+poln</td><td>2.76[76σ]</td><td>2.78[46σ]</td><td>2.75[44σ]</td><td>2.81[40σ]</td><td>2.75[33σ]</td></tr><tr><td>Φt-e</td><td>2.78[77σ]</td><td>2.80[40σ]</td><td>2.80[40σ]</td><td>2.72[30σ]</td><td>2.74[29σ]</td></tr><tr><td rowspan="2">DOF</td><td colspan="5">Polarization projected subspaces</td></tr><tr><td colspan="2">No polarizers</td><td colspan="2">|HH&gt;&lt;HH|</td><td>|VV&gt;&lt;VV|</td></tr><tr><td>Φ+spa</td><td colspan="2">2.78[78σ]</td><td colspan="2">2.80[36σ]</td><td>2.79[37σ]</td></tr><tr><td>α|gg&gt; + |rl&gt;</td><td colspan="2">2.33[55σ]</td><td colspan="2">2.30[25σ]</td><td>2.38[30σ]</td></tr><tr><td>α|gg&gt; + |lr&gt;</td><td colspan="2">2.28[47σ]</td><td colspan="2">2.26[20σ]</td><td>2.31[26σ]</td></tr></table>

relations for the state  $\Phi_{\mathrm{spa}}^{+}$  were close to maximal ( $S = 2\sqrt{2} \approx 2.83$ ), also in agreement with predictions from the measured state density matrix. In addition, we tested Bell inequalities for nonmaximally entangled states in the OAM subspace:  $\alpha |gg\rangle + |rl\rangle$  and  $\alpha |gg\rangle + |lr\rangle$ ; the measured Bell parameters in this case were slightly smaller (5%, maximum) than predictions from tomographic reconstruction [31], yet still  $20\sigma$  above the classical limit. Finally, our measured Bell violation for the energy-time DOF using particular phase settings is in good agreement with the prediction ( $S = 2\sqrt{2} V$ ) from the measured 2-photon interference visibility  $V = 0.985(2)$ .

The polarization and spatial-mode state was fully characterized via tomography [27]. We performed the 1296 linearly independent state projections required for a full reconstruction in the  $(2\otimes 3)\otimes (2\otimes 3)$  Hilbert space consisting of two polarization and three OAM modes for each photon. The measured state (Fig. 2) overlaps the anticipated state [polarization and spatial DOFs of Eq. (1)] with a fidelity of  $0.69(1)$  for  $\alpha = 1.88e^{0.16i\pi}$  (numerically fitted), and  $S_{L} = 0.46(1)$ , suggesting the difference arises mostly from mixture. Treating the photon pairs as a six-level two-particle system, we can quantify the entanglement using the negativity  $N$  [32]. In this  $6\otimes 6$  Hilbert space,  $N$  ranges from 0 (for separable states) to 5 (for maximally entangled states), and the fitted state above has  $N\approx 4.44$ . Our measured partially mixed state has  $N = 2.96(4)$ , indicating strong entanglement. The spatial mode alone has  $N = 1.14(2)$ , greater than the maximum  $(N = 1)$

![](images/18ce6b61b94f7571b801aadf1461928a3875111370880fc9c54a6e2feb074ed1.jpg)  
FIG. 2 (color online). Measured density matrix  $(\rho)$  and close pure state  $\left[|\Psi_p\rangle \sim \Phi_{\mathrm{poln}}^+\otimes \left(|lr\rangle +\alpha |gg\rangle +|rl\rangle\right)\right.$  with  $\alpha = 1.88e^{0.16i\pi}]$  of a  $(2\times 2\times 3\times 3)$ -dimensional state of 2-photon polarization and spatial mode [35].

of any two-qubit system. Thus, our large state possesses 2-qubit and 2-qutrit entanglement.

We also selected a state [neglecting the  $|gg\rangle$  component, Fig. 3(a)] maximally entangled in both polarization and spatial mode that had  $F = 0.974(1)$  with the target  $\Phi_{\mathrm{poln}}^{+}\otimes$

![](images/b8efc41662065a38ac8b3cbcf65b81a9c54ca7016c9f7eb221d12ceb16f1316f.jpg)

![](images/240899cb5c92b5f4b2c420d24597a92a2a8fb2fae5fc7b8970097e7e34558797.jpg)

![](images/aa5237fba9d812a262ec8236b0dd65b621c46ca464cbc7e79ead2279aaeb5af8.jpg)

![](images/c7b94bbd4309f50bec48ccc71fa7e86a0549212b7f247f62196730ceb6f36e12.jpg)  
FIG. 3 (color online). Measured density matrices (real parts) of  $(2 \times 2 \times 2 \times 2)$ -dimensional states of 2-photon polarization and  $(+1, -1)$ -qubit OAM [35]. For each state, we list the target state  $\rho_{t}$ , the fidelity  $F(\rho, \rho_{t})$  of the measured state  $\rho$  with the target  $\rho_{t}$ , their negativities and linear entropies, and the tangle and linear entropy for each subspace. The negativity for two-qubit states is the square root of the tangle. The magnitudes of all imaginary elements, not shown, are less than 0.03.

$\Phi_{\mathrm{spa}}^{+}$ . By tracing over polarization (spatial mode), we look at the measured state in the spatial-mode (polarization) subspaces. The reduced states in both DOFs are pure ( $S_L < 0.04$ ) and highly entangled ( $T > 0.94$ ).

With this precise source of hyperentanglement, we have the flexibility to prepare nearly arbitrary polarization states [33], and to select arbitrary spatial-mode encodings. For example, we also generated a different maximally entangled state:  $\Psi_{\mathrm{poln}}^{+} \otimes \Phi_{\mathrm{spa}}^{+}$  [Fig. 3(b)]. By coupling to and tracing over the energy-time DOF using quartz decohers [33], we can add mixture to the polarization subspace, allowing us to prepare a previously unrealized state that simultaneously displays classical correlations in polarization and maximal quantum correlations between spatial modes [Fig. 3(c)]:  $\rho \approx \frac{1}{2} (|HH\rangle \langle HH| + |VV\rangle \langle VV|)\otimes |\Phi_{\mathrm{spa}}^{+}\rangle \langle \Phi_{\mathrm{spa}}^{+}|$ . We were also able to accurately prepare the state  $\rho_{t} = \frac{1}{4} I_{\mathrm{poln}}\otimes |\Phi_{\mathrm{spa}}^{+}\rangle \langle \Phi_{\mathrm{spa}}^{+}|$ , with no polarization correlations at all (i.e., completely mixed or unpolarized), while still maintaining near maximal entanglement in the spatial DOF [Fig. 3(d)].

We report the first realization of hyperentanglement of a pair of single photons. The entanglement in each DOF is demonstrated by violations of CHSH-Bell inequalities of greater than  $20\sigma$ . Also, using tomography we fully characterize a  $2 \otimes 2 \otimes 3 \otimes 3$  state, the largest quantum system to date. In restricted  $(2 \times 2 \times 2 \times 2)$ -dimensional subspace, we prepare a range of target states with unprecedented fidelities for quantum systems of this size, including novel states with a controllable degree of correlation in the polarization subspace. These hyperentangled states enable  $100\%$  efficient Bell-state analysis [11], which is important for a variety of quantum information protocols [3,13]. Because the spatial-mode and energy-time DOFs are infinite in size, we envision examining even larger subspaces, encoding higher-dimensional quuds [7,8]. Finally, we note that the pairwise mechanism of the  $\chi^{(2)}$  down-conversion process inherently produces entanglement in photon number [34].

We thank A. G. White and T.-C. Wei for helpful discussions and the ARO/ARDA-sponsored MURI Center for Photonic Quantum Information Systems, the ARC, and the University of Queensland Foundation for support. J. T. B. acknowledges support from CONACYT-Mexico.

[1] R. Raussendorf and H. J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[2] A.K. Ekert, Phys. Rev. Lett. 67, 661 (1991).  
[3] C. H. Bennett and S. J. Wiesner, Phys. Rev. Lett. 69, 2881 (1992).  
[4] C. H. Bennett et al., Phys. Rev. Lett. 70, 1895 (1993).  
[5] Z. Zhao et al., Nature (London) 430, 54 (2004); P. Walther et al., Nature (London) 434, 169 (2005).  
[6] A. Mair, A. Vaziri, G. Weihs, and A. Zeilinger, Nature (London) 412, 313 (2001).

[7] R. T. Thew, A. Acín, H. Zbinden, and N. Gisin, Phys. Rev. Lett. 93, 010503 (2004).  
[8] M.N. O'Sullivan-Hale, I.A. Khan, R.W. Boyd, and J.C. Howell, Phys. Rev. Lett. 94, 220501 (2005).  
[9] S. Oemrawsingh et al., Phys. Rev. Lett. 95, 240501 (2005).  
[10] P.G. Kwiat, J. Mod. Opt. 44, 2173 (1997).  
[11] P.G. Kwiat and H. Weinfurter, Phys. Rev. A 58, R2623 (1998).  
[12] C. Simon and J.-W. Pan, Phys. Rev. Lett. 89, 257901 (2002).  
[13] C. Wang et al., Phys. Rev. A 71, 044305 (2005).  
[14] D. Bruss and C. Macchiavello, Phys. Rev. Lett. 88, 127901 (2002); N.J. Cerf, M. Bourennane, A. Karlsson, and N. Gisin, Phys. Rev. Lett. 88, 127902 (2002).  
[15] Z.Y. Ou and L. Mandel, Phys. Rev. Lett. 61, 50 (1988).  
[16] Y.H. Shih and C.O. Alley, Phys. Rev. Lett. 61, 2921 (1988).  
[17] J.G. Rarity and P.R. Tapster, Phys. Rev. Lett. 64, 2495 (1990).  
[18] N. Langford et al., Phys. Rev. Lett. 93, 053601 (2004).  
[19] J.D. Franson, Phys. Rev. Lett. 62, 2205 (1989).  
[20] J. Brendel, N. Gisin, W. Tittel, and H. Zbinden, Phys. Rev. Lett. 82, 2594 (1999).  
[21] D. V. Strekalov et al., Phys. Rev. A 54, R1 (1996).  
[22] T. Yang et al., Phys. Rev. Lett. 95, 240406 (2005); C. Cinelli et al., Phys. Rev. Lett. 95, 240405 (2005).  
[23] P.G. Kwiat et al., Phys. Rev. A 60, R773 (1999).  
[24] Optical Angular Momentum, edited by L. Allen, S.M. Barnett, and M.J. Padgett (IOP Publishing, Bristol, 2003).  
[25] J.P. Torres, A. Alexandrescu, and L. Torner, Phys. Rev. A 68, 050301 (2003).  
[26] W. K. Wootters, Phys. Rev. Lett. 80, 2245 (1998);  $T(\rho) = [\max \{0, \lambda_1 - \lambda_2 - \lambda_3 - \lambda_4\}]^2$ ,  $\lambda_i$  are the square roots of the eigenvalues of  $\rho(\sigma_2 \otimes \sigma_2) \rho^*(\sigma_2 \otimes \sigma_2)$  in nonincreasing order by magnitude, with

$$
\sigma_ {2} = \left( \begin{array}{c c} 0 & - i \\ i & 0 \end{array} \right).
$$

[27] D.F.V. James, P.G. Kwiat, W.J. Munro, and A.G. White, Phys. Rev. A 64, 052312 (2001).  
[28] Binary plane-wave phase gratings [24] ( $\sim 40\%$  diffraction efficiency) project the states  $|g\rangle$ ,  $|l\rangle$ ,  $|r\rangle$ , and  $\cos(\theta)|h\rangle + \sin(\theta)|v\rangle = |l\rangle + e^{i2\theta}|r\rangle$  with  $\theta = n\pi/8$ ,  $n = -1, 0, \ldots, 8$ . By displacing the holograms for  $|l\rangle$  ( $|r\rangle$ ) we project arbitrary linear combinations [6] of  $|g\rangle$  and  $|l\rangle$  ( $|r\rangle$ ).  
[29] J. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, Phys. Rev. Lett. 23, 880 (1969).  
[30] B.M. Terhal, Phys. Lett. A 271, 319 (2000).  
[31] Displaced plane-wave holograms allow a small leakage of unwanted states into the fiber [18]. This potentially explains the smaller-than-predicted Bell parameter for the nonmaximally entangled spatial-mode states [e.g.,  $S_{\mathrm{exp}} = 2.28(1)$  versus the prediction  $S_{\mathrm{pred}} = 2.35$ ].  
[32] K. Zyczkowski, P. Horodecki, A. Sanpera, and M. Lewenstein, Phys. Rev. A 58, 883 (1998).  
[33] A. G. White, D. F. V. James, W. J. Munro, and P. G. Kwiat, Phys. Rev. A 65, 012301 (2002).  
[34] H. S. Eisenberg et al., Phys. Rev. Lett. 93, 193901 (2004).  
[35] Data in Fig. 2 (Fig. 3) were collected for  $40\mathrm{~s}$ $(20\mathrm{~s})$  per projection with  $\sim 600$ $(\sim 100)$  detected pairs/s.