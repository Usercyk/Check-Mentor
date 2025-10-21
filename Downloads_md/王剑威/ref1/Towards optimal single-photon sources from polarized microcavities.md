# Towards optimal single-photon sources from polarized microcavities

Hui Wang $^{1,2,8}$ , Yu-Ming He $^{1,2,8}$ , T.-H. Chung $^{1,2}$ , Hai Hu $^{3}$ , Ying Yu $^{4}$ , Si Chen $^{1,2}$ , Xing Ding $^{1,2}$ , M.-C. Chen $^{1,2}$ , Jian Qin $^{1,2}$ , Xiaoxia Yang $^{3}$ , Run-Ze Liu $^{1,2}$ , Z.-C. Duan $^{1,2}$ , J.-P. Li $^{1,2}$ , S. Gerhardt $^{5}$ , K. Winkler $^{5}$ , J. Jurkat $^{5}$ , Lin-Jun Wang $^{1}$ , Niels Gregersen $^{6}$ , Yong-Heng Huo $^{1,2}$ , Qing Dai $^{3}$ , Siyuan Yu $^{4}$ , Sven Höfling $^{5,7}$ , Chao-Yang Lu $^{1,2*}$  and Jian-Wei Pan $^{1,2*}$

An optimal single-photon source should deterministically deliver one, and only one, photon at a time, with no trade-off between the source's efficiency and the photon indistinguishability. However, all reported solid-state sources of indistinguishable single photons had to rely on polarization filtering, which reduced the efficiency by  $50\%$ , fundamentally limiting the scaling of photonic quantum technologies. Here, we overcome this long-standing challenge by coherently driving quantum dots deterministically coupled to polarization-selective Purcell microcavities. We present two examples: narrowband, elliptical micropillars and broadband, elliptical Bragg gratings. A polarization-orthogonal excitation-collection scheme is designed to minimize the polarization filtering loss under resonant excitation. We demonstrate a polarized single-photon efficiency of  $0.60 \pm 0.02$  ( $0.56 \pm 0.02$ ), a single-photon purity of  $0.975 \pm 0.005$  ( $0.991 \pm 0.003$ ) and an indistinguishability of  $0.975 \pm 0.006$  ( $0.951 \pm 0.005$ ) for the micropillar (Bragg grating) device. Our work provides promising solutions for truly optimal single-photon sources combining near-unity indistinguishability and near-unity system efficiency simultaneously.

Single photons are appealing candidates for quantum communications $^{1,2}$ , quantum-enhanced metrology $^{3,4}$  and quantum computing $^{5,6}$ . Given such quantum information applications, the single photons need to be controllably prepared with high efficiency into a given quantum state. Specifically, the single photons should possess the same polarization, spatial mode and transform-limited spectrotemporal profile for a high-visibility Hong-Ou-Mandel-type quantum interference $^{1,7}$ .

So far, self-assembled quantum dots show the highest quantum efficiency among solid-state quantum emitters and thus have the potential to serve as an ideal single-photon source[8,9,10,11,12,13,14,15]. There has been encouraging progress in recent years in developing high-performance single-photon sources[11]. Pulsed resonant excitation on single quantum dots has been developed to eliminate dephasing and time jitter, creating single photons with near-unity indistinguishability[15]. Furthermore, by combining resonant excitation with Purcell-enhanced micropillars[16,17] or photonic crystals[18,19], the generated transform-limited[20,21] single photons have been efficiently extracted out of the bulk and funnelled into a single mode at far field.

Despite recent progress $^{16,17,18,19,20,21,22}$ , the experimentally achieved polarized single-photon efficiency (defined as the number of single-polarized photons extracted from the bulk semiconductor and collected by the first lens per pumping pulse) was found to be only  $\sim 33\%$  in ref.  $^{16}$  and  $\sim 15\%$  in ref.  $^{17}$ , still short of the minimally efficiency of  $50\%$  required for boson sampling to show a computational advantage over classical algorithms $^{23}$  and below the efficiency

threshold of  $67\%$  needed for photon-loss-tolerant encoding in cluster-state models of optical quantum computing[24]. It should be noted that a  $< 50\%$  single-photon efficiency would render nearly all linear optical quantum computing schemes[1,5] not scalable.

This indistinguishable single-photon source efficiency has remained a persistent problem for years for two main reasons. First, in previous experiments $^{16,20,22}$  that relied on the optically bright, doubly-degenerate transitions in singly-charged quantum dots, the optical selection rule dictates that the resonance fluorescence photons are randomly right or left circularly polarized. For many quantum information applications that require input single photons in a fixed polarization state, passive polarization filtering is needed to project into a single polarization, which reduces the system efficiency by at least a factor of two.

