# Experimental entanglement of four particles

C. A. Sackett*, D. Kielpinski*, B. E. King*, C. Langer*, V. Meyer*, C. J. Myatt*, M. Rowe*, Q. A. Turchette*, W. M. Itano*, D. J. Wineland* & C. Monroe*

* Time and Frequency Division, National Institute of Standards and Technology, Boulder, Colorado 80303, USA  
† Atomic Physics Division, NIST, Gaithersburg, Maryland 20899, USA  
$\ddagger$  Research Electro-Optics, 1855 S. 57th Ct., Boulder, Colorado 80301, USA

Quantum mechanics allows for many-particle wavefunctions that cannot be factorized into a product of single-particle wavefunctions, even when the constituent particles are entirely distinct. Such 'entangled' states explicitly demonstrate the non-local character of quantum theory $^{1}$ , having potential applications in high-precision spectroscopy $^{2}$ , quantum communication, cryptography and computation $^{3}$ . In general, the more particles that can be entangled, the more clearly nonclassical effects are exhibited $^{4,5}$  and the more useful the states are for quantum applications. Here we implement a recently proposed entanglement technique to generate entangled states of two and four trapped ions. Coupling between the ions is provided through their collective motional degrees of freedom, but actual motional excitation is minimized. Entanglement is achieved using a single laser pulse, and the method can in principle be applied to any number of ions.

Most experimental demonstrations of entanglement to date have relied on the selection of data from random processes, such as the preparation and detection of photon pairs in parametric downconversion $^{7-9}$  or of atoms in a thermal beam $^{10}$ . All methods of this type suffer from inescapable signal degradation when entanglement of larger numbers of particles is attempted, as the probability of randomly generating the appropriate conditions decreases exponentially. For instance, in the experiment of ref. 7, two-photon entangled states could be generated and detected at a rate of roughly 1,000 per second, three-photon states at a rate of 30 per hour, and four-photon states at an extrapolated rate of several per year. Trapped ions have been suggested as a system in which such effects might be avoided $^{11}$ , and we have demonstrated two-particle entanglement in a deterministic way $^{12}$ . By 'deterministic' we mean that the desired state could be produced with a high degree of certainty at a user-specified time $^{13}$ , which is necessary for avoiding the degradation described above. However, that experiment relied on the particular behaviour of two ions in a quadrupole radio-frequency trap, and could not easily be applied to larger numbers of particles.

The entanglement technique proposed by Mølmer and Sørensen<sup>6,14</sup> can be understood by considering a pair of spin-half charged particles confined together in a harmonic potential. The energy levels of this system are illustrated in Fig. 1, where  $\hbar \omega_0$  is the internal energy splitting of each particle, and  $\nu$  is the oscillation frequency of a particular collective mode of the particles in the trap. Using laser-cooling and optical-pumping techniques<sup>15</sup>, the particles are initially prepared in their spin-down internal state and in the ground state of their collective motion:  $|\psi\rangle = |\downarrow\downarrow 0\rangle$ . By applying optical fields oscillating at  $\omega_0 + \nu - \delta$  and  $\omega_0 - \nu + \delta$ , the two-step transition from  $|\downarrow\downarrow 0\rangle$  to  $|\uparrow\uparrow 0\rangle$  is driven. For sufficiently large  $\delta$ , the intermediate states  $|\uparrow\downarrow 1\rangle$  and  $|\downarrow\uparrow 1\rangle$  are negligibly occupied, so that no motional excitation occurs. The resulting interaction hamiltonian, in the rotating-wave approximation and the Lamb-Dicke limit, is then

$$
H = \frac {\hbar \tilde {\Omega}}{2} (| \uparrow \uparrow \uparrow \downarrow | + | \downarrow \downarrow \uparrow \uparrow | + | \uparrow \downarrow \uparrow \downarrow | + | \downarrow \uparrow \uparrow \uparrow |) \tag {1}
$$

with  $\tilde{\Omega} = \eta^2\Omega^2 /\delta$  when the single particle  $|\downarrow \rangle \leftrightarrow |\uparrow \rangle$  transition has

