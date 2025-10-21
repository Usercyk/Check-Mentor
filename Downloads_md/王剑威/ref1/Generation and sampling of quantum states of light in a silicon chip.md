# Generation and sampling of quantum states of light in a silicon chip

Stefano Paesani $^{1,6}$ , Yunhong Ding $^{2,3,6*}$ , Raffaele Santagati $^{1}$ , Levon Chakhmakhchyan $^{1}$ , Caterina Vigliar $^{1}$ , Karsten Rottwitt $^{2,3}$ , Leif K. Oxenlowe $^{2,3}$ , Jianwei Wang $^{1,4,5*}$ , Mark G. Thompson $^{1*}$  and Anthony Laing $^{1*}$

Implementing large instances of quantum algorithms<sup>1-5</sup> requires the processing of many quantum information carriers in a hardware platform that supports the integration of different components<sup>6</sup>. Although established semiconductor fabrication processes can integrate many photonic components<sup>7</sup>, the generation and algorithmic processing of many photons has been a bottleneck in integrated photonics. Here, we report the on-chip generation and algorithmic processing of quantum states of light with up to eight photons. Switching between different optical pumping regimes, we implement the scattershot<sup>8,9</sup>, Gaussian<sup>10</sup> and standard boson sampling<sup>3,11-14</sup> protocols in the same silicon chip, which integrates linear and nonlinear photonic circuitry. We use these results to benchmark a quantum algorithm for calculating molecular vibronic spectra<sup>4</sup>. Our techniques can be readily scaled for the on-chip implementation of specialized quantum algorithms with tens of photons, pointing the way to efficiency advantages over conventional computers<sup>15</sup>.

Devices that address customized problems with quantum algorithms are expected to demonstrate an efficiency advantage over conventional computers. Boson sampling is a specific model of quantum computing that is suited to the platform of photonics $^{3,11-14}$  and has been mapped to the calculation of molecular vibronic spectra $^{4}$ , simulation of spin Hamiltonians $^{16}$ , simulation of molecular quantum dynamics $^{5}$  and the enhancement of classical optimization heuristics $^{17}$ . Implementing such applications at a size that challenges conventional computers $^{15}$  demands the integration and high-fidelity operation of a large number of different components, including circuitry $^{7,18,19}$ , detectors $^{20}$ , filters $^{21}$  and photon sources $^{22,23}$ . The low efficiency of individual spontaneous photon sources has motivated the adoption of deterministic solid-state photon sources $^{24-28}$ . However, the low-loss integration of solid-state sources into photonic circuitry is an ongoing challenge $^{29,30}$ .

Creative approaches to realize boson sampling with high numbers of photons from spontaneous sources have seen the design of variant models. In principle, the simultaneous optical pumping of a number  $k$  of spontaneous sources that exceeds the number  $n$  of desired photons boosts the overall rate of photon-pair production combinatorially. In scattershot boson sampling (SBS) $^{8,9,31}$ , one photon from each pair heralds the location of its partner, such that a Fock state of  $n$  photons is prepared over a random subset of modes. In Gaussian boson

sampling (GBS) $^{10}$ ,  $k$  single-mode optical nonlinearities are coherently pumped to produce  $k$  modes of squeezed (vacuum) light, before linear optical processing and  $n$ -photon detection at the output.

The complex photonic circuitry required to scale these approaches can be addressed with integrated photonics. Here, by pumping four integrated spontaneous four wave mixing (SFWM) sources with either a single-colour or a two-colour laser, we select between the Fock state required for SBS and the squeezed state required for GBS. Both states of light are routed on-chip to the same linear optical circuit, which implements a random unitary operation over 12 waveguides. In the GBS mode of operation, we benchmark this class of device for the calculation of vibronic spectra. In the limit of the SBS mode of operation, with  $n = k = 4$ , we implement standard boson sampling with four heralded photons, generating and processing eight photons on-chip. Our analysis shows that larger versions of our silicon photonic chip, which exploit the combinatorial boost in photon rate available through the SBS and GBS protocols, open up the regime of efficiency advantages over conventional computers.

