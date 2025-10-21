# Observation of non-Hermitian topology from optical loss modulation

Received: 29 June 2024

Accepted: 31 May 2025

Published online: 23 July 2025

![](images/4f7e66763caa4968204d58408bd09dc762d9c2e89fa950b20ce129b0150a3e04.jpg)

Check for updates

Amin Hashemi $^{1}$ , Elizabeth Louis Pereira $^{2}$ , Hongwei Li $^{3}$ , Jose L. Lado $^{2}$  & Andrea Blanco-Redondo $^{1}$

Understanding the interplay of non-Hermiticity and topology is crucial given the intrinsic openness of most natural and engineered systems, and has important ramifications in topological lasers and sensors. Recently, it has been theoretically proposed that topological features could originate solely from a system's non-Hermiticity in photonic platforms. Here we experimentally demonstrate the appearance of non-Hermitian topology exclusively from loss modulation in a photonic system that is topologically trivial in the absence of loss. We do this by implementing a non-Hermitian generalization of an Aubry-Andre-Harper model with purely imaginary potential in a programmable integrated photonics platform, which allows us to investigate different periodic and quasiperiodic configurations of the model. In both cases, we show the emergence of topological edge modes and explore their resilience to different kinds of disorder. Our work highlights loss engineering as a mechanism to generate topological properties.

The last two decades have witnessed outstanding progress in topological photonics $^{1,2}$ . This has mainly been driven by the prospect of robust electromagnetic modes, protected by global topologies of the dispersion relation of photonic materials, and their applications in classical $^{3-5}$  and quantum integrated photonic devices $^{6-9}$ . Although most of this progress has occurred in Hermitian (closed) systems, there have also been notable advances in open systems, where non-Hermiticity and topology interplay to produce unique features $^{10,11}$ . Non-Hermiticity enriches topological phases beyond the traditional Hermitian framework. By introducing a new class of symmetries $^{12}$ , it substantially expands the existing symmetry classifications, thereby enhancing the complexity and diversity of topological phases beyond what is possible in Hermitian systems. A notable feature of non-Hermitian topological systems is that they generally have complex eigenvalues, which has vast implications, including the appearance of exceptional points $^{13}$  and the emergence of eigenvalue topology $^{14}$ . Building on theoretical investigations $^{15-20}$ , a number of optical experiments have demonstrated topological effects by incorporating gain or loss: from the observation of stationary zero-order topological states $^{21}$ , topological parity–time symmetric interface states $^{22}$  and light steering $^{23}$  in non-Hermitian lattices, to recent demonstrations of gain-related asymmetric long-range couplings in

the Haldane model $^{24}$ , triple topological phase transitions in topological quasicrystals $^{25}$  and non-linearly induced non-Hermitian topological phase transitions $^{26}$ , all the way through the extensive literature on topological lasers $^{3,4,27-29}$ . All demonstrations to date have relied on the introduction of loss and/or gain in systems that were already topological in their Hermitian version $^{21,22,25,27-29}$  or used gain in an indirect way to engineer asymmetric couplings in Hermitian systems $^{24}$ . Recently, it was theoretically proposed that a photonic topological insulating phase can arise, exclusively, from a system's non-Hermiticity through gain and loss modulation in an otherwise topologically trivial system $^{30}$ . Subsequent theoretical studies have shown topological transitions and edge states in non-Hermitian Aubry–Andre–Harper (AAH) models with commensurate $^{31}$  and incommensurate $^{32}$  imaginary potentials. Although experimental demonstrations of topological phases arising solely from non-Hermiticity have occurred in electrical circuits $^{33}$ , acoustics $^{34,35}$ , elastic waves $^{36}$  and plasmonics $^{37}$ , an experimental demonstration in photonic systems remained elusive.

In this study, we experimentally demonstrate the appearance of non-Hermitian topology and the existence of edge modes from optical loss modulation exclusively. Our experiments realize a non-Hermitian generalization of the AAH model $^{32}$  in a reconfigurable integrated

<sup>1</sup>CREOL, The College of Optics and Photonics, University of Central Florida, Orlando, FL, USA. <sup>2</sup>Department of Applied Physics, Aalto University, Espoo, Finland. <sup>3</sup>Nokia Bell Labs, Cambridge, UK. e-mail: andrea.blancoredondo@ucf.edu

![](images/0cf52ec6dee560fd43f6cd6a14a79745929b0648a3ad1273a9f52ac0a0ea9540.jpg)  
a

![](images/0951eb879aea7cf90ee5b75d8c371f4bfc680818a96be0585e1a2b443f8ba77a.jpg)  
C  
Fig. 1|Commensurate configurations with and without edge states. a,b, The loss modulation of the periodic (commensurate) non-Hermitian topological models under investigation in our experiments for periodic models with (a) and

![](images/3a36e59a275b5044549ea7d66f794fc5df737a43625b51fcfb352ad3411b1715.jpg)  
b

