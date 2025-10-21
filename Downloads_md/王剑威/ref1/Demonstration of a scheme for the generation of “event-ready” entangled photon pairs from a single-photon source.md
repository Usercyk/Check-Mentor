# Demonstration of a scheme for the generation of "event-ready" entangled photon pairs from a single-photon source

Qiang Zhang, $^{1,2}$  Xiao-Hui Bao, $^{1}$  Chao-Yang Lu, $^{1}$  Xiao-Qi Zhou, $^{1}$  Tao Yang, $^{1}$  Terry Rudolph, $^{3,4}$  and Jian-Wei Pan $^{1,2}$

<sup>1</sup>Hefei National Laboratory for Physical Sciences at Microscale & Department of Modern Physics,  
University of Science and Technology of China, Hefei, Anhui 230026, People's Republic of China  
$^{2}$ Physikalisches Institut, Universität Heidelberg, Philosophenweg 12, 69120 Heidelberg, Germany  
<sup>3</sup>Optics Section, Blackett Laboratory, Imperial College London, London SW7 2BZ, United Kingdom  
$^{4}$ Institute for Mathematical Sciences, Imperial College London, London SW7 2BW, United Kingdom

(Received 18 October 2006; published 12 June 2008)

We present a feasible and efficient scheme, and its proof-of-principle demonstration, of creating "event-ready" polarization-entangled photon pairs using only simple linear optical elements and single photons. The quality of entangled photon pairs produced in our experiment is confirmed by a strict violation of Bell's inequality. This scheme and the associated experimental techniques present a step toward linear optics quantum computation.

DOI: 10.1103/PhysRevA.77.062316

PACS number(s): 03.67.Mn, 03.65.Ud

# I. INTRODUCTION

There is a considerable worldwide effort to produce clean single-photon sources; whole conferences [1] and journal issues [2] have been devoted to the topic. Leading technologies in this effort are based on physical systems as diverse as quantum dots [3], nitrogen vacancy centers in diamond [4], single trapped atoms [5], filtered signal photons from parametric down conversion [6] and surface acoustic waves in silicon [7], to name but a few. Although they will find immediate uses in quantum communication, one of the more exciting possibilities for single photon sources is that they may be utilized with only linear optical elements and photon number detectors to build a quantum computer, as was shown in the seminal paper of Knill, Laflamme, and Milburn (KLM) [8].

A first necessary step to turn single photons into a useful resource for quantum information processing is to generate "event-ready" entangled pairs from them. Although the KLM scheme shows that this is in principle possible, in practice their proposal requires keeping complicated interferometers stable over a photon wavelength; moreover the gates succeed with probability only 1/16. By contrast we present here an idea for generation of entangled photon pairs from single photons which requires stability only over the coherence length of the photons, and which succeeds with a probability of up to 3/16 [9]. We demonstrate this idea using filtered signal photons from parametric down conversion [6].

# II. SCHEME

Our scheme for generation of an "event-ready" maximally entangled pair of photons, given four single photons as input, is shown in Fig. 1, which works as follows: Four single photons A1,A2,B1,B2 are each prepared in the state  $|H\rangle + |V\rangle$ , corresponding to polarization of  $45^{\circ}$ . Photons A1 and A2 interfere at one polarizing beam splitter (PBS), B1 and B2 interfere at another PBS. The state after the two PBS's is

$$
\begin{array}{l} \left| \psi \right\rangle = \frac {1}{4} (\left| H V \right\rangle_ {A 1 ^ {\prime}} \left| 0 \right\rangle_ {A 2 ^ {\prime}} + \left| 0 \right\rangle_ {A 1 ^ {\prime}} \left| H V \right\rangle_ {A 2 ^ {\prime}} + \left| H \right\rangle_ {A 1 ^ {\prime}} \left| H \right\rangle_ {A 2 ^ {\prime}} \\ + \left| V \right\rangle_ {A 1 ^ {\prime}} \left| V \right\rangle_ {A 2 ^ {\prime}}) \otimes \left(\left| H V \right\rangle_ {B 1 ^ {\prime}} \left| 0 \right\rangle_ {B 2 ^ {\prime}} + \left| 0 \right\rangle_ {B 1 ^ {\prime}} \left| H V \right\rangle_ {B 2 ^ {\prime}} \right. \\ + \left| H \right\rangle_ {B 1 ^ {\prime}} \left| H \right\rangle_ {B 2 ^ {\prime}} + \left| V \right\rangle_ {B 1 ^ {\prime}} \left| V \right\rangle_ {B 2 ^ {\prime}}). \tag {1} \\ \end{array}
$$