The silicon circuitry and configuration of these experiments can be understood with reference to Fig. 1. Four SFWM spiral sources are coherently pumped by on-chip splitting of the near-1,550 nm pump laser via multi-mode interference (MMI) near 50:50 beamsplitters; pump light is then removed by asymmetric Mach-Zehnder interferometers (AMZIs). In the dual-wavelength pumping (GBS) scheme (where photons are generated at the same signal wavelength), two spectral regions of the temporally compressed (spectrally broadened) pump are selected and recombined using wavelength-division multiplexers (WDMs), before injection to the chip. In the single-wavelength pumping (SBS) scheme (where signal and idler photons are generated at different wavelengths), idler photons are separated using a second layer of AMZIs and coupled out to a fibre array to herald the presence of the signal photons. In both regimes, signal photons are routed to the four central modes of a continuous random walk, implemented over 12 evanescently coupled waveguides, then coupled out to the fibre array. Ultra-low-loss outcoupling is implemented by aluminium assisted apodized grating couplers, with a measured coupling efficiency of  $-1.1\mathrm{dB}$  (refs. [32],[33]). An array of 16 superconducting nanowire single-photon detectors (SNSPDs) with  $\sim 78\%$  efficiency detect the four heralding modes and the 12 modes from the random walk (see Supplementary Section 1 for details).

![](images/ff6f7f8ccd6a6b2fd20343e246b8c5cbee5866b5514862d687bd8e2ff064e0da.jpg)  
a

![](images/f9730e20c33e5efd05188ebb023fdfdb9cbed419409db2705c31dc7e82568130.jpg)  
c  
Fig. 1 | Silicon photonic chip and experimental configuration. a, The silicon chip integrates four SFWM spiral photon sources and twelve continuously coupled waveguides with a network of MMIs and grating couplers. AMZIs separate the idler (blue) and signal (red) photons, and remove pump light (purple). b, The SBS pumping scheme, where two-mode vacuum squeezing (TMS) is generated via non-degenerate SFWM, comprises a  $1,550\mathrm{nm}$  laser with a bandwidth of  $2\mathrm{nm}$ , and a WDM for wavelength selection. In the GBS scheme, which relies on single-mode squeezing (SMS) generation via degenerate SFWM, a pulse compressor increases the bandwidth to  $10\mathrm{nm}$ , WDMs select dual wavelengths, and a delay line synchronizes the arrival of the two pulses. The selected spectra, in the wavelength domain, are shown at the different stages of the schemes. c, In a given run of the SBS protocol, the detection pattern  $\mathbf{j}$  measured in the idler modes heralds the modes in which signal photons enter the random walk. The probability to measure a given pattern  $\mathbf{k}$  after the random walk (described by a unitary matrix  $T$ ) is related to the permanent of a sub-matrix of  $T$ , whose rows and columns are defined by  $\mathbf{j}$  and  $\mathbf{k}$ , respectively. d, In a given run of the GBS protocol, four SMS states are generated and delivered to the random walk. The probability for a given measurement pattern in the GBS protocol is given by the Hafnian of sub-matrices of  $B$ , which is a function of both  $T$  and the squeezing parameters.

![](images/4fea5acb390d9303423e8725d3e43f4f230499cbb827c3f86df72baebd3a4916.jpg)  
d

![](images/834ec9728f791a24d85e4556cbab6e748f5f6dd614bfbf6c6e407868b8b76991.jpg)  
b

