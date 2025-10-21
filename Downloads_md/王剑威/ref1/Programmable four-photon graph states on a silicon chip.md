ARTICLE

https://doi.org/10.1038/s41467-019-11489-y

OPEN

# Programmable four-photon graph states on a silicon chip

Jeremy C. Adcock  $①$ , Caterina Vigliar  $①$ , Raffaele Santagati  $①$ , Joshua W. Silverstone  $①$  & Mark G. Thompson  $①$

Future quantum computers require a scalable architecture on a scalable technology—one that supports millions of high-performance components. Measurement-based protocols, using graph states, represent the state of the art in architectures for optical quantum computing. Silicon photonics technology offers enormous scale and proven quantum optical functionality. Here we produce and encode photonic graph states on a mass-manufactured chip, using four on-chip-generated photons. We programmably generate all types of four-photon graph state, implementing a basic measurement-based protocol, and measure high-visibility heralded interference of the chip's four photons. We develop a model of the device and bound the dominant sources of error using Bayesian inference. The combination of measurement-based quantum computation, silicon photonics technology, and on-chip multipair sources will be a useful one for future scalable quantum information processing with photons.

Graph states are key entangled resources for quantum information processing. They are quantum states, which can be drawn as a graph, with a qubit on each vertex and pair-wise entanglement on each edge<sup>1</sup>. In measurement-based quantum computing, where single-qubit measurements on a graph state drive the computation forward, particular graphs enable particular computational tasks<sup>2</sup>. Topological quantum error correction, relying centrally on graph states, will provide essential noise tolerance to future experimental realisations<sup>3</sup>. Graph states also play a central role as platforms for the simulation of complex processes and dynamics<sup>4</sup>, and for quantum secret sharing protocols<sup>5</sup>. As such, graph states have featured strongly in experiment, in both optics<sup>6-9</sup> and other platforms<sup>10</sup>. The reconfigurable generation of arbitrary graphs, never before achieved in optics, will accelerate development of many graph-based applications.

Integrated optics promises new levels of scale for optical quantum devices. It offers robustly mode-matched, miniature components, lithographically defined in a planar process. Phase stability and matched optical path lengths are guaranteed. State-of-the-art chip-scale devices now exhibit loss and error performance approaching that of bulk and fibre systems. Quantum optical functionality has been demonstrated in all major technology platforms: lithium niobate $^{11}$ , silica $^{12-14}$  (both lithographic and laser-written), silicon nitride $^{15}$ , gallium arsenide $^{16}$ , indium phosphide $^{17}$ , and silicon $^{18,19}$ .

Silicon devices have rapidly grown in complexity in recent years, with quantum demonstrators now exceeding 500 on-chip components[20], and classical silicon photonic devices having thousands[21,22]. Integration with CMOS electronics could push this scale further still, by miniaturising control and interconnect functionality[22]. A quantum device's computational power is related to the quantum configuration (Hilbert) space accessible to it. In optics, this space has  $m^n$  dimensions, for  $n$  photons scattered across  $m$  modes. So far, the scaling up of silicon quantum photonics has mainly involved scattering one or two photons ( $n = 1$  or 2) over more and more waveguides (increasing  $m$ ) as a route to polynomially larger Hilbert spaces[20,23]. Extending chip-scale quantum optics into the multi-pair regime, increasing  $n$ , is a crucial step for exponential Hilbert space scaling. Only recently has on-chip heralded interference between on-chip-generated photons been demonstrated[24,28], though visibility is limited and no quantum information has yet been encoded.

We present a silicon quantum-optical device that can generate four photons and programmably encode them into either of the two classes $^{25}$  of four-qubit graph state entanglement—classes closed under local unitary transformations. We refer to these two classes by their best-known members: 'star'  $|S_4\rangle$ , and 'line'  $|L_4\rangle$ . We observe quantum interference between photons heralded from two of the on-chip photon-pair sources, characterise the stabilisers of the star and line states, and test their multipartite nonlocality. Finally, we use Bayesian inference to access key device parameters, based on the four-photon data alone.

# Results

Device and experiment design. Our device, shown schematically in Fig. 1, operates in four stages. (1) Four photons in two pairs are generated in superposition over four sources. (2) These are demultiplexed by wavelength and rearranged to group signal and idler photons. The resulting dual-rail, path-encoded qubit state is a product of Bell-pairs,  $|\Phi^{+}\rangle_{1,3} \otimes |\Phi^{+}\rangle_{2,4}$  (with qubit indices in subscript). (3) The signal-photon qubits are operated upon by a reconfigurable postselected entangling gate (R-PEG). This can be programmed to perform either a fusion or controlled-Z operation, to generate star- or line-type entanglement $^{25}$ , respectively,

with postselected probability 1/2 or 1/9. (4) We then perform arbitrary single-qubit projective measurements, using Mach-Zehnder interferometers (MZI), on the four-qubit states. A full description of the state evolution can be found in Supplementary Note 3 and Supplementary Fig. 5.