![](images/95ef628de9d9c5a7730821fedf2db67d51e91dafbdd2c0f4c8a6021911cc47a4.jpg)  
d  
without (b) edge states. c,d, The schematic of the programmable integrated photonics platform for implementing the configurations with (c) and without (d) edge states. PS, phase-shifter; MMI, multi-mode interferometer.

photonics platform $^{38}$ . We reveal the presence of topological transitions, the emergence of distinct topological phases and the presence of topologically protected edge states, for both periodic (commensurate) and quasiperiodic (incommensurate) potentials. Due to the reconfigurability afforded by the programmable photonic platform, we systematically investigate the robustness of the system against different types of disorders. Our experimental results, in conjunction with theoretical analysis, illuminate the intricate interplay between disorder, topology and the emergence of protected modes in photonic NH periodic systems and quasicrystals. These findings may have implications in open topological systems and their applications, such as topological lasers and sensors, where gain and loss play a crucial role.

# Non-Hermitian topological model

We examine a one-dimensional non-Hermitian topological model, as theoretically introduced by Pereira et al.32, wherein sites are interconnected with uniform coupling strengths, while exhibiting varying degrees of on-site loss modulated by a sinusoidal function, leading to the following effective Hamiltonian:

$$
H = \sum_ {n = 0} ^ {N - 2} \left(t \hat {a} _ {n} ^ {\dagger} \hat {a} _ {n + 1} + \mathrm {h . c .}\right) - i \sum_ {n = 0} ^ {N - 1} \left[ v _ {1} + v _ {2} \sin (2 \pi n \alpha + \delta) \right] \hat {a} _ {n} ^ {\dagger} \hat {a} _ {n}, \tag {1}
$$

where  $\hat{a}_n^\dagger$  and  $\hat{a}_n$  are creation and annihilation operators in site  $n$ ,  $t$  is the coupling between neighbouring sites,  $\alpha$  is the inverse of the loss modulation period,  $\delta$  represents the modulation phase,  $\nu_{2}$  is the amplitude of the modulation and  $\nu_{1}$  is a uniform loss introduced to compensate for the gain induced by sinusoidal gain/loss modulation; h.c. is the Hermitian conjugate.

A rational modulation frequency  $\alpha = p / q$ , where the number of sites  $N$  is a multiple of  $q$ , ensures commensurability between the potential and the lattice periodicity, leading to a periodic scenario. Conversely, when the modulation frequency takes irrational values, the potential is incommensurate with the lattice periodicity, resulting in aperiodic scenarios akin to quasicrystals.

# Programmable integrated photonic platform

To implement the non-Hermitian topological model experimentally, we utilize a programmable integrated photonics platform composed of a hexagonal mesh of reconfigurable Mach-Zehnder interferometers (MZI), as illustrated in Fig. 1c (see Supplementary Note 1 for details). Recently, this kind of platform has proven its potential to implement Hermitian topological Hamiltonians $^{38-40}$ . The inset shows the configuration of each MZI, composed of an input and an output  $2 \times 2$  multi-mode interferometer and a controllable phase shifter in each arm.

By adjusting the phase imparted by each phase shifter we can configure the splitting ratio of each MZI, and thence the path followed by light in the mesh. Doing so, we configure the paths into an array of coupled ring resonators, using the MZIs common to two rings (cyan cells) to implement uniform coupling  $t$ . The loss in each ring is controlled by tapping the desired amount of power out of the mesh via one of the MZIs in each ring: green (magenta) cells highlight the MZIs used to tap a small (large) amount of power out of the ring, leading to a low (high) loss ring. These ports are connected to on-chip photodiodes that are used to monitor the power in each ring. Finally, we control the input excitation to each ring independently using the cells highlighted in brown. Although controlling the coupling and loss by modifying the splitting ratios of individual MZIs could in principle lead to undesired local phase shifts, the inclusion of two phase-shifters per MZI, as shown in the inset of Fig. 1c, allows us to adjust not only the splitting ratio but also the phase of the signal in both output arms of the MZI. This feature also enables compensation of thermal cross-talk in the lattice by tuning the individual resonant frequencies of each ring without affecting the phase<sup>41</sup>.

# Configurations with commensurate loss modulation