The second reason is associated with the use of the resonant excitation method, which requires suppression of the pump laser light having the same frequency as the single photons. So far, the most effective method is polarization filtering[15,25], where a linearly polarized laser excites the quantum dot, and a cross polarizer in the collection arm extinguishes the scattering laser background. However, such polarization filtering again reduces the system efficiency of the quantum-dot single photons by at least a factor of two. One possible remedy is to excite the quantum dot from the side into the waveguide mode of the micropillar and collect single photons from the top. Yet, the spatially orthogonal excitation-collection methods[26,27] were only attempted in low-Purcell and non-polarized quantum dot devices and did not realize background-free, high-performance

![](images/533bebd9754222e5d27dea77261801feff686c35d97774a03cc9ec7fee28c324.jpg)

![](images/11c99059954547265a0262406434a05162f428bb8dc5ff7b114342665ced5b38.jpg)  
Fig. 1 | Theoretical scheme of a polarized single-photon source by resonantly pumping a quantum emitter in a birefringent microcavity. a, The asymmetric cavity supports two-fold non-degenerate cavity modes, one in the horizontal (H) polarization and the other one in the vertical (V) polarization. We bring the emitter into resonance with the H mode, where single photons are preferentially prepared due to polarization-selective Purcell enhancement. The V cavity mode, suitably detuned from the emitter, provides laser excitation. A V-polarized laser pulse is weakly coupled to the H mode due to a small overlap between the two cavity modes, and thus can pump the two-level system to its excited state with higher power. b, System efficiency of preparing polarized single photons as a function of the ratio of the cavity splitting to the cavity linewidth. Examples with four different Purcell factors,  $F_{\mathrm{Pr}}$ , are plotted. The dashed line shows the increase factor of the pump laser power required for a deterministic π pulse, compared to the case of a micropillar with circular cross-section.

single-photon sources. Therefore, overcoming the outstanding challenge of  $50\%$  efficiency loss has remained the most difficult and final challenge in achieving an ultimate high-performance single-photon source, both theoretically and technologically.

# Theoretical scheme

To develop a polarized single-photon source with simultaneously near-unity system efficiency and near-unity indistinguishability, (1) we break the original polarization symmetry of the quantum dot emission and (2) we develop a new way to achieve background-free resonance fluorescence without sacrificing system efficiency. Here, we propose a feasible proposal that achieves both and report its experimental demonstrations. A general framework of our protocol is shown in Fig. 1a. The key idea is to couple a single quantum dot to a geometrically birefringent cavity in the Purcell regime. The asymmetric microcavity is designed such that it lifts the polarization degeneracy of the fundamental mode and splits it into two orthogonal linearly polarized—horizontal  $(H)$  and vertical  $(V)$ -modes, with a cavity linewidth of  $\delta \omega$  and a frequency separation of  $\Delta \omega$ . Suppose a single-electron charged quantum dot, which is a degenerate two-level system, is brought into resonance with the cavity  $H$  mode, and off-resonant with the cavity  $V$  mode with a detuning of  $\Delta \omega$ . The cavity redistributes the spontaneous emission rate of the quantum emitter into the  $H$  and  $V$  polarizations with a ratio of  $1 + 4(\Delta \omega / \delta \omega)^{2}:1$  (see Supplementary Information). For a series of realistic Purcell factors, the extraction efficiency of polarized single photons is plotted in Fig. 1b. For example, with a Purcell factor of 20 and  $\Delta \omega / \delta \omega = 3$ , the polarized single-photon extraction efficiency is  $93\%$ .

Having singled out a polarized two-level system, we also need to develop a way to resonantly drive the quantum dot transition and obtain near-background-free collection of the resonance fluorescence, which is another outstanding challenge in itself. Our method is compatible with the cross-polarization technique but has little loss of single-photon system efficiency. The excitation laser's polarization is set to be  $V$ , while in the output, an  $H$  polarizer-aligned with the dominant polarization of the Purcell-enhanced single photons—is used to extinguish pump laser scattering. Note that our protocol favours a suitable  $\Delta \omega / \delta \omega$  ratio, practically in the range of 1.5-3. As the  $V$ -polarized excitation laser off-resonantly couples to the  $V$ -cavity mode at the emitter's transition (Fig. 1a), the  $\pi$ -pulse driving power needs to be moderately stronger than with an

isotropic microcavity (the increase factor is calculated and plotted in Fig. 1b). For example, at  $\Delta \omega / \delta \omega = 2.5$ , the excitation laser power is estimated to be approximately seven times higher.