The  $\chi^{(3)}$  process, spontaneous four-wave mixing, converts bright telecommunications-band pump pulses into quantum-correlated signal and idler photons in the spiralled silicon waveguides of our source stage[26]. Thermo-optic phase modulators provide electronic reconfigurability throughout the device. Focussing vertical grating couplers connect on-chip waveguides to optical fibre. Finally, signal and idler photons are tightly filtered in fibre (pump:photon filtering bandwidth ratio 2:1, see Supplementary Fig. 7), and registered by superconducting nanowire single-photon detectors. See Methods for more details. Using this apparatus, we measure heralded two-photon fringes, the purity of our sources, and the stabilisers of our programmed graph states with four photons.

Heraldeng Hong-Ou-Mandel interference. Indistinguishable photons are key for high-fidelity operation. Hong-Ou-Mandel (HOM) interference, whereby two photons launched into the two ports of a beamsplitter bunch at the outputs, directly indicates their distinguishability—over all degrees of freedom—via the residual rate of antibunching from the beamsplitter outputs. When the interfering photons are heralded from entangled pairs (four photons total), non-unit photon purity also contributes to their distinguishability. On-chip path lengths are naturally matched, so rather than using the conventional time-delay HOM dip, we measure an on-chip heralded fringe $^{24,27}$  (Supplementary Note 2 and Supplementary Fig. 4 relate these two measurements). In both measurements, the residual antibunching rate indicates the photons' overall distinguishability. We interfere signal photons from sources 2 and 3, heralding on the two corresponding idler photons. By tuning the central R-PEG Mach-Zehnder's phase,  $\phi$ , we sweep its effective reflectivity,  $R(\phi)$ , from  $R(0) = 0$ , through  $R(\pi) = 1$ , to  $R(2\pi) = 0$ . At  $R(m\pi)$ , there is no interference, while at  $R(m\pi + \pi/2) = 1/2$ , the Hong-Ou-Mandel effect occurs ( $m \in \mathbb{Z}$ ). The measured fringe, shown in Fig. 2d, exhibits a visibility of  $V = 0.82 \pm 0.02$ , in line with other measurements on chip $^{24,28}$ . Here,  $V = (N_{\max} - N_{\min}) / (N_{\max} + N_{\min})$ , and  $N_{\max}$  and  $N_{\min}$  are the maximum and minimum values of the fitted sinusoid; classical light is limited to  $V < 1/3$ . The conventional HOM-dip-equivalent visibility, upper-bounded by the heralded purity of our photons, is  $V_{\mathrm{HOM}} = (N_{\max} - 2N_{\min}) / N_{\max} = 0.80 \pm 0.02$  (see Supplementary Note 2). The photon-pair generation probability here is  $p = 0.06$ . We corroborate  $V_{\mathrm{HOM}}$  by measuring the unheraldined second-order correlation function  $g^{(2)}(0)$  for the eight modes of our four on-chip sources, implying $^{29}$  heralded purities between 0.82 and 0.92 (Supplementary Note 1 and Supplementary Fig. 2 contain a full listing). New on-chip parametric source designs will improve brightness and purity further $^{14,30,31}$ .

Graph state measurements. We verify the generation of the four-photon star and line graph states  $(|S_4\rangle$  and  $|L_4\rangle)$  by measuring their 16 stabilisers $^{32}$ ,  $g_{\{i\}}$ , where  $\{i\}$  is the set of generators whose product composes each stabiliser (e.g.,  $g_{12} = g_1g_2$ ). The four stabiliser generators of the state  $|S_4\rangle$  are:

$$
g _ {1} = X I Z, \quad g _ {2} = I X I Z, \quad g _ {3} = I I X Z, \quad g _ {4} = Z Z Z X, \tag {1}
$$

where  $X$ ,  $Y$ , and  $Z$  are Pauli matrices and  $I$  is the identity matrix; tensor products are implied. For  $|L_4\rangle$ , the stabiliser generators are:

$$
g _ {1} = X Z Z I, \quad g _ {2} = Z X I Z, \quad g _ {3} = Z I X I, \quad g _ {4} = I Z I X. \tag {2}
$$

![](images/39ba87bd7a43e7def330fa71e6afb0bcf5bfcce93058ba05b1ed461bb52f2a74.jpg)  
Fig. 1 Experiment overview. A schematic of the silicon-on-insulator chip-scale device is shown, comprising: four telecommunications-band photon-pair sources, producing four photons in superposition; a qubit demultiplexer, which configures that superposition into a product of two Bell-pairs; a reconfigurable postselected entangling gate (R-PEG); and four single-qubit projection and analysis stages, formed of four Mach-Zehnder interferometers implementing qubit  $Y$  rotations, preceded by four  $Z$  rotations. An optical micrograph of the device can be found in Supplementary Fig. 1. Corresponding graph states are indicated above, starting with the two input Bell-pairs, and ending with either 'star' or 'line' graph states, for fusion or controlled-Z R-PEG configurations, respectively

Measurements for each stabiliser are plotted in Fig. 2a, b, for  $|S_4\rangle$  and  $|L_4\rangle$ , respectively. From these, we compute fidelities, shown in Table 1, and find that both states robustly satisfy the  $F > 1/2$  threshold to witness genuine multipartite entanglement<sup>32</sup>. These fidelities compare favourably with the first bulk-optics measurements on these states<sup>6,33</sup>. In these and subsequent four-photon measurements, we reduce the photon-pair generation probability to  $p = 0.03$  to suppress multiphoton noise.

