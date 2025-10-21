# Quantum tomography of an entangled three-qubit state in silicon

Kenta Takeda $^{1}$ , Akito Noiri $^{1}$ , Takashi Nakajima $^{1}$ , Jun Yoneda $^{1,2}$ , Takashi Kobayashi $^{1}$  and Seigo Tarucha $^{1}$

Quantum entanglement is a fundamental property of coherent quantum states and an essential resource for quantum computing<sup>1</sup>. In large-scale quantum systems, the error accumulation requires concepts for quantum error correction. A first step toward error correction is the creation of genuinely multipartite entanglement, which has served as a performance benchmark for quantum computing platforms such as superconducting circuits<sup>2,3</sup>, trapped ions<sup>4</sup> and nitrogen-vacancy centres in diamond<sup>5</sup>. Among the candidates for large-scale quantum computing devices, silicon-based spin qubits offer an outstanding nanofabrication capability for scaling-up. Recent studies demonstrated improved coherence times<sup>6-8</sup>, high-fidelity all-electrical control<sup>9-13</sup>, high-temperature operation<sup>14,15</sup> and quantum entanglement of two spin qubits<sup>9,11,12</sup>. Here we generated a three-qubit Greenberger-Horne-Zeilinger state using a low-disorder, fully controllable array of three spin qubits in silicon. We performed quantum state tomography<sup>16</sup> and obtained a state fidelity of  $88.0\%$ . The measurements witness a genuine Greenberger-Horne-Zeilinger class quantum entanglement that cannot be separated into any biseparable state. Our results showcase the potential of silicon-based spin qubit platforms for multiquubit quantum algorithms.

Silicon-based quantum dots are promising candidates for quantum computing hardware due to their great potential for high-density integration using semiconductor nanofabrication technologies $^{17,18}$ . For the single electron spins in silicon, key ingredients, such as single-qubit gate fidelities that exceed  $99.9\%$  (refs. $^{10,13}$ ), a two-qubit gate fidelity of about  $98\%$  (ref. $^{12}$ ), quantum non-demolition measurement $^{19,20}$  and high-temperature operation $^{14,15}$ , have been demonstrated. To create and characterize a genuine multiqubit entangled state, high-fidelity initialization, measurement and one-and two-qubit control must be properly combined in a single multiqubit device. Previously, control of four-spin states was performed in a gallium arsenide device $^{21}$ , but the device lacked the capability of single-spin manipulation. In silicon, a nine-quantum-dot array was realized using a low-disorder silicon/silicon-germanium (Si/SiGe) heterostructure $^{22}$ , but universal coherent manipulation was performed for only one- and two-spin states $^{9,11,12}$ . Now, it is crucial to demonstrate the capability of extending the size of quantum entanglement toward scaling up silicon-based quantum computing.

Our three-qubit device is a triple quantum dot fabricated on an isotopically natural Si/SiGe heterostructure wafer (Fig. 1b and Methods). Nanofabricated overlapping aluminium gates $^{23}$  are used to control the triple-quantum-dot confinement potential (Fig. 1a). Each quantum dot is configured to host one electron (Fig. 1c) and

its spin-up and -down states are used to encode a spin qubit (Fig. 1b,  $\mathrm{Q}_1$  to  $\mathrm{Q}_3$  from left to right). An in-plane external magnetic field of  $B_{\mathrm{ext}} = 0.5275\mathrm{T}$  is applied to create a Zeeman splitting ( $\sim 18\mathrm{GHz}$ ) much larger than the thermal broadening of the nearby electron reservoir ( $\sim 40\mathrm{mK}$ ). This enables the initialization and measurement of the spin qubits ( $\mathrm{Q}_1$  and  $\mathrm{Q}_3$ ) with neighbouring electron reservoirs via energy-selective tunnelling[24] (see Fig. 1c for the bias configuration). The middle spin qubit ( $\mathrm{Q}_2$ ), which does not directly couple to any reservoir, can be initialized and measured by the combinations of a resonant SWAP gate[25,26] and energy-selective tunnelling (see Extended Data Fig. 1 for the details). With this initialization and measurement procedure, we obtained high initialization fidelities ( $>99\%$  for all qubits) and readout fidelities of  $F_1^{\mathrm{M}} = 87.9\%$  ( $\mathrm{Q}_1$ ),  $F_2^{\mathrm{M}} = 82.9\%$  ( $\mathrm{Q}_2$ ) and  $F_3^{\mathrm{M}} = 89.9\%$  ( $\mathrm{Q}_3$ ).

The single-qubit control is performed by electric-dipole spin resonance. A magnetic field gradient created by a cobalt micromagnet placed on top of the quantum dot array enables a fast and addressable single-qubit control[27]. To demonstrate this, we measured the Rabi chevron patterns for the three spin qubits (Fig. 2a-c). The resonance frequencies of the three qubits were separated by  $\delta E_{12} \sim 435.4\mathrm{MHz}$  (between  $\mathrm{Q}_1$  and  $\mathrm{Q}_2$ ) and  $\delta E_{23} \sim 523.2\mathrm{MHz}$  (between  $\mathrm{Q}_2$  and  $\mathrm{Q}_3$ ) due to the micromagnet field gradient[9,11,19,26,28]. These large separations ensure that our single-qubit drive (with  $f_{\mathrm{Rabi}} = 6\mathrm{MHz}$ ) does not rotate the other spins. We then characterized the  $T_1$  relaxation times,  $T_2^*$  inhomogeneous dephasing times and  $T_2^{\mathrm{echo}}$  Hahn echo times (Extended Data Fig. 2). We found that  $T_1 = 4.30 \pm 0.08\mathrm{ms}$  ( $\mathrm{Q}_1$ ),  $2.67 \pm 0.09\mathrm{ms}$  ( $\mathrm{Q}_2$ ) and  $1.31 \pm 0.02\mathrm{ms}$  ( $\mathrm{Q}_3$ ), which are long enough to perform single-shot spin readout, but shorter than those typically expected for electron spins in silicon, probably due to spin-valley mixing[29]. The dephasing times of  $T_2^* = 1.82 \pm 0.08\mu\mathrm{s}$  ( $\mathrm{Q}_1$ ),  $1.69 \pm 0.08\mu\mathrm{s}$  ( $\mathrm{Q}_2$ ) and  $1.69 \pm 0.04\mu\mathrm{s}$  ( $\mathrm{Q}_3$ ) are similar to those reported for natural silicon spin-1/2 qubits[9,11,28] and are most probably limited by the fluctuation of  $4.7\%$  [29] Si nuclear spins in natural silicon. Hahn echo extends the dephasing times to  $T_2^{\mathrm{echo}} = 28.1 \pm 0.8\mu\mathrm{s}$  ( $\mathrm{Q}_1$ ),  $20.5 \pm 0.2\mu\mathrm{s}$  ( $\mathrm{Q}_2$ ) and  $45.8 \pm 0.4\mu\mathrm{s}$  ( $\mathrm{Q}_3$ ). The average single-qubit fidelities were examined through the Clifford-based randomized benchmarking[30] and found to be  $99.43 \pm 0.01\%$  ( $\mathrm{Q}_1$ ),  $99.57 \pm 0.01\%$  ( $\mathrm{Q}_2$ ) and  $99.91 \pm 0.004\%$  ( $\mathrm{Q}_3$ ) (Fig. 2d-f; see Methods and Extended Data Fig. 3 for details of randomized benchmarking implementation). We note that these fidelities were measured with all the qubits initialized to spin-down. The single-qubit control for multiqubit input states, however, can be degraded by the residual exchange interactions unless they are low enough compared to  $f_{\mathrm{Rabi}}$ . In this experiment, the residual exchange was relatively large between  $\mathrm{Q}_2$  and  $\mathrm{Q}_3$ , which resulted in a reduction of the single-qubit gate fidelities of  $\mathrm{Q}_2$  ( $\mathrm{Q}_3$ ) by  $\sim 0.6$  (0.5)%