The SBS protocol is designed to tackle the inefficiency that results from implementing standard boson sampling with spontaneous photon sources. In the original model of boson sampling, a linear optical circuit is configured to implement a random unitary operation over  $m$  modes. A number  $n < m$  of input ports are each populated with a single photon, such that  $n$  photons undergo an  $n \times m$  random operation, before detection with photon counters. Because the probability amplitude for each  $n$ -photon transition is equal to the permanent of the corresponding transfer matrix, which is in general intractable to classical computation, an ideal experiment would efficiently produce samples from a classically computationally hard probability distribution. However, the rate at which the required  $n$ -photon state is produced with spontaneous sources decreases exponentially with  $n$ . As shown in Fig. 1c, the SBS protocol addresses this inefficiency by pumping  $k$  sources that each produce weak TMS light (with  $n < k \leq m$ ). The algorithm requires in total  $2n$  photons, where one (idler) photon from each pair is directly detected to identify the input port of its partner (signal) photon. In comparison to the original scheme, the probability to generate  $n$ -signal photon input states is boosted by a factor  $\propto \binom{k}{n}$  (refs. 8,9).

We implemented the SBS protocol in our silicon chip, with  $k = 4$  sources, using the single wavelength pumping scheme shown in Fig. 1b. The experimentally measured distribution  $p$  for the  $n = 3$  case (six-photon events) shown in Fig. 2a, has a mean statistical fidelity  $F = \sum_{i} \sqrt{p_i q_i}$  with a theoretical distribution  $q$  of  $92\%$ . Figure 2b shows the measured difference in photon pair generation rates between the SBS and standard boson sampling (where only  $n$  sources are pumped) protocols for  $n = 1$  to 3, and for  $n = 4$  where the two regimes converge. As predicted, the  $n$ -photon pair generation rate is enhanced by a factor of approximately  $\binom{4}{n}$ . In the SBS regime, the two-pair and three-pair photon rates were measured at

$5.8\mathrm{kHz}$  and  $4\mathrm{Hz}$ , respectively, while the four-pair (eight-photon) rate was approximately four events per hour. The average purity of the signal photons, estimated via unheraldined second-order correlation measurements<sup>34</sup>, was calculated to be  $86\%$  (see Supplementary Section 5 for details).

Although fidelity comparisons with theoretical distributions are not a scalable method of validating boson sampling, a more efficient alternative, although still computationally hard, is to compare measurements against those predicted by a classically tractable and plausible distribution. As shown in Fig. 2c, we used a Bayesian model comparison $^{9,18,35-37}$  to validate our  $n = 4$  (eight-photon) statistics against those predicted by distinguishable photons (the  $n = 3$  case is shown in the inset). The dynamically updated confidence that samples are drawn from the distribution of indistinguishable particles versus distinguishable particles reaches higher than  $99.9\%$  (see Supplementary Section 6 for details and Supplementary Section 8 for additional validation tests).

In contrast to SBS, the GBS protocol does not project the input state onto a single Fock state. Rather, the input in GBS is an ensemble of SMS states, as shown in Fig. 1d, which further increases the  $n$ -photon detection probability as compared to  $\mathrm{SBS}^{10}$ . After processing with linear optical circuitry, the probability for a particular pattern at single-photon detectors is given by a function known as the Hafnian of the relevant transfer matrix. Similar to the permanent of a matrix, the Hafnian is computationally hard to calculate[10,38,39] (see Supplementary Section 9 for details).

We implemented the GBS protocol using the two-colour pumping scheme described in Fig. 1b, which generates weak single-mode squeezed light at each source. Although this spectral selection reduces the pump power below that of the single-colour configuration, we observed statistics with up to four signal photons at a  $1.1\mathrm{Hz}$  rate. The experimentally measured distribution for  $n = 4$

![](images/e6b456891bad2a87fc2e138499e6051039d781383c21e3d37e53174603c73583.jpg)

