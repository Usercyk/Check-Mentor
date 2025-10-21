# Observation of compact localized states in synthetic Floquet-Lieb topological photonic lattices

![](images/2ee16b74e20fed4e42814a52a459bf059928f71b3d687e909985a194d5c974ff.jpg)

Check for updates

Hanfa Song, Ruoheng Zhang & Vien Van

Flat bands are unique quantum states in translationally-invariant lattices that are characterized by dispersionless energy bands and compact localized Wannier functions. In static, tight-binding systems, topologically nontrivial and gapped, perfectly flat bands require infinite hopping range, making these systems difficult to realize. By introducing periodic driving into the system, it is possible to achieve flat bands embedded in topologically nontrivial bandgaps while requiring only nearest neighbor couplings. Here we realize perfectly flat bands in a Floquet-Lieb microring lattice in which the periodic circulation of light around the rings emulates a synthetic time-like dimension. Near-infrared imaging of the scattered light allows direct observation of the compact localized state, which confirms the cyclic trajectory of the Wannier function of the flat band. In addition to a symmetry-protected flat band, the dispersive bands of the lattice can also be flattened by tuning the geometric phase of the cyclically-evolving Wannier function, leading to light localization effect which may be called Aharonov-Anandan caging. The Aharonov-Anandan phase can be directly measured from the frequency displacement of the flat-band resonance. These results suggest that flat band modes in lattices with periodic synthetic dimension could provide a versatile platform for studying novel phenomena in strongly correlated quantum systems.

Flat band states are special modes existing in certain translationally invariant lattices whose energy bands are independent of the crystal momentum. The degeneracy of the dispersionless flat bands allows compact localized states (CLS) to be constructed in real space with vanishing group velocity $^{1,2}$ . Due to their quenched kinetic energy and macroscopic degeneracy, interaction dynamics become enhanced, making flat band systems especially well-suited for investigating strongly correlated phenomena and many-body physics $^{3,4}$ . Flat bands are crucial for understanding various phenomena such as ferromagnetism $^{5,6}$ , Anderson localization $^{7,8}$ , superconductivity $^{9}$ , fractional quantum Hall effect and topological insulators $^{10,11}$ . Photonic flat bands also provide a compelling platform for studying interesting phenomena such as nonlinear caging $^{12}$ , quantum caging $^{13}$ , enhanced light-matter interaction $^{14}$ , as well as strongly interacting bosonic systems $^{15}$ , where, for example, Bose condensation is entirely driven by interactions $^{4}$ . Their unique properties have spurred much interest in designing and realizing flat bands in solid state systems $^{5,6,16,17}$ , optical lattices $^{18,19}$ , and photonics $^{20-23}$ . In addition to deepening the theoretical understanding of strongly correlated phenomena, photonic flat band systems can also have potential applications. For example, the strong light localization of flat band modes can be

used to realize high-quality factor resonators in robust programmable topological photonic circuits[24] as well as for enhanced nonlinear frequency generation[25].

In general, perfectly flat bands can arise either from interference by fine-tuning certain system parameters or from lattice symmetry $^{1,2}$ . An example of the former case is Aharonov-Bohm (AB) caging, where a real or synthetic magnetic flux threading a plaquette in the lattice is fine-tuned to achieve destructive interference of the eigenmodes, resulting in localized flat band states $^{26}$ . AB caging has been realized in various photonic systems, such as coupled waveguides and 1D microring arrays $^{27-29}$ . These systems require delicate parameter tuning, such as fine-tuning of the modulation phase in curved 3D waveguides $^{28}$  or precise positioning of auxiliary microrings in 1D microring chain $^{29}$ , and thus tend to be sensitive to parameter variations. By contrast, symmetry-protected flat bands, such as in a Lieb lattice $^{17,20,30}$ , do not require a magnetic field and are more robust to perturbations. However, since the flat band of a Lieb lattice touches the two dispersive bands at the corners of the Brillouin zone, its basis space is not restricted to just the CLS but also contains extended states $^{31}$ , so that photon caging does not always occur in a Lieb lattice. Recently, there is also growing interest in realizing flat

bands with nontrivial topological invariants $^{10,16,32}$ . These topological flat bands are important for studying strongly interacting phases of matter in topological systems, such as the fractional quantum Hall effect $^{10}$ . However, it has been shown that achieving isolated perfectly flat bands with nontrivial Chern numbers in a 2D system requires infinite hopping range $^{33,34}$ , making these lattices challenging to realize physically. We also note that techniques such as in $^{35}$  can be used to isolate the flat band of a Lieb lattice but the band remains topologically trivial.

Previously, we showed that by introducing an extra time-like synthetic dimension to a conventional Lieb lattice, it is possible to obtain a gapped and perfectly flat band with nontrivial winding number $^{36}$ . We call such a lattice a Floquet-Lieb insulator (FLI), with an effective dimension of  $(2 + 1)\mathrm{D}$ , whose evolution consists of a periodic sequence of hopping steps on a Lieb lattice. In addition to the symmetry-protected flat band at zero quasenergy, the dispersive bulk bands of the FLI can also be flattened by tuning the hopping strengths, resulting in an all-bands-flat (ABF) system. While Floquet topological insulators have been theoretically shown to host all flat bands in the atomic or perfect coupling limit $^{37,38}$ , these systems have not been experimentally demonstrated before due to the challenge of realizing lattices with near-perfect coupling $^{38}$ . In our previous study we exploited the orthogonality between the edge modes and the flat band modes to extend the topological edge mode spectrum of the FLI across the flat bands without exciting them $^{36}$ . However, since the flat band modes were not excited, the existence of compact localized states associated with the flat bands has not been experimentally confirmed. We also note that light localization caused by Floquet Defect Mode Resonance has been observed in 2D coupled microring lattices $^{39,40}$  by tuning the phase of a site ring to lift a dispersive band into a band gap. However, these resonances were defect modes rather than localized Bloch states of a translationally invariant lattice.

In this paper, we report the excitation and direct observation of compact localized states in a FLI realized on Silicon-on-Insulator (SOI). The FLI was implemented in a photonic lattice of 2D coupled microring resonators in which the circulation of light in the microrings emulates a synthetic time-like dimension. The flat band modes were excited by coupling to a topological edge mode of the lattice through two different mechanisms. In the first case, coupling between the edge mode and the zero quasienergy flat band was mediated by lattice disorder. Near-infrared (NIR) imaging of the scattered light intensity provides direct evidence of the spatial localization of the flat band modes, experimentally validating the pattern predicted by the evolution of the Wannier function of the CLS. In the second case, femtosecond laser irradiation was used to tune the coupling in an FLI lattice with all flat bands. The transmission spectrum of the edge mode shows three flat-band resonances excited in each Floquet-Brillouin zone, confirming that the lattice is an ABF system. In addition, from the displacements of the flatband resonances in the frequency domain, we could directly measure the Aharonov-Anandan (AA) phase[41] of the cyclically evolving CLS. Unlike the adiabatic Berry phase, the AA phase is a nonadiabatic geometric phase that is intimately related to the topological behavior of periodically-driven systems[42]. Its experimental determination is thus important for validating the theoretical understanding of Floquet insulators. While AA phase has been measured for a quantum harmonic oscillator implemented in a 1D photonic Glauber-Foch lattice[43], our result provides the first measurement of the AA phases of flat band modes in a Floquet topological insulator. Moreover, we show that this geometric phase is responsible for the constructive interference of the CLS after each evolution cycle, leading to light localization which may be called AA caging, since it is similar to AB caging but there is no magnetic flux threading the FLI lattice. Our work suggests that by introducing a periodic synthetic dimension to static flat band systems, we can obtain new and richer platforms for investigating photon caging and other novel phenomena associated with CLS in topologically nontrivial flatband quantum systems.