![](images/fd75c287edf7c5ae0e6843c9bc3391a83cfd44b8c16c3c7c54fade35818c8567.jpg)

![](images/eb6156b0e2b966066ee8dffe4d18d7a6541af43bfb0dc58d155536136a9e3c16.jpg)  
Fig. 1 | Device and experimental setup. a, False-coloured scanning electron microscope image of the device. Scale bar,  $100\mathrm{nm}$ . Three layers of overlapping aluminium gates are fabricated on top of a Si/SiGe heterostructure wafer. The plunger (green) and barrier (purple) gates are used to control the confinement potential and accumulate the reservoirs. The screening gates (ochre) restrict the electric field of the plunger and barrier gates. The lower channel is used as a triple-quantum-dot array and the upper channel is used as a charge sensor. Gates P1, P2, P3, B2 and B3 are connected to high-bandwidth coaxial cables to apply fast voltage pulses. The microwave pulses are applied to the lower screening gate. b, Cross-sectional schematic of the device. The black solid line in the silicon quantum well (Si QW) illustrates the triple-quantum-dot confinement potential. c, Charge stability diagram with the exchange interactions turned off. The colour plot shows the demodulated voltage of the radio-frequency sensor quantum dot as a function of the voltages applied to the P1 and P3 gates. Kinks appear when the charge occupation of the triple quantum dot  $(n_{1}n_{2}n_{3})$  changes, where  $n_1,n_2$  and  $n_3$  are the respective numbers of electrons in the left, middle and right quantum dots. The background signal variation is due to the sensor dot Coulomb oscillation.

![](images/14062392e0c0d307e7e2a098d2bbcd3e12ef405da0405e62748afacd2c9b19d1.jpg)  
$\mathbb{Q}_1$  readout/initialization point  
Q2 and Q3 readout/initialization point  
$\bullet$  Single-qubit manipulation point

(see Methods and Extended Data Fig. 4 for the details). Nevertheless, these fidelities were high enough to perform the quantum state tomography measurements.

To create the quantum entanglement, we utilized controlled phase (CZ) gates between the neighbouring spin qubits. The exchange interaction  $J_{ij}$  between the neighbouring spin qubits  $Q_{i}$  and  $Q_{j}$  acts as an effective Ising type interaction  $(hJ_{ij}' / 4)\sigma_z^i\otimes \sigma_z^j$  under the large micromagnet local Zeeman gradient  $\delta E_{ij}$ , where  $J_{ij}' = \sqrt{J_{ij}^2 + (\delta E_{ij})^2} -\delta E_{ij}$  and  $h$  is Planck's constant[31]. The time evolution under this interaction for a period of  $(2J_{ij}')^{-1}$  is equivalent to a CZ gate between  $Q_{i}$  and  $Q_{j}$ $(CZ_{ij})$  up to local single-qubit phases. The single-qubit phases can be compensated by single-qubit Z rotations, which we implement by shifting the reference phase of any subsequent microwave pulses in the software. To control  $J_{12}'(J_{23}')$  in the time domain, we utilized fast gate voltage pulses applied on the B2 (B3) gate (Fig. 1b). When turned on,  $J_{12}'$  and  $J_{23}'$  are nominally 2.8 and 12.5 MHz, respectively (Extended Data Fig. 5a-d). Additional linear compensations were applied to the plunger gates P1, P2 and P3 to keep the triple-dot charge configuration near the symmetric operation point (Methods). At this point, the charge-noise-induced dephasing was minimized as  $J_{ij}'$  became first-order insensitive to detuning fluctuations[32,33].

We combined the single-qubit and CZ gates to perform a three-qubit entangling operation. Although three qubits can be entangled simply by sequentially applying CZ gates between neighbouring qubits  $(\mathrm{CZ}_{12}$  and  $\mathrm{CZ}_{23})$ , as demonstrated in other systems[2,3,34], the qubits are vulnerable to low-frequency noise during manipulation. To fully leverage the long intrinsic phase coherence times of spins, we implemented a decoupled three-qubit entangling operation by extending a decoupled CZ gate[11] to a three-qubit system (Fig. 2g). In this sequence, the CZ gates are separated into CZ/2

gates with  $\pi$  pulses inserted in the middle, where the CZ/2 gate is defined as  $\mathrm{diag}(1,1,1,i)$ . As in the standard Hahn echo experiments, the  $\pi$  pulses reverse the non-conditional phase accumulation during free evolution, and therefore decouple the quasi-static single-qubit phase noise (for example, the low-frequency nuclear magnetic and charge noises and the local phase accumulated by the CZ pulses). The action of our three-qubit operation was measured by the quantum gate sequence shown in Fig. 2g.  $Q_{2}$  was used as a control qubit and the phase of the second  $\pi /2$  pulse  $(\phi)$  was varied to detect the phase accumulation on  $Q_{1}$  and  $Q_{3}$ . Figure 2h,i shows the spin-up probabilities of  $Q_{1}$  and  $Q_{3}$ , respectively, measured as a function of  $\phi$ . The additional Z rotations at the end were required to adjust the additional phases that originated from the  $\pi$  pulses. The exchange pulse durations were tuned up so that the conditional phase accumulation was  $\sim \pi$ . The phases are typically calibrated to within  $\pm 0.01\pi$  from the target values. As a benchmark of our CZ gate quality, we measured the fidelities of two-qubit Bell states using  $Q_{2}$  and  $Q_{3}$ . We obtained an average Bell state fidelity of  $94.1\%$  and concurrence of 0.929 (Extended Data Fig. 6), which compare favourably to the values previously reported in other silicon quantum-dot-based qubit devices (fidelities of  $78 - 89\%$  and concurrences of 0.73–0.82 (refs. 9,11,12)). The result indicates that our CZ gate fidelity is reasonably high, although further assessment using two-qubit Clifford-based randomized benchmarking is necessary to extract the CZ gate fidelity, which remains for future study.

Now we turn to the generation of three-qubit entanglement. Figure 3a shows our quantum gate sequence to generate a three-qubit GHZ state  $|\mathrm{GHZ}\rangle = (|\uparrow \uparrow \uparrow \rangle + |\downarrow \downarrow \downarrow \rangle) / \sqrt{2}$ . The sequence is similar to that in Fig. 2g, but with the first rotation on  $\mathbf{Q}_2$  replaced with a Y/2 gate and the other X (X/2) gates replaced with Y (Y/2) gates. After the state preparation, we applied a single-qubit pre-rotation (I,X/2,Y/2) on each qubit to rotate the measurement

![](images/e513cb311a3e71a7ebf9fd0da58e4f5b004ae3a79b5e981bc59f5f2d13931689.jpg)

![](images/22cb0a6ce5d036b4ae8171cca9e5bf805d71ad319d0fcfccb7bab09273271ec2.jpg)

![](images/c22c6778edec38c6eafb3487fd5adaf1de8eca09e736a4ff7506068ae7565f9b.jpg)

![](images/72f25599e668d38319f84a9e16d8ea18866546b56fae9153b70e75f60f959712.jpg)

![](images/046ec2cf579aa49b9021e88179d3cc4b8d8cddb626b424d2701d515a7f43ea65.jpg)

![](images/3caee95b78a2908d4ee3a09a8b8a3323e164f6a6314c4bed01b1a71a8a74384d.jpg)

![](images/bafd4071ddbfcb37935e19483367c26d8fec3a8811b6e7cf2f8a1071c375ad23.jpg)