![](images/e2296283d2ec6879340840f5f9ac2cf8a1df6bd885e4d40e768c81343c738cd5.jpg)  
Fig. 2 | Results for SBS. a, Experimental and theoretical distribution for six-photon events, with anti-bunched states (one photon per detector) on the horizontal axis in increasing order  $\{(1,2,3),(1,2,4),\ldots,(10,11,12)\}$  from left to right; input states on the vertical axis are  $\{(1,2,3),(1,2,4),(1,3,4),(2,3,4)\}$  from bottom to top. b, Measured event rates for two to eight photons are shown for the SBS (black points) and standard (red points) regimes. Dashed lines are fits to the theoretical rates for  $n$ -photon events emitted from four sources in SBS, and from  $n$  sources in standard boson sampling. For standard boson sampling, data are reported for all  $\binom{4}{n}$  possible input configurations, with markers overlapping due to similar rates. Inset: photon rate enhancement for SBS over the standard boson sampling protocol. Error bars, one standard deviation confidence intervals, calculated assuming Poissonian counting statistics. c, Dynamic Bayesian model updating for validation that statistics are from indistinguishable rather than distinguishable photons for eight photons (inset, six photons).

![](images/5c011154d7c858f25439880161a1db01bd75c4d315c6a4b651270d10dcea645c.jpg)

![](images/3b321a2c57a4968e3675cc547ff72996910386a323cd3ce806b9312a11c02a94.jpg)

![](images/35acc39cea38d5b64cff6294f04a872fa57fe8d31c8768bcbc3356038d35455f.jpg)  
Fig. 3 | Experimental results for GBS. a, Experimental distribution for four-photon events, showing an  $87\%$  fidelity with the theoretical distribution. The horizontal axis labels anti-bunched (one photon per detector) states in increasing order  $\{(1,2,3,4), (1,2,3,5), \ldots, (9,10,11,12)\}$  from left to right.  
b, Results of dynamic Bayesian model updating to validate that data are from the ideal GBS model of single-mode squeezed states (SMS GBS, blue lines) against alternative (red lines) states; from left to right—thermal, coherent, distinguishable SMS and TMS states.

photons, with one photon per detector (full anti-bunching), shown in Fig. 3a, has a mean statistical fidelity of  $87\%$  with the ideal theoretical distribution. In validating GBS, a wide range of alternative models is available where output distributions arising from general Gaussian input states are classically tractable. As illustrated in Fig. 3b, we focus on models that are plausible in our experiment. We validate the ideal input state of four SMS states against input with the following: thermal states, resulting from excessive loss; coherent states, from unfiltered pump light; distinguishable SMS light, due to spectral mismatch; TMS states, from spurious photons generated at

different wavelengths. For each test, a confidence  $>99.9\%$  is reached after  $\sim 120$  samples for an ideal model using SMS states rather than the alternative models (see Supplementary Section 10 for details).

An application related to GBS is the calculation of molecular vibronic spectra $^{4,40,41}$ , where programmable linear optical circuitry, together with squeezed and displaced light, can approximate probabilities for the vibrational transition (Frank-Condon factors) between ground and excited states of a given molecule. Although most resources employed are the same as in GBS, in the reconstruction of Franck-Condon (FC) profiles, photon-number detection on

![](images/c0e61f3e242792d309f37731423acc8a945721660260239779bad58be9282e3a.jpg)  
Fig. 4 | Reconstructed FC profile. Reconstructed FC factors from number-resolved GBS data (black) for frequencies  $\omega$  are contrasted with theoretical estimates (red) for contributions of up to eight photons ( $>8$  photon contributions are negligible). Inset: the improvement over optimal classical strategies in the fidelity of estimating the FC profile, using simulated squeezing. The solid line plots cases that simulate squeezing by processing experimental data, while the dashed line indicates no post-processing. Red circle, the specific FC profile plotted in the main figure.

the individual output modes is required, while no post-selection on the total number of photons is performed, rendering the protocol more susceptible to imperfections compared to standard GBS. To investigate the performance of silicon photonic chips for this application, we mapped our random walk circuit to a synthetic molecule, implemented a pseudo-number-resolving detection scheme (see Supplementary Section 13) and considered the difference  $\mathcal{C} = F_{\mathrm{Q}} - F_{\mathrm{C}}$  between the fidelity of the reconstructed Franck-Condon profile  $F_{\mathrm{Q}}$  and the optimal fidelity obtainable from a classical strategy  $F_{\mathrm{C}}$  (ref. [40]). The merit of this procedure in the present device is to benchmark the quality of the produced squeezed states (assuming high-fidelity linear optics[19,42]) when addressing molecular vibronic spectra simulations. Although the FC profile directly reconstructed from number-resolved GBS measurements has a fidelity of  $>99\%$  to the ideal FC profile, the low level of squeezing means that classically tractable vacuum contributions dominate and the improvement over a classical strategy is small ( $\mathcal{C} = 0.4\%$ ).

