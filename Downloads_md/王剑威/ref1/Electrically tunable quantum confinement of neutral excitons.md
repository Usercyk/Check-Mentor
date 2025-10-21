# Electrically tunable quantum confinement of neutral excitons

https://doi.org/10.1038/s41586-022-04634-z

Received: 7 July 2021

Accepted: 14 March 2022

Published online: 25 May 2022

Check for updates

Deepankur Thureja $^{1,2}$ , Atac Imamoglu $^{1*}$ , Tomasz Smolénski $^{1}$ , Ivan Amelio $^{1}$ , Alexander Popert $^{1}$ , Thibault Chervy $^{1,6}$ , Xiaobo Lu $^{1,7}$ , Song Liu $^{3}$ , Katayun Barmak $^{4}$ , Kenji Watanabe $^{5}$ , Takashi Taniguchi $^{5}$ , David J. Norris $^{2}$ , Martin Kroner $^{1}$  & Puneet A. Murthy $^{1*}$

Confining particles to distances below their de Broglie wavelength discretizes their motional state. This fundamental effect is observed in many physical systems, ranging from electrons confined in atoms or quantum dots $^{1,2}$  to ultracold atoms trapped in optical tweezers $^{3,4}$ . In solid-state photonics, a long-standing goal has been to achieve fully tunable quantum confinement of optically active electron-hole pairs, known as excitons. To confine excitons, existing approaches mainly rely on material modulation $^{5}$ , which suffers from poor control over the energy and position of trapping potentials. This has severely impeded the engineering of large-scale quantum photonic systems. Here we demonstrate electrically controlled quantum confinement of neutral excitons in 2D semiconductors. By combining gate-defined in-plane electric fields with inherent interactions between excitons and free charges in a lateral p-i-n junction, we achieve exciton confinement below  $10 \mathrm{~nm}$ . Quantization of excitonic motion manifests in the measured optical response as a ladder of discrete voltage-dependent states below the continuum. Furthermore, we observe that our confining potentials lead to a strong modification of the relative wave function of excitons. Our technique provides an experimental route towards creating scalable arrays of identical single-photon sources and has wide-ranging implications for realizing strongly correlated photonic phases $^{6,7}$  and on-chip optical quantum information processors $^{8,9}$ .

Neutral excitons, which are bound electron-hole pairs, are intrinsically more challenging to electrically confine than charged particles. One possible route for exciton confinement involves the dc Stark effect, which ensures that excitons experience an attractive potential around the absolute maximum of an inhomogeneous electric field distribution. However, achieving quantum confinement in such a potential requires that the energy splitting between discrete motional excitonic states  $(\hbar \omega)$  exceeds the exciton line broadening  $\Gamma$ , as well as the characteristic energy of thermal fluctuations  $k_{\mathrm{B}}T$ . For excitons in semiconductor heterostructures at  $T = 4\mathrm{K}$ , this implies  $\hbar \omega \gtrsim 1$  meV. This – in turn – requires a confinement length scale of  $\ell = \sqrt{\hbar / m_{\chi}\omega} \lesssim 10$  nm for exciton mass  $m_{\chi}$  comparable with free electron mass. Engineering electrically tunable confinement potentials at such small length scales is a technical challenge. In addition, unless the exciton binding energy is much larger than  $\hbar \omega$ , the requisite applied fields will lead to fast ionization of excitons, greatly reducing their radiative efficiency.

Previous experiments have mainly approached the problem of electrical confinement by relying on indirect excitons, in which the electron and hole comprising an exciton are spatially separated in different quantum wells. This gives rise to a permanent electric dipole moment, which makes them easier to electrically manipulate, but at the expense of weaker coupling to light. In III-V semiconductor heterostructures

with coupled quantum wells, different potential landscapes have been demonstrated for indirect excitons, such as ramps, lattices and harmonic traps $^{10-15}$ . However, the requirement to suppress exciton ionization in these systems $^{16}$  prevented the observation of quantum confinement. Moreover, the quantum wells typically need to be buried deep within the heterostructure, which limits the electric field gradients that can be applied using lithographically patterned gates outside the structure. Electrical manipulation as well as confinement of spatially indirect excitons at large length scales has also been reported in transition metal dichalcogenide (TMD) heterostructure devices $^{17-21}$ . Nevertheless, tunable confinement and quantization of motional states of direct excitons, which couple strongly to light, has not been demonstrated previously.

In this work, we overcome these challenges and demonstrate an electrically tunable quantum confining potential for spatially direct excitons in a monolayer semiconductor. In achieving this goal, we not only solve a long-standing experimental problem in quantum photonics but show intriguing aspects of quantum-confined excitons unique to our system. In addition to being highly relevant for technological applications, our work highlights that the electrically controlled quantum-confined system is a promising experimental platform for exploring strongly correlated physics of excitons and photons.

$^{1}$ Institute for Quantum Electronics, ETH Zurich, Zurich, Switzerland.  $^{2}$ Optical Materials Engineering Laboratory, Department of Mechanical and Process Engineering, ETH Zurich, Zurich, Switzerland.  $^{3}$ Department of Mechanical Engineering, Columbia University, New York, NY, USA.  $^{4}$ Department of Applied Physics and Applied Mathematics, Columbia University, New York, NY, USA.  $^{5}$ National Institute for Materials Science, Tsukuba, Ibaraki, Japan.  $^{6}$ Present address: NTT Research, Inc., Physics & Informatics (PHI) Laboratories, Sunnyvale, CA, USA.  $^{7}$ Present address: International Center for Quantum Materials, Peking University, Beijing, China.  $^{8}$ e-mail: imamoglu@phys.ethz.ch; murthyp@ethz.ch

![](images/5101dc13f0353f641cf6914556d0e7b63f54a8a6bbf8b6a7d3f03fd34c4cbb88.jpg)

![](images/160d38c631aa28a47aadc82a4c64ec3e0e85456f048d368f6da21ddf2fd513a1.jpg)

![](images/e08736ac01dab6de67e61b5a96edfd2eba468a144ee32e8b25eaf71e4762a6ad.jpg)  
f, Interaction-induced confinement arises from the repulsive interaction between excitons and itinerant charges, which imposes a density-dependent energy cost,  $\Delta E \propto \sigma(x)$ , for excitons entering the doped regions.

![](images/81c9251ba1865c68969467a9ccf57ffc8f4306814d025894400e07ffa5caa3d7.jpg)

![](images/b50be5b514d0d6c86103d768535fde52710a49af06b6ed6834e984a63cb3f0ee.jpg)  
Fig.1| Tunable quantum confinement of excitons. a, Schematic side view of the device consisting of a monolayer TMD semiconductor, such as  $\mathrm{MoSe}_2$ , encapsulated by h-BN, and partially overlapping gates (TG and BG). By applying voltage between TG and BG, we generate inhomogeneous in-plane electric fields along the TG edge (black dashed lines) and obtain a p-i-n charging configuration, in which holes (region II) and electrons (region I) are represented by blue and red circles, respectively. b, Schematic diagram of CB and VB edges in the p-i-n regime. c, The spatial dependence of the in-plane electric field strength  $F_{\mathrm{x}}$  (blue line) and the total charge density  $|\sigma|$  (black dashed line) obtained from electrostatic simulations. d, The total confining

![](images/73db2caea21a6853c83b6054158ffddf322a8f9e39aae3c590eb75d98cd670d0.jpg)  
potential  $V(x)$  (see equation (1)), along with the discrete eigenstates. Exciton confinement stems from two fundamentally distinct effects, namely, field-induced confinement and interaction-induced confinement, which are illustrated in panels e and f, respectively. e, Field-induced confinement originates from the local in-plane electric field  $F_{x}$ , which induces a permanent dipole moment for 2D excitons and causes a dc Stark shift  $\Delta E \propto |F_{\mathrm{x}}|^2$ .

# Confinement scheme