Rabi frequency  $\Omega$  and the Lamb-Dicke parameter is  $\eta$ . For an excitation involving momentum transfer  $\hbar k$  and a total particle mass of  $M$ ,  $\eta$  is given by  $(\hbar k^2 / 2M\nu)^{1/2}$ . Entanglement is achieved by applying  $H$  for a time  $t = \pi/2\bar{\Omega}$ , making the spin wavefunction  $|\psi_2\rangle = (|\uparrow \uparrow\rangle - i|\downarrow \downarrow\rangle)/\sqrt{2}$ . This spin state is in fact created for any initial motional state  $|n\rangle$ , so long as the Lamb-Dicke criterion  $\eta^2 n \ll 1$  is satisfied.

In order for the intermediate states  $|\uparrow \downarrow 1\rangle$  and  $|\uparrow \uparrow 1\rangle$  to be negligibly occupied, the detuning  $\delta$  must be large compared to the transition linewidth  $\eta \Omega$ . However, it is clear from the expression for  $\tilde{\Omega}$  that the entanglement speed is maximized for small  $\delta$ , and in fact the technique can still be applied for  $\delta \approx \eta \Omega$  (refs 14, 16). Although motional excitation does then occur to some degree, for select values of  $\delta$  the excitation vanishes at precisely the time that the entangled spin state is created. The condition for this to occur is

$$
\delta / \eta \Omega = 2 \sqrt {m} \tag {2}
$$

for any integer  $m$ , and the maximum excitation during the pulse then has mean quantum number  $\bar{n} = 1 / 2m$ . Our experiment is operated with  $m = 1$ .

As discussed in ref. 6, the entanglement method is scalable in the sense that precisely the same operation can be used to generate the  $N$ -particle entangled state

$$
\left| \psi_ {N} \right\rangle = \left(\left| \uparrow \uparrow \dots \uparrow \right\rangle + i ^ {: N + 1} \left| \downarrow \downarrow \dots \downarrow \right\rangle\right) / \sqrt {2} \tag {3}
$$

if  $N$  is any even number, while for  $N$  odd,  $|\psi_N\rangle$  can be generated using one entanglement pulse accompanied by a separate independent rotation of each particle's spin.

If the ions are uniformly illuminated, the Mølmer and Sørensen scheme<sup>6,14</sup> requires that they all participate equally in the intermediate motional excitation, which implies that the only suitable mode for arbitrary  $N$  is the centre-of-mass mode. However, this mode has a practical disadvantage because in our experiments fluctuating ambient electric fields cause it to heat at a significant rate. Although for large  $\delta$  the entanglement operation is largely independent of the motion, so that heating is unimportant, in the small- $\delta$  case it is necessary that motional decoherence be avoided. Modes involving only relative ion motion couple to higher moments of the field, so heating of these modes is negligible<sup>15</sup>. For  $N = 2$  and  $N = 4$ , such modes do exist in which each particle participates with equal amplitude<sup>17</sup>. In both cases, they are symmetric 'stretch' modes, in which alternating ions oscillate out of

![](images/e4e9d98ae22c41e711ea9723eb9bf6e380d6e871676e82dd6ac7ac1869c41954.jpg)  
Figure 1 Entanglement scheme for two particles. Each ion is initially prepared in the  $|I\rangle$  internal state, and the collective motion of the pair is cooled to its ground state  $|0\rangle$ . Laser fields oscillating near  $\omega_0 + \nu$  and  $\omega_0 - \nu$  couple the  $|I\uparrow \rangle$  and  $|I\uparrow \rangle$  states as shown. By detuning the single transition frequencies by a small amount  $\delta$ , the populations of the  $|I\uparrow \uparrow 1\rangle$  and  $|I\uparrow \downarrow 1\rangle$  states are kept small. Then, by driving the double transition for the appropriate time, the entangled state  $(|I\uparrow \rangle - i|I\downarrow \rangle) / \sqrt{2}$  is created. For four ions, the same procedure generates the state  $(|I\uparrow \uparrow \uparrow \rangle + i|I\downarrow \downarrow \downarrow \rangle) / \sqrt{2}$ . We note that in the actual experiment, each of the single transitions shown is itself a two-photon Raman transition, driven by a pair of laser beams; the entire process therefore consists of a four-photon transition.