We perform a basic measurement-based protocol<sup>34</sup> by projecting various qubits of  $|S_4\rangle$  onto  $|0\rangle$ , and measuring the remaining two- and three-qubit graph states. We denote these states  $|S_4\rangle_J = (\otimes_{j\neq J}\langle 0|_j|S_4\rangle$ , where  $J$  is the set of remaining (un-projected) qubits. The three-qubit state  $|S_4\rangle_{1,3,4}$  and the two-qubit states  $|S_4\rangle_{1,4}$  and  $|S_4\rangle_{3,4}$  can be produced by projecting qubits  $\{2\}$ ,  $\{2,3\}$ , and  $\{1,2\}$  onto  $|0\rangle$ , respectively. Measured fidelity data for these states, along with those for the two input Bell-pairs,  $|\Phi^{+}\rangle_{1,3}$  and  $|\Phi^{+}\rangle_{2,4}$ , are listed in Table 1. Notice that the two photons encoding  $|S_4\rangle_{1,4}$  are orthogonal in colour, and have never interacted.

Tests of multipartite nonlocality. Mermin tests let us verify the nonlocality of multipartite states $^{35,36}$ . We construct tests $^{32}$  comprising two and three measurement settings per qubit,  $\mathcal{M}_{II}^{G}$  and  $\mathcal{M}_{III}^{G}$ , based on the stabiliser observables of each graph state  $G$ . For convenience, we use  $\mathcal{M}_{II}^{G}$  and  $\mathcal{M}_{III}^{G}$  to indicate both the test's operator and the modulus of its expectation value (e.g.,  $|\langle \mathcal{M}_{II}^{G}|\rangle$ ). Results are listed in Table 1 and plotted in Fig. 2c.  $\mathcal{M}_{II}^{G}$  allows a choice, one for each graph symmetry, of stabilisers; we report

only the optimal choice here, though all choices exceed the classical bound. Other measurement results are reported in Supplementary Table 1. We find that  $|S_4\rangle$  exceeds both  $\mathcal{M}_{II}^{G} < 2$  and  $\mathcal{M}_{III}^{G} < 12$  classical bounds.  $|L_4\rangle$  exceeds the classical bound for  $\mathcal{M}_{II}^{G}$ , but not for the more strict  $\mathcal{M}_{III}^{G}$ . The higher postselection penalty of the controlled-  $Z$ , required to generate  $|L_4\rangle$ , results in a decreased fidelity, of which  $\mathcal{M}_{III}^{G}$  is a simple rescaling.

Understanding device performance. As quantum devices increase in complexity, the scaling of errors is of critical importance. The first step to correcting any error is to understand its source. Error models differ substantially between platforms, even within optics. Here, we develop methods for quantifying low-level performance parameters and apply these methods to our device. We seek to understand the effects of photon distinguishability, multiphoton noise, and thermo-optic phase error. Each effect is modelled independently. Since all effects contribute to the data, our estimates for each parameter are pessimistic. We apply Bayesian parameter estimation to learn the likeliest model parameters based on the four-photon stabiliser data<sup>37</sup>. The indistinguishability  $(\sigma)$ , multiphoton emission  $(p)$ , and random phase error  $(\delta)$ , are estimated with no prior assumptions. The resulting probability distributions of the three parameters are reported in Fig. 2e-g, for both  $|S_4\rangle$  and  $|L_4\rangle$ . Fitting each with a normal distribution, we compute parameter estimates and standard deviations:  $\sigma_{\mathrm{S,L}} = \{0.82 \pm 0.01, 0.82 \pm 0.01\}$ ,  $p_{\mathrm{S,L}} = \{0.036 \pm 0.009, 0.037 \pm 0.012\}$ , and  $\delta_{\mathrm{S,L}} = \{0.185 \pm 0.007$  rad,  $0.182 \pm 0.009$  rad\}. Our other measurements (HOM interference,  $g^{(2)}$ , source brightness, and cross-talk—see Methods) are compatible with

![](images/88c2873616e13e74b23e7520a8ecd123064103fdb26ec537fc42d026c9733786.jpg)

![](images/8db16cf64c1af3908f5a45c9ca142e0eb31abec24bdae43e17ee4b6ef78b2cab.jpg)

![](images/84762031409a0d2c9bd2b90f369c850a3fb455da60487c770703793c257a2d5d.jpg)

![](images/2698d5378f60c50c4a63e3096e8e77529398e31796d376a08a6ec03767337540.jpg)  
Fig. 2 Summary of experimental data. a, b Stabiliser observables of the star and line graph states,  $\langle S_4|g_iS_4\rangle$  and  $\langle L_4|g_iL_4\rangle$ , used to estimate state fidelity. Dashed lines indicate the  $F > 1/2$  threshold to witness genuine multipartite entanglement, where  $F = \text{mean}\{\langle g_i\rangle\}$ . The final bar of each plot,  $g_i g_i$ , is the identity for any  $i \in \{1, 2, 3, 4\}$ . c Mermin parameters  $\mathcal{M}_{II}^{G}$  and  $\mathcal{M}_{III}^{G}$  for the  $|S_4\rangle$  and  $|L_4\rangle$  states, estimated from stabilisers measurements. Local hidden variable bounds are indicated with a dashed line. Values are reported in Table 1. d On-chip Hong-Ou-Mandel interference, with HOM fringe visibility of  $V = 0.82 \pm 0.02$ . Probability distributions for the e indistinguishability, f source brightness, and g phase error, derived via a Bayesian parameter estimation method. All error bars represent the standard error of the mean, obtained from Monte Carlo simulations assuming a Poissonian distribution of the measured counts

![](images/665c7dd6e01b62fc6f428bda285cf6f2b09e546db7d39bdebd8cc02dd017728b.jpg)

![](images/98a8afeeb5020336c51534cf45f55e042c52fc3c4fde6522c1b1923ee773e3e1.jpg)

![](images/873fa4fc8cc0f013a9d2551971659e1ef26590ee2657972deccc243f47976509.jpg)  
Star state  
Line state

Table 1 Summary of measured parameters for on-chip graph states  

<table><tr><td>State</td><td>Fidelity</td><td>MGI2,4)</td><td>MIGIII</td><td>Count rate</td><td>Counts</td></tr><tr><td>|S4)</td><td>0.78 ± 0.01</td><td>3.17 ± 0.07</td><td>12.45 ± 0.13 (12, 16)</td><td>5.7 mHz</td><td>2640</td></tr><tr><td>|L4)</td><td>0.68 ± 0.02</td><td>2.61 ± 0.13</td><td>10.93 ± 0.29 (12, 16)</td><td>1.1 mHz</td><td>1085</td></tr><tr><td>|S4)1,3,4</td><td>0.77 ± 0.01</td><td>2.79 ± 0.09</td><td>6.16 ± 0.11 (6, 8)</td><td>3.3 mHz</td><td>1142</td></tr><tr><td>|S4)1,4</td><td>0.83 ± 0.02</td><td>-</td><td>3.32 ± 0.09 (2, 4)</td><td>4.0 mHz</td><td>416</td></tr><tr><td>|S4)3,4</td><td>0.83 ± 0.02</td><td>-</td><td>3.31 ± 0.09 (2, 4)</td><td>4.1 mHz</td><td>369</td></tr><tr><td>|Φ+)1,3</td><td>0.97 ± 0.01</td><td>2.79 ± 0.01a</td><td>3.90 ± 0.03 (2, 4)</td><td>1.8 kHz</td><td>38003</td></tr><tr><td>|Φ+)2,4</td><td>0.97 ± 0.01</td><td>2.71 ± 0.01a</td><td>3.88 ± 0.03 (2, 4)</td><td>1.9 kHz</td><td>41769</td></tr></table>