![](images/8966c83f1b0e2b9145391276fd5b4a94eddfe2d08e96037bb84380cff4ec04a1.jpg)  
Fig. 2 | Single-qubit and controlled phase operations. All the qubits were initialized to spin-down before the manipulation stage. a-c, Single-qubit Rabi chevron patterns of each qubit. Each spin state was read out right after the manipulation stage without a sequential readout for the three spins. The frequency offsets are 17,789.15 MHz  $(Q_{1})$  (a), 18,224.5 MHz  $(Q_{2})$  (b) and 18,747.7 MHz  $(Q_{3})$  (c). d-f, Single-qubit randomized benchmarking results for each qubit. The visibilities were 0.894, 0.746 and 0.794 for  $Q_{1}(\mathbf{d})$ ,  $Q_{2}(\mathbf{e})$  and  $Q_{3}(\mathbf{f})$ . For each data point, we averaged over 16 random Clifford sequences. The errors represent the estimated standard errors for the best-fit values. g, Quantum gate sequence used to tune up the decoupled CZ gates that target both qubits  $Q_{1}$  and  $Q_{3}$ . A similar gate sequence, but with the target and control qubits swapped, was used to tune up the unconditional phase accumulated on  $Q_{2}$  during the exchange pulses. X (X/2) denotes a  $\pi$  ( $\pi/2$ ) rotation around the x axis and the rotations around the y and z axes are defined in a similar manner.  $\phi/2$  indicates a  $\pi/2$  rotation around an axis in the xy plane—when  $\phi = 0$  ( $0.5\pi$ ), it is around the x (y) axis. h,i, Measured  $Q_{1}$  and  $Q_{3}$  spin-up probabilities for two different control bit states of  $Q_{2}$ . The filled (open) circles represent the result when  $Q_{2}$  is spin-down (up). The solid lines are the sinusoidal fitting curves. From the phase offsets of the sinusoids, we obtained the conditional phase shifts of  $(1.004 \pm 0.005)\pi$  radian for  $Q_{1}$  and  $(1.003 \pm 0.004)\pi$  radian for  $Q_{3}$ . Note that we also applied a small ( $< 0.1\pi$ ) phase correction to each qubit to account for the imperfect cancellation of the non-conditional phase accumulation during the echo sequence. The errors represent the estimated standard errors for the best-fit values.

![](images/3d2fa9f167317e3e9c582f5d021ba9c0303a880e661c690c700c3a28a8225646.jpg)

![](images/db97ff1b0cd8bb460f00483213322cfcfffacbc324ea49ab206af51b9b62af39.jpg)

![](images/22f1b89bc14a105525ddbd5d9cdd0ec3b72a98beedf209e51fbe68052350df8d.jpg)  
Fig. 3 | Three-qubit entanglement generation and measurement. a, Quantum gate sequence used for the GHZ state generation and measurement. It is similar to the double CZ sequence in Fig. 2g. The key difference is that the first control pulse for  $Q_{2}$  is replaced with a Y/2 pulse to prepare a superposition state. In addition, the X pulses are replaced with the Y pulses to obtain a final state with the desired phase components. b, Real part of the measured density matrix in the computational basis. The imaginary part can be found in Extended Data Fig. 7. The error represents one sigma from the mean. c, Measured expectation values for Pauli operators. An obvious expectation value,  $\langle \mathrm{III}\rangle = 1$ , is omitted in the plot. The open boxes represent the expectation values for an ideal three-qubit GHZ state (0, 1 or -1).

![](images/84aa5ff56cbbf710e46f7d2a55483215937525376df0e20bd2a63dea3196610d.jpg)

axis. For each of the 27 combinations of pre-rotations, we averaged 2,000 single-shot readout outcomes to obtain the eight probabilities projected to the computational basis. The measurement errors were removed by correcting the obtained probabilities based on the spin-up and -down readout fidelities (Methods). We reconstructed a density matrix  $\rho$  using a maximum likelihood estimation so that  $\rho$  is a physical, that is, Hermitian, positive-semidefinite and unit trace (Methods). Figure 3b shows the real part of the measured density matrix  $\mathrm{Re}(\rho)$  in the computational basis (see Extended Data Fig. 7 for the imaginary part). As expected for a GHZ state, there are four peaks at the corners. Figure 3c shows the expectation values for non-trivial 63 Pauli operators, which are also in a good agreement with the ideal GHZ state shown as the open black boxes. By comparing the measured state with the ideal one, we obtained a state fidelity of  $F_{\mathrm{GHZ}} = \langle \mathrm{GHZ}|\rho |\mathrm{GHZ}\rangle = 0.880\pm 0.007$ , which is comparable with the value obtained in the first demonstration in a superconducting transmon three-qubit device and high enough to test quantum algorithms[35,36].

To understand the properties of the generated state, we evaluated entanglement witness operators. The measured state fidelity is useful to distinguish two types of maximally entangled three-qubit states, the GHZ-class and W-class states. Only the GHZ-class state becomes completely separable after loss and/or measurement of one-qubit information, and therefore is a useful type for quantum error correction. Our measured state strictly belongs to the GHZ-class because any W-class state  $\rho_{\mathrm{W}}$  satisfies  $\langle \mathrm{GHZ}|\rho_{\mathrm{W}}|\mathrm{GHZ}\rangle \leq 0.75$ . To further infer the degree of the generated three-qubit entanglement, we evaluated a witness function  $M = \langle \mathrm{XXX}\rangle -\langle \mathrm{XYY}\rangle -\langle \mathrm{YXY}\rangle -\langle \mathrm{YYX}\rangle$ , which satisfies the Mermin-Bell inequality  $|M|\leq 2$ , for any biseparable states[37]. We measured  $M = 3.47\pm 0.05$ , which violates the inequality by more than 28 standard deviations. The violation requires the readout error removal, but it is, nonetheless, an important indication of a three-qubit entanglement.

We believe that there is still room to enhance the state fidelity by efforts to improve the quantum gates. The obtained state fidelity is comparably limited by the eight single-qubit and four CZ/2 gates in the GHZ-state generation protocol in Fig. 3a. Although the single-qubit gates are expected to have higher fidelities  $(> - 99\%)$  than

the CZ gates, they will have a non-negligible contribution to the measured state infidelity of  $12\%$ . In Fig. 2d-f, the single-qubit gate fidelities are limited by the nuclear spin fluctuations in the isotopically natural silicon quantum well and can be improved by using an isotopically enriched  ${}^{28}\mathrm{Si} / \mathrm{SiGe}$  material[10]. In contrast, improvement of the decoupled CZ gate fidelity will require the reduction of charge noise, which may be possible with optimization of the device structure[38].

In conclusion, we show the operation of a three-qubit device in silicon and performed the generation and measurement of a three-qubit GHZ state. We implemented a high-fidelity, individual electrical control of three spin qubits using an on-chip micromagnet. Furthermore, we utilized a combination of barrier-controlled exchange and decoupling pulses to implement high-fidelity two-qubit CZ gates. We then combined the single- and two-qubit gates with a three-spin initialization and measurement to generate a three-qubit GHZ state. The generated state was fully characterized by quantum-state tomography and confirmed to have properties of a genuine three-qubit GHZ-class entanglement. We anticipate that our results will enable the exploration of multispin correlations and demonstration of multiqubit algorithms, such as quantum error correction in scalable silicon-based quantum computing devices.

During the completion of this Letter, we became aware of a related experiment that demonstrates control and measurement of a germanium-based four-spin qubit device<sup>39</sup>.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41565-021-00925-0.

Received: 29 November 2020; Accepted: 30 April 2021; Published online: 7 June 2021

# References

1. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).

