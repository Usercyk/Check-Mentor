# Topological rejection of noise by quantum skyrmions

Received: 16 September 2024

Pedro Ornelas<sup>1</sup>, Isaac Nape<sup>®</sup>, Robert de Mello Koch<sup>®</sup> & Andrew Forbes<sup>®</sup>

Accepted: 13 March 2025

Published online: 26 March 2025

Check for updates

An open challenge in the context of quantum information processing and communication is improving the robustness of quantum information to environmental contributions of noise, a severe hindrance in real-world scenarios. Here, we show that quantum skyrmions and their nonlocal topological observables remain resilient to noise even as typical entanglement witnesses and measures of the state decay. This allows us to introduce the notion of digitization of quantum information based on our discrete topological quantum observables, foregoing the need for robustness of entanglement. We compliment our experiments with a full theoretical treatment that unlocks the quantum mechanisms behind the topological behavior, explaining why the topology leads to robustness. Our approach holds exciting promise for intrinsic quantum information resilience through topology, highly applicable to real-world systems such as global quantum networks and noisy quantum computers.

Quantum entanglement is an essential and viable resource for future quantum technologies. It has proven its worth in applications as diverse as secure quantum communication $^{1-3}$ , even over large distances in satellite based networks $^{4,5}$ , quantum computing $^{6-8}$ , quantum imaging of complex objects $^{9,10}$ , quantum metrology $^{11}$  and lithography $^{12,13}$ . However, it is well known that noise deteriorates entanglement, for instance, due to noisy detectors (shot and thermal noise), stray light (e.g., daylight), depolarizing channels, lost photons to name but a few, all examples of generic (isotropic) noise that results in the decay of quantum information in realistic quantum scenarios $^{14-16}$ . The consequence is a diminished ability to certify, identify and exploit the full benefits of quantum entanglement for information processing $^{14,17-19}$ . High dimensional ( $d > 2$  dimensions) entangled states are able to increase the noise threshold to which the usual entanglement witnesses certify entanglement $^{15,20-24}$  but comes with the cost of limited state purity $^{16}$  and complex quantum state analysis $^{25}$ . Although some mitigation techniques exist such as real-time channel analysis $^{26}$  and entanglement purification $^{27}$ , real-world noise correction remains challenging in general photonic systems $^{28,29}$ , prohibiting noise-free communication when information is distributed by entanglement.

An emerging trend is to exploit quantum topological photonics<sup>30</sup>, which has already realized stable quantum emitters<sup>31-33</sup>, robust

transport of entanglement through quantum circuits $^{34,35}$  and entanglement storage $^{36}$  but here the topology is not in the quantum state but in topologically structured matter. Recently the notion of optical topology has emerged, specifically optical skyrmions $^{37}$ , with the potential to embed measurable topological properties into the non-separable spatial and polarization degrees of freedom of classical $^{38-42}$  and quantum $^{43}$  photonic states. A motivation for the interest in skyrmions is their potential to act as resilient information carriers in the presence of noise, a topic very much in its infancy. So far, resilience of classical optical skyrmions under known (non-random) perturbations has been demonstrated experimentally $^{44}$ , yet numerical studies of such classical skyrmions to realistic noise scenarios have returned mixed outcomes $^{45}$ . To the best of our knowledge, no evidence (theoretical or experimental) exists for the resilience of quantum skyrmionic topologies to noise.

Here we show both theoretically and experimentally that quantum skyrmions and their topological quantum observables remain resilient to noise even as typical entanglement witnesses and quantum observables of the state decay. To realize this we create a nonlocal skyrmionic topology as a shared property of two entangled photons and pass the quantum topology through noise, as illustrated in Fig. 1, which we simulate by a generic (isotropic) noise model, a standard

$^{1}$ School of Physics, University of the Witwatersrand, Johannesburg, South Africa.  $^{2}$ School of Science, Huzhou University, Huzhou, China.  $^{3}$ Mandelstam Institute for Theoretical Physics, School of Physics, University of the Witwatersrand, Wits, South Africa.  $\boxtimes$  e-mail: andrew.forbes@wits.ac.za

approach to test quantum states in noise $^{46-48}$ . We provide an intuitive explanation, supported by a rigorous theoretical treatment, as to why such noise can be considered a smooth deformation of the state - an operation that does not modify its topology - independent of its topological class. We present experimental results across various topologies and for a wide range of noise levels, confirming the topological invariance despite the decay of typical entanglement witnesses. Our work opens a path to quantum information processing and communication in real-world noisy quantum systems and channels without the need for compensation or mitigation strategies.

# Results

# Quantum skyrmions