State f d   t  i th aIndicates a Bell-CHsH test. All error bars represent the standard error of the mean, obtained from Monte Carlo simulations assuming a Poissonian distribution of the measured counts

these estimates; the distributions for the two states,  $|S_4\rangle$  and  $|L_4\rangle$ , also broadly agree. This approach can reveal additional device performance information from existing data—no new measurements are required.

To completely describe device performance a holistic error model—one that simultaneously captures all the effects—is needed. To formulate such a model requires knowledge of difficult-to-access quantities and significant computational power. A distinguishability model, for example, must have the Schmidt spectrum of each source—inaccessible from simple HOM dips—and a common basis for them. Computationally, modelling variable, high photon-number states in high-dimensional spaces is a challenge. Moreover, the three effects we studied affected the observables in a similar way and depended on the state: a holistic model may not help to effectively distinguish these effects, but tailored or adaptive measurements may help.

# Discussion

High-fidelity is crucial for many quantum information processing applications. We demonstrate entangled resources of sufficient fidelity to violate several Mermin inequalities, though future scaling will need higher fidelity still. Improved throughput (lower loss) increases fidelity: directly, multiphoton noise scales with loss, due to an increase in the relative likelihood of a multiphoton term being detected; and indirectly, shorter integration times, via higher throughput and increased rates, yield improved stability and so reduced variation in system parameters (phase setting error, calibration, pump, fibre-chip coupling, detector efficiency, etc.). Using state-of-the-art silicon photonics and customised fabrication processes, four-fold coincidence rates could be propelled to the  $100\mathrm{-kHz}$  regime (see Supplementary Note 4). Finally, it should be noted that our observation of rates in the  $1\mathrm{-mHz}$  range are comparable to rates

observed in first experiments achieving historic increases in photon number (e.g., ref. 38).

We have demonstrated a multiphoton, multiqubit capability using standard, commercially available silicon photonic components. The techniques we have demonstrated—combining multiple postselected Bell-pairs in reconfigurable gates—can be applied to construct sophisticated chip-scale graph state generators. Although four is the largest number of dual-rail qubits for which all entanglement classes can be postselected, six- and eight-qubit devices can still access most classes: 10/11 and 73/101, respectively[25].