The outputs  $\mathrm{A}2^{\prime}$  and  $\mathrm{B}2^{\prime}$  then undergo type-II fusion [9]—specifically they are interfered at a PBS oriented at  $45^{\circ}$  (accomplished by inserting one half-wave plate in each of the two inputs and two outputs of an ordinary PBS), and then undergo polarization sensitive detection. Whenever there is a coincidence between detectors D1 (either D1h or D1v) and D2 (either D2h or D2v), photon  $\mathrm{A}1^{\prime}$  and  $\mathrm{B}1^{\prime}$  will be collapsed into a maximally entangled Bell state. To understand why, note from Eq. (1) that the four-photon state has 16 terms before entering the  $45^{\circ}$  oriented PBS. However, the photons in the state of  $|HV\rangle |0\rangle$  or  $|0\rangle |HV\rangle$  will "stick" together because of the "photon bunching" effect [10] when passing through the  $45^{\circ}$  oriented PBS. Therefore, only the term  $\frac{1}{4}(|H\rangle_{A1^{\prime}}|H\rangle_{A2^{\prime}} + |V\rangle_{A1^{\prime}}|V\rangle_{A2^{\prime}})(|H\rangle_{B1^{\prime}}|H\rangle_{B2^{\prime}} + |V\rangle_{B1^{\prime}}|V\rangle_{B2^{\prime}})$  from Eq. (1) can contribute to the coincidence, where there is one and only one photon in each photon-number detector D1 and D2. Similar to the case of

![](images/8969e2f7090c4104830db228ccfff528140b4f8b0baa3e3bf53ab4917f4b0226.jpg)  
FIG. 1. Scheme for creation of event-ready entangled photon pairs from single photons. RPBS represents a  $45^{\circ}$  oriented PBS.

"entanglement swapping"[11,12],we can rewrite this term as

$$
\begin{array}{l} \left| \psi \right\rangle = \frac {1}{4} \left(\left| \psi^ {+} \right\rangle_ {A 2 ^ {\prime} B 2 ^ {\prime}} \otimes \left| \psi^ {+} \right\rangle_ {A 1 ^ {\prime} B 1 ^ {\prime}} + \left| \psi^ {-} \right\rangle_ {A 2 ^ {\prime} B 2 ^ {\prime}} \otimes \left| \psi^ {-} \right\rangle_ {A 1 ^ {\prime} B 1 ^ {\prime}} \right. \\ + \left| \phi^ {+} \right\rangle_ {A 2 ^ {\prime} B 2 ^ {\prime}} \otimes \left| \phi^ {+} \right\rangle_ {A 1 ^ {\prime} B 1 ^ {\prime}} + \left| \phi^ {-} \right\rangle_ {A 2 ^ {\prime} B 2 ^ {\prime}} \otimes \left| \phi^ {-} \right\rangle_ {A 1 ^ {\prime} B 1 ^ {\prime}}), \tag {2} \\ \end{array}
$$

where  $|\phi^{\pm}\rangle = |H\rangle |H\rangle \pm |V\rangle |V\rangle$ ,  $|\psi^{\pm}\rangle = |H\rangle |V\rangle \pm |V\rangle |H\rangle$ , and a normalization constant is omitted. Since the linear optical Bell-state analyzer can only discriminate two of the four Bell states, the success probability of the scheme is 1/8.