2. Dicarlo, L. et al. Preparation and measurement of three-qubit entanglement in a superconducting circuit. Nature 467, 574-578 (2010).  
3. Neeley, M. et al. Generation of three-qubit entangled states using superconducting phase qubits. Nature 467, 570-573 (2010).  
4. Häffner, H. et al. Scalable multiparticle entanglement of trapped ions. Nature 438, 643-646 (2005).  
5. Neumann, P. et al. Multipartite entanglement among single spins in diamond. Science 323, 1326-1330 (2009).  
6. Pla, J. J. et al. A single-atom electron spin qubit in silicon. Nature 489, 541-544 (2012).  
7. Pla, J. J. et al. High-fidelity readout and control of a nuclear spin qubit in silicon. Nature 496, 334-338 (2013).  
8. Veldhorst, M. et al. An addressable quantum dot qubit with fault-tolerant control-fidelity. Nat. Nanotechnol. 9, 981-985 (2014).  
9. Zajac, D. M. et al. Resonantly driven CNOT gate for electron spins. Science 359, 439-442 (2018).  
10. Yoneda, J. et al. A quantum-dot spin qubit with coherence limited by charge noise and fidelity higher than  $99.9\%$ . Nat. Nanotechnol. 13, 102-106 (2018).  
11. Watson, T. F. et al. A programmable two-qubit quantum processor in silicon. Nature 555, 633-637 (2018).  
12. Huang, W. et al. Fidelity benchmarks for two-qubit gates in silicon. Nature 569, 532-536 (2019).  
13. Yang, C. H. et al. Silicon qubit fidelities approaching incoherent noise limits via pulse engineering. Nat. Electron. 2, 151-158 (2019).  
14. Yang, C. H. et al. Silicon quantum processor unit cell operation above one Kelvin. Nature 580, 350-354 (2020).  
15. Petit, L. et al. Universal quantum logic in hot silicon qubits. Nature 580, 355-359 (2020).  
16. James, D. F. V., Kwiat, P. G., Munro, W. J. & White, A. G. Measurement of qubits. Phys. Rev. A 64, 052312 (2001).  
17. Vandersypen, L. M. K. et al. Interfacing spin qubits in quantum dots and donors—hot, dense, and coherent. npj Quantum Inf. 3, 34 (2017).  
18. Veldhorst, M., Eenink, H. G. J., Yang, C. H. & Dzurak, A. S. Silicon CMOS architecture for a spin-based quantum computer. Nat. Commun. 8, 1766 (2017).  
19. Yoneda, J. et al. Quantum non-demolition readout of an electron spin in silicon. Nat. Commun. 11, 1144 (2020).  
20. Xue, X. et al. Repetitive quantum non-demolition measurement and soft decoding of a silicon spin qubit. Phys. Rev. X 10, 021006 (2020).  
21. Qiao, H. et al. Coherent multi-spin exchange coupling in a quantum-dot spin chain. Phys. Rev. X 10, 31006 (2020).  
22. Zajac, D. M., Hazard, T. M., Mi, X., Nielsen, E. & Petta, J. R. Scalable gate architecture for densely packed semiconductor spin qubits. Phys. Rev. Appl. 6, 054013 (2016).

23. Angus, S. J., Ferguson, A. J., Dzurak, A. S. & Clark, R. G. Gate-defined quantum dots in intrinsic silicon. Nano Lett. 7, 2051-2055 (2007).  
24. Elzerman, J. M. et al. Single-shot read-out of an individual electron spin in a quantum dot. Nature 430, 431-435 (2004).  
25. Sigillito, A. J., Gullans, M. J., Edge, L. F., Borselli, M. & Petta, J. R. Coherent transfer of quantum information in silicon using resonant SWAP gates. npj Quantum Inf. 5, 110 (2019).  
26. Takeda, K., Noiri, A., Yoneda, J., Nakajima, T. & Tarucha, S. Resonantly driven singlet-triplet spin qubit in silicon. Phys. Rev. Lett. 124, 117701 (2020).  
27. Tokura, Y., Van Der Wiel, W. G., Obata, T. & Tarucha, S. Coherent single electron spin control in a slanting Zeeman field. Phys. Rev. Lett. 96, 047202 (2006).  
28. Takeda, K. et al. A fault-tolerant addressable spin qubit in a natural silicon quantum dot. Sci. Adv. 2, e1600694 (2016).  
29. Borjans, F., Zajac, D. M., Hazard, T. M. & Petta, J. R. Single-spin relaxation in a synthetic spin-orbit field. Phys. Rev. Appl. 11, 044063 (2018).  
30. Knill, E. et al. Randomized benchmarking of quantum gates. Phys. Rev. A 77, 012307 (2008).  
31. Meunier, T., Calado, V. E. & Vandersypen, L. M. K. Efficient controlled-phase gate for single-spin qubits in quantum dots. Phys. Rev. B 83, 121403(R) (2011).  
32. Martins, F. et al. Noise suppression using symmetric exchange gates in spin qubits. Phys. Rev. Lett. 116, 116801 (2016).  
33. Reed, M. D. et al. Reduced sensitivity to charge noise in semiconductor spin qubits via symmetric operation. Phys. Rev. Lett. 116, 110402 (2016).  
34. Barends, R. et al. Superconducting quantum circuits at the surface code threshold for fault tolerance. Nature 508, 500-503 (2014).  
35. Reed, M. D. et al. Realization of three-qubit quantum error correction with superconducting circuits. Nature 482, 382-385 (2012).  
36. Kelly, J. et al. State preservation by repetitive error detection in a superconducting quantum circuit. Nature 519, 66-69 (2015).  
37. Mermin, N. D. Extreme quantum entanglement in a superposition of macroscopically distinct states. Phys. Rev. Lett. 65, 1838 (1990).  
38. Connors, E. J., Nelson, J., Qiao, H., Edge, L. F. & Nichol, J. M. Low-frequency charge noise in Si/SiGe quantum dots. Phys. Rev. B 100, 165305 (2019).  
39. Hendricks, N. W. et al. A four-qubit germanium quantum processor. Nature 591, 580-585 (2021).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

© The Author(s), under exclusive licence to Springer Nature Limited 2021

# Methods

Sample fabrication. The triple quantum dot device was fabricated using an isotopically natural, undoped Si/SiGe heterostructure with a mobility of  $300,000\mathrm{cm}^2\mathrm{V}^{-1}\mathrm{s}^{-1}$  at an electron density of  $n = 5\times 10^{11}\mathrm{cm}^{-2}$  and a temperature of  $2\mathrm{K}$ . Phosphorus ion implantation was used to make the ohmic contacts. Standard electron-beam lithography and lift-off techniques were used to fabricate the overlapping aluminium gates and the micromagnet. The micromagnet is a stack of Ti/Co/Al films with thicknesses of  $10 / 250 / 20\mathrm{nm}$ . The  $20\mathrm{-nm}$ -thick aluminium film is expected to serve as an anti-oxidation layer.

Measurement setup. The sample was cooled down in a dry dilution refrigerator (Oxford Instruments Triton) to a base electron temperature of  $\sim 40\mathrm{mK}$ . The d.c. gate voltages were supplied using a 24-channel digital-to-analog converter (QDevil ApS QDAC). Homemade cryogenic low-pass filters with a cutoff frequency of  $160\mathrm{Hz}$  were used to filter its outputs. Each low-pass filter comprised lumped-element resistor-capacitor and inductor-capacitor filters and a copper powder filter[40]. The gate voltage pulses were generated by an arbitrary waveform generator (Tektronix AWG5208) and filtered by Mini Circuits SBLP-39+ Bessel low-pass filters.

The microwave pulses for electric-dipole spin resonance were generated using three I/Q modulated signal generators (two Keysight E8267D and a Keysight E8257D with a Marki microwave MMIQ-0626H I/Q mixer). The waveforms for I/Q modulation were generated by another AWG5208 unit triggered by the arbitrary waveform generator used to generate the gate voltage pulses. The microwave signals were sideband modulated by  $20\mathrm{MHz}$  from the baseband frequencies to avoid an unintentional spin rotation due to leakage (a typical isolation is  $\sim 50$  dBc after calibration of the I/Q imbalances and the d.c. offsets). Unless noted, the microwave pulses had a square envelope with rise and fall times of  $\sim 10$  ns. During the initialization and measurement stages, additional pulse modulations were used to provide further isolation of the microwave signals. The radio-frequency pulses used for resonant SWAP gates were generated by a pulse-modulated Agilent E4432B signal generator. The radio-frequency pulses were combined with the microwave pulses and applied to a screening gate.