phase. We use these modes here. Excitation of the centre-of-mass mode still affects the experiment, as the motion in spectator modes modifies the coupling strength to the mode of interest $^{14,15}$ . For this reason, we initially cool both the centre-of-mass and stretch modes to near their ground state.

The experiment was performed using  $^9\mathrm{Be}^+$  ions confined in a miniature linear radio-frequency trap<sup>18</sup>, with the  $N$  ions lying in a line along the trap's weak axis. Two spectrally resolved ground-state hyperfine levels comprise the effective spin-half system, with  $|\downarrow\rangle \equiv |F = 2,m_F = -2\rangle$  and  $|\uparrow\rangle \equiv |F = 1,m_F = -1\rangle$ , where  $F$  is the total angular momentum quantum number, and  $\hbar m_{F}$  is the projection of the angular momentum along the quantization axis defined by an externally applied magnetic field. The hyperfine splitting  $\omega_0 / 2\pi$  is approximately  $1.25\mathrm{GHz}$ . Coherent coupling between  $|\downarrow\rangle$  and  $|\uparrow\rangle$  is provided by stimulated Raman transitions. The two Raman laser beams have a wavelength of  $313\mathrm{nm}$  with a difference frequency near  $\omega_0$ , and are perpendicular, with their difference wave-vector lying along the line of ions. They are detuned  $\sim 80\mathrm{GHz}$  blue of the  $2P_{1/2}$  excited state, with intensities giving  $\Omega / 2\pi \approx 500\mathrm{kHz}$ . For both the two- and four-ion experiments, the desired stretch-mode frequency  $\nu / 2\pi$  was  $8.8\mathrm{MHz}$ , giving  $\eta = 0.23 / N^{1/2}$ . The two driving frequencies required for the entanglement operation are generated by frequency-modulating one of the Raman beams using an electro-optic modulator.

After the entanglement operation, the ions are probed by illuminating them with a circularly polarized laser beam tuned to the  $2S_{1/2}(F = 2,m_F = -2)\leftrightarrow 2P_{3/2}(F = 3,m_F = -3)$  cycling transition. Each ion in  $|\downarrow \rangle$  fluoresces brightly, leading to the detection of  $\sim 15$  photons per ion on a photomultiplier tube during a  $200\text{-}\mu s$  detection period. In contrast, an ion in  $|\uparrow \rangle$  remains nearly dark. Because the number of photons detected from a spin-down ion fluctuates according to Poisson statistics, in a single experiment the number of spin-down ions can be determined with only a limited accuracy. For the data reported, each experiment was repeated 1,000 times under the same conditions, and the resulting photon-number distribution fitted to a sum of poissonians to determine the probabilities  $P_{j}$  for  $j$  ions to be in  $|\downarrow \rangle$ . The results are given in Table 1, and show that in both cases, the probabilities for all  $N$  ions to be in the same state are large compared to the probabilities for the other cases. This is characteristic of the states  $|\psi_N\rangle$ , although the fact that the probability of a single ion is small is not always true.

Table 1 Characterization of two-ion and four-ion states  

<table><tr><td>N</td><td>P0</td><td>P1</td><td>P2</td><td>P3</td><td>P4</td><td>ρ(Π)</td></tr><tr><td>2</td><td>0.43</td><td>0.11</td><td>0.46</td><td>-</td><td>-</td><td>0.385</td></tr><tr><td>4</td><td>0.35</td><td>0.10</td><td>0.10</td><td>0.10</td><td>0.35</td><td>0.215</td></tr></table>

$N$  is the number of ions,  $P_{i}$  denotes the probability that  $j$  ions were measured to be in  $\left|\mathbb{I}\right\rangle$ , and  $\rho_{\{\mathbb{I}\}}$  denotes the amplitude of the density matrix element  $\rho_{1\dots 1\dots 1\dots}$ . Uncertainties in  $\rho_{\{\mathbb{I}\}}$  and the  $N = 2$  populations are  $\pm 0.01$ , and uncertainties in the  $N = 4$  populations are  $\pm 0.02$ .

that the middle probabilities are non-zero indicates that we do not generate the entangled states with perfect accuracy.

