# Nonlinear quantum optics at a topological interface enabled by defect engineering

Check for updates

L. Hallacy $^{1,4}$ , N. J. Martin $^{1,4}$ , M. Jalali Mehrabad $^{2}$ , D. Hallett $^{1}$ , X. Chen $^{1}$ , R. Dost $^{1}$ , A. Foster $^{1}$ , L. Brunswick $^{1}$ , A. Fenzl $^{1}$ , E. Clarke $^{3}$ , P. K. Patil $^{3}$ , A. M. Fox $^{1}$ , M. S. Skolnick $^{1}$  & L. R. Wilson $^{1}$

The integration of topology into photonics has generated a new design framework for constructing robust and unidirectional waveguides, which are not feasible with traditional photonic devices. Here, we overcome current barriers to the successful integration of quantum emitters such as quantum dots (QDs) into valley-Hall (VH) topological waveguides, utilising photonic defects at the topological interface to stabilise the local charge environment and inverse design for efficient topological-conventional mode conversion. By incorporating QDs within defects of VH-photonic crystals, we demonstrate the first instances of single-photon resonant fluorescence and resonant transmission spectroscopy of a quantum emitter at a topological waveguide interface. Our results bring together topological photonics with optical nonlinear effects at the single-photon level, offering a new avenue to investigate the interaction between topology and quantum nonlinear systems.

The last two decades have seen the emergence of topological photonics as a new and powerful approach to the design of photonic devices with novel functionalities $^{1-7}$ . Many of these developments have been motivated by the fact that topological systems exhibit chiral or helical edge states that are confined to the boundary of the system and are remarkably robust against imperfections common to integrated photonic devices $^{8-10}$ . Examples of implementation of topological photonics in the linear regime include robust optical delay lines $^{11}$ , slow-light engineering $^{12}$ , waveguides, tapers, and reconfigurable routers $^{13-18}$ . While early efforts in topological photonics focused on linear devices, more recent demonstrations have included nonlinear effects, extending the scope of possible applications to include lasers $^{19-22}$ , parametric amplifiers $^{23,24}$ , quantum light sources $^{25-28}$  and frequency combs $^{29}$ . A more recent and intriguing direction has been exploring strong light-matter coupling to induce strong interaction between photons. To achieve this, microcavity exciton-polaritons $^{30,31}$ , transition metal dichalcogenides $^{32}$  and quantum dots (QDs) $^{33}$  were integrated into topological photonic devices. In particular, due to their scalability and high optical quality for on-chip single photon generation, there has been great interest in implementing QDs in topological photonic devices. For example, QDs have been utilised in various applications, such as internal light sources in topological photonic ring resonators $^{34}$ , topological 1D cavity lasers $^{35}$ , and topological slow-light waveguides $^{36,37}$ . They have also been used as integrated single-photon emitters for cavity-QED in topological nanocavities $^{38,39}$ , as well as for chiral quantum optics in fast and slow-light topological waveguides $^{33,40,41}$ , topological all-pass $^{40,42}$  and add-drop filters $^{43}$ .

Efficient integration of several QDs in topological photonics could lead to the realisation of collective effects such as chiral super and sub-radiance effects and spin chains $^{44}$ . However, development in this direction has remained elusive due to several remaining challenges. By optimising solely around optical properties, we can inadvertently introduce challenges related to the environment of quantum emitters. Integrating QDs within stable environments is essential for high-performance single-photon emission and operation as few-photon nonlinearities. Achieving this in VH waveguides requires careful optimisation of the waveguide design, taking into account the stability of the environment of embedded quantum emitters. On one hand, position-dependence of the emitter's coupling efficiency and chiral coupling in QD-coupled topological waveguides is a significant limitation in these quantum optics interfaces, as recently explored both theoretically and experimentally $^{45,46}$ . Moreover, regions of high directionality and high coupling efficiency are mostly present in the holes of the crystal rather than the material $^{40,46,47}$ , which is detrimental for coupling to solid-state quantum emitters.

Challenges associated with performing successful resonance fluorescence (RF) studies in conventional photonic devices have largely been addressed by embedding QDs in diode structures to minimise charge noise and reduce spectral wandering $^{48-52}$ . However, in photonic structures such as valley-Hall (VH) waveguides, extensive etching of the waveguide membrane exposes remaining sections to increased charge noise from surface charge traps, leading to higher spectral wandering and making stable charge state observation via RF particularly challenging $^{53}$ . These charge traps degrade

$^{1}$ Department of Physics and Astronomy, University of Sheffield, Sheffield, S3 7RH, UK.  $^{2}$ Joint Quantum Institute, University of Maryland, College Park, MD, 20742, USA.  $^{3}$ EPSRC National Epitaxy Facility, University of Sheffield, Sheffield, S1 4DE, UK.  $^{4}$ These authors contributed equally: L. Hallacy, N. J. Martin.

e-mail: n.j.martin@sheffield.ac.uk

![](images/55e0885564fa0f052709c6d828c883c93a1b1a688eff0e232765a24cf766a3de.jpg)  
Fig. 1 | Device design and transmission properties. a Schematic diagram of the (i) single aperture removed (Mono) defect waveguide and (ii) triple aperture removed (Tri) waveguide-coupled defect cavity. b An illustration of the perturbed unit cells that form the VH-waveguide and their bandstrutures, showing the formation of a band gap at the  
K point. c The  $C_3$  unit cell. d SEM image of the waveguide structure showing the location of the defect at point (1), scale bar represents  $2\mu \mathrm{m}$ . e The frequency dependence of the transmission through the mono and tri defects presented on the left Y-axis (red) with the Purcell enhancement at the centre of the defects presented on the right Y-axis (Blue).