Charge sensing was performed using a radio-frequency reflectometry technique $^{41,42}$ . The charge sensor quantum dot was connected to a tank circuit with a resonance frequency of  $181.5\mathrm{MHz}$ . The reflected signal was amplified by a cryogenic amplifier (Caltech CITLF1) and further amplified and demodulated at room temperature. The demodulated signal was digitized using an AlazarTech ATS9440 digitizer card at a sampling rate of  $5\mathrm{MSa s^{-1}}$ . The digitized signal was filtered by a seventh-order digital Bessel low-pass filter with a cutoff frequency of  $0.4\mathrm{MHz}$  to achieve a signal-to-noise ratio high enough for the single-shot spin readout.

Single-qubit randomized benchmarking. In some randomized benchmarking implementations, the recovery Clifford was chosen so that ideal final state was spin-up. In this case, the measured spin-up projection outcome was  $F_{1}(m) = A p^{m} + C$ , where  $m$  is the number of Clifford gates,  $p$  is the depolarizing parameter and  $A$  and  $C$  are the constants to account for the state preparation and measurement errors. When the readout fidelities for spin-up and -down states are different,  $C \neq 0.5$  and it has to be a fitting parameter. Determining  $p$  and  $C$  precisely from fitting requires a very long sequence to measure the asymptotic behaviour, especially if the gate fidelity (or  $p$ ) is close to 1. Instead, we performed another set of randomized benchmarking experiments in which the same random Clifford gates were used, but the recovery Clifford was chosen so that the ideal final state was spin-down[8,10,11,28]. The spin-up projection outcome in this case was  $F_{0}(m) = -A p^{m} + C$ . Thus, the sequence fidelity in Fig. 2d-f is defined as  $F(m) = F_{1}(m) - F_{0}(m) = 2A p^{m}$  so that the uncertainty in the estimation of  $C$  can be removed.

To validate this randomized benchmarking implementation, we performed additional randomized benchmarking measurements on  $\mathrm{Q}_{1}$  in a different cool down. The difference in the device condition resulted in overall higher fidelities than those in Fig. 2d. In Extended Data Fig. 3a, we plot four different curves:  $F_{1}(m)$  (data with a spin-up ideal final state),  $F_{0}(m)$  (data with a spin-down ideal final state), the difference  $F_{1}(m) - F_{0}(m)$  and the sum  $F_{1}(m) + F_{0}(m)$ . In addition, we used longer sequences up to  $m = 300$  Clifford gates to identify the asymptotic behaviour. The measurement fidelities in this case were estimated from the data at  $m = 0$  as  $F_{\uparrow} = F_{1}(0) = 0.905$  and  $F_{\downarrow} = 1 - F_{0}(0) = 0.980$ . The asymptotes  $F_{1}(m)$  and  $F_{0}(m)$  were symmetric around the saturation value expected from the readout asymmetry,  $(F_{\uparrow} - F_{\downarrow} + 1)/2 = 0.462$ . By fitting  $F_{1}(m)(F_{0}(m))$  with the given saturation value, we obtained a gate fidelity of  $99.73 \pm 0.01$  ( $99.79 \pm 0.01 \%$ ). When the saturation value was set as a fitting parameter, the gate fidelity was  $99.73 \pm 0.01$  ( $99.84 \pm 0.01 \%$ ) and the saturation value was  $0.477 \pm 0.02$  ( $0.398 \pm 0.02$ ). In contrast, we obtained a gate fidelity of  $99.76 \pm 0.01 \%$  by fitting the difference  $F_{1}(m) - F_{0}(m)$ . Even when using part of the data up to only  $m = 50$ , we obtained a consistent gate fidelity of  $99.77 \pm 0.01\%$ . We note additionally that the sum  $F_{1}(m) + F_{0}(m)$  is useful to probe state leakage[43]. Leakage out of the computational states causes the reduction of the sum as  $m$  increases. In our case, the sum did not show any clear decay up to  $m = 300$  and therefore we conclude that the state leakage was negligible, as usually expected for spin-1/2 qubit systems.

Extended Data Fig. 3b shows the results of another experimental run with a slightly different readout condition and more symmetric readout fidelities  $(F_{\uparrow} = 0.937$  and  $F_{\downarrow} = 0.962)$ . The difference is a shift of  $100\mu \mathrm{V}$  on the P1 gate voltage and we expect the same gate fidelity as in Extended Data Fig. 3a. For this data set, we obtained gate fidelities of  $99.75\pm 0.01\%$ ,  $99.78\pm 0.01\%$  and  $99.76\pm 0.01\%$  from the fittings of  $F_{1}(m)$ ,  $F_{0}(m)$  and  $F_{1}(m) - F_{0}(m)$ , respectively. The saturation value was fixed to 0.488 in the fitting of  $F_{1}(m)$  and  $F_{0}(m)$ . These fidelities are in reasonable agreement with that obtained by fitting the difference  $F_{1}(m) - F_{0}(m)$  in the different readout condition (Extended Data Fig. 3a).

These results show that, especially when the readout is asymmetric, as in Fig. 2d-f, it is more accurate and efficient to use  $F_{1}(m) - F_{0}(m)$  instead of using just one of  $F_{1}(m)$  and  $F_{0}(m)$ .

Fidelity reduction due to residual exchange coupling. The fidelities in Fig. 2d-f were measured with all the qubits initialized to the spin-down state and the microwave frequencies were adjusted to the resonance conditions with the  $|\downarrow \downarrow \downarrow \rangle$  state as an initial state. With this configuration, for the  $|\downarrow \uparrow \downarrow \rangle$ ,  $|\downarrow \downarrow \uparrow \rangle$ ,  $|\uparrow \uparrow \downarrow \rangle$  and  $|\uparrow \downarrow \uparrow \rangle$  input states, there is a  $J_{23}^{\mathrm{off}} = 1.2\mathrm{MHz}$  frequency detuning when we performed the  $Q_{2}$  and  $Q_{3}$  single-qubit gates. For simplicity, we neglected  $J_{12}^{\mathrm{off}}$  which was measured to be small. As  $J_{23}^{\mathrm{off}} = 1.2\mathrm{MHz}$  is a substantial fraction of  $f_{\mathrm{Rabi}} = 6\mathrm{MHz}$ , the control fidelities decrease too much. To mitigate this, we deliberately detuned our  $Q_{2}$  and  $Q_{3}$  single-qubit control frequencies by  $+0.6\mathrm{MHz}$  from the resonance conditions calibrated with the  $|\downarrow \downarrow \downarrow \rangle$  input state. In this case, for the input states  $|\downarrow \downarrow \downarrow \rangle$ ,  $|\downarrow \uparrow \uparrow \rangle$ ,  $|\uparrow \downarrow \downarrow \rangle$  and  $|\uparrow \uparrow \uparrow \rangle$ , there is a frequency detuning of  $-0.6\mathrm{MHz}$ . In turn, for the input states  $|\downarrow \uparrow \downarrow \rangle$ ,  $|\downarrow \downarrow \uparrow \rangle$ ,  $|\uparrow \uparrow \downarrow \rangle$  and  $|\uparrow \downarrow \uparrow \rangle$ , the frequency detuning decreases to  $0.6\mathrm{MHz}$ . The frequency offset of  $0.6\mathrm{MHz}$  is  $10\%$  of  $f_{\mathrm{Rabi}}$  and comparable to the value in a previous two-qubit demonstration[11]. To infer the average control fidelities for multiqubit input states in this configuration, we performed randomized benchmarking experiments with the control qubit initialized to  $|\downarrow \rangle$  in half of the experiments and  $|\uparrow \rangle$  in the other half of the experiments (Extended Data Fig. 4). Here, we just initialized  $Q_{1}$  to a spin-down state because the effect of  $J_{12}^{\mathrm{off}}$  is small. For the  $Q_{2}(Q_{3})$  single-qubit gate, we obtained a fidelity of  $98.96 \pm 0.05$  ( $99.38 \pm 0.03\%$ ). By comparing these fidelities with those in Fig. 2e,f, we obtained fidelity reductions of  $\sim 0.6\%$  for  $Q_{2}$  and  $\sim 0.5\%$  for  $Q_{3}$ .