# Results

# Flat bands in a FLI microring lattice

The FLI is implemented using a coupled optical microring lattice shown in Fig. 1a, with each unit cell consisting of three identical microrings  $A$ ,  $B$  and  $C$ . Each microring is assumed to support only either a clockwise or counterclockwise propagating mode, with neighbor rings having opposite directions of light circulation. Adjacent microrings are evanescently coupled with coupling strength denoted by a coupling angle  $\theta$ , defined such that the power coupling coefficient is  $\kappa^2 = \sin^2\theta$ . We note that unlike AB caging lattices (such as in refs. 28,29), the total coupling phase around each plaquette of the FLI is zero so that there is no net magnetic flux threading the lattice. As light circulates around each microring, it periodically couples to neighbor rings so that the lattice emulates a periodically-driven system with dimension  $(2 + 1)\mathrm{D}$ , where the 1D represents a synthetic dimension taken as the coordinate  $z$  along each microring waveguide. Since light propagates in only one direction in each microring,  $z$  behaves like time with a periodicity  $L$  equal to the ring circumference. To explicitly show the driving sequence in each period, we start at the point  $z = 0$  in each microring indicated by the red mark in Fig. 1a and trace the path of light propagation around the ring while keeping track of the couplings to neighbor rings. In this manner we obtain a sequence of four coupling steps over each period, as shown in Fig. 1b. Using waveguide coupled mode theory, we can express the evolution of light in each unit cell in terms of a Schrodinger-like equation<sup>36</sup>,

$$
- i \frac {\partial}{\partial z} | \psi (\mathbf {k}, z) \rangle = [ \beta I + H _ {\mathrm {F B}} (\mathbf {k}, z) ] | \psi (\mathbf {k}, z) \rangle \tag {1}
$$

where  $|\psi \rangle = [\psi_A,\psi_B,\psi_C]^{\mathrm{T}}$  represents the fields in waveguides  $A,B$ , and  $C$  of a unit cell,  $\beta$  is the ring waveguide propagation constant,  $\mathbf{k} = (k_x,k_y)$  is the crystal momentum vector, and  $I$  is the  $3\times 3$  identity matrix. The Floquet-Bloch Hamiltonian  $H_{\mathrm{FB}}$  is given by the Hamiltonian  $H_{j}$  in each coupling step  $j\in \{1,2,3,4\}$

$$
H _ {\mathrm {F B}} (\mathbf {k}, z) = H _ {j} (\mathbf {k}), \quad (j - 1) L / 4 \leq z <   j L / 4 \tag {2}
$$

where

$$
H _ {j} (\mathbf {k}) = \left[ \begin{array}{c c c} 0 & 0 & 0 \\ 0 & 0 & k _ {\mathrm {c}} e ^ {- i s _ {j} k _ {\mathrm {x}}} \\ 0 & k _ {\mathrm {c}} e ^ {i s _ {j} k _ {\mathrm {x}}} & 0 \end{array} \right], j = 1, 3 \tag {3}
$$

$$
H _ {j} (\mathbf {k}) = \left[ \begin{array}{c c c} 0 & k _ {\mathrm {c}} e ^ {i s _ {j} k _ {y}} & 0 \\ k _ {\mathrm {c}} e ^ {- i s _ {j} k _ {y}} & 0 & 0 \\ 0 & 0 & 0 \end{array} \right], j = 2, 4,
$$

with  $k_{\mathrm{c}} = 4\theta / L$ ,  $s_j = 0$  for  $j = 1, 2$  and  $s_j = 1$  for  $j = 3, 4$ . A state in the lattice evolves as  $|\psi(\mathbf{k}, z)\rangle = \mathcal{U}(\mathbf{k}, z)|\psi(\mathbf{k}, 0)\rangle$ , with the evolution operator given by

$$
\mathcal {U} (\mathbf {k}, z) = e ^ {i \beta z} \mathcal {P} e ^ {i \int_ {0} ^ {z} H _ {\mathrm {F B}} (\mathbf {k}, z ^ {\prime}) d z ^ {\prime}} \tag {4}
$$

where  $\mathcal{P}$  is the path ordering operator which accounts for the order of the coupling steps. Over one period, the evolution is given by the Floquet operator  $U_{\mathrm{F}}(\mathbf{k}) = \mathcal{U}(\mathbf{k},L)$ . Since the Hamiltonian  $H_{j}$  in each step  $j$  is independent of  $z$ , we can define the evolution operator  $U_{j}$  over step  $j$  as  $U_{j}(\mathbf{k}) = e^{iH_{j}(\mathbf{k})L / 4}$ . The Floquet operator can then be explicitly computed as

$$
U _ {\mathrm {F}} (\mathbf {k}) = e ^ {i \beta L} e ^ {i H _ {4} (\mathbf {k}) L / 4} e ^ {i H _ {3} (\mathbf {k}) L / 4} e ^ {i H _ {2} (\mathbf {k}) L / 4} e ^ {i H _ {1} (\mathbf {k}) L / 4} \tag {5}
$$

Since the field in each microring must return to its initial position at  $z = 0$  after each roundtrip, the eigenmodes  $|\Phi_n\rangle$  of the lattice must satisfy

![](images/380a0626085726b98b219e32dc2b60c76ff4aa6690656f6ee8d6e15377c44082.jpg)  
(a)

![](images/2f329695f55c2d9ade0e8f55cc4fec03cf3259cb938e9ac60c52a5af7e4f1c11.jpg)  
(b)

![](images/a69d67cb0d5c16de6eb3880424c14479f14254f3ea0a7a66eb615dda620319b6.jpg)  
(c)

![](images/4b2a2b9aee655d30b4162cd7ebef98d0ce6e819cb44d5076b12ec2c2b34c7d51.jpg)  
(d)  
Fig. 1 | Floquet-Lieb insulator (FLI) microring lattice. a Schematic of a FLI microring lattice, with each unit cell consisting of three microrings A, B and C with coupling angle  $\theta$ . Red arrows indicate direction of light propagation in each microring. b Coupling sequence of the periodically-driven FLI lattice. The dots are microring waveguides and the red lines represent direct couplings. c Plot of the  
quasienergy spreads of the FLI lattice as function of the coupling angle  $\theta$ . The two black dots indicate degeneracy point. Yellow, red and blue dots indicate flat bands. Quasienergy band diagram of FLI lattice with (d)  $\theta = 0.45\pi$  and (e)  $\theta = 0.5\pi$ .  $W$  is the winding number of the band gap.