This protocol is applicable in many photonic structures $^{8,9,10,11}$ , including micropillars $^{16,17,20}$ , bullseyes $^{28,29}$ , microdisks $^{30}$ , nanowires $^{31,32}$  and photonic crystals $^{18,19}$ . Here, we demonstrate our protocol by resonant excitation of single quantum dots deterministically embedded in two types of polarized microcavity—elliptical micropillars (narrowband) and elliptical Bragg gratings (broadband)—for the generation of single-polarized single-photon sources with both high system efficiency and near-unity indistinguishability.

# Elliptical micropillar

GaAs/InAs micropillars with elliptical cross-section were first studied by Gayral and others in 1998, who observed a splitting of the degenerate fundamental modes of the cavity[33]. It was shown that the two split modes were linearly polarized, aligned in parallel with the major and minor axes of the elliptical cross-section[34,35]. Single GaAs/InAs quantum dots embedded in such elliptical micropillars showed polarization-dependent Purcell enhancement[36,37] and single photons were preferentially generated in a single polarized state[33,34,35,36,37,38,39] with up to  $44\%$  extraction efficiency[39]. However, all previous work with elliptical micropillars was performed with non-resonant excitation, which degraded the purity of the emitted photons. Moreover, neither high collection efficiency nor high indistinguishability was realized in the first generation of elliptical micropillar devices.

In this work, we use two-colour photoluminescence imaging to determine the position of single quantum dots preselected with bright emission and narrow linewidth[29]. With suitably low quantum dot density  $(\sim 4\times 10^{7}\mathrm{cm}^{-2})$ , the wide-field optical imaging method can obtain a position accuracy of  $\sim 22\mathrm{nm}$  (Fig. 2a and Supplementary Information). This allows us to deterministically etch the micropillar with the quantum dot in the centre of the cavity, which is important for optimal emitter-cavity coupling.

The micropillar devices in our experiment have elliptical cross-sections (Fig. 2a) with a major (minor) axis diameter of  $2.1\mu \mathrm{m}$ $(1.4\mu \mathrm{m})$ . The elliptical micropillar is characterized using non-resonant excitation with an  $\sim 780\mathrm{nm}$  continuous-wave laser at high power. Figure 2b shows the two non-degenerate fundamental cavity modes[33,35,36,37,38,39] at  $896.54\mathrm{nm}$  (labelled as  $\mathbf{M}_1$ ) and  $897.04\mathrm{nm}$  (labelled as  $\mathbf{M}_2$ ), respectively, with a splitting of  $183\mathrm{GHz}$ . The  $\mathbf{M}_1$

![](images/a7103ce482f235ebff3abcbfdc04f7dd0245aef788b0dd168d6703346780da53.jpg)  
a

![](images/545e71b954c9abde0235784a615fcd36496c629c2741c0f1bea63a85a7422a4b.jpg)  
b  
c

![](images/4c206d2a1971d9554c92f65440edbf613a34dc613905891aa77e88cccd9f009c.jpg)

![](images/2b755e88b7177add42f3ae69a61c87001e0ca0607c7fc2d28e2d23e5f16d1d3e.jpg)  
d  
Fig. 2 | Characterization of the elliptical micropillar and elliptical Bragg grating. a, Illustration of the InGaAs quantum-dot elliptical micropillar device used in this work, which has a major (minor) axis of  $2.1\mu \mathrm{m}$  ( $1.4\mu \mathrm{m}$ ). The quantum dot is sandwiched between 25.5 (15)  $\lambda/4$ -thick AlAs/GaAs mirror pairs forming the lower (upper) distributed Bragg reflectors. b, Two fundamental modes of the elliptical micropillar,  $M_1$  and  $M_2$ , with a splitting of  $183\mathrm{GHz}$ . The linewidths of  $M_1$  and  $M_2$  are  $74\mathrm{GHz}$  and  $62\mathrm{GHz}$ , respectively. The quantum dot is resonant with  $M_2$  at a temperature of  $4\mathrm{K}$ . c, Polarization-resolved measurement of the two cavity modes, which are perpendicular to one another. The degree of polarization of the  $M_1$  and  $M_2$  modes is  $99.7\%$  and  $99.6\%$ , respectively. d, Schematic structure of the elliptical Bragg grating, which consists of a central elliptical disk, surrounding elliptical grating and fully etched trenches. A thin low-refractive-index  $\mathrm{SiO}_2$  layer and a gold mirror were added at the bottom of the Bragg grating, followed by a 500-nm-thick SU-8 and  $500\mu \mathrm{m}$  silicon substrate. The red dot indicates the position of the coupled quantum dot. e, Two non-degenerate modes of broadband bullseye cavity,  $B_1$  and  $B_2$ , with a splitting of  $2.8\mathrm{THz}$ , which are 1.5 (1.3) times larger than the linewidth of  $B_1(B_2)$ . The investigated quantum dot is resonant with  $B_2$ . f, Radiative lifetime of the quantum dots coupled to the bullseye cavity (red) and in the micropillar cavity (blue), which is 69.1 (1) ps and 61.0 (1) ps, respectively, measured using a superconducting nanowire single-photon detector with a time resolution of 20 ps. Inset: data of the lifetime (-1.1 ns) of the quantum dots (QDs) in the slab from the same area.