QD performance if they are less than  $40~\mathrm{nm}$  away from these surfaces[53,46], resulting in higher spectral wandering. No point within a typical VH-waveguide is more than  $50\mathrm{-nm}$  away from an etched surface. Given these considerations, it is unsurprising that topological structures with embedded emitters encounter difficulties in achieving RF and emitter-based strong nonlinear interactions, significantly hindering their potential for scalable quantum systems with high coherence and indistinguishability. Another remaining challenge is the efficiency of mode conversion at the topological-conventional waveguide interfaces[40,43,54]. Further optimisation of such mode conversion is essential for the efficient integration of these optical components for scalable photonic circuitry.

In this work, we report a novel platform based on the integration of QDs in lattice defects that overcomes many of the aforementioned challenges. To address these challenges, we remove specific etched holes within the un-modified topological waveguide (as illustrated in Fig. 1a(i-ii)) to create defect regions where QDs can be located without being in close proximity to etched surfaces. We focus on two types of defects, which we refer to as Mono and Tri-defects, involving the removal of one and three holes, respectively. The Mono-defect offers a minimal perturbation to the waveguide mode without leading to electric field localisation in the topologically non-trivial portion of the waveguide, thereby improving the QD environment while maintaining high transmission. The Tri-defect, on the other hand, is the smallest defect to produce a localisation within the topologically non-trivial region (a defect involving the removal of two holes produces a cavity mode only in the topologically trivial region), enhancing the Purcell factor for the QD. Figure 1e shows that the Mono-defect has little impact on the transmission through the topologically non-trivial spectral region of the waveguide's operation. The Tri-defect offers a significantly greater simulated maximum Purcell enhancement in comparison to the Mono-defect, with the trade-off of a moderate decrease in transmission. While larger defects could be utilised, each with its own unique electric field localisation, coupling strengths and associated transmission loss, we have confined our study to these small defects, as larger defects lead to an increased mode volume, thus reducing the Purcell enhancement. Further optimisation of these defects, by introducing a tapering of the waveguide, or through manipulation of the size or position of the apertures around the defect, could lead to greater Purcell enhancements and reduced transmission loss, as has been demonstrated in conventional photonic crystal waveguide systems[55-57]. We believe that this method significantly reduces the adverse effects of charge instability caused by surface states and does not compromise the coupling efficiency of QDs into non-trivial topological modes. Such an approach promises to leverage the unique advantages of topological waveguides while circumventing the limitations imposed by conventional photonic crystal structures. We demonstrate that these defects can be utilised to achieve highly directional emission, and we harness the

improvements to the QDs' local environment to achieve the first demonstration of resonance spectroscopy and optical nonlinear response of quantum emitters at a topological edge state. Additionally, we use an inverse design approach to improve the mode conversion efficiency between topological and non-topological regions (see supplementary section S1), enhancing the scalability of the system.

# Results

# Construction of a Valley-Hall waveguide with embedded quantum dots

The VH topological photonic crystal (PhC) used in this work is created from a honeycomb lattice of triangular holes in a semiconductor membrane. For these semiconductor-based QD systems, we grow a GaAs-based p-i-n diode using molecular beam epitaxy with InAs Stranski-Krastanov dots positioned in the middle of the intrinsic layer. This wafer design allows for fast tuning of embedded QDs via the quantum-confined Stark effect and reduces charge noise by modulating the electric field. The rhombic unit cell of the PhC contains a pair of triangular holes. Initially, with holes of equivalent diameters, the band structure of the PhC for TE polarisation shows a Dirac cone at the  $K$  point (and similarly at the  $K^{\prime}$  point), as shown in Fig. 1b. By shrinking one triangle and expanding the other, a modified PhC supports a bandgap for TE polarised light. A notable aspect of the band structure is the opposite sign of the Berry curvature at the  $K$  and  $K^{\prime}$  points, as demonstrated in ref. 58. By interfacing two of these perturbed photonic crystal structures together, one the inverse of the other, a topological waveguide interface can be created. The difference in Berry curvature at the connection of the two PhCs results in the confinement of counter-propagating edge states with opposing helicity at the interface[58]. The design used in this work utilises a small triangle side length of  $L_{\mathrm{S}} = 0.7a / \sqrt{3}$  and a large triangle side length of  $L_{\mathrm{L}} = 1.3a / \sqrt{3}$ , which establishes a single-mode, topologically non-trivial, slow-light region within the waveguide[59]. In this work, we use a lattice constant of  $a = 265~\mathrm{nm}$ .

# Observation of high-directional contrast

A documented challenge for topological waveguides $^{46,47}$  has been reliably creating highly directional emissions. Here, we demonstrate that the introduction of the Mono and Tri-defects are a way to create highly directional QD emission. Figure 2b(i–ii) show the Stokes  $S_{3}$  parameter, which for the un-modified waveguide and mono-defect characterises the degree of circular polarisation of the localised electric field. The strong light confinement in these structures locks the local polarisation of the light to its propagation direction. This interplay between polarisation and propagation direction leverages spin–orbit coupling, where the spin state associated with a particular transition of a quantum emitter determines its polarisation and, thus, its emission direction $^{44}$ . For the un-modified waveguide, regions of the

![](images/15ebcb86b92faf47456ab5f6395c25d563e3b2902dc0e672ce5e404f187720c6.jpg)  
(a) (i) Waveguide

![](images/d7d7963acae517709c4bf5dc6424052acb09add30b769ece52a079b814ddfe68.jpg)  
(b) (ii)  
(b) (i)