Exchange gates. The exchange interactions were controlled through gate voltage pulses. To keep the quantum dot potential near the symmetric operation point during the exchange pulses, we utilized the virtual gate technique $^{44}$ . We measured the gate-voltage-induced shift of the charge transition line of every quantum dot to extract the lever arms of the gates P1, P2, P3, B2 and B3. From the measured lever arms, we constructed the virtual barrier gates  $\delta V_{12}$  and  $\delta V_{23}$  as follows:

$$
(- 0. 2 1 8, 1, - 0. 1 8 0, 0, 0. 0 0 5) \delta V _ {1 2} = (\delta V _ {\mathrm {P} 1}, \delta V _ {\mathrm {B} 2}, \delta V _ {\mathrm {P} 2}, \delta V _ {\mathrm {B} 3}, \delta V _ {\mathrm {P} 3}),
$$

$$
(0. 0 1 8, 0, - 0. 2 4 4, 1, - 0. 2 2 6) \delta V _ {2 3} = (\delta V _ {\mathrm {P} 1}, \delta V _ {\mathrm {B} 2}, \delta V _ {\mathrm {P} 2}, \delta V _ {\mathrm {B} 3}, \delta V _ {\mathrm {P} 3}).
$$

We typically used the virtual barrier gate voltage pulses  $\delta V_{12} = 0.13\mathrm{V}$  and  $\delta V_{23} = 0.075\mathrm{V}$  to turn on  $J_{12}^{\prime} = 2.75\pm 0.02\mathrm{MHz}$  and  $J_{23}^{\prime} = 12.50\pm 0.02\mathrm{MHz}$ , respectively (Extended Data Fig. 3a,b). The residual exchange interactions were measured to be  $J_{12}^{\mathrm{off}} < 0.1\mathrm{MHz}$  and  $J_{23}^{\mathrm{off}} = 1.17\pm 0.01\mathrm{MHz}$  using Ramsey interferometry (Extended Data Fig. 3c,d).  $J_{12}^{\mathrm{off}}$  was below our detection limit and had a minor effect on our measurements.  $J_{23}^{\mathrm{off}}$  was noticeably larger than our qubit linewidths and affected the single-qubit control fidelities. This effect was mitigated by shifting the qubit drive frequencies of  $\mathbf{Q}_2$  and  $\mathbf{Q}_3$  by  $0.6\mathrm{MHz}$  from their resonance frequencies measured with all the qubits initialized to spin-down. Although the tunnel coupling between the middle and right quantum dots could be quenched by reducing the d.c. voltage applied on the B3 gate, this resulted in a drastic reduction of the  $T_{1}$  relaxation time of  $\mathbf{Q}_3$ . The valley splitting of the right quantum dot most probably changes with the barrier gate voltage[45] and enhances the spin-valley hotspot relaxation at the magnetic field used. Although the external magnetic field could be tuned to avoid the spin-valley relaxation, we were not able to take this approach due to the limited microwave frequency range available in our measurement setup.

State tomography. To remove the state preparation and measurement errors, we characterized the initialization and readout fidelities. First, we measured the initialization fidelity of each qubit using a similar scheme as that in Watson et al. As we did not see any enhancement of the initialization fidelities even after waiting for  $50\mathrm{ms}$  (longer than  $9T_{1}$ ) at the single-qubit operation point, we concluded that the initialization fidelities were high ( $>99\%$ ) for all the qubits. As these are much higher than the readout fidelities, throughout this work the initialization infidelities are ignored. The spin-down (up) readout fidelity  $F_{i1}$  ( $F_{11}$ ) was determined from the measured spin-up probability after the standard initialization protocol followed by an I (X) gate. Typical readout fidelities were measured to be  $F_{11} = 0.906$ ,  $F_{11} = 0.852$ ,  $F_{12} = 0.948$ ,  $F_{12} = 0.711$ ,  $F_{13} = 0.955$  and  $F_{13} = 0.844$ . The readout fidelities in the main text were defined as  $F_{i} = (F_{1i} + F_{1t}) / 2$ . The spin-up readout fidelities of  $Q_{1}$  and  $Q_{2}$  were largely limited by the spin relaxation during the sequential readout. Using these parameters, we corrected

the measured probabilities  $\mathbf{P}_{\mathrm{M}} = (P_{\downarrow \downarrow \uparrow},\dots ,P_{\uparrow \uparrow \uparrow})$  as  $\mathbf{P} = (F_{1}\otimes F_{2}\otimes F_{3})^{-1}\mathbf{P}_{\mathrm{M}}$  where  $F_{i} = \left( \begin{array}{ccc}F_{\downarrow i} & 1 - F_{\uparrow i}\\ 1 - F_{\downarrow i} & F_{\uparrow i} \end{array} \right)$  and  $\mathbf{P}$  is the probability used for the input of the

maximum likelihood estimation. This means that we assumed no correlation in the readout errors. Without this readout error removal, we obtained a GHZ state fidelity of 0.458 for the same data as used in Fig. 3.

A maximum likelihood estimation was performed to restrict the density matrix to be physical. A physical density matrix can be written as  $\rho = T^{*}T / \mathrm{Tr}(T^{*}T)$ , where  $T$  is a complex lower triangular matrix with real diagonal elements.  $T$  has 64 real parameters,  $\mathbf{t} = (t_{1},\dots,t_{64})$  and we minimized the cost function:

$$
C (\boldsymbol {t}) = \sum_ {\nu = 1} ^ {6 4} \frac {(\langle \psi_ {\nu} | \rho (\boldsymbol {t}) | \psi_ {\nu} \rangle - P _ {\nu}) ^ {2}}{2 \langle \psi_ {\nu} | \rho (\boldsymbol {t}) | \psi_ {\nu} \rangle},
$$

where  $P_{\nu}$  is the measured probability projected at a state  $|\psi_{\nu}\rangle$ . To determine the 64 parameters, the projection outcomes for linearly independent pre-rotations  $(\mathrm{I},\mathrm{X} / 2,\mathrm{Y} / 2,\mathrm{X})^{\otimes 3}$  are used. To remove the error that could be introduced by the X pre-rotation, the projection outcomes, including the X pre-rotations, were calculated from the corresponding I rotation outcomes<sup>11</sup>. The errors of the maximum likelihood estimation results were obtained by the Monte Carlo method assuming that the measured single-shot probabilities followed multinomial distributions<sup>11,12</sup>. We fitted each of the resulting distributions with a Gaussian function to extract its standard deviation.

Data analysis software. All the curve fittings were performed using non-linear least-squares minimization and curve-fitting for Python (LmFit) $^{46}$ . For minimization of the cost function in the maximum likelihood estimation, we used the minimize function in SciPy $^{47}$ .

# Data availability

All data in this study are available from the Zenodo repository at https://doi.org/10.5281/zenodo.4722605. Source data are provided with this paper.

# References

40. Mueller, F. et al. Printed circuit board metal powder filters for low electron temperatures. Rev. Sci. Instrum. 84, 044706 (2013).  
41. Reilly, D. J., Marcus, C. M., Hanson, M. P. & Gossard, A. C. Fast single-charge sensing with a rf quantum point contact. Appl. Phys. Lett. 91, 162101 (2007).  
42. Noiri, A. et al. Radio-frequency detected fast charge sensing in undoped silicon quantum dots. Nano Lett. 20, 947-952 (2020).