We analysed two distinct periodic (commensurate) scenarios with different topological features: one, illustrated in Fig. 1a, exhibits edge states, while the other, depicted in Fig. 1b, does not. Both periodic scenarios have a modulation period of  $1 / \alpha = 4$ , which corresponds to four sites (ring resonators) within each cell, and we consider a chain of two cells. The modulation phase parameter  $\delta$  is set to  $\delta = 3\pi /4$  ( $\delta = \pi /4$ ) for the periodic configuration with (without) edge states. In both cases, the periodicity of the sinusoidal loss function—indicated by the dashed black line in Fig. 1a,b—aligns with the lattice periodicity. The described commensurate scenarios were implemented by reconfiguring the programmable mesh into a chain of eight rings with uniform coupling strength,  $t = 0.820\mathrm{GHz}$ , and two discrete loss levels,  $l_{1} = 0.034\mathrm{GHz}, l_{2} = 1.840\mathrm{GHz}$ , as shown in Fig. 1c,d. These parameters relate to those in equation (1) by the expressions  $\upsilon_{1} = l_{0} + (l_{1} + l_{2}) / 2$ , and  $\upsilon_{2} = (l_{1} - l_{2}) / \sqrt{2}$ , where  $l_{0} = 0.35\mathrm{GHz}$  is the intrinsic decay rate of the ring resonators (see Supplementary Note 2 for details). Figure 2a shows the real and imaginary parts of the eigenfrequencies of the systems implemented in Fig. 1a (dots) and Fig. 1b (triangles). Although both cases show the emergence of a bandgap of approximately the same size, the first case shows two edge states, whose mode profiles are depicted in Fig. 2b, within the gap near the resonance frequency of the ring resonators at  $f_{0} = 193.366\mathrm{THz}$ , highlighted in red, but the latter does not exhibit any edge modes. For comparison, Fig. 2a also shows the eigenvalues of an equivalent system with the same uniform coupling

![](images/97c76019875ce9f4a2ffef17b43eb6e765fbcd838142eabe9b94e5c2c750a68a.jpg)

![](images/54e1a870aca8143fb3fd8ccd85ae5fb1a52ba2341259bd38c75fff642dd1c7ec.jpg)

![](images/f4bf8f88c0f98ffaa95fb9654be9cfdb219e26e558da12bbc11f14b3129f3d1d.jpg)

![](images/447c4efa3972724f90f2f366ae62ff1406c789507261c9f0478f6ae1076e2c31.jpg)

![](images/912b18ca936e73569696e187981498dfd56a3341e4310d0c3520b12009072e5f.jpg)

![](images/619f9d7284bd0d6522d8c9b0c75a8663c5766c928f9f9c5ea77315f2cfbd78dd.jpg)

![](images/237aea69271eac9dcf454a49ed4f1c6cd5d857eb5340ffb6888b0b01c17f98b5.jpg)

![](images/caf9e27cb18f3693b01e27af6411e97e85da3a57cca5274c9e4b0b85fe9a372c.jpg)

![](images/db6e49fbe4987b97bc9db8d1a9425ae524962015a1422f2131b8dcdddb0665b4.jpg)  
Fig. 2 | Theoretical and experimental characterization of the commensurate configurations with/without edge states. a, Real and imaginary parts of the eigenfrequencies for the commensurate case with edge states shown in Fig. 1a (dots), commensurate case without edge states shown in Fig. 1b (triangles) and the topologically trivial model devoid of any loss modulation (asterisks). b, Spatial distribution of edge states corresponding to the red points shown in

![](images/1fda0167c9e375bfadd8d73c4a70b05348ba1b722e89c17ed1209dd8445a6e1c.jpg)

![](images/545fbe747f7ded433a36c25ad7d17d13d9e8af22e8fb99e35170c0e8863bfef8.jpg)  
Fig. 2a. The colour bar represents the phase  $\phi$  of the fields. c, The real part of the model's eigenfrequencies as a function of modulation phase,  $\delta$ , illustrating topological phase transitions. d, LDOS spectrum. e,f, Normalized field amplitude at each ring for an excitation frequency of  $f = f_{0}(\mathbf{e})$  and  $f = f_{0} + 0.93 \mathrm{GHz}(\mathbf{f})$ . g-i, same as d-f for the commensurate case without edge states.

![](images/0fc43ea6cf60cf6cfbad61acee6dba93c9c4ce539cd3ceddba9e9d996d8a2ef2.jpg)

but no loss modulation (marked by asterisks). It is noteworthy that the modulation phase parameter  $\delta$  serves as a tuning mechanism for inducing topological phase transitions in the model<sup>31</sup>. Figure 2c illustrates the real part of the system's eigenfrequencies plotted against the modulation phase  $\delta$ , where the colour represents the eigenstate's degree of localization (see Supplementary Note 3 for details). We observe that, as the phase of modulation  $\delta$  increases from zero, a bandgap emerges, reaching its maximum around  $\delta = \pi /4$ . Subsequently, the bandgap closes, signifying a topological phase transition, and the system eventually exhibits edge states, denoted by the red points within the gap. Two distinct periodic configurations of the system, characterized by different modulation phase values under investigation in this study, are depicted by the dashed red ( $\delta = 3\pi /4$ ) and dashed blue ( $\delta = \pi /4$ ) vertical lines in Fig. 2c.