![](images/9fd5dda92829ea4b603fe77f15311c5625c01bd0bf17aa7c0c52d09e706d6d24.jpg)  
(c)  
(d) Mono-Defect

![](images/fed73fbfc4b66fbb0184912a5931a8e83c2600b730701852a66e67207399c643.jpg)  
(a) (ii) Mono-Defect

![](images/282a1d7bc5466eb86d6da405e2cd58e6efd0744090235bbd8161ee1c57a02131.jpg)

![](images/c0552aa00c39cbd6c2be290dd222092a99e05daa3301b84c67eafbcf6c07fa95.jpg)  
Left Col  
Right Col  
(e) Tri-Defect

![](images/235e58419db44cca76f97603cde3ab8d42c994725cf45a32cd4697013a2ad3f8.jpg)  
(a) (iii) Tri-Defect

![](images/706e083026caa398b10bc34f8a5808532cf50bba8ac858aeaf3a7d8e5288efc0.jpg)  
(b) (iii)  
directionality of an emitter placed within the tri-defect cavity at the red cross indicated in (aiii). c SEM of the device showing the left and right collection ports (Col). d An example of high chiral contrast  $(85\%)$  PL emission, from a QD located within the Mono-defect. e An example of high chiral contrast  $(92\%)$  PL emission, from a QD located within the Tri-defect.

![](images/822f48454149d3d3b5bd018101d4c6867e037cbd62a1ecb0570bafdad66e0156.jpg)  
Left Col  
Right Col

![](images/5ecd1f70d54b3085343ed1e0fbdf90c479388e5fcc6cfd15ad91200d692dce06.jpg)  
Fig. 2 | Directional properties and results. Within a(i–iii), regions less than  $50~\mathrm{nm}$  greater than  $50~\mathrm{nm}$  and greater than  $100~\mathrm{nm}$  away from an etched surface are highlighted. b(i–ii) Shows the Stokes  $S_{3}$  parameter for the localised electric field at the centre of the slab waveguide slab for the (i) un-modified waveguide and (ii) the Mono-defect waveguide. b(iii) Shows the equivalent frequency dependence of the

waveguide that can achieve high directionality are located close to etched surfaces ( $< 50\mathrm{nm}$ ) from the waveguides apertures. Removing one of these apertures to form the mono-defect greatly increases the distance from the peak of the  $S_{3}$  value to any etched surfaces, and creates a better spatial overlap of the electric field intensity and the  $S_{3}$  map (see supplementary section S3). This distance is even greater for the Tri-defect. In the case of the Tri-defect, the mechanism for the directionality arises from an interference effect between the two cavity modes it supports[55] with the wavelength dependence of the directionality shown in Fig. 2b(iii). More information on this mechanism for directional coupling within the Tri-defect cavity can be found in supplementary section S2.

In order to demonstrate directional emission from QDs in these defect structures,  $\mu \mathrm{PL}$  measurements of individual QDs were carried out, measuring from the left and right ports of the waveguide, as shown in the SEM of Fig. 2c. The resulting photoluminescence (PL) spectra from a single representative QD under a magnetic field in the Faraday geometry of 2T are illustrated in Fig. 2d, e for the mono-defect and tri-defect, respectively. These spectra reveal two Zeeman-split states, exhibiting an asymmetric intensity for the  $\sigma^{+}$  and  $\sigma^{-}$  polarised transitions. Notably, the intensity asymmetry reverses when collecting PL from the opposite optical collection direction, indicating directional emission. The measured directional contrast for these two examples, reached a maximum of  $85\%$  for the Mono-defect and  $92\%$  for the Tri-defect, notably higher than the values achieved in our previous work with valley-Hall waveguides[40,43]. It is common to observe asymmetry in the

contrast measured in either direction in experiments of this nature $^{43,60}$ , an effect that is visible in these results, and not yet fully understood.

# Quasi-resonant and resonant excitation

To measure RF from a QD within the Tri-defect, we use the excitation scheme and device design illustrated in Fig. 3a. This consists of a VH-waveguide with a Tri-defect placed in the centre of the waveguide. The PhC is coupled via the inversely designed mode converter to two deep-etched Bragg grating couplers for far-field collection.

Figure 3b(i-iii) compares the energy level diagrams of non-resonant, quasi-resonant and resonant excitation schemes of a QD. In above-band excitation b(i), photons with energy greater than the bandgap of the QD material are used to create electron-hole pairs in the bulk material, which then relax through phonon emission and are captured by the quantum dot. The multiple steps and environmental interactions involved in this process lead to dephasing and broader emission linewidths compared to more targeted excitation methods. In quasi-resonant schemes b(ii), since the excitation energy is closer to the actual QD states, there are fewer relaxation steps involving phonons or other dephasing interactions, leading to a more coherent emission in comparison to the above band scheme[61,62]. Finally, moving to the resonant scheme b(iii), the excitation photons have precisely the energy needed to excite the QD directly from the ground state to an excited state. By directly pumping a single QD transition, we minimise the instability associated with that transition, leading to enhanced photon

![](images/55acc47ce2585d700423996ec5d5eae36fb898ee060bb1eccfa457e26e4d5b86.jpg)  
(b) (i)  
(b) (ii)  
Resonant  
(b) (iii)

![](images/52a48c2f5b57080480680beb1d79219737f93f28afc29362c5b6090fd4802fcc.jpg)  
Non-resonant

![](images/e0d651f2e7f364ee7cf99d1defc4f92ca1995809ed4b3458912f968df0b5cf8d.jpg)  
Quasi-resonant (p-shell)

![](images/c3db72487f683b1d46f9ec38054eb588138986113912a0f5850a9762b2fbcef0.jpg)

