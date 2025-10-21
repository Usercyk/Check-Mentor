ARTICLE

https://doi.org/10.1038/s41467-020-16187-8

OPEN

![](images/b2985c2e514637f7594fed3c9caa3a73dad7f478566f2617c7c04be8b022210c.jpg)

Check for updates

# Near-ideal spontaneous photon sources in silicon quantum photonics

S. Paesani $^{1,4}$ , M. Borghi $^{1,2,4}$ , S. Signorini $^{3,4}$ , A. Mainos $^{1}$ , L. Pavesi $^{3}$  & A. Laing $^{1}$

While integrated photonics is a robust platform for quantum information processing, architectures for photonic quantum computing place stringent demands on high quality information carriers. Sources of single photons that are highly indistinguishable and pure, that are either near-deterministic or heralded with high efficiency, and that are suitable for mass-manufacture, have been elusive. Here, we demonstrate on-chip photon sources that simultaneously meet each of these requirements. Our photon sources are fabricated in silicon using mature processes, and exploit a dual-mode pump-delayed excitation scheme to engineer the emission of spectrally pure photon pairs through inter-modal spontaneous four-wave mixing in low-loss spiralled multi-mode waveguides. We simultaneously measure a spectral purity of  $0.9904 \pm 0.0006$ , a mutual indistinguishability of  $0.987 \pm 0.002$ , and  $>90\%$  intrinsic heralding efficiency. We measure on-chip quantum interference with a visibility of  $0.96 \pm 0.02$  between heralded photons from different sources.

Sustained progress in the engineering of platforms for quantum information processing has recently achieved a scale that surpasses the capabilities of classical computers to solve specialised and abstract problems $^{1-4}$ . But while achieving a computational advantage for practical or industrially relevant problems may be possible with further scaling of special purpose NISQ (noisy intermediate scale quantum) devices $^{1}$ , more general purpose quantum computers will require a hardware platform that integrates millions of components, individually operating above some fidelity threshold $^{5,6}$ . Silicon quantum photonics $^{7}$ , which is compatible with complementary metal-oxide-semiconductor (CMOS) fabrication, provides a potential platform for very large-scale quantum information processing $^{8-10}$ .

All-photonic quantum computing architectures rely on arrays of many photon sources to achieve combinatorial speed-ups in quantum sampling algorithms $^{11,12}$ , or to approximate an on-demand source of single photons $^{13-15}$ , and supply entangling circuitry for general purpose quantum computing $^{8,16}$ . In the former case, the level of indistinguishability among photons upper bounds the computational complexity of sampling algorithms $^{17}$ ; in the latter case, photon impurity and distinguishability lead to logical errors $^{16,18}$ . Furthermore, and in general, lossy or inefficient heralding of photons vitiates the scaling of photonic quantum information processing. The lack of a demonstration that simultaneously overcomes all of these challenges has been a bottleneck to scalability for quantum computing in integrated photonics.

Progress in solid-state sources of single photons make quantum dots an attractive approach for certain NISQ experiments[19,20]. However, the low-loss integration of solid-state sources into photonic circuitry, that maintains distinguishability over many photons, is an ongoing challenge[21,22]. Integrated sources of photons based on spontaneous processes, such as four-wave mixing (SFWM) in single-mode waveguides or micro-ring cavities[7,23] are appealing for their manufacturability. However, spontaneous sources incur limitations to purity and to heralding efficiency[23], with micro-ring cavities additionally requiring resonance tuning to avoid distinguishability among different cavities[24,25].

Here, we demonstrate the engineering of a CMOS-compatible source of heralded single photons using silicon photonics, which simultaneously meets the requirements for scalable quantum photonics: high purity, high heralding efficiency, and high indistinguishability.

The source is based on inter-modal SFWM, where phase-matching is engineered by propagating the pump in different transverse modes of a spiralled multi-mode (MM) waveguide[26].

# Results

Discrete-band inter-modal SFWM phase-matching and delayed-pump scheme. Integrated photon sources in silicon are based on SFWM, where, if phase-matching (momentum conservation) and energy conservation conditions are satisfied, light from a pump laser can be converted into pairs of single photons[23,27]. In standard SFWM in single-mode waveguides, near-zero dispersion produces broad phase-matching bands around the pump wavelength, such that the process, dominated by energy conservation conditions, induces undesired strong spectral anticorrelations between the emitted photons. In contrast, in this work we suppress such correlations adopting a inter-modal approach to SFWM. As shown in Fig. 1a, an input pulsed laser coherently pumps the two lowest order transverse magnetic (TM) modes of a MM waveguide, namely TM0 and TM1 (see Fig. 1a inset), and generates pairs of idler and signal photons in these modes via inter-modal phase-matching. The dispersion