As our aim is to study quantum skyrmionic topology in the presence of noise, we begin by constructing a bi-photon entangled state of the form  $|\Psi \rangle = \frac{1}{\sqrt{2}} \left( |\ell_1\rangle_A |P_1\rangle_B + e^{i\delta} |\ell_2\rangle_A |P_2\rangle_B \right)$ , as depicted graphically in Fig. 2a. Here  $\ell_1$  and  $\ell_2$  denote orbital angular momentum (OAM) of  $\ell_1\hbar$  and  $\ell_2\hbar$  per photon, respectively,  $|P_1\rangle$ ,  $|P_2\rangle$  are orthogonal polarization states and  $\delta$  allows for a relative phase between the two components of the state vector. When  $|\ell_1| \neq |\ell_2|$  the bi-photon correlations form the desired skyrmionic mapping from  $\mathcal{R}^2 \rightarrow \mathcal{S}^2$ , so that the entanglement defines a topology<sup>43</sup>. The topological invariant, the Skyrion number  $(N)$ , characterizes the number of times  $\mathcal{R}^2$  (stereographically projected Hilbert space of photon A) wraps  $S^2$  (Hilbert space of photon B), i.e., the number of times photon B's collapsed states wrap its own Hilbert space after completing a full set of spatial position measurements on photon A. This mapping is evident when expressing the OAM states of photon A in the position basis, using  $|\ell\rangle = \int_{\mathcal{R}^2} |\mathrm{LG}_{\ell}(\mathbf{r})| e^{i\langle \phi \rangle} |\mathbf{r}\rangle d^2 r$  where  $\mathrm{LG}_{\ell}(\mathbf{r})$  are the Laguerre-Gaussian fields and  $|\mathbf{r}\rangle$  are position states corresponding to coordinates vectors  $\mathbf{r}_A \in \mathcal{R}^2$ . Ignoring global phase factors, this recasts our state to

$$
| \Psi \rangle = \int_ {\mathcal {R} ^ {2}} | \mathbf {r} \rangle_ {A} (a (\mathbf {r} _ {A}) | P _ {1} \rangle_ {B} + b (\mathbf {r} _ {A}) | P _ {2} \rangle_ {B}) d ^ {2} r _ {A}, \tag {1}
$$

where the coefficients  $a(\mathbf{r}_A)\equiv |\mathrm{LG}_{\ell_1}(\mathbf{r}_A)|$  and  $b(\mathbf{r}_A)\equiv \exp (i(\Delta \ell \phi_A + \delta))|\mathrm{LG}_{\ell_2}(\mathbf{r}_A)|$  are chosen to be normalized according to  $|a(\mathbf{r}_A)|^2 +$

![](images/7d29b68df571fa71c573684a3db2b3fc9dee0c8871d833be5997fb825504055f.jpg)  
Fig. 1 | Quantum skyrmions through noise. Photons A and B form an entangled state characterized by a non-local quantum skyrmion, shown as a stereographic projection of vectors on a sphere. Passing such a state through noise diminishes the quality of the entangled state, but leaves the topological observable unaltered so long as some entanglement persists.

$|b(\mathbf{r}_A)|^2 = 1$  for all  $\mathbf{r}_A \in \mathcal{R}^2$  and  $\Delta \ell = \ell_2 - \ell_1$ . The Skyrmion number of such a state is then calculated from

$$
N = \frac {1}{4 \pi} \int_ {\mathcal {R} ^ {2}} \epsilon_ {p q r} S _ {p} \frac {\partial S _ {q}}{\partial x} \frac {\partial S _ {r}}{\partial y} d x d y, \tag {2}
$$

where  $\epsilon_{pqr}$  is the Levi-Civita symbol and it is assumed that the sphere has been normalized such that  $\Sigma_{i=1}^{3}S_{i}^{2}=1$ , i.e., a mapping to the unit sphere. To find the necessary quantum Stokes parameters,  $S_{i}$ , one computes the expectation values of the Pauli matrices, calculated by taking the diagonal matrix element at position  $\mathbf{r}$  for photon A and the partial trace over photon B, such that  $S_{i}=\mathrm{Tr}_{B}(\langle|\mathbf{r}\rangle_{A}\langle\mathbf{r}|_{A}\otimes\sigma_{B,i}))=\mathrm{Tr}_{B}\bigl(\sigma_{B,iA}\langle\mathbf{r}|\Psi\rangle\langle\Psi|\mathbf{r}\rangle_{A}\bigr)$ .

# Topological protection

A common way to simulate real-world noisy conditions is to use a generic (isotropic) noise model, by mixing the initially pure state with a maximally mixed state $^{49}$ , covering a wide range of random noise sources e.g., from the source (multi-photon events), the channel (background and lost photons), and the detector (dark counts). To keep the conclusions general we will use the purity of the state as our measure of the noise, and not knowledge of the noise source itself, i.e., an agnostic measure of the noise impact. Without loss of generality we restrict ourselves to the original two-dimensional OAM subspace of the Hilbert space of photon A so that the density matrix can be written as

$$
\rho = p | \Psi \rangle \langle \Psi | + \frac {1 - p}{4} 1 _ {4}, \tag {3}
$$

and  $\mathbb{1}_4$  is the  $4\times 4$  identity matrix on the tensor product of the Hilbert space of photon B and the subspace of photon A that we restrict to. See the supplementary information for an explicit account. The purity of this state is given by  $\gamma = \mathrm{Tr}(\rho^2) = p^2 +\frac{1 - p^2}{4}$  with  $p\in [0,1]$ , e.g., a pure state  $(|\Psi \rangle \langle \Psi |)$  for  $p = 1$  and a maximally mixed state  $(\frac{1}{4}\mathbb{1}_4)$  for  $p = 0$ . To calculate the Skyrmion number we must determine the effect of the noise on the quantum Stokes parameters, whose action is to produce new parameters,  $S_{i}^{\prime}$ .