![](images/64801e3b7aa53cc2cf70b6217c715cb4da31ef7f10f1c6823aae21906f9758d6.jpg)  
(e)

$U_{\mathrm{F}}(\mathbf{k})|\Phi_n(\mathbf{k})\rangle = e^{i2m\pi}|\Phi_n(\mathbf{k})\rangle (m\in \mathcal{Z}),$  yielding the eigenvalue equation

$$
U _ {4} (\mathbf {k}) U _ {3} (\mathbf {k}) U _ {2} (\mathbf {k}) U _ {1} (\mathbf {k}) \left| \Phi_ {n} \right\rangle = e ^ {i \varepsilon_ {n} (\mathbf {k}) L} \left| \Phi_ {n} \right\rangle \tag {6}
$$

where  $\varepsilon_{n}(\mathbf{k}) = 2m\pi /L - \beta_{n}(\mathbf{k})$  is the quasienergy band  $n$  of the lattice. The quasienergy spectrum of the FLI thus has a periodicity of  $2\pi /L$ , which corresponds to the free spectral range (FSR) of the microrings. Over the first Floquet-Brillouin zone,  $\varepsilon \in [-\pi /L,\pi /L]$ , the lattice hosts three bands: a flat band at zero quasienergy,  $\varepsilon_0(\mathbf{k}) = 0$ , and symmetric upper and lower dispersive bands  $\varepsilon_{\pm}$  given by<sup>36</sup>

$$
\varepsilon_ {\pm} (\mathbf {k}) = \pm \left\{\pi - \cos^ {- 1} \left[ \kappa^ {4} / 2 - \tau^ {4} + \kappa^ {2} \tau \left(\cos k _ {x} + \cos k _ {y}\right) \right] \right\} / L, \tag {7}
$$

where  $\tau = \cos \theta$ . Figure 1c plots the spreads of the three quasienergy bands as function of the coupling angle  $\theta$ , with the full band structures for  $\theta = 0.45\pi$  displayed in Fig. 1d. Unlike the conventional static Lieb lattice, the quasienergy bands of the FLI lattice are fully gapped, except for the case  $\theta = 2\arctan (\sqrt{2} - 1)^{1/2} \simeq 0.36\pi$ , when the two dispersive bands become degenerate at  $(k_x, k_y) = (0, 0)$ , resulting in the closing of the gap at  $\varepsilon = \pi/L$ . This gap closing also corresponds to a topological phase transition of the lattice from a Floquet Chern insulator ( $\theta < 0.36\pi$ ) to an anomalous Floquet insulator ( $\theta > 0.36\pi$ ), which is characterized by the band gaps having nontrivial winding number ( $W = 1$ ) even though all the bands have zero Chern number[44]. It has been shown[45] that in a periodically-driven  $(2 + 1)\mathrm{D}$  system, the Chern number does not completely classify the topology of the

quasienergy bands, including the flat bands; instead, a more complete classification is given by the winding number, which takes into account the full evolution history of the system. Thus for the case  $\theta > 0.36\pi$ , although the flat band of the FLI has zero Chern number, the lattice is topologically nontrivial since the band gaps have nonzero winding number and can thus host topologically protected edge modes. When the coupling angle is tuned to  $\theta = 0.5\pi$ , which corresponds to  $100\%$  power transfer at each coupling step, the upper and lower bands also become flat with quasienergies  $\varepsilon_{\pm} = \pm 2\pi / 3L$ , so that the lattice is an ABF system, as shown in Fig. 1e. While the flat band  $\varepsilon_0$  is protected by lattice symmetry, the flat bands  $\varepsilon_{\pm}$  arise due to interference and require parameter tuning.

The appearance of the gapped flat bands can be understood by constructing a static effective Hamiltonian  $H_{\mathrm{eff}}(\mathbf{k})$  for the FLI such that  $U_{\mathrm{F}}(\mathbf{k}) = e^{i\beta L}e^{iH_{\mathrm{eff}}(\mathbf{k})L}$ . Since the Hamiltonians  $H_{j}$  in Eq. (5) do not commute, the effective Hamiltonian is not just the sum of  $H_{j}$  but also contains contributions from nested commutator terms of  $H_{j}$ ,

$$
H _ {\text {e f f}} (\mathbf {k}) = \sum_ {j = 1} ^ {4} H _ {j} + \frac {i}{2} \sum_ {j = 1} ^ {4} \sum_ {k > j} ^ {4} \left[ H _ {k}, H _ {j} \right] + \dots \tag {8}
$$

The first term on the right-hand side gives the tight-binding Hamiltonian of a conventional Lieb lattice. The infinite series of nested commutator terms gives rise to long-range hoppings which help lift the degeneracy of the bands at the corners of the Brillouin zone. In particular, for the case of perfect

coupling  $(\theta = \pi /2)$ , the effective Hamiltonian can be explicitly computed to show an effective next-nearest neighbor (NNN) coupling between rings  $A$  and  $C$ ,<sup>36</sup>

$$
H _ {\text {e f f}} (\mathbf {k}) = - \frac {2 \pi}{3 \sqrt {3}} \left[ \begin{array}{c c c} 0 & e ^ {- i k _ {x}} & - i e ^ {- i k _ {x}} e ^ {i k _ {y}} \\ e ^ {i k _ {x}} & 0 & e ^ {i k _ {y}} \\ i e ^ {i k _ {x}} e ^ {- i k _ {y}} & e ^ {- i k _ {y}} & 0 \end{array} \right] \tag {9}
$$

More generally, long-range hoppings beyond NNN can be explicit shown for all coupling angles by constructing the effective Bloch Hamiltonian for larger supercells consisting of  $N \times N$  unit cells ( $N > 1$ ). When the coupling is imperfect ( $\theta < \pi /2$ ), non-zero on-site potentials (or phase detunes) also appear on the diagonal of  $H_{\mathrm{eff}}$  although the effective Hamiltonian remains traceless. These on-site potential terms can be understood as arising from self-coupling, i.e., light in each ring coupling back to itself over each roundtrip. However, even in the presence of the on-site potentials, the lattice still maintains a flat band at zero quasienergy with two dispersive bands protected by particle-hole symmetry. It should be noted that not all hopping sequences on a Lieb lattice will produce a flat band. For example, interchanging coupling steps 2 and 3 in Fig. 1b results in all the bands being dispersive.

# Evolution of compact localized states in FLI microring lattice

The flat bands typically imply that the associated eigenstates are compact spatially-localized states, although there are exceptions such as flat bands in the presence of a DC field or nontrivial Fubini-Study quantum metric. For the ABF lattice, the CLS's belonging to the same band form a complete and orthogonal set of basis functions, which are given by

$$
\left| \Phi_ {n} (\mathbf {k}) \right\rangle = \frac {1}{\sqrt {3}} \left[ e ^ {- i \left(k _ {x} + \phi_ {n}\right)}, i e ^ {- i k _ {y}}, - e ^ {i \phi_ {n}} \right] ^ {\mathrm {T}} \tag {10}
$$