relations between the TM0 and TM1 modes are such that a discrete narrow phase-matching band appears $^{26}$ . By tailoring the waveguide cross-section, the modal dispersion can be accurately engineered to design the phase-matching band with a bandwidth similar to the pump bandwidth (related to energy conservation). This suppresses the frequency anticorrelations imposed by energy conservation, and enhances the spectral purity of the emitted photons $^{26}$ . In particular, we exploit the different modal group velocities in silicon waveguides to achieve a condition where the idler and signal photons are generated on TM0 at  $\simeq 1516$  nm and on TM1 at  $\simeq 1588$  nm, respectively, with a bandwidth of approximately  $4\mathrm{nm}$  (see Supplementary Note 1).

Moreover, to obtain a near-unit spectral purity, we further suppress residual correlations in the joint spectrum by inserting a delay  $\tau$  on the TM0 component of the pump (with higher group velocity than TM1) before injecting it in the source. The delay gradually increases and decreases the temporal overlap between the pump in the TM0 and TM1 modes along the multi-modal waveguide source (colour-coded in Fig. 1a). This results in an adiabatic switching of non-linear interactions in the source, which suppresses spurious spectral correlations[28,29]. Simulations (see Supplementary Note 1) predict a spectral purity of  $99.4\%$  in this configuration, in contrast to the case where no delay is applied, which predicts a purity of  $84.0\%$ , as shown in Fig. 1b.

Source design. Figure 1c, shows the compact footprint for the MM waveguide source obtained by adopting a spiral geometry. The delayed-pump excitation scheme is implemented in three stages, as shown in Fig. 1a. The pump, initially in TM0, is split by a balanced beam-splitter; one arm receives a delay of  $\tau$  with respect to the other, then the two arms are recombined using a TM0 to TM1 mode converter, and injected in the MM waveguide. Once generated, the signal photon is separated from the idler via a second TM1 to TM0 mode converter. After processing, signal and idler photons are out-coupled to fibres, where the pump is filtered out via broad-band fibre bragg-gratings, and single photons are detected with superconducting-nanowire single photon detectors (SNSPDs).

Source brightness characterisation. We experimentally characterised the squeezing value  $\xi$  of the generated two-mode squeezed state emitted from individual sources with second-order correlation measurements $^{30}$  (see Supplementary Note 5). Fig. 1e compares results for both the delayed and the non-delayed cases. Experimental results confirm our simulations and additionally demonstrate higher brightness as a benefit of the temporal delay scheme (see Supplementary Note 1). Squeezing values up to  $|\tanh (\xi)|^2\simeq 0.2$  are observed using a small input (off-chip) average pump power of  $3\mathrm{mW}$ , corresponding to  $>8\mathrm{MHz}$  photon-pair generation rates on-chip. To reduce noise from multi-photon events, measurements reported from this point on are performed with an input pump power of approximately  $0.5\mathrm{mW}$ : coincidence rates are measured at  $15\mathrm{kHz}$ , with heralded single photon  $g_{\mathrm{h}}^{(2)}$  measured at  $0.053(1)$  (Fig. 1e inset).

Spectral purity characterisation. Source purity is first estimated from a direct measurement of the joint spectral intensity (JSI) $^{31}$ . The JSI reconstruction is implemented using narrow-bandwidth tunable filters to scan the emitted wavelengths of the signal and idler photons, as pictured in Fig. 1f. Data from a source with no temporal delay yields a JSI with a spectral purity of  $93.1(2)\%$ , which increases to  $99.04(6)\%$ , in the scheme with a delay, as shown in Fig. 1g. The contrasting measurements show a clear suppression of spurious correlations with the delay scheme. A second estimation of the emitted single photon purity

![](images/1bdf13bf32d15cec73f9ff561a6e093fbe81cbc641db8f582f4d295467717357.jpg)

![](images/1c0dd52b96dd3697e717a06ebe875009fce0f8eba8f92736be11a60a4afad570.jpg)

![](images/a4d7f6d9cb758adfaf89d0dda3b89c0e8b9a038d8b31f142eaf0db09db92b65f.jpg)