![](images/52bc577dd232629cf6491e7fab265276ff02cb1bff0645d401b3560d8f63f86a.jpg)  
e

![](images/538455a4eb5442d23d7d563ff424cdc1dc4c98f35ce7d7ac584353e010c0ea65.jpg)  
f

and  $\mathrm{M}_2$  modes correspond to the minor and major axes, with quality factors of 4,075 and 5,016, respectively. The modest reduction of the quality factor of  $\mathrm{M}_1$  compared to  $\mathrm{M}_2$  is due to the smaller micropillar diameter. Polarization-resolved measurements (Fig. 2c) confirm that the polarization of  $\mathrm{M}_1(\mathrm{M}_2)$  is parallel to the minor (major) axis, which we label as  $V(H)$ , with a high degree of polarization of  $99.7\%$ $(99.6\%)$ , which confirms the symmetry-broken, highly-polarized nature of the microcavity.

# Elliptical Bragg grating

Circular Bragg grating bullseye microcavities, which tightly confine the light in a sub-  $\lambda$  transverse plane, were previously fabricated on quantum dots $^{28,29}$  and diamond nitrogen-vacancy centres $^{40}$  to enhance their collection efficiencies. Recently, a thin low-refractive-index  $\mathrm{SiO}_2$  layer and a gold mirror $^{31,41,42,43,44,45,46,47}$  were added at the bottom of the bullseye to redirect the downward propagating light towards the top, thus improving the collection efficiency to near unity. Here, we break the polarization symmetry of the circular Bragg grating and design it as a geometrically birefringent Purcell cavity.

The spectral resonance of the bullseye cavity is very sensitive to the radius of the central disk and the grating period. It was previously shown that a  $1\mathrm{nm}$  change in the central disk radius (grating period) causes a  $1.14\mathrm{nm}$ $(0.25\mathrm{nm})$  shift in the cavity mode<sup>46</sup>. Thus, a  $1\%$  ellipticity, which is 23 times smaller than that of our

elliptical micropillar, is sufficient to induce a suitable cavity mode splitting. This is favourable for producing a near-Gaussian far-field emission profile.

Assisted by finite-different time-domain simulations, we designed the elliptical Bragg grating (Fig. 2d) with a central elliptical disk with a major (minor) axis of  $770\mathrm{nm}$  ( $755\mathrm{nm}$ ), surrounded by an elliptical grating with a period of  $380\mathrm{nm}$  ( $372\mathrm{nm}$ ) for the major (minor) axis, with fully etched  $100\mathrm{-nm}$ -wide trenches (see Supplementary Information for the detailed fabrication process). The cavity mode of our fabricated bullseye device (Fig. 2e) splits into a doublet (labelled as  $\mathbf{B}_1$  and  $\mathbf{B}_2$  in the  $V$  and  $H$  polarizations, respectively). The splitting is  $2.8\mathrm{THz}$ , which is 1.5 (1.3) times larger than the linewidth of  $\mathbf{B}_1$  ( $\mathbf{B}_2$ ). The broadband nature of the bullseye geometry greatly facilitates the emitter-cavity spectral alignment. As shown in Supplementary Fig. 7, the design can ideally yield a high Purcell factor of  $>20$  in a wavelength range of a few nanometres.

# Polarized indistinguishable single photons

The samples are placed inside a bath cryostat with a lowest temperature of  $1.5\mathrm{K}$ . A confocal microscope is used to excite the quantum dot and collect the emitted single photons. Following the protocol shown in Fig. 1a, driven by a  $V$  -polarized laser,  $H$  -polarized single photons from the Purcell-enhanced  $\mathbf{M}_2$  cavity spectrally resonant with a charged quantum dot are created and collected into the

![](images/9a780a33d6320c1910e34e1ec4275aa3b50bf2a5baf23b49e10f7df3e5d4da2c.jpg)