In order to prove that we are generating a reasonable approximation to  $|\psi_N\rangle$ , it is necessary to prove that the populations of  $|\uparrow \dots \uparrow \rangle$  and  $|\downarrow \dots \downarrow \rangle$  are coherent. In terms of the density matrix for the system,  $\rho$ , we must measure the far off-diagonal element  $\rho_{\uparrow \dots \uparrow \downarrow \dots \downarrow}$ , whose amplitude will be abbreviated  $\rho_{(\uparrow \downarrow)}$ . This can be achieved by applying a simple analysis pulse to the ions before observing them. If the Raman difference frequency is set to  $\omega_0$  (and the frequency modulator turned off), each ion  $i$  undergoes ordinary Rabi oscillations, evolving according to the hamiltonian

$$
H _ {i} = \frac {\hbar \Omega}{2} \left(e ^ {i \phi} | \uparrow \rangle_ {i} \langle \downarrow | _ {i} + e ^ {- i \phi} | \downarrow \rangle_ {i} \langle \uparrow | _ {i}\right) \tag {4}
$$

where  $\phi$  is the phase of the difference frequency relative to that of the entanglement pulse. This hamiltonian is applied for time  $\pi /2\Omega$  (a  $\pi /2$  pulse), and the parity

$$
\varPi \equiv \sum_ {j = 0} ^ {N} (- 1) ^ {j} P _ {j} \tag {5}
$$

is observed while  $\phi$  is varied. As seen in Fig. 2, for  $N$  ions  $\Pi$  oscillates as  $\cos N\phi$ , and the amplitude of this oscillation is in fact  $2\rho_{(\uparrow \downarrow)}$  (ref. 2). The resulting values are given in Table 1. From the data shown in the table, our state preparation fidelity

$$
F \equiv \left\langle \psi_ {N} \right| \rho | \psi_ {N} \rangle = \frac {1}{2} \left(P _ {(1)} + P _ {(1)}\right) + \rho_ {(1)} \tag {6}
$$

can be determined, where  $P_{(\uparrow)}$  is the population of  $|\uparrow \dots \uparrow \rangle$  and  $P_{(\downarrow)}$  is the population of  $|\downarrow \dots \downarrow \rangle$ . For  $N = 2$  we achieve  $F = 0.83 \pm 0.01$  while for  $N = 4$ ,  $F = 0.57 \pm 0.02$ .

![](images/9e65c73b1b70a91f41a441a97d385452da109440194e3a6de4fda1bc5c3968fe.jpg)

![](images/87bb3566c80b7f30410b4057d9d44563d98d994ee929d4dea591abe520fbc54f.jpg)  
Figure 2 Determination of  $\rho_{\{\uparrow\}}$ . a, Interference signal for two ions; b, four ions. After the entanglement operation of Fig. 1, an analysis pulse with relative phase  $\phi$  is applied on the single-ion  $|\downarrow\rangle \leftrightarrow |\uparrow\rangle$  transition. As  $\phi$  is varied, the parity of the  $N$  ions oscillates as

$\cos N\phi$ , and the amplitude of the oscillation is twice the magnitude of the density-matrix element  $\rho_{(11)}$ . Each data point represents an average of 1,000 experiments, corresponding to a total integration time of roughly 10 s for each graph.

The fact that  $\rho_{\langle \mathbb{I}\rangle}$  is non-zero is still insufficient to guarantee entanglement. To be explicit, a system with density matrix  $\rho$  exhibits  $N$ -particle entanglement only if no decomposition  $\rho = \Sigma_k p_k |\psi_k\rangle \langle \psi_k|$  exists with all the  $|\psi_k\rangle$  factorizable into products of wavefunctions that depend on fewer than  $N$  particles. For example, if  $|\psi \rangle_i = (|\uparrow \rangle_i + |\downarrow \rangle_i) / \sqrt{2}$  is a state of ion  $i$ , then the four-particle state  $|\psi \rangle_1 |\psi \rangle_2 |\psi \rangle_3 |\psi \rangle_4$  is not entangled, but still has  $\rho_{\langle \mathbb{I}\rangle} = 1/16$ . We note that these are the types of states studied in liquid-state nuclear magnetic resonance experiments<sup>19</sup>. Alternatively, for  $|\psi \rangle_{12} = (|\uparrow \rangle_1 |\uparrow \rangle_2 + |\downarrow \rangle_1 |\downarrow \rangle_2) / \sqrt{2}$  and  $|\psi \rangle_{34} = (|\uparrow \rangle_3 | \uparrow \rangle_4 + |\downarrow \rangle_3 | \downarrow \rangle_4) / \sqrt{2}$ , the state  $|\psi \rangle_{12} | \psi \rangle_{34}$  exhibits two-particle, but not four-particle entanglement, and has  $\rho_{\langle \mathbb{I}\rangle} = 1/4$ .