![](images/c6329aec9d142c564ccdc43ae4aea30fdc576c5a804ca632ec8430b03c1840ad.jpg)  
Fig. 3 | Quasi-resonant and resonant excitation. a Render of topological PhC with Tri-defect defect showing excitation scheme for resonant measurements. b(i) Energy level diagram illustrating non-resonant driving from the ground state  $|g\rangle$  (at energy  $\Omega$ ) to above band state  $|R\rangle$  and recombination to intermediate charge state  $|X\rangle$  with non-resonant radiative emission energy  $\gamma_{NR}$  and back to ground state with resonant emission energy  $\gamma$ . (ii) Energy level diagram for the quasi-resonant scheme with P shell state  $|X^{*}\rangle$  (determined from the difference in pumping and emission wavelength  $\Delta \lambda = 14.83 \mathrm{~nm}$ ) and intermediate emission  $\gamma_{p}$  to charge state  $|X\rangle$ . (iii) Energy level diagram for resonant scheme directly exciting charged excitonic state. c Comparison  
of linewidth in non-resonant, quasi-resonant, and resonant excitation showing a reduction in spectral wandering (Gaussian fit of linewidth given in top right corner). Non-resonant and quasi-resonant spectra are obtained via CCD spectrometer scans, while resonant spectra is obtained from bias-modulated photon-intensity with background subtraction (further details in supplementary section S6) while scanning laser with wavelengths shown on the x-axis in plot. d RF from a QD in a topological defect waveguide. RF signal obtained by scanning bias and measuring APD flux and normalised. Minimum linewidth observed was  $8.9 \pm 0.4 \mu \mathrm{eV}$  at  $954.16 \mathrm{~nm}$ . e Autocorrelation measurement of single dot emission under quasi-resonant excitation.

![](images/1dd2843948bd11b56661a79699a8ca1450ceed30a5be26e1366a1d3118ba5d95.jpg)  
(e)

![](images/9a92c6fa64ed0ff1b5344db6cc4aabe02545218f470a35b42e7c325a3b9bdda5.jpg)

indistinguishably and coherence, and minimum time jitter $^{63,64}$ . This makes it desirable for deterministic single-photon generation, which is essential for large-scale quantum networks $^{65}$ . For the resonant measurements, the Tri-defect was excited from above with a resonant laser, scanning from 954.1 to  $954.25 \mathrm{~nm}$ . The emission of the QD was modulated using an applied bias, to allow for the subtraction of the background laser scatter from the RF signal. To ensure a high signal-to-noise ratio, we introduced a cross-polarisation scheme that introduced a phase of  $\pi / 2$  between the linearly polarised pump laser and QD emission. A more detailed description of this process is discussed in the supplementary material S6. Figure 3c compares the non-resonant emission from a single QD excited with a  $808 \mathrm{~nm}$  laser (red) with the equivalent quasi-resonant (P-shell, excited at  $939.33 \mathrm{~nm}$ ) and resonant scheme that delivers emission at  $954.16 \mathrm{~nm}$ . Here a significant reduction in linewidth to  $8.9 \pm 0.4 \mu \mathrm{eV}$  (resonant) from  $40.5 \pm 0.6 \mu \mathrm{eV}$  (non-resonant) is observed, indicating a significant reduction in dephasing.

In Fig. 3d the normalised RF signal at different applied biases is shown. An RF peak from the emitter is present, and tunes  $0.7\mathrm{nm}$  from 954.15 to  $954.22\mathrm{nm}$  as the bias is changed. As illustrated in Fig. 3c, d, the absence of

fine structure splitting in the emission spectrum suggests the QD is in a charged exciton state, either  $X^{-}$  (negatively charged exciton) or  $X^{+}$  (positively charged exciton). We believe the ability to observe stable charged states can be attributable to the combined charge stabilisation/state tuning from the p-i-n diode structure and the minimised charge noise by having the QD in the Tri-defect region. Non-resonant and quasi-resonant excitation in and around the defect at low powers revealed very few emission lines, with the investigated QD line isolated from any others within the vicinity; this low dot density, and position-dependent excitation, helped ensure that the RF signal observed in our wavelength scans originate specifically from the QD located in the defect. In order to gauge the single photon behaviour, we performed a Hanbury Brown and Twiss (HBT) auto-correlation measurement under a quasi-resonant excitation giving us a second-order correlation function,  $g^{(2)}(\tau)$  (as a function of coincidence time delay  $\tau$ ). From Fig. 3e at zero time delay  $(\tau = 0)$  we have observed strong anti bunching such that,  $g^{(2)}(0) = 0.14 \pm 0.05$  showing we are operating in the single photon regime from a QD inside the Tri-defect region. More information on this measurement can be found in supplementary section S7.

![](images/d190243c244d4773f4e1ac3702370fd56ea85aacf8646f5db6a59517edeb71f4.jpg)  
(a)

![](images/9ce0fe083ff993f9093deb1c6af98f94be843d8bd473ca2dc81f9e0089103625.jpg)  
(b)  
(e)

![](images/a2e9ddcf54965949d7d7a24a2956bf68a91c2f654580ab45ab013c224ccddcf0.jpg)  
(c)  
Fig. 4 | Resonant transmission and nonlinearity. a Diagram showing resonant scattering in the tri-defect transmission. The Render shows the resonant transmission scheme, where the pump laser and far-field collection are at separate out-couplers. b Resonant transmission scan measured by sweeping voltage under a resonantly driven CW laser (at  $50\mathrm{nW}$ ). c An example of transmission spectra observed at  $50\mathrm{nW}$  power