where  $\phi_n = \varepsilon_n L \in \{0, \pm 2\pi/3\}$ . Moreover, the CLS's remain localized and orthogonal to each other over the entire evolution period. This can be shown by tracking the evolution of their Wannier functions in real space. Starting at  $z = 0$ , a flat-band state  $|\Phi_n\rangle$  evolves as  $|\Psi_n(\mathbf{k}, z)\rangle = \mathcal{U}(\mathbf{k}, z)|\Phi_n(\mathbf{k})\rangle$ . The corresponding Wannier function of the  $z$ -evolved state in the home unit cell (centered at  $\mathbf{R} = [0, 0]^{\mathrm{T}}$ ) is given by<sup>42</sup>

$$
\left| w _ {n} (x, y, z) \right\rangle = \frac {a ^ {2}}{4 \pi^ {2}} \int_ {B Z} e ^ {i \mathbf {k} \cdot \mathbf {r}} \left| \Psi_ {n} (\mathbf {k}, z) \right\rangle d ^ {2} \mathbf {k} \tag {11}
$$

where  $a$  is the lattice constant. For the initial Floquet-Bloch state  $\left|\Phi_n(\mathbf{k})\right\rangle$  in Eq. (10), the Wannier function can be explicitly determined as

$$
\left| w _ {n} (x, y, 0) \right\rangle = \frac {1}{\sqrt {3}} \left[ \begin{array}{c} e ^ {- i \phi_ {n}} \delta (x - a) \delta (y) \\ i \delta (x) \delta (y - a) \\ - e ^ {i \phi_ {n}} \delta (x) \delta (y) \end{array} \right] \tag {12}
$$

or in the site basis representation,

$$
\left| w _ {n} (x, y, 0) \right\rangle = \frac {1}{\sqrt {3}} \left[ e ^ {- i \phi_ {n}} \left| A _ {1, 0} \right\rangle + i \left| B _ {0, 1} \right\rangle - e ^ {i \phi_ {n}} \left| C _ {0, 0} \right\rangle \right] \tag {13}
$$

Here  $\left|M_{p,q}\right\rangle$  indicates a state localized in ring waveguide  $M\in \{A,B,C\}$  of cell  $(p,q)$  with center located at  $\mathbf{R} = [pa,qa]^{\mathrm{T}}$ . The CLS's of the three flat bands thus consist of light localized in waveguides  $A$  of unit cell  $(1,0)$ ,  $B$  of unit cell  $(0,1)$ , and  $C$  of the home unit cell  $(0,0)$ , as shown in Fig. 2.

For the  $z$ -evolved state  $|\Psi_{n}(\mathbf{k},z)\rangle$ , the Wannier function during step 1  $(0\leq z < L / 4)$  can be expressed as (see Supplementary Note 1)

$$
\begin{array}{l} \left| w _ {n} (x, y, z) \right\rangle = \frac {e ^ {i \theta_ {n} z}}{\sqrt {3}} \left[ e ^ {- i \phi_ {n}} \left| A _ {1, 0} \right\rangle + i \left(\tau_ {z} \left| B _ {0, 1} \right\rangle + i \kappa_ {z} \left| C _ {0, 1} \right\rangle\right) \right. \tag {14} \\ \left. - e ^ {i \phi_ {n}} \left(\tau_ {z} \left| C _ {0, 0} \right\rangle + i \kappa_ {z} \left| B _ {0, 0} \right\rangle\right) \right] \\ \end{array}
$$

![](images/b8b479cb9642c00280cdce110b7939ea7652c7690a6fe4a588a043cf892e88ff.jpg)  
Fig. 2 | Evolution of compact localized states (CLS) in an all-bands-flat Floquet-Lieb insulator (FLI) microring lattice. The CLS Wannier function  $|w_{n}\rangle$  of flat-band mode  $|\Phi_n(\mathbf{k})\rangle$  consists of three components which evolve to form a complete loop over each period. The initial starting point in each ring is marked by  ${}^{\prime}0^{\prime}$ .

![](images/a4c88a0419f3a5055f1e9cb7f1667a64a91a49e609f3e117a4cb15d8c737b9c6.jpg)  
(a)

![](images/b7c257e74bfaa4384c014a812bac9fdbf1f1f68ded79c4f2e7067188236f67c6.jpg)  
(b)

![](images/de5b84be78871ead662838ae282813b430f4f5b8829535f526e2cce3b3666736.jpg)  
(c)

![](images/b97ba141742f2377565539e873a2d0344f388e6ccba224c15306162ab4a58b4b.jpg)

![](images/53d15977fa5c9578c4e0d08529467ca9fa2abdad637022aaba59ad205f7d12f4.jpg)  
(d)  
Fig. 3 | Observation of compact localized state induced by lattice disorder in a Floquet-Lieb insulator (FLI) lattice. a Optical microscope image of an FLI lattice with  $10 \times 10$  unit cells. b Transmission spectrum of edge mode along bottom lattice boundary. c Zoomed-in edge mode spectrum over one free spectral range (FSR). Top panel shows the projected quasienergy band diagram of the lattice with  $\theta = 0.45\pi$  and the edge mode dispersion (red lines) in the band gaps. d, e Near-infrared images of

![](images/fc62c30d72ebb6b3d97c9444c9283f1b919fbf1a78c195603d7421e0be6289f8.jpg)  
(e)

![](images/7af6ec5a2df33faaccff770ae0b9a92ccbe938694356f85203322e84db43477c.jpg)  
scattered light from the chip obtained at wavelengths  $\lambda_{1} = 1540.5\mathrm{nm}$  and  $\lambda_{2} = 1541.13\mathrm{nm}$ , respectively, indicated by black and blue arrows in (c). f Simulated transmission spectra of an FLI with  $\theta = 0.45\pi$  subject to various levels of coupling disorders  $\delta \theta$ . A sample of the simulated light intensity distribution in the lattice is shown in the inset of (e).  
(f)

where  $\kappa_{z} = \sin (k_{c}z)$  and  $\tau_z = \cos (k_c z)$ . Thus during step 1, light stays localized in ring  $A$  of cell (1,0) but complete power transfer occurs between rings  $B$  and  $C$  of cells (0,0) and (0,1), as illustrated in Fig. 2. The Wannier functions for the other steps are obtained in a similar manner (see Supplementary Note 1). After one complete period of evolution, the Wannier function is given by

$$
\begin{array}{l} \left| w _ {n} (x, y, L) \right\rangle = \frac {e ^ {i \beta_ {n} L}}{\sqrt {3}} \left[ \left| A _ {1, 0} \right\rangle + i e ^ {i \phi_ {n}} \left| B _ {0, 1} \right\rangle - e ^ {- i \phi_ {n}} \left| C _ {0, 0} \right\rangle \right] \tag {15} \\ = e ^ {i \left(\beta_ {n} L + \phi_ {n}\right)} | w _ {n} (x, y, 0) \rangle . \\ \end{array}
$$