![](images/d76d2825d69a9b61125064cfec79f3c424606d7dff6a17ffb1df983d7b022b6c.jpg)

![](images/955b571f5b79dada077eaf7d93b8e70e8f5b87c3977235ddf395fab912f6b054.jpg)

![](images/e86c436256a2e1e04a5e73531a45458107c80ea44d83f42746c4c03e0104c263.jpg)  
Fig. 1 Design and performance of the multi-modal source. a Schematic of the source. An input near-1550 nm pulsed pump laser (4.5 nm bandwidth), initially propagating in the TMO mode, is split using a 50:50 beam-splitter (BS). The output in the upper arm of the BS is converted into the TM1 mode via a mode-converter (MC), while the TMO output in the lower arm is delayed by a time  $\tau = 1.46$  ps. Due to the different group velocities, the two modes become overlapped and subsequently diverge again while propagating through the source, as qualitatively colour-coded in the figure. Photon pairs, with the signal photon (near 1588 nm) in the TM1 mode and the idler photon (near 1516 nm) in the TMO mode, are emitted via inter-modal SFWM and finally deterministically separated via a MC. Inset: cross sections of the TMO and TM1 modes in the MM waveguide. b Simulated JSI of the source in the presence of a delay  $\tau = 1.46$  ps (left) and with no delay (right), with corresponding single photon purities of  $99.4\%$  and  $84.0\%$ . c Optical microscope image of a single multi-modal source structure-waveguides are highlighted. d Set-up to characterise squeezed light via second-order correlation measurements, using a polarisation controller (PC), fibre pass-band filter (F), variable optical attenuator (VOA), and an optical power monitor (PM). e Measured squeezing as a function of (off-chip) pump power. Blue and red points are data measured in a source with and without delay, respectively, with a fit shown as a black line. The stars indicate the typical operating regime. Inset: measured heralded  $g_{\mathrm{h}}^{(2)}(0)$  as a function of input powers. f Set-up for the characterisation of the emitted JSI, using a tunable filter (TF). g Measured JSI from the source with delay (left) and without delay (right), with respective corresponding spectral purities of 0.9904(6) and 0.931(2). h Set-up for purity characterisation via unheralded second-order correlation measurements. Idler photons are discarded via an absorbing termination (AT). i Measured unheralded  $g_{\mathrm{u}}^{(2)}(\Delta t)$  in the source with delay. Each bar corresponds to a coincidence window of 2 ns (inset). The measured  $g_{\mathrm{u}}^{(2)}(0) = 1.97(3)$  corresponds to a photon spectral purity of 0.97(3). Error bars represent 1 s.d. and are calculated assuming Poissonian error statistics.

![](images/e7eeebbcbd9d4f4cd31072a97e315b519c8268e2dc87d389856d63e331fd10f5.jpg)

![](images/498abb0eb23b8d26c5946b26a4a740eb54320a50ffe27351984ef453d18da372.jpg)

for the delayed structure is performed via unheralded second-order correlation measurements  $g_{\mathrm{u}}^{(2)}$  [30]. These are implemented by dividing the output signal mode with an off-chip balanced fibre beam-splitter and measuring coincidences between the two output arms (see Fig. 1h). Measured unheralded second order-correlation values are reported in Fig. 1i. We obtain  $g_{\mathrm{u}}^{(2)}(0) = 1.97(3)$ , which corresponds to a single photon purity of  $97(3)\%$ , consistent with the value obtained from the JSI.

Heralding efficiency characterisation. The capability of the sources to generate pure photons with no requirement for filtering enables the simultaneous achievement of high heralding efficiency and high purity. In our experiment, off-chip filters are used solely for pump rejection: their bandwidth (12 nm, flat transmission) contains  $>99\%$  of the emitted spectra, which results in ultra-high filtering heralding efficiency[32]. While the effect of filtering is thus negligible, the intrinsic heralding efficiency of the source is affected by linear and non-linear transmission losses inside the waveguide. These losses are, however, greatly mitigated in MM waveguides (which present  $<0.5$  dB/cm linear loss, see Supplementary Note 2). Taking into account the characterised losses, we estimate a heralding efficiency of approximately  $95\%$

for an individual source. The measured heralding efficiency at the off-chip detectors is  $12.6(2)\%$ , corresponding to  $91(9)\%$  on-chip intrinsic heralding efficiency after correcting for the characterised losses in the channel to the detectors (see Supplementary Note 2), which can be highly suppressed by implementing low-loss off-chip couplers $^{33}$  or with integrated detectors $^{34}$ .