![](images/9294b1c5eda7ccda27f72cbc503e75cf29e0d0948adcd433f40b2b7d40d38822.jpg)  
(d)  
at  $\lambda_{L} = 954.16\mathrm{nm}$  with a fitted maximum dip of  $8\%$  with a fano-lineshape. d Normalised transmission on resonance with the spectral line as a function of laser power, for  $\lambda_{L} = 954.16\mathrm{nm}$ . e Second-order auto-correlation function for photons transmitted through the topological waveguide and defect region at zero detuning. We observe clear bunching at  $\tau = 0$  (peaking at 1.038) using 200 ps bin width.

![](images/5c7ffab4c2dd2863fcf65421eba8a23575df483327f1e90728c70f2745c32a16.jpg)

# Resonant transmission

By moving into a resonant transmission scheme (seen in Fig. 4a), the nonlinear response of the QD within the Tri-defect region can be investigated. A QD that is well coupled to an optical mode behaves non-linearly at the few-photon level. Single photons are reflected by the emitter, while multi-photon states are more likely to be transmitted. This occurs because the QD saturates after absorbing a single photon, making it transparent to additional photons arriving simultaneously. Consequently, the QD may act as a photon-number-dependent switch, enabling the manipulation of light at the quantum level for applications in quantum optics and information processing[52,66]. The observation of this phenomenon in this device indicates a strong interaction between the QD in the defect and photons in the topologically protected waveguide mode. Such phenomena underscore the potential of defect regions to enhance the interaction between photons mediated by topologically protected modes.

In the data presented in Fig. 4, continuous-wave pumping at resonant wavelengths and voltages are used to probe these nonlinear behaviours. At low excitation powers, on the order of  $10\mathrm{nW}$ , the strongly attenuated guided laser light predominantly occupies zero and one photon states within a single QD emission cycle. When the wavelength of the incoming photons is resonant with the QD transition, the system exhibits a characteristic dip in the transmission spectrum, indicative of photon reflection by the QD. Figure 4b shows the waveguide transmission as a function of laser wavelength and applied voltage when the laser is tuned across the  $X^{\pm}$  state of the QD. The consistent Stark tuning behaviour and matching linewidths of the RF emission and the transmission dip indicate that both measurements are associated with the same QD in the defect region. The transmission is normalised at each point to the transmission measured with the QD in an optically inactive state (at a bias of  $1\mathrm{V}$ , in this case).

Figure 4c shows a snapshot of (b) with the excitation laser fixed at  $954.16\mathrm{nm}$ , where it is possible to see the strongest transmission dip with a

minimal Fano-lineshape ( $\approx 8\%$  dip). The degree and width of the transmission dip allow us to model the cavity-waveguide coupling efficiency into the propagating modes. We can place a lower bound on this coupling from a fit to the transmission spectra for  $50~\mathrm{nW}$  (by taking an upper bound on the resonant decay rate as the measured quasi-resonant decay rate shown in supplementary section S5), giving a coupling efficiency of  $61 \pm 4\%$  (details of calculation in supplementary section S9). In Fig. 4d, at an excitation wavelength of  $954.16~\mathrm{nm}$ , as we increase the input laser power we observe a transition towards higher photon occupancy within the laser field, which diminishes the transmission minimum via dot saturation (from  $\approx 7\%$  at  $50~\mathrm{nW}$  to  $\approx 0.5\%$  at  $10~\mu \mathrm{W}$ ). The relationship between the transmission and the power is given by:

$$
T = 1 - A \left(1 + \frac {P}{P _ {c}}\right) ^ {- 1} \tag {1}
$$

Where  $P_{c}$  is the critical power at which one photon within the time period of the QD's lifetime, couples through the QD, and A is the minimum transmission dip. A least squares fit (represented by the dashed line) to the experimental data presented in Fig. 4d, gives  $A = 0.071$  and  $P_{c} = 388 \mathrm{nW}$ . This power-dependent transmission behaviour shows the nonlinear nature of the interaction.

By characterising the photon statistics of this nonlinear response, we can gauge the system's ability to sustain the highly coherent interactions of the resonant scattering (operating in the coherent scattering regime using a pump power of  $50\mathrm{nW}$ ). In an ideal case, the QD will reflect single-photon components and only photon-photon bound pairs (multi-photon states) will transmit, leading to a bunching effect at  $\tau = 0$  in a  $g^{(2)}(\tau)$  measurement. In Fig. 4e, we can see a distinct bunching peak of  $g^{(2)}(0) = 1.04$  indicating the coherent scattering of single-photon components as predicted. This behaviour would be difficult to observe if not for a sufficiently high coupling

efficiency from the cavity into the topological waveguide mode, and efficient collection of the light-by mode adaptors. This shows promise that these devices can become integrated into larger scalable systems.

# Discussion

The successful demonstration of RF of QDs embedded within topological photonic crystal waveguides marks a notable advancement towards realising on-chip integrated quantum optical devices. The integration of QDs within defects provides enhanced stability and efficiency for single-photon sources, crucial for quantum computing, communication, and sensing technologies. The use of an inverse designed connection between the topological waveguide and conventional nanobeam structures significantly improves the coupling efficiency, facilitating better integration into larger photonic circuits. Additionally, the enhancement in chiral coupling within the defect-engineered regions enables precise control over the emission directionality of single photons, which is a critical factor for advanced quantum communication protocols. The exploration of nonlinear optical effects at the single-photon level within such topologically protected environments addresses a previously ongoing challenge in the field. The ability to manipulate single photons within these systems, as evidenced by the observed resonant/nonlinear behaviour under different excitation conditions, opens up new avenues for research and application. The engineered defect regions within photonic crystal waveguides, facilitating these interactions, underscore the potential of topological photonics in enhancing light-matter interactions at the quantum level.

