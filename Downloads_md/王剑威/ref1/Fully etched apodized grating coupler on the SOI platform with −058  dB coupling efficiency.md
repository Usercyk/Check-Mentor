# Fully etched apodized grating coupler on the SOI platform with -0.58 dB coupling efficiency

Yunhong Ding, $^{1,*}$  Christophe Peucheret, $^{2}$  Haiyan Ou, $^{1}$  and Kresten Yvind $^{1}$

$^{1}$ Technical University of Denmark, Department of Photonics Engineering, Kongens Lyngby, Denmark

$^{2}$ FOTON Laboratory-CNRS UMR 6082, ENSSAT, University of Rennes 1, 22300 Lannion, France

*Corresponding author: yudin@fotonik.dtu.dk

Received July 3, 2014; revised August 1, 2014; accepted August 6, 2014;

posted August 7, 2014 (Doc. ID 215256); published September 9, 2014

We design and fabricate an ultrahigh coupling efficiency (CE) fully etched apodized grating coupler on the silicon-on-insulator (SOI) platform using subwavelength photonic crystals and bonded aluminum mirror. Fabrication error sensitivity and coupling angle dependence are experimentally investigated. A record ultrahigh CE of  $-0.58$  dB with a 3 dB bandwidth of  $71~\mathrm{nm}$  and low back reflection are demonstrated. © 2014 Optical Society of America

OCIS codes: (130.0130) Integrated optics; (230.3120) Integrated optics devices; (230.1950) Diffraction gratings; (050.2770) Gratings.

http://dx.doi.org/10.1364/OL.39.005348

Grating couplers are attractive thanks to their ability to directly couple light from nanowire waveguides to standard single-mode fibers (SSMFs). The biggest advantage of grating couplers is the large alignment tolerance and absence of need for chip cleaving, making wafer-scale testing possible. Traditional grating couplers are uniform and are shallowly etched in order to introduce a proper scattering strength [1-8]. However, their coupling efficiency (CE) is sensitive to both the etching depth and slot width [1]. Moreover, the CE of such uniform shallowly etched grating couplers is limited not only by power leakage to the substrate, but also by the intrinsic mode mismatch between the gratings and SSMFs. For applications where only fully etched silicon waveguides are present on a photonic-integrated circuit, such as multimode multiplexers [9] or multicore fiber couplers [10], fully etched grating couplers are preferred [11-16] in order to simplify the fabrication process.

Table 1 summarizes the performances of state-of-the-art fully etched and shallowly etched grating couplers that have been demonstrated over the past few years. The highest CE of  $-0.62\mathrm{dB}$  was demonstrated for a shallowly etched grating coupler with an aluminum (Al) mirror, which was realized by etching through the silicon substrate followed by Al deposition [8]. However, the optimum thickness of the lower cladding (i.e. buried oxide (BOX) layer), which is critical for maximizing the CE, might not correspond to that of commercial silicon-on-insulator (SOI) wafers.

In this Letter, we demonstrate an ultrahigh CE fully etched apodized grating coupler on the silicon-on-insulator (SOI) platform using subwavelength photonic crystals (PhCs), an Al mirror, and adhesive bonding to a silicon wafer. With optimum upper and lower  $\mathrm{SiO_2}$  cladding thicknesses,  $-0.58$  dB CE with a wide  $3\mathrm{dB}$  bandwidth of  $71~\mathrm{nm}$  are achieved. Such CE is, to the best of our knowledge, the highest ever reported for grating couplers.

The proposed grating coupler is based on flip-chip bonding of a silica-clad fully etched silicon PhC grating coupler on a silicon carrier wafer, as schematically depicted in Fig. 1. The thickness of the top silicon-device layer is  $250\mathrm{nm}$ . Artificial materials are introduced for

the scattering units, with refractive indices  $n_i$  and lengths of scattering units  $l_i$  changed along the grating [11].  $\mathrm{SiO}_2$  is used as upper and lower cladding material with thicknesses of  $h_u$  and  $h_d$ , respectively. A 100 nm Al mirror is introduced below the lower cladding. Another layer of  $\mathrm{SiO}_2$  is introduced beneath the Al mirror and is bonded to the silicon carrier wafer using a benzocyclobutene (BCB) layer. The coupling angle  $\theta$  is designed to be  $15^\circ$ . In the design, the width  $d_i$  of the artificial material slots is fixed to be  $d_0 = 345 \mathrm{~nm}$ .

The coupling wavelength  $\lambda$  of the grating unit is given by

$$
\lambda = l _ {i} \left[ n _ {\text {e f f}, i} \left(l _ {i}, n _ {i}\right) - n _ {\text {u p}} \sin \theta \right], \tag {1}
$$