However, the term  $(|HV\rangle_{A1^{\prime}}|0\rangle_{A2^{\prime}}|0\rangle_{B1^{\prime}}|HV\rangle_{B2^{\prime}} + |0\rangle_{A1^{\prime}}|HV\rangle_{A2^{\prime}}|HV\rangle_{B1^{\prime}}|0\rangle_{B2^{\prime}}) / 4$  may collapse photons A1' and B1' into the maximally entangled state  $(|HV\rangle_{A1^{\prime}}|0\rangle_{B1^{\prime}} + |0\rangle_{A1^{\prime}}|HV\rangle_{B1^{\prime}}) / \sqrt{2}$  when there is a coincidence between D1h(D2h) with D1v(D2v), with a probability of 1/16. This state can be unitary changed into the state  $|\psi^{+}\rangle$  by combing the modes A1' and b1' into a PBS. So the overall success probability of our scheme is 3/16.

# III. EXPERIMENT

In the experiment, we generate the four single photons by filtering signal photons from type-II spontaneous parametric down conversion (SPDC) [13,14]. The setup of our experiment is shown in Fig. 2. A  $394~\mathrm{nm}$  ultraviolet (uv) pulse with a  $76\mathrm{-MHz}$  repetition frequency, passes through a nonlinear crystal (BBO) twice, generates two polarization entangled photon pairs in the state  $|\psi^{-}\rangle$  via type-II SPDC and was changed into the state  $|\phi^{+}\rangle$  with a half-wave plates (HWP). The power of the uv pulse is  $600\mathrm{mw}$ , the overall detection efficiency including the fiber-coupling efficiency and the quantum efficiency of the SPCM is  $10\%$  and 10 000 photon pairs are generated per sec. Four  $45^{\circ}$  linear polarizers are utilized to project the photon pairs into single photons (A1-2, B1-2) each in the state  $|+\rangle = \frac{1}{\sqrt{2}}(|H\rangle + |V\rangle)$ .

With the help of a prism  $\tilde{1}(2)$  mounted on a micrometer translation stage, single-photon A1(B1) and A2(B2) are interfered at a PBS as suggested in Fig. 1. Scanning the prism 1(2)'s position to overlap the input single photons perfectly at the PBS's, we can achieve an "Hong-Ou-Mandle"-type interference curve [15] by measuring the twofold coincidence between the output modes toward detectors D1 and D3 (D2 and D4) behind  $45^{\circ}$  polarizers. We lay the prism 1(2) on the position which provides the best interference visibility (about  $94\%$ ), where perfect temporal overlap is achieved.

After the interference, the output modes  $\mathrm{A}2^{\prime}$ ,  $\mathrm{B}2^{\prime}$  are directed into the  $45^{\circ}$  oriented PBS as is shown in Fig. 2. To further generate the event-ready entangled photon pairs, we vary B2's path length by scanning the delay mirror such that photon  $\mathrm{A}2^{\prime}$  and  $\mathrm{B}2^{\prime}$  arrive at the  $45^{\circ}$  oriented PBS simultaneously.

However, due to the poor fourfold coincidence (about 0.3 per min) and the ultrashort coherence length of the single photons (about  $200\mu \mathrm{m}$ ), it is not easy to achieve a good spatial and temporal overlap of photons  $\mathrm{A}2^{\prime}$  and  $\mathrm{B}2^{\prime}$  at the  $45^{\circ}$  oriented PBS. As such, we developed a two-photon

![](images/5f30af060a9563633541fb5cdf6b1a68ac7310d1869153c25cb050461c05f67e.jpg)  
FIG. 2. Experimental setup for a proof-of-principle demonstration of our scheme. A uv pulse with a length of 180 fs passes through a  $2\mathrm{mm}$  BBO ( $\beta$ -bariumborate) crystal and produces a polarized entangled photon pair via the process of type-II SPDC. The uv pulse is reflected by a delay mirror mounted on a step motor (minimum step is  $0.1\mu \mathrm{m}$ ) to pass the BBO crystal twice and prepare the second entangled photon pairs. HWP and polarizers (POL) are used to project the photon pairs into the product state as the single photons. Prisms 1 and 2 are all mounted on micrometer translation stages (minimum step is  $10\mu \mathrm{m}$ ) to adjust the path length. Four  $45^{\circ}$  HwPs and a normal PBS constitute the  $45^{\circ}$  oriented PBS. Two  $0^{\circ}$  polarizers are placed before detectors 1 and 2 to make a partial Bell-state measurement instead of the PBSs suggested in our original scheme. The photons are collected by fiber couplers into avalanche diode single photon detectors (SPCM) after narrow band filters (with a FWHM of  $2.8\mathrm{nm}$ ).