Our experimental scheme to confine excitons is illustrated in Fig. 1. We base our experiments on monolayer TMD heterostructures, as they offer several key advantages over conventional semiconductor platforms, such as III-V heterostructures. The most important one is the strong exciton binding energy  $(E_{\mathrm{B}}$ , around  $200\mathrm{meV}$  (ref. [22]), which renders the excitons more resilient to in-plane electric fields. We consider a device that includes a monolayer TMD semiconductor, such as  $\mathrm{MoSe}_2$ , encapsulated by insulating dielectric spacer layers and two gate electrodes (top gate, TG; bottom gate, BG). Notably the TG and BG have partial spatial overlap as shown in Fig. 1a, which allows to separately define adjacent p-doped and n-doped regions and generate in-plane electric fields along the TG edge. The energies of conduction band (CB) and valence band (VB) edges relative to the Fermi level  $E_{\mathrm{F}}$  in this doping configuration are illustrated in Fig. 1b. In Fig. 1c, we show the spatial dependence of in-plane electric field  $F_{\mathrm{x}}$  (blue line) and total charge density  $|\sigma(x)|$  (black dashed line) in the vicinity of the TG edge, obtained from electrostatic simulations of the device (see Methods and Extended Data Fig. 1).

Two fundamentally distinct effects contribute to quantum confinement of excitons in our structure. The first arises from the strong in-plane electric field  $F_{\mathrm{x}}$ , which polarizes the excitons along  $x$  and lowers their energy owing to the dc Stark shift,  $\Delta E_{\mathrm{S}} = -\frac{1}{2}\alpha |F_{\mathrm{x}}|^2$ , in which  $\alpha$  is the exciton polarizability[23]. Because  $F_{\mathrm{x}}$  vanishes on either side of the insulating region (Fig. 1c), excitons experience an attractive confining potential towards the local maximum in  $|F_{\mathrm{x}}(x)|$ , hence we expect the dipole size to be the largest for excitons confined in the lowest eigenstates, as illustrated in Fig. 1e. In addition to the Stark shift, we describe a new confinement mechanism that stems from the

interaction between neutral excitons and itinerant charges present in the neighbouring p-doped and n-doped regions (Fig. 1f). As neutral excitons generated in the i region enter the n-doped or p-doped regions, they experience a repulsive interaction, which increases their energy proportional to the charge density,  $\Delta E_{\mathrm{P}} \propto \sigma(x)$ . This many-body dressed state can be described as a repulsive polaron[24] and has been previously observed in charge-tunable semiconductor heterostructure devices[25]. In this scenario, a gradient in charge density exerts a force on excitons that pushes them towards the local minimum in charge density[26]. A steep charge density gradient on both sides of the i region therefore acts as a repulsive potential barrier for excitons, which confines them spatially.

The total potential experienced by excitons in the centre-of-mass (COM) frame is a sum of dc Stark shift and repulsive interaction shift contributions:

$$
V (x) = \underbrace {- \frac {1}{2} \alpha | F _ {\mathrm {x}} (x) | ^ {2}} _ {\text {d c S t a r k s h i f t}} + \underbrace {\beta | \sigma (x) |} _ {\text {I n t e r a c t i o n s h i f t}}. \tag {1}
$$

Here the proportionality constant  $\beta$  is an effective exciton-charge coupling constant. We emphasize that the potential in equation (1) provides confinement only for excitons, whereas unbound electrons or holes experience a repulsive potential that accelerates them towards the n-doped and p-doped regions, respectively.

The exciton confinement strength achieved with the potential in equation (1) depends on the geometry of the device and the excitonic properties of the material. In Fig. 1d, we show the overall confining potential  $V(x)$  calculated for a device with 30-nm-thick hexagonal boron nitride (h-BN) spacers. In addition, we assume a BG voltage  $V_{\mathrm{BG}} = 4\mathrm{V}$  and TG voltage  $V_{\mathrm{TG}} = -8\mathrm{V}$ . The simulated potentials for a wider range

![](images/0664392acf138d10c2c64a9c94d8a70b376f275139d138227af90adfe84d185c.jpg)

![](images/5f9b3c3dc979292df38b7fa077aaab9bdb707d6f921b7369ba6f7176a9429d85.jpg)

![](images/f63a6860b5384311e2e43a3aa6b23b9f7b68434f38d910ba4586a296a12aba2a.jpg)  
Fig. 2 | Optical signatures of quantum-confined excitons. a, Optical micrograph of Device 1, in which the white dashed line indicates the monolayer  $\mathrm{MoSe}_2$  flake. TG and BG are the top and bottom gates, respectively. The scale bar denotes  $5\mu \mathrm{m}$ . b, The normalized differential reflectance  $\Delta R / R$  as a function of  $V_{\mathrm{TG}}$ , measured on the TG edge at  $V_{\mathrm{BG}} = 4\mathrm{V}$ . In addition to the typical features associated with the neutral exciton ( $\mathrm{X}_{2\mathrm{D}}$ ) and repulsive polaron branches ( $\mathrm{RP}^+$  and  $\mathrm{RP}^-$ ) from underneath the TG, we observe narrow discrete spectral lines that redshift as a function of  $V_{\mathrm{TG}}$  compared with the exciton or  $\mathrm{RP}^+$  energy at that voltage. c, Spectra at  $V_{\mathrm{TG}} = -3.5\mathrm{V}$  (black),  $-5.5\mathrm{V}$  (green) and  $-6.2\mathrm{V}$  (blue).

![](images/654b7ca1241493259d88af5fa66748d1dce7e75a7d5cff31fddfe09a6353b512.jpg)  
The inset shows the estimated shape of the total potential  $V(x)$  for excitons at the corresponding voltages (see equation (1)). d, Energy of discrete resonances  $(E)$  with respect to the free exciton continuum  $E_{\mathrm{cont}}$ . The continuum energy is the 2D exciton energy in the neutral regime and the repulsive polaron energy in the doped regime. The inset shows the resonance energies obtained from Lorentzian fits of reflectance with respect to the 2D exciton energy. We observe a maximum level spacing of  $\hbar \omega \approx 1.5 \mathrm{meV}$  between the lowest two confined states. This is accompanied by a narrowing of the linewidth from  $\Gamma_{2\mathrm{D}} \approx 2 \mathrm{meV}$  for free excitons to  $\Gamma_{\mathrm{QC}} \approx 300 \mu \mathrm{eV}$  for confined excitons.

of gate voltages are shown in the Extended Data Fig.1. From these calculations, we obtain a level separation between the discrete eigenstates  $\hbar \omega_{\mathrm{x}}\approx 1 - 2\mathrm{meV}$ , which is on the order of the exciton linewidth. We emphasize that, despite the i region being approximately  $60~\mathrm{nm}$  wide, the strong in-plane electric field  $(F_{\mathrm{x,max}}(x)$  around  $40\mathrm{V}\mu \mathrm{m}^{-1})$  and field gradient  $(\partial F_{\mathrm{x}}(x) / \partial x$  around  $10^{3}\mathrm{V}\mu \mathrm{m}^{-2})$  result in tight COM confinement for excitons, with a harmonic oscillator length  $\ell_{\mathrm{x}}$  of around  $6 - 8\mathrm{nm}$ .

# Signatures of quantum confinement

We fabricate two van der Waals heterostructure devices, which we refer to as Device 1 and Device 2. A micrograph of Device 1 is shown in Fig. 2a. Both devices consist of a  $\mathrm{MoSe}_2$  flake sandwiched between h-BN slabs and gated by two electrodes, as illustrated in Fig. 1a. The device parameters and fabrication procedure are detailed in Methods. To investigate the excitonic properties in these devices, we perform optical reflectance and photoluminescence (PL) spectroscopy at a temperature of approximately  $4\mathrm{K}$ .

The modification of excitonic states owing to confinement can be observed in the optical response of the narrow depleted region close to the TG edge. Owing to the diffraction-limited spot size of our optical setup (about  $700\mathrm{nm}$ ), our measurements include the combined optical response of three distinct spatial regions (see Fig. 1a): (I) the electron-doped region away from the TG that is affected only by the BG, (II) the region directly underneath the TG and (III) the narrow region between I and II. The contribution of region I to the total optical response remains unchanged as  $V_{\mathrm{TG}}$  is varied. Therefore, to discern the influence of the TG alone, we measure  $V_{\mathrm{TG}}$ -dependent spectra for fixed values of  $V_{\mathrm{BG}}$  and obtain the normalized differential reflectance according to:

$$
\frac {\Delta R}{R} = \frac {R \left(V _ {\mathrm {T G}}\right) - R \left(V _ {\mathrm {T G}} = 0\right)}{R \left(V _ {\mathrm {T G}} = 0\right)}. \tag {2}
$$

In Fig. 2b, we present  $\Delta R / R$  as a function of  $V_{\mathrm{TG}}$  at fixed  $V_{\mathrm{BG}} = 4\mathrm{~V}$ , which corresponds to an electron density  $\sigma_{\mathrm{n}} = 2\times 10^{12}\mathrm{cm}^{-2}$  in region I. First, we identify the typical doping-dependent optical response from region II directly under the TG. This includes a neutral regime  $(X_{2\mathrm{D}}: -6\mathrm{~V}\lesssim V_{\mathrm{TG}}\lesssim -3\mathrm{~V})$ . As we dope the system with holes or electrons, we observe the density-dependent blue shift of the exciton resonance, which we refer to as the repulsive polaron branch  $(\mathbb{R}\mathbb{P}^{-},\mathbb{R}\mathbb{P}^{+})$ . The charging behaviour of the device is discussed in detail in Methods (see Extended Data Fig. 2).

In addition to the expected optical response, we observe several narrow and discrete spectral lines for  $V_{\mathrm{TG}} \lesssim -4 \mathrm{~V}$ , which emerge below the 2D exciton and repulsive polaron continuum, and redshift with decreasing  $V_{\mathrm{TG}}$ . In Fig. 2c, we show representative reflectance spectra taken at  $V_{\mathrm{TG}} = -3.5 \mathrm{~V}, -5.5 \mathrm{~V}$  and  $-6.2 \mathrm{~V}$ , which highlight the appearance of new states with varying  $V_{\mathrm{TG}}$ . For these voltages, estimates of the corresponding potential  $V(x)$  (equation (1)) are shown in the inset. The resonance centre frequencies of the discrete states, obtained from Lorentzian fits to the reflectance spectra, are shown in the inset of Fig. 2d. We measure an energy separation  $E_2 - E_1$  of around  $1.5 \mathrm{meV}$  between the lowest two resonances at  $V_{\mathrm{TG}} = -8 \mathrm{~V}$ . These observations in Device I are strongly corroborated by optical measurements on Device 2 (see Extended Data Fig. 3). Moreover, signatures of confinement are also observed in the n-i-p regime, in which region I is hole-doped and region II is electron-doped, as shown in Extended Data Fig. 4.

The emergence of discrete lines from the 2D continuum is an unambiguous signature of quantization of the COM motion of excitons

![](images/66bc97dbf9d4062a1c5d6901ea262e93fddc72c348e14e86812ccc4eae8e6cac.jpg)

![](images/83a82779a162a1baeb5b65e280566041794e98b73161953c94679e1f0217af9b.jpg)

![](images/b5d6a51e8deb3a75c473bfdd0617d0c0648e9041b21f67610636814e7cdad0e0.jpg)

![](images/5a167c68bf30ab42fec57184bfc815b46e0d3c9641ae597542fdc421f427cab9.jpg)  
Fig. 3|1D confinement. a, b, Position-dependent spectra as the diffraction-limited optical spot is scanned across the TG edge in Device 1 and Device 2. In Device 1, we measure PL as we scan the optical spot across the two edges of the TG, leading to the discrete states appearing twice. In Device 2, we show the derivative of the reflection contrast as we scan across a single edge. c, d, PL spectra as a function of linear polarization angle in Device 1 and Device 2, respectively. e, The polarization splitting  $\delta$  increases with decreasing  $V_{\mathrm{TG}}$ ,

![](images/53c42d983b5dce0696ebc873269b27380247dbcee5a570da817f560beac80f9d.jpg)  
corresponding to tighter confinement. The shaded blue area represents fitting errors. f, Power dependence of normalized PL emission intensity from quantum-confined 1D excitons  $(I_{\mathrm{QC}})$  relative to emission from free 2D excitons  $(I_{2\mathrm{D}})$ . The shaded grey area represents fitting errors.  $I_{2\mathrm{D}}$  scales linearly with power (blue points), whereas  $I_{\mathrm{QC}}$  exhibits sublinear behaviour (red points), as shown in the inset. The PL intensities for  $\mathrm{X}_{2\mathrm{D}}$  and  $\mathrm{X}_{\mathrm{QC}}$  are normalized by their corresponding values at the lowest power.

![](images/bc899eb8233c8556ef982bed9be61f6aeb16db29ab560ebba1191dd0d6514afc.jpg)

resulting from strong confinement. Henceforth, we refer to the series of confined exciton states as  $\mathrm{X_{QC}}$ . The level separations observed in the experiment are similar to those obtained from the electrostatic simulations of the device. Further evidence for strong confinement of excitons is provided by the notable reduction of the linewidth of the lowest energy resonance  $\mathrm{X_{QC}}$  compared with the free 1s exciton  $\mathrm{X}_{2\mathrm{D}}$ . Whereas the  $\mathrm{X}_{2\mathrm{D}}$  linewidth is typically  $\Gamma_{2\mathrm{D}}\approx 2\mathrm{meV}$ ,  $\mathrm{X_{QC}}$  shows a linewidth  $\Gamma_{\mathrm{QC}}\approx 300~\mu \mathrm{eV}$  (see Methods and Extended Data Fig. 5 for details of the spectral analysis procedure). Such linewidth narrowing is qualitatively expected to stem from three factors: (1) lower inhomogeneous broadening, as exciton COM motion is restricted to a smaller area owing to confinement; (2) reduction of radiative decay of  $\mathrm{X_{QC}}$  as compared with their free 2D counterparts according to the ratio  $\ell_x / \lambda_{\mathrm{photon}}$ , in which  $\ell_{x}$  is the harmonic oscillator length along  $x$  and  $\lambda_{\mathrm{photon}}$  is the photon wavelength; (3) the reduced electron-hole wave function overlap originating from the electric dipole moment induced by the in-plane electric field.

In the voltage regime  $-6\mathrm{V} < V_{\mathrm{TG}} < -4\mathrm{V}$ , which corresponds to the i-i-n charging configuration, the red shift of the narrow resonances with decreasing  $V_{\mathrm{TG}}$  arises mainly from the field-induced confinement (Fig. 1e) mechanism. Here the dc Stark shift lowers the energy below the continuum given by the 2D exciton energy  $E_{\mathrm{x,2D}}$ . In the p-i-n regime ( $V_{\mathrm{TG}} < -6\mathrm{V}$ ), as region II becomes hole-doped, we observe further quantized modes with energy higher than the  $E_{\mathrm{x,2D}}$  that split off from the repulsive polaron branch  $\mathrm{RP^{+}}$  (inset of Fig. 2d). In this regime, the confinement potential is the sum of the field-induced and interaction-induced contributions. Therefore, the free-particle continuum is no longer the 2D exciton state but the blueshifted repulsive polaron  $(\mathrm{RP^{+}})$  in region II. In other words, to escape the confinement, an exciton in the lowest state must pay not only the dc Stark energy shift but a further repulsive polaron energy,  $E = \beta \cdot \sigma_{\mathrm{max}}$ , in which  $\sigma_{\mathrm{max}}$  denotes the maximum charge density (see Methods and Extended Data Fig. 1). The energy of confined resonances with respect to the continuum energy  $(E_{\mathrm{cont}})$  at each

$V_{\mathrm{TG}}$  is shown in Fig. 2d. This clearly demonstrates the successive emergence of discrete states below the free-particle continuum as the potential is made deeper.

# 1D edge confinement

The strong in-plane confinement perpendicular to the TG edge implies that exciton confinement in our system is effectively 1D in nature. In Fig. 3a, b, we show the position-dependent optical spectra of confined exciton states in Device 1 (PL) and Device 2 (derivative of reflection contrast), respectively. These measurements are performed by scanning the optical spot across the sample using nanopositioners, while keeping  $V_{\mathrm{BG}}$  and  $V_{\mathrm{TG}}$  fixed. In Device 1, the TG consists of two edges separated by roughly  $1\mu \mathrm{m}$  (see inset of Fig. 3a) and hence the discrete states appear at two spatial locations, while vanishing in the intermediate region. In Device 2, because the graphene TG has a single edge (inset of Fig. 3b), the  $\mathrm{X}_{\mathrm{QC}}$  states appear once as we scan across the edge and vanish on either side.

To show the effect of such an anisotropic potential on the COM motion of excitons, we turn our attention to the polarization properties of emission from the confined states. Excitons in 1D semiconductor nanowires have been previously reported to emit photons that are linearly polarized along the wire axis $^{27-31}$ . Linearly polarized emission originates from long-range electron-hole exchange interaction, which couples the valley degrees of freedom and the COM motion of excitons $^{32,33}$ . For finite exciton COM momenta, the valley-COM coupling leads to an energy splitting between longitudinal and transverse electromagnetic modes. Introducing spatial anisotropy, for instance in the form of a 1D confinement potential, breaks the rotational symmetry of the system, thus opening a gap between orthogonal linear polarization states at momentum  $K = 0$ . The magnitude of the  $x-y$  polarization splitting  $\delta$  depends on both the COM  $K$ -space wave function  $\psi_{\mathrm{COM}}(K)$  and the relative wave function  $|\psi_{\mathrm{rel}}(r = 0)|^2$  according to  $\delta \propto |\psi_{\mathrm{rel}}(r = 0)|^2\int \psi_{\mathrm{COM}}^2 (K)|K|\mathrm{d}K$  (refs. 30,32,33).

![](images/43b9113153c189bcf23cebb74b400b2a681866fb816d05090267b26422d6b4af.jpg)  
Fig. 4 | The internal structure of quantum-confined excitons. Reflectance spectra as a function of magnetic fields  $(B)$  shown for 2D excitons (a) and confined excitons (b) in Device 2. The experimental data points are indicated with circles and fits to the spectra are shown by solid lines. c, Evolution of  $E^{+}$  and  $E^{-}$  as a function of  $B$  for  $\mathrm{X}_{2\mathrm{D}}$  (black closed squares and blue open squares) and  $\mathrm{X}_{\mathrm{QC}}$  (black closed circles and blue open circles). d, The Zeeman splitting  $\Delta E_{z} = E^{+} - E^{-}$  scales linearly with  $B$  for  $\mathrm{X}_{2\mathrm{D}}$  (black open squares), whereas for  $\mathrm{X}_{\mathrm{QC}}$ , polarization splitting is

![](images/1adc288046acdf7ae2bf178f0fcbee60d5958c77286014c3745c23370e85c62f.jpg)  
non-zero at  $B = 0$  T and asymptotically approaches linear scaling for large  $B$  (purple closed circles). e, The average energy  $\overline{E} = (E^{+} + E^{-}) / 2$  for  $X_{2D}$  and  $X_{QC}$  at different values of  $V_{\mathrm{TG}}$ . The 2D exciton shows no measurable diamagnetic shift, even at 16 T (black open squares), consistent with the small Bohr radius. On the other hand, the confined dipolar excitons exhibit a sizeable shift, which also increases with decreasing  $V_{\mathrm{TG}}$ . The uncertainties in energies  $(E^{+}$  and  $E^{-}$  are  $\lesssim 15 \mu \mathrm{eV}$ . All energies in c-e are plotted with respect to the average energy  $\overline{E} (B = 0$  T).

![](images/1cb8f17dd03918c30d6ef25d4152c5781737497497f068fd61d08dd223eabea1.jpg)

![](images/da13719807b6ac526ac208ff38ed4cff08b101ee3e18c65c2adab820ed3ea619.jpg)

![](images/03d1690483a72e09c98a91b48c09f744b54f9cd778e94e7835edaa80baf9ccc0.jpg)

We measure linear polarization-resolved PL spectra of quantum confined excitons in Device 1 and 2 (see Fig. 3). In Device 1 (Fig. 3c), we find all discrete states to be linearly polarized parallel to the TG edge (that is,  $y$ -polarized). On the other hand, in Device 2 (Fig. 3d), we observe a polarization doublet comprising both parallel ( $y$ -polarized) and perpendicular ( $x$ -polarized) components with an energy splitting of  $\delta = E_{\parallel} - E_{\perp} \approx 1$  meV. The discrepancy between the two devices can be explained by the thicker h-BN spacers in Device 2 compared with Device 1, which consequently leads to weaker confinement in the former. In Device 1, the confinement is strong enough that  $x - y$  polarization splitting exceeds the confinement energy, whereas the weaker confinement in Device 2 allows to observe both polarization states and their relative splitting  $\delta$ . The dependence of polarization splitting on COM confinement can be seen clearly in Fig. 3e, in which we observe that  $\delta$  increases with decreasing  $V_{\mathrm{TG}}$ , which corresponds to stronger confinement. Further analysis of the polarization properties of the device is presented in Methods and Extended Data Figs. 6, 7.

Further confirmation of strong COM confinement is provided by comparing the excitation power dependence of PL emission of the  $\mathrm{X}_{2\mathrm{D}}$  and  $\mathrm{X}_{\mathrm{QC}}$  states. In Fig. 3f, we show the ratio  $I_{\mathrm{QC}} / I_{2\mathrm{D}}$  of the normalized PL intensity of the  $\mathrm{X}_{\mathrm{QC}}$  and  $\mathrm{X}_{2\mathrm{D}}$  states. Whereas at low powers  $I_{\mathrm{QC}} / I_{2\mathrm{D}}$  is relatively insensitive to power, the ratio decreases sharply in the high-power regime  $>0.5~\mu \mathrm{W}$ . The power dependence of the normalized PL emission for the two states is shown in the inset. As expected for free 2D excitons,  $I_{2\mathrm{D}}$  scales linearly with increasing power (blue points). On the other

hand, the PL emission from quantum-confined 1D excitons  $\mathrm{X_{QC}}$  grows sublinearly (red points) with power. Such saturation behaviour arises in confined systems owing to repulsive exciton-exciton interactions, which prohibit high-density occupation of excitons within the optical spot. More details of the excitation power dependence measurements can be found in Methods and Extended Data Fig. 8.

# Relative exciton wave function

The presence of strong inhomogeneous in-plane electric fields influences not only the COM motion but also the relative wave function of the confined exciton. To shed light on the modification of the internal structure of the  $\mathrm{X_{QC}}$  states, we perform circular-polarization-resolved measurements with an external out-of-plane magnetic field  $B$  on Device 2 (Fig. 4). In Fig. 4a, b, we show the measured spectra at different  $B$ -fields, from  $B = 0$  T to  $B = 16$  T, for the free 1s excitons  $\mathrm{X_{2D}}$  and confined excitons  $\mathrm{X_{QC}}$ , respectively. The  $\mathrm{X_{QC}}$  spectra are measured for fixed  $V_{\mathrm{BG}} = 1$  V and  $V_{\mathrm{TG}} = -7.5$  V. For both  $\mathrm{X_{2D}}$  and  $\mathrm{X_{QC}}$  states, we observe a splitting of spectral lines into two orthogonally polarized states. The corresponding energies,  $E^{+}$ and  $E^{-}$ , are plotted as a function of  $B$  in Fig. 4c. For  $\mathrm{X_{QC}}$ , we focus on the  $B$ -dependent behaviour of the lowest-energy confined state (denoted with black arrows in Fig. 4b). The Zeeman splitting  $E^{+} - E^{-}$ is shown in Fig. 4d. The 2D exciton shows the expected linear-in- $B$  splitting with perfect valley degeneracy at  $B = 0$  T. The confined excitons exhibit a finite splitting  $\delta$  of approximately

1 meV at  $B = 0$  T and approach linear behaviour at high  $B$ -fields. Details of the magnetic field measurements are presented in Methods (see Extended Data Fig. 9).

Information on the relative wave function of excitons is encoded in the diamagnetic energy shifts, which can be extracted from the average energy  $\bar{E} = (E^{+} + E^{-}) / 2$  of the two polarization states. For the 1s exciton, the root mean square size  $\langle r^2\rangle$  is related to the diamagnetic shift according to  $E_{\mathrm{dia}} = e^2\langle r^2\rangle B^2 /8m_{\mathrm{r}}$  , in which  $m_{\mathrm{r}} = m_{\mathrm{n}}^{*}m_{\mathrm{p}}^{*} / (m_{\mathrm{n}}^{*} + m_{\mathrm{p}}^{*})$  is the reduced mass. In Fig. 4e, we show  $\bar{E} = (E^{+} + E^{-}) / 2$  as a function of  $B$  , measured for both  $\mathrm{X}_{2\mathrm{D}}$  (open black squares) and  $\mathrm{X}_{\mathrm{QC}}$  states. The energy shifts of  $\mathrm{X}_{\mathrm{QC}}$  are shown for four  $V_{\mathrm{TG}}$  values:  $V_{\mathrm{TG}} = -7.5\mathrm{V}, - 8\mathrm{V}, - 9\mathrm{V}$  and  $-10\mathrm{V}$  .As 2D excitons (in the 1s manifold) in TMD monolayers are strongly bound and have small Bohr radii  $(a_{\mathrm{B}}$  around  $1\mathrm{nm}$  for  $\mathrm{MoSe}_2$  (ref. 22)), we do not observe a shift in  $\bar{E}$  for  $\mathrm{X}_{2\mathrm{D}}$  beyond our experimental uncertainties. By contrast, we observe strikingly enhanced shift of  $\bar{E}$  for  $\mathrm{X}_{\mathrm{QC}}$  states with increasing  $B$  -field. Moreover, we find a clear dependence of  $\bar{E}$  on  $V_{\mathrm{TG}}$  that is, a stronger in-plane electric field corresponds to larger blue shift of the average energy.

These observations are surprising for several reasons. First, we note that, in conventional quantum-confined systems such as cleaved-edge-overgrowth quantum wires or self-assembled quantum dots $^{34}$ , the confinement has the effect of increasing the electron-hole overlap and hence reducing the diamagnetic shift compared with bulk 2D systems. This is in strong contrast to our scenario, in which the confined states show much larger energy shifts than  $\mathrm{X}_{2\mathrm{D}}$ . Furthermore, the fact that the absolute energy of  $\mathrm{X}_{\mathrm{QC}}$  is only slightly redshifted from  $\mathrm{X}_{2\mathrm{D}}$  by a few meV suggests that confined excitons have comparable binding energies as their free 2D counterparts. Furthermore, the high reflection contrast of  $\mathrm{X}_{\mathrm{QC}}$  is also consistent with an exciton with a small Bohr radius. On the other hand, the substantially larger  $\overline{E}$  of  $\mathrm{X}_{\mathrm{QC}}$  indicates an enhanced spatial extent. For example, in the case of a free 2D exciton, an energy shift  $\overline{E}$  of around  $600~\mu \mathrm{eV}$  at  $B = 16\mathrm{T}$  would correspond to a root mean square size  $\sqrt{\langle r^2\rangle}$  of about  $6\mathrm{nm}$ , which would correspondingly - have a much smaller oscillator strength and a different energy from the observed values. Taken together, our measurements indicate that the inhomogeneous in-plane  $E$ -field gives rise to a non-trivial, spatially extended relative wave function of  $\mathrm{X}_{\mathrm{QC}}$  that is not captured by a simple hydrogenic picture of exciton states.

To understand the mechanism underlying the large  $B$ -dependent shift of  $\overline{E}$  of  $\mathrm{X_{QC}}$  states, we perform exact diagonalization calculations of the electron-hole Hamiltonian in the relative frame, including an external in-plane electric and out-of-plane magnetic field (see Methods and Extended Data Fig. 10). We find that, at strong enough in-plane electric fields, the electron (or hole) wave function in the relative frame of the exciton leaks out of the attractive Coulomb potential and hybridizes with the quasi-continuum states. Furthermore, even though only a small fraction of the wave function leaks out, the state exhibits a substantial blue shift at finite  $B$ -fields, on the same order of magnitude as observed in our experiment. These shifts show a clear dependence on the in-plane electric field, in qualitative agreement with the measurements. Our observations and calculations therefore suggest that the quantum-confined exciton states have a modified internal structure compared with 2D excitons, or even in-plane dipolar excitons at weak fields. This feature could potentially have new applications, for instance towards enhancing exciton-exciton interactions<sup>35</sup> and realizing effective gauge potentials<sup>36,37</sup>.

# Discussion

Our method of tunable quantum confinement of excitons provides several crucial design advantages over material modulation approaches, such as band-gap engineering, moiré potentials and strain engineering. Tailor-made potentials can be deterministically positioned without the need for nanoscopic lithographic patterning (only the overlap of gate edges is needed). The confined exciton energy can be electrically tuned,

which can correct for spatial disorder and enable creation of several identical emitters. Finally, quantum confinement of in-plane direct excitons is achieved, as opposed to layer-indirect excitons, which can facilitate strong coupling to light.

By using proper design of electrodes, our technique can also straightforwardly offer arbitrary potential landscapes for excitons. In particular, lower-dimensional quantum-confined structures such as quantum dots or quantum rings may be realized. Such tunable quantum-confined systems are expected to exhibit strongly enhanced exciton-exciton interactions $^{38-40}$ , while allowing for hybridization with an optical cavity or waveguide mode $^{35,41,42}$ . This could therefore emerge as a building block of a strongly interacting many-body photonic system $^{6,7}$  and enable the investigation of correlated phases such as a 1D Tonks-Girardeau gas $^{43,44}$  or a bosonic Mott insulator of exciton-polaritons $^{45,46}$ .

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-022-04634-z.

1. Hawrylak, P. & Korkusinski, M. in Single Quantum Dots: Fundamentals, Applications, and New Concepts (ed. Michler, P.) 25-92 (Springer, 2003).  
2. Harrison, P. & Valavanis, A. Quantum Wells, Wires and Dots: Theoretical and Computational Physics of Semiconductor Nanostructures 241-265 (Wiley, 2016).  
3. Serwane, F. et al. Deterministic preparation of a tunable few-fermion system. Science 332, 336-338 (2011).  
4. Kaufman, A. M., Lester, B. J. & Regal, C. A. Cooling a single atom in an optical tweezer to its quantum ground state. Phys. Rev. X 2, 041014 (2012).  
5. Davies, J. H. The Physics of Low-dimensional Semiconductors 118-129 (Cambridge Univ. Press, 1997).  
6. Carusotto, I. & Ciuti, C. Quantum fluids of light. Rev. Mod. Phys. 85, 299-366 (2013).  
7. Noh, C. & Angelakis, D. G. Quantum simulations and many-body physics with light. Rep. Prog. Phys. 80, 016401 (2016).  
8. O'Brien, J. L., Furusawa, A. & Vučković, J. Photonic quantum technologies. Nat. Photonics 3, 687-695 (2009).  
9. Aspuru-Guzik, A. & Walther, P. Photonic quantum simulators. Nat. Phys. 8, 285-291 (2012).  
10. Hagn, M., Zrenner, A., Böhm, G. & Weimann, G. Electric-field-induced exciton transport in coupled quantum well structures. Appl. Phys. Lett. 67, 232 (1995).  
11. Rapaport, R. et al. Electrostatic traps for dipolar excitons. Phys. Rev. B 72, 075428 (2005).  
12. Gartner, A., Prechtel, L., Schuh, D., Holleitner, A. W. & Kotthaus, J. P. Micropatterned electrostatic traps for indirect excitons in coupled GaAs quantum wells. Phys. Rev. B 76, 085304 (2007).  
13. Vogele, X. P., Schuh, D., Wegscheider, W., Kotthaus, J. P. & Holleitner, A. W. Density enhanced diffusion of dipolar excitons within a one-dimensional channel. Phys. Rev. Lett. 103, 126402 (2009).  
14. Schinner, G. J. et al. Confinement and interaction of single indirect excitons in a voltage-controlled trap formed inside double InGaAs quantum wells. Phys. Rev. Lett. 110, 127403 (2013).  
15. Butov, L. V. Excitonic devices. Superlattices Microstruct. 108, 2-26 (2017).  
16. Hammack, A. T. et al. Excitons in electrostatic traps. J. Appl. Phys. 99, 066104 (2006).  
17. Unuchek, D. et al. Room-temperature electrical control of exciton flux in a van der Waals heterostructure. Nature 560, 340-344 (2018).  
18. Wang, G. et al. Colloquium: Excitons in atomically thin transition metal dichalcogenides. Rev. Mod. Phys. 90, 021001 (2018).  
19. Liu, Y. et al. Electrically controllable router of interlayer excitons. Sci. Adv. 6, 1830 (2020).  
20. Jauregui, L. A. et al. Electrical control of interlayer exciton dynamics in atomically thin heterostructures. Science 366, 870-875 (2019).  
21. Shanks, D. N. et al. Nanoscale trapping of interlayer excitons in a 2D semiconductor heterostructure. Nano Lett. 21, 5641-5647 (2021).  
22. Goryca, M. et al. Revealing exciton masses and dielectric properties of monolayer semiconductors with high magnetic fields. Nat. Commun. 10, 4172 (2019).  
23. Cavalcante, L. S., Da Costa, D. R., Farias, G. A., Reichman, D. R. & Chaves, A. Stark shift of excitons and trions in two-dimensional materials. Phys. Rev. B 98, 245309 (2018).  
24. Efimkin, D. K. & MacDonald, A. H. Many-body theory of trion absorption features in two-dimensional semiconductors. Phys. Rev. B 95, 035417 (2017).  
25. Sidler, M. et al. Fermi polaron-polaritons in charge-tunable atomically thin semiconductors. Nat. Phys. 13, 255-261 (2017).  
26. Chervy, T. et al. Accelerating polaritons with external electric and magnetic fields. Phys. Rev. 10, 011040 (2020).  
27. Wang, J. Highly polarized photoluminescence and photodetection from single indium phosphide nanowires. Science 293, 1455-1457 (2001).  
28. Akiyama, H., Someya, T. & Sakaki, H. Optical anisotropy in 5-nm-scale T-shaped quantum wires fabricated by the cleaved-edge overgrowth method. Phys. Rev. B 53, 4229-4232 (1996).

# Article

29. Lefebvre, J., Fraser, J. M., Finnie, P. & Homma, Y. Photoluminescence from an individual single-walled carbon nanotube. Phys. Rev. B 69, 075403 (2004).  
30. Bai, Y. et al. Excitons in strain-induced one-dimensional moiré potentials at transition metal dichalcogenide heterojunctions. Nat. Mater. 19, 1068-1073 (2020).  
31. Wang, Q. et al. Highly polarized single photons from strain-induced quasi-1D localized excitons in  $\mathrm{WSe}_2$ . Nano Lett. 21, 7175-7182 (2021).  
32. Glazov, M. M. et al. Spin and valley dynamics of excitons in transition metal dichalcogenide monolayers. Phys. Status Solidi B 252, 2349-2362 (2015).  
33. Yu, H., Cui, X., Xu, X. & Yao, W. Valley excitons in two-dimensional semiconductors. Natl Sci. Rev. 2, 57-70 (2015).  
34. Nagamune, Y. et al. Photoluminescence spectra and anisotropic energy shift of GaAs quantum wires in high magnetic fields. Phys. Rev. Lett. 69, 2963-2966 (1992).  
35. Togan, E., Lim, H.-T., Faelt, S., Wegscheider, W. & Imamoglu, A. Enhanced interactions between dipolar polaritons. Phys. Rev. Lett. 121, 227402 (2018).  
36. Lim, H.-T., Togan, E., Kroner, M., Miguel-Sanchez, J. & Imamoglu, A. Electrically tunable artificial gauge potential for polaritons. Nat. Commun. 8, 14540 (2017).  
37. Chestnov, I. Y., Arakelian, S. M. & Kavokin, A. V. Giant synthetic gauge field for spinless microcavity polaritons in crossed electric and magnetic fields. New J. Phys. 23, 023024 (2021).  
38. Li, W., Lu, X., Dubey, S., Devenica, L. & Srivastava, A. Dipolar interactions between localized interlayer excitons in van der Waals heterostructures. Nat. Mater. 19, 624-629 (2020).

39. Kremser, M. et al. Discrete interactions between a few interlayer excitons trapped at a  $\mathrm{MoSe}_2$ - $\mathrm{WSe}_2$  heterointerface. NPJ 2D Mater. Appl. 4, 8 (2020).  
40. Baek, H. et al. Highly energy-tunable quantum light from moiré-trapped excitons. Sci. Adv. 6, eaba8526 (2020).  
41. Rosenberg, I. et al. Strongly interacting dipolar-polaritons. Sci. Adv. 4, eaat8880 (2018).  
42. Lodahl, P., Mahmoodian, S. & Stobbe, S. Interfacing single photons and single quantum dots with photonic nanostructures. Rev. Mod. Phys. 87, 347-400 (2015).  
43. Carusotto, I. et al. Fermionized photons in an array of driven dissipative nonlinear cavities. Phys. Rev. Lett. 103, 033601 (2009).  
44. Oldziejewski, R., Chiocchetta, A., Knörzer, J. & Schmidt, R. Excitonic Tonks-Girardeau and charge-density wave phases in monolayer semiconductors. Preprint at https://arxiv.org/abs/2106.07290 (2021).  
45. Hartmann, M. J., Brandao, F. G. & Plenio, M. B. Strongly interacting polaritons in coupled arrays of cavities. Nat. Phys. 2, 849-855 (2006).  
46. Greentree, A. D., Tahan, C., Cole, J. H. & Hollenberg, L. C. Quantum phase transitions of light. Nat. Phys. 2, 856-861 (2006).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2022

# Methods

# Device fabrication and experimental setup

All  $\mathrm{MoSe}_2$ , h-BN and graphene flakes used to assemble the devices presented in the main text are obtained through mechanical exfoliation of bulk crystals. The flakes are stacked into a heterostructure in an inert Ar atmosphere inside a glovebox using a standard dry polymer transfer technique[47]. For Device 1, the  $\mathrm{MoSe}_2$  monolayer is encapsulated using approximately 30-nm-thick h-BN and deposited on a prepatterned Ti/Au (3 nm/10 nm) BG. Pd/Au (20 nm/30 nm) contacts to the  $\mathrm{MoSe}_2$  layer are embedded in the top h-BN layer and prepared using the via-contacting method[48,49]. Subsequently, a 200-nm-wide split TG electrode featuring a 100-nm gap is formed by evaporating Ti/Au (3 nm/10 nm). This renders the TG optically transparent and therefore allows to investigate the optical properties of the monolayer underneath, while the local charge density is being altered. Metal electrodes to all contacts and both gates are formed with Ti/Au (5 nm/85 nm). Device 2 has a similar architecture as Device 1. However, all gate electrodes and the contact to the  $\mathrm{MoSe}_2$  layer were made using few-layer graphene. Furthermore, the top/bottom h-BN spacer layers were chosen to be thicker (40 nm and 54 nm, respectively).

We perform our optical experiments in a confocal microscope setup. The sample is mounted on  $x - y - z$  piezo-electric stages located inside a stainless steel tube, which is immersed in a liquid helium bath cryostat. The steel tube is filled with 20 mbar helium exchange gas to maintain a sample temperature of about  $4.2\mathrm{K}$ . Free-space optical access to the sample is enabled through a glass window on top of the tube. White-light reflectance and PL is measured using a broadband light-emitting diode centred at  $760\mathrm{nm}$  and a single-mode Ti:sapphire laser tuned to  $720\mathrm{nm}$  as the excitation source, respectively. The light from the source is focused to a diffraction-limited spot through a high-numerical-aperture (0.68) lens. The light reflected/emitted from the sample is then collected using the same lens, separated from the incident light by a beam splitter, coupled into a single-mode fibre and imaged on a spectrometer equipped with a liquid-nitrogen-cooled charge-coupled device. For white-light measurements an excitation power of a few tens of nW and for PL a few  $\mu \mathrm{W}$  is maintained. The polarization-resolved PL measurements are carried out with an angle-scanning polarizer placed in the emission path.

# Electrostatic simulation of TMD heterostructure devices

In this section, we discuss the finite-element calculations of our devices, which provide us with quantitative information of the in-plane fields, charge densities and the corresponding confinement potentials. These computations are performed using the Electrostatics package in COM-SOL. For all our simulations, we assume temperature  $T = 0$  K. We use the Thomas-Fermi approximation and model the  $\mathrm{MoSe}_2$  monolayer as a single sheet of charge with density,

$$
\sigma (x) = \sigma_ {\mathrm {n}} (x) + \sigma_ {\mathrm {p}} (x) \tag {3}
$$

in which  $\sigma_{\mathrm{n}}$  and  $\sigma_{\mathrm{p}}$  are the electron and hole charge densities, respectively, which are - in turn - given by,

$$
\begin{array}{l} \sigma_ {\mathrm {n}} (x) = - e \int_ {E _ {\mathrm {C}} (V (x))} ^ {E _ {\mathrm {F}}} \mathcal {D} (E) \mathrm {d} E, \quad E _ {\mathrm {F}} > E _ {\mathrm {C}} (V (x)) \tag {4} \\ = - e \mathcal {D} (E) \left(E _ {\mathrm {F}} - E _ {\mathrm {C}}\right), \\ \end{array}
$$

$$
\begin{array}{l} \sigma_ {\mathrm {p}} (x) = e \int_ {E _ {\mathrm {F}}} ^ {E _ {\mathrm {V}} (V (x))} \mathcal {D} (E) \mathrm {d} E, \quad E _ {\mathrm {F}} <   E _ {\mathrm {V}} (V (x)) \tag {5} \\ = e \mathcal {D} (E) \left(E _ {\mathrm {V}} - E _ {\mathrm {F}}\right). \\ \end{array}
$$

Here  $\mathcal{D}(E) = g_{\mathrm{s}}g_{\mathrm{v}}m^{*} / 2\pi \hbar^{2}$  is the 2D density of states for electrons and holes in the semiconductor, in which  $g_{\mathrm{s}} = 1$  is the spin degeneracy

and  $g_{\mathrm{V}} = 2$  is the valley degeneracy.  $E_{\mathrm{C}}$  and  $E_{\mathrm{V}}$  are the conduction and valence band edge energies, respectively, which depend on the local electrostatic potential.  $E_{\mathrm{F}}$  is the Fermi level determined by the alignment of the contact work function with respect to the band edges.

The simulated device geometry is depicted in Fig. 1a. The sheet of charge is encapsulated by 30-nm-thick h-BN slabs and contacted by ohmic electrodes. Furthermore, we include two gates with partial overlap. The BG is kept at a fixed bias of  $4\mathrm{V}$  and ensures a global electron doping throughout the semiconductor. The voltage on the TG is varied from  $0\mathrm{V}$  to  $-10\mathrm{V}$  in our simulations. The material parameters assumed for this calculation are as follows:  $\mathrm{MoSe}_2$  bandgap  $E_{\mathrm{b}} = 1.85\mathrm{eV}$ , Fermi level offset relative to the valence band edge at zero potential  $E_{\mathrm{F}} - E_{\mathrm{V}}(V = 0) = 0.99\mathrm{eV}$  (ref. [50]), electron effective mass  $m_{\mathrm{n}}^{*} = 0.7m_{\mathrm{e}}$  (ref. [51]), hole effective mass  $m_{\mathrm{p}}^{*} = 0.6m_{\mathrm{e}}$  (refs. [22,52]), out-of-plane dielectric constant  $\varepsilon_{\parallel} = 3.76$  and in-plane dielectric constant  $\varepsilon_{\parallel \parallel} = 6.93$  for h-BN[53].

In this manner, we obtain the spatial charge density and in-plane electric field distribution for varying TG voltages  $V_{\mathrm{TG}}$ , which are depicted in the top panel of each subplot in Extended Data Fig. 1. The BG extends over the entire plotted range of the position from  $-80 \mathrm{~nm}$  to  $80 \mathrm{~nm}$ , whereas the TG only ranges from  $-80 \mathrm{~nm}$  to  $0 \mathrm{~nm}$ , with the edge located at  $x = 0$ . We can identify three distinct regimes as we vary  $V_{\mathrm{TG}}$ , which we identify according to the doping state in regions I, II and III. For  $V_{\mathrm{TG}} > -4 \mathrm{~V}$ , we are in the n-n-n regime, in which all three regions are n-doped but the electron density varies spatially, as shown in Extended Data Fig. 1a, b. As we decrease  $V_{\mathrm{TG}}$  further, we deplete regions II and III completely and hence we are in the i-i-n regime, which is accompanied by a large increase in magnitude of the in-plane electric field  $|F_{\mathrm{x}}|$  (Extended Data Fig. 1c, d). Although the maximum of the field distribution is located close to the TG edge, owing to the large lateral extent of the neutral region, the in-plane field persists even under the TG and exhibits a spatial asymmetry. The i-i-n regime persists until the onset of hole doping in region II, which occurs in our simulations (and experiments) at  $V_{\mathrm{TG}} < -6 \mathrm{~V}$  (see Extended Data Fig. 1e, f). As hole doping starts, only a narrow, roughly 60-nm-wide neutral region remains, located at the edge of the TG and flanked by a steep increase in charge density. This is the p-i-n regime. As a consequence, the in-plane field distribution also becomes concentrated in this narrow region owing to screening in the neighbouring charged areas. Lowering  $V_{\mathrm{TG}}$  further pushes the neutral junction region further away from the TG, thereby making the electric field distribution increasingly symmetric. Ultimately, at  $V_{\mathrm{TG}} = -10 \mathrm{~V}$ , we obtain a sizeable in-plane electric field, with a maximum  $|F_{\mathrm{x}}|$  of around  $40 \mathrm{~V} \mu \mathrm{m}^{-1}$ .

From these quantities, we determine the total excitonic confining potential as outlined in equation (1). The dc Stark shift contribution is computed by assuming an exciton polarizability  $\alpha = 6.5\mathrm{eV}\mathrm{nm}^2\mathrm{V}^{-2}$  (ref. [23]). The repulsive polaron shift is determined by empirically extracting an effective exciton-electron coupling strength  $\beta \simeq 0.7~\mu \mathrm{eV}~\mu \mathrm{m}^2$  from our experimental data. It corresponds to the slope of a linear function fitted to the density-dependent blue shift of the repulsive polaron in the reflectance data, shown in Fig. 2b.

The resulting potential experienced by the exciton in its COM frame for various  $V_{\mathrm{TG}}$  is depicted in the lower panel of each subplot in Extended Data Fig. 1. Furthermore, we also show the calculated discrete eigenstates associated with the confining potential obtained by numerically solving the Schrödinger equation in the COM frame<sup>2</sup>. A potential well starts to form only at  $V_{\mathrm{TG}} = -4\mathrm{V}$ , but is not strong enough to lead to discernible quantization (Extended Data Fig. 1c). However, the 2D excitonic state may exhibit a small red shift. At  $V_{\mathrm{TG}} < -4\mathrm{V}$ , the Stark shift contribution starts to become notable and leads to the formation of a narrower potential well localized in close proximity to the TG edge. Here, in the i-i-n regime, the continuum is given by the 2D free exciton energy  $E_{\mathrm{X,2D}}$  and the confinement is solely driven by the dc Stark shift. As the gate voltage is lowered further to  $V_{\mathrm{TG}} < -6\mathrm{V}$ , we enter the p-i-n regime (Extended Data Fig. 1e, f), in which the continuum is solely determined by the hole or electron repulsive polaron  $(\mathrm{RP}^{\pm})$  energy, depending on whether the electron side or the hole side has

# Article

lower density. This leads to the striking observation of quantized states above the free exciton energy  $E_{\mathrm{X,2D}}$ .

# Device-charging behaviour

To understand the doping behaviour in our devices, we consider three spatial regions as follows: (I) the region away from the TG that is affected only by the BG, (II) the region directly underneath the TG and (III) the narrow region between I and II. Owing to the diffraction-limited spot size, we simultaneously measure the combined optical response of all three regions. We note that the energy of the repulsive polaron state is a sensitive detector of the charge density. Therefore the charging behaviour of the p-i-n junction in our devices can be understood by measuring the reflectance spectra as a function of  $V_{\mathrm{BG}}$  and  $V_{\mathrm{TG}}$ . Specifically, measuring the reflectance at fixed energy  $E = E_{\mathrm{X,2D}} + \Gamma / 2 = 1,645 \mathrm{meV}$  (dashed line in Extended Data Fig. 2a, b) allows us to identify the doping configuration.

In Extended Data Fig. 2a, we show the reflectance spectra, measured on Device1, as a function of  $V_{\mathrm{BG}}$  (for fixed  $V_{\mathrm{TG}}$ ), which shows the typical charging behaviour that exhibits neutral exciton, repulsive and attractive polaron branches on the n-doping and p-doping regimes in region I. Moving from right to left along the horizontal dashed line takes us from the n-doped to i-doped to p-doped regimes in region I. Similarly, in Extended Data Fig. 2b, we show the reflectance as a function of  $V_{\mathrm{TG}}$  (for fixed  $V_{\mathrm{BG}}$ ), which also exhibits the neutral and attractive polaron branches. Once again, moving from right to left along the horizontal dashed line takes us from n-doped to i-doped to p-doped regimes in region II. We note that, in both cases, as we move along the dashed lines, we observe two repulsive polaron states,  $\mathrm{RP}^{-}$ and  $\mathrm{RP}^{+}$ . These resonances demarcate regions of electron and hole doping. On the right of  $\mathrm{RP}^{-}$ , we are always electron-doped, whereas on the left of  $\mathrm{RP}^{+}$ , we are always hole-doped. In between, we are in the neutral regime.

Using this method, we can monitor the charge configurations in both regions I and II by measuring the reflectance at fixed energy as a function of  $V_{\mathrm{TG}}$  and  $V_{\mathrm{BG}}$ , as shown in Extended Data Fig. 2c. Owing to the mechanism explained above, we observe that the  $\mathrm{RP^{+}}$  and  $\mathrm{RP^{-}}$  resonance exhibit a zigzag shape in the  $V_{\mathrm{BG}} - V_{\mathrm{TG}}$  plane. As the energy of the repulsive polaron state is proportional to charge density, moving on the zigzag line amounts to moving along a path of constant charge density. To identify the charging configurations, we use the notation (II, I). For example, (p, n) refers to p-doping in II and n-doping in I. In general, moving vertically at fixed  $V_{\mathrm{TG}}$  tunes the doping in region I. For example, moving along path 1 takes the doping configuration from (p, p) to (p, i) to (p, n). Similarly, moving horizontally keeping  $V_{\mathrm{BG}}$  fixed tunes the doping in region II.

We observe in Extended Data Fig. 2c that all charging configurations are possible in our device. This is surprising considering that the electrical contact to the TMD monolayer exists only in region I and not in region II. Therefore, any charges that have to reach region II from the contacts (in region I) have to necessarily pass through region I in an equilibrium setting. For example, in the top-left corner, we observe the p-n regime that is relevant for this work. In this voltage range, it is energetically unfavourable for holes to reach region II by traversing region I, which is n-doped. To explain this, we consider a charge injection mechanism on the basis of optical doping, which is a local effect.

When region I is neutral, a voltage bias between TG and BG results in electric fields  $(F \propto V_{\mathrm{BG}} - V_{\mathrm{TG}})$  which can lead to a trapping potential for charges under the TG. However, because the Fermi energy is in the gap, in thermodynamic equilibrium, it is not energetically favourable for electrons or holes to populate this trap. Nevertheless, on optical excitation, excitons can dissociate under the strong in-plane electric field generated at the edges of the TG. Thus, individual charge carriers are left behind, which are accelerated towards region II, in which they ultimately get trapped. On the other hand, the generated field between the TG and the BG also leads to a finite rate of charges tunnelling out of the TMD in the out-of-plane direction. We suspect that this interplay between charge injection through exciton dissociation and charge removal by means

of leakage currents defines the doping configuration in our device. The impact of both mechanisms is influenced by the electric field magnitude. Correspondingly, the observed charge density in region II also scales linearly,  $\sigma \propto V_{\mathrm{BG}} - V_{\mathrm{TG}}$ . The doping situation is different when the device is globally n-doped or p-doped. To reach charge neutrality,  $V_{\mathrm{TG}}$  now needs to be tuned to a voltage that removes the charges under the TG, therefore at the equal density line  $\sigma \propto V_{\mathrm{TG}} + V_{\mathrm{BG}}$ . We expect that, in this scenario, the doping of opposite charge carriers in region II also arises from the aforementioned optical doping mechanism.

# n-i-p Regime in Device 2

In our work, we mainly focused on the p-i-n regime, in which region I is n-doped and region II is p-doped. In principle, the mechanism of quantum confinement in the i region should work the same way, even in the opposite n-i-p regime, in which region I is p-doped and region II is n-doped. In Extended Data Fig. 4, we show the normalized reflectance measured as a function of  $V_{\mathrm{TG}}$  for fixed  $V_{\mathrm{BG}} = -7\mathrm{V}$ .

We observe similar qualitative signatures of quantum confinement, that is, the narrow discrete lines emerging out of the repulsive polaron continuum. As expected, these lines now appear at positive  $V_{\mathrm{TG}}$ . However, we do observe conspicuous quantitative differences between the p-i-n and n-i-p settings. We find that a prolonged neutral region, seen in Fig. 2b, is absent in the data shown in Extended Data Fig. 4. Because of this we suspect that the discrete resonances in the n-i-p scenario do not exhibit the sharp initial red shift as observed in the voltage range  $-6\mathrm{V} < V_{\mathrm{TG}} < -4\mathrm{V}$  in Fig. 2b.

We suspect that the origin of this discrepancy could be rooted in the substantially different leakage current for electrons and holes. Owing to the small valence band offset between h-BN and  $\mathrm{MoSe}_2$ , the tunnelling rate for holes is expected to be considerably larger than for electrons. This gives rise to a long lifetime of trapped electrons. Hence, while increasing  $V_{\mathrm{TG}}$ , a non-equilibrium electron population in region II can be sustained immediately after the hole population has been fully depleted.

# Spectral analysis procedure

Whereas a detailed analysis of the reflectance line shape requires the use of the transfer matrix method, a more straightforward approach is to describe the measured reflectance signal as  $\mathrm{Im}[\mathrm{e}^{\mathrm{i}\alpha (E)}\chi (E)]$ , in which  $\chi (E)$  is the  $\mathrm{MoSe}_2$  monolayer optical susceptibility and  $\alpha (E)$  a wavelength-dependent effective phase shift  $^{54}$ . The parameter  $\alpha (E)$  captures the effect of light interfering at different material interfaces in our device heterostructure (for example, h-BN/Au). To the first order we assume  $\alpha$  to be wavelength-independent in our spectral range of interest. The reflectance spectral profile  $S(E)$  associated with an optical resonance can then be modelled in the following manner:

$$
L _ {0} (E) = \frac {\Gamma / 2}{\left(E - E _ {0}\right) ^ {2} + \Gamma^ {2} / 4} \tag {6}
$$

$$
L _ {\mathrm {D}} (E) = \frac {E _ {0} - E}{\left(E - E _ {0}\right) ^ {2} + \Gamma^ {2} / 4} \tag {7}
$$

$$
S (E) = A \left(\cos (\alpha) L _ {0} (E) + \sin (\alpha) L _ {\mathrm {D}} (E)\right) + C \tag {8}
$$

in which  $L_{0}(E)$  and  $L_{\mathrm{D}}(E)$  constitute a pure Lorentzian and a dispersive Lorentzian line shape, respectively, with  $E_{0}$  being the centre frequency and  $\Gamma$  the linewidth. The parameter  $A$  characterizes the overall amplitude of the resonance, whereas  $C$  takes into account any broad background signal. The result of fitting this spectral profile to the bare 2D exciton transition (corresponding to the linecut taken at  $V_{\mathrm{TG}} = -3.5\mathrm{V}$  in Fig. 2c) is depicted in Extended Data Fig. 5a.

We attribute the origin of the discrete spectral features in our optical measurements to quantum confinement of excitons. As a consequence, when the energy splitting  $\hbar \omega$  becomes comparable with the exciton

In the following, we present a new method for measuring the line width, we expect to see a coherent superposition of overlapping discrete lines that are associated with individual states splitting off from a broad continuum resonance. To justify this claim, we take the spectrum at  $V_{\mathrm{TG}} = -6.2 \mathrm{~V}$  (Fig. 2c) as an example and fit it with a superposition of narrow spectral profiles  $\sum_{i} S(E; E_{0,i}, \Gamma_{i}, A_{i}, \alpha_{c})$ , which characterize the lines associated with quantized motional states, and a broad resonance  $S(E; E_{\mathrm{RP}}, \Gamma_{\mathrm{RP}}, A_{\mathrm{RP}}, \alpha_{\mathrm{RP}})$  that accounts for the repulsive polaron continuum. As shown in Extended Data Fig. 5b, a good fit of the measured data can be achieved over the whole spectral range of interest. We emphasize that, during this procedure, the same phase factor  $\alpha_{c}$  is assumed for all lines associated with confined states. This can also be seen in Extended Data Fig. 5c, which depicts the individual components of the overall spectrum. The states for which the transition energy is not traced in Fig. 2d are thereby marked in grey. Furthermore, the phase factor of the hole repulsive polaron resonance  $\alpha_{\mathrm{RP}}$  is not the same as  $\alpha_{c}$ . This is justified considering that the origin of this resonance is rooted in a separate spatial region of the device, thus causing a different interference pattern. For the purpose of illustration, we also show in Extended Data Fig. 5d the resonances when the asymmetry in their line shape is removed by setting  $\alpha_{c} = 0^{\circ}$  while retaining the other fit parameters.

The full list of parameters obtained from the fit of this spectrum at  $V_{\mathrm{TG}} = -6.2$  V is shown in Extended Data Fig. 5e. The lower energy resonances exhibit a linewidth  $\Gamma_{i} \gtrsim 500 \mu \mathrm{eV}$ , which is almost a factor of 4 smaller than the bare 2D exciton linewidth (see Extended Data Fig. 5a). At lower  $V_{\mathrm{TG}}$ , in which a stronger excitonic confinement is expected, we observe narrowing of the linewidth down to  $300 \mu \mathrm{eV}$ . This analysis shows how, after the onset of hole doping, not only does the continuum blueshift owing to the emergence of the repulsive polaron but, concurrently, a broadening and loss of oscillator strength for the higher-lying discrete states is observed.

Owing to the intricate structure of our reflectance data, the fitting procedure described above cannot be performed in an automated way for the entire range of  $V_{\mathrm{TG}}$ . Hence, the transition energies shown in Fig. 2d are obtained by selecting a narrow spectral range that only contains the confined states and fitting a superposition of pure Lorentzians, that is,  $\sum_{i} L_{0}(E; E_{0,i}, \Gamma_{i}, A_{i})$ , in other words, the phase factor  $\alpha_{c}$  is set to  $0^{\circ}$ . This assumption probably introduces a systematic offset in the estimation of the resonance energy. However, this is not a big hindrance because we focus on the evolution of transition energies as a function of  $V_{\mathrm{TG}}$ . Similarly, PL spectra are also fit by a superposition of pure Lorentzians, that is,  $\sum_{i} L_{0}(E; E_{0,i}, \Gamma_{i}, A_{i})$ .

# Polarization anisotropy data

In Fig. 3, we depicted the polarization dependence in PL originating from 1D quantum-confined excitons. In Extended Data Fig. 6, we show linecuts from these datasets (corresponding to measurements performed on Device 1 and Device 2, that is, Fig. 3c, d, respectively) at orthogonal detection angles. To verify that the strong polarization anisotropy we report for Device 1 in the main text is indeed associated with the confined states of the exciton, we perform polarization-resolved PL measurements also for various other optical transitions observed in the device. Extended Data Figure 7a demonstrates a reference BG  $(V_{\mathrm{BG}})$  scan conducted at a position away from the TG region. Also shown in Extended Data Fig. 7b, c is a  $V_{\mathrm{TG}}$  scan performed on the TG edge. We reiterate that, because the spot size of our excitation beam is diffraction-limited, PL emission from three distinct spatial regions is measured: (1) the region away from the TG is electron-doped and thus gives rise to a broad attractive polaron resonance  $(\mathrm{AP}_{\mathrm{I}}^{-})$  centred at around  $1.615\mathrm{eV}$ , which remains unaffected as a function of  $V_{\mathrm{TG}}$ ; (2) the region underneath the TG leads to neutral exciton  $(\mathrm{X}_{\mathrm{II}}^{0})$  and attractive polaron resonances  $(\mathrm{AP}_{\mathrm{II}}^{-}$  and  $\mathrm{AP}_{\mathrm{II}}^{+})$  as it changes from being electron-doped, neutral and finally hole-doped when  $V_{\mathrm{TG}}$  is lowered; (3) the neutral intermediate region at the edge of the TG gives rise to redshifting confined exciton lines  $(\mathrm{X}_{\mathrm{III}}^{0})$  as  $V_{\mathrm{TG}}$  is lowered.

In Extended Data Fig. 7d–f, we show the polarization dependence of these optical transitions by plotting the normalized PL emission as a

function of linear polarization detection angle.  $0^{\circ}$  thereby constitutes the direction along the quantum wire and thus the TG edge. As shown in Extended Data Fig. 7f, the attractive polaron resonances originating from underneath the TG  $(\mathrm{AP}_{\parallel}^{+})$  and away from the TG  $(\mathrm{AP}_{1}^{-})$  have a low degree of linear polarization  $\xi = (I_{\max} - I_{\min}) / (I_{\max} + I_{\min}) \lesssim 20\%$ , in which  $I_{\max}$  and  $I_{\min}$  are the maximum and minimum intensities, respectively. These are obtained by fitting the function  $A \cdot \cos^2 (\theta - \theta_0) + C$  to the normalized PL intensities as a function of the detection angle  $\theta$ . The neutral exciton originating from underneath the TG  $(X_{\parallel}^{0})$  exhibits a similar behaviour ( $\xi \approx 10\%$ , see Extended Data Fig. 7e). Furthermore, the primary polarization axis of these resonances, given by  $\theta_0$ , has varying orientation and does not align with the TG edge. As a reference, we also compute  $\xi$  for these optical transitions away from the TG and find that it is in the same range (Extended Data Fig. 7d). In strong contrast to this behaviour, the confined exciton states exhibit  $\xi = 96\%$ , along with a primary polarization axis oriented within  $\pm 5^{\circ}$  along the TG edge.

Owing to the similarity in polarization properties of exciton and polaron resonances from regions I and II, we conclude that the strongly polarized emission of the confined excitonic states has its origin in the 1D confinement rather than a screening by the metallic TG, the effect of which cannot be distinguished from a typical strain-induced polarization dependence. If the geometry of the metallic TG had an impact on the polarization properties of the emission, also other optical transitions would exhibit an enhanced linear emission.

# Power dependence data

In Fig. 3f, we showed the excitation power dependence of the normalized PL emission intensity of the  $\mathrm{X}_{2\mathrm{D}}$  and  $\mathrm{X}_{\mathrm{QC}}$  states. In this section, we comment on the evolution of the resonance energy of these states, which is extracted from the same measurement dataset. The free 2D exciton states only exhibit a slight variation in energy of approximately  $0.1\mathrm{meV}$  blue shift as the excitation power is increased from  $100\mathrm{nW}$  to  $100\mu \mathrm{W}$  (Extended Data Fig. 8a). For the analysis of  $\mathrm{X}_{\mathrm{QC}}$  excitons, we track the power dependence of the two lowest quantum-confined states. For the lowest confined state, we observe that the resonance energy first exhibits a blue shift by approximately  $0.2\mathrm{meV}$  at low powers. This trend changes sign to a red shift at high powers ( $P > 1\mu \mathrm{W}$ ) (Extended Data Fig. 8a).

In an ideal scenario, the interaction between dipolar excitons, particularly in strongly confined systems, is expected to give rise to a shift of the resonance energy. However, it can be difficult to isolate such interaction effects from other effects that can arise from the continuous-wave PL excitation[55]. Specifically, in our system, we suspect that the observed red shift occurs owing to optically induced doping that introduces charges to the p-doped and n-doped regions, and thus modifies the spatial in-plane electric field distribution. This can be seen most clearly by extracting the energy splitting between the lowest quantum-confined eigenstates as a function of excitation power, as shown in Extended Data Fig. 8b. Here we observe a clear increase in the level splitting, indicating tighter confinement at higher power.

If this picture is correct, it would be a very interesting feature of our scheme, as it potentially suggests a control of the confinement using optical excitation. However, we hesitate to make definite claims before carrying out time-resolved pump-probe measurements, which should help distinguish between contributions of interaction-induced blue shift and a possible enhancement of the in-plane electric field.

# Magnetic field measurements

Here we provide details of the  $B$ -field measurements reported in Fig. 4. These measurements are performed at around  $4\mathrm{K}$  in a cryostat with fibre-optical access and a superconducting coil that can generate  $B$ -fields of up to  $16\mathrm{T}$  in the direction perpendicular to the sample surface. Using nanopositioners, we can position the optical spot on the

# Article

edge of the graphene TG in Device 2. As we ramp the magnetic field, we observe spatial drift of the sample. Hence the optical spot must be readjusted to measure on the same position at every magnetic field. We achieve this by using the bright 2D exciton state as a reference spectrum and scanning the sample position until the observed spectrum matches the reference at charge neutrality. In addition to realigning the position, we also recalibrate the optical setup at every magnetic field, to compensate for any Faraday rotation resulting from the strong  $B$ -fields. In this way, we are able to reliably perform circular-polarization-resolved measurements in the range  $B = 0 - 16$  T. At every value of the magnetic field, we perform measurements at different  $V_{\mathrm{TG}}$  and  $V_{\mathrm{BG}}$ .

In accordance with the spectral analysis procedure described above, the measured spectra are then fitted with the reflectance spectral profile  $S(E)$  (equation (8)) for  $\mathrm{X}_{2\mathrm{D}}$  and a superposition of such spectral profiles  $\sum_{i} S(E; E_{0,i}, \Gamma_{i}, A_{i}, \alpha_{i})$  for the quantum-confined states. In the case of  $\mathrm{X}_{\mathrm{QC}}$ , we track only the evolution of the polarization-split ground state (black arrows in Fig. 4b). Only at  $B = 0 \mathrm{T}$  are both of the linear-polarization-split quantum-confined ground states visible in the same circular polarization. Hence, for the zero-field case, their phase factor  $\alpha$  is assumed to be the same. From the resulting fits (shown in Fig. 4a, b), we extract the resonance energies  $E^{+}$  and  $E^{-}$  of the respective polarization-split states. The corresponding fitting error is approximately  $\lesssim 15 \mu \mathrm{eV}$ . Therefore we can obtain the Zeeman splitting  $E^{+} - E^{-}$  and the average energy  $\overline{E} = (E^{+} + E^{-}) / 2$  with a similar precision. The fact that  $\overline{E}$  for 2D excitons is almost zero is a consistency check for the position alignment procedure described above.

The Zeeman splitting for both  $\mathrm{X}_{2\mathrm{D}}$  and  $\mathrm{X_{QC}}$  are shown in Fig. 4c. We observe perfect linear behaviour for 2D excitons as expected, leading to a  $g$ -factor of about 4.6 (Extended Data Fig. 9a). The confined states start with a finite polarization splitting at  $B = 0$  T and asymptotically approach linearity only at high fields. This can be modelled with the  $B$ -field dependence

$$
\Delta E = \sqrt {\delta^ {2} + \left(\mathrm {g} \mu_ {\mathrm {B}} B\right) ^ {2}} \tag {9}
$$

in which  $\delta$  is the zero-field splitting and  $\mu_{\mathrm{B}}$  is the Bohr magneton. The fitted results are shown in Fig. 4d, along with  $\Delta E$  determined from experimental data points. We observe that, at low fields, the model seems to have a systematic error. The fitted values for  $\delta$  systematically underestimate the value obtained by directly taking the difference of the fitted  $E^{+}$  and  $E^{-}$  resonance energy at  $B = 0$  T. Therefore, the fitted values of  $\delta$  exhibit larger fitting errors of around  $100~\mu \mathrm{eV}$  (Extended Data Fig. 9b). The  $g$ -factor of  $X_{\mathrm{QC}}$  states as a function of  $V_{\mathrm{TG}}$  is shown in Extended Data Fig. 9a. We observe a decrease of the  $g$ -factor below the value for 2D excitons as  $V_{\mathrm{TG}}$  is reduced. We do not have an explanation for this voltage-dependent  $g$ -factor. We speculate that strong in-plane electric fields may modify the Bloch states of free electrons and holes, as well as the relative motion of bound electrons and holes in excitons, thus leading to the observed voltage-dependent shifts of the  $g$ -factor.

# Exact diagonalization calculations

To better understand the physics of confined excitons in in-plane electric and out-of-plane magnetic fields, we exactly diagonalize the following Hamiltonian in relative coordinates  $(r,\theta)$  between the electron and the hole comprising the exciton<sup>37,56</sup>:

$$
H = - \frac {\hbar^ {2}}{2 \mu_ {+}} \nabla^ {2} + \hbar \frac {e B}{2 \mu} (- i \partial_ {\theta}) + \frac {e ^ {2} B ^ {2}}{8 \mu_ {+}} r ^ {2} + V _ {\mathrm {K}} (r) - e F _ {\mathrm {x}} x, \tag {10}
$$

in which  $\mu_{\pm} = \frac{m_{\mathrm{n}}^{*}m_{\mathrm{p}}^{*}}{m_{\mathrm{n}}^{*}\pm m_{\mathrm{p}}^{*}}$  and  $V_{\mathrm{K}}$  is the Keldysh potential

$$
V _ {\mathrm {K}} (r) = - \frac {e ^ {2}}{4 \pi \varepsilon_ {0}} \frac {\pi}{2 \varepsilon r _ {0}} \left[ H _ {0} \left(r / r _ {0}\right) - Y _ {0} \left(r / r _ {0}\right) \right] \tag {11}
$$

We use  $m_{\mathrm{n}}^{*} = 0.7m_{\mathrm{e}}$  (ref. 51),  $m_{\mathrm{p}}^{*} = 0.6m_{\mathrm{e}}$  (ref. 52) for effective electron and hole masses, respectively,  $\varepsilon = 4.4$  for the dielectric constant and

$r_0 = 3.9 / \varepsilon$  nm for the screening length[22]. In the absence of any applied electric or magnetic field, we obtain with this procedure a binding energy of 1s excitons  $E_{\mathrm{B}} = 217$  meV, which is comparable with experimental values.

We exactly diagonalize the above Hamiltonian on the basis of Bessel functions with Dirichlet boundary conditions, on a disc of radius  $R$ . The Hilbert space of a 2D disc of radius  $R$  admits the basis  $|m,n\rangle|$  for  $m\in \mathbb{Z},n = 1,2,\ldots$ , whose elements can be expressed in polar coordinates as

$$
\langle r, \theta | m, n \rangle = \frac {1}{Z _ {m , n}} J _ {m} \left(k _ {m, n} r\right) e ^ {i m \theta}, \tag {12}
$$

in which  $k_{m,n} = z_{m,n} / R$ , with  $z_{m,n}$  being the nth zeros of the Bessel function  $J_{m}(z)$ . Typically, we consider up to  $n = 250$  modes and  $m \leq 10$  angular modes. This basis is particularly convenient to treat a particle in an electric field, as only a few angular modes are required. The difficulty in dealing with an external uniform in-plane electric field is that the Hamiltonian spectrum is not bounded from below, and – hence – the ground state of the system depends on the system size  $R$ . To mitigate this problem, we monitor the energy variation as a function of  $B$  and  $F_{\mathrm{x}}$  not of the ground state but of the most localized eigenstate at the origin, which we abbreviate as MLESO.

Moreover, we focus on  $R$  values in the range 25-40 nm, comparable with the size of the intrinsic region of the experiment. Within this range, the results at different sizes are in agreement provided one avoids values of  $R$  and  $F_{\mathrm{x}}$  for which an unbound state is exactly resonant with the bound state. We note that the oscillations seen in Extended Data Fig. 10d are an artefact of the finite size box, whereas one would have a plane wave for an ionized state in a real continuum. A mathematical treatment of the limit  $R \to \infty$  is the subject of current theoretical research.

In Extended Data Fig. 10a, we show the MLESO energy as a function of the in-plane electric field strength  $|F_{\mathrm{x}}|$  at  $B = 0$  T, which shows a quadratic  $F_{\mathrm{x}}$  dependence, as expected from the dc Stark effect. The order of magnitude of the calculated shift is comparable with the measured Stark shifts in our experiment. In Extended Data Fig. 10b, we show  $|\psi (r = 0)|^2$ , which is proportional to the exciton oscillator strength, as a function of electric field, approximately spanning the range of field magnitudes achievable in the experiment. We observe that the wave function overlap in the Coulomb well, which directly corresponds to the oscillator strength, decreases with increasing  $F_{\mathrm{x}}$ , but only by about  $10 - 15\%$ . In the experiment, the overall oscillator strength is strongly reduced owing to COM confinement, but does not vary appreciably as a function of applied gate voltage. In Extended Data Fig. 10c, d, we show the 2D probability density  $|\psi (x,y)|^2$  in the relative frame for in-plane electric field values of  $|F_{\mathrm{x}}| = 0$  and  $|F_{\mathrm{x}}| = 30 \mathrm{~V} \mu \mathrm{m}^{-1}$ , respectively. The probability density along  $x$  at  $y = 0$  for these fields is shown in Extended Data Fig. 10e. Whereas at  $|F_{\mathrm{x}}| = 0$  we obtain the expected decay of a tightly bound 2D exciton, the case for high electric fields indicates a modified wave function, with longer decay length scale. The spatial oscillations observed in Extended Data Fig. 10e are artefacts arising from a finite-sized box. In Extended Data Fig. 10f, we show the MLESO energy shift as a function of  $B$  for different values of  $F_{\mathrm{x}}$  and  $R = 40 \mathrm{~nm}$ . The energy shift is shown with respect to the energy  $E(B = 0 \mathrm{~T})$ . We observe a clear  $B$ -dependent shift on the same order of magnitude as seen in the experiment. Moreover, we observe that the shift is larger for larger applied electric field, which is also qualitatively in agreement with the experimental observation (Fig. 4e).

# Data availability

The data that support the findings of this study will be made publicly available at the ETH Research Collection on publication (http://hdl.handle.net/20.500.11850/478320).

47. Zomer, P. J., Guimarães, M. H. D., Brant, J. C., Tombros, N. & van Wees, B. J. Fast pick up technique for high quality heterostructures of bilayer graphene and hexagonal boron nitride. Appl. Phys. Lett. 105, 013101 (2014).  
48. Telford, E. J. et al. Via method for lithography free contact and preservation of 2D materials. Nano Lett. 18, 1416-1420 (2018).  
49. Jung, Y. et al. Transferred via contacts as a platform for ideal two-dimensional transistors. Nat. Electron. 2, 187-194 (2019).  
50. Wilson, N. R. et al. Determination of band offsets, hybridization, and exciton binding in 2D semiconductor heterostructures. Sci. Adv. 3, 1601832 (2017).  
51. Larentis, S. et al. Large effective mass and interaction-enhanced Zeeman splitting of K-valley electrons in  $\mathrm{MoSe}_2$ . Phys. Rev. B 97, 201407 (2018).  
52. Zhang, Y. et al. Direct observation of the transition from indirect to direct bandgap in atomically thin epitaxial  $\mathrm{MoSe}_2$ . Nat. Nanotechnol. 9, 111-115 (2014).  
53. Laturia, A., de Put, M. L. V. & Vandenberghe, W. G. Dielectric properties of hexagonal boron nitride and transition metal dichalcogenides: from monolayer to bulk. NPJ 2D Mater. Appl. 2, 6 (2018).  
54. Smolenski, T. et al. Interaction-induced Shubnikov-de Haas oscillations in optical conductivity of monolayer  $\mathrm{MoSe}_2$ . Phys. Rev. Lett. 123, 097403 (2019).  
55. Scuri, G. et al. Large excitonic reflectivity of monolayer  $\mathrm{MoSe}_2$  encapsulated in hexagonal boron nitride. Phys. Rev. Lett. 120, 037402 (2018).  
56. Lozovik, Y. E., Ovchinnikov, I. V., Volkov, S. Y., Butov, L. V. & Chemla, D. S.  
Quasi-two-dimensional excitons in finite magnetic fields. Phys. Rev. B 65, 235304 (2002).

Acknowledgements We thank A. Srivastava, I. Schwartz, R. Schmidt, A. Bergschneider and N. Lassaline for insightful discussions. This work was produced within the scope of the National Research Programme NCCR QSIT, which was financed by the Swiss National Science Foundation (SNSF) and supported by the SNSF grant 200021-178909/1. P.A.M. acknowledges

financing from the European Union's Horizon 2020 programme under Marie Skłodowska-Curie grant MSCA-IF-OptoTransport (843842). K.W. and T.T. acknowledge support from the Elemental Strategy Initiative conducted by MEXT, Japan, A3 Foresight by JSPS and CREST (grant number JPMJCR15F3) and JST. D.T. and D.J.N. acknowledge support by the SNSF under grant 200021-165559. T.C. acknowledges support from NTT Research, Inc., USA. Synthesis of  $\mathrm{MoSe_2}$  crystals in Device 2 was supported by the United States National Science Foundation Materials Research Science and Engineering Centers DMR-2011738.

Author contributions P.A.M., A.I. and D.T. conceptualized the project. D.T., T.S. and P.A.M. carried out the experiments. D.T. performed the electrostatic simulations, with input from P.A.M. and A.P. D.T. fabricated Device 1 and X.L. fabricated Device 2. I.A. performed exact diagonalization calculations. A.P. assisted with measurements, device fabrication and simulations. K.W. and T.T. provided the h-BN crystals. S.L. and K.B. provided the  $\mathrm{MoSe}_2$  crystals for Device 2. M.K. and T.C. assisted P.A.M. and D.T. with the experimental setup. P.A.M., D.T. and A.I. wrote the manuscript. A.I., D.J.N., M.K. and P.A.M. supervised the project.

Competing interests D.T., P.A.M., M.K., A.P. and A.I. are seeking patent protection for ideas described in this work.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41586-022-04634-z.

Correspondence and requests for materials should be addressed to Atac Imamoglu or Puneet A. Murthy.

Peer review information Nature thanks Mikhail Glazov, Libai Huang and the other, anonymous, reviewer for their contribution to the peer review of this work. Peer reviewer reports are available.

Reprints and permissions information is available at http://www.nature.com/reprints.

![](images/5f25764debf8b9741ddcc480f1721a74dde9248966bd98905dbe70328abf120a.jpg)  
a

![](images/58eb5fdf6619bf3a750c9306198c37ad5cfa88b394f5b8199d7d9740827260f2.jpg)  
b

![](images/535f2a6a354a3d28ccf9786dc9b84df8bb969cbc245fc851f947c91637738634.jpg)  
C

![](images/a453da34aa3394156d692fbcda66d3bed2e1362b8c0028517437e5f66e1277c9.jpg)  
d

![](images/75140c09c7a12537851a174b5d607e3b069e24f135427776de8aaa9304623572.jpg)  
e  
Extended Data Fig.1|Electrostatic simulations of the device. Magnitude of charge density  $|\sigma (x)|$  , in-plane electric field  $|F_{\mathrm{x}}|$  and exciton confining potential  $V(x)$  as a function of position for varying TG voltages  $V_{\mathrm{TG}}$  and fixed BG voltage  $V_{\mathrm{BG}} = 4\mathrm{V}$  . The BG extends over the entire plotted range of the position from

![](images/34460166112a43c20f86547174cc438d1bd352da3df68ac799e55285c87be9d0.jpg)  
f  
$-80 \mathrm{~nm}$  to  $80 \mathrm{~nm}$ . The TG extends from  $-80 \mathrm{~nm}$  to  $0 \mathrm{~nm}$ , with the edge at  $x = 0$ . The different charging configurations, namely n-n-n (a, b), i-i-n (c, d) and p-i-n (e, f), show the evolution of the confinement potential as a function of  $V_{\mathrm{TG}}$ .

![](images/2d941db65548d213b74838d4c5f40c3744790df66a25984cc99b9aceb6a35aea.jpg)

![](images/eb61a58902c30619daa1eb6861cb58f2e988edc64adf29a24b5d9b815205044d.jpg)  
Extended Data Fig. 2 | Doping characteristics of Device1. We use the charge-density-dependent energy shifts of the repulsive polaron states to obtain the doping configuration of the device. Because the RP states exist in regions I and II of the device and on electron and hole sides, we use the notation  $\mathrm{RP}_{\text {region }}^{\text {charge }}$  to denote the different states. a, Normalized reflectance  $\Delta R / R$  measured for fixed  $V_{\mathrm{TG}} = -6 \mathrm{~V}$  as a function of  $V_{\mathrm{BG}}$ , in which we mainly observe features from region I. b,  $\Delta R / R$  measured for fixed  $V_{\mathrm{BG}} = 1.8 \mathrm{~V}$  as a function of  $V_{\mathrm{TG}}$ , in which we observe the spectral changes in region II. In addition to the features from region II, we see the repulsive polaron resonance from region I  
at  $E \approx 1,648$  meV, which is not affected by  $V_{\mathrm{TG}}$ , c, Normalized reflectance taken at a fixed energy  $E_{\mathrm{X0}} + \Gamma / 2 = 1,645$  meV, in which  $\Gamma$  is the bare 2D exciton linewidth. The horizontal solid lines demarcate the n-doped, neutral and p-doped regimes in region I. The doping configurations in regions I and II in different voltage regimes are identified. For example, in the top-left corner, which is the relevant regime for this work, the doping configuration is (II, I) ≡ (p, n). d, Schematic of the device showing regions I and II, as well as the position of the electrical contact to the monolayer.

![](images/d87d94361b89145faa9f28086eaa95c32c57affdc034aec2d5b3fe5f113ea638.jpg)  
c

![](images/de23ce86c0aa69b35b19b6b69fc0adba96ba107fd0840c9843f27c6bed386051.jpg)

![](images/b1c368f0f05a64d1ceb5fca9986cde7df2fccfc9cc918302b06fcacf54594d35.jpg)

![](images/b99d7a385c32880672666aeaa255e873f7a886bf0f315ebfec85574af93ed23e.jpg)

![](images/e6166d36d6fd88533af9941f449bf630f114b1232a3ffdb8d7f8008598365c7d.jpg)

# Extended Data Fig. 3 | Electrically tunable quantum confinement in

Device 2. a, Optical micrograph of Device 2, in which the outline of the  $\mathrm{MoSe}_2$  monolayer is indicated by the red line. The TG and BG, made of few-layer graphene, are indicated by dashed black lines. b, Schematic diagram of Device 2. c, Spectra taken at the edge of the few-layer graphene TG at  $V_{\mathrm{BG}} = 1\mathrm{V}$  show the emergence of discrete states below the 2D continuum, in excellent

agreement with the observations in Device1 (Fig. 2b). d, Spectral linecuts at  $V_{\mathrm{TG}} = 0$  V, -4 V and -9 V show the emergence of confined states as the potential is made deeper. The exact voltage range and the magnitude of red shift may differ between the two devices owing to design differences, in particular, the thickness of h-BN spacers.

![](images/acab940ba2aa76a96431ba9ae65b08ced0d992c736bc64f1ca64f99fc4065c4b.jpg)

# Extended Data Fig.4 | Quantum confinement in the  $i$ -pre regime.

Normalized reflectance  $\Delta R / R$  from Device 2 as a function of  $V_{\mathrm{TG}}$  for fixed  $V_{\mathrm{BG}} = -7\mathrm{V}$ , corresponding to hole doping in region I. We observe qualitatively similar signatures of quantum confinement as the p-i-n regime shown in the main text, which includes narrow discrete states emerging out of the repulsive polaron  $(\mathrm{RP}^{-})$  continuum for  $V_{\mathrm{TG}} \gtrsim 2.5\mathrm{V}$ .

![](images/a459c3f8d6ec6f6d674864420b8da02f88b3ea817af5667c73659aa31c0087e0.jpg)

![](images/17fbe191b558883ec76fa9190d3711b393b7aa79009057e46068c09286cc4694.jpg)

e  

<table><tr><td>i</td><td>E0 (meV)</td><td>Γ (meV)</td><td>A (meV)</td><td>a (deg)</td></tr><tr><td>1</td><td>1638.2</td><td>0.42</td><td>0.022</td><td>-55.5</td></tr><tr><td>2</td><td>1638.7</td><td>0.62</td><td>0.056</td><td>-55.5</td></tr><tr><td>3</td><td>1639.5</td><td>0.91</td><td>0.050</td><td>-55.5</td></tr><tr><td>4</td><td>1640.1</td><td>0.56</td><td>0.038</td><td>-55.5</td></tr><tr><td>5</td><td>1640.5</td><td>0.88</td><td>0.028</td><td>-55.5</td></tr><tr><td>6</td><td>1641.2</td><td>0.53</td><td>0.027</td><td>-55.5</td></tr><tr><td>7</td><td>1642.0</td><td>1.02</td><td>0.048</td><td>-55.5</td></tr><tr><td>8</td><td>1642.9</td><td>1.00</td><td>0.030</td><td>-55.5</td></tr><tr><td>RP</td><td>1644.7</td><td>4.95</td><td>0.685</td><td>236.8</td></tr></table>

![](images/0dfdb5f3d0736eb3bc63988734bf7d41c66532d1f3f1adce1d8ec745a4ef93e0.jpg)  
Extended Data Fig. 5|Line shape analysis of reflectance data.a, Spectral profile described by equation (8) fit to the bare 2D exciton transition at  $V_{\mathrm{TG}} = -3.5\mathrm{V.b}$ , Reflectance linecut at  $V_{\mathrm{TG}} = -6.2\mathrm{V}$  fit by a superposition of several narrow spectral profiles  $\sum_{i}S\left(E;E_{0,i},\Gamma_{i},A_{i},\alpha_{c}\right) + S(E;E_{\mathrm{RP}},\Gamma_{\mathrm{RP}},A_{\mathrm{RP}},\alpha_{\mathrm{RP}})$

![](images/cd98814ef9de368174feed48299bc35b217d15ac3e0a2adbc743a67e8f5361ca.jpg)  
c, Individual components of the fit. d, Individual components after removing line asymmetry by setting  $\alpha_{\mathrm{c}}$  and  $\alpha_{\mathrm{RP}}$  to  $0^{\circ}$ . The resulting overall line shape is shown in red. e, Results of the fitting procedure for the different resonances at  $V_{\mathrm{TG}} = -6.2\mathrm{V}$ .

![](images/fc7f7f03bcd16dec3b457ac920c9d5eb06fbcd5cd9dbe70b4d761c62bc2a9036.jpg)  
Extended Data Fig. 6 | PL spectra at orthogonal polarization angles for Device1 and Device2. a, In Device1, all discrete states show linear polarized states along the edge of the gate, with a high degree of linear polarization. b, In Device2, the confinement is weaker owing to thicker h-BN spacer layers, which leads to the observation of both  $x$ -polarized and  $y$ -polarized states with finite energy splitting  $\delta$  of around  $1\mathrm{meV}$ . The unmodified resonance at  $E - E_{2t}$  around  $0.5\mathrm{meV}$  corresponds to the repulsive polaron emission from the regi under the TG.

![](images/0b734934267bd3ea0b5fd1a8b1f5393a2febcda57b2ddf69ffafbaf7e479ea7b.jpg)

![](images/bef0b8e89aec8a12ca401f6731782c7e564e021093727fccc59294534ad07d25.jpg)  
a

![](images/eca6748b5a5973eda907c42bb6fd8c2542169d572def2ce2d9dc5f05a2460813.jpg)  
d

![](images/5ba89fe19c0ad0db515ec261bb36e50a58956119fcf4e82d3851e7a36176620b.jpg)  
b  
C

![](images/f3f21af5681a27ab4f0674649ff2c4ad45926d748d06b42f9c3cf356b442477b.jpg)  
e

![](images/79be5e7152128d42a74e72e29d93b4591f78784a2047bfb0da4a1fc75a95e143.jpg)  
Extended Data Fig. 7 | Linear polarization anisotropy of different optical resonances. a, PL BG ( $V_{\mathrm{BG}}$ ) scan conducted on bare  $\mathrm{MoSe}_2$  away from TG region. b, c, PL TG ( $V_{\mathrm{TG}}$ ) scan performed on the TG. d-f, Polarization dependence of optical transitions in regions I, II and III, which are represented in purple,  
magenta and orange, respectively. The exciton, hole-side attractive polaron and electron-side attractive polaron is marked with a circle, cross and dash, respectively.

![](images/4358fbb66d4125c280a33f70a28d8594dcd697636693576c1da7fef87b26847f.jpg)  
f

![](images/856d156dfa49a5a0b702077a038f61e209858b25eaed0e26e7af64f69ed1680d.jpg)  
Extended Data Fig. 8 | Excitation power dependence of resonance energy in PL. a, Shift in resonance energy of  $\mathrm{X}_{2\mathrm{D}}$  (blue) and  $\mathrm{X}_{\mathrm{QC}}$  (black) states relative to their energy measured at the lowest excitation power. b, Evolution of energy splitting between two successive quantum-confined states with power. The shaded areas represent errors from fitting.

![](images/b4642932fa855cc5b137129227575ca07bb957c98606f1b5e370b8dc025503fa.jpg)

![](images/5531c5bb66627e1350db55b4c5a1caee115bd3a4ffdbb2505b0003188ef14dd4.jpg)  
Extended Data Fig. 9 | Extracted  $g$ -factor and zero-field splitting,  $g$ -Factor (a) and zero-field splitting  $\delta$  as a function of TG voltage  $V_{\mathrm{TG}}(\mathbf{b})$ , determined by fitting reflection spectra acquired at finite magnetic fields in the range  $B = 0 - 16$  T. The shaded areas represent fitting errors.

![](images/cf8d7a2320202d3be6a2ce28267843b6b6693f7b6861760a45d84c70a6e8bf14.jpg)

![](images/ac91c4df01234f469016307f7c060c834317c467bb766b41d513d68503d0559f.jpg)

![](images/bfb2e48337dd2523266a5745afc2a8e2d1417e0f8848705fe35003889eeb0d5d.jpg)

![](images/4d4a2161fd1d69ab46766c4adb09338d449b80f6e9dcab7e52e31c9066fc8b49.jpg)

![](images/2f6eea262e517f2aaac82d15a7bfa08a8132852ca88884ecaaf8fc1e8b4fcaa0.jpg)  
Extended Data Fig.10|Exact diagonalization of exciton relative motion in crossed electric and magnetic fields. a, Energy of the MLESO as a function of the in-plane electric field strength  $F_{\mathrm{x}}$  at  $B = 0$  T. A quadratic dependence with the electric field is observed, as expected from the dc Stark effect. b, The probability density  $|\psi (r = 0)|^2$ , proportional to the exciton oscillator strength, decreases by about  $10 - 15\%$  with increasing electric field  $F_{\mathrm{x}}$ . Hence, a decrease in oscillator strength, as seen in the experiment, should primarily arise from COM quantum confinement of excitons. c, d, Calculated probability density  $|\psi (r)|^2$  for  $F_{\mathrm{x}} = 0$  and  $F_{\mathrm{x}} = 30\mathrm{V}\mu \mathrm{m}^{-1}$ , respectively. e, Probability density

![](images/0b522f805339aef329afbb2ff71a6198adb31bd3bc3942d3a9b38fb18d366a12.jpg)  
$|\psi (x,y = 0)|^2$  in the direction of the electric field for  $F_{\mathrm{x}} = 0$  (blue) and  $F_{\mathrm{x}} = 30\mathrm{V}\mu \mathrm{m}^{-1}$  (red). The oscillations seen at finite electric field arise from reflections from the finite-sized box assumed in the calculations. The black curve is a guide to the eye, to show the small but finite component of the wave function that exists outside the Coulomb potential. f, MLESO energy shift with respect to the energy  $E(B = 0\mathrm{T})$  as a function of  $B$ , for different values of  $F_{\mathrm{x}}$ . The magnitude of the predicted shift is on the same order as in the experimental observation.

![](images/04bf8f4ba59dca678a59bf448eb854b0b9204e9706be38dcfc63a4e8d0ec2488.jpg)