Source indistinguishability characterisation. To experimentally test the source indistinguishability we integrate a reconfigurable photonic circuit to perform quantum interference between different sources. Schematics of the circuit are shown in Fig. 2a-b. Two sources are coherently pumped by splitting the input laser with an on-chip tunable Mach-Zehnder interferometer (MZI); the resulting idler and signal modes from the different sources are grouped and interfered on-chip using additional integrated phase-shifters and MZIs (see Methods). Using this circuit, we experimentally estimate the indistinguishability among the sources using three different types of measurements. First, we reconstruct the JSI of each source by operating the two sources individually. The overlap of the JSIs reconstructed from each source (Fig. 2c) estimates a mutual indistinguishability of  $98.5(1)\%$ .

![](images/69b244fa6a87139c0aaaa7f209bd6209785fcdc35d440325ff36068139b1b114.jpg)

![](images/354c4102a6efb7a7ad24e9cd498d89a295dda000a9747e1461d232b1b730db81.jpg)  
Fig. 2 Multiple sources and indistinguishability characterisation. a Optical microscope image of the device for the coherent pumping of two sources and processing of the emitted photons. Input pump light is split between the two sources via an input MZI. Waveguide crossings are used to group the signal and idler photons emitted from both sources, and arbitrary unitary operations on signals (idlers) are implemented via a phase-shifter  $\phi_{1}(\phi_{2})$  and a MZI with internal phase  $\theta_{1}(\theta_{2})$ . b Schematic of the integrated circuit and set-up to characterise the indistinguishability between the sources. c Individual JSIs measured with separate pumping of source 1 (top panel) and source 2 (bottom panel). The indistinguishability of the two measured spectra, calculated with the overlap of the two JSIs, is 0.985(1). d Measured reverse-HOM fringe from the two sources. Error bars, from Poissonian photon statistics, are smaller than markers. The fringe visibility, which corresponds to source indistinguishability, is 0.987(2). e Density matrix of the two-qubit entangled state obtained when coherently pumping the two sources, reconstructed via quantum state tomography. Fidelity with the ideal state  $|\Phi_{+}\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$ , pictured as transparent bars, is 0.989(3). The source indistinguishability inferred from the tomography is 0.982(6).

![](images/ab3524956f03ebd8e2a87f375fad52db7cc4e27b9944bac75297db9cdf1604ea.jpg)

![](images/a51e607b2eea82be80698a3f8bebac585bfe877b5b4d20ca96c3fcf5eef2e993.jpg)

![](images/c6b2e11cc9a48115da647c642d5c44c9851f513b07504539c70ac93e4c529dc5.jpg)

A second measurement of the indistinguishability was performed via reversed Hong-Ou-Mandel (HOM) interference between the two sources[9,35,36]. Both sources were pumped and the respective idler and signal modes were interfered by tuning the output MZIs to act as 50:50 beam-splitters. The  $98.7(2)\%$  visibility of the reversed HOM fringe, shown in Fig. 2d and obtained by scanning the phases  $\phi_{1} = \phi_{2} = \phi$ , corresponds directly to the source indistinguishability (see Supplementary Note 6).

A further estimate of indistinguishability is obtained by testing the entanglement generated when coherently pumping the two sources $^{9,36}$ . Using quantum state tomography, we experimentally reconstruct the density matrix shown in Fig. 2e, which has a fidelity of  $98.9(3)\%$  with the ideal maximally-entangled state  $\left|\Phi_{+}\right\rangle = \left(|00\rangle +|11\rangle\right) / \sqrt{2}$ , and provides an indistinguishability value of  $98.2(6)\%$  (see Supplementary Note 6 for details).

Herald ed Hong-Ou-Mandel experiments. A key figure of merit for multi-photon experiments, particularly in the context of many photon quantum information processing, is the heralded Hong-Ou-Mandel visibility, which quantifies the interference of photons heralded from different sources. This quantity, which simultaneously incorporates source indistinguishability, purity and absence of multi-photon noise, determines the stochastic noise in photonic quantum computing architectures[8,18], and the computational complexity achievable in photonic sampling algorithms[17]. We implemented heralded HOM experiments by operating our two-source device in the four-photon regime, as shown in Fig. 3a. The circuit is configured such that idler photons from both sources are directly out-coupled to detectors to herald the signal photons, which are interfered in the MZI (see inset of Fig. 3b). The heralded HOM fringe is measured by scanning the phase  $\theta_{1}$  inside the MZI and collecting 4-photon events[37,38]. The measured on-chip heralded HOM fringe is shown in Fig. 3b. The raw-data visibility (no multi-photon noise correction) is  $96(2)\%$ .