Looking forward, coupling multiple QDs to the edge states $^{67}$  within topological photonic systems presents an exciting direction for further research. By selecting appropriate defect sizes, for example using Tri-defects for strong emitter integration in small-scale devices and Mono-defects for minimising transmission losses in larger photonic networks, we can effectively manage free-space losses as the system scales up. The further the QDs are from the etched surfaces, the better their emission characteristics tend to be $^{53}$ , meaning that even within the defect regions, the emission efficiency and spectral stability of individual QDs can differ based on their exact distance from the etched surfaces. By exploring different defect geometries and optimisations, such as designing defects that shift the electric field intensity and chiral contrast maxima even further away from etched surfaces, we can mitigate the adverse effects of surface proximity. Additionally, surface passivation techniques $^{68}$  can reduce losses due to scattering and absorption at the surfaces, enhancing the overall performance and scalability of the system. The collective dynamics between distant emitters $^{69}$ , within such a framework could unveil new quantum phenomena and enable the development of more complex and scalable quantum photonic circuits. The interplay between the quantum emitters and the topological modes, as facilitated by the engineered defects, offers a rich platform for exploring new regimes of light-matter interaction. This could lead to the realisation of novel quantum optical devices and functionalities, such as topologically protected quantum gates or routers, which are essential for the advancement of quantum information technologies.

# Methods

# Quantum dot wafer and device fabrication

In this work, the device layers were grown on a semi-insulating (100) GaAs substrate using molecular beam epitaxy. In order of deposition, the layers are: a 30-nm p-doped GaAs layer with a doping concentration of  $2.0 \times 10^{19} \mathrm{~cm}^{-3}$ , a 25-nm p-doped GaAs layer with a doping concentration of  $2.0 \times 10^{18} \mathrm{~cm}^{-3}$ , a 55-nm undoped GaAs layer to serve as a spacer, a 0.7-nm layer of InAs quantum dots formed via the Stranski-Krastanov growth method, another 55-nm undoped GaAs layer as a spacer above the quantum dots, a 30-nm n-doped GaAs layer with a doping concentration of  $3.0 \times 10^{18} \mathrm{~cm}^{-3}$ , a 200-nm n-doped  $\mathrm{Al}_{0.60} \mathrm{Ga}_{0.40} \mathrm{As}$  layer with a doping concentration of  $3.0 \times 10^{18} \mathrm{~cm}^{-3}$ , a 950-nm undoped  $\mathrm{Al}_{0.60} \mathrm{Ga}_{0.40} \mathrm{As}$  sacrificial layer, and finally, a 300-nm n-doped GaAs layer with a doping concentration of  $3.0 \times 10^{18} \mathrm{~cm}^{-3}$ . This layer structure was designed to ensure robust electrical functionality while maintaining high optical quality in the

quantum dot region. Nanophotonic devices were fabricated using standard lithography and wet/dry etching techniques. A 120-nm-thick  $\mathrm{SiO}_x$  hardmask was deposited using plasma-enhanced chemical vapour deposition, followed by the spin-coating of an electron beam-sensitive resist (CSAR). The device patterns were defined with  $50\mathrm{kV}$  electron beam lithography (Raith Voyager), then transferred into the hardmask and epitaxial layers using reactive ion etching (RIE) and inductively coupled plasma RIE, respectively. Finally, the hardmask and AlGaAs sacrificial layer were removed by a hydrofluoric acid wet etch.

# Experimental methods

The sample was mounted in a superconducting magnet cryostat (CryoIndustries of America) operating at  $4.2\mathrm{K}$ . The laser and QD emission, collected in the far-field scattering from out-couplers exhibit a primary polarisation along a specific linear axis. Taking advantage of this, the polarisation between the excitation and collection paths was modified using a series of linear polarisers, half-waveplates, and quarter-waveplates (or adjustable waveplates) to ensure a  $90^{\circ}$  difference in polarisation angle. This configuration (see supplementary Fig. S6) allows the scattered laser light to be rejected en route to the spectrometer or avalanche photodiode (APD). Additionally, voltage modulation was employed to filter out background fluctuations caused by electroluminescence or scattering processes from the pump laser during measurements and to compensate for changes in laser power resulting from tuning or instability.

# Data availability

Data used in this study are available from the corresponding author upon request.

Received: 4 September 2024; Accepted: 19 January 2025

Published online: 06 March 2025

# References

1. Lu, L., Joannopoulos, J. D. & Soljacic, M. Topological photonics. Nat. Photonics 8, 821-829 (2014).  
2. Ozawa, T. et al. Topological photonics. Rev. Mod. Phys. 91, 015006 (2019).  
3. Price, H. et al. Roadmap on topological photonics. J. Phys. Photonics 4, 032501 (2022).  
4. Zhang, X., Zangeneh-Nejad, F., Chen, Z.-G., Lu, M.-H. & Christensen, J. A second wave of topological phenomena in photonics and acoustics. Nature 618, 687-697 (2023).  
5. Smirnova, D., Leykam, D., Chong, Y. & Kivshar, Y. Nonlinear topological photonics. Appl. Phys. Rev. 7, 021306 (2020).  
6. Jalali Mehrabad, M., Mittal, S. & Hafezi, M. Topological photonics: fundamental concepts, recent developments, and future directions. Phys. Rev. A 108, 040101 (2023).  
7. Khanikaev, A. B. & Alu, A. Topological photonics: robustness and beyond. Nat. Commun. 15, 931 (2024).  
8. Wang, Z., Chong, Y., Joannopoulos, J. D. & Soljacic, M. Observation of unidirectional backscattering-immune topological electromagnetic states. Nature 461, 772-775 (2009).  
9. Rechtsman, M. C. et al. Photonic floquet topological insulators. Nature 496, 196-200 (2013).  
10. Hafezi, M., Mittal, S., Fan, J., Migdall, A. & Taylor, J. M. Imaging topological edge states in silicon photonics. Nat. Photonics 7, 1001-1005 (2013).  
11. Mittal, S. et al. Topologically robust transport of photons in a synthetic gauge field. Phys. Rev. Lett. 113, 087403 (2014).  
12. Guglielmon, J. & Rechtsman, M. C. Broadband topological slow light through higher momentum-space winding. Phys. Rev. Lett. 122, 153904 (2019).  
13. Shalaev, M. I., Walasik, W., Tsukernik, A., Xu, Y. & Litchinitser, N. M. Robust topologically protected transport in photonic crystals at telecommunication wavelengths. Nat. Nanotechnol. 14, 31-34 (2019).