Mach-Zehnder interferometer to calibrate the time delay between  $\mathrm{A}2^{\prime}$  and  $\mathrm{B}2^{\prime}$  with a slight modification of the setup.

We considered the condition that there is one and only one photon pair generated in the SPDC process, but we cannot tell if it is in the path mode A1 and A2 or in B1 and B2 [16]. Thus the state after the four polarizers will be  $\left| + + \right\rangle_{A1A2} + e^{i\phi}\left| + + \right\rangle_{B1B2}$ , where the phase  $\phi$  is determined by the position of the delay mirror. After the first two PBSs, the state is,  $|HH\rangle_{A1^{\prime}A2^{\prime}} + |VV\rangle_{A1^{\prime}A2^{\prime}} + |HV\rangle_{A1^{\prime}} + |HV\rangle_{A2^{\prime}}$ $+e^{i\phi}(|HH\rangle_{B1^{\prime}B2^{\prime}} + |VV\rangle_{B1^{\prime}B2^{\prime}} + |HV\rangle_{B1^{\prime}} + |HV\rangle_{B2^{\prime}})$ . Then we change the two half-wave plates at the input modes of the  $45^{\circ}$  oriented PBS from  $45^{\circ}$  to  $0^{\circ}$ . With this modification, the photon bunching effect will disappear. Only the two terms  $|HV\rangle_{A2^{\prime}}$  and  $|HV\rangle_{B2^{\prime}}$  in the state above can provide a coincidence of detectors D1 and D2. When the two modes A2' and B2' are overlapped perfectly, the state of the two output modes of the last PBS will be  $|H\rangle |V\rangle +e^{i\phi}|V\rangle |H\rangle$ . As is shown in Fig. 3, we scan the delay mirror with a step motor to observe the two-photon interference curve and lock the delay at the position with the best visibility, which is just the position for the photons to perfectly overlap. Since only two photons are involved in the process above, the coincidence is much higher than in the four-photon case and makes it much easier to find the interference position. This step is only helping to calibrate the delay between mode A2' and B2'.

In this proof-of-principle demonstration, we only identify the state  $|\phi^{+}\rangle_{A2'B2'}|\phi^{+}\rangle_{A1'B1'}$ . However, higher probability

![](images/6ed5fe3ccf1bcf0411d01d3a03d1ca31635b2669bf0ed2751e9e1b09b741b89a.jpg)  
FIG. 3. Interference fringe observed when the delay mirror is moved to achieve perfect temporal overlap. We measure the twofold coincidence between the output modes toward detectors D1 and D2 behind  $45^{\circ}$  polarizers, by scanning the position of the delay mirror with step sizes of  $1\mu \mathrm{m}$ . The envelope of the observed twofold coincidence varies indicating the visibility of the two-photon coherence. Inside the coherent region, the best visibility is obtained at the position where perfect temporal overlap is achieved.

can be achieved with minor modification [17]. In the experiment, we put two  $0^{\circ}$  polarizers in front of D1 and D2, respectively, instead of the PBSs in the idealized scheme, which are utilized to discriminate  $\left|\phi^{+}\right\rangle_{A2'B2'}$  and  $\left|\psi^{+}\right\rangle_{A2'B2'}$ . Only the state  $\left|\phi^{+}\right\rangle_{A2'B2'}$  can provide a coincidence between D1 and D2.