Thus the CLS returns to its initial state after each period, with an accumulated roundtrip phase  $\phi_{\mathrm{rt}} = \beta_nL + \phi_n$ . The first term,  $\beta_{n}L$ , is the dynamic phase whereas the second term,  $\phi_{n}$ , is the geometric phase and can be shown to be equal to the AA phase of the periodic evolution (see Supplementary Note 2). When the total roundtrip phase  $\phi_{\mathrm{rt}} = 2m\pi$ ,  $m \in \mathcal{Z}$ , the CLS constructively interferes with itself after every period, resulting in a resonance mode at frequency  $\omega_{n} = \Omega_{m} - c\phi_{n} / (n_{\mathrm{eff}}L)$ , where  $\Omega_{m} = 2m\pi c / (n_{\mathrm{eff}}L)$  is the frequency of the resonance mode  $m$  of the microrings and  $n_{\mathrm{eff}}$  is the effective index of the ring waveguide. Thus the AA phase  $\phi_{n}$  can be measured from the displacement of the resonance frequency of the flat band  $n$  relative to the microring resonance frequency.

The complete field evolution of the CLS  $|\Phi_n\rangle$  over one period is depicted in Fig. 2. The mode comprises of three strands which evolve to form a complete loop pattern over each period. This light localization is similar to AB caging, although there is no magnetic field or synthetic gauge in the FLI lattice. We note, however, that the flat band modes at quasienergies  $\varepsilon_{\pm}$  require tuning the AA phase  $\phi_n$  by varying the coupling angle  $\theta$  to achieve constructive interference of the CLS. The resulting light localization effect may thus be called AA caging. It is also interesting to note that while it is possible to choose a single unit cell to completely contain the initial CLS  $|\Phi_n(\mathbf{k})\rangle$ , the  $z$ -evolved state  $|\Psi_n(\mathbf{k},z)\rangle$  does not stay in the same cell but visits 3 adjacent unit cells over each cycle. This behavior is not observed in

static systems, where the number of unit cells  $U$  occupied by a CLS does not change and is even used to classify flat bands $^{2,48}$ .

# Excitation and observation of compact localized states

To experimentally observe photon caging by the CLS, we fabricated FLI lattices on an SOI integrated photonics platform using the AMF Silicon Photonics foundry $^{49}$ . The SOI substrate consisted of a  $220\mathrm{-nm}$  thick silicon layer lying on a  $2 - \mu \mathrm{m}$  thick  $\mathrm{SiO}_2$  buffer layer. The microrings were formed using rib waveguides with  $500\mathrm{nm}$  core width and  $130\mathrm{-nm}$  rib height. To obtain strong evanescent coupling between neighbor rings, we designed the rings to have square shape with long side coupling length of  $18\mu \mathrm{m}$  and coupling gap of  $250\mathrm{nm}$  between neighbor rings. The corners of the square resonators were rounded with  $5\mu \mathrm{m}$  bend radius to reduce scattering loss at the corners. From numerical simulation using Lumentical software $^{50}$  we obtained a nominal coupling angle  $\theta$  of  $0.45\pi$  between neighbor rings around the  $1550\mathrm{-nm}$  wavelength, so the lattice behaves as an anomalous Floquet insulator. The fabricated lattices consisted of  $10\times 10$  unit cells.

We used a topological edge mode of the lattice to couple light into the flat-band modes at the degenerate frequencies where the edge mode dispersion line intersects the flat bands. To excite an edge mode along the bottom boundary of the lattice, we coupled an input waveguide to the ring at the bottom left corner of the lattice, as shown in Fig. 3a. An output waveguide coupled to the ring at the bottom right corner was used to measure the transmitted light. Since the edge mode and flat-band modes are orthogonal to each other at the degenerate frequencies<sup>36</sup>, it is necessary to introduce coupling perturbations to the lattice in order to mediate the coupling between the two modes. We observed excitation of the flat-band modes under two scenarios. In the first case, coupling between the flat-band mode and the edge mode was induced by lattice disorder. In the second case, we intentionally introduced coupling perturbation between the flat band and edge modes by femtosecond laser irradiation. Observation of flat-band modes in each case is described below.

Observation of disorder-induced CLS in FLI microring lattice. In the presence of sufficiently large defects in the FLI lattice, the orthogonality between the edge modes and flat-band modes at the degenerate frequencies can be destroyed, allowing for excitation of the flat-band mode from the edge mode. This was observed in the sample in Fig. 3a. Figure 3b shows the measured edge mode transmission spectrum over the wavelength range  $1515 - 1545\mathrm{nm}$  (see Methods section for measurement setup). Over each FSR of about  $5.6\mathrm{nm}$ , the spectrum exhibits a central band of high transmission sandwiched between two stop-bands corresponding to the two dispersive bulk bands. The central transmission band can be identified as the two nontrivial band gaps above and below the zero quasienergy flat band, as shown by the projected band diagram in Fig. 3c. The nontrivial band gaps host topologically-protected edge modes, which have been shown to be immune to defects along the lattice boundaries[51]. At the center of the transmission band we observe a sharp transmission dip, indicating that a flat-band mode at the zero quasienergy was excited. To verify the origin of this resonance dip, we performed NIR imaging of the scattered light intensity at the two wavelengths indicated by the arrows in Fig. 3c. At the  $1540.5\mathrm{nm}$  wavelength (black arrow) in the band gap where the transmission is high, the NIR image in Fig. 3d shows light localized along the bottom boundary of the lattice, indicating the excitation and propagation of the edge mode. When the wavelength was tuned to the resonance dip at  $1541.13\mathrm{nm}$  (blue arrow), the NIR image in Fig. 3e shows light localized in a loop around the third unit cell from the bottom left corner. This spatial localization pattern matches well with the trajectory of the Wannier state of the CLS over an evolution period depicted in Fig. 2. The 3-dB linewidth of the transmission dip at  $1541.13\mathrm{nm}$  was measured to be  $0.03\mathrm{nm}$ , yielding a quality factor of  $5.1\times 10^4$  for the flat-band resonance mode.

The excitation of the flat-band mode can be attributed to the presence of sufficiently large defects around the third unit cell that help break the orthogonality between the edge mode and flat-band mode, causing light to couple into the resonance mode. To verify this, we performed Monte-Carlo simulations of a  $10 \times 10$  FLI microring lattice with nominal coupling angle  $\theta = 0.45\pi$  subject to uniformly-distributed random variations  $\delta \theta$  in the coupling angles of the third unit cell from the bottom left corner (see ref. 36 for simulation method). A nominal silicon waveguide loss of  $3\mathrm{dB/cm}$  was also assumed for the lattice. Figure 3f plots the average transmission spectra of 1000 simulations for coupling disorders  $|\delta \theta/\theta| \leq 1\%$ ,  $3\%$ ,  $5\%$  and  $7\%$ . We observe a transmission dip at the zero quasienergy (microring resonance wavelength) which becomes broader as the coupling disorder is increased. A sample light intensity distribution in the lattice obtained at the miroring resonance wavelength for disorder  $|\delta \theta/\theta| \leq 7\%$  is shown in the inset of Fig. 3e. Light is seen to be localized in a loop pattern in agreement with the NIR image of the flat-band mode, thus confirming that the CLS was excited due to lattice disorder.

