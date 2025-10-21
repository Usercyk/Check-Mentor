https://doi.org/10.1038/s41467-021-22264-3

OPEN

# Topological protection versus degree of entanglement of two-photon light in photonic topological insulators

Konrad Tschernig  $^{1,2\boxtimes}$ , Álvaro Jimenez-Galán<sup>1</sup>, Demetrios N. Christodoulides  $^{3}$ , Misha Ivanov  $^{1,2,4}$ , Kurt Busch<sup>1,2</sup>, Miguel A. Bandres<sup>3 $\boxtimes$ </sup> & Armando Perez-Leija  $^{1,2\boxtimes}$

Topological insulators combine insulating properties in the bulk with scattering-free transport along edges, supporting dissipationless unidirectional energy and information flow even in the presence of defects and disorder. The feasibility of engineering quantum Hamiltonians with photonic tools, combined with the availability of entangled photons, raises the intriguing possibility of employing topologically protected entangled states in optical quantum computing and information processing. However, while two-photon states built as a product of two topologically protected single-photon states inherit full protection from their single-photon "parents", a high degree of non-separability may lead to rapid deterioration of the two-photon states after propagation through disorder. In this work, we identify physical mechanisms which contribute to the vulnerability of entangled states in topological photonic lattices. Further, we show that in order to maximize entanglement without sacrificing topological protection, the joint spectral correlation map of two-photon states must fit inside a well-defined topological window of protection.

The prospect of generating topologically protected entangled states of several photons is a highly intriguing proposition<sup>1-3</sup>. Specifically, topological protection can enable robust transport of quantum information across disordered photonic structures without degradation<sup>4,5</sup>, just as efficiently as for single-particle wavepackets<sup>6-10</sup>.

In recent years, we have witnessed several experimental demonstrations of topological protection at the single-photon level in integrated one-dimensional lattice systems. Notably, Wang and co-workers[11] showed that the fundamental quantum features of spatially entangled biphoton-states can be protected against disorder in the so-called Su-Schrieffer-Heeger (SSH) topological lattice. Interestingly, SSH lattices turned out to be equally effective in protecting polarization-entangled photon pairs[12]. Another important ingredient was provided by Tambasco et al.[13] showing that Hong-Ou-Mandel two-photon interference of topological edge-modes is feasible, by implementing a topological beamsplitter in a judiciously engineered time-dependent Harper-model.

Concurrently, on the theory front several ideas have been suggested to investigate topological two-photon effects in linear $^{14,15}$  and nonlinear $^{16}$  lattice systems. In this regard, an intriguing proposition was recently put forward $^{17}$ , where the Bose-Hubbard model, which is topologically trivial for single particles, becomes topologically nontrivial for two interacting photons. That is, particle interactions have a dramatic impact on topological properties, not only modifying the topology of the spectra but also creating a topological order in otherwise topologically trivial systems.

In order to maximize the potential of topological photonic networks for transferring quantum information, it is indispensable to have a considerable number of edge modes at our disposal. One possibility is to use two-dimensional topological systems, which intrinsically support a multitude of topological edge-states $^{18-20}$ .

In two-dimensional photonic topological insulators, single-particle edge-states reside in the gap existing between the energy bands supporting the bulk states[21-23]. Thus, breaking the topological protection requires disorder with sufficient strength to close the bandgap. For states describing two indistinguishable photons, the same bandgap is fundamentally lacking. The reason is because the propagation eigenvalues  $\lambda_{12}^{(2)}$  for two-photon eigenstates in a photonic system are given by the sum of the eigenvalues  $\lambda_1,\lambda_2$  corresponding to the constituent individual photons,  $\lambda_{12}^{(2)} = \lambda_1 + \lambda_2$ . This implies that we can keep  $\lambda_{12}^{(2)}$  constant while increasing  $\lambda_{1}$  and simultaneously decreasing  $\lambda_{2}$ , or vice versa. In this way, we can combine two single-photon bulk states, one from the lower and one from the upper band, to create a biphoton bulk-bulk state whose energy lies inside the single-particle bandgap. This fundamental additive property of the single-particle eigenvalues removes the bandgap and leads to massive degeneracies of the edge-edge, edge-bulk, and bulk-bulk two-photon states. Hence, considering the lack of the topological bandgap for two-photon systems, it is not clear whether topological protection will be automatically granted to two-particle states provided single particles are topologically protected in the same system.

In solids, the degeneracies described above lead to the decay of two-electron edge states when electron-electron correlations are substantial[24-26]. This decay mechanism is reminiscent of auto-ionization, where electron-electron correlations lead to energy exchange between the two particles, coupling two bound electronic excitations to an energy-degenerate bound-continuum two-electron state[27,28].

Still, photonic systems are fundamentally different from solids, as the two photons do not readily interact with each other[29].

Consequently, the evolution operator for two-photon states,  $U^{(2)}(z)$ , breaks down into the product of two propagators for individual single-photon states,  $U^{(2)}(z) = U(z) \otimes U(z)^{30}$ . Thus, a natural question to ask is whether such a factorization and the absence of bangap will prevent decoherence and dissipation of non-factorizable two-photon edge-states into the bulk?

In this work, we analyze possible mechanisms of dissipation of two-photon edge states into the bulk of two different topological insulator system, the Haldane lattice model and an aperiodic lattice corresponding to the quantum Hall effect. Our results show that the key to topological protection is to minimize the disorder-induced overlap of the initial two-photon (joint) spectrum with the edge-bulk and bulk-bulk spectral regions.

# Results

Theoretical approach. In lattice systems, static disorder can be introduced in either the site energies—termed diagonal disorder<sup>31</sup> or in the coupling coefficients—so-called off-diagonal disorder<sup>32</sup>. In either case, static disorder is represented by a single-particle operator  $\hat{V}^{(1)}$ . Since such perturbation is time-independent, energy conserving resonant coupling into the bulk is absent within first-order perturbation theory—the single-particle transition induced by  $\hat{V}^{(1)}$  does not preserve energy. The process that can resonantly couple a two-photon edge-edge state to a bulk-bulk, or to a bulk-edge, state would require a correlated change of states for both photons and it might arise within the second-order corrections in  $\hat{V}^{(1)}$ .