Upon projection of photon  $A2^{\prime}$  and photon  $B2^{\prime}$  into the  $\left|V\right\rangle \left|V\right\rangle$  state, photons  $A1^{\prime}$  and  $B1^{\prime}$  should be in the state  $\left|\phi^{+}\right\rangle_{A1'B1'}$ . To verify whether this entangled state is obtained or not, we analyze the polarization correlation between photon  $A1^{\prime}$  and photon  $B1^{\prime}$  conditioned on coincidences of D1 and D2. We utilize two polarizers in modes  $A1^{\prime}$  and  $B1^{\prime}$  to analyze the polarization coherence. B1's polarizer is put at 0 or  $45^{\circ}$ , and we change the polarizer in A1's mode to do the analysis. If the entangled photon pair is produced, the twofold coincidence between  $A1^{\prime}$  and  $B1^{\prime}$  should show two sine curves as functions of  $\theta_{A1'}$ , as  $\theta_{B1'}$  is set at 0 or  $45^{\circ}$ , respectively. Figure 4 shows the experimental result for the coincidences between  $A1^{\prime}$  and  $B1^{\prime}$ , given that photons  $A2^{\prime}$  and  $B2^{\prime}$  have been registered as a trigger. The experimentally obtained coincidences shown in Fig. 4 have been fitted by a joint sine function with the same amplitude for both curves. The observed visibility of  $89\%$  clearly surpasses the 0.71 limit of Bell's inequality [18], which indicates the photon pair is genuinely entangled.

The high-visibility sinusoidal coincidence curves in the experiment imply a violation of the Bell-Clauser-Horne-Shimony-Holt (CHSH) [19] inequality,  $S < 2$  for any local theory, where  $S = E(a,b) - E(a,b') + E(a',b) + E(a',b')$ . Here  $E(a,b)$  are the usual expectations of differences in correlation or anticorrelation of the outcomes, where  $a$ ,  $a'$  ( $b$ ,  $b'$ ) is the polarizer setting for photon  $A1'$  ( $B1'$ ). In our experiment, we set  $a = 0$ ,  $a' = 45$ ,  $b = 22.5$ , and  $b' = 67.5$ , which maximizes the prediction of quantum mechanics of  $S$  to  $S_{qm} = 2.8$  and leads to a contradiction between locality and the predictions of quantum mechanics. The four correlation coefficients between photons 1 and 3 gave the following

![](images/7b86fc7c37d505e3d5e818fcc6ac444604f5f6ccb2d0812cdc8342a05741a2b4.jpg)  
FIG. 4. (Color online) Entanglement verification. Coincidence between photon  $A1'$  and  $B1'$  conditioned on the detection of photon  $A2'$  and photon  $B2'$ . When setting photon  $B1'$  at 0 or  $45^{\circ}$ , respectively, and varying the polarizer angle  $A1'$ , the two sine curves with a visibility of  $89\%$  demonstrate that the two single photons  $A1'$  and  $B1'$  are genuinely entangled.

results:  $E(0,22.5) = 0.57 \pm 0.05$ ,  $E(0.67.5) = -0.67 \pm 0.04$ ,  $E(45,22.5) = 0.65 \pm 0.04$ , and  $E(45,67.5) = 0.69 \pm 0.04$ . Hence  $S = 2.58 \pm 0.07$ , which violates the classical limit of 2 by 6 standard deviations. In fact, in order to simply confirm the state is entangled,  $S > \sqrt{2}$  suffices [20], and our data exceeds this by more than 16 standard deviations. Since our average photon-pair generation rate per pulse is about 0.05, the contribution to the fourfold coincidence of the noise from three-pair emission in SPDC is nearly  $2\%$ . The main reason for the imperfect visibility is due to the three nonideal interferometers.

# IV. CONCLUSION

In summary, we have presented a feasible and efficient scheme to create event-ready entangled photon pairs with single photon sources and detectors. We also provide a proof-in-principle experimental demonstration of the scheme with the help of filtered signal photons from down conversion. The generated entangled photon pairs exhibit a strict violation of Bell's inequality by six standard deviations. Although our experiment is only a proof-in-principle demonstration which still needs postselection, the techniques developed in the experiment can be readily used to generate heralded entangled photon pairs with the help of photon number detectors [21,22], which will find more application in long distance quantum communication [23] and large scale quantum computation [8,9].

# ACKNOWLEDGMENTS

This work was supported by the NNSF of China, the CAS, the PCSIRT and the National Fundamental Research Program. This work was also supported by the Marie Curie Excellent Grant of the EU, the Alexander von Humboldt Foundation, and the Engineering and Physical Sciences Research Council of the UK.