where  $n_{\mathrm{up}}$  is the refractive index of the uppermost cladding (air).  $n_{\mathrm{eff},i}$  is the effective refractive index of the

Table 1. Summary of Published Experimental Results for Grating Couplers  

<table><tr><td colspan="3">Fully Etched</td><td colspan="3">Shallowly Etched</td></tr><tr><td>CE (dB)</td><td>3 dB BW (nm)</td><td>Ref.</td><td>CE (dB)</td><td>3 dB BW (nm)</td><td>Ref.</td></tr><tr><td>-3.76</td><td>68</td><td>[12]</td><td>-1.6</td><td>65</td><td>[2]</td></tr><tr><td>-3.7</td><td>60</td><td>[13]</td><td>-1.9</td><td>70</td><td>[3]</td></tr><tr><td>-4.6</td><td>83</td><td>[14]</td><td>-1.2</td><td>48</td><td>[4]</td></tr><tr><td>-2.3</td><td>60</td><td>[15]</td><td>-1.6</td><td>80</td><td>[5]</td></tr><tr><td>-1.65</td><td>60</td><td>[11]</td><td>-1.5</td><td>54</td><td>[6]</td></tr><tr><td>-4.7</td><td>&gt;140</td><td>[16]</td><td>-2.7</td><td>60</td><td>[7]</td></tr><tr><td>-0.58</td><td>71</td><td>This work</td><td>-0.62</td><td>67</td><td>[8]</td></tr></table>

![](images/fd24607a9d4f8967aea177c542016c15d9876711f55c9c6b3122941bfdf0ca59.jpg)  
Fig. 1. Schematic structure of the proposed grating coupler.

scattering unit, which is determined by  $l_{i}$  and  $n_i$ . The light scatters with a power leakage factor  $2\alpha_{i}$  when it propagates through each scattering unit [11]. By jointly optimizing  $n_i$  and  $l_{i}$ , one can tune  $2\alpha_{i}$  while maintaining the scattering angle of  $15^{\circ}$  at  $1550~\mathrm{nm}$ . In order to obtain a Gaussian output profile  $G(z)$  with beam diameter of  $10.4~{\mu\mathrm{m}}$ , corresponding to that of an SSMF, the power-leakage factor distribution  $2\alpha (z)$  should satisfy [6,11]:

$$
2 \alpha (z) = G ^ {2} (z) / \left[ 1 - \int_ {0} ^ {z} G ^ {2} (z) \mathrm {d} z \right]. \tag {2}
$$

Figure 2(a) shows the designed distributions of  $n_i$  and  $l_i$  of the grating coupler. PhCs with a triangular lattice with lattice constant of  $2d_0 / 3$  can be used for the artificial material slots [11,12], and the hole size  $D_{\mathrm{hole}}$  can be determined by the effective index approximation [11]. According to the effective index approximation, the optimized hole size of the designed grating coupler has a feature size  $D_{\mathrm{hole,min}}$  of  $70~\mathrm{nm}$ . Considering that such a dimension is beyond the capability of some fabrication methods such as conventional deep ultraviolet (DUV) lithography, alternative optimum designs restricting  $D_{\mathrm{hole,min}}$  to  $100~\mathrm{nm}$  and  $150~\mathrm{nm}$  are also shown in Fig. 2(a). The CE of the transverse electric (TE) mode is then investigated by a two-dimensional (2D) eigenmode-expansion method (EME) as a function of  $h_d$  with  $h_u$  set to  $1000~\mathrm{nm}$ , as shown in Fig. 2(b). The CE depends periodically on  $h_d$ , and reaches a local maximum at  $h_d = 1600~\mathrm{nm}$ . With  $h_d = 1600~\mathrm{nm}$ , the CE is further calculated by changing  $h_u$ . One can find that the CE is moderately influenced by the value of  $h_u$ , and can reach its maximum when  $h_u = 1000~\mathrm{nm}$ . With  $h_d = 1600~\mathrm{nm}$  and  $h_u = 1000~\mathrm{nm}$ , the CE is then calculated as a function of wavelength for the original design with  $D_{\mathrm{hole,min}} = 70~\mathrm{nm}$ , as well as for the designs with restricted  $D_{\mathrm{hole,min}}$  of  $100~\mathrm{nm}$  and  $150~\mathrm{nm}$ , as shown in Fig. 3. A highest CE of -0.43 dB (corresponding to 91%) is predicted for the original design at  $1560~\mathrm{nm}$ , with a