The proposed noise rejection mechanism can be understood if we consider the spectral decomposition of the Pauli observables, given by  $\sigma_{B,i} = \lambda_i^+ P_i^+ +\lambda_i^- P_i^-$  where  $P_{i}^{\pm} = |\lambda_{i}^{\pm}\rangle \langle \lambda_{i}^{\pm}|$  for positive and negative eigenvalues  $\lambda^{\pm} = \pm 1$  , thus

$$
\begin{array}{l} S _ {i} ^ {\prime} = \operatorname {T r} _ {B} \left(P _ {i} ^ {+} \left[ p _ {A} \langle \mathbf {r} | \Psi \rangle \langle \Psi | \mathbf {r} \rangle_ {A} + \frac {1 - p}{2} \mathbb {1} _ {2} \right]\right) \\ - \operatorname {T r} _ {B} \left(P _ {i} ^ {-} \left[ p _ {A} \langle \mathbf {r} | \Psi \rangle \langle \Psi | \mathbf {r} \rangle_ {A} + \frac {1 - p}{2} \mathbb {1} _ {2} \right]\right) \tag {4} \\ = (I _ {i, \text {p u r e}} ^ {+} + I _ {i, \text {n o i s e}} ^ {+}) - (I _ {i, \text {p u r e}} ^ {-} + I _ {i, \text {n o i s e}} ^ {-}), \\ \end{array}
$$

where  $I_{i,\mathrm{pure}}^{\pm} = \mathrm{Tr}_{B}\big(P_{i}^{\pm}p_{A}\langle \mathbf{r}|\Psi \rangle \langle \Psi |\mathbf{r}\rangle_{A}\big)$  and  $I_{i,\mathrm{noise}}^{\pm} = \frac{1 - p}{2}\mathrm{Tr}_{B}\big(P_{i}^{\pm}\mathbb{1}_{2}\big) = \frac{1 - p}{2}$ . This exposes a subtle point: the noise rejection mechanism stems from subtracting measured values of the projections  $P_{i}^{\pm}$ , which each contain the same noise contribution,  $I_{i,\mathrm{noise}}^{+} = I_{i,\mathrm{noise}}^{-}$ . This invariance is depicted in Fig. 2b where the Skyrmion number remains constant in the presence of noise despite the decay of the initial state, quantified by a decrease in typical entanglement witnesses. Normalizing each of the  $S_{i}^{\prime}$  parameters by  $S_0^{\prime 2} = \mathrm{Tr}_B\big(A\langle \mathbf{r}|\rho |\mathbf{r}\rangle_A\big)$  reveals the smooth deformation that takes place under the addition of this noise to the system. Without this normalization it can be shown that  $\sum_{i}^{3}S_{i}^{\prime 2} = \frac{4p^{2}}{(p + 1)^{2}}\leq 1$  which reveals that photon B's state is mapped to a state on a shell in the interior of its Hilbert space (a unit two sphere), with a radius dictated by the purity of the state, as depicted in Fig. 2c. This does not change the topology:  $\mathcal{R}^2$  still maps to a sphere  $S^2$ , albeit one of a smaller radius, with the same Skyrmion number. When the state is maximally mixed,  $\gamma = \frac{1}{4}$ , the calculated Skyrmion number vanishes as the radius of the shell has reduced to zero. In this singular limit  $\mathcal{R}^2$  maps to a single point, depicted in Fig. 2c, consistent with the fact that when there is no

![](images/da24c79cf0e457c652360d56a03ab5a6dd100e4741e7c1aab7658e75fbab7c09.jpg)

![](images/753ebed9268f9d23dc2a8b567032e21dfb479330875168733f611d9b7bb6c2a5.jpg)

![](images/95899e809f3abe429837c6965464cd8cc6157880d7881a4b97543636c2a589ec.jpg)  
Fig. 2 | Topological rejection of noise. a We create a bi-photon entangled state, with photon A in the spatial degree of freedom and photon B in the polarization degree of freedom, for a non-local skyrmionic topology as a shared emergent property of the two photons, shown as a stereographic projection. b The Skyrmion number is a digitized observable, shown here for integer values from  $N = -2$  to  $N = 2$ , remaining intact along with the topology after the isotropic noise even while the entanglement decreases, except in the case when the entanglement reaches its

![](images/57c73dc8b79365bfa8b7831b618f390534dbe37493dcfaba0a7319c28733ae20.jpg)  
minimum, indicating a non-entangled state. c In the geometric picture of photon B's Hilbert space as expressed by Stokes vectors  $(S_x, S_y, S_z)$ , the change of state purity due to noise is a sphere of diminishing size, which for partially mixed states can always be renormalized while leaving the topology unaltered. Once the state is maximally-mixed, the Hilbert space of photon B has zero radius, no entanglement, and thus only a trivial topology ( $N = 0$ ).