First, we characterize the configuration featuring topological edge states by measuring the spectrum of its local density of states (LDOS). In Hermitian systems, the existence of the edge mode is probed by exciting the edge site with light at the frequency of the edge mode<sup>38</sup>. However, in non-Hermitian systems these conditions are not sufficient to excite the edge mode efficiently, and hence the LDOS is a more informative measurement (see Supplementary Note 4 for details). To measure the LDOS spectrum, we excited one ring at a time and measured its intracavity power as a function of excitation frequency. Figure 2d displays the measured LDOS spectrum, normalized to the

input power, which exhibits a notable level of agreement with the temporal coupled mode theory (TCMT) analysis. TCMT is a valid approximation here because the power coupled out of each ring is relatively small and we can thus assume uniform intensity distribution within the rings. For excitation frequencies matching the eigenfrequency of the edge modes, that is, modes 4 and 5 in Fig. 2a, the obtained LDOS spectrum exhibits pronounced intensity localization at the chain's edges, namely at ring 1 and ring 8. This localization pattern serves as a signature of the presence of edge states (see Supplementary Note 5 for step-by-step measurements showing the formation of the edge state). To further illustrate the localization of the system's mode at  $f = f_{0}$ , Fig. 2e presents the normalized amplitude of the system's mode obtained from both experimental results and TCMT analysis by exciting each ring at a time and measuring its output power. Notably, this figure highlights the localization of the mode at the chain's edge rings. The presence of the bulk modes in the band is illustrated by the relatively high intensity in the middle rings 4 and 5, peaking at frequencies  $f - f_{0} \approx \pm 1 \mathrm{GHz}$ . To provide further clarity regarding the delocalization of these modes, we depict the normalized field amplitude of the rings at  $f - f_{0} = 0.93 \mathrm{GHz}$  in Fig. 2f. Rings with similar levels of loss demonstrate comparable amplitudes for the mode, thus suggesting the mode's delocalization. It is also worth mentioning that choosing a chain with eight microring resonators is sufficient to accurately capture the topological properties of the non-Hermitian AAH model (Supplementary Note 6).

![](images/dfb2bf057eafb07890a2d07e252dcacdd90bc7b40d36590527c83c2aeef72865.jpg)

![](images/c10ea9c3be1800ef03ddd262a13969ce14994e79aa80a27bc95adacc2f1b40ac.jpg)

![](images/7dc5b1c0b378e1bf81383a9abc0b6eb5c6aa6637d6ce3586281d025b880a5b7e.jpg)

![](images/393b9dde9d60838dd1a68df97dbd4a16d7df81b17af5898bca20a81b15d6a828.jpg)  
Fig. 3 | A quasiperiodic (incommensurate) configuration. a, The loss modulation for the incommensurate case. b, Implementation of the quasiperiodic configuration. c, The real part of the eigenfrequencies of the quasiperiodic configuration as a function of the modulation phase. d, The real

![](images/0d9ff3253256226467cda180f03dfae4c2b4bbb5fa3233e76a1e28a3616f08a3.jpg)  
and imaginary parts of the eigenfrequencies of the system with  $\delta = 0.44\pi$ . e, Normalized mode profiles for eigenmodes 4 and 5 shown in d.f, LDOS spectrum of the incommensurate configuration.

![](images/656fa88545175e4a092f2ff4be6bc2913e7f0e2c596db624ffdd8e75af0d949c.jpg)

Next, we proceeded with similar LDOS analysis for the periodic configuration devoid of edge states, as illustrated in Fig. 1b. The measured and TMCT-calculated LDOS spectrum for this scenario is depicted in Fig. 2g. In this scenario the LDOS spectrum does not exhibit a localization at the edge of the chain for any particular frequency. The heightened intensity around  $f - f_{0} \approx \pm 1$  GHz corresponds to the eigenfrequencies of the two bands of the system plotted with triangles in Fig. 2. The normalized field amplitude at each ring, obtained through local excitation and power detection with excitation frequencies of  $f - f_{0} = \pm 0.93$  GHz, and shown in Fig. 2h,i, respectively, corroborate our inference that the modes of the system in this configuration are delocalized.

# Configuration with incommensurate loss modulation