[1] Single-Photon Workshop (SPW) 2005: Sources, Detectors, Applications and Measurement Methods, 24–26 October 2005, National Physical Laboratories, Teddington, UK (unpublished) http://www.spw2005.npl.co.uk/  
[2] P. Grangier, B. Sanders, and J. Vuckovic, New J. Phys. 6, E04 (2004).  
[3] P. Michler et al., Science 290, 2282 (2000); C. Santori, M. Pelton, G. Solomon, Y. Dale, and Y. Yamamoto, Phys. Rev. Lett. 86, 1502 (2001); V. Zwiller et al., Appl. Phys. Lett. 78, 2476 (2001); Z. Yuan et al., Science 295, 102 (2002); J. Vuckovic, D. Fattal, C. Santor, G. S. Solomon, and Y. Yamamoto, Appl. Phys. Lett. 82, 3596 (2003).  
[4] C. Kurtsiefer, S. Mayer, P. Zarda, and H. Weinfurter, Phys. Rev. Lett. 85, 290 (2000); A. Beveratos et al., Eur. Phys. J. D 18, 191 (2002).  
[5] A. Kuhn, M. Henrich, and G. Rempe, Phys. Rev. Lett. 89, 067901 (2002); J. McKeever et al., Science 303, 1992 (2004).  
[6] T. B. Pittman, B. C. Jacobs, and J. D. Franson, Phys. Rev. A 66, 042303 (2002).  
[7] C. L. Foden, V. I. Talyanskii, G. J. Milburn, M. L. Leadbeater, and M. Pepper, Phys. Rev. A 62, 011803(R) (2000).  
[8] E. Knill, R. Laflamme, and G. J. Milburn, Nature (London) 409, 46 (2001).  
[9] D. E. Browne and T. Rudolph, Phys. Rev. Lett. 95, 010501 (2005).  
[10] J. Beugnon et al., Nature (London) 440, 779 (2006).  
[11] M. Zukowski, A. Zeilinger, M. A. Horne, and A. K. Ekert, Phys. Rev. Lett. 71, 4287 (1993).  
[12] J.-W. Pan, D. Bouwmeester, H. Weinfurter, and A. Zeilinger,

Phys. Rev. Lett. 80, 3891 (1998).  
[13] P. G. Kwiat, K. Mattle, H. Weinfurter, A. Zeilinger, A. V. Sergienko, and Y. Shih, Phys. Rev. Lett. 75, 4337 (1995).  
[14] One can also achieve the single photons by photon pairs generated by PDC. We chosed the entangled photon pair from SPDC just because it is easy to approach in our lab. However, the polarizer projection only destroyed the polarization entanglement, but the frequency entanglement between the two photons still exists. So the photons can only be considered as single photon source in its polarization mode.  
[15] C. K. Hong, Z. Y. Ou, and L. Mandel, Phys. Rev. Lett. 59, 2044 (1987).  
[16] T. Yang, Q. Zhang, J. Zhang, J. Yin, Z. Zhao, M. Zukowski, Z. B. Chen, and J. W. Pan, Phys. Rev. Lett. 95, 240406 (2005).  
[17] The paper, J. Joo, P. L. Knight, J. L. O'Brien, and T. Rudolph, Phys. Rev. A 76, 052326 (2007), shows that in principle the success probability of our scheme can be  $1/4$  using only linear optical elements.  
[18] J. S. Bell, Physics (Long Island City, N.Y.) 1, 195 (1964).  
[19] J. F. Clauser, M. Horne, A. Shimony, and R. A. Holt, Phys. Rev. Lett. 23, 880 (1969).  
[20] J. Uffink and M. Seevinck, Phys. Lett. A 372, 1205 (2008).  
[21] E. Waks, K. Inoue, W. D. Oliver, E. Diamanti, and Y. Yamamoto, IEEE J. Sel. Top. Quantum Electron. 9, 1502 (2003).  
[22] M. Fujiwara and M. Sasaki, Appl. Phys. Lett. 86, 111119 (2005).  
[23] H.-J. Briiegel, W. Dur, J. I. Cirac, and P. Zoller, Phys. Rev. Lett. 81, 5932 (1998).