To establish that we are actually observing  $N$ -particle entanglement, consider an arbitrary factorizable wavefunction

$$
\left| \psi_ {F} \right\rangle = [ a | \uparrow \dots \uparrow \rangle_ {X} + b | \downarrow \dots \downarrow \rangle_ {X} + \dots ] [ c | \uparrow \dots \uparrow \rangle_ {Y} + d | \downarrow \dots \downarrow \rangle_ {Y} + \dots ] \tag {7}
$$

where  $X$  and  $Y$  refer to two distinct subsets of the  $N$  particles, with  $|\uparrow \dots \uparrow \rangle_{X}$  indicating the state with all particles in subset  $X$  spin-up, and similarly for the other terms. Normalization of the factor wavefunctions requires  $|a|^2 + |b|^2 \leqslant 1$  and  $|c|^2 + |d|^2 \leqslant 1$ , which can be combined and rewritten as

$$
\left. \left(| a | - | c |\right) ^ {2} + 2 | a c | + \left(| b | - | d |\right) ^ {2} + 2 | b d | \leqslant 2 \right. \tag {8}
$$

Since the squared terms on the left are positive, equation (8) implies that  $|ac| + |bd| \leqslant 1$ , and in turn that  $(|ac| + |bd|)^2 \leqslant 1$ . Expanding the square yields the desired relation<sup>20</sup>:

$$
P _ {(\mathrm {l})} + P _ {(\mathrm {l})} + 2 \rho_ {(\mathrm {l})} = 2 F \leqslant 1 \tag {9}
$$

where  $P_{(\uparrow)} = |ac|^2$ ,  $P_{(\downarrow)} = |bd|^2$ , and  $\rho_{(\uparrow \downarrow)} = |abcd|$  are the previously defined quantities. Since equation (9) holds for any separable wavefunction, it must also hold for any separable density matrix. Both our  $N = 2$  and  $N = 4$  experiments give  $F > 1/2$ , so the states they produce exhibit  $N$ -particle entanglement.

Quantifying the amount of entanglement present is a more difficult question. A variety of measures of entanglement have been proposed, but most are difficult to calculate even numerically[21,22]. For  $N = 2$ , there is an explicit formula for the "entanglement of formation"  $E$  as a function of  $\rho$  (ref. 23). Although we have not reconstructed the entire two-particle density matrix, the populations measured place sufficient bounds on the unmeasured elements to determine that  $E \approx 0.5$ . This indicates that roughly two pairs of our ions would be required to carry the same quantum information as a single perfectly entangled pair.

In the four-ion case, no explicit formula for entanglement is known. The data do indicate that our density matrix can be expressed approximately as

$$
\rho = 0. 4 3 \left| \psi_ {4} \right\rangle \left\langle \psi_ {4} \right| + 0. 5 7 \rho_ {\text {i n c o h}} \tag {10}
$$

where  $|\psi_4\rangle$  is the desired state and  $\rho_{\mathrm{incoh}}$  is completely incoherent (that is, diagonal). These coefficients are determined directly from the value of  $\rho_{(1)}$  in Table 1, together with the fact that no evidence for other off-diagonal matrix elements was observed. To determine a measure of entanglement, however, it is necessary to decompose  $\rho$  as a sum of  $|\psi_4\rangle$  and a 'worst-case' factorizable matrix  $\rho_F$ , which can be accomplished as

$$
\rho = 0. 1 3 \left| \psi_ {4} \right\rangle \left\langle \psi_ {4} \right| + 0. 8 7 \rho_ {F}. \tag {11}
$$

Note that equations (10) and (11) both describe the same physical state, but that in equation (11),  $\rho_{F}$  consists of a specific mixture of two- and three-particle entangled states that is highly unlikely to occur in our experiments. In either description, it is clear that our state-preparation accuracy is limited.