Finally we turn our attention to the quasiperiodic case with incommensurate loss modulation, schematically depicted in Fig. 3a. To achieve a quasiperiodic configuration we set the parameters as follows:  $\alpha = (\sqrt{5} -1) / 2$ ,  $\delta = 0.44\pi$ ,  $t = 0.63\mathrm{GHz}$ ,  $\upsilon_{1} = l_{0} + 0.94\mathrm{GHz}$  and  $\upsilon_{2} = -0.92\mathrm{GHz}$  in equation (1). In Fig. 3b, we show the implementation of this configuration on the programmable mesh. Notably, because the parameter  $\alpha$  is an irrational number the values of ring losses (indicated by black points) do not align with the lattice periodicity, resulting in an incommensurate (quasiperiodic) configuration. Once again, we plot the real part of the system's eigenfrequencies as a function of the modulation phase parameter in Fig. 3c to elucidate the role of this parameter in topological phase transitions in the incommensurate case. This time we differentiate between localization at the left and right edges: red represents modes localized at the left end of the lattice, blue represents modes localized at the right end, and green represents delocalized modes (see Supplementary Note 3 for details). Here, the bands near the resonance frequency of the rings repeatedly intersect and open as the modulation phase varies. Figure 3d shows the real (left panel) and imaginary (right panel) parts of the system's eigenfrequencies for  $\delta = 0.44\pi$ , corresponding to the dashed brown vertical line in Fig. 3c. Unlike the commensurate scenario, where two edge states are present at  $f \approx f_0$ , here only one mode exhibits localization at the lattice's edge. This becomes evident in Fig. 3e, which depicts the field amplitude inside the rings for these two modes (modes 4 and 5). The origin of this feature lies in the fact

that, despite the real part of their eigenfrequencies being identical, their imaginary parts differ, indicating non-degeneracy between them. In non-Hermitian systems like the one in our experiment, two modes with the same real part but a different imaginary part of their eigenfrequencies can exhibit vastly different localization behaviour. The presence of a single edge mode is easily rationalized from the pumping of the edge mode as a function of the phason. This feature, analogous to the pumping of the edge modes in the Hermitian AAH model, establishes that different terminations of the system are associated with sampling different values of the phason. A single experimental configuration thus corresponds to a phason  $\delta$  featuring a mode on a single edge (see Supplementary Note 7 for further details). Finally, it is worth noting that this incommensurate scenario will provide an attractive platform to observe localization-delocalization transitions in non-Hermitian systems for longer chains.

The LDOS spectrum for the quasiperiodic chain is depicted in Fig. 3f; again, this shows good agreement with TCMT. Notably, in the obtained LDOS spectrum, ring 1 demonstrates localization at  $f = f_{0}$ , while intermediate rings also exhibit considerable power at the same frequency. This observation suggests the coexistence of a localized and a delocalized state at  $f = f_{0}$ .

# Robustness study of the edge states

Next, we study the robustness of the topological edge modes, which in our non-Hermitian model are protected by an emergent Chern number of a parent two-dimensional Hamiltonian where the loss acts as a quasimomenta (see Supplementary Note 8 for details). We first investigate the robustness of the edge states in the periodic configuration depicted in Fig. 1a. The resilience of the system against two kinds of disorders, namely variations in the loss and variations in the resonance frequency of the ring resonators, has been examined. For each excitation frequency, we deliberately perturbed the decay rates,  $l_{1,2}$ , of the rings, with perturbations following a Gaussian distribution having a standard deviation of  $\sigma_{1,2} = 0.1 \times l_{1,2}$ . Each excitation frequency underwent measurements with 20 different random iterations of disorder. In Fig. 4a, we show the normalized measured power in each ring as a function of frequency under local excitation: the red curves show the measurements in the absence of disorder, and the grey curves show the measurements in the presence of each random iteration of disorder in the ring's decay rates. For reference, the power spectrum obtained by

![](images/526663902fa85e983e711aae5c96605617ea893d9910d05b2da80632a2b8487d.jpg)  
a

![](images/78e72b0bb9db13df31b3a00af6f1fbeafa9d559491e8bcbed52a51a8404d16af.jpg)  
$f - f_{0}$  (GHz)

![](images/e546f7b53969f5f3f141269533ffef75b89606f166f4519ac1862155adff430d.jpg)

![](images/fb299a0e976a20abb101e3ba07e1cd1fcc4019991ac796e79ff2767c64b63cd0.jpg)

![](images/15155cddf6f99b464e7737a73e687780c697ffc042b206b967196761f595603b.jpg)  
b  
Fig. 4 | Robustness against disorder in the loss and resonance frequency in the commensurate case. a,b, Plots of the local power spectrum for each ring resonator of the commensurate configuration featuring the edge states depicted in Fig. 1a. The red curves show the unperturbed reference; blue (TCMT) and grey show the effects of loss (a) and frequency (b) disorders.

![](images/090ee5a91b44dcd0709047bc420cee0ad3e488fbc0a0e883ba783ecd558d7411.jpg)

![](images/a7f73a0f51819fefc2880c1432c7f977666214764ddcb48e9014221034f42ac3.jpg)  
$f - f_{0}$  (GHz)

![](images/d76bdd84606a9bc398fd8616a8b23029926749a481a59b541775811c8ea69366.jpg)

![](images/73be5106126a16959d1a94caab5ff1544bcfd723d1f2fa21ed31d282b43c3beb.jpg)

![](images/ceacdd9a5888cd4defa0b16cf98d6aaebbdfe7c6d017194e97bfc00180262ad8.jpg)

![](images/103ba7d538d02575670c24a80659567926fe3105e66f1d6d424d12f43548babe.jpg)