Data post-processing, based on characterized losses and detection efficiencies, makes it possible to investigate how the fidelity of the FC profile depends on the amount of squeezing, as shown in Fig. 4 (inset). In fact, varying the squeezing values by a constant factor  $\gamma$  results in a trivial renormalization dependent on the photon number  $n$ . Consequently, for the FC profile calculation, only the relative probabilities of contributions with different photon numbers are affected as  $p^{\prime}(\mathbf{k})\propto \gamma^{n}p(\mathbf{k})$ . This allows us to approximate a profile arising from higher squeezing values (that is,  $\tanh \xi_{i} = \gamma \tanh \overline{\xi}_{i}$ , where  $\overline{\xi}_i$  is the implemented squeezing of the ith source, and  $\xi_{i}$  is the postprocessed squeezing used in Fig. 4). For moderate levels of post-processed squeezing, an improvement of up to  $\mathcal{C} = 9\%$  corresponding to  $F_{\mathrm{Q}} = 86\%$  (shown in Fig. 4), is obtained from post-processing. For high values of squeezing, due to the increased contribution of higher-order photon terms, the approach does not provide any further advantage. See Supplementary Section 13 for details.

Compared to SBS with four heralded photons, we observed much higher rates for four-photon GBS using a pump with lower power, and requiring fewer detectors. This type of resource saving for GBS over SBS increases as the size of the demonstration increases, although GBS requires approximately twice as many photons as SBS to demonstrate efficiency advantages over classical algorithms. Increasing the number and purity of integrated photon sources $^{43}$ , while decreasing the loss in photonic circuitry to reduce noise and distinguishability among photons, leads to similar fidelities when considering the scaling of both the GBS and SBS protocols (for example, loss acts to add noise via thermal components to the initial

SBS-TMS or GBS-SMS resource states). The maximum number of photons we generated and processed in these experiments is eight, which is double the largest reported so far in integrated photonics.

Based on these results and further analyses (Supplementary Section 14), we estimate that arrays of  $\sim 400$  integrated detectors, possible with current fabrication technologies $^{44}$ , would allow fully integrated experiments with up to 48 and 70 signal photons in the SBS and GBS schemes, respectively (Supplementary Fig. 14). Such experiments are expected to enter a regime of quantum efficiency advantages over conventional computers $^{15}$ . In the context of calculating molecular transition probabilities, our class of photonic chip will be useful for reconstructing FC profiles from photonic quantum sampling algorithms, if relevant instances requiring  $>20$  photon events are discovered. More generally, for problems that can be mapped to variant models of boson sampling, such as interrogating the vibrational dynamics of molecules $^{5}$ , our results and analysis show that efficiency advantages over conventional computers are a realistic prospect with the platform of integrated photonics.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, statements of code and data availability and associated accession codes are available at https://doi.org/10.1038/s41567-019-0567-8.

# Data availability

The data that support the plots within this paper and other findings of this study are available at https://doi.org/10.6084/m9.figshare.7492991.

Received: 11 December 2018; Accepted: 22 May 2019

Published online: 1 July 2019

# References