![](images/530c0573877df20b2ba96c7a7bc90823d5c87ad8398488c6f33b15adc6315d36.jpg)  
Fig. 2. (a) Designed  $l_{i}$  and  $n_i$  distributions of the grating couplers, with  $D_{\mathrm{hole,min}}$  of 70, 100, and 150 nm. Simulated CE as a function of (b) lower cladding thickness with  $h_u = 1000 \mathrm{~nm}$  and (c) upper cladding thickness with  $h_d = 1600 \mathrm{~nm}$ .

![](images/5ffd6fe3e97ab1eaa5302b211f22deb306d8e64b325861eb6cef14de81f84dc0.jpg)  
Fig. 3. Simulated CE as a function of wavelength for designed grating couplers with different feature sizes.

3 dB bandwidth of  $76~\mathrm{nm}$ . In addition, the  $100~\mathrm{nm}$  feature size design shows negligible CE degradation and the  $150~\mathrm{nm}$  design exhibits only  $0.4\mathrm{dB}$  CE degradation, indicating that our design is compatible with most fabrication methods. Considering that the scattering cell length  $l_{i}$  changes along the grating coupler, which is different from the case of uniform grating couplers, it is important to investigate the coupling-angle dependence. As shown in Fig. 3, a  $2^{\circ}$  coupling-angle change results in an  $18~\mathrm{nm}$  peak coupling wavelength shift, which is slightly smaller than previous demonstrations [8]. In addition, the peak CE does not degrade as the coupling angle is changed.

In order to validate our design, the device was fabricated on a commercial SOI sample with top silicon thickness of  $250\mathrm{nm}$  and BOX layer thickness of  $3\mu \mathrm{m}$ . A single step of standard SOI processing, including e-beam lithography and inductively coupled plasma (ICP) etching, was first used to fabricate the grating coupler and silicon nanowire waveguide simultaneously. An  $800\mathrm{nm}$  thick layer of  $\mathrm{SiO}_2$  was then deposited on top of the grating coupler. Considering the surface is not flat after  $\mathrm{SiO}_2$  deposition, another  $800\mathrm{nm}$  borophosphosilicate glass (BPSG) was deposited and annealed at  $950^{\circ}\mathrm{C}$  for 30 minutes in nitrogen, giving a planarity across the grating

![](images/344ee2517321f89473a330c7da66a66c6f57e2d74a1cdd8440ce7029d83f9819.jpg)  
Fig. 4. (a) Scanning electron microscopy (SEM) and (b) optical microscopy images of the fabricated grating coupler. (c) Measured CE for the fabricated coupler with Al mirror with and without  $8\mathrm{nm}$  hole size change as well as for the same grating coupler fabricated on the same type of SOI wafer without Al mirror.

![](images/549bfb4160483aa66097b50b4f639a031bdea2a4bba9a4e89cd54249044f8edc.jpg)  
Fig. 5. Measured CE as a function of wavelength for different coupling angles.

region better than  $100\mathrm{nm}$ . Afterward,  $100\mathrm{nm}$  Al was deposited on top of the BPSG, followed by another  $1\mu \mathrm{m}$ $\mathrm{SiO}_2$  deposition. Then, about  $2\mu \mathrm{m}$  BCB was spun on both the sample and silicon-carrier wafer. The sample was then flip-bonded on the silicon carrier wafer and thermally cured in an oven. The substrate of the chip was then removed by ICP fast etching stopping on the BOX layer. Finally, the BOX layer was thinned to  $1\mu \mathrm{m}$  by buffered hydrofluoric acid (BHF) etching.

Figures 4(a) and 4(b) show details of the fabricated device. In order to test the CE, two identical grating couplers were fabricated, with a  $700\mu \mathrm{m}$  long single-mode straight waveguide introduced in between. The waveguide width was tapered from  $12\mu \mathrm{m}$  for the grating couplers to  $450\mathrm{nm}$  for the single-mode waveguide with  $500~{\mu\mathrm{m}}$  tapering length. The CE was obtained by  $(\eta_0 - \eta_s) / 2$  where  $\eta_0$  is the grating-to-grating transmission and  $\eta_{s}$  is the loss of the single-mode silicon waveguide, with propagation loss of  $2\mathrm{dB / cm}$  measured by the cut-back method. Figure 4(c) shows the measured CE as a function of wavelength for the designed grating coupler with the bonded Al mirror. The CE for the same grating coupler fabricated on the same type of SOI wafer but without Al mirror is also shown. A significant improvement provided by the bonded mirror is confirmed. The tolerance to fabrication error was investigated by changing the size of all the holes. A diameter change of the holes  $\mathrm{dD_{hole}}$  of  $8\mathrm{nm}$  resulted in a peak coupling wavelength shift of only  $23\mathrm{nm}$  without peak CE degradation. Such coupling wavelength shift could be compensated by adjusting the coupling angle. The slight peak coupling wavelength deviation compared to the simulations is believed to be due to fabrication error, e.g., the hole size error and top silicon thickness error of the SOI sample.