14. Flower, C. J. et al. Topological edge mode tapering. ACS Photonics 10, 3502-3507 (2023).  
15. Zhao, H. et al. Non-hermitian topological light steering. Science 365, 1163-1166 (2019).  
16. Zheng, X. et al. Dynamic control of 2d non-hermitian photonic corner states in synthetic dimensions. Preprint at arXiv:2402.14946 (2024).  
17. Jalali Mehrabad, M. & Hafezi, M. Strain-induced landau levels in photonic crystals. Nat. Photonics 18, 527-528 (2024).  
18. Sharp, D. et al. Near-visible topological edge states in a silicon nitride platform. Opt. Mater. Express 14, 1596-1602 (2024).  
19. St-Jean, P. et al. Lasing in topological edge states of a one-dimensional lattice. Nat. Photonics 11, 651-656 (2017).  
20. Bahari, B. et al. Nonreciprocal lasing in topological cavities of arbitrary geometries. Science 358, 636-640 (2017).  
21. Bandres, M. A. et al. Topological insulator laser: experiments. Science 359, eaar4005 (2018).  
22. Yang, L., Li, G., Gao, X. & Lu, L. Topological-cavity surface-emitting laser. Nat. Photonics 16, 279-283 (2022).  
23. Peano, V., Houde, M., Marquardt, F. & Clerk, A. A. Topological quantum fluctuations and traveling wave amplifiers. Phys. Rev. X 6, 041026 (2016).  
24. Sohn, B.-U. et al. A topological nonlinear parametric amplifier. Nat. Commun. 13, 7218 (2022).  
25. Mittal, S., Goldschmidt, E. A. & Hafezi, M. A topological source of quantum light. Nature 561, 502-506 (2018).  
26. Blanco-Redondo, A., Bell, B., Oren, D., Eggleton, B. J. & Segev, M. Topological protection of biphoton states. Science 362, 568-571 (2018).  
27. Mittal, S., Orre, V.V., Goldschmidt, E.A. & Hafezi, M. Tunable quantum interference using a topological source of indistinguishable photon pairs. Nat. Photonics 15, 542-548 (2021).  
28. Dai, T. et al. Topologically protected quantum entanglement emitters. Nat. Photonics 16, 248-257 (2022).  
29. Flower, C. J. et al. Observation of topological frequency combs. Science 384, 1356-1361 (2024).  
30. Klembt, S. et al. Exciton-polariton topological insulator. Nature 562, 552-556 (2018).  
31. Dikopoltsev, A. et al. Topological insulator vertical-cavity laser array. Science 373, 1514-1517 (2021).  
32. Li, M. et al. Experimental observation of topological z2 exciton-polaritons in transition metal dichalcogenide monolayers. Nat. Commun. 12, 4425 (2021).  
33. Barik, S. et al. A topological quantum optics interface. Science 359, 666-668 (2018).  
34. Jalali Mehrabad, M. et al. A semiconductor topological photonic ring resonator. Appl. Phys. Lett. 116, 061102 (2020).  
35. Ota, Y., Katsumi, R., Watanabe, K., Iwamoto, S. & Arakawa, Y. Topological photonic crystal nanocavity laser. Commun. Phys. 1, 86 (2018).  
36. Yamaguchi, T. et al. Gaas valley photonic crystal waveguide with light-emitting inas quantum dots. Appl. Phys. Express 12, 062005 (2019).  
37. Yoshimi, H., Yamaguchi, T., Ota, Y., Arakawa, Y. & Iwamoto, S. Slow light waveguides in topological valley photonic crystals. Opt. Lett. 45, 2648-2651 (2020).  
38. Rao, M. et al. Single photon emitter deterministically coupled to a topological corner state. Light Sci. Appl. 13, 19 (2024).  
39. Xie, X. et al. Cavity quantum electrodynamics with second-order topological corner state. *Laser Photonics* Rev. **14**, 1900425 (2020).  
40. Mehrabad, M. J. et al. Chiral topological photonics with an embedded quantum emitter. Optica 7, 1690-1696 (2020).  
41. Kuruma, K. et al. Topologically-protected single-photon sources with topological slow light photonic crystal waveguides. *Laser Photonics* Rev. **16**, 2200077 (2022).  
42. Barik, S., Karasahin, A., Mittal, S., Waks, E. & Hafezi, M. Chiral quantum optics using a topological resonator. Phys. Rev. B 101, 205303 (2020).