1. Shor, P. W. Algorithms for quantum computation: discrete logarithms and factoring. In 35th Annual Symposium on Foundations of Computer Science 124-134 (IEEE, 1994).  
2. Lloyd, S. Universal quantum simulators. Science 273, 1073-1078 (1996).  
3. Aaronson, S. & Arkhipov, A. The computational complexity of linear optics. In Proceedings of the 43rd Annual ACM Symposium on Theory of Computing 333-342 (ACM, 2011).  
4. Huh, J., Guerreschi, G. G., Peropadre, B., McClean, J. R. & Aspuru-Guzik, A. Boson sampling for molecular vibronic spectra. Nat. Photon. 9, 615-620 (2015).  
5. Sparrow, C. et al. Simulating the vibrational quantum dynamics of molecules using photonics. Nature 557, 660-667 (2018).  
6. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
7. Wang, J. et al. Multidimensional quantum entanglement with large-scale integrated optics. Science 260, 285-291 (2018).  
8. Lund, A. P. et al. Boson sampling from a Gaussian state. Phys. Rev. Lett. 113, 100502 (2014).  
9. Bentivegna, M. et al. Experimental scattershot boson sampling. Sci. Adv. 1, e1400255 (2015).  
10. Hamilton, C. S. et al. Gaussian boson sampling. Phys. Rev. Lett. 119, 170501 (2017).  
11. Broome, M. A. et al. Photonic boson sampling in a tunable circuit. Science 339, 794-798 (2013).  
12. Spring, J. B. et al. Boson sampling on a photonic chip. Science 339, 798-801 (2013).  
13. Crespi, A. et al. Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nat. Photon. 7, 545-549 (2013).  
14. Tillmann, M. et al. Experimental boson sampling. Nat. Photon. 7, 540-544 (2013).  
15. Neville, A. et al. Classical boson sampling algorithms with superior performance to near-term experiments. Nat. Phys. 13, 1153-1157 (2017).  
16. Olivares, D. G., Peropadre, B., Aspuru-Guzik, A. & Garcia-Ripoll, J. J. Quantum simulation with a boson sampling circuit. Phys. Rev. A 94, 022319 (2016).  
17. Arrazola, J. M. & Bromley, T. R. Using Gaussian boson sampling to find dense subgraphs. Phys. Rev. Lett. 121, 030503 (2018).  
18. Carolan, J. et al. Universal linear optics. Science 349, 711-716 (2015).  
19. Harris, N. C. et al. Quantum transport simulations in a programmable nanophotonic processor. Nat. Photon. 11, 447-452 (2017).

20. Pernice, W. H. P. et al. High-speed and high-efficiency travelling wave single-photon detectors embedded in nanophotonic circuits. Nat. Commun. 3, 1325 (2012).  
21. Harris, N. C. et al. Integrated source of spectrally filtered correlated photons for large-scale quantum photonic systems. Phys. Rev. X 4, 041047 (2014).  
22. Silverstone, J. W. et al. On-chip quantum interference between silicon photon-pair sources. Nat. Photon. 8, 104-108 (2014).  
23. Spring, J. B. et al. Chip-based array of near-identical, pure, heralded single-photon sources. Optica 4, 90–96 (2017).  
24. Ding, X. et al. On-demand single photons with high extraction efficiency and near-unity indistinguishability from a resonantly driven quantum dot in a micropillar. Phys. Rev. Lett. 116, 020401 (2016).  
25. Somaschi, N. et al. Near-optimal single-photon sources in the solid state. Nat. Photon. 10, 340-345 (2016).  
26. Loredo, J. C. et al. Boson sampling with single-photon Fock states from a bright solid-state source. Phys. Rev. Lett. 118, 130503 (2017).  
27. Wang, H. et al. High-efficiency multiphoton boson sampling. Nat. Photon. 11, 361-365 (2017).  
28. Wang, H. et al. Toward scalable boson sampling with photon loss. Phys. Rev. Lett. 120, 230502 (2018).  
29. Laucht, A. et al. A waveguide-coupled on-chip single-photon source. Phys. Rev. X 2, 011014 (2012).  
30. Arcari, M. et al. Near-unity coupling efficiency of a quantum emitter to a photonic crystal waveguide. Phys. Rev. Lett. 113, 093603 (2014).  
31. Zhong, H.-S. et al. 12-photon entanglement and scalable scattershot boson sampling with optimal entangled-photon pairs from parametric downconversion. Phys. Rev. Lett. 121, 250505 (2018).  
32. Ding, Y., Peucheret, C., Ou, H. & Yvind, K. Fully etched apodized grating coupler on the SOI platform with  $-0.58\mathrm{dB}$  coupling efficiency. Opt. Lett. 39, 5348-5350 (2014).  
33. Ding, Y., Ou, H. & Peucheret, C. Ultra-high-efficiency apodized grating coupler using fully etched photonic crystals. Opt. Lett. 38, 2732-2734 (2013).  
34. Christ, A., Laiho, K., Eckstein, A., Cassemiro, K. N. & Silberhorn, C. Probing multimode squeezing with correlation functions. New J. Phys. 13, 033027 (2011).  
35. Bentivegna, M. et al. Bayesian approach to boson sampling validation. Int. J. Quantum Inf. 12, 1560028 (2014).  
36. Spagnolo, N. et al. Experimental validation of photonic boson sampling. Nat. Photon. 8, 615-620 (2014).  
37. Carolan, J. et al. On the experimental verification of quantum complexity in linear optics. Nat. Photon. 8, 621-626 (2014).  
38. Caianiello, E. R. Combinatorics and Renormalization in Quantum Field Theory (W. A. Benjamin, 1973).  
39. Kruse, R. et al. A detailed study of Gaussian boson sampling. Preprint at https://arxiv.org/abs/1801.07488 (2018).  
40. Clements, W. R. et al. Approximating vibronic spectroscopy with imperfect quantum optics. J. Phys. B At. Mol. Opt. Phys. 51, 245503 (2018).