The CE of the fabricated grating coupler was further characterized by changing the coupling angle, as shown in Fig. 5. One can find that a  $2^{\circ}$  coupling angle change results in an  $18\mathrm{nm}$  peak coupling wavelength shift, which agrees well with the simulation. In addition, the highest CE of only  $-0.58\mathrm{dB}$  with  $3\mathrm{dB}$  bandwidth of  $71\mathrm{nm}$  was obtained at a coupling angle of  $13^{\circ}$ . The back reflection of the grating coupler was extracted from the contrast of the Fabry-Perot (FP) fringes of the

fiber-to-fiber transmission spectrum, and is lower than  $1.4\%$  at the peak coupling wavelength, which is comparable to previous demonstrations [12-16].

In summary, we have designed and demonstrated a fully etched fiber-to-chip grating coupler using subwavelength PhCs and bonded Al mirror. A record-high CE of  $-0.58$  dB with 3 dB bandwidth of  $71~\mathrm{nm}$  and low back reflection were demonstrated. In the present work, the use of BCB is not compatible with conventional CMOS processes, and it also may influence the thermal performance. However, thermocompression bonding using aluminum [17], which is a CMOS-compatible process, can be used to solve the heat-sinking problem as well as to simplify the fabrication process. In addition, the Al mirror could be introduced during the fabrication of the SOI wafers, which would also simplify the fabrication process.

This work is supported by the Danish Council for Independent Research (DFF-1337-00152 and DFF-1335-00771).

# References

1. D. Taillaert, W. Bogaerts, P. Bienstman, T. F. Krauss, P. Van Daele, I. Moerman, S. Verstuyft, K. De Mesel, and R. Baets, IEEE J. Quantum Electron. 38, 949 (2002).  
2. F. Van Laere, G. Roelkens, M. Ayre, J. Schrauwen, D. Taillaert, D. Van Thourhout, T. F. Krauss, and R. Baets, J. Lightwave Technol. 25, 151 (2007).  
3. Y. Tang, Z. Wang, L. Wosinski, U. Westergren, and S. He, Opt. Lett. 35, 1290 (2010).  
4. X. Chen, C. Li, C. K. Y. Fung, S. M. G. Lo, and H. K. Tsang, IEEE Photon. Technol. Lett. 22, 1156 (2010).  
5. D. Vermeulen, S. Selvaraja, P. Verheyen, G. Lepage, W. Bogaerts, P. Absil, D. Van Thourhout, and G. Roelkens, Opt. Express 18, 18278 (2010).  
6. C. Li, H. Zhang, M. Yu, and G. Q. Lo, Opt. Express 21, 7868 (2013).  
7. L. He, Y. Liu, C. Galland, A. E.-J. Lim, G.-Q. Lo, T. Baehr-Jones, and M. Hochberg, IEEE Photon. Technol. Lett. 25, 1358 (2013).  
8. W. S. Zaoui, A. Kunze, W. Vogel, M. Berroth, J. Butschke, F. Letzkus, and J. Burghartz, Opt. Express 22, 1277 (2014).  
9. Y. Ding, H. Ou, J. Xu, and C. Peucheret, IEEE Photon. Technol. Lett. 25, 648 (2013).  
10. Y. Ding, F. Ye, C. Peucheret, H. Ou, Y. Miyamoto, and T. Morioka, in European Conference and Exhibition on Optical Communication (ECOC, 2014), paper We.1.1.3.  
11. Y. Ding, H. Ou, and C. Peucheret, Opt. Lett. 38, 2732 (2013).  
12. L. Liu, M. Pu, K. Yvind, and J. M. Hvam, Appl. Phys. Lett. 96, 051126 (2010).  
13. R. Halir, P. Cheben, J. Schmid, R. Ma, D. Bedard, S. Janz, D. Xu, A. Densmore, J. Lapointe, and I. Molina-Fernández, Opt. Lett. 35, 3243 (2010).  
14. M. Antelius, K. B. Gylfason, and H. Sohlström, Opt. Express 19, 3592 (2011).  
15. X. Xu, H. Subbaraman, J. Covey, D. Kwong, A. Hosseini, and R. T. Chen, Appl. Phys. Lett. 101, 031109 (2012).  
16. Q. Zhong, V. Veerasubramanian, Y. Wang, W. Shi, D. Patel, S. Ghosh, A. Samani, L. Chrostowski, R. Bojko, and D. V. Plant, Opt. Express 22, 18224 (2014).  
17. H. Lin, J. T. M. Stevenson, A. M. Gundlach, C. C. Dunare, and A. J. Walton, Microelectron. Eng. 85, 1059 (2008).