To see this, we examine the second-order transition matrix elements between an initial two-photon edge-edge state  $|\mathrm{i}\rangle = |n_{\mathrm{i}},m_{\mathrm{i}}\rangle$  and a final edge-bulk, or bulk-bulk, state  $|\mathrm{f}\rangle = |n_{\mathrm{f}},m_{\mathrm{f}}\rangle$

$$
V _ {\mathrm {i}, \mathrm {f}} ^ {(2)} = \sum_ {j ^ {\prime}} \frac {V _ {\mathrm {f} j ^ {\prime}} ^ {(1)} V _ {j ^ {\prime} \mathrm {i}} ^ {(1)}}{\lambda_ {j ^ {\prime}} ^ {(2)} - \lambda_ {\mathrm {i}} ^ {(2)}}, \tag {1}
$$

where  $|j^{\prime}\rangle = |n^{\prime},m^{\prime}\rangle$  labels intermediate virtual states and  $\lambda_{j^{\prime}}^{(2)} = \lambda_{n^{\prime}} + \lambda_{m^{\prime}}$ . The single-particle nature of  $\hat{V}^{(1)}$  ensures that only two terms corresponding to the two possible time-orderings of the two single-particle transitions are left in the sum

$$
V _ {\mathrm {i}, \mathrm {f}} ^ {(2)} = V _ {n _ {\mathrm {f}}, n _ {\mathrm {i}}} ^ {(1)} V _ {m _ {\mathrm {f}}, m _ {\mathrm {i}}} ^ {(1)} \left[ \frac {1}{\lambda_ {n _ {\mathrm {f}}} - \lambda_ {n _ {\mathrm {i}}}} + \frac {1}{\lambda_ {m _ {\mathrm {f}}} - \lambda_ {m _ {\mathrm {i}}}} \right]. \tag {2}
$$

The stationary nature of the disorder dictates that real transitions from the edge-edge states can occur only if the initial eigenvalue  $\lambda_{\mathrm{i}}^{(2)} = \lambda_{n_{\mathrm{i}}} + \lambda_{m_{\mathrm{i}}}$  is equal to the final one  $\lambda_{\mathrm{f}}^{(2)} = \lambda_{n_{\mathrm{f}}} + \lambda_{m_{\mathrm{f}}}$ . Therefore,  $\lambda_{n_{\mathrm{f}}} - \lambda_{n_{\mathrm{i}}} = -(\lambda_{m_{\mathrm{f}}} - \lambda_{m_{\mathrm{i}}})$ , and the two terms in  $V_{\mathrm{i,f}}^{(2)}$  exactly cancel each other,  $V_{\mathrm{i,f}}^{(2)} = 0$ . That is, two-particle dissipation from each product state is zero, and the same is true for any entangled two-particle state  $\psi^{(2)}$  represented as a quantum superposition of two possible distinguishable configurations  $\psi_{\mathrm{i}}^{(2)}$ , e.g.,  $\psi^{(2)} = \psi_1^{(2)} + \psi_2^{(2)}$ . Physically, this destructive interference is a direct outcome of the indistinguishability of the photons, which ensures that the two-particle eigenvalue is a sum of the two single-particle eigenvalues, and that the two-particle propagator is a product of the single-particle counterparts.

In contrast to dissipation, the situation with dephasing can be different: while each constituent state in an entangled superposition can be protected against disorder<sup>1</sup>, the overall superposition is, in general, not. To be precise, motion through different disordered regions may lead to disorder-induced random phase shifts between the states destroying the entanglement. To avoid this fate, all states in the superposition must travel

across the same spatial region of the photonic structure, such that they are affected by disorder in the exact same manner $^{33}$ . These effects have been explored for spatial path-entangled states $^{1}$ , and for states built from an entangled superposition of an initial nonstationary state  $\psi_{1}^{(2)}$  with its time-delayed replica  $\psi_{1}^{(2)}(\tau)$ , that is, entangled states in the time-domain $^{2}$ . In these two cases, however, the entanglement of the states can be related to the entanglement of symmetrized wavefunction of identical particles $^{34}$ . Consequently, the states exhibit the lowest possible amount of entanglement, as indicated by the corresponding Schmidt numbers  $S_{\mathrm{N}} = 2$ . Throughout this work we use the Schmidt number to quantify the amount of entanglement:  $S_{\mathrm{N}} = 1$  denotes complete separability while  $S_{\mathrm{N}} \gg 1$  corresponds to high entanglement $^{35}$ .

A more appealing type of highly entangled two-photon states are multimode optical Gaussian states in which both photons are most likely to be found inhabiting any waveguide, within an excitation window, simultaneously $^{36}$ . The importance of such states is based on the fact that any phase difference arising among the paths becomes enhanced by a factor of two in comparison with single photon states $^{37}$ . Naturally, the enhanced phase sensitivity of such highly entangled two-photon states manifests as faster diffraction of the associated wavepackets propagating in any photonic system, periodic and disordered $^{38}$ . Therefore, it is not clear to what extent topological protection will persist for these types of highly entangled states.

Propagation of entangled two-photon states in disordered topological lattices. In what follows we analyze the impact of disorder onto a continuum of two-photon states that extend from the correlated to the anti-correlated limits, passing through a completely separable state. For our analysis we consider two topological lattices, one periodic and one aperiodic. In the periodic case we consider the Haldane model $^{39}$ , and for the aperiodic we use a square lattice whose single-particle dynamics corresponds to the quantum Hall effect $^{6,40}$  (information, S. Supporting material). The results for the Haldane model are presented here, while the quantum Hall effect lattice is discussed in the Supplementary Note 5.