43. Andrews, R. W. et al. Quantifying error and leakage in an encoded Si/SiGe triple-dot qubit. Nat. Nanotechnol. 14, 747-750 (2019).  
44. Hensgens, T. et al. Quantum simulation of a Fermi-Hubbard model using a semiconductor quantum dot array. Nature 548, 70-73 (2017).  
45. Jones, A. M. et al. Spin-blockade spectroscopy of Si/Si-Ge quantum dots. Phys. Rev. Appl. 12, 014026 (2019).  
46. Newville, M., Stensitzki, T., Allen, D. & Ingargiola, A. LMFIT: non-linear least-square minimization and curve-fitting for Python. Zenodo https:// zenodo.org/record/11813#.YH6fbej7SUI (2014).  
47. Jones, E., Oliphant, T. & Peterson, P. SciPy: open source scientific tools for Python. Science Open https://www.scienceopen.com/document?vid=ab12905a-8a5b-43d8-a2bb-defc771410b9 (2001).

# Acknowledgements

We thank the Microwave Research Group at Caltech for technical support. This work was supported financially by Core Research for Evolutional Science and Technology (CREST), Japan Science and Technology Agency (JST) (JPMJCR15N2 and JPMJCR1675), MEXT Quantum Leap Flagship Program (MEXT Q-LEAP) grant no. JPMXS0118069228, JST Moonshot R&D grant no. JPMJMS2065 and JSPS KAKENHI grant nos. 16H02204, 17K14078, 18H01819, 19K14640 and 20H00237. T.N. acknowledges support from the Murata Science Foundation Research Grant and JST, PRESTO grant no. JPMJPR2017.

# Author contributions

K.T. and A.N. fabricated the device and performed the measurements. T.N., J.Y. and T.K. contributed the data acquisition and discussed the results. K.T. wrote the paper with inputs from all the co-authors. S.T. supervised the project.

# Competing interests

The authors declare no competing interests.

# Additional information

Extended data is available for this paper at https://doi.org/10.1038/s41565-021-00925-0.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41565-021-00925-0.

Correspondence and requests for materials should be addressed to K.T. or S.T.

Peer review information Nature Nanotechnology thanks Joseph Kerckhoff and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at www.nature.com/reprints.

![](images/348c3bff7667a423ee2e59f3c470e018cd490431f998dedbe0f13c4400dd61ce.jpg)  
Extended Data Fig. 1 | Initialization and measurement protocol. Initialization and readout procedure. The spin readout and initialization for  $Q_{1}$  is performed near the (111)-(011) boundary, whereas for  $Q_{2}$  and  $Q_{3}$  it is performed near the (111)-(110) boundary. Note that  $Q_{2}$  cannot be directly read out through the reservoir as the co-tunnelling rate between the (111) and (101) states is too small compared to the spin relaxation rate  $T_{1}^{-1}$ . The dwell times are  $450~\mu s$  for  $Q_{3}$  initialization,  $750~\mu s$  for  $Q_{1}$  initialization,  $300~\mu s$  for  $Q_{3}$  readout and  $750~\mu s$  for  $Q_{1}$  readout. The resonant SWAP pulses are  $0.25~\mu s$  long and it corresponds to an exchange Rabi frequency of  $2\mathrm{MHz}$ . The resonance frequency is typically around  $410\mathrm{MHz}$ . The readout dwell time of  $Q_{3}$  is compromised for the finite  $T_{1}$  relaxation times of  $Q_{1}$  and  $Q_{2}$  and it results in imperfect spin-down initialization after the readout stage. Therefore, in order to increase the initialization fidelities, we use an explicit initialization stage which is redundant in the ideal case where all the three spins are initialized to spin-down after the readout stage.

![](images/1c0ed99a3a188e9e39867523f44f43942be81cd94bbab2d45897a153574bb07d.jpg)  
a

![](images/891fcd926ac8baa9c1f1297dd9a242b2dddfaca697acfa3f43e855038e78fd35.jpg)  
b

![](images/bf75b6a52dcb441b693abaa37c3cc3ef455987899d86cf2c527237dc8b1e9561.jpg)  
c

![](images/7afa8fcd4052f65ef16217b24820e84bd84486bcabaef2e5878b1b12b3e442c0.jpg)  
d

![](images/b4d413626fe3398d2b3195f12943a8353cd3f1dc9d814c4c92af691944ac2f46.jpg)  
e

![](images/f781049e0b5e6d737b12d655f597814eedd68a368c84084d021f164f6fb65424.jpg)  
f

![](images/e3d9ba54248cd2dd9c0a31ce38fc32a98fd43aca49e9b4a9ae0ec5b0db66cb04.jpg)  
g

![](images/75c07ebe0ce1ca16210b640879bf51690c1db0a85beae51d8d5de94643ea9d1f.jpg)  
h

![](images/7bcd3bd41995630ab4acc077ee2801009853e2627364c65caf50052f5a62e376.jpg)  
i

![](images/c6addd68c74943dfda962d7cf483867ce09d4d431114df4a86299913237ba65f.jpg)  
j  
Extended Data Fig. 2 | Single-qubit characterization. All qubits are initialized to spin-down before the manipulation stage and only one of the qubits is read out right after the manipulation stage unless noted. The exchange interactions are turned off. All errors represent the estimated standard errors for the best-fit values. a-d,  $T_{1}$  measurements. First, a spin-up state is prepared using an X pulse. Then we vary the waiting time of  $t_w$  at the single-qubit manipulation point before performing single-shot measurement. In this  $T_{1}$  measurement, all three spins are sequentially read out and therefore the visibilities of  $Q_{1}$  and  $Q_{2}$  are decreased by  $T_{1}$  relaxation during the readout stage. Note that the visibility of  $Q_{3}$  is unaffected by the sequential readout. e-h, Ramsey interferometry measurements. First, a  $\pi /2$  pulse (+2 MHz detuned from the resonance frequency) is applied to rotate the spin state to the xy-plane in the Bloch sphere. After an evolution time of  $t_{\mathrm{evol}}$ , another  $\pi /2$  pulse is applied to project the spin state in the z-axis for measurement. The black solid curves are the fit with Gaussian decay. The integration time is 75.8 sec for all qubits. i-l, Hahn echo measurements. Each fitting curve is given by  $P_{\uparrow}(t_{\mathrm{evol}}) = A\exp(-(t_{\mathrm{evol}} / T_2^{\mathrm{echo}})^{\gamma}) + B$ , where  $A$  and  $B$  are the constants to account for the readout fidelities and  $\gamma$  is an exponent. The exponents are found to be  $\gamma = 1.79 \pm 0.12 (Q_1)$ ,  $2.75 \pm 0.10 (Q_2)$  and  $2.61 \pm 0.09 (Q_3)$ .

![](images/90df488f99f7d53d5715d356b78d8b4c30bbb98659e89717b8c55da8fa98d788.jpg)  
k

![](images/29b165fae6aa6e7e70cbee711c0d0379a877398fc8d18afd206f261671a235f0.jpg)  
1

![](images/f6039d78371d661e8124e8ad4506a744533447df2cf2f171255d49b76692387f.jpg)  
Extended Data Fig. 3 | Additional randomized benchmarking measurements. a, Measurement result with an asymmetric readout condition.  $F_{1}(F_{0})$  is the spin-up probability when the recovery Clifford gate is chosen so that the ideal final spin state is spin-up (-down). The data points at  $m = 0$  are measured without any random Clifford gates applied. Only an X pulse is applied in the case of  $F_{1}$  and no pulse is applied in the case of  $F_{0}$ . The dashed line shows a constant 0.462, the expected saturation value derived from the readout asymmetry. b, Measurement result with a more symmetric readout condition.

![](images/d35c88c798177b6d681e2b5b17a2a0e3b39fd679f207d0373985878a1d0b7bbc.jpg)

![](images/d3ca7b413973c1bc4fd5e7fd21ee6170b0a318ebab728b98f45b274d41806043.jpg)  
a  
C: random Clifford gate  $C_{g}$ : recovery Clifford gate  
c