Excitation of flat-band mode by femtosecond laser tuning of coupling angle. Instead of relying on random lattice disorder, it is possible to excite a flat-band mode in the FLI lattice by perturbing a coupling junction shared by the edge mode and the flat-band mode. This allows a CLS to be excited at a specific location in the lattice, which could be useful for investigating novel phenomena associated with localized states, as well as potential applications such as realizing high-Q resonators in robust programmable topological photonic circuits[24]. Here we introduce controllable coupling perturbation to the lattice using fs laser irradiation, which has been shown to be an effective method for post-fabrication tuning of silicon photonic devices[52,53]. Femtosecond laser pulses at fluences below the ablation threshold can modify the local crystalline structure of silicon, leading to a permanent increase in its refractive index[52,53]. By irradiating the waveguide coupler between two adjacent microrings in the FLI lattice with 130-fs laser pulses at  $800\mathrm{nm}$  wavelength, we can induce a permanent change in the coupling angle, allowing light to be coupled into the flat-band mode from the edge mode. The coupling angle can also be tuned by varying the laser fluence. The

experimental setup for performing fs irradiation of the lattice is described in the Methods section.

The FLI lattice used in this experiment had the same design parameters as the device in Fig. 3a, except that it was also covered by a  $2 - \mu \mathrm{m}$  thick oxide cladding. The presence of the oxide cladding increases the coupling strength between adjacent microrings so that the coupling angle is close to  $0.5\pi$ , making the lattice an ABF system. This can be verified from the measured edge mode transmission spectrum in Fig. 4b (red trace), which shows a wide region of high and flat transmission spanning 7 FSRs from 1515 to  $1555~\mathrm{nm}$ . The absence of transmission dips within this wavelength range indicates that no bulk modes were excited, since the edge mode is orthogonal to all the flat bands<sup>36</sup>. To excite a flat-band mode at the second unit cell from the bottom left corner, we irradiated the coupling junction between rings  $B$  and  $C$  of the unit cell, which is shared by both the edge mode and the flat-band mode, as indicated in Fig. 4a. We monitored the effect of the fs laser irradiation by measuring the edge mode transmission spectrum after each laser shot. The spectra obtained are also plotted in Fig. 4b. For laser fluences below  $20\mathrm{mJ} / \mathrm{cm}^2$ , no noticeable changes in the transmission spectrum were observed, as shown by the green trace. However, when the fluence was increased to  $27\mathrm{mJ} / \mathrm{cm}^2$ , small transmission dips began to emerge, as shown by the brown and black traces. A further shot at  $33\mathrm{mJ} / \mathrm{cm}^2$  caused the dips to become prominent (blue trace), indicating stronger light coupling into the flat-band modes. The transmission spectrum shows three resonance dips in each FSR, which correspond to the three flat band modes excited in each Floquet-Brillouin zone. To verify this behavior we simulated the transmission spectrum of a  $10\times 10$  FLI lattice with coupling angle  $\theta = \pi /2$  and nominal silicon waveguide loss of  $3\mathrm{dB / cm}$ . By tuning the coupling angle of the irradiated waveguide coupler to  $\theta = 0.25\pi$  and increasing the roundtrip field attenuation in the irradiated rings to  $a_{\mathrm{rt}} = 0.95$  to account for the extra loss due to laser irradiation<sup>52</sup>, we obtained a relatively good fit between the simulated and measured edge mode spectra, as shown in Fig. 4c. We note that the simulation did not take into account lattice disorder, which may cause the linewidths of the measured transmission dips to be slightly broader than the simulated spectrum. The simulation result confirms that the transmission dips in the edge mode spectrum were caused by the coupling perturbation induced by fs laser irradiation, allowing light to couple from the edge mode into the flat-band modes.

From the resonance frequencies of the excited flat band modes we can determine the AA phase of the CLS acquired over a period of evolution. Over each FSR in the 1515-1550 nm wavelength range, we measured the resonance frequency shift  $\Delta \omega_{n} = \omega_{n} - \omega_{2}$ ,  $n = 1, 2, 3$  of each mode  $n$  relative to the center resonance at  $\omega_{2}$ . The AA phase shift of mode  $n$  is calculated from  $\phi_{n} = 2\pi \times \Delta \omega_{n} / \Delta \omega_{\mathrm{FSR}}$ , where  $\Delta \omega_{\mathrm{FSR}}$  is the FSR frequency. The AA phase for each mode is plotted vs. the resonance wavelength  $\lambda_{n}$  in Fig. 5, which shows a relative constant phase shift for each mode over the six FSRs. The average AA phase is calculated to be  $-0.66\pi \pm 0.01\pi$  for mode  $n = 1$  and  $0.667\pi \pm 0.008\pi$  for mode  $n = 3$ . These values are in excellent agreement with the theoretical AA phase  $\phi_{n} = \pm 2\pi / 3$  of the CLS in the FLI lattice, providing further evidence of the geometric origin of the flat band resonances and the observed AA caging effect.

# Conclusion

We report the realization of flat bands in FLI microring lattices in which the internal circulation of light around the microrings emulates a periodic synthetic dimension. The periodic driving sequence of the FLI gives rise to long-range couplings, resulting in isolated and perfectly flat bands embedded in topologically nontrivial bandgaps. In addition to the symmetry-protected flat band at zero quasienergy, the two dispersive bulk bands of the FLI can also be flattened by tuning the AA phase of the corresponding CLS's, resulting in light localization which may be called AA caging. We observed excitation of the flat band modes by lattice disorder and by fs laser irradiation. NIR imaging of the scattered light distribution from the lattice showed CLS localized in a loop pattern, in agreement with the theoretically predicted trajectory of the Wannier function. The quasienergy spectra of the flat bands were also shown to be strongly localized in the

![](images/51fb0cea049d2483ac4743f5c152ae2d640d61e84d11240080cc52c04969c51d.jpg)

![](images/593e24224c68510674e6595fd74404396896f8aa418ded1939c92c0dfae85ff6.jpg)  
Fig. 4 | Observation of flat band modes in a Floquet-Lieb insulator (FLI) induced by femtosecond laser irradiation. a Schematic and optical microscope image of FLI lattice showing location of coupling junction irradiated by fs laser pulses (metal lines on the sample were not used in this experiment). Inset shows a scanning electron microscope image of the irradiated coupling junction. b Edge mode transmission  
spectra measured after each laser pulse with increasing fluence. Spectra are offset vertically for clarity. c Measured (blue) and simulated (red) edge mode spectra of an FLI lattice with  $10 \times 10$  unit cells, coupling angle  $\theta = 0.5\pi$  after irradiation with  $33\mathrm{mJ} / \mathrm{cm}^2$  laser pulse. In the simulation the irradiated coupling angle was tuned to  $\theta = 0.25\pi$  and the roundtrip field attenuation of the irradiated rings was set to  $a_{\mathrm{rt}} = 0.95$ .