entanglement, there can be no non-trivial topology $^{43}$ . Importantly, this analysis does not assume anything about the initial pure state under investigation. Thus the texture, controlled via a change of polarization basis or relative phase,  $\delta$ , and initial topology of the state does not play a role in ensuring that the topology of the state remains invariant. The topology remains robust to the noise so long as some entanglement persists.

In the interest of creating a useful topological alphabet within a practical setting, in what follows we focus on states with  $|N| > 0$ . The motivation is that all topological states are entangled, but not all entangled states are topological. Thus states with  $N = 0$  with no topology may or may not be entangled, negating the benefit of entanglement distributed information, and further, a topological detection scheme would not be able to distinguish between pure states and completely mixed states when  $N = 0$ .

# Experiment

To verify the concept we use the experiment depicted in Fig. 3a, with full details given in the SI. Entangled OAM biphotons of wavelength  $710\mathrm{nm}$  were generated through spontaneous parametric downconversion (SPDC) in a  $3\mathrm{mm}$  long Type-I Barium Borate (BBO) nonlinear crystal pumped by a  $355\mathrm{nm}$  wavelength collimated Gaussian beam. A spiral bandwidth measurement (top left inset) was performed from which a Schmidt number of  $K = 11$  was calculated[25]. This allows for hybrid state generation with OAM order as high as  $\ell = \pm 5$ . To achieve our topologically non-trivial states we used the spatial-to-polarization coupling (SPC) state preparation stage, exchanging the OAM-OAM correlations between photons A and B for OAM-Polarization correlations. To do so, Photon A was left unaltered while photon B's spatial

information was coupled to its polarization using a double bounce off a spatial light modulator (SLM B). The incoming horizontally polarized photons were modulated in the first pass and the vertically polarized photons in the second (by splitting the SLM screen in two parts), with the quarter-wave plate (QWP) serving to accommodate the fact that the SLM can only modulate horizontally polarized light. For non-trivial topologies the holograms displayed on SLM B were set such that  $|\ell_1| - |\ell_2| \neq 0$ . It should be noted that while this approach allowed for the dynamic selection of a desired hybrid state, it came at the cost of efficiency which limited the creation of hybrid states to OAM values  $|\ell| \leq 3$ . However, these losses may be mitigated by more compact and efficient methods of dynamic spin-orbit coupling techniques[50,51]. In the detection stage, photon A was directed to a spatial light modulator (SLM A) for spatial projective measurements while photon B was passed through a HWP orientated to  $45^{\circ}$  and a linear polarizer orientated at  $90^{\circ}$  for polarization projective measurements. Both photons were collected by single-mode fibres (SMFs) coupled to an avalanche photon detector (APD) and measured in coincidence. Six projective measurements on each photon allowed for an overcomplete quantum state tomography (QST) with 36 entries, which was used to reconstruct the quantum state (with and without noise), with full details given in the SI. Initially, the experiment was run without noise to certify the creation and detection of the example state  $|\Psi\rangle = \frac{1}{\sqrt{2}} \left( |\mathbf{I}\rangle_A |H\rangle_B + |\mathbf{O}\rangle_A |V\rangle_B \right)$ .

Figure 3b shows the reconstructed density matrix and 3c non-local topology of the state with a Neel-type Skyrmion texture, adopting the convention  $S_{z} = S_{1}$  (See SI for full details on vector textures). The data is in agreement with the results expected from the desired pure state, with a purity of  $\gamma = 0.80$  and Skyrmion number  $N = 0.96 \pm 0.01$  (theory:

![](images/090023a7e3cfb63b38939b6e7aeb1f322a8aba269835fcf6d8bf67ddf8bfc768.jpg)  
Fig. 3 | Experimental generation of quantum skyrmions. a Experimental setup for the generation, preparation and detection of non-local skyrmionic quantum states, with details given in the main text and Supplementary Information. The desired hybrid states are prepared via a spatial-to-polarization coupling (SPC) technique. A spiral bandwidth measurement (shown as an inset) reveals the available OAM modes in the initial high-dimensional entangled state. To confirm the  
system performance we show  $\mathbf{b}$  the reconstructed experimental density matrix and,  $\mathbf{c}$  non-local topology for the ideal example state,  $|\Psi\rangle = \frac{1}{\sqrt{2}}(|1\rangle_A|H\rangle_B + |0\rangle_A|V\rangle_B)$ . Abbreviations: Barium Borate (BBO), band-pass filter (BPF), 50:50 beam splitter (BS), lens (L), spatial light modulator (SLM), avalanche photodiode (APD), single mode fibre (SMF), coincidence counter (CC), half-wave plate (HWP), quarter-wave plate (QWP), linear polarizer (LP).

![](images/c752857443c069c1bdf3984a923ed72e67ab4115948a1c5d2bdf4e0801c206f3.jpg)  
Fig. 4 | Noise characterization. Purity as a function of quantum contrast, with theory (dashed lines) and experiment (points) in good agreement. The inset is used to show the error bars from the experiment derived from Poissonian statistics. We use quantum contrast as our measure of the noise impact as it is agnostic to the noise source.

$N = 1$ ). To introduce noise we used an incoherent light source of variable intensity, which is known to be a good approximation to isotropic noise<sup>15</sup>. The contribution of the white light source to the final state was determined from the average quantum contrast,  $Q_{c}$ , which estimated the signal-to-noise (SNR) ratio in our system (See SI for full details), reaching values as high as 32.3 and as low as 2.24 for low and high levels of noise, respectively. This impacts directly on the purity of the state following  $\gamma = \frac{1}{4} \left[3 \left(\frac{Q_{c} - 1}{Q_{c} + 1}\right)^{2} + 1\right]$ , which we used as a measure of the impact of the noise, ranging from our target pure state (no noise,  $Q_{c} \gg 1$ ) to a maximally mixed (separable) state (high noise,  $Q_{c} \approx 1$ ). In Fig. 4 the experimentally obtained purity is plotted against average quantum contrast and is in excellent agreement with theory with a calculated mean-squared error of 0.02, with minor deviations