![](images/cae886aeb7a0063ef9d2fd11f8bed8e1d242853fc9792f46157d461f9bf699dc.jpg)  
Fig. 3 | Deterministic generation of polarized single photons under resonant excitation. a, Polarization of the excitation laser is set to be parallel to the minor axis, and the output polarizer is aligned parallel to the major axis, that is, orthogonal to the input laser polarization, in order to extinguish the laser background. Measured pulsed resonance fluorescence single-photon counts are plotted as a function of the laser power, which shows a clear Rabi oscillation. Under a  $\pi$  pulse at  $\sim63\mathrm{nW}$ , we observe  $\sim13.7$  million single-photon counts per second by a superconducting nanowire single-photon detector. b, In a control experiment, we exchange the polarizations of the excitation laser and the collected single photons. In this case, the single photons are suppressed by the cavity. Under a  $\pi$  pulse at  $\sim5\mathrm{nW}$ , only 0.54 million single photons per second are detected.

output of the microscope with an  $\sim 10^{7}$ :1 cross-polarization extinction of the scattered laser background. We first study the emitter-cavity coupling and measure the Purcell factors in both devices. With time-resolved resonance fluorescence measurements (Fig. 2f), the radiative lifetime for the single quantum dots coupled to the elliptical micropillar and the elliptical Bragg grating are  $\sim 61.0(1)$  ps and  $\sim 69.1(1)$  ps, respectively,  $\sim 17.8$  and  $\sim 15.7$  times shorter than the average lifetime ( $\sim 1.09\mu s$ ) of more than 20 quantum dots in the slab from the same area. Such high Purcell factors serve to efficiently funnel the spontaneous emission into a single output mode and additionally to reduce the influence of dephasing on the indistinguishability[48].

Figure 3a shows the detected resonance fluorescence single photons as a function of the driving field amplitude, and a full Rabi oscillation curve is observed. With a pumping repetition rate of  $76\mathrm{MHz}$  and using a  $\pi$  pulse,  $\sim 13.7$  million photon counts per second are detected by a single-mode fibre-coupled superconducting nanowire single-photon detector with an efficiency of  $\sim 76\%$ . A comparison experiment is performed where we excite the dot with an  $H$ -polarized laser and collect  $V$ -polarized single photons (Fig. 1a). As shown in Fig. 3b, using a  $\pi$  pulse, only  $\sim 0.54$  million photons per second are detected. We estimate a degree of polarization—defined as  $(I_H - I_V) / (I_H + I_V)$ , where  $I_H(I_V)$  denotes the detected intensity of  $H$ -(V-) polarized photons—of  $92.3\%$  for the generated single photons from the polarized micropillar device. Thus, the single-photon source suffers a loss of  $3.8\%$  due to polarization, whereas the previous resonance fluorescence experiments lost at least  $50\%$  photons in polarization filtering[16,17,20,22]. Similarly, we have also observed polarized resonance fluorescence for

![](images/375f1a1e55338de26c5369194aba7daabf36a7d91afd85e5b4e773012ec52695.jpg)

![](images/c86f486f2b1511e1fbb0a93883f8da1e2ec1ab8e03a4e63f893b5465103f3499.jpg)  
Fig. 4 | Single-photon purity and indistinguishability. a, Measurement of the second-order correlation function, which gives  $g^2(0) = 0.025(5)$ . b, Characterization of photon indistinguishability in a Hong-Ou-Mandel interferometer with a time delay of 13 ns. Significant count suppression at zero delay is observed when the two photons are in parallel polarization (red) compared with the case when the two photons are in cross polarization (grey). After correction, the calculated indistinguishability is 0.975(6).

quantum dot two-level systems in the bullseye membrane structure. The finally detected polarized single-photon count rate is 12.4 million per second for a  $\pi$  pulse.

A detailed photon loss budget analysis for both devices, including quantum radiative efficiency, blinking, collection optics, optical path transmission efficiency and single-mode fibre coupling, is presented in the Supplementary Information. For the elliptical micropillar-quantum dot device, the polarized single-photon efficiency is measured to be 0.60(2), where the dominant loss mechanisms are imperfect sidewall scattering $^{49}$  ( $\sim 22.8\%$ ), mode leakage ( $\sim 5.3\%$ ) and imperfect internal quantum efficiency (including the excited-state preparation efficiency at the  $\pi$  pulse and the radiative efficiency of the quantum dot), which is estimated to be  $\sim 82\%$ . For the elliptical bullseye devices, the polarized single-photon efficiency is 0.56(2), where the loss is mainly due to quantum dot blinking ( $35\%$ ), as the dot is close to the etched surface (distance of  $62.5\mathrm{nm}$ ). The blinking can be reduced in the future by surface passivation and by applying an electric field.