![](images/120996cef0f49ea8e4e6f192348cb2255ddd405c01361f2af8a3e637d9e2e916.jpg)

![](images/dbb3b2975b501e1ee5d3aabe949fc77c4f7a84bf7b11b1dcc68d79626b269f82.jpg)  
Fig. 3 Heralded Hong-Ou-Mandel interference. a Experimental setup for 4-photon heralded HOM experiments. b Heralded HOM results. Points are raw four-photon counts measured over 4-h of integration time each for different values of the MZI phase  $\theta$ , with a solid line fit to the data, presenting a visibility of 0.96(2). Error bars represent 1 s.d. and consider Poissonian photon statistics. Inset: schematic of the integrated circuit configuration for measuring the heralded HOM fringe.

# Discussion

Our results have a significant impact on the prospects of quantum information processing in integrated photonics. Photon sources from previous state-of-the-art integrated photonic devices demonstrated an on-chip heralded quantum inference raw

visibility of  $82\%^{38}$  which upper-bounds any potential quantum sampling experiment to a computational complexity equivalent to 31-photon interference (considering error bounds of  $10\%^{17}$ ). Our results lift this bound to a computational complexity equivalent to  $>150$  photon interference (see Supplementary Note 4), deep in the regime of quantum computational supremacy<sup>39</sup>.

Furthermore, in the context of digital quantum computing, our results make a significant leap toward the  $\gtrsim 99.9\%$  heralded HOM visibility required to construct lattices of physical qubits with error rates below  $1\%$  using current fault-tolerance photonic architectures[16,18]. Our analysis (see Supplementary Note 3) suggests that heralded HOM visibilities of  $99.9\%$  could be achievable with minor modifications to our design; for example by using an improved quality pump laser and by using semiconductor fabrication processes with approximately  $4\mathrm{nm}$  uniformity[40,41]. Our results represent the near removal of a critical set of physical errors that had limited the scaling of photonic quantum information processing.

# Methods

Device fabrication. The silicon devices used were fabricated using CMOS-compatible UV-lithography processes in a commercial multi-project wafer run by the Advanced Micro Foundry (AMF) in Singapore. Waveguides are etched in a  $220\mathrm{nm}$  silicon layer atop a  $2\mu \mathrm{m}$  buried oxide, and an oxide top cladding of  $3\mu \mathrm{m}$ . The thermo-optic phase-shifters to reconfigure the integrated circuits are formed by TiN heaters positioned  $2\mu \mathrm{m}$  above the waveguide layer.

Inter-modal four-wave mixing in silicon waveguides. Inter-modal spontaneous four-wave mixing is performed by propagating the pump, signal and idler waves on different waveguide modes. The spectral properties of the perfect phase matching depend on the group velocity dispersion of the different modes employed in the process, which can be tuned by engineering the waveguide geometry. In our experiment, we operate the pump on the TM0 and TM1 modes, and the signal and idler on the TM1 and TM0, respectively. With these modes, phase matching of the SFWM process is enabled in the  $1500 - 1600\mathrm{nm}$  spectral window using standard silicon-on-insulator waveguides with a geometry of  $2\mu \mathrm{m} \times 0.22\mu \mathrm{m}$ , which is used in our source design.

Pump-delayed generation. When a delay is applied between non-degenerate pump pulses, the effective interaction length depends on the value of such delay. This is due to the walk-off, which limits the nonlinear length. The best scenario is when the overtaking process of the faster pulse over the slower one occurs completely within the waveguide, thus maximising the interaction length and the generation efficiency. In this case the delay is such that the maximum spatial overlap between the pump pulses occurs in the middle of the waveguide. With different delays, the nonlinear medium is not optimally exploited, resulting in reduced generation efficiency. The delay used to optimise the generation efficiency corresponds to the delay for maximum spectral purity (details in Supplementary Note 1).