43. Mehrabad, M. J. et al. Chiral topological add-drop filter for integrated quantum photonic circuits. Optica 10, 415-421 (2023).  
44. Lodahl, P. et al. Chiral quantum optics. Nature 541, 473-480 (2017).  
45. Hauff, N. V., Le Jeannic, H., Lodahl, P., Hughes, S. & Rotenberg, N. Chiral quantum optics in broken-symmetry and topological photonic crystal waveguides. Phys. Rev. Res. 4, 023082 (2022).  
46. Martin, N. et al. Topological and conventional nanophotonic waveguides for directional integrated quantum optics. Phys. Rev. Res 6, L022065 (2024).  
47. Nussbaum, E., Rotenberg, N. & Hughes, S. Optimizing the chiral purcell factor for unidirectional single-photon emitters in topological photonic crystal waveguides using inverse design. Phys. Rev. A 106, 033514 (2022).  
48. Pedersen, F. T. et al. Near transform-limited quantum dot linewidths in a broadband photonic crystal waveguide. ACS Photonics 7, 2343-2349 (2020).  
49. Wang, H. et al. Near-transform-limited single photons from an efficient solid-state quantum emitter. Phys. Rev. Lett. 116, 213601 (2016).  
50. Zhai, L. et al. Low-noise gaas quantum dots for quantum photonics. Nat. Commun. 11, 4745 (2020).  
51. Nguyen, H.-S. et al. Optically gated resonant emission of single quantum dots. Phys. Rev. Lett. 108, 057401 (2012).  
52. Hallett, D. et al. Electrical control of nonlinear quantum optics in a nano-photonic waveguide. Optica 5, 644-650 (2018).  
53. Liu, J. et al. Single self-assembled InAs/GaAs quantum dots in photonic nanostructures: the role of nanofabrication. Phys. Rev. Appl. 9, 064019 (2018).  
54. Shalaev, M. I., Walasik, W., Tsukernik, A., Xu, Y. & Litchinitser, N. M. Robust topologically protected transport in photonic crystals at telecommunication wavelengths. Nat. Nanotechnol. 14, 31-34 (2018).  
55. Hallett, D., Foster, A. P., Whittaker, D., Skolnick, M. S. & Wilson, L. R. Engineering chiral light-matter interactions in a waveguide-coupled nanocavity. ACS Photonics 9, 706-713 (2022).  
56. Ooka, Y., Tetsumoto, T., Fushimi, A., Yoshiki, W. & Tanabe, T. Cmos compatible high-q photonic crystal nanocavity fabricated with photolithography on silicon photonic platform. Sci. Rep. 5, 11312 (2015).  
57. Faggiani, R., Yang, J., Hostein, R. & Lalanne, P. Implementing structural slow light on short length scales: the photonic speed bump. Optica 4, 393-399 (2017).  
58. He, X.-T. et al. A silicon-on-insulator slab for topological valley transport. Nat. Commun. 10, 872 (2019).  
59. Yoshimi, H. et al. Experimental demonstration of topological slow light waveguides in valley photonic crystals. Opt. Express 29, 13441-13450 (2021).  
60. Cole, D. C., Lamb, E. S., Del'Haye, P., Diddams, S. A. & Papp, S. B. Soliton crystals in kerr resonators. Nat. Photonics 11, 671-676 (2017).  
61. Phillips, C. L. et al. Purcell-enhanced single photons at telecom wavelengths from a quantum dot in a photonic crystal cavity. Sci. Rep. 14, 4450 (2024).  
62. Dusanowski, L., et al. Triggered high-purity telecom-wavelength single-photon generation from p-shell-driven ingaas/gaas quantum dot. Opt. Express 25, 31122-31129 (2017).  
63. Unsleber, S. et al. Highly indistinguishable on-demand resonance fluorescence photons from a deterministic quantum dot micropillar device with  $74\%$  extraction efficiency. Opt. Express 24, 8539-8546 (2016).  
64. Liu, F. et al. High purcell factor generation of indistinguishable on-chip single photons. Nat. Nanotechnol. 13, 835-840 (2018).  
65. Lodahl, P. Quantum-dot based photonic quantum networks. Quantum Sci. Technol. 3, 013001 (2017).  
66. Javadi, A. et al. Single-photon non-linear optics with a quantum dot in a waveguide. Nat. Commun. 6, 8655 (2015).  
67. Grim, J. Q. et al. Scalable in operando strain tuning in nanophotonic waveguides enabling three-quantum-dot superradiance. Nat. Mater. 18, 963-969 (2019).

68. Theeuwes, R. J., Kessels, W. M. M. & Macco, B. Surface passivation approaches for silicon, germanium, and iii-v semiconductors. J. Vac. Sci. Technol. A 42, 060801 (2024).  
69. Tiranov, A. et al. Collective super- and subradiant dynamics between distant optical quantum emitters. Science 379, 389-393 (2023).

# Acknowledgements

The authors would like to acknowledge helpful discussions with Mohammad Hafezi, Peter Millington-Hotze and Catherine Phillips. This work was supported by EPSRC Grant No. EP/N031776/1 and EP/V026496/1 and the Quantum Communications Hub EP/T001011/1.

# Author contributions

N.J.M. and M.J.M. designed the photonic structures, which R.D. fabricated. E.C. and P.K.P. grew the sample. N.J.M., X.C. and L.H. carried out the simulations of the devices. L.H., N.J.M., D.H., L.B. and A.F. carried out the measurements. L.R.W., A.M.F. and M.S.S. provided supervision and expertise. N.J.M., L.H. and M.J.M. wrote the manuscript, with input from all authors. N.J.M. and L.H. contributed equally to this work.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains

supplementary material available at

https://doi.org/10.1038/s44310-025-00057-6.

Correspondence and requests for materials should be addressed to N. J. Martin.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2025