occurring at higher noise levels likely occurring from random noisy detector contributions and small fluctuations between projective measurements which are averaged over to determine the quantum contrast for a single state. This demonstrates that precise control over the experimental purity was achieved through control over the quantum contrast of the system. Moreover, as the impact of the noise was characterized based on how it affected the state and quantified using a universal metric,  $Q_{c}$ , we expect our model and experiment to remain agnostic to the origin of the noise whether that be the entanglement source, the detectors or the channel, thus emphasizing the applicability of our results to real world scenarios.

The experiment was run for six different initial states with varying topology,  $N \in \{-3, -2, -1, 1, 2, 3\}$ , and textures: Neel-type ( $N = 1$ ), anti-skyrmion ( $N = -1$ ) and higher-order Skyrmions ( $N > 1$ ) and anti-skyrmions ( $N < -1$ ), each for a wide range of isotropic noise levels, and in each case the quantum Stokes parameters inferred from a quantum state tomography. Example data is shown in Fig. 5a-c for the states  $\rho = p|\Psi\rangle \langle\Psi| + \frac{1-p}{4} \mathbb{1}_4$  where  $|\Psi\rangle = \frac{1}{\sqrt{2}} \left(|3\rangle_A |H\rangle_B + |0\rangle_A |V\rangle_B\right)$  in the presence of varying isotropic noise levels from pure (point 1,  $\gamma = 0.80$ ) to partially-mixed (point 2,  $\gamma = 0.45$ ) and then maximally mixed (point 3,  $\gamma = 0.25$ ). As expected the QST data shown in Fig. 5a reveals a constant noise contribution across all projections within a single QST measurement, further indication of the isotropic nature of the noise as the contribution of noise is independent of the type of polarization and spatial projection performed. Furthermore, the QST reveals a characteristic saturation of each projection measurement with an increase in isotropic noise. This is accompanied by a clear transition of the density matrix describing a pure state (entangled) to that describing a maximally-mixed state (no entanglement) as shown in Fig. 5b. The quantum Stokes vector,  $\vec{S}(x,y) = (S_x, S_y, S_z)^T$ , derived from each density matrix is plotted in Fig. 5c. As expected, the magnitude of the quantum Stokes vector diminishes with decreasing purity (increasing noise), until it collapses to a point with zero magnitude. The Skyrmion number for these three states (1-3) was calculated to be  $N = 2.99 \pm 0.01$ ,  $N = 2.99 \pm 0.01$  and  $N = 0.01 \pm 0.01$ , respectively, revealing that the skyrmion number remains intact until the entanglement vanishes altogether.

![](images/adb9756f4b7d05273330150d6585063f5a1201438649c4d7217555c0313e98c2.jpg)  
(a)

![](images/9c391683f6c3caa0933f069bb00554d0358bbf6f26075890eff698c0b4684cea.jpg)  
(b)  
(c)

![](images/8df796fbfd3cba5af69f4ac485e6564c96202fccb1df1b3236c28921a29a71a8.jpg)  
Fig. 5 | Experimental verification of topological resilience. a QST results for the example state  $|\Psi \rangle = \frac{1}{\sqrt{2}} (|3\rangle_A|H\rangle_B + |0\rangle_A|V\rangle_B)$  in the presence of varying noise levels from pure (point 1,  $\gamma = 0.80$ ) to partially-mixed (point 2,  $\gamma = 0.45$ ) and then maximally-mixed (point 3,  $\gamma = 0.25$ ). b The experimental density matrices extracted from the QST of each state. c The quantum Stokes vector,  $\vec{S}(x,y) = (S_x,S_y,S_z)^T$ , derived from each density matrix corresponding to points 1 to 3 in part a.

![](images/a58ca77f3f84ccb1669ea120cd4257179f78f15bef00aa02757b6dd7e8e1b599.jpg)  
(d)  
(e)

![](images/d354d0a1571e95cb4176d5b52c6a25d79eac669fd5ffad6e22bdf856d268010f.jpg)  
d Skyrmion number as a function of quantum contrast, with experiment (points) in excellent agreement with theory (dashed lines). The collapse of the topology when the maximally-mixed state limit  $(Q_{c} = 1)$  is reached is shown in the zoomed-in inset. e While the Skyrmion number is stable to noise, typical entanglement witnesses such as concurrence, fidelity and purity are not, as shown experimentally (points) and theoretically (lines).