The purity of the elliptical micropillar single-photon source is characterized with a Hanbury Brown and Twiss set-up. As displayed in Fig. 4a, the measured second-order correlation data shows  $g^{2}(0) = 0.025(5)$  at zero time delay. The imperfection of the measured  $g^{2}(0)$  is mainly due to laser leakage. The photon indistinguishability is measured using a Hong-Ou-Mandel interferometer with the time separation between the two consecutive excitation laser pulses—and thus the two emitted single photons—set at 13 ns. Figure 4b shows the photon correlation histograms of normalized two-photon counts for cross and parallel polarizations. The observed contrast of the counts for the two cases at zero delay can be used to extract a raw two-photon interference visibility of 0.913(5). Taking into account the imperfect single-photon purity and the unbalanced (47:53) beam splitting ratio in the optical setup, we calculate a corrected photon indistinguishability of 0.975(6). For the elliptical bullseye device, similar results are observed: after

sending the photons through a 5GHz etalon to filter out the photon sideband (which also reduces the single photon count by  $\sim 30\%$  due to the filtering and etalon transmission rate), a single photon purity of 0.991(3) and an indistinguishability of 0.951(5) for two single photons separated by 13 ns is presented (see Supplementary Information). These results show that high efficiency, purity and indistinguishability can be simultaneously combined with high degrees of polarization in a coherently driven single-photon device.

# Discussion and conclusion

In summary, we have theoretically proposed and experimentally demonstrated near-optimal single-photon sources operating in a single polarization, combined with simultaneous high purity, indistinguishability and efficiency, by resonantly driving single quantum dots coupled to polarized microcavities, thus overcoming the long-standing problem of  $50\%$  photon loss. Our design is compatible with the mature cross-polarization set-up and does not require complicated sample fabrications, and side excitation set-up and so on. This has enabled the creation of bright polarized sources of single indistinguishable photons. The generality and versatility of our protocol have been demonstrated in both narrowband and broadband cavities, which, interestingly, have their own pros and cons. The bullseye cavity is robust to fabricate, requires negligible ellipticity and features tighter confinement. The micropillar cavity requires a more precise matching of the microcavity-emitter spectral resonance than the bullseye device, but also comes with the benefit that the phonon emission can be suppressed due to its narrowband nature. It will be interesting in the future to combine these two nanostructures[50] to take advantage of both their merits, including tight confinement, minimal scattering loss and suppression of phonon-assisted emission. Further optimization of sample fabrication, electrical gating, surface passivation[51] and single-mode fibre coupling are expected to deliver near-optimal single photons[52]—the central resources for optical quantum information technologies[53,54].

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, statements of code and data availability and associated accession codes are available at https://doi.org/10.1038/s41566-019-0494-3.

# Data availability

The data that support the plots within this paper and other findings of this study are available from the corresponding authors upon reasonable request.

Received: 28 February 2019; Accepted: 20 June 2019

Published online: 5 August 2019

# References

1. Pan, J. W. et al. Multiphoton entanglement and interferometry. Rev. Mod. Phys. 84, 777-838 (2012).  
2. Yin, J. et al. Satellite-based entanglement distribution over 1,200 kilometers. Science 356, 1140-1144 (2017).  
3. Chu, X. L., Gotzinger, S. & Sandoghdar, V. A single molecule as a high-fidelity photon gun for producing intensity-squeezed light. Nat. Photon. 11, 58-62 (2017).  
4. Slussarenko, S. et al. Unconditional violation of the shot-noise limit in photonic quantum metrology. Nat. Photon. 11, 700-703 (2017).  
5. Kok, P. et al. Linear optical quantum computing with photonic qubits. Rev. Mod. Phys. 79, 135-174 (2007).  
6. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. In Proc. 43rd Annu. ACM Symp. Theory of Computing 333-342 (ACM, 2011).  
7. Hong, C. K., Ou, Z. Y. & Mandel, L. Measurement of subpicosecond time intervals between two photons by interference. Phys. Rev. Lett. 59, 2044-2046 (1987).  
8. Shields, A. J. Semiconductor quantum light sources. Nat. Photon. 1, 215-223 (2007).