41. Shen, Y. et al. Quantum optical emulation of molecular vibronic spectroscopy using a trapped-ion device. Chem. Sci. 9, 836-840 (2018).  
42. Wilkes, C. M. et al. 60 dB high-extinction auto-configured Mach-Zehnder interferometer. Opt. Lett. 41, 5318-5321 (2016).  
43. Caspani, L. et al. Integrated sources of photon quantum states based on nonlinear optics. Light. Sci. Appl. 6, e17100 (2017).  
44. Schuck, C. et al. Matrix of integrated superconducting single-photon detectors with high timing resolution. IEEE Trans. Appl. Supercond. 23, 2201007 (2013).

# Acknowledgements

The authors thank N. Maraviglia, R. Chadwick, C. Sparrow, L. Banchi, G. Sinclair and D. Bacco for useful discussions and W.A. Murray, M. Louit, E. Johnston, H. Fedder, M. Schlagmüller, M. Borghi and J. Lennon for technical assistance. The authors acknowledge support from the Engineering and Physical Sciences Research Council (EPSRC), the European Research Council (ERC) and European Commission (EC) funded grants PICQUE, BBOI, QuChip, QuPIC, QITBOX, Quantera-eranet Square, VILLUM FONDEN, QUANPIC (ref. 00025298) and the Center of Excellence, Denmark SPOC (ref. DNRF123). J.W. acknowledges support from the Beijing Academy of Quantum Information Sciences (Y18G21) and from The Key R&D Program of Guangdong province (2018B030329001). A.L. acknowledges fellowship support from EPSRC (EP/N003470/1).

# Author contributions

S.P., Y.D., R.S., J.W., M.G.T. and A.L. designed the experiment. Y.D. fabricated the silicon photonics device. S.P., R.S. and C.V. performed the experiment. S.P. and L.C. analysed the data. S.P., Y.D., R.S., L.C. and A.L. wrote the manuscript with feedback from all authors. K.R., L.K.O., M.G.T. and A.L. managed the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Supplementary information is available for this paper at https://doi.org/10.1038/s41567-019-0567-8.

Reprints and permissions information is available at www.nature.com/reprints.

Correspondence and requests for materials should be addressed to Y.D., J.W., M.G.T. or A.L.

Peer review information: Nature Physics thanks Sonja Barkhofen, Robert Keil and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2019