Figure 5d shows data for the rest of the entangled states considered. The theoretical (dashed lines) and experimental (points) results for the Skyrmion number as a function of quantum contrast are in excellent agreement across all topologies, providing further evidence for topological robustness across all topological classes. The zoomed inset shows experimental data near the classical limit where it is clear that a topological transition from  $N \neq 0$  to  $N = 0$  occurs because without entanglement there can be no topology. This robustness of the topological observable is in stark contrast to the decay of typical entanglement witnesses such as concurrence, fidelity and state purity (See SI for the definitions of these quantities), as shown in Fig. 5e using the same example state as that used in Fig. 5a-c. While each of the entanglement witnesses decay continuously until they each reach their expected minima for a 2D maximally mixed state ( $C = 0$ ,  $F = 0.25$ ,  $\gamma = 0.25$ ), the Skyrmion number remains intact regardless of the degree of noise present, only decaying once the state is maximally mixed.

We can further visualize this in Fig. 6, where we show the ideal topology without noise along side that with noise, for three Skyrmion numbers. We see that the topology remains unchanged as noted by the position, length and orientation of the vectors, resulting in an almost unchanged Skyrmion number that is in excellent agreement with the ideal case (within experimental uncertainty). The insets show one zoomed in vector from each sphere to confirm the equivalence.

# Discussion

Typical quantum information encoding schemes rely on the entanglement of non-separable quantum states, a resource that is highly vulnerable to noise, as we have shown. In contrast, we propose encoding quantum information into robust topological observables of entangled states. Despite being rooted in the state's entanglement, these topological features remain entirely intact, even as the state itself degrades when transmitted through a noisy channel. Our approach to

noise rejection can be understood in the context of information digitization, where continuous analogue signals are replaced by a discrete signal of bits through binning, e.g., by declaring signals below some threshold as 0 and those above it as 1. At the quantum level, employing discrete subsystems represented as qubits does not achieve the desired discretization. The basic quantum resource, entanglement, is encoded in correlations between the subsystems and simply using subsystems with a finite number of states does not render these correlations discrete. We moot that the topology of the wavefunction with its associated discrete observable naturally achieves this. Why is the discretization of entanglement interesting? Discrete signals are always more robust against the effects of noise. This follows because for discrete signals the noise can't produce an arbitrarily small perturbation of the signal: the noise must be able to flip the signal between two discrete states before any effect is registered. In the same way that digital signals enabled successful classical computation and communication, digital quantum signals may allow successful quantum computation and communication. Given a discretization scheme, it then becomes urgent to establish that noise is not able to drive the jumps between discrete states that would corrupt the discrete signal. The importance of our work is that, for a physical and realistic source of noise, we have been able to demonstrate this.

Skyrmionic photonic topologies have been celebrated for their potential to act as resilient information carriers $^{37}$ , with some convincing experimental results shown for the resilience of classical optical skyrmions under known operations with optical elements $^{44}$ . This report offers, to the best of our knowledge, the first experimental results on the resilience of quantum skyrmions to noise, confirming that such quantum channels are map preserving: they can be viewed as a smooth deformation of the state (map) and thus preserves topology even when the entanglement itself is decaying. Moreover, the isotropic model employed in this work makes no assumptions about the photons'

Topology without noise

Topology with noise

![](images/7275a103131b65c73cd73f2163a35ebeec7784e9827bd453710b6d8cdd434a08.jpg)  
$N = 1$

![](images/3d0af1baefd7a9012d5a7e6efc0410ec7c08f1ad37b8263593814c597620bc8f.jpg)  
$N = 0.96\pm 0.01$

![](images/72f71b054230ea21131cea599012ff2f6b7325174f8bf193a51cc17701024c1b.jpg)  
$N = -1$

![](images/96cc26d3a32fe511603d5022cc66e573be30cca5cc2fe7d083ee31e265aa84c3.jpg)  
$N = -0.97\pm 0.01$

![](images/d83032aa8afc61e5969a90a9eb96a02efcc0439c40fc060e1f1546b165dee177.jpg)  
$N = 2$  
Fig. 6 | Invariance of topology to noise. The topology of the ideal (Topology without noise) and experimentally retrieved state after passing through the noisy channel (Topology with noise), shown as stereographic projections of the state vectors (normalized to aid visualization) of photon B on a sphere. The experimental state vectors exhibit minimal deviation from the ideal case as the noise acts only to scale the vectors, not to change their orientation. The calculated Skyrmion number is given for each case, confirming the robustness and the conceptual picture of Fig. 2b.

![](images/290ee3f83866c2aa4e74e6c3702ca6785b6fd841251d164d4ae756a0559096b8.jpg)  
$N = 1.99\pm 0.01$

degrees of freedom and can be extended to investigate its impact on higher-dimensional states. This enables the exploration of topological properties distributed across distances in diverse higher-dimensional entangled states in the presence of noise. We believe that this noise rejection by topology mechanism could be exploited in practical quantum information processing and communication protocols, e.g., quantum communication under ambient (daylight) conditions, or quantum computing on noisy photonic chips, and could be used in conjunction with the entanglement preserving strategies mentioned in the introduction for preservation of entanglement and information. The demonstrated resilience comes without the need for error mitigation or state purification techniques, thus offering an approach to quantum information resilience in realistic and non-ideal conditions.