In optics, a first-order approximation of the Haldane model can be implemented using a honeycomb lattice composed of helical waveguides as illustrated in Fig. 1a, see pioneering work[41]. In this system, every waveguide has a nearest-neighbor coupling  $\kappa_{1}$  and a complex second-nearest-neighbor coupling  $\kappa_{2}$  or  $\kappa_{2}^{*}$ , see Fig. 1b. At the single-photon level, the Haldane lattice is governed by the Hamiltonian

$$
\hat {H} = \sum_ {i} \beta_ {i} \hat {a} _ {i} ^ {\dagger} \hat {a} _ {i} + \kappa_ {1} \sum_ {\langle i, j \rangle} \left(\hat {a} _ {i} ^ {\dagger} \hat {a} _ {j} + \hat {a} _ {j} ^ {\dagger} \hat {a} _ {i}\right) + i \kappa_ {2} \sum_ {\langle \langle i, j \rangle \rangle} \left(\hat {a} _ {i} ^ {\dagger} \hat {a} _ {j} - \hat {a} _ {j} ^ {\dagger} \hat {a} _ {i}\right), \tag {3}
$$

where  $\beta_{i}$  represents the propagation constant of the  $i$ -th waveguide and the corresponding optical mode is represented by the creation (annihilation) operator,  $\hat{a}_{i}^{\dagger}(\hat{a}_{i})$ . Notice, in a disorder-free lattice  $\beta_{i} = \beta$ . The symbols  $\langle \rangle$  and  $\langle \langle \rangle$  indicate summation over nearest and next-nearest-neighbor sites, respectively. The lattice used in our simulations is a ribbon with  $N_{\mathrm{y}} = 90$  hexagons in the  $y$ -direction and  $N_{\mathrm{x}} = 10$  hexagons in  $x$ -direction, Fig. 1c. We normalized the units in terms of  $\kappa_{1}$  throughout this work, and set  $\kappa_{2} = i\kappa_{1} / 5$ .

For pure states of two indistinguishable noninteracting particles the Hamiltonian is  $H_{2} = H \otimes I + I \otimes H$ , where  $H$  is the single-particle Hamiltonian and  $I$  is the identity operator[42]. The two-photon eigenstates are given by the symmetric tensor

product combinations of the single-photon eigenstates