9. Buckley, S., Rivoire, K. & Vuckovic, J. Engineered quantum dot single-photon sources. Rep. Prog. Phys. 75, 126503 (2012).  
10. Lodahl, P., Mahmoodian, S. & Stobbe, S. Interfacing single photons and single quantum dots with photonic nanostructures. Rev. Mod. Phys. 87, 347-400 (2015).  
11. Senellart, P., Solomon, G. & White, A. High-performance semiconductor quantum-dot single-photon sources. Nat. Nanotechnol. 12, 1026-1039 (2017).  
12. Gerard, J. M. et al. Enhanced spontaneous emission by quantum boxes in a monolithic optical microcavity. Phys. Rev. Lett. 81, 1110-1113 (1998).  
13. Michler, P. et al. A quantum dot single-photon turnstile device. Science 290, 2282-2285 (2000).  
14. Santori, C., Fattal, D., Vuckovic, J., Solomon, G. S. & Yamamoto, Y. Indistinguishable photons from a single-photon device. Nature 419, 594-597 (2002).  
15. He, Y. M. et al. On-demand semiconductor single-photon source with near-unity indistinguishability. Nat. Nanotechnol. 8, 213-217 (2013).  
16. Ding, X. et al. On-demand single photons with high extraction efficiency and near-unity indistinguishability from a resonantly driven quantum dot in a micropillar. Phys. Rev. Lett. 116, 020401 (2016).  
17. Somaschi, N. et al. Near-optimal single-photon sources in the solid state. Nat. Photon. 10, 340-345 (2016).  
18. Madsen, K. H. et al. Efficient out-coupling of high-purity single photons from a coherent quantum dot in a photonic-crystal cavity. Phys. Rev. B 90, 155303 (2014).  
19. Liu, F. et al. High Purcell factor generation of coherent on-chip single photons. Nat. Nanotechnol. 13, 835-840 (2018).  
20. Wang, H. et al. Near-transform-limited single photons from an efficient solid-state quantum emitter. Phys. Rev. Lett. 116, 213601 (2016).  
21. Kuhlmann, A. V. et al. Transform-limited single photons from a single quantum dot. Nat. Commun. 6, 8204 (2015).  
22. Wang, H. et al. High efficiency multiphoton boson sampling. Nat. Photon. 11, 361-365 (2017).  
23. Neville, A. et al. Classical boson sampling algorithms with superior performance to near-term experiments. Nat. Phys. 13, 1153-1157 (2017).  
24. Varnava, M., Browne, D. E. & Rudolph, T. How good must single photon sources and detectors be for efficient linear optical quantum computation? Phys. Rev. Lett. 100, 060502 (2008).  
25. Vamivakas, A. N., Zhao, Y., Lu, C. Y. & Atature, M. Spin-resolved quantum-dot resonance fluorescence. Nat. Phys. 5, 198-202 (2009).  
26. Muller, A. et al. Resonance fluorescence from a coherently driven semiconductor quantum dot in a cavity. Phys. Rev. Lett. 99, 187402 (2007).  
27. Ates, S. et al. Post-selected indistinguishable photons from the resonance fluorescence of a single quantum dot in a microcavity. Phys. Rev. Lett. 103, 167402 (2009).  
28. Davanço, M., Rakher, M. T., Schuh, D., Badolato, A. & Srinivasan, K. A circular dielectric grating for vertical extraction of single quantum dot emission. Appl. Phys. Lett. 99, 041102 (2011).  
29. Sapienza, L., Davanço, M., Badolato, A. & Srinivasan, K. Nanoscale optical positioning of single quantum dots for bright and pure single-photon emission. Nat. Commun. 6, 7833 (2015).  
30. Srinivasan, K. & Painter, O. Linear and nonlinear optical spectroscopy of a strongly coupled microdisk-quantum dot system. Nature 450, 862-865 (2007).  
31. Claudon, J. et al. A highly efficient single-photon source based on a quantum dot in a photonic nanowire. Nat. Photon. 4, 174-177 (2010).  
32. Munsch, M. et al. Linearly polarized, single-mode spontaneous emission in a photonic nanowire. Phys. Rev. Lett. 108, 077405 (2012).  
33. Gayral, B., Gérard, J. M., Legrand, B., Costard, E. & Thierry-Mieg, V. Optical study of GaAs/AlAs pillar microcavities with elliptical cross section. Appl. Phys. Lett. 72, 1421-1423 (1998).  
34. Moreau, E. et al. Single-mode solid-state single photon source based on isolated quantum dots in pillar microcavities. Appl. Phys. Lett. 79, 2865-2867 (2001).  
35. Unitt, D. C., Bennett, A. J., Atkinson, P., Ritchie, D. A. & Shields, A. J. Polarization control of quantum dot single-photon sources via a dipole-dependent Purcell effect. Phys. Rev. B 72, 033318 (2005).  
36. Lee, Y. & Lin, S. Polarized emission of quantum dots in microcavity and anisotropic Purcell factors. Opt. Express 22, 1512-1523 (2014).  
37. Daraei, A. et al. Control of polarized single quantum dot emission in high-quality-factor microcavity pillars. Appl. Phys. Lett. 88, 051113 (2006).  
38. Strauf, S. et al. High-frequency single-photon source with polarization control. Nat. Photon. 1, 704-708 (2007).  
39. Moreau, E. et al. A single-mode solid-state source of single photons based on isolated quantum dots in a micropillar. Physica E 13, 418-422 (2002).  
40. Li, L. Z. et al. Efficient photon collection from a nitrogen vacancy center in a circular bullseye grating. Nano Lett. 15, 1493-1497 (2015).  
41. Chen, X.-W., Gotzinger, S. & Sandoghdar, V.  $99\%$  efficiency in collecting photons from a single emitter. Opt. Lett. 36, 3545-3547 (2011).