TCMT is plotted with dashed blue curves. Disorders in the loss respect the particle-hole symmetry of the system $^{31,32}$ , thereby resulting in the robustness of the topological states against loss disorder.

In contrast, disorder in the resonance frequency of the rings, or in the ring couplings, does not respect the particle-hole symmetry, leading to the disappearance of the robustness of the edge states. To demonstrate this we introduce deliberate perturbations in the resonance frequency of the ring resonators with uniform distribution and a standard deviation of  $\sigma = 0.04 \times \mathrm{FSR}$ , where  $\mathrm{FSR} = 13.97\mathrm{GHz}$  is the free spectral range of the ring resonators, and performed measurements of the power spectrum per ring as described above. The experimental results are shown in Fig. 4b: in the absence of disorder in the resonance frequencies (red curve), the experimental results align closely with the TCMT results (dashed blue curve); in contrast, the grey curves, representing the outcomes under 20 random iterations of disorder in the resonance frequencies show notable fluctuations in the power spectra, observed not only in the vertical direction but also horizontally. This behaviour can be contrasted with the effects of loss disorders shown in Fig. 4a, which primarily induce vertical fluctuations in the spectra. Another important observation evident in Fig. 4b is the alteration in the shape of the rings' power spectrum upon introducing perturbations at the resonance frequency of the rings. To emphasize this further, we have plotted some power spectra with green curves to magnify the change in the shape of the power spectrum. These observations highlight the susceptibility of edge states to disorder in

the resonance frequency of the rings, or equivalently, to variations in the coupling between rings.

We performed a similar analysis of the robustness of the edge mode in the incommensurate scenario. Figure 5 shows measured power spectra of each ring in the absence of disorder (red curves) and under 20 different iterations of random disorder in the loss drawn from a Gaussian distribution with  $\sigma_{n} = 0.1 \times l_{n}$ ,  $n = 1, 2, \ldots, 8$ . These results highlight a high level of robustness to disorder preserving the particle-hole symmetry, similar to that of the periodic case with edge states.

# Discussion and conclusion

We have demonstrated here a photonic system in which topological properties arise exclusively from the system's non-Hermiticity. We showed that non-trivial topological phases and topological edge modes can arise in the presence of periodic or quasiperiodic loss modulation. Our robustness analysis revealed that the topological edge modes in these systems are immune to kinds of disorder that preserve the particle-hole symmetry, such as disorder in the loss, but not to disorder that breaks such symmetry, such as disorder in the resonant frequency that affects the coupling terms.

The AAH model<sup>42</sup> has been extensively studied in the realm of condensed matter physics, providing insights into the behaviour of quantum particles in periodic or quasiperiodic potentials. In photonics, the AAH model has underpinned many of the studies of topology in quasicrystals, leading to crucial demonstrations of topological

![](images/d2e9056532fee262241b6dbd6f1d1591149d6569c2338559c68596b3ceb9d750.jpg)

![](images/aac2cc8995048314a0184ab39e892ff7eca2db6c3f6cf8dd44b9fdf08c9e8a34.jpg)  
Fig. 5 | Robustness against disorder in the loss in the incommensurate case. Plots of the local power spectrum for each ring resonator of the incommensurate configuration depicted in Fig. 3a. The red curves show the unperturbed reference; blue (TCMT) and grey show the effects of loss disorders.

![](images/c138186c6576d58ae624d3ab373120ca1d523adcab6d2ee7c6b747cb90c99bd3.jpg)

![](images/ea41cf1ac8d19ad3695814a7f548eb12e82ce88bb7a706fcb17c0290cc4a430a.jpg)  
$f - f_{0}$  (GHz)

![](images/2c6db747cb77f08381c70e6b71eaf714dac66b75b9da763166d313e6768d0950.jpg)

![](images/6a6f796856aac73e345ca283936d632d5c196c6d642f91bcca85b2d79aa53ff0.jpg)

![](images/4bb5a1a44b7b4b361393db2bbb151d846a0477564b3243cc324faf75d20eb6a7.jpg)

![](images/72026ae14675d58f81ae0a628e1d9ab6df27a9b26ba381e2f2f2629520f7cb97.jpg)

pumping $^{43}$  and topologically protected quantum interference $^{44}$ , among many others. Adding to the previous literature on non-Hermitian extensions of the AAH model $^{25,30-32,45-47}$ , our programmable non-Hermitian platform allows for extensive exploration of the intricate dynamics in non-Hermitian systems. The quasiperiodic configuration of this model, specifically, offers a convenient testing ground to explore phase transitions in dissipative quasicrystals.

This method of creating topological transitions by solely modulating the imaginary part of the onsite potential could also have implications in two-dimensional schemes. For example, a strong parallelism can be drawn with bimorphic topological insulators<sup>48</sup>, based on modulation of the real part of the onsite potential as a function of time. The ideas presented here could provide inspiration for non-Hermitian versions of bimorphic topological insulators using time modulation of the imaginary part of the onsite energy.