Although our postselection-reliant approach to sourcing photons and preparing entanglement is not scalable, scalable approaches (e.g., those using feedforward $^{39-41}$ ) must overcome many of the same challenges. We can now bring the reconfigurability and control of integrated photonics to bear on the exploration of multiphoton space. The combination of multiple photons and high-dimensional techniques $^{20}$  will soon make vast Hilbert spaces accessible. Ultimately, postselection lets us test the components and techniques key to unlocking the huge graph states needed for photonic quantum computation $^{41,42}$ .

Graph states are, and will continue to be, a building block of large-scale quantum technology. We have demonstrated a photonic generator of arbitrary graph states, in a miniature, high-performance technology. We have encoded quantum information in more than one pair of photons generated on a chip. Future increases in photon number depend principally on improving rates, by engineering photon throughput, and dispensing with postselection. This prototype represents the next step towards a future of large-scale quantum photonic devices.

# Methods

Experimental set-up. Pump pulses at  $1544.40\mathrm{nm}$  (1.1 ps pulse duration,  $500\mathrm{MHz}$  repetition rate) from an erbium-doped fibre laser (Pritel) are filtered with square-shaped,  $1.4\mathrm{-nm}$  -bandwidth filters and injected into the device. The average launched pump power is  $4.5\mathrm{mW}$ . The pump pulse spectrum and autocorrelation are shown in Supplementary Fig. 3. The  $\mathrm{sech}^2$  pulse duration is  $4.80\pm 0.03$  ps. Signal and idler photons are collected at pump-detuned  $\pm 4.8\mathrm{nm}$ , and filtered with square-shaped,  $0.7\mathrm{-nm}$  -bandwidth filters (Opneti DWDM) for spectral shaping and pump light rejection. They are detected off-chip by four superconducting nanowire single-photon detectors with  $80\pm 5\%$  efficiency (Photon Spot), operating around  $0.85\mathrm{K}$ . Time-tags are generated (UQD-Logic) and converted to coincidences by bespoke software. The device is mounted using thermal epoxy and wire-bonded to an FR4 printed circuit board; temperature is stabilised using a closed-loop thermoelectric cooler. Optical coupling to fibre is via a fibre V-groove array (OZ Optics) and a 6-axis piezo-electric actuator (Thorlabs). Analogue voltage drivers (Qontrol Systems) are used to drive the on-chip phase shifters, with 16-bit and  $300 - \mu \mathrm{V}$  resolution. The device was fabricated by the A\*STAR Institute of Microelectronics, Singapore. A  $220\mathrm{-nm}$  device layer performs waveguiding, atop a  $2\mathrm{-m}$  buried oxide (silicon-on-insulator) with an oxide top cladding. It has an area of  $1.4\times 3\mathrm{mm}^2$  with  $500\mathrm{-nm}$  wide waveguides. Kilohertz-bandwidth thermo-optic phase modulators are formed by TiN heaters,  $180\times 2\mu \mathrm{m}^2$ , positioned  $2\mu \mathrm{m}$  above the waveguide layer. See Supplementary Fig. 1 for a schematic of the experimental setup.

Phase shifter calibration and cross-talk. We calibrate the device's thermo-optic phase shifters by illuminating their enclosing MZIs with a continuous-wave laser at the relevant wavelength, and applying a range of voltages to produce a fringe at the MZI output. We fit this fringe with a function  $A \sin (f \cdot P(V) + \phi_0) + c$ , where  $P(V) = I(V) \cdot V$  is the Joule heating of the phase shifter, to find  $A, f, \phi_0$ , and  $c$ . By measuring the current-voltage relationship of the phase shifters and fitting them to  $I(V) = \rho_1 V + \rho_2 V^2 + \rho_3 V^3$ , we can 'dial in' a phase  $\phi_{\mathrm{d}}$  by numerically solving the quartic equation  $\phi_{\mathrm{d}} = f \cdot I(V) \cdot V + \phi_{\mathrm{c}}$ . Loss-matched, evanescently coupled waveguide taps with 2% transmission are strategically placed around the device to allow independent calibration of each on-chip phase shifter.

We measure the phase deviation within one on-chip demultiplexer per unit power dissipated in the other thermo-optic modulators. A thermal cross-talk coefficient of 0.003 rad  $\mathrm{mW}^{-1}$  results. The average power dissipated over all chip configurations used in the stabiliser measurements was 443 and  $472\mathrm{mW}$  for the star and line states, respectively. These distributions indicate an average deviation from the mean of 39 and  $22\mathrm{mW}$  for the two states. Working backwards, we estimate the average thermo-optic phase error is 0.12 rad and 0.065 rad,

respectively. Power histograms and cross-talk fringes are shown in Supplementary Fig. 6.

Loss. The device insertion loss is  $26.1\mathrm{dB}$  for the light path through source 1 to the  $|0\rangle$  output of qubit 1, after optimising the relevant phase settings. We estimate losses, based on measurements on test structures on the same die, as:  $4\mathrm{dB}$  per vertical grating coupler,  $0.65\mathrm{dB}$  per  $2\times 2$  multimode interferometer (MMI),  $3\mathrm{dB}$ $\mathrm{cm}^{-1}$  of straight waveguide propagation, and  $7.5\mathrm{dBcm}^{-1}$  of spiral waveguide propagation. All measurements are at  $1544.4\mathrm{nm}$ . By including off-chip losses (3 dB), input coupling (one grating, two MMIs), and one half of the source length, we estimate that signal photons experience a loss of  $19.3\mathrm{dB}$ .