The source of decoherence in our experiments is not entirely clear, but evidence suggests that it is related to intensity fluctuations in the Raman laser beams, a problem we are working to understand

and correct $^{24}$ . The presence of decoherence, and the fact that it affects the four-ion experiment more strongly than the two-ion one, illustrates the need to carefully define the sense in which our entanglement operation is 'scalable'. Any entanglement experiment is more sensitive to decoherence as the number of particles involved is increased, unless sufficient accuracy can be achieved for error-correction schemes to be usefully applied. Such schemes are thought to require an error rate of the order of  $10^{-4}$  per operation $^{25}$ , and we are certainly far from this regime. However, even if such a level of fidelity were to be achieved, applications such as quantum computing still require very large entangled states to be generated in a reasonable amount of time and using a reasonable amount of resources. The method demonstrated here is important in this regard, since it uses only a single operation and requires a time that scales roughly as  $N^{1/2}$ .

In the language of quantum information science, we have realized a four-quantum-bit logic gate. This system is relevant for the future development of quantum information technology, as such states may be used to implement quantum error-detection schemes[26] or to make rudimentary demonstrations of quantum algorithms[27,28]. Entanglement of four particles is also interesting in its own right, as such states can show strong violations of local realism[5]. Even the two-particle Bell's inequality measurement would be interesting to implement, as the near-perfect detection efficiency for ions would eliminate the "fair sampling" hypothesis which has been required in other experiments[29]. In addition to improved fidelity, applications such as these do require the ability to perform individual manipulation and detection of each ion, but this is not expected to be a severe experimental challenge[30].

Received 11 February; accepted 15 February 2000.

1. Bell, J. Speakable and Unspeakable in Quantum Mechanics (Cambridge Univ. Press, 1987).  
2. Bollinger, J., Itano, W. M., Wineland, D. & Heinzen, D. Optimal frequency measurements with maximally correlated states. Phys. Rev. A 54, R4649-R4652 (1996).  
3. Lo, H.-K., Popescu, S. & Spiller, T. (eds) Introduction to Quantum Computation and Information (World Scientific, Singapore, 1997).  
4. Pan, J.-W., Bouwmeester, D., Daniell, M., Weinfurter, H. & Zeilinger, A. Experimental test of quantum non-locality in three-photon Greenberger-Horne-Zeilinger entanglement. Nature 403, 515-519 (2000).  
5. Mermin, N. D. Extreme quantum entanglement in a superposition of macroscopically distinct states. Phys. Rev. Lett. 65, 1838-1840 (1990).  
6. Mølmer, K. & Sørensen, A. Multiparticle entanglement of hot trapped ions. Phys. Rev. Lett. 82, 1835-1838 (1999).  
7. Bouwmeester, D., Pan, J.-W., Daniell, M., Weinfurter, H. & Zeilinger, A. Observation of three-photon Greenberger-Horne-Zeilinger entanglement. Phys. Rev. Lett. 82, 1345-1349 (1999).  
8. Kwiat, P. et al. New high-intensity source of polarization-entangled photon pairs. Phys. Rev. Lett. 75, 4337-4341 (1995).  
9. Tittle, W., Brendel, J., Zbinden, H. & Gisin, N. Violation of Bell inequalities by photons more than  $10\mathrm{km}$  apart. Phys. Rev. Lett. 81, 3565-3566 (1998).  
10. Hagley, E. et al. Generation of Einstein-Podolsky-Rosen pairs of atoms. Phys. Rev. Lett. 79, 1-5 (1997).  
11. Cirac, J. & Zoller, P. Quantum computations with cold trapped ions. Phys. Rev. Lett. 74, 4091-4094 (1995).  
12. Turchette, Q. et al. Deterministic entanglement of two trapped ions. Phys. Rev. Lett. 81, 3631-3634 (1998).  
13. Law, C. & Kimble, J. Deterministic generation of a bit-stream of single-photon pulses. J. Mod. Opt. 44, 2067-2074 (1997).  
14. Mølmer, K. & Sørensen, A. Entanglement and quantum computation with ions in thermal motion. Pre-print quant-ph/0002024 at  $\langle \mathrm{xxx.lanl.gov}\rangle$  (2000).  
15. King, B. et al. Cooling the collective motion of trapped ions to initialize a quantum register. Phys. Rev. Lett. 81, 1525-2528 (1998).  
16. Milburn, G. Simulating nonlinear spin models in an ion trap. Pre-print quant-ph/9908037 at  $\langle \mathrm{xxx.lanl.gov}\rangle$  (1999).  
17. James, D. Quantum dynamics of cold trapped ions with applications to quantum computation. Appl. Phys. B 66, 181-190 (1998).  
18. Turchette, Q. et al. Heating of trapped ions from the quantum ground state. Pre-print quant-ph/0002040 at  $\langle \mathrm{xxx.lanl.gov}\rangle$  (2000).  
19. Fitzgerald, R. What really gives a quantum computer its power? Phys. Today 53, 20-22 (2000).  
20. Bennett, C. et al. Purification of noisy entanglement and faithful teleportation via noisy channels. Phys. Rev. Lett. 76, 722-725 (1996).  
21. Vedral, V., Plenio, M., Rippin, M. & Knight, P. Quantifying entanglement. Phys. Rev. Lett. 78, 2275-2279 (1997).  
22. Lewenstein, M. & Sanpera, A. Separability and entanglement of composite quantum systems. Phys. Rev. Lett. 80, 2261-2264 (1998).  
23. Wootters, W. K. Entanglement of formation of an arbitrary state of two qubits. Phys. Rev. Lett. 80, 2245-2248 (1998).  
24. Wineland, D. et al. Experimental issues in coherent quantum-state manipulation of trapped atomic ions. J. Res. NIST 103, 259-328 (1998).