Naturally, these ideas can also penetrate the field of topological laser arrays, a crucial application domain for non-Hermitian topology. By allowing the imaginary part of the Hamiltonian in equation (1) to be positive (gain) or negative (loss), this model can be easily adapted to incorporate gain and loss modulation<sup>30</sup>.

Overall, our results point to new avenues of research in non-Hermitian topological photonics where loss, far from being a nuisance, becomes a powerful knob to control the topological properties of electromagnetic modes.

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41563-025-02278-8.

# References

1. Ozawa, T. et al. Topological photonics. Rev. Mod. Phys. 91, 015006 (2019).  
2. Price, H. et al. Roadmap on topological photonics. J. Phys. Photonics 4, 032501 (2022).  
3. Bandres, M. A. et al. Topological insulator laser: experiments. Science 359, eaar4005 (2018).  
4. Contractor, R. et al. Scalable single-mode surface-emitting laser via open-Dirac singularities. Nature 608, 692-698 (2022).  
5. Kumar, A. et al. Topological sensor on a silicon chip. Appl. Phys. Lett. 121, 011101 (2022).

6. Blanco-Redondo, A., Bell, B., Oren, D., Eggleton, B. J. & Segev, M. Topological protection of biphoton states. Science 362, 568-571 (2018).  
7. Mittal, S., Goldschmidt, E. A. & Hafezi, M. A topological source of quantum light. Nature 561, 502-506 (2018).  
8. Dai, T. et al. Topologically protected quantum entanglement emitters. Nat. Photonics 16, 248-257 (2022).  
9. Hashemi, A., Zakeri, M. J., Jung, P. S. & Blanco-Redondo, A. Topological quantum photonics. APL Photonics 10, 010903 (2025).  
10. Nasari, H., Pyrialakos, G. G., Christodoulides, D. N. & Khajavikhan, M. Non-Hermitian topological photonics. Opt. Mater. Express 13, 870-885 (2023).  
11. Yan, Q. et al. Advances and applications on non-Hermitian topological photonics. *Nanophotonics* 12, 2247-2271 (2023).  
12. Kawabata, K., Shiozaki, K., Ueda, M. & Sato, M. Symmetry and topology in non-Hermitian physics. Phys. Rev. X 9, 041015 (2019).  
13. Meng, H., Ang, Y. S. and Lee, C. H. Exceptional points in non-Hermitian systems: applications and recent developments. Appl. Phys. Lett. 124, 060502 (2024).  
14. Ding, K., Fang, C. & Ma, G. Non-hermitian topology and exceptional-point geometries. Nat. Rev. Phys. 4, 745-760 (2022).  
15. Rudner, M. S. & Levitov, L. S. Topological transition in a non-Hermitian quantum walk. Phys. Rev. Lett. 102, 065703 (2009).  
16. Esaki, K., Sato, M., Hasebe, K. & Kohmoto, M. Edge states and topological phases in non-Hermitian systems. Phys. Rev. B 84, 205128 (2011).  
17. Diehl, S., Rico, E., Baranov, M. A. & Zoller, P. Topology by dissipation in atomic quantum wires. Nat. Phys. 7, 971-977 (2011).  
18. Schomerus, H. Topologically protected midgap states in complex photonic lattices. Opt. Lett. 38, 1912-1914 (2013).  
19. Leykam, D., Bliokh, K. Y., Huang, C., Chong, Yi. Dong & Nori, F. Edge modes, degeneracies, and topological numbers in non-Hermitian systems. Phys. Rev. Lett. 118, 040401 (2017).  
20. Reséndiz-Vázquez, P., Tschernig, K., Perez-Leija, A., Busch, K. & León-Montiel, Roberto de J. Topological protection in non-HermitianHaldane honeycomb lattices. Phys. Rev. Res. 2, 013387 (2020).  
21. Zeuner, J. M. et al. Observation of a topological transition in the bulk of a non-Hermitian system. Phys. Rev. Lett. 115, 040402 (2015).  
22. Weimann, S. et al. Topologically protected bound states in photonic parity-time-symmetric crystals. Nat. Mater. 16, 433-438 (2017).