Source design. The  $2\mu \mathrm{m}\times 0.22\mu \mathrm{m}$  multi-mode waveguide in the source is designed with a length of  $11\mathrm{mm}$  and an initial temporal delay of  $\tau = 1.46$  ps between the TM0 and TM1 modes. A spiral geometry for the waveguide is used to increase the compactness. Modal cross-talk in the spiral is kept below  $-25\mathrm{dB}$  extinction by adopting  $90^{\circ}$  Euler bends of radius  $45\mu \mathrm{m}$  (see Supplementary Note 1 for more details). The footprint of an individual silicon-on-insulator source with our design is approximately  $200\mu \mathrm{m}\times 900\mu \mathrm{m}$ . The TM0-TM1 mode converters used to inject the pump in the MM waveguide and separate the signal and idler photons at the output have  $\ll -30$  dB characterised modal cross-talk, and  $>95\%$  conversion efficiency.

Integrated circuit. The integrated circuit pictured in Fig. 2a (see also Supplementary Fig. 6 for a more detailed schematic) used for the multi-source interference experiments consists of three reconfigurable MZIs (internal phases  $\varphi$ ,  $\theta_{1}$  and  $\theta_{2}$ ), two phase-shifters  $(\phi_{1},\phi_{2})$ , a broad-band waveguide crosser, and two sources. The circuit used is a two-mode version of the circuits implemented, for example, in ref.  $^{9}$ . At the input, the MZI  $\varphi$  is configured to split the pump between the two sources: using  $\varphi = 0$  ( $\varphi = \pi$ ) we operate the sources individually by pumping only source 1 (source 2), while  $\varphi = \pi /2$  implements a balanced pump splitting to coherently operate both sources simultaneously. When uniformly pumping both sources ( $\varphi = \pi /2$ ), each source receives half of the input pump power, and thus the photon-pair generation probability in each source is decreased by a factor four compared to the single source regime. After photons are generated in the sources, the waveguide crosser allows us to route together to signal and idler

modes. Arbitrary and reconfigurable two-mode unitary operations are then performed on the signal (idler) modes via the phase  $\phi_{1}$  ( $\phi_{2}$ ) and the MZI  $\theta_{1}$  ( $\theta_{2}$ ). Light is coupled in and out of the circuit by means of TM0 focusing grating couplers, which have been individually optimised to maximise their efficiency at the pump, signal and idler wavelengths ( $\simeq 6.6$  dB loss per coupler). The coupling was observed to be stable over few hours, but to gradually decrease over longer periods (approximately between 0.5 and 1 dB/day without active coupling optimisation). Insertion losses for the individual on-chip circuit components in our devices are:  $0.19\mathrm{dB/cm}$  ( $0.40\mathrm{dB/cm}$ ) for TM0 (TM1) transmission in the MM waveguide,  $0.1\mathrm{dB}$  per mode converter,  $< 0.01\mathrm{dB}$  loss per directional coupler, and  $0.4\mathrm{dB}$  per waveguide crossing.

Total insertion losses in the integrated circuit are approximately 14 dB, mostly due to grating couplers. In both the single-source circuit (Fig. 1b) and the two-source circuit (Fig. 2a) the intrinsic heralding efficiencies of the sources have been measured to be approximately the same, with a near-90% efficiency after correcting for the off-chip channel loss. Off-chip pump rejection filters have an insertion loss for the unfiltered photons of 0.4 dB. When including this external transmission loss for pump rejection, the heralding efficiency of the systems is approximately 83%. See Supplementary Note 2 for more details on the design and characterisation of the individual components.

Experimental set-up. Pump pulses at  $1550\mathrm{nm}$  (4.5 nm bandwidth, 800 fs pulse length, 50 MHz repetition rate) from an erbium-doped fibre laser (Pritel) are filtered via a square-shaped, 5 nm bandwidth filter (Semrock) to eliminate spurious tails at the signal and idler wavelengths, and then injected into the device. A fibre polarisation controller (Lambda) is used to ensure injection of TM0 polarised light to maximise the coupling. After the chip, pump rejection is performed via broadband ( $>12\mathrm{nm}$  bandwidth, much larger than the photon spectra) band-pass filters (Opneti), and photons are finally detected using superconducting nanowire single-photon detectors with approximately 80% average efficiency (Photon Spot). For the JSI reconstruction, we use tunable filters with adjustable bandwidth (EXFO XTA-50). Analogue voltage drivers (Qcontrol Systems,  $300\mu V$  resolution) are used to drive the on-chip phase shifters and reconfigure the integrated circuit.

# Data availability