$$
\left| \phi_ {m, n} ^ {(2)} \right\rangle = \left\{ \begin{array}{l} \left| \phi_ {m} \right\rangle \otimes \left| \phi_ {n} \right\rangle \Longleftrightarrow m = n, \\ \frac {1}{\sqrt {2}} \left(\left| \phi_ {m} \right\rangle \otimes \left| \phi_ {n} \right\rangle + \left| \phi_ {n} \right\rangle \otimes \left| \phi_ {m} \right\rangle\right) \Longleftrightarrow m \neq n. \end{array} \right. \tag {4}
$$

As alluded to above, the two-photon eigenvalues are the sums of the single-photon ones,  $\lambda_{m,n}^{(2)} = \lambda_m + \lambda_n$ .

In the absence of disorder, the eigenvalue spectrum for single-photon states in a finite lattice exhibits topological edge states in the bandgap $^{43}$ , Fig. 1d. In contrast, for two indistinguishable photons, the spectrum does not have a bandgap: the edge-edge states can have the same eigenvalues  $\lambda_{n,m}^{(2)} = \lambda_n + \lambda_m$  as those lying in the bulk-bulk region, Fig. 1e.

To include disorder, we separate the lattice shown in Fig. 1c into three regions<sup>1</sup>. The left and right parts of the system are disorder-free, while its middle part exhibits diagonal disorder<sup>31</sup>, that is, random modifications of the on-site refractive index taken from a normal distribution with zero mean and variance  $\sigma = 1$ . Importantly, taking  $\sigma = 1$  ensures that the disorder strength does not destroy the topological protection for single photons, since  $\sigma = 1$  corresponds to half the size of the topological bandgap. The two-photon eigenspectrum in the presence of disorder is shown in Fig. 1f.

We now send trial two-photon wavepackets into the system. They are built from single-photon edge states and vary continuously from an unentangled product state, with Schmidt number  $S_{\mathrm{N}} = 1$ , to highly entangled two-photon states,  $S_{\mathrm{N}} \gg 1^{44,45}$ , with the two photons either correlated or anti-correlated in space[46].

To construct these states, we begin with protected single-photon states as a template,  $|\tilde{\psi}_{\sigma}^{(1)} \rangle = \sum_{j=1}^{M_{\mathrm{e}}} (-1)^{j} e^{-\frac{(x_{0}-j)^{2}}{2\sigma^{2}}} |j\rangle$ , where  $|j\rangle$  describes a photon initialized in waveguide  $j$ ,  $M_{\mathrm{e}} = 20$  is the selected range of waveguides in the upper-left edge of our system, and  $x_{0} = (M_{\mathrm{e}} + 1)/2 = 10.5$  is the center of this range. These single-photon wavepackets travel through both clean and disordered lattice without scattering to the bulk or back scattering. Importantly, the alternating sign  $(-1)^{j}$  in the amplitude ensures that the wavepacket has proper momentum and resides in the single-photon edge subspace.

Next, we construct our trial two-photon states as follows

$$
\left| \tilde {\psi} _ {\sigma_ {c}, \sigma_ {a}} ^ {(2)} \right\rangle = \sum_ {j, k = 1} ^ {M _ {e}} \psi_ {j, k} | j, k \rangle = \sum_ {j, k = 1} ^ {M _ {e}} (- 1) ^ {j + k} e ^ {- \frac {(j - k) ^ {2}}{4 \sigma_ {a} ^ {2}} - \frac {(x _ {0} - (j + k) / 2) ^ {2}}{\sigma_ {c} ^ {2}}} | j, k \rangle . \tag {5}
$$

Here,  $|j,k\rangle$  represents the state where a photon starts at waveguide  $j$  and its twin at  $k$ . The spatial two-photon correlations are controlled by the parameters  $\sigma_{\mathrm{c}}$  and  $\sigma_{\mathrm{a}}$ . For  $\sigma_{\mathrm{c}} \gg \sigma_{\mathrm{a}}$  we have a spatially correlated state, in which both photons most probably enter into the same waveguide simultaneously[38]. For  $\sigma_{\mathrm{a}} \gg \sigma_{\mathrm{c}}$  we obtain a spatially anti-correlated state, in which the two photons enter at two waveguides symmetrically lying on opposite sides of the window covered by the wavefunction[46].

Finally, we must ensure that the initial wavepackets only include edge states. To this end, we project our state onto the two-photon eigenstates  $|\phi_{m,n}^{(2)}\rangle$  of the system and then remove the components belonging to the subspaces  $\mathcal{B}\otimes \mathcal{E}$  and  $\mathcal{B}\otimes \mathcal{B}$ , keeping only states that belong to the edge-edge subspace

$$
\left| \psi_ {\sigma_ {c}, \sigma_ {a}} ^ {(2)} \right\rangle = \frac {1}{A} \sum_ {m, n} ^ {\mathcal {E} \otimes \mathcal {E}} \sum_ {j, k = 1} ^ {M _ {e}} \psi_ {j, k} \langle \phi_ {m, n} ^ {(2)} | j, k \rangle \left| \phi_ {m, n} ^ {(2)} \right\rangle , \tag {6}
$$

where  $A$  is the normalization constant. It is worth noting that two-photon states described by Eq. (6) are a lattice adoption of Gaussian two-mode squeezed states $^{47}$ , which are a commonplace

![](images/c9c4937954ac4e9c06fc3016ab85f3189e554b0309a2e05e37284a9c957ef4b0.jpg)  
a

![](images/30b0099c3e8cc0d2195f0548f46798546684a18a89d492307ff167389e283e68.jpg)  
b

![](images/e6a5a68a04c03ba5e07f9992a252b429ce01bc6828b9e406497fa3a608af6223.jpg)  
C  
d

![](images/bd77eef343700ea466108a4fc9275617d55fbdcc59e690c80b0150afa63e16e9.jpg)

![](images/043fa171868f4bec8a3993d0b32863dc2d9f0905af71f9f7cb69896ef9e81c7e.jpg)  
e  
Two-photon spectrum  
f

![](images/565386577dccf0475ab60d1f364cd5f3c067022db6a72f4a901d3964e25063ab.jpg)  
Fig. 1 The Haldane photonic lattice. a Photonic implementation of the Haldane system using a honeycomb lattice of helical waveguides. b Elementary hexagonal cell of the Haldane system, with real-valued nearest-neighbor coupling (blue arrows)  $\kappa_{1} = 1$  and imaginary next-nearest-neighbor coupling (red arrows);  $\kappa_{2} = i\kappa_{1} / 5$  along the arrow and  $-i\kappa_{1} / 5$  in the opposite direction. c Pictorial view of the finite lattice used in our numerical analysis. d Single-photon spectrum formed by eigenvalues  $\lambda_{n}$ . In e and f we show the two-photon eigenspectra without and with disorder, respectively. Colors encode the two-photon eigenvalue  $\lambda_{n,m}^{(2)} = \lambda_n + \lambda_m$ . For better appreciation we have separated the spectrum into the subspaces edge-edge ( $\mathcal{E} \otimes \mathcal{E}$ ), bulk-edge ( $\mathcal{B} \otimes \mathcal{E}$ ), and bulk-bulk ( $\mathcal{B} \otimes \mathcal{B}$ ).  
Single particle eigenstate  $n$

choice in quantum optical experiments. The corresponding spatial  $P_{j,k} = |\langle j,k|\psi_{\sigma_c,\sigma_a}^{(2)}\rangle |^2$  and spectral  $S_{m,n} = |\langle \phi_{m,n}^{(2)}|\psi_{\sigma_c,\sigma_a}^{(2)}\rangle |^2$  correlation maps of our initial states, Eq. (6), are shown in Fig. 2. Tuning  $\sigma_{\mathrm{a}}$  and  $\sigma_{\mathrm{c}}$ , one can go from the spatially correlated state  $|\psi_{\mathrm{c}}^{(2)}\rangle$ , Fig. 2a, to the product state  $|\psi_{\mathrm{p}}^{(2)}\rangle$ , Fig. 2b, and to the spatially anti-correlated state  $|\psi_{\mathrm{a}}^{(2)}\rangle$ , Fig. 2c. Note the relation between spatial and spectral distributions: the state  $|\psi_{\mathrm{c}}^{(2)}\rangle$ , which is strongly correlated in space, Fig. 2a, is strongly anti-correlated spectrally Fig. 2d, and vice versa for  $|\psi_{\mathrm{a}}^{(2)}\rangle$ . Irrespective of their correlation maps, all these states occupy the same spatial area on the upper-left edge of the lattice, see Supplementary Note 1. The Schmidt number for  $|\psi_{\mathrm{c,a}}^{(2)}\rangle$  is  $S_{\mathrm{N}} = 13$ , while for  $|\psi_{\mathrm{p}}^{(2)}\rangle$  we have  $S_{\mathrm{N}} = 1$ . We now explore the robustness of these two-photon states as they traverse the disordered lattice. We begin with the product state  $|\psi_{\mathrm{p}}^{(2)}\rangle$ . To characterize the impact of disorder, we compute the fidelity<sup>30</sup> that is given as the overlap of the state  $|\psi_{\mathrm{p}}^{(2)}(z_{\mathrm{f}})\rangle$  after it has traversed the lattice with the reference state  $|\psi_{\mathrm{p}}^{(2)}(z_{\mathrm{m}})\rangle$  obtained after propagating the same state  $|\psi_{\mathrm{p}}^{(2)}\rangle$  in a disorder-free lattice, see Supplementary Note 2. The two wavepackets are taken

at slightly different propagation distances  $z_{\mathrm{f}}$  and  $z_{\mathrm{m}}$  to account for the somewhat different travel distance in a disordered lattice. We find the fidelity  $F_{\mathrm{p}} = |\langle \psi_{\mathrm{p}}^{(2)}(z_{\mathrm{f}})|\psi_{\mathrm{p}}^{(2)}(z_{\mathrm{m}})\rangle |^2 = 0.98$ , confirming that both the single-photon states and their product are immune to disorder. The edge-mode content of the evolved state is almost  $100\%$ ,  $E_{\mathrm{p}} = \sum_{n,m}^{\mathcal{E}\otimes \mathcal{E}}|\langle \phi_{n,m}^{(2)}|\psi_{\mathrm{p}}^{(2)}(z_{\mathrm{f}})\rangle |^2 = 0.9934$ . The product state traverses the lattice without distortion, see Supplementary Movie M1, in spite of the degeneracy between the two-photon edge-edge and bulk-bulk states.

Figure 3a, b visualize this outcome by showing the single-photon spatial distribution and two-photon spectral correlation maps for the two-photon product state  $|\psi_{\mathrm{P}}^{(2)}\rangle$  traversing the disordered lattice. The spatial single-photon probability density  $R(n)$  is given by the diagonal elements  $\rho_{nn}^{(1)}$  of the reduced single-photon density matrix  $\hat{\rho}^{(1)}$ ,  $R(n)\equiv \langle n|\hat{\rho}^{(1)}|n\rangle \equiv \rho_{nn}^{(1)48}$ . The reduced single-photon density matrix  $\hat{\rho}^{(1)}$  is obtained from the two-photon density matrix  $\hat{\rho}^{(2)}$  in the usual way,  $\hat{\rho}^{(1)} = \sum_{m}^{M}\langle m|\hat{\rho}^{(2)}|m\rangle^{30}$ . As expected, the spectral composition of the wavepacket remains undisturbed and the wavepacket

![](images/9a2906616e6e02cf6759dcbe6e4c65a8e908a39a6657b2d6757b8e2a17659eeb.jpg)

![](images/a44e1be1e95d474c0b2fc656bf5d2020460eb03210bc2e4542ddd1ee7bad32bb.jpg)

![](images/257fc56159f4763d8fe5c319d9fa5ce936858003d9728a5893a05f9f367f3e77.jpg)

![](images/5146ed5a46e633379ee77559fbd7e8636c0f2eff262514078252314d17ddb165.jpg)  
Fig. 2 Initial two-photon states. a, b, c Spatial correlation maps  $P_{n,m}$  over the 91 sites of the upper edge of the lattice. d, e, f Spectral correlation maps  $S_{n,m}$  in the  $\mathcal{E} \otimes \mathcal{E}$ -subspace. a, d correspond to the strongly spatially correlated state  $|\psi_c^{(2)}\rangle$ ,  $(\sigma_c, \sigma_a) = (\sqrt{40}, 0.01)$ , b, e stand for the product state  $|\psi_p^{(2)}\rangle$ ,  $(\sigma_c, \sigma_a) = (\sqrt{40}, \sqrt{40})$ , and c, f for the strongly spatially anti-correlated state  $|\psi_a^{(2)}\rangle$ ,  $(\sigma_c, \sigma_a) = (0.01, \sqrt{40})$ .

![](images/1c7bbdbe313e26951c3f7e8634de83c9822e2f32bcfefcd237b61fed9f3064f0.jpg)

![](images/cc4e8e20baa69222273a872f195b5432fbf59db2f29d09bc5be58087a4bdb608.jpg)

![](images/442c9fb9f25aa67a4cbc2bc398b049f8f73eb1408ce896dd79234ae384267c33.jpg)

![](images/f1e44abf3dad384773458349953a27a2ddbe0435b5e5c3bbd9b9ffafc687fd6f.jpg)

![](images/1333faecf7fb25277b52beddf77fb534b99b835da702d7a05c4fc918765b81d8.jpg)

![](images/19c7737c1aab52f6928b672540aeb1d4269cf1b3f9613792bdc04eb4bb0fbfca.jpg)

![](images/6d72b13582838c29f0f8e56018417c9ac5776472c37996b176114560d5b7a372.jpg)  
Fig. 3 Propagation of two-photon edge states. a Probability density distribution for the reduced single-photon state and b the spectral correlation map for the product state  $|\psi_{\mathfrak{p}}^{(2)}\rangle$ , which survives disorder. c, d The same for the spatially correlated entangled state  $|\psi_{\mathrm{c}}^{(2)}\rangle$  propagating in the clean lattice, while e, f show the impact of disorder on this highly entangled state. In all cases the rightmost panels show a magnification of the edge-edge subspace. Dashed lines in a, c, e indicate the disordered region.

![](images/b8ac5d777e41d340e189cc94038e0896ebc89e95bc253f0d4e45ca5f5fcda058.jpg)

propagates through the disordered region without leaving the edge.

We now turn our attention to entangled two-photon states. Figure 3c, d depict  $R(n)$  and the spectral correlation maps for the

two-photon state  $|\psi_{\mathrm{c}}^{(2)}\rangle$  traversing the "clean" lattice, and Fig. 3e, f show the same for the disordered lattice. While in the absence of disorder,  $R(n)$  stays on the edge and the highly correlated two-photon spectral distribution is unchanged (panels c, d), the

disorder strongly affects these states. Figure 3e shows strong dissipation into the bulk as soon as the entangled wavepacket encounters the disordered region. The spectral distribution spreads all over the system, with both bulk-bulk and bulk-edge states becoming occupied, Fig. 3f. A similar result is obtained for  $|\psi_{\mathrm{a}}^{(2)}\rangle$ , except that the cross-like shape observed in Fig. 3f is flipped towards the opposite diagonal, Supplementary Note 3.

To quantify the probability fraction of the states scattered into the bulk we compute the edge-mode content. For  $|\psi_{\mathrm{c}}^{(2)}\rangle$  the edge-mode content after traversing the disordered lattice is  $E_{\mathrm{c}} = 0.4524$ , while for  $|\psi_{\mathrm{a}}^{(2)}\rangle$  it gives  $E_{\mathrm{a}} = 0.4453$ . Thus,  $>50\%$  of both types of states is scattered into the bulk. The part of the states that survives the disordered region and stays on the edge remains strongly correlated in the spectral domain: the edge-edge part of its spectral content preserves the initial shape, see the right column in Fig. 3f. However, the spectral phase of the state is scrambled. To illustrate this point, we have renormalized the transmitted edge part of the two-photon wavepacket to unity and computed its fidelity  $F_{\mathrm{N}}$  by overlapping it with the reference two-photon wavepacket from a clean system, yielding  $F_{\mathrm{N}} = 0.405$ .

The topological window of protection. We find that the conduit for dissipation of the two-photon edge-edge states is always provided by the edge-bulk states, which are degenerate in energy with the edge-edge states. Once disorder induces transitions into the edge-bulk states, they further transfer the amplitudes into the energy-degenerate bulk-bulk states, see Supplementary Movies M2 and M3. Hence, the key to topological protection is to minimize the disorder-induced overlap of the initial joint spectrum with the edge-bulk and bulk-bulk spectral regions, keeping it as close to the center as possible. That is, there is a topological protection window for two-photon states that offers the key guideline for designing robust two-photon states. To infer the protection window, we sent a probe product state with  $\sigma_{\mathrm{c}} = \sigma_{\mathrm{a}} = 0.01$  through an ensemble of 1000 disordered lattices. This initial state is very well localized onto the edge region in real space, ensuring that all components within the state travel along very close paths. The spectral content of the state before and after the disorder is shown in in Fig. 4a, b. The components that have survived the impact of disorder are within the marked window—the topological window of protection. The joint spectral correlation map of any entangled state with varying  $\sigma_{\mathrm{a}}$  and  $\sigma_{\mathrm{c}}$  must fit inside this protection window to be robust against disorder.

In practice, to increase the amount of entanglement we need to increase  $\sigma_{\mathrm{a}}(\sigma_{\mathrm{c}})$  while decreasing  $\sigma_{\mathrm{c}}(\sigma_{\mathrm{a}})$ , and by doing so the joint spectrum unavoidably tends to fall outside the protection window. However, we can always find two-photon states with a considerable amount of entanglement, which are protected. To elucidate this we have scanned the edge-mode content of the two-photon states after propagation through the disordered region as a function of  $\sigma_{\mathrm{a}}$  and  $\sigma_{\mathrm{c}}$ . In Fig. 4c, d we show the contour maps of the edge-mode content as we vary  $\sigma_{\mathrm{a}}$  and  $\sigma_{\mathrm{c}}$ . Figure 4c shows the edge-mode content of the two-photon states after propagation through the disordered region, with the diagonal corresponding to the product states, that is, states with  $\sigma_{\mathrm{a}} = \sigma_{\mathrm{c}}$ . The states with the highest degree of entanglement correspond to very different  $\sigma_{\mathrm{a}}$  and  $\sigma_{\mathrm{c}}$  and, therefore, they are found in the top left and lower right corners in Fig. 4c. In general, highly entangled states lay on the top left ( $\sigma_{\mathrm{a}} \ll \sigma_{\mathrm{c}}$ ) and bottom right ( $\sigma_{\mathrm{a}} \gg \sigma_{\mathrm{c}}$ ) corners and the edge-mode content quickly drops below 0.5. The reason is because as one increases  $\sigma_{\mathrm{a}}$ , or  $\sigma_{\mathrm{c}}$ , the tails of the spectral correlation ellipse fall outside of the protection window and, as a result, the states scatter into the bulk. Similarly, uncorrelated states may experience the same fate when they are initially confined into a small spatial region, which is the case for states that are not confined to the bulk.

with  $\sigma_{\mathrm{a}} = \sigma_{\mathrm{c}} \in (0, 2.5)$ . Figure 4d shows the key figure of merit,  $E \cdot S_{\mathrm{N}}$ , the product of the Schmidt number  $S_{\mathrm{N}}$  and the edge-mode content  $E$ . The bright yellow islands indicate the best two-photon states, which combine robustness against disorder with high degree of entanglement. Importantly, the spectral correlation ellipse of these states always fits into the protection window shown in Fig. 4b. It is worth mentioning the features exhibited by the contour maps are generic as similar structures are obtained for disordered Haldane lattices with different dimensions, see Supplementary Note 4. This demonstrates that, in principle, one can create states with high Schmidt number and edge-mode content close to unity.

As evidence that our results are generic, in the sense that they apply to other two-dimensional topological systems, in the Supplementary Note 5 we have performed a similar analysis for an aperiodic topological lattice system $^{6,40}$ . We have found that the contour map of the edge-mode content  $E$  is not symmetric, implying that the correlated states are slightly less protected than their anti-correlated mirror-images. Nevertheless, we obtain the same qualitative features as in the Haldane model.

# Discussion

Before concluding, we would like to outline possible ways to generate the initial states and address the potential challenges for experimental observations of these effects. The initially highly correlated states can be implemented using standard spontaneous-parametric-down-conversion nonlinear crystals to generate photon pairs that are coupled to the edge of the lattice using a positive achromatic doublet lens as demonstrated in $^{38}$ . Anti-correlated photon pairs can be generated by applying the fractional Fourier transform to the highly correlated states $^{49}$ . The Haldane lattice has been previously demonstrated using femtosecond laser written waveguides as reported in $^{41}$ . Hence, the challenges are reduced to optimizing the fabrication for minimal scattering, absorption and bending losses associated with the helical waveguides.

These results lead to the following conclusions. Two issues have to be considered when constructing two-photon entangled edge states in topological systems: their dissipation into the bulk and the relative dephasing between the different components comprising the entangled state. Regarding dissipation, the two-photon edge states can be protected just as well as the single-photon edge states. Further, phase scrambling can also be minimized if the different components of the entangled state travel along the same path in the edge region. Both aims are achieved by keeping the spectral correlation map of the two-photon state in the center of the window of protection. Thus, attempts to increase entanglement must be balanced against keeping the spectral correlation maps of the two-photon states within the narrow spectral region at the very center of the single-photon gap—the topological window of protection. This limits the degree of entanglement one can safely encode in practice, but presents a clear strategy for creating useful states with high degree of entanglement and robustness.

Looking forward, one could take advantage of the static nature of disorder to circumvent entanglement-induced dissipation into the bulk. While the disorder-induced relative phase between the different product-state components of the entangled wavepacket may appear random due to the random nature of disorder, for static disorder scrambling and dissipation are nevertheless fixed. This opens an opportunity to find the windows of protection as we have done in the cases considered here, and generate robust wavepackets tailored to the particular disordered system at hand. From a practical perspective, the stability of entangled states up to relatively high Schmidt numbers offers practical guidelines for

![](images/8aa49823ddbe1d508ce2c48b73e3b31daae0749cf8c65626b8e2944fd7ee1ee4.jpg)

![](images/f8ad774617e3ae1c973a18243daab15577e7d749944ea5d36b998a69139471e7.jpg)  
Fig. 4 Topological window of protection. In order to identify the topological window of protection, we considered a spectrally broad product state with  $(\sigma_{\mathrm{a}} = \sigma_{\mathrm{c}} = 0.01)$  as initial state and propagate it through an ensemble of 1000 random Haldane lattices. In a we depict the spectral correlation map for the initial state. b depicts the ensemble-average of the spectral correlation maps inside the edge-edge subspace after the propagation through the ensemble of disordered lattices. We find that the only two-photon amplitudes that survive the disorder lie in the region indicated by the black square, which is the protection window. c shows the edge-mode content E and d the product of the edge-mode content and the Schmidt-number  $E\cdot S_N$  as a function of the parameters  $\sigma_{\mathrm{a}},\sigma_{\mathrm{c}}$  of the initial states in the range  $\sigma_{\mathrm{a}},\sigma_{\mathrm{c}}\in [0.01,10]$ .

generating useful entangled edge states in topological photonic systems. Finally, our work may open the door to study topological protection of highly entangled multiphoton non-Gaussian states that fulfill the protection conditions.

# Data availability

The data that support the findings of this study are available from the corresponding author upon reasonable request.

# Code availability

The Matlab programs used to simulate the systems discussed in the paper are available as supplementary software.

Received: 6 August 2020; Accepted: 3 March 2021

Published online: 30 March 2021

# References

1. Rechtsman, M. C. et al. Topological protection of photonic path entanglement. Optica 3, 925-930 (2016).  
2. Mittal, S., Orre, V. V. & Hafezi, M. Topologically robust transport of entangled photons in a 2d photonic system. Opt. Express 24, 15631-15641 (2016).  
3. Gneiting, C., Leykam, D. & Nori, F. Disorder-robust entanglement transport. Phys. Rev. Lett. 122, 066601 (2019).

4. Blanco-Redondo, A., Bell, B., Oren, D., Eggleton, B. J. & Segev, M. Topological protection of biphoton states. Science 362, 568-571 (2018).  
5. Wang, Y. et al. Topological protection of two-photon quantum correlation on a photonic chip. Optica 6, 955-960 (2019).  
6. Hafezi, M., Mittal, S., Fan, J., Migdall, A. & Taylor, J. M. Imaging topological edge states in silicon photonics. Nat. Photon. 7, 1001-1005 (2013).  
7. Blanco-Redondo, A. et al. Topological optical waveguiding in silicon and the transition between topological and trivial defect states. Phys. Rev. Lett. 116, 163901 (2016).  
8. Cheng, X. et al. Robust reconfigurable electromagnetic pathways within a photonic topological insulator. Nat. Mater. 15, 542-548 (2016).  
9. Khanikaev, A. B. & Shvets, G. Two-dimensional topological photonics. Nat. Photon. 11, 763-773 (2017).  
10. Jotzu, G. et al. Experimental realization of the topological haldane model with ultracold fermions. Nature 515, 237-240 (2014).  
11. Wang, M. et al. Topologically protected entangled photonic states. Nanophotonics 8(Aug), 1327-1335 (2019).  
12. Wang, Y. et al. Topologically protected quantum entanglement. Preprint at https://arxiv.org/abs/1903.03015 (2019).  
13. Tambasco, J.-L. et al. Quantum interference of topological states of light. Sci. Adv. 4, eaat3187 (2018).  
14. Gorlach, M. A. & Poddubny, A. N. Interaction-induced two-photon edge states in an extended hubbard model realized in a cavity array. Phys. Rev. A 95, 033831 (2017).  
15. Gorlach, M. A. et al. Simulation of two-boson bound states using arrays of driven-dissipative coupled linear optical resonators. Phys. Rev. A 98, 063625 (2018).  
16. Gorlach, M. A. & Poddubny, A. N. Topological edge states of bound photon pairs. Phys. Rev. A 95, 053866 (2017).

17. Stepanenko, A. A. & Gorlach, M. A. Interaction-induced topological states of photon pairs. Phys. Rev. A 102, 013510 (2020).  
18. Barik, S. et al. A topological quantum optics interface. Science 359, 666-668 (2018).  
19. Bandres, M. A. et al. Topological insulator laser: experiments. Science 359, eaar4005 (2018).  
20. Harari, G. et al. Topological insulator laser: theory. Science 359, eaar4003 (2018).  
21. Kane, C. L. & Mele, E. J. Quantum spin hall effect in graphene. Phys. Rev. Lett. 95, 226801 (2005).  
22. Haldane, F. D. M. & Raghu, S. Possible realization of directional optical waveguides in photonic crystals with broken time-reversal symmetry. Phys. Rev. Lett. 100, 013904 (2008).  
23. Liu, F., Yamamoto, M. & Wakabayashi, K. Topological edge states of honeycomb lattices with zero berry curvature. J. Phys. Soc. Jpn. 86, 123707 (2017).  
24. Strunz, J. et al. Interacting topological edge channels. Nat. Phys. 16, 83-88 (2020).  
25. Stuhler, R. et al. Tomonaga-luttinger liquid in the edge channels of a quantum spin hall insulator. Nat. Phys. 16, 47-51 (2020).  
26. Anirban, A. Interactions on the edge. Nat. Rev. Phys. 1, 699-699 (2019).  
27. Fano, U. Effects of configuration interaction on intensities and phase shifts. Phys. Rev. 124, 1866-1878 (1961).  
28. Jiménez-Galán, A., Argenti, L. & Martin, F. Modulation of attosecond beating in resonant two-photon ionization. Phys. Rev. Lett. 113, 263001 (2014).  
29. Saleh, B. E. A., Abouraddy, A. F., Sergienko, A. V. & Teich, M. C. Duality between partial coherence and partial entanglement. Phys. Rev. A 62, 043816 (2000).  
30. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2010).  
31. Lahini, Y. et al. Anderson localization and nonlinearity in one-dimensional disordered photonic lattices. Phys. Rev. Lett. 100, 013906 (2008).  
32. Martin, L. et al. Anderson localization in optical waveguide arrays with off-diagonal coupling disorder. Opt. Express 19, 13636-13646 (2011).  
33. Perez-Leija, A. et al. Endurance of quantum coherence due to particle indistinguishability in noisy quantum networks. NPJ Quantum Inf. 4, 45 (2018).  
34. Tschernig, K. et al. Direct observation of the particle exchange phase of photons. Preprint at https://arxiv.org/abs/2011.08777 (2020).  
35. Sperling, J. & Vogel, W. The schmidt number as a universal entanglement measure. Phys. Scr. 83, 045002 (2011).  
36. Humphreys, P. C., Barbieri, M., Datta, A. & Walmsley, I. A. Quantum enhanced multiple phase estimation. Phys. Rev. Lett. 111, 070403 (2013).  
37. Afek, I., Ambar, O. & Silberberg, Y. Highnoon states by mixing quantum and classical light. Science 328, 879-881 (2010).  
38. Di Giuseppe, G. et al. Einstein-podolsky-rosen spatial entanglement in ordered and anderson photonic lattices. Phys. Rev. Lett. 110, 150503 (2013).  
39. Haldane, F. D. M. Model for a quantum hall effect without landau levels: condensed-matter realization of the "parity anomaly". Phys. Rev. Lett. 61, 2015-2018 (1988).  
40. Hafezi, M., Demler, E. A., Lukin, M. D. & Taylor, J. M. Robust optical delay lines with topological protection. Nat. Phys. 7, 907-912 (2011).  
41. Rechtsman, M. C. et al. Photonic floquet topological insulators. Nature 496, 196-200 (2013).  
42. Perez-Leija, A. et al. in: CLEO: 2015, JW2A.20 (Optical Society of America, 2015).  
43. Ozawa, T. et al. Topological photonics. Rev. Mod. Phys. 91, 015006 (2019).  
44. Ekert, A. & Knight, P. L. Entangled quantum systems and the schmidt decomposition. Am. J. Phys. 63, 415-423 (1995).  
45. Law, C. K., Walmsley, I. A. & Eberly, J. H. Continuous frequency entanglement: effective finite hilbert space and entropy control. Phys. Rev. Lett. 84, 5304-5307 (2000).  
46. Perez-Leija, A., Keil, R., Moya-Cessa, H., Szameit, A. & Christodoulides, D. N. Perfect transfer of path-entangled photons in  $J_{x}$  photonic lattices. Phys. Rev. A 87, 022303 (2013).