23. Zhao, H. et al. Non-Hermitian topological light steering. Science 365, 1163-1166 (2019).  
24. Liu, Y. G. N., Jung, P. S., Parto, M., Christodoulides, D. N. & Khajavikhan, M. Gain-induced topological response via tailored long-range interactions. Nat. Phys. 17, 704-709 (2021).  
25. Weidemann, S., Kremer, M., Longhi, S. & Szameit, A. Topological triple phase transition in non-Hermitian Floquet quasicrystals. Nature 601, 354-359 (2022).  
26. Dai, T. et al. Non-Hermitian topological phase transitions controlled by nonlinearity. Nat. Phys. 20, 101-108 (2024).  
27. Bahari, B. et al. Nonreciprocal lasing in topological cavities of arbitrary geometries. Science 358, 636-640 (2017).  
28. St-Jean, P. et al. Lasing in topological edge states of a one-dimensional lattice. Nat. Photonics 11, 651-656 (2017).  
29. Zhao, H. et al. Topological hybrid silicon microlasers. Nat. Commun. 9, 981 (2018).  
30. Takata, K. & Notomi, M. Photonic topological insulating phase induced solely by gain and loss. Phys. Rev. Lett. 121, 213902 (2018).  
31. Zhu, B., Lang, Li-Jun, Wang, Q., Wang, Qi. Jie & Chong, Y. D. Topological transitions with an imaginary Aubry-Andre-Harper potential. Phys. Rev. Res. 5, 023044 (2023).  
32. Pereira, E. L., Li, H., Blanco-Redondo, A. & Lado, J. L. Non-Hermitian topology and criticality in photonic arrays with engineered losses. Phys. Rev. Res. 6, 023004 (2024).  
33. Liu, S. et al. Gain- and loss-induced topological insulating phase in a non-Hermitian electrical circuit. Phys. Rev. Appl. 13, 014047 (2020).  
34. Gao, H. et al. Observation of topological edge states induced solely by non-Hermiticity in an acoustic crystal. Phys. Rev. B 101, 180303 (2020).  
35. Gao, H. et al. Non-Hermitian route to higher-order topology in an acoustic crystal. Nat. Commun. 12, 1888 (2021).  
36. Fan, H. et al. Hermitian and non-Hermitian topological edge states in one-dimensional perturbative elastic metamaterials. Mech. Syst. Signal Process. 169, 108774 (2022).  
37. Wetter, H., Fleischhauer, M., Linden, S. & Schmitt, J. Observation of a topological edge state stabilized by dissipation. Phys. Rev. Lett. 131, 083801 (2023).

38. On, M. B. et al. Programmable integrated photonics for topological Hamiltonians. Nat. Commun. 15, 629 (2024).  
39. Dai, T. et al. A programmable topological photonic chip. Nat. Mater. 23, 928-936 (2024).  
40. Capmany, J. & Pérez-López, D. Programming topological photonics. Nat. Mater. 23, 874-875 (2024).  
41. Cem, A., Sanchez-Jacome, D., Pérez-López, D. & Da Ros, F. Thermal crosstalk modeling and compensation for programmable photonic processors. In 2023 IEEE Photonics Conference, 1-2 (IEEE, 2023); https://doi.org/10.1109/IPC57732.2023.10360567  
42. Aubry, S. & Andre, G. Analyticity breaking and anderson localization in incommensurate lattices. Ann. Isr. Phys. Soc. 3, 133 (1980).  
43. Verbin, M., Zilberberg, O., Lahini, Y., Kraus, Y. E. & Silberberg, Y. Topological pumping over a photonic Fibonacci quasicrystal. Phys. Rev. B 91, 064201 (2015).  
44. Tambasco, Jean-Luc et al. Quantum interference of topological states of light. Sci. Adv. 4, eaat3187 (2018).  
45. Yuce, C. Pt symmetric Aubry-André model. Phys. Lett. A 378, 2024-2028 (2014).  
46. Longhi, S. Metal-insulator phase transition in a non-Hermitian Aubry-Andre-Harper model. Phys. Rev. B 100, 125157 (2019).  
47. Zeng, Q.-B., Yang, Y.-B. & Xu, Y. Topological phases in non-Hermitian Aubry-Andre-Harper models. Phys. Rev. B 101, 020201 (2020).  
48. Pyrialakos, G. G. et al. Bimorphic Floquet topological insulators. Nat. Mater. 21, 634-639 (2022).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© The Author(s), under exclusive licence to Springer Nature Limited 2025

# Data availability

All experimental and simulation data supporting the findings are presented in the paper and the Supplementary Information in graphic form. Source data will be provided by the corresponding authors upon request.

# Acknowledgements

A.B.-R. acknowledges support by the NSF award number 2328993. E.L.P. acknowledges support from the Nokia Industrial Doctoral School in Quantum Technology. J.L.L. acknowledges financial support from the Research Council of Finland project numbers 331342 and 358088, and the Jane and Aatos Erkko Foundation. E.L.P. and J.L.L. acknowledge the computational resources provided by the Aalto Science-IT project.

# Author contributions

A.B.-R. and A.H. conceived the experiment and simulations, analysed the results and wrote the paper. A.H. performed the experiments and simulations. J.L.L. and E.L.P. developed the

supporting theory. All authors contributed to technical discussions and edited the paper.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41563-025-02278-8.

Correspondence and requests for materials should be addressed to Andrea Blanco-Redondo.

Peer review information Nature Materials thanks Jianwei Wang and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at

www.nature.com/reprints.