25. Preskill, J. Battling decoherence: the fault tolerant quantum computer. Phys. Today 52, 24-30 (1999).  
26. Vaidman, L., Goldenberg, L. & Wiesner, S. Error prevention scheme with four particles. Phys. Rev. A 54, R1745–R1748 (1996).  
27. Shor, P. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM J. Comput. 26, 1484-1509 (1997).  
28. Grover, L. Quantum mechanics helps in searching for a needle in a haystack. Phys. Rev. Lett. 79, 325-328 (1997).  
29. Eberhard, P. Background level and counter efficiencies required for a loophole-free Einstein-Podolsky-Rosen experiment. Phys. Rev. A 47, R747–R750 (1993).  
30. Nagerl, H. et al. Laser addressing of individual ions in a linear ion trap. Phys. Rev. A 60, 145-148 (1999).

# Acknowledgements

We thank J. Bollinger and E. A. Cornell for comments on the manuscript. This work was supported by the US National Security Agency, Army Research Office and Office of Naval Research.

Correspondence and requests for materials should be addressed to C. M. (e-mail: monroe@boulder.nist.gov).

# Quantum distribution of protons in solid molecular hydrogen at megabar pressures

Hikaru Kitamura\*, Shinji Tsuneyuki\*, Tadashi Ogitsu\* & Takashi Miyake

* Institute for Solid State Physics, University of Tokyo, Ropponji, Tokyo 106-8666, Japan  
† Department of Space Physics and Astronomy, Rice University, Houston, Texas 77251-1892, USA  
$\ddagger$  Applied Theoretical and Computational Physics Division, Los Alamos National Laboratory, Los Alamos, New Mexico 87545, USA  
$\S$  National Center for Supercomputing Applications, University of Illinois at Urbana-Champaign, Urbana, Illinois 61801, USA  
$\parallel$  Joint Research Center for Atom Technology, Tsukuba, Ibaraki 305-0046, Japan

Solid hydrogen, a simple system consisting only of protons and electrons, exhibits a variety of structural phase transitions at high pressures. Experimental studies<sup>1</sup> based on static compression up to about 230 GPa revealed three relevant phases of solid molecular hydrogen: phase I (high-temperature, low-pressure phase), phase II (low-temperature phase) and phase III (high-pressure phase). Spectroscopic data suggest that symmetry breaking, possibly related to orientational ordering<sup>1,2</sup>, accompanies the transition into phases II and III. The boundaries dividing the three phases exhibit a strong isotope effect<sup>3</sup>, indicating that the quantum-mechanical properties of hydrogen nuclei are important. Here we report the quantum distributions of protons in the three phases of solid hydrogen, obtained by a first-principles path-integral molecular dynamics method. We show that quantum fluctuations of protons effectively hinder molecular rotation—that is, a quantum localization occurs. The obtained crystal structures have entirely different symmetries from those predicted by the conventional simulations which treat protons classically.