The data that support the plots within this paper and other findings of this study are available at [https://doi.org/10.6084/m9.figshare.11882760].

Received: 13 December 2019; Accepted: 6 April 2020

Published online: 19 May 2020

# References

1. Preskill, J. Quantum computing in the nisq era and beyond. Quantum 2, 79 (2018).  
2. Bernien, H. et al. Probing many-body dynamics on a 51-atom quantum simulator. Nature 551, 579-584 (2017).  
3. Arute, F. et al. Quantum supremacy using a programmable superconducting processor. Nature 574, 505-510 (2019).  
4. Wang, H. et al. Boson sampling with 20 input photons and a 60-mode interferometer in a  $10^{14}$  -dimensional hilbert space. Phys. Rev. Lett. 123, 250503 (2019).  
5. Reiher, M., Wiebe, N., Svore, K. M., Wecker, D. & Troyer, M. Elucidating reaction mechanisms on quantum computers. PNAS 114, 7555-7560 (2017).  
6. Gidney, C. & Ekerä, M. How to factor 2048 bit rsa integers in 8 hours using 20 million noisy qubits. Preprint at arXiv 1905.09749 (2019).  
7. Silverstone, J. W., Bonnaue, D., O'Brien, J. L. & Thompson, M. G. Silicon quantum photonics. IEEE J. Sel. Top. Quantum Electron. 22, 390-402 (2016).  
8. Rudolph, T. Why i am optimistic about the silicon-photonic route to quantum computing. APL Photon. 2, 030901 (2017).  
9. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 360, 285-291 (2018).  
10. Paesani, S. et al. Generation and sampling of quantum states of light in a silicon chip. Nat. Phys. 15, 925-929 (2019).  
11. Lund, A. P. et al. Boson sampling from a gaussian state. Phys. Rev. Lett. 113, 100502 (2014).  
12. Hamilton, C. S. et al. Gaussian boson sampling. Phys. Rev. Lett. 119, 170501 (2017).  
13. Pittman, T. B., Jacobs, B. C. & Franson, J. D. Single photons on pseudodemand from stored parametric down-conversion. Phys. Rev. A 66, 042303 (2002).  
14. Migdall, A. L., Branning, D. & Castelletto, S. Tailoring single-photon and multiphoton probabilities of a single-photon on-demand source. Phys. Rev. A 66, 053805 (2002).

15. Kaneda, F. & Kwiat, P. G. High-efficiency single-photon generation via large-scale active time multiplexing. Sci. Adv. 5, eaaw8586 (2019).  
16. Gimeno-Segovia, M., Shadbolt, P., Browne, D. E. & Rudolph, T. From three-photon greenberger-horne-zeilinger states to ballistic universal quantum computation. Phys. Rev. Lett. 115, 020502 (2015).  
17. Renema, J. J. et al. Efficient classical algorithm for boson sampling with partially distinguishable photons. Phys. Rev. Lett. 120, 220502 (2018).  
18. Sparrow, C. Quantum Interference in Universal Linear Optical Devices for Quantum Computation and Simulation. Ph.D. thesis, Department of Physics, Imperial College London (2018).  
19. Somaschi, N. et al. Near-optimal single-photon sources in the solid state. Nat. Photon. 10, 340-345 (2016).  
20. Wang, H. et al. Towards optimal single-photon sources from polarized microcavities. Nat. Photon. 13, 770-775 (2019).  
21. Laucht, A. et al. A waveguide-coupled on-chip single-photon source. Phys. Rev. X 2, 011014 (2012).  
22. Arcari, M. et al. Near-unity coupling efficiency of a quantum emitter to a photonic crystal waveguide. Phys. Rev. Lett. 113, 093603 (2014).  
23. Caspani, L. et al. Integrated sources of photon quantum states based on nonlinear optics. Light.: Sci. Appl. 6, e17100 (2017).  
24. Carolan, J. et al. Scalable feedback control of single photon sources for photonic quantum technologies. Optica 6, 335-340 (2019).  
25. Llewellyn, D. et al. Chip-to-chip quantum teleportation and multi-photon entanglement in silicon. Nat. Phys. 16, 148-153 (2020).  
26. Signorini, S. et al. Intermodal four-wave mixing in silicon waveguides. *Photon Res* 6, 805-814 (2018).  
27. Feng, L.-T. et al. On-chip transverse-mode entangled photon pair source. npj Quantum Inf. 5, 1-7 (2019).  
28. Fang, B., Cohen, O., Moreno, J. B. & Lorenz, V. O. State engineering of photon pairs produced through dual-pump spontaneous four-wave mixing. Opt. Express 21, 2707-2717 (2013).  
29. Zhang, Y. et al. Dual-pump approach to photon-pair generation: demonstration of enhanced characterization and engineering capabilities. Opt. Express 27, 19050-19061 (2019).  
30. Christ, A., Laiho, K., Eckstein, A., Cassemiro, K. N. & Silberhorn, C. Probing multimode squeezing with correlation functions. N. J. Phys. 13, 033027 (2011).  
31. Jizan, I. et al. Bi-photon spectral correlation measurements from a silicon nanowire in the quantum and classical regimes. Sci. Rep. 5, 12557 (2015).  
32. Meyer-Scott, E. et al. Limits on the heralding efficiencies and spectral purities of spectrally filtered single photons from photon-pair sources. Phys. Rev. A 95, 061803 (2017).  
33. Ding, Y., Peucheret, C., Ou, H. & Yvind, K. Fully etched apodized grating coupler on the soi platform with  $-0.58$  db coupling efficiency. Opt. Lett. 39, 5348-5350 (2014).  
34. Khasminskaya, S. et al. Fully integrated quantum photonic circuit with an electrically driven light source. Nat. Photon 10, 727-732 (2016).  
35. Silverstone, J. W. et al. On-chip quantum interference between silicon photon-pair sources. Nat. Photon 8, 104-108 (2014).  
36. Silverstone, J. W. et al. Qubit entanglement between ring-resonator photon-pair sources on a silicon chip. Nat. Commun. 6, 7948 (2015).  
37. Faruque, I. I., Sinclair, G. F., Bonnaueau, D., Rarity, J. G. & Thompson, M. G. On-chip quantum interference with heralded photons from two independent micro-ring resonator sources in silicon photonics. Opt. Express 26, 20379-20395 (2018).  
38. Adcock, J. C., Vigliar, C., Santagati, R., Silverstone, J. W. & Thompson, M. G. Programmable four-photon graph states on a silicon chip. Nat. Commun. 10, 1-6 (2019).  
39. Neville, A. et al. Classical boson sampling algorithms with superior performance to near-term experiments. Nat. Phys. 13, 1153-1157 (2017).  
40. Selvaraja, S. K., Bogaerts, W., Dumon, P., Van Thouhout, D. & Baets, R. Subnanometer linewidth uniformity in silicon nanophotonic waveguide

devices using cmos fabrication technology. IEEE J. Sel. Top. Quantum Electron. 16, 316-324 (2009).  
41. Lu, Z. et al. Performance prediction for silicon photonics integrated circuits with layout-dependent correlated manufacturing variability. Opt. Express 25, 9712-9733 (2017).

# Acknowledgements

We thank N. Maraviglia, J. Bulmer and F. Graffiti for useful discussions, and L. Kling for technical assistance. We acknowledge support from the Engineering and Physical Sciences Research Council (EPSRC) Hub in Quantum Computing and Simulation (EP/T001062/1), European Commission QUCHIP (H2020-FETPROACT-3-2014: quantum simulation), QUPIC, and the European Research Council (ERC). L.P. and S.S. have been supported by the University of Trento's strategic initiative  $\mathrm{Q@TN}$ , the European Union's Horizon 2020 research and innovation programme under grant agreement No. 820405. Fellowship support from EPSRC is acknowledged by A.L. (EP/N003470/1).

# Author contributions

S.P., M.B. and S.S. contributed equally. M.B. conceived the idea of the multi-modal source combined with the delayed pump. M.B. and S.S. performed simulations of the sources and designed the integrated components. S.P., M.B. and S.S. designed the experiments. S.P. and A.M. performed the experiments and analysed the data. L.P. and A.L. supervised the project. All authors contributed to the discussion of the results and to the writing of the manuscript.

# Competing interests

S.P., M.B., S.S. and L.P declare UK patent application number 2005827.7.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41467-020-16187-8.

Correspondence and requests for materials should be addressed to A.L.

Peer review information Nature Communications thanks Alessandro Farsi and the other anonymous reviewer(s) for their contribution to the peer review of this work. Peer reviewer reports are available.

Reprints and permission information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/94914d9c3d94188197d9f0fe98b204149568488254522837c6f4677b86addf38.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing,

adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2020