![](images/3155308955cbf18d0e566a4ed7659f5ba538669e98d27368cd95d1450c662c69.jpg)  
Fig. 5 | Aharonov-Anandan (AA) phases of the Compact Localized States (CLS) in an all-bands-flat Floquet-Lieb microring lattice. The extracted AA phase  $\phi_{n}$  of each CLS mode  $n = 1,2,3$  is plotted as a function of the flat band resonance wavelength  $\lambda_{n}$ .

frequency domain, and the displacements of their resonance frequencies from the microring resonances allowed us to directly measure the AA phases of the CLS's. Our work could open up new avenues for investigating novel phenomena associated with flat-band states in 2D systems with periodic synthetic dimension.

# Methods

# Experimental setup for measurement and NIR imaging of the FLI lattices

In the measurement setup, light from a tunable laser was set to the TE polarization using a polarization controller and butt-coupled to the input waveguide through a lensed fiber. The transmitted light in the output waveguide was collected by another lensed fiber and detected with an InGaAs photodetector and a power meter. The coupling loss between the lensed fiber and the silicon waveguide was estimated to be about  $7.5\mathrm{dB}$  giving a total input and output coupling loss of  $15\mathrm{dB}$ . This loss was subtracted from the measured transmitted power, and the result was normalized by the laser input power. To image the scattered light intensity

![](images/afbf5feedf24fa2fc159bd5b9de32e3895545881b69c21d1e54e74e8e8c634d9.jpg)  
Fig. 6 | Experimental setup of the femtosecond laser irradiation system. The silicon chip is mounted on the 3D stage. Light pulses at  $800\mathrm{nm}$  wavelength from the femtosecond laser (red line) are controlled by a shutter and focused on the chip through a 10X microscope objective (M1, M2 are high-reflection dielectric mirrors at  $800\mathrm{nm}$ ; BS1, BS2, BS3 are beam splitters). A light emitted diode (LED) at  $532\mathrm{nm}$  (green line) is used to illuminate the chip and the reflected light imaged by a CCD camera to perform alignment. A broadband light source is coupled to the input waveguide of the device via a lensed fiber and the transmitted light collected from the output waveguide for measurement of the device's transmission spectrum with the Optical Spectrum Analyzer (OSA).

distribution from the sample, we used an NIR camera (Sensor Unlimited SU320M) to image the lattice from above via a  $20\times$  objective lens.

# Experimental setup for femtosecond laser irradiation

A schematic of the experimental setup for fs irradiation of silicon waveguides is shown in Fig. 6. A Ti:sapphire fs laser (Coherent Legend) was used to generate laser pulses at  $800\mathrm{nm}$  wavelength with a repetition rate of  $1\mathrm{kHz}$  and pulse duration of around 130 fs. The number of pulses for irradiation was controlled using a combination of a fast electric shutter and a delay generator to generate a specified number of shots. The laser fluence was controlled with a combination of a glan-polarizer and a halfwave plate and calibrated using a photodiode (PD) placed before the electric shutter. The FLI sample was mounted on a 3D motion stage with a resolution of  $200\mathrm{nm}$ . The laser beam was focused with a  $10\times$  microscope objective lens illuminating the sample vertically. The Gaussian beam profile was measured to have a radius of  $13\mu \mathrm{m}$  at the sample surface. An LED light source at  $532\mathrm{nm}$  wavelength was used to illuminate the sample surface and the image was captured with a CCD camera and a  $100\mathrm{cm}$  focal length achromatic lens for visualization and alignment of the sample. For in-situ monitoring of the spectral response of the device after each fs laser shot, broadband light source from a Superluminescent LED was butt-coupled to the input waveguide of the FLI lattice and the transmitted light in the output waveguide was measured using an Optical Spectrum Analyzer (OSA).

# Data availability

Data for Fig. 3b, f are provided in Supplementary Dataset 1. Data for Fig. 4b, c are provided in Supplementary Dataset 2. Data for Fig. 5 are provided in Supplementary Dataset 3.

# Code availability

All relevant code used in this study is available from the corresponding authors upon reasonable request.

Received: 11 December 2024; Accepted: 13 May 2025; Published online: 27 May 2025

# References

1. Aoki, H., Ando, M. & Matsumura, H. Hofstadter butterflies for flat bands. Phy. Rev. B 54, 296-299 (1996).  
2. Leykam, D., Andreanov, A. & Flach, S. Artificial flat band systems: from lattice models to experiments. Adv. Phys. X 3, 1473052 (2018).

3. Balents, L., Dean, C. R., Efetov, D. K. & Young, A. F. Superconductivity and strong correlations in moiré flat bands. Nat. Phys. 16, 725-733 (2020).  
4. Huber, S. D. & Altman, E. Bose condensation in flat bands. Phys. Rev. B 82, 184502 (2010).  
5. Tasaki, H. Ferromagnetism in the Hubbard models with degenerate single-electron ground states. Phys. Rev. Lett. 69, 1608-1612 (1992).  
6. Lin, Z. et al. Flatbands and emergent ferromagnetic ordering in Fe3Sn2 Kagome lattices. Phys. Rev. Lett. 121, 096401 (2018).  
7. Goda, M., Nishino, S. & Matsuda, H. Inverse Anderson transition caused by flatbands. Phys. Rev. Lett. 96, 126401 (2006).  
8. Chalker, J. T., Pickles, T. S. & Shukla, P. Anderson localization in tight-binding models with flat bands. Phys. Rev. B 82, 104209 (2010).  
9. Kauppila, V. J., Aikebaier, F. & Heikkilä, T. T. Flat-band superconductivity in strained Dirac materials. Phys. Rev. B 93, 214505 (2016).  
10. Tang, E., Mei, J.-W. & Wen, X.-G. High-temperature fractional quantum Hall states. Phys. Rev. Lett. 106, 236802 (2011).  
11. Wang, Y.-F., Gu, Z.-C., Gong, C.-D. & Sheng, D. N. Fractional quantum hall effect of hard-core bosons in topological flat bands. Phys. Rev. Lett. 107, 146803 (2011).  
12. Danieli, C., Andreanov, A., Mithun, T. & Flach, S. Nonlinear caging in all-bands-flat lattices. Phys. Rev. B 104, 085131 (2021).  
13. Danieli, C., Andreanov, A., Mithun, T. & Flach, S. Quantum caging in interacting many-body all-bands-flat lattices. Phys. Rev. B 104, 085132 (2021).  
14. Yang, Y. et al. Photonic flatband resonances for free-electron radiation. Nature 613, 42-47 (2023).  
15. Grygiel, B. & Patucha, K. Excitation spectra of strongly interacting bosons in the flat-band lieb lattice. Phys. Rev. B 106, 224514 (2022).  
16. Sun, K., Gu, Z., Katsura, H. & Das Sarma, S. Nearly flatbands with nontrivial topology. Phys. Rev. Lett. 106, 236803 (2011).  
17. Slot, M. R. et al. Experimental realization and characterization of an electronic Lieb lattice. Nat. Phys. 13, 672-677 (2017).  
18. Wu, C., Bergman, D., Balents, L. & Das Sarma, S. Flat bands and Wigner crystallization in the honeycomb optical lattice. Phys. Rev. Lett. 99, 070401 (2007).  
19. Drost, R., Ojanen, T., Harju, A. & Liljeroth, P. Topological states in engineered atomic lattices. Nat. Phys. 13, 668-672 (2017).  
20. Vicencio, R. A. et al. Observation of localized states in Lieb photonic lattices. Phys. Rev. Lett. 114, 245503 (2015).