HOM-fringe visibilities. In an ideal HOM fringe the maximum is twice the background 'distinguishable' level of an ideal HOM dip. To calculate the equivalent dip visibility  $V_{\mathrm{HOM}}$  from the maximum and minimum values measured in a fringe, we use  $V_{\mathrm{HOM}} = (N_{\mathrm{max}} / 2 - N_{\mathrm{min}}) / (N_{\mathrm{max}} / 2) = (N_{\mathrm{max}} - 2N_{\mathrm{min}}) / N_{\mathrm{max}}$ . More details are in Supplementary Note 2.

Measuring state fidelities. We wish to find the fidelity of our experimental state  $\rho_{\mathrm{ex}}$  with a graph state  $\rho$ , with stabilisers  $\{g_i\}$ . Since  $\rho$  is a stabiliser state,  $\rho = \frac{1}{2^n} \sum_i^{2^n} g_i$ . Hence,  $F = \operatorname{tr}[\rho_{\mathrm{ex}} \rho] = \frac{1}{2^n} \sum_i^{2^n} \operatorname{tr}[g_i \rho_{\mathrm{ex}}] = \frac{1}{2^n} \sum_i^{2^n} \langle g_i \rangle$  (see ref. 32). This measurement method is used for all reported state fidelities.

Local Pauli expectation values are measured by projecting each of the  $2^{n}$  eigenvectors onto each qubit's single output waveguide and counting  $n$ -fold coincidences (in our experiment,  $n = 4$ ). Summing the results of each projective measurement (total counts  $C_j$ ) by eigenvalue and normalising gives  $\langle g_i\rangle = \sum_j^{2^n}\lambda_jC_j / \sum_j^{2^n}C_j$ . Here the eigenvalue of stabiliser projector  $j$  is a product of its local components  $\lambda_{j} = \prod_{k}^{n}\mu_{j}^{(k)}$ , with  $\mu_j^{(k)}\in \{-1,1\}$  being the eigenvalue of the local operator on qubit  $k$ . Supplementary Note 5 contains a complete list of each state's stabilisers.

Mermin tests. For both  $|S_4\rangle$  and  $|L_4\rangle$ , we measure every two-setting Mermin test that can be composed from its stabilisers. The tests for the star state are as follows (graph symmetries are indicated by an arrow):  $\mathcal{M}_{II}^{S} = g_{4}(1 + g_{2}g_{3} + g_{2}g_{1} + g_{3}g_{1}), g_{4} \rightarrow g_{4}g_{1}$  and  $\mathcal{M}_{II'}^{S} = g_{4}(1 + g_{i})(1 + g_{j}), g_{4} \rightarrow g_{4}g_{k}$ , where  $g_{i}$  are the stabiliser generators and  $i, j, k = \{1, 2, 3\}$ . For the line state:  $\mathcal{M}_{II}^{L} = g_{1}(1 + g_{2})(1 + g_{3})$ , with  $g_{2} \rightarrow g_{2}g_{4}$  and  $\mathcal{M}_{II'}^{L} = g_{1}(1 + g_{3})(g_{2} + g_{4})$ , with  $g_{2} \rightarrow g_{2}g_{4}$ , and  $g_{i} \rightarrow gg_{i+1}$ , for  $i \in \{1, 2, 3, 4\}$ . Local-realistic ('classical') theories obey  $\mathcal{M}_{II}'^{G} < 2$ , while  $\mathcal{M}_{II}'^{G} < 4$  for quantum mechanics.

We also report a three-setting Mermin test:  $\mathcal{M}_{III}^{G} = \sum_{i}\langle g_{i}\rangle$ , where the sum is take over all the  $2^{n}$  (16) stabilisers of the graph state. Local-realistic theories obey  $\mathcal{M}_{III}^{G} < 12$ , while  $\mathcal{M}_{III}^{G} < 16$  for quantum mechanics.

Bayesian parameter estimation. We use three independent models to simulate the effects of partial distinguishability, multiphoton emission, and phase error (see Supplementary Note 6 for model details). These output a fourfold rate for each measurement setting, used to estimate a fidelity, for a range of  $\sigma$ ,  $p$ , and  $\delta$ . The phase error model was based on  $10^4$  normally distributed Monte Carlo samples for each chip configuration, with  $\delta$  the phase offset standard deviation. Data from each model is compared to the experimentally obtained data, and Bayesian inference learns the likeliest value for each parameter.