In conclusion, we have shown both theoretically and experimentally that quantum skyrmions and their topological quantum observables remain resilient to isotropic noise, a generic form of quantum noise that captures realistic effects from the source, channel, and detector, e.g., multi-photon events, dark counts, shot and thermal noise, background light (e.g., daylight) and lost photons. We present experimental results across various topologies (up to orders  $N = \pm 3$ ) and for a wide range of noise levels, confirming the topological invariance and only collapsing once there is no entanglement at all. We show that traditional quantum measures decrease continuously under the same conditions, highlighting the advantage of discrete rather than continuous observables. Our work opens a pathway to quantum information processing and

communication in noisy quantum systems and channels without the need for compensation or mitigation strategies.

# Data availability

The data supporting the findings of this study are available from the corresponding author upon request.

# Code availability

The code used to produce the results are available from the corresponding author upon request.

# References

1. Gisin, N., Ribordy, G., Tittel, W. & Zbinden, H. Quantum cryptography. Rev. Mod. Phys. 74, 145 (2002).  
2. Scarani, V. et al. The security of practical quantum key distribution. Rev. Mod. Phys. 81, 1301 (2009).  
3. Ma, X., Fung, C.-H. F. & Lo, H.-K. Quantum key distribution with entangled photon sources. Phys. Rev. A 76, 012307 (2007).  
4. Liao, S.-K. et al. Satellite-to-ground quantum key distribution. Nature 549, 43-47 (2017).  
5. Bedington, R., Arrazola, J. M. & Ling, A. Progress in satellite quantum key distribution. npj Quantum Inf. 3, 30 (2017).  
6. Thomas, P., Ruscio, L., Morin, O. & Rempe, G. Efficient generation of entangled multiphoton graph states from a single atom. Nature 608, 677-681 (2022).  
7. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188 (2001).  
8. Briegel, H. J., Browne, D. E., Dür, W., Raussendorf, R. & Van den Nest, M. Measurement-based quantum computation. Nat. Phys. 5, 19-26 (2009).  
9. Pepe, F. V., Di Lena, F., Garuccio, A., Scarcelli, G. & D'Angelo, M. Correlation plenoptic imaging with entangled photons. Technologies 4, 17 (2016).  
10. Sephton, B., Nape, I., Moodley, C., Francis, J. & Forbes, A. Revealing the embedded phase in single-pixel quantum ghost imaging. Optica 10, 286-291 (2023).  
11. Giovannetti, V., Lloyd, S. & Maccone, L. Advances in quantum metrology. Nat. photonics 5, 222-229 (2011).  
12. Boto, A. N. et al. Quantum interferometric optical lithography: exploiting entanglement to beat the diffraction limit. Phys. Rev. Lett. 85, 2733 (2000).  
13. Kok, P. et al. Quantum-interferometric optical lithography: towards arbitrary two-dimensional patterns. Phys. Rev. A 63, 063407 (2001).  
14. Nielsen, M. A. & Chuang, I. L. Quantum computation and quantum information (Cambridge university press, 2001).  
15. Ecker, S. et al. Overcoming noise in entanglement distribution. Phys. Rev. X 9, 041042 (2019).  
16. Zhu, F., Tyler, M., Valencia, N. H., Malik, M. & Leach, J. Is high-dimensional photonic entanglement robust to noise? AVS Quantum Sci. 3, 011401 (2021).  
17. Kumar, D. & Pandey, P. Effect of noise on quantum teleportation. Phys. Rev. A 68, 012317 (2003).  
18. Lloyd, S. Capacity of the noisy quantum channel. Phys. Rev. A 55, 1613 (1997).  
19. Liang, H.-Q., Liu, J.-M., Feng, S.-S. & Chen, J.-G. Quantum teleportation with partially entangled states via noisy channels. Quantum Inf. Process. 12, 2671-2687 (2013).  
20. Peterfreund, E. & Gavish, M. Multidimensional scaling of noisy high dimensional data. Appl. Comput. Harmonic Anal. 51, 333-373 (2021).  
21. Almeida, M. L., Pironio, S., Barrett, J., Toth, G. & Acín, A. Noise robustness of the nonlocality of entangled quantum states. Phys. Rev. Lett. 99, 040403 (2007).  
22. Qu, R. et al. Robust method for certifying genuine high-dimensional quantum steering with multimeasurement settings. Optica 9, 473-478 (2022).