47. Schneeloch, J. & Howell, J. C. Introduction to the transverse spatial correlations in spontaneous parametric down-conversion through the biphoton birth zone. J. Opt. 18, 053501 (2016).  
48. Abouraddy, A. F., Saleh, B. E. A., Sergienko, A. V. & Teich, M. C. Role of entanglement in two-photon imaging. Phys. Rev. Lett. 87, 123602 (2001).  
49. Weimann, S. et al. Implementation of quantum and classical discrete fractional fourier transforms. Nat. Commun. 7, 11027 (2016).

# Acknowledgements

We acknowledge support by the Open Access Publication Fund of Humboldt-Universität zu Berlin. K.T., A.P.L., and K.B. acknowledge support by the Deutsche Forschungsgemeinschaft (DFG) within the framework of the DFG priority program 1839 Tailored Disorder (BU 1107/12-2, PE 2602/2-2). A.J.-G. acknowledges funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 899794. M.I. acknowledges funding from the Deutsche Forschungsgemeinschaft under grant agreement IV 152/6-2. The work of DNC was partially supported by AFOSR (MURI FA9550-20-1-0322).

# Author contributions

A.P.L., M.A.B., and D.N.C. initiated the project. A.P.L., M.A.B., D.N.C., M.I., and K.B. outlined the work. K.T., A.J.G., M.I., M.A.B., and A.P.L. developed the theory. K.T., K.B., and A.P.L. performed the simulations. All the authors discussed and analyzed the results. K.T., M.I., and A.P.L. wrote the manuscript with input from all coauthors. M.A.B. and A.P.L. coordinated the project.

# Funding

Open Access funding enabled and organized by Projekt DEAL.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-021-22264-3.

Correspondence and requests for materials should be addressed to K.T., M.A.B. or A.P.-I.

Peer review information Nature Communications thanks the anonymous reviewer(s) for their contribution to the peer review of this work.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/5b47c6d141bb2bc76eddc97d381a1a4f444f057cb992de670ddfd3eebc5c2308.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2021