Consider a system described by a known model  $M(\sigma)$  with free parameter  $\sigma$ , a set of  $N$  observables  $\Pi = \{\pi_i\}_{i=1}^N$  and a data set  $X = \{x_i\}_{i=1}^N$ : the general aim of Bayesian parameter estimation is to find the parameter  $\bar{\sigma}$  that best describes the data outputted by the system. Learning  $\bar{\sigma}$  relies on the estimation of likelihoods, over a discretised space  $\{\sigma_k\}_{k=1}^K$  of  $K$  possible  $\sigma_k$ :  $L(\sigma_k) = \prod_{i=1}^N P(x_i|\sigma_k,\pi_i)$ , where  $P(x_i|\sigma_k,\pi_i)$  is the probability of observing  $x_i$  given model parameter  $\sigma_k$  and measured the observable  $\pi_i$ . This probability can be calculated from the frequency of the observed data  $x_i$  over many samples of simulated data  $\tilde{x}_i$ . We can therefore derive the probability of  $\sigma_k$  being the parameter that best describes the data by applying Bayes's rule:

$$
\begin{array}{l} P \left(\sigma_ {k} | X, \Pi\right) = \frac {P \left(X \mid \sigma_ {k} , \Pi\right) P \left(\sigma_ {k}\right)}{\sum_ {l = 1} ^ {K} P \left(X \mid \sigma_ {l} , \Pi\right) \times P \left(\sigma_ {l}\right)} \\ = \frac {\prod_ {i = 1} ^ {N} P \left(x _ {i} \mid \sigma_ {k} , \pi_ {i}\right)}{\sum_ {l = 1} ^ {K} \prod_ {i = 1} ^ {N} P \left(x _ {i} \mid \sigma_ {l} , \pi_ {i}\right)} = \frac {L \left(\sigma_ {k}\right)}{\sum_ {l = 1} ^ {K} L \left(\sigma_ {l}\right)}, \tag {3} \\ \end{array}
$$

thus retrieving a probability distribution for each parameter. We have assumed the measurements to be uncorrelated and the a priori distribution of the parameters  $P(\sigma_k)$  to be constant over the discretised range.

# Data availability

Data and computer code that support the findings of this study are available at the University of Bristol's data repository, data.bris (Digital object identifier: 10.5523/bris.2nk9fm85ssqaa2lyu4trhp5rqs). Other information is available from the authors upon reasonable request.

Received: 16 April 2019 Accepted: 25 June 2019

Published online: 06 August 2019

# References

1. Hein, M., Eisert, J. & Briegel, H. J. Multiparty entanglement in graph states. Phys. Rev. A. 69, 1-20 (2004).  
2. Hein, M., et al. Entanglement in graph states and its applications. Preprint at http://arxiv.org/abs/0602096 (2006).  
3. Raussendorf, R., Harrington, J. & Goyal, K. Topological fault-tolerance in cluster state quantum computation. New J. Phys. 9, 199-223 (2007).  
4. Georgescu, I. M., Ashhab, S. & Nori, F. Quantum simulation. Rev. Mod. Phys. 86, 153-185 (2014).  
5. Markham, D. & Sanders, B. C. Graph states for quantum secret sharing. Phys. Rev. A. 78, 042309 (2008).  
6. Walther, P. et al. Experimental one-way quantum computing. Nature 434, 169-176 (2005).  
7. Bell, B. et al. Experimental demonstration of a graph state quantum error-correction code. Nature Communications 5, 3658 (2014).  
8. Ciampini, M. A. et al. Path-polarization hyperentangled and cluster states of photons on a chip. Light.: Sci. Appl. 5, e16064 (2016).  
9. Zhang, C., Huang, Y.-F., Liu, B.-H., Li, C.-F. & Guo, G.-C. Experimental generation of a high-fidelity four-photon linear cluster state. Phys. Rev. A 93, 062329 (2016).  
10. Wang, Y., Li, Y. & Bei, Z. 16-qubit IBM universal quantum computer can be fully entangled. NPJ Quantum Inf. 4, 46 (2018).  
11. Alibart, O. et al. Quantum photonics at telecom wavelengths based on lithium niobate waveguides. J. Opt. 18, 104001 (2016).  
12. Politi, A., Cryan, M. J., Rarity, J. G., Yu, S. & O'brien, J. L. Silica-on-silicon waveguide quantum circuits. Science 320, 646-649 (2008).  
13. Crespi, A. et al. Suppression law of quantum states in a 3D photonic fast Fourier transform chip. Nat. Commun. 7, 10469 (2016).  
14. Spring, J. B. et al. Chip-based array of near-identical, pure, heralded single-photon sources. Optica 4, 90-96 (2017).  
15. Taballione, C., et al.  $8 \times 8$  Reconfigurable quantum photonic processor based on silicon nitride waveguides. Preprint at http://arxiv.org/abs/1805.10999v2 (2018).  
16. Dietrich, C. P., Fiore, A., Thompson, M. G., Kamp, M. & Höfling, S. GaAs integrated quantum photonics: towards compact and multi-functional quantum photonic integrated circuits. *Laser Photonics* Rev. **10**, 870–894 (2016).  
17. Sibson, P. et al. Chip-based quantum key distribution. Nat. Commun. 8, 13984 (2017).  
18. Silverstone, J. W., Bonnaue, D., O'Brien, J. L. & Thompson, M. G. Silicon quantum photonics. IEEE J. Sel. Top. Quant. Elect. 22, 390-402 (2016).  
19. Silverstone, J. W. et al. On-chip quantum interference between silicon photon-pair sources. Nat. Photonics 8, 104-108 (2014).  
20. Wang, J., et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, eaar7053 (2018).  
21. Sun, J., Timurdogan, E., Yaacobi, A., Hosseini, E. S. & Watts, M. R. Large-scale nanophotonic phased array. Nature 493, 195 (2013).  
22. Chung, S., Abediasl, H. & Hashemi, H. A monolithically integrated large-scale optical phased array in silicon-on-insulator cmos. IEEE J. Solid-State Circuits 53, 275-296 (2018).  
23. Harris, N. C., et al. Quantum transport simulations in a programmable nanophotonic processor. Nature Photonics 103, 090504-452 (2017).  
24. Faruque, I. I., Sinclair, G. F., Bonnaueau, D., Rarity, J. G. & Thompson, M. G. On-chip quantum interference with heralded photons from two independent micro-ring resonator sources in silicon photonics. Opt. Express 26, 20379-20395 (2018).  
25. Adcock, J. C., Morley-Short, S., Silverstone, J. W. & Thompson, M. G. Hard limits on the postselectability of optical graph states. Quantum Sci. Technol. 4, 015010 (2018).  
26. Sharping, J. E. et al. Generation of correlated photons in nanoscale silicon waveguides. Opt. Express 14, 12388-12393 (2006).  
27. Hong, C. K., Ou, Z. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044 (1987).  
28. Vergyris, P. et al. On-chip generation of heralded photon-number states. Sci. Rep. 6, 35975 (2016).  
29. Christ, A., Laiho, K., Eckstein, A., Cassemiro, K. N. & Silberhorn, C. Probing multimode squeezing with correlation functions. New J. Phys. 13, 033027 (2011).