The structures of these broken-symmetry phases have been extensively investigated both by experimental $^{1-3}$  and by theoretical $^{4-9}$  studies, though the results are still controversial. In most theoretical studies, even when they precisely compare total energies of model structures on the basis of electronic-structure calculations, quantum fluctuations of protons are usually neglected, or roughly discussed, perhaps due to some technical reason. But as shown by our previous study on impurity muonium (a bound state comprising

a positive muon and an electron) and hydrogen in crystalline silicon $^{10}$ , quantum states of light particles may exhibit distributions significantly different from those expected from stability analyses based on the classical potential-energy surface. It is therefore desirable to examine quantitatively the quantum-mechanical properties of protons in solid hydrogen, especially when we are concerned with its symmetry breaking under high pressure. Natoli et al. $^{11}$  treated both electrons and protons with quantum Monte Carlo methods; their simulations were, however, performed with trial wavefunctions based on the fixed static configuration of the protons, and were restricted to the molecules centred on the hexagonal close packed (h.c.p.) lattice sites.

The first-principles path-integral molecular dynamics (FP-PIMD) method enables us to incorporate quantum-mechanical properties of protons in conventional Car-Parrinello-type first-principles simulations. The basic formalism was first presented by Marx and Parrinello $^{12}$ . Recently this scheme was further developed by the present authors $^{10}$ , and we use this in the present study. We consider a supercell containing  $N (= 64)$  atoms, which is subject to the periodic boundary conditions. To represent the quantum properties of protons in the path-integral formalism, imaginary time  $\beta \hbar$  (where  $\beta$  is the inverse temperature in units of Boltzmann constant) is divided into  $P$  finite time slices; each proton is thus represented by a polymer consisting of  $P$  'beads' interacting via intrapolymeric harmonic forces $^{13}$ . Exchange effects between protons are neglected in this study. Assuming the Born-Oppenheimer approximation, interatomic forces between protons at each atomic configuration and at each time slice are determined by electronic-structure calculation based on the density-functional theory (DFT). The resultant classical system of  $NP$  particles is simulated by molecular dynamics (MD) at constant volume and temperature with the aid of the Nosé-Hoover chain thermostat $^{14}$ . In the evaluation of the exchange-correlation potential in the DFT calculation, we adopt the generalized gradient approximation (GGA) $^{15}$ . The interaction between a proton and an electron has been described by the norm-conserving non-local pseudopotential of the Troullier-Martins type $^{16}$ ; the electronic wavefunctions have been expanded in plane waves with a cut-off energy of  $50\mathrm{Ry}$ . Integration over the first Brillouin zone has been achieved by sampling 8 uniform  $k$ -points. Energy eigenvalues of the lowest 32 occupied bands have been explicitly calculated, since the system should remain an insulator in the relevant pressure range $^{1}$ . The ground-state electron density has been obtained by minimizing the total energy functional through the conjugated-gradient method $^{17}$ . We have verified, through static DFT calculations with these parameter conditions, that the potential energy surface associated with molecular rotation in the  $Pca2_{1}$  structure obtained earlier by

![](images/c348dd4b18f62a1ffd87f40fa0eb743187fb1af44f92f67bf7b0affb4c9f2dd8.jpg)  
Figure 1 Illustration of the  $Pca2_{1}$  structure projected onto the  $x - y$  plane. Thick arrows represent molecules on the  $\alpha$ -plane and thin arrows depict those on the  $\beta$ -plane, both pointing towards the positive- $z$  hemisphere. These two planes are apart from each other by  $c / 2$  in the  $z$ -direction. The quantity  $\theta$  measures the angle between a molecular axis and the  $c(z)$ -axis of the crystal:  $\varphi$  is the corresponding azimuthal angle. The  $Cmc2_{1}$  structure is obtained by setting  $\varphi = 90^{\circ}$ .