21. Longhi, S. Aharonov-Bohm photonic cages in waveguide and coupled resonator lattices by synthetic magnetic fields. Opt. Lett. 39, 5892-5895 (2014).  
22. Mukherjee, S. & Thomson, R. R. Observation of robust flat-band localization in driven photonic rhombic lattices. Opt. Lett. 42, 2243-2246 (2017).  
23. Tang, L. et al. Photonic flat-band lattices and unconventional light localization. *Nanophotonics* 9, 1161-1176 (2020).  
24. Song, H., Zimmerling, T. & Van, V. Robust programmable photonic circuits based on a Floquet-Lieb topological waveguide lattice. IEEE Photonics J. 15, 4601107 (2023).  
25. Zimmerling, T. J., Afzal, S. & Van, V. Broadband resonance-enhanced frequency generation by four-wave mixing in a silicon floquet topological photonic insulator. APL Photonics 7, 056104 (2022).  
26. Vidal, J., Mosseri, R. & Doucot, B. Aharonov-Bohm cages in two-dimensional structures. Phys. Rev. Lett. 81, 5888-5891 (1998).  
27. Cáceres-Aravena, G., Guzmán-Silva, D., Salinas, I. & Vicencio, R. A. Controlled transport based on multiorbital Aharonov-Bohm photonic caging. Phys. Rev. Lett. 128, 256602 (2022).  
28. Mukherjee, S., Di Liberto, M., Öhberg, P., Thomson, R. R. & Goldman, N. Experimental observation of Aharonov-Bohm cages in photonic lattices. Phys. Rev. Lett. 121, 075502 (2018).  
29. Chen, S. et al. On-chip photonic localization in Aharonov-Bohm cages composed of microring lattices. Nano Letters 24, 4810-4815 (2024).  
30. Mukherjee, S. et al. Observation of a localized flat-band state in a photonic Lieb lattice. Phys. Rev. Lett. 114, 245504 (2015).  
31. Bergman, D. L., Wu, C. W. & Balents, L. Band touching from real-space topology in frustrated hopping models. Phys. Rev. B 78, 125104 (2008).  
32. Parameswarana, S. A., Roy, R. & Sondhi, S. L. Fractional quantum Hall physics in topological flat bands. Comptes Rendus Physique 14, 816-839 (2013).  
33. Chen, L., Mazaheri, T., Seidel, A. & Tang, X. The impossibility of exactly flat non-trivial Chern bands in strictly local periodic tight binding models. J. Phys. A Math. Theor. 47, 152001 (2014).  
34. Lee, C. H., Arovas, D. P. & Thomale, R. Band flatness optimization through complex analysis. Phys. Rev. B 93, 155155 (2016).  
35. Bae, J.-H. B., Sedrakyan, T. & Maiti, S. Isolated flat bands in 2D lattices based on a novel path-exchange symmetry. SciPost Phys. 15, 139 (2023).  
36. Song, H., Zimmerling, T. J., Leng, B. & Van, V. Wide edge state supercontinuum in a Floquet-Lieb topological photonic insulator. APL Photonics 8, 106102 (2023).  
37. Kitagawa, T., Berg, E., Rudner, M. & Demler, E. Topological characterization of periodically driven quantum systems. Phys. Rev. B. 82, 235114 (2010).  
38. Mukherjee, S. et al. Experimental observation of anomalous topological edge modes in a slowly driven photonic lattice. Nat. Commun. 8, 13918 (2017).  
39. Afzal, S. & Van, V. Trapping light in a Floquet topological photonic insulator by floquet defect mode resonance. APL Photonics 6, 116101 (2021).  
40. Zimmerling, T. J., Afzal, S. & Van, V. Broadband resonance-enhanced frequency generation by four-wave mixing in a silicon Floquet topological photonic insulator. APL Photonics 7, 056104 (2022).  
41. Aharonov, Y. & Anandan, J. Phase change during a cyclic quantum evolution. Phys. Rev. Lett. 58, 1593 (1987).  
42. Nakagawa, M., Slager, R.-J., Higashikawa, S. & Oka, T. Wannier representation of Floquet topological states. Phys. Rev. B 101, 075108 (2020).

43. Wang, K., Weimann, S., Nolte, S., Perez-Leija, A. & Szameit, A. Measuring the Aharonov-Anandan phase in multiport photonic systems. Opt. Lett. 41, 1889-1892 (2016).  
44. Afzal, S. & Van, V. Topological phases and the bulk-edge correspondence in 2D photonic microring resonator lattices. Opt. Express 26, 14567-14577 (2018).  
45. Rudner, M. S., Lindner, N. H., Berg, E. & Levin, M. Anomalous edge states and the bulk-edge correspondence for periodically driven two-dimensional systems. Phys. Rev. X 3, 031005 (2013).  
46. Mallick, A., Chang, N., Maimaiti, W., Flach, S. & Andreanov, A. Wannier-stark flatbands in bravais lattices. Phys. Rev. Res. 3, 013174 (2021).  
47. Hofmann, J. S., Berg, E. & Chowdhury, D. Superconductivity, charge density wave, and supersolidity in flat bands with a tunable quantum metric. Phys. Rev. Lett. 130, 226001 (2023).  
48. Flach, S., Leykam, D., Bodyfelt, J. D., Matthies, P. & Desyatnikov, A. S. Detangling flat bands into Fano lattices. *Europhys. Lett.* 105, 30001 (2014).  
49. www.advmf.com.  
50. https://www.lumerical.com/products/.  
51. Dai, T. et al. Topologically protected quantum entanglement emitters. Nat. Photon. 16, 248-257 (2022).  
52. Bachman, D. et al. Femtosecond laser tuning of silicon microring resonators. Opt. Lett. 36, 4695-4697 (2011).  
53. Zhang, R. et al. Multi-shot near-infrared femtosecond laser tuning of silicon microring resonators. Opt. Commun. 560, 130446 (2024).

# Acknowledgements

This work was supported by the Canadian Microelectronics Corporation, Alberta Innovates, and the Natural Sciences and Engineering Research Council of Canada.

# Author contributions

H. Song performed modeling, numerical simulations, and data analyses of FLI devices. R.Zhang built the femtosecond laser irradiation system. H. Song performed transmission measurements and NIR imaging of the chips. H. Song and R. Zhang performed the femtosecond laser irradiation and transmission measurements of the chips. H. Song and V. Van wrote the paper, with contributions from all the authors.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s42005-025-02138-6.

Correspondence and requests for materials should be addressed to Vien Van.

Peer review information Communications Physics thanks Alexei Andreanov, Bing Wang and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at

http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025