42. Reimer, M. E. et al. Bright single-photon sources in bottom-up tailored nanowires. Nat. Commun. 3, 737 (2012).  
43. Fischbach, S. et al. Efficient single-photon source based on a deterministically fabricated single quantum dot-microstructure with backside gold mirror. Appl. Phys. Lett. 111, 011106 (2017).  
44. Chen, Y., Zopf, M., Keil, R., Ding, F. & Schmidt, O. G. Highly-efficient extraction of entangled photons from quantum dots using a broadband optical antenna. Nat. Commun. 9, 2994 (2018).  
45. Abudayyeh, H. A. & Rapaport, R. Quantum emitters coupled to circular nanoantennas for high-brightness quantum light sources. Quantum Sci. Technol. 2, 034004 (2017).  
46. Wang, H. et al. On-demand semiconductor source of entangled photons which simultaneously has high fidelity, efficiency and indistinguishability. Phys. Rev. Lett. 122, 113602 (2019).  
47. Liu, J. et al. A solid-state source of strongly entangled photon pairs with high brightness and indistinguishability. Nat. Nanotechnol. 14, 586-593 (2019).  
48. Kaer, P., Gregersen, N. & Mørk, J. The role of phonon scattering in the indistinguishability of photons emitted from semiconductor cavity QED systems. New J. Phys. 15, 035027 (2013).  
49. Rivera, T. et al. Optical losses in plasma-etched AlGaAs microresonators using reflection spectroscopy. Appl. Phys. Lett. 74, 911-913 (1999).  
50. Winkler, K. et al. High quality factor GaAs microcavity with buried bullseye defects. Phys. Rev. Mater. 2, 052201 (2018).  
51. Liu, J. et al. Single self-assembled InAs/GaAs quantum dots in photonic nanostructures: the role of nanofabrication. Phys. Rev. Appl. 9, 064019 (2018).  
52. Iles-Smith, J., McCutcheon, D. P. S., Nazir, A. & Mork, J. Phonon scattering inhibits simultaneous near-unity efficiency and indistinguishability in semiconductor single-photon sources. Nat. Photon. 11, 521-526 (2017).  
53. O'Brien, J. L., Furusawa, A. & Vuckovic, J. Photonic quantum technologies. Nat. Photon. 3, 687-695 (2009).  
54. Flamini, F., Spagnolo, N. & Sciarrino, F. Photonic quantum information processing: a review. Rep. Prog. Phys. 82, 016001 (2018).

# Acknowledgements

This work is supported by the National Natural Science Foundation of China (grant no. 11525419, 91836303, 11674308), the Chinese Academy of Science, the Anhui Initiative in Quantum Information Technologies, the Science and Technology Commission of Shanghai Municipality, the National Fundamental Research Program (grant no. 2018YFA0306104) and the State of Bavaria.

# Author contributions

C.-Y.L. and J.-W.P. conceived the research, and M.-C.C., C.-Y.L. and J.-W.P. designed the protocol. S.G., K.W., J.J. and S.H. grew the quantum dot samples. X.D. performed the optical imaging for positioning the quantum dots. H.W., Y.-M.H. and C.-Y.L. designed the parameters of the microcavities. Y.Y., S.C., L.-J.W. and S.Y. etched the micropillars. T.H.C., H.H., X.Y., Y.-H.H. and Q.D. etched the bullseyes. H.W., Y.-M.H., J.Q., R.-Z.L., Z.-C.D., J.-P.L. and C.-Y.L. performed the resonant optical excitation and quantum optics measurements. H.W. and N.G. performed theoretical simulations and numerical analyses. All authors discussed the results and prepared the manuscript. C.-Y.L. and J.-W.P. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41566-019-0494-3.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to C.-Y.L. or J.-W.P.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2019