23. Tsokeng, A. T., Tchoffo, M. & Fai, L. C. Dynamics of entanglement and quantum states transitions in spin-qutrit systems under classical dephasing and the relevance of the initial state. J. Phys. Commun. 2, 035031 (2018).  
24. Qu, R. et al. Retrieving high-dimensional quantum steering from a noisy environment with n measurement settings. Phys. Rev. Lett. 128, 240402 (2022).  
25. Nape, I., Sephton, B., Ornelas, P., Moodley, C. & Forbes, A. Quantum structured light in high dimensions. APL Photonics 8, 5 (2023).  
26. Ndagano, B. et al. Characterizing quantum channels with nonseparable states of classical light. Nat. Phys. 13, 397-402 (2017).  
27. Yan, P.-S., Zhou, L., Zhong, W. & Sheng, Y.-B. Advances in quantum entanglement purification. Sci. China Phys., Mech. Astron. 66, 250301 (2023).  
28. Quek, Y., Stilck Franca, D., Khatri, S., Meyer, J. J. & Eisert, J. Exponentially tighter bounds on limitations of quantum error mitigation. Nat. Phys. 20, 1648-1658 (2024).  
29. Oh, C., Liu, M., Alexeev, Y., Fefferman, B. & Jiang, L. Classical algorithm for simulating experimental gaussian boson sampling. Nat. Phys. 20, 1461-1468 (2024).  
30. Yan, Q. et al. Quantum topological photonics. Adv. Opt. Mater. 9, 2001739 (2021).  
31. Mehrabad, M. J. et al. Chiral topological photonics with an embedded quantum emitter. Optica 7, 1690-1696 (2020).  
32. Dai, T. et al. Topologically protected quantum entanglement emitters. Nat. Photonics 16, 248-257 (2022).  
33. Mittal, S., Goldschmidt, E. A. & Hafezi, M. A topological source of quantum light. Nature 561, 502-506 (2018).  
34. Barik, S. et al. A topological quantum optics interface. Science 359, 666-668 (2018).  
35. Blanco-Redondo, A., Bell, B., Oren, D., Eggleton, B. J. & Segev, M. Topological protection of biphoton states. Science 362, 568-571 (2018).  
36. Parmee, C. D., Dennis, M. R. & Ruostekoski, J. Optical excitations of skyrmions, knotted solitons, and defects in atoms. Commun. Phys. 5, 54 (2022).  
37. Shen, Y. et al. Optical skyrmions and other topological quasiparticles of light. Nat. Photonics 18, 15-25 (2024).  
38. Gao, S. et al. Paraxial skyrmionic beams. Phys. Rev. A 102, 053513 (2020).  
39. Shen, Y. Topological bimeronic beams. Opt. Lett. 46, 3737-3740 (2021).  
40. Shen, Y., Martínez, E. C. & Rosales-Guzmán, C. Generation of optical skyrmions with tunable topological textures. ACS Photonics 9, 296-303 (2022).  
41. Singh, K., Ornelas, P., Dudley, A. & Forbes, A. Synthetic spin dynamics with bessel-gaussian optical skyrmions. Opt. Express 31, 15289-15300 (2023).  
42. Sugic, D. et al. Particle-like topologies in light. Nat. Commun. 12, 1-10 (2021).  
43. Ornelas, P., Nape, I., de Mello Koch, R. & Forbes, A. Non-local skyrmions as topologically resilient quantum entangled states of light. Nat. Photon. 18, 258-266 (2024).  
44. Wang, A. A. et al. Topological protection of optical skyrmions through complex media. Light. Sci. Appl. 13, 314 (2024).  
45. Liu, C., Zhang, S., Maier, S. A. & Ren, H. Disorder-induced topological state transition in the optical skyrmion family. Phys. Rev. Lett. 129, 267401 (2022).  
46. Horodecki, M., Horodecki, P. & Horodecki, R. Limits for entanglement measures. Phys. Rev. Lett. 84, 2014 (2000).  
47. Horodecki, M., Horodecki, P. & Horodecki, R. General teleportation channel, singlet fraction, and quasidistillation. Phys. Rev. A 60, 1888 (1999).

48. Horodecki, R., Horodecki, P., Horodecki, M. & Horodecki, K. Quantum entanglement. Rev. Mod. Phys. 81, 865 (2009).  
49. Dur, W., Briegel, H.-J., Cirac, J. I. & Zoller, P. Quantum repeaters based on entanglement purification. Phys. Rev. A 59, 169 (1999).  
50. Wu, H.-J. et al. Heralded generation of vectorially structured photons with a high purity. Front. Phys. 9, 654451 (2021).  
51. Zhong, R.-Y. et al. Gouy-phase-mediated propagation variations and revivals of transverse structure in vectorially structured light. Phys. Rev. A 103, 053520 (2021).

# Acknowledgements

We thank Bienvenu Ndagano for useful initial discussions concerning the project. This work was supported by the South African National Research Foundation/CSIR Rental Pool Programme and the South African Quantum Technology Initiative. The research of R.M.K. is in part supported by a start up research fund of Huzhou University, a Zhejiang Province talent award and by a Changjiang Scholar award.

# Author contributions

The experiment was performed by P.O. and I.N. performed the experiment, and P.O., I.N., and R.M.K. contributed the theory. All authors contributed to the writing of the manuscript and analysis of data. A.F. conceived of the idea and supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-025-58232-4.

Correspondence and requests for materials should be addressed to Andrew Forbes.

Peer review information Nature Communications thanks Changxu Liu, and the other, anonymous, reviewer for their contribution to the peer review of this work. A peer review file is available.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025