![](images/69d844bfc00bb21fb5a7c80503f1533d0cf35a917325a3dcf934d827e51d84dd.jpg)  
C: random Clifford gate  $C_{\mathrm{R}}$ : recovery Clifford gate

![](images/7448f7fdb24d3baebc869539ed3cb1c80ab8b7dc4408c22493708fb82856d3df.jpg)  
b  
Extended Data Fig. 4 | Randomized benchmarking with detuned microwave frequency. a, Randomized benchmarking sequence for  $Q_{2}$  fidelity measurement. b, Randomized benchmarking measurement result of  $Q_{2}$  with a frequency detuning of 0.6 MHz. For each of the control bit  $(Q_{3})$  states, the measurement is performed for 16 sets of random Clifford gate sequences. The sequence fidelity shows an average of the results for the two control bit configurations. The errors represent the estimated standard errors for the best-fit values. c, d, Similar randomized benchmarking measurement performed for  $Q_{3}$ . The errors represent the estimated standard errors for the best-fit values.

![](images/1b2b70ca6d77b09fd2fe7e687c009fe95b0bf840aadfb7e59ca6aebac0955e96.jpg)  
d

![](images/10dbd271f9844544015462f673ff39f35fee9ed073e030542038db4bc427e156.jpg)  
a

![](images/abff9b620a7cb21d6316444d32b0995497786a33adbff08a5a90b5257abd73bd.jpg)  
b  
c

![](images/651b08d74d2299c7f6079037dc7e62adb474a58c655c99ac5676bc77f6e1d1c6.jpg)

![](images/aea35aa39dded436cdc267cef5cd7d490b408fe37abefdfd5bd39b6bc38b2dae.jpg)  
d

![](images/1b2c2787ddb98433f33f378a9fffb042e1c98db0e3c37441c2d9d79f6d70fb45.jpg)  
e

![](images/be80548dcbdcbf6c6dad26daaee5483de991ad4598224559f6332b153f837496.jpg)  
f

![](images/0a42d4fe7e6e13ea07c1337165f5551b175b6895b73e9d94523db497eebc5947.jpg)  
g

![](images/f6f477978dad719c271a4b42ea6d4d8f7379c0dd207253eddcd9e45e03788b74.jpg)  
h

![](images/62c36a1a94b557644c3e4223fb3c8543614073581d9ae9d04ab4a63b8c3ddec6.jpg)  
i  
Extended Data Fig. 5 | Measurements of exchange interactions. All errors represent the estimated standard errors for the best-fit values. a, b, Controlled-rotation for  $Q_{1}$  and  $Q_{2}$ . The measurement is performed to probe  $J_{12}^{\prime}$ . First,  $Q_{1}$  and  $Q_{2}$  are initialized to spin-down. To prepare a spin-up control qubit  $(Q_{2})$  state, an X pulse is applied. After tuning on  $J_{12}^{\prime}$  by a gate voltage pulse, a low-power Gaussian microwave pulse (truncated at  $\pm 2\sigma$ ) is applied to induce a controlled-rotation. The filled (open) circles show the measured spin-up probabilities with the control qubit spin-down (up). The solid lines are Gaussian fitting curves. From the separation of the two peaks, we obtain  $J_{12}^{\prime} = 2.75 \pm 0.02 \mathrm{MHz}$ . c, d, Similar controlled rotation measurement for  $Q_{2}$  and  $Q_{3}$ . We obtain  $J_{23}^{\prime} = 12.50 \pm 0.02 \mathrm{MHz}$  from this measurement. e, Ramsey experiment to extract  $J_{12}^{\mathrm{off}}$ . We perform two Ramsey measurements of  $Q_{1}$  with different control qubit  $(Q_{2})$  states. The difference of qubit frequency detuning is equivalent to  $J_{12}^{\mathrm{off}}$ . f, Ramsey measurement result when  $Q_{2}$  is spin-down. The red circles are the measured  $Q_{1}$  spin-up probabilities and the black solid curve shows a fit with Gaussian decay. From the oscillation frequency of the decay curve, we extract  $\delta f_{\downarrow} = 2.28 \pm 0.01 \mathrm{MHz}$ . g, Measurement similar to the one in f when  $Q_{2}$  is spin-up. We extract  $\delta f_{\uparrow} = 2.21 \pm 0.01 \mathrm{MHz}$ . Since the difference between  $\delta f_{\downarrow}$  and  $\delta f_{\uparrow}$  is below the stochastic fluctuation of the frequency detuning, we conclude that  $J_{12}^{\mathrm{off}}$  is below our detection limit. Note that each frequency error shows one standard deviation of the fitting parameter. h-j, Ramsey experiments to extract  $J_{23}^{\mathrm{off}}$ . We obtain  $J_{23}^{\mathrm{off}} = \delta f_{\uparrow} - \delta f_{\downarrow} = 1.17 \pm 0.01 \mathrm{MHz}$  from these measurements.

![](images/9fc5190ac473b6b385a893f008a5548e4426ec6350516782912dbbfeff3392db.jpg)  
j

![](images/69fed891d7546a1f06c253936153599cd383ddb4771ce147cdd884ad981a7f96.jpg)  
a

![](images/a6c84b6a42ee17400b0854fd9ab225e0841a0718cae2bf46693c5b500ab9d098.jpg)  
b

![](images/35897ec35ebd2bd59fa3bc196cf8503a6db7b5b76ca984199c171b1305c3acf6.jpg)  
C

![](images/96fe030b9efa20928d84bc672a6a71fa3c2ee16bce1aa2de02946cae6ce1861e.jpg)  
d

![](images/9ea0df4be6a44735eb6804fad9ab1595db80dccd5c242be057eb26ed30f97e3f.jpg)  
e

![](images/fb8f85424ed9a8e4e4e9cd45f703b7845f4af42d714a16ad487de9746738a58d.jpg)  
Extended Data Fig. 6 | Bell state tomography using  $Q_{2}$  and  $Q_{3}$ . As a benchmark of our two-qubit CZ gate, we perform Bell state tomography on  $Q_{2}$  and  $Q_{3}$ . The experiment is a reduced version of the three-qubit GHZ state tomography. The readout errors are removed using the measured readout fidelities and maximum likelihood estimation is used to reconstruct the density matrices. a, Quantum gate sequence for Bell state creation and state tomography. By modifying the phase gates after the second CZ/2 pulse, we can create all four Bell states. b-e, Real parts of the measured density matrices for four Bell states,  $\Phi^{+} = (|\uparrow \uparrow \rangle + |\downarrow \downarrow \rangle) / \sqrt{2} (\mathbf{b})$ ,  $\Phi^{-} = (|\uparrow \uparrow \rangle - |\downarrow \downarrow \rangle) / \sqrt{2} (\mathbf{c})$ ,  $\Psi^{+} = (|\downarrow \uparrow \rangle + |\downarrow \uparrow \rangle) / \sqrt{2} (\mathbf{d})$ , and  $\Psi^{-} = (|\downarrow \uparrow \rangle - |\uparrow \downarrow \rangle) / \sqrt{2} (\mathbf{e})$ . We obtain the state fidelities relative to the target states of 0.942  $(\Phi^{+})$ , 0.933  $(\Phi^{-})$ , 0.950  $(\Psi^{+})$  and 0.940  $(\Psi^{-})$ , and the concurrences of 0.950  $(\Phi^{+})$ , 0.906  $(\Phi^{-})$ , 0.923  $(\Psi^{+})$  and 0.935  $(\Psi^{-})$ .

![](images/1a603b7317c607f81a7ce3adae4852b6c2a123e4ebe4551a9128f1a8ac23e0e4.jpg)  
Extended Data Fig. 7 | Imaginary part of the experimental GHZ state. The imaginary part is all zero for an ideal GHZ state. Here, the maximum absolute value of the matrix elements is 0.09.