30. Christensen, J. B., Koefoed, J. G., Rottwitt, K. & McKinstrie, C. J. Engineering spectrally unentangled photon pairs from nonlinear microring resonators by pump manipulation. Opt. Lett. 43, 859-862 (2018).  
31. Vernon, Z. et al. Truly unentangled photon pairs without spectral filtering. Opt. Lett. 42, 3638-3641 (2017).  
32. Gühne, O. & Toth, G. Entanglement detection. Phys. Rep. 474, 1-75 (2009).  
33. Zhao, Z. et al. Experimental violation of local realism by four-photon Greenberger-Horne-Zeilinger entanglement. Phys. Rev. Lett. 91, 180401 (2003).  
34. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188 (2001).  
35. Walther, P., Aspelmeyer, M., Resch, K. J. & Zeilinger, A. Experimental violation of a cluster state bell inequality. Phys. Rev. Lett. 95, 020403 (2005).  
36. Ciampini, M. A. et al. Experimental nonlocality-based network diagnostics of multipartite entangled states. Sci. Rep. 7, 17122 (2017).  
37. Barber, D. Bayesian Reasoning and Machine Learning (Cambridge University Press, Cambridge, England, 2012).  
38. Bouwmeester, D. et al. Experimental quantum teleportation. Nature 390, 575 (1997).  
39. Knill, E., Laflamme, R. & Milburn, G. J. A scheme for efficient quantum computation with linear optics. Nature 409, 46-52 (2001).  
40. Gimeno-Segovia, M. et al. Relative multiplexing for minimising switching in linear-optical quantum computing. New J. Phys. 19, 063013 (2017).  
41. Gimeno-Segovia, M., Shadbolt, P., Browne, D. E. & Rudolph, T. From three-photon Greenberger-Horne-Zeilinger states to ballistic universal quantum computation. Phys. Rev. Lett. 115, 020502 (2015).  
42. Rudolph, T. Why I am optimistic about the silicon-photonic route to quantum computing. APL Photonics 2, 030901 (2017).

# Acknowledgements

This work was possible with the invaluable help of Damien Bonneau, Chris Sparrow, Mercedes Gimeno-Sergovia, Sam Pallister, Will McCutcheon, Stefano Paesani, Eric Johnston, Laurent Kling, Graham D. Marshall, and John G. Rarity. It was generously supported by EPSRC Programme Grant EP/L024020/1, the EPSRC Quantum Engineering Centre for Doctoral Training EP/L015730/1, and the ERC Starting Grant ERC-2014-STG 640079. J.W.S. acknowledges the generous support of the Leverhulme Trust, through Leverhulme Early Career Fellowship ECF-2018-276. MGT acknowledges support from EPSRC Early Career Fellowship EP/K033085/1.

# Author contributions

J.W.S., R.S. and J.C.A. conceived the device. J.C.A. and C.V. designed and carried out the experiments and experimental modelling. J.W.S. and M.G.T. supervised the project. All authors analysed the results and wrote the manuscript.

# Additional information

Supplementary Information accompanies this paper at https://doi.org/10.1038/s41467-019-11489-y.

Competing interests: The authors declare no competing interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

Peer review information: Nature Communications thanks the anonymous reviewers for their contribution to the peer review of this work.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/bacf3c6a64630983b8cb835bf6a57d06f7fbe140df603898a991dee0997b11b7.jpg)

Open Access This article is licensed under a Creative Commons

Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2019