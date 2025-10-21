# Quantum error correction with silicon spin qubits

https://doi.org/10.1038/s41586-022-04986-6

Received: 21 January 2022

Accepted: 16 June 2022

Published online: 24 August 2022

Open access

Check for updates

Kenta Takeda $^{1\boxtimes}$ , Akito Noiri $^{1}$ , Takashi Nakajima $^{1}$ , Takashi Kobayashi $^{2}$  & Seigo Tarucha $^{1,2\boxtimes}$

Future large-scale quantum computers will rely on quantum error correction (QEC) to protect the fragile quantum information during computation<sup>1,2</sup>. Among the possible candidate platforms for realizing quantum computing devices, the compatibility with mature nanofabrication technologies of silicon-based spin qubits offers promise to overcome the challenges in scaling up device sizes from the prototypes of today to large-scale computers<sup>3-5</sup>. Recent advances in silicon-based qubits have enabled the implementations of high-quality one-qubit and two-qubit systems<sup>6-8</sup>. However, the demonstration of QEC, which requires three or more coupled qubits<sup>1</sup>, and involves a three-qubit gate<sup>9-11</sup> or measurement-based feedback, remains an open challenge. Here we demonstrate a three-qubit phase-correcting code in silicon, in which an encoded three-qubit state is protected against any phase-flip error on one of the three qubits. The correction to this encoded state is performed by a three-qubit conditional rotation, which we implement by an efficient single-step resonantly driven iToffoli gate. As expected, the error correction mitigates the errors owing to one-qubit phase-flip, as well as the intrinsic dephasing mainly owing to quasi-static phase noise.

These results show successful implementation of QEC and the potential of a silicon-based platform for large-scale quantum computing.

Quantum computing takes advantage of quantum superposition and entanglement to accelerate the computational tasks $^{12,13}$ . However, these quantum properties are sensitive to decoherence errors owing to energy relaxation and dephasing. As the number of qubits increases and/or the computational tasks become more complex, the errors cause exponential reduction of the accuracy of computational results. QEC is a protocol to circumvent this problem by distributing the quantum information across a larger multiqubit entangled state so that the errors can be detected and corrected $^{14}$ . Its basic concept has been demonstrated in various platforms, such as nuclear magnetic resonance $^{9,15}$ , trapped ions $^{10,16}$ , nitrogen vacancy centres $^{17}$  and superconducting circuits $^{11,18,19}$ , and has served as an important benchmark of the qubit systems. Silicon-based spin qubits have emerged as a qubit platform in the past decade, and there has been rapid progress in long coherence times $^{20,21}$ , high-fidelity universal quantum gates $^{6-8}$ , high-temperature operation $^{22,23}$  and generation of three-qubit entanglement $^{24,25}$ .

Our three-qubit system (Fig. 1a) comprises one data qubit  $(\mathrm{Q}_2)$  to be corrected and two ancilla qubits  $(\mathrm{Q}_1$  and  $\mathrm{Q}_3)$ . The sequence starts from encoding the data qubit state to a three-qubit entangled state. Then the phase-flip errors that occurred in the encoded state are mapped to the ancilla qubit states by the decoding. The original data qubit state can finally be restored by a correcting logic gate based on the ancilla qubit states. Most commonly, this correction can be performed by a projective measurement of ancilla qubits followed by a feedback quantum gate on the data qubit. However, this requires a capability to perform high-fidelity qubit measurement much faster than the coherence time, which is still challenging with spins in silicon. Although this measurement-based operation is a key component for

fault tolerance, in the case of three-qubit QEC, it can alternatively be performed by a multiqubit conditional qubit rotation. In this Article, we take this approach by using a three-qubit iToffoli gate, which coherently rotates the data qubit conditioned on the ancilla spin polarization. We synthesize a three-qubit phase-flip code and demonstrate that one-qubit phase-flip error can be corrected and the intrinsic ensemble spin dephasing can be mitigated.

Our sample is a gate-defined triple quantum dot in an isotopically natural silicon/silicon-germanium (Si/SiGe) heterostructure. Three layers of overlapping aluminium gates $^{26}$  are used to control the triple-dot confinement. A micro-magnet is fabricated on top of the aluminium gates to provide a local magnetic field gradient $^{27}$ . As schematically shown in Fig. 1b, we configure the gate voltages so that only one electron is confined under each of the plunger gates (P1, P2 and P3) and the inter-dot tunnel coupling is controlled by the barrier gates (B2 and B3). Measurement of the triple-dot charge configuration is performed by monitoring the conductance of the nearby charge sensor quantum dot using the radio-frequency reflectometry technique $^{28,29}$ . An in-plane external magnetic field of  $B_{\mathrm{ext}} = 0.607 \mathrm{T}$  is applied using a superconducting magnet. We use the Zeeman-split spin-1/2 states of the single electrons as our spin qubits (labelled  $Q_1$ ,  $Q_2$  and  $Q_3$  in Fig. 1b,c). The Zeeman energy splitting (about 20 GHz) much larger than the thermal excitation energy (about 0.8 GHz or 40 mK) enables initialization and readout of the three-spin state by the combination of energy-selective tunnelling $^{30}$ , shuttling $^{31}$  and controlled rotation (see Methods and Extended Data Fig. 1 for the full details of the sequence).

The single-qubit rotations are performed by applying resonant microwave pulses (see Methods and Extended Data Fig. 2). The

![](images/222a8e4f3a486459817a791be37066d0c63e1bdbdecf8df3fd8bef60d496f637.jpg)  
a  
C

![](images/2ec11962e2c883ded82f1c3cf2a3843f639fe49dc539be833d45e5f7e22f4075.jpg)  
b

![](images/91fc1d3116d55d792e6d1d09e2f0b6b362925a5e6715c26aaa4bfd5816c376f4.jpg)  
Fig. 1|Three-qubit QEC and silicon-based three-qubit device. a, Outline of the three-qubit phase-flip quantum error correcting code. The two-qubit CNOT gates entangle the three qubits, then the Hadamard (H) gates rotate the qubit basis for phase-flip errors. The decoding is the inverse of the encoding. Finally, the correction is performed by a three-qubit Toffoli gate. b, Scanning electron microscope image of the device. Scale bar,  $100\mathrm{nm}$ . The screening gates (brown) are used to restrict the electric field of the plunger (green) and barrier (purple) gates. The three circles (red, green and blue) indicate the position of the triple-quantum-dot array. A further quantum dot shown as the grey circle is used as a charge sensor. The gates P1, P2, P3, B2 and B3 are connected to an arbitrary waveform generator to apply fast voltage pulses. The microwave control pulse for electric-dipole spin resonance is applied to the lower screening gate. c, Schematic cross section of the device. The line in the silicon quantum well shows the schematic triple-dot confinement potential.  $J_{12}(J_{23})$  represents the nearest-neighbour exchange coupling between  $\mathbf{Q}_1$  and  $\mathbf{Q}_2$  ( $\mathbf{Q}_2$  and  $\mathbf{Q}_3$ ).

microwave pulse displaces the quantum dot position, effectively creating an oscillating transverse magnetic field that induces electric-dipole spin resonance[27]. The two-qubit controlled phase (CZ) gate is implemented by adiabatically pulsing the exchange couplings  $J_{12}$  and  $J_{23}$  by the barrier gates B2 and B3, respectively (see Methods and Extended Data Fig. 3). To operate the qubit close to the charge-symmetry point, the effect of capacitive crosstalk between the plunger and barrier gates is suppressed by the virtual gate technique (see Methods). The spin qubits herein have an average  $T_{1}$  relaxation time of  $22\mathrm{ms}$ , inhomogeneous dephasing time  $T_{2}^{*}$  of  $1.8\mu \mathrm{s}$  and Hahn echo dephasing time  $T_{2}^{\mathrm{H}}$  of  $43~\mu \mathrm{s}$  (Extended Data Fig. 4). Because electron spins have orders of magnitude longer  $T_{1}$  times compared with the dephasing times  $T_{2}^{*}$  and  $T_{2}^{\mathrm{H}}$ , we focus on the implementation of a phase-flip correction code in this work, whereas a bit-flip correction code can easily be assembled by introducing further single-qubit rotations.

First we demonstrate the ability to encode and decode the data qubit state. For simplicity, here we perform encoding of an input state on the equator of the Bloch sphere,  $Q_{2} = (|\downarrow \rangle + e^{i\phi}|\uparrow \rangle) / \sqrt{2}$  (Fig. 2a,  $\phi$  is an azimuthal angle), which is encoded to a maximally entangled three-qubit Greenberger-Horne-Zeilinger (GHZ) state  $|GHZ_{\phi}\rangle = (|\downarrow \downarrow \downarrow \rangle + e^{i\phi}|\uparrow \uparrow \uparrow \rangle) / \sqrt{2}$ . The controlled NOT (CNOT) gates used in the encoding are decomposed to native CZ gates combined with the decoupling pulses to mitigate the local quasi-static phase noise. For the QEC implementation, a crucial property is that the encoded state is a genuine three-qubit GHZ-class state. We confirm this by characterizing the generated state using three-qubit quantum state tomography (Methods). In Fig. 2b (2c), the real part of the measured experimental density matrix  $\rho$  for  $\phi = 0$  ( $\pi$ ) is plotted. We evaluate the state fidelities  $F = \langle GHZ_{\phi}|\rho |GHZ_{\phi}\rangle$  for various  $\phi$  (Fig. 2d) and confirm that all the states

![](images/6d2237f9426c517365da05ae23c8f024006f842b624dd2bd9c9325d04d753f2d.jpg)  
a

![](images/6ba76a5bd21c6479397b59358ae8d0ce8eb2d7b5b8f64248b163783cb2d1bd10.jpg)  
b  
d

![](images/fdd34e88c185b2401e9c3b05054a7bba61c1b2313cd77f55e8129f78b00ef908.jpg)  
c  
9

![](images/f39eb78d389a014f660316dabce0cb58f5a288c28b122cd78fbc6cfbc29e8b00.jpg)  
Fig.2 | See next page for caption.

![](images/d232574179a4ee1f255b4f9535f463c0a0c547d4fd635d7d34a55d764ffb1a36.jpg)  
e

![](images/f3de75a86bb6c56fe19b7abccee13f551533f055dc42276aca60cdc8f844046c.jpg)  
f

![](images/37cf15eb06dca1c54f1634c0e230afe1a4dc8b83e5d425e28eb4f2cf23eb6139.jpg)

![](images/528a83dc32bf20021d03b7a7bc920c4b98b4833f954cc2d5ffb98f1f01f613f9.jpg)  
h

# Article

Fig. 2 | Encoding of three-qubit GHZ states and resonantly driveniToffoli gate. a, Quantum circuit to generate three-qubit GHZ-class states. X (Y, Z) represents a  $\pi$  rotation about the  $x(y,z)$  axis and X/2 (Y/2, Z/2) represents a  $\pi/2$  rotation about the  $x(y,z)$  axis. The two CNOT gates acting on the neighbouring qubits are implemented by the combination of single-qubit and two-qubit gates, as shown in the bottom half. The Y pulses in the middle of the sequence (surrounded by the purple box) are used to suppress the low-frequency single-qubit phase noise. b,c, Real parts of the measured density matrices of the three-qubit GHZ states ( $\phi = 0$  in b and  $\phi = \pi$  in c). d, Result of the GHZ state generation for various input states. The solid black line shows the average of

GHZ state fidelities, that is 0.866. The range above the threshold value 0.75 (0.5) to distinguish the GHZ-class states from the W-class (biseparable) states $^{40}$  is shown as the coloured band. e, Schematic energy diagram of the three-spin state. f, Resonance peaks of  $\mathrm{Q}_2$  for four different control qubit states at the exchange couplings  $J_{12} = J_{23} = 4.5\mathrm{MHz}$ . Here we define  $\delta f = 0$  as the resonance condition when  $\mathrm{Q}_1\mathrm{Q}_3 = |\downarrow \downarrow \rangle$ . The circles show the measured  $\mathrm{Q}_2$  spin-up probabilities for the four different control qubit configurations. The solid lines show fitting with Gaussian functions. The traces are offset by 1 from each other for clarity. g, Schematic sequence of the measurement of the iToffoli gate truth table. h, Measurement result of the iToffoli gate truth table.

have fidelities above 0.75, the threshold to witness genuine GHZ-class states.

For correcting the decoded state, we implement a Toffoli-class three-qubit gate. The standard three-qubit Toffoli gate can be synthesized from 12 CNOT and two single-qubit gates $^{32,33}$  (excluding T gates that can be implemented in software), albeit that decoherence in our device does not allow this implementation with a reasonable fidelity. Alternatively, we use a single-step, resonantly driven iToffoli gate implemented by a resonant  $\pi$  pulse in the presence of simultaneous nearest-neighbour exchange couplings (Fig. 2e). Without the exchange couplings (left side of Fig. 2e), the four transitions associated with the  $Q_{2}$  rotation are degenerate with a resonance frequency of  $f_{0}$ . The finite exchange couplings shift downward the energy levels of the antiparallel spin configurations. As a result, the resonance frequency of  $Q_{2}$  is modulated as  $f_{0} + s_{1}J_{12} + s_{3}J_{23}$ , in which  $s_i = \pm 1/2$  is the spin number of  $Q_{i}$ . Under the condition of  $J_{12} = J_{23}$  required for conditional phase synchronization (see Methods), a rotation of  $Q_{2}$  with  $Q_{1}Q_{3} = |\downarrow \downarrow\rangle$  or  $|\uparrow \uparrow\rangle$  corresponds to a controlled-controlled-rotation.

Figure 2f shows the spectra of  $\mathrm{Q}_2$  with four different ancilla qubit states  $\mathrm{Q}_1\mathrm{Q}_3 = |\downarrow \downarrow \rangle, |\downarrow \uparrow \rangle, |\uparrow \downarrow \rangle$  and  $|\uparrow \uparrow \rangle$  at  $J_{12} = J_{23} = 4.5\mathrm{MHz}$ , in which we observe the peak positions as expected from the exchange couplings. We use a resonant  $\pi$  pulse at  $f_{\mathrm{MW}} = f_1(\mathrm{Q}_1\mathrm{Q}_3 = |\downarrow \downarrow \rangle)$  to implement our iToffoli gate, as this transition yields the highest visibility[34]. The iToffoli gate is a three-qubit gate equivalent to a Toffoli gate with an extra phase factor of  $i$  on the ancilla qubits. To characterize its property, we prepare the eight possible three-spin eigenstates, apply the iToffoli gate and perform three-spin projective measurement (Fig. 2g,h). The readout errors are removed from the data based on the measured readout fidelities (see Methods). The Rabi frequency is chosen so that the off-resonant rotations for the  $\mathrm{Q}_1\mathrm{Q}_3 = |\downarrow \uparrow \rangle /|\uparrow \downarrow \rangle$  subspaces are synchronized (see Methods). In Fig. 2h, as expected, the populations of  $|\downarrow \downarrow \downarrow \rangle$  and  $|\downarrow \uparrow \downarrow \rangle$  states are swapped, whereas the other states are essentially unaffected. From this result, we obtain a population transfer fidelity of our iToffoli gate as  $\mathrm{Tr}(U_{\mathrm{expt}}U_{\mathrm{idcal}}) / 8 = 0.96$ , in which  $U_{\mathrm{expt}}(U_{\mathrm{idcal}})$  represents the experimental (ideal) gate action on the eigenstates (see Methods and Extended Data Fig. 5e-g for the result of the full quantum process tomography). In addition, we perform a calibration of the pulse duration and timing to eliminate unwanted phase accumulation on  $\mathrm{Q}_2$  (see Methods). Note that the dephasing and phase accumulation on the ancilla qubits do not affect the error correction outcome.

We then turn to the implementation of the phase-flip correcting code. Figure 3a shows the quantum circuit diagram. The three-qubit operation U serves to encode the data qubit state  $|\psi \rangle$  to the three-qubit entangled state. The exact implementation of U is shown in the bottom half of the figure, and it is equivalent to the two CNOT gates shown in Fig. 2a, except for the single-qubit gates that do not affect the function of the QEC. Here the data qubit state  $|\psi \rangle = \alpha |\downarrow \rangle +\beta |\uparrow \rangle$  is encoded to a phase-sensitive three-qubit state  $\alpha | + + + \rangle +\beta | - - - \rangle$  in which  $|\pm \rangle = (|\downarrow \rangle \pm |\uparrow \rangle) / \sqrt{2}$  are the eigenstates of the Pauli X operator. For a phase-flip error with a flip rate of  $p$  on  $\mathrm{Q}_2$ , the decoded state is  $\sqrt{1 - p} |\downarrow \rangle (\alpha |\downarrow \rangle +\beta |\uparrow \rangle)|\downarrow \rangle +\sqrt{p} |\uparrow \rangle (\beta |\downarrow \rangle +\alpha |\uparrow \rangle)|\uparrow \rangle$  (see Extended Data Table 1 for the cases with an error on ancilla). The correcting procedure

is implemented so that  $\mathrm{Q}_2$  is flipped only when  $\mathrm{Q}_1\mathrm{Q}_3 = |\uparrow \uparrow \rangle$  by applying  $\pi$  pulses on the ancilla qubits followed by the iToffoli gate, resulting in a product state of  $\mathrm{Q}_2 = \alpha |\downarrow \rangle + \beta |\uparrow \rangle$  and  $\mathrm{Q}_1\mathrm{Q}_3 = \sqrt{1 - p} |\uparrow \uparrow \rangle + i\sqrt{p} |\downarrow \downarrow \rangle$ . Now the data qubit state is the same as the input state regardless of  $p$ . This is demonstrated in Fig. 3b, in which we estimate the process fidelity of the data qubit for various intentional one-qubit errors (see Methods for details of the quantum process tomography). We implement the one-qubit error as a phase rotation with a known rotation angle  $\theta$ , which is equivalent to a phase-flip error with  $p = \sin^2(\theta / 2)$ . Therefore, without the correction, the process fidelity oscillates as a function of  $\theta$ , shown as the black points. With the correction, the oscillation vanishes, and it confirms the basic function of the phase-flip correcting code (corrected  $\mathrm{Q}_i$  error means that a phase-flip error is applied to only  $\mathrm{Q}_i$  and the correction is performed). When there is no error  $(\theta = 0)$ , the process fidelity slightly decreases after the correction. This can be attributed to the infidelity of the iToffoli gate projected to the data qubit subspace. Furthermore, we show that the state of ancilla

![](images/3b9fd25ac5a499a7c514ed8b0ee9f445c891d4d1fd899bbad4d0584d462eeaeb.jpg)

![](images/158f7029492e3ee57eac6cb89659168e43069fb1100069a677754e3f3ae5981e.jpg)  
Fig. 3|One-qubit phase error correction. a, Schematic of the quantum circuit. The operation U used for encoding and decoding is decomposed into the single-qubit and two-qubit gates, as shown in the lower half of the figure. b, Result of one-qubit phase error correction. In the case of uncorrected, we omit the iToffoli gate and the rest of the quantum circuit is the same as the one for the corrected case. For the ideal case without gate infidelities, the uncorrected fidelity oscillates from 0 to 1 and the corrected fidelities are always equal to 1. c, Ancilla qubit measurement results. Note that, owing to the implementation of our correcting procedure, the resulting population of the ancilla qubit state is flipped as compared with the implementation using a standard Toffoli gate<sup>11</sup>.

![](images/65e24d63f05ffedca554f8cd19edbffb1b92076e9ae484f561ea8641ef7709dc.jpg)

![](images/2116fdfa0573032a2be1fb7ce2e86725cf4a656b7d2f160a0e5703f2c56223fa.jpg)

![](images/379895f0e2c11079270d3f48c6f543150448b409162c5636a68864875d4368a2.jpg)  
Fig. 4 | Three-qubit phase error correction. a, Schematic of the quantum circuit for three-qubit phase error correction. The phase error  $Z(p)$  is a virtual phase rotation with a rotation angle of  $2\arcsin(\sqrt{p})$ , which results in an effective error rate of  $p$ . We prepare the data qubit input state  $|\psi\rangle$  by initialization to a spin-down state and a subsequent single-qubit rotation I, X/2, Y/2 or X. b, Measured process fidelities for the corrected and uncorrected cases. Each data point is obtained by averaging 2,000 experiments that are segmented into 1,000 experiments with interleaved qubit frequency calibrations. The error bars are obtained by a Monte Carlo resampling method<sup>41</sup> and represent  $1\sigma$  from the mean. Inset, calculated fidelities for the ideal cases without gate errors. c, Schematic of the quantum circuit for three-qubit dephasing error correction. The waiting time  $t_w$  is the time interval between the last single-qubit rotation in U and the first single-qubit rotation in  $U^{-1}$ . The

qubits reflects the error on the encoded qubit state (error detection). We measure the joint probability of the ancilla qubits  $Q_{1}$  and  $Q_{3}$  for the four possible cases with no error or a full  $\pi$  flip error. We observe that the measured ancilla states correctly reflect the error occurring on the encoded three-qubit state (Fig. 3c).

Errors in actual quantum computers probably occur on all qubits simultaneously rather than on only one of the qubits. We verify the performance of our error correcting code in such a case in which all errors have the same effective error rate of  $p$  as per the common assumption in QEC $^{14}$  (Fig. 4a). Without the correction, the data qubit process fidelity linearly decreases as  $p$  is increased. When the error correction is applied, errors on two and three qubits remain uncorrected, resulting in a process fidelity insensitive to  $p$  up to the first order,  $F(p) = 1 - 3p^2 + 2p^3$  (ref.  ${}^{14}$ ) (see Fig. 4b inset). The quadratic dependence on  $p$  is a crucial property of QEC and it ideally results in an improvement of the fidelity for  $p < 0.5$ . We confirm this crucial property in Fig. 4b, in which the measured process fidelity with the correction is plotted as the cyan curve. A quadratic function fits well to the data (see Extended Data Fig. 6 for a comparison between different fitting models). If we allow the first-order term in the fit, it is  $0.0 \pm 0.1$  (the error is  $1\sigma$ ), representing a marked reduction of the first-order sensitivity as compared with the uncorrected case. As for the fidelity enhancement, the corrected qubit shows improvements in the range  $p < 0.429 \pm 0.003$  (the threshold is obtained by comparing the two fitted curves in Fig. 4b, the error is  $1\sigma$ ). Although the corrected fidelities are always lower than those of the ideal uncorrected qubit in the present experiment (dashed grey line in

![](images/fea91befb72201274583df8ca66b47b7bf0248f8b30ec96f6454cd356b648e98.jpg)

![](images/4d972f8c0ba5da8590ec7e4a4738923fc21661dc9ebba6de2221be7ebce99b5e.jpg)  
deviation of the purple curve from the black curve reflects the gate infidelities in the encoding and decoding. d, Comparison of the state fidelities of the corrected and uncorrected qubits. In the case of the physical qubit, we perform a Ramsey measurement with varying waiting time  $t_{\mathrm{w}}$  between the first  $\pi / 2$  pulse and the pre-rotation for tomographic readout. Each data point is obtained by averaging 3,000 experiments that are segmented into 1,000 experiments with interleaved qubit frequency calibrations. The data acquisition time is the same for all traces in this figure. The solid curves are guides to the eye obtained by fitting to a general exponential decaying function  ${}^{42}F(t) = (1 + \alpha \exp(-(t / T_2)^n) / 2$ , with  $\alpha = 0.492 \pm 0.005$ ,  $0.432 \pm 0.008$  and  $0.464 \pm 0.007$ ,  $T_2 = 1.44 \pm 0.02$ ,  $1.36 \pm 0.04$  and  $1.12 \pm 0.03 \mu \mathrm{s}$ , and  $n = 1.90 \pm 0.08$ ,  $2.1 \pm 0.2$  and  $1.68 \pm 0.08$  for the physical qubit, corrected qubit and uncorrected qubit, respectively. The errors are  $1\sigma$  from the mean.

Fig. 4b), improvement of the coherence times and thereby the fidelity of the iToffoli gate, which primarily limits the performance in the corrected case, would ameliorate the situation. In silicon spin qubits, the intrinsic phase error is more like a quasi-static phase shift rather than a sudden phase flip. In our device, the phase shift is mainly caused by the fluctuating spins of surrounding  $^{29}\mathrm{Si}$  nuclei. To demonstrate the effectiveness of our error correcting code to this type of phase error, we measure the dephasing of the encoded three-qubit state (Fig. 4c,d). As predicted from the ability to correct small phase errors in Fig. 4b, the initial slope of the fidelity decay is suppressed as compared with that of an uncorrected encoded qubit. Overall, these results show a successful implementation of three-qubit phase-correcting code in silicon.

In conclusion, we have demonstrated the generation of the various three-qubit entangled states, the effective single-step resonantly driven iToffoligate and the fundamental properties of three-qubit QEC in silicon. Extending the experiment to a larger scale would require a more flexible feedback-based correcting rotation. This would be limited by the slow spin measurement and initialization by energy-selective tunnelling, which also pose a challenge to complete the error correction (or detection) before the phase coherence is completely lost. Substantial improvements should be possible by switching to the singlet-triplet readout, in which high-fidelity spin measurements in a few  $\mu s$  (refs. $^{35,36}$ ), orders of magnitude shorter than the phase coherence time with dynamical decoupling $^{21}$ , are routinely achieved. Along with the recent advances in scalable device design $^{37}$ , electronics $^{38}$  and gate fidelities $^{6-8}$ , we anticipate that it will become possible to demonstrate

more sophisticated quantum error correcting codes in a large-scale silicon-based quantum processor.

# Online content

Any methods, additional references, Nature Research reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-022-04986-6.

1. Shor, P. W. Scheme for reducing decoherence in quantum computer memory. Phys. Rev. A 52, 2493-2496 (1995).  
2. Fowler, A. G., Stephens, A. M. & Groszkowski, P. High-threshold universal quantum computation on the surface code. Phys. Rev. A 80, 052312 (2009).  
3. Gonzalez-Zalba, M. F. et al. Scaling silicon-based quantum computing using CMOS technology. Nat. Electron. 4, 872-884 (2021).  
4. Camenzind, L. C. et al. A hole spin qubit in a fin field-effect transistor above 4 kelvin. Nat. Electron. 5, 178-183 (2022).  
5. Zwerver, A. M. J. et al. Qubits made by advanced semiconductor manufacturing. Nat. Electron. 5, 184-190 (2022).  
6. Xue, X. et al. Quantum logic with spin qubits crossing the surface code threshold. Nature 601, 343-347 (2022).  
7. Noiri, A. et al. Fast universal quantum gate above the fault-tolerance threshold in silicon. Nature 601, 338-342 (2022).  
8. Mills, A. R. et al. Two-qubit silicon quantum processor with operation fidelity exceeding  $99\%$ . Sci. Adv. 8, eabn5130 (2022).  
9. Cory, D. G. et al. Experimental quantum error correction. Phys. Rev. Lett. 81, 2152-2155 (1998).  
10. Schindler, P. et al. Experimental repetitive quantum error correction. Science (1979) 332, 1059-1061 (2011).  
11. Reed, M. D. et al. Realization of three-qubit quantum error correction with superconducting circuits. Nature 482, 382-385 (2012).  
12. Feynman, R. P. Simulating physics with computers. Int. J. Theor. Phys. 21, 467-488 (1982).  
13. Shor, P. W. Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. SIAM J. Comput. 26, 1484-1509 (1997).  
14. Nielsen, M. A. & Chuang, I. L. Quantum Computation and Quantum Information (Cambridge Univ. Press, 2000).  
15. Knill, E., Laflamme, R., Martinez, R. & Negrevergne, C. Benchmarking quantum computers: the five-qubit error correcting code. Phys. Rev. Lett. 86, 5811-5814 (2001).  
16. Egan, L. et al. Fault-tolerant control of an error-corrected qubit. Nature 598, 281-286 (2021).  
17. Waldherr, G. et al. Quantum error correction in a solid-state hybrid spin register. Nature 506, 204-207 (2014).  
18. Kelly, J. et al. State preservation by repetitive error detection in a superconducting quantum circuit. Nature 519, 66-69 (2015).  
19. Chen, Z. et al. Exponential suppression of bit or phase errors with cyclic error correction. Nature 595, 383-387 (2021).  
20. Veldhorst, M. et al. An addressable quantum dot qubit with fault-tolerant control-fidelity. Nat. Nanotechnol. 9, 981-985 (2014).  
21. Yoneda, J. et al. A quantum-dot spin qubit with coherence limited by charge noise and fidelity higher than  $99.9\%$ . Nat. Nanotechnol. 13, 102-106 (2018).

22. Yang, C. H. et al. Silicon quantum processor unit cell operation above one Kelvin. Nature 580, 350-354 (2020).  
23. Petit, L. et al. Universal quantum logic in hot silicon qubits. Nature 580, 355-359 (2020).  
24. Takeda, K. et al. Quantum tomography of an entangled three-qubit state in silicon. Nat. Nanotechnol. 16, 965-969 (2021).  
25. Philips, S. G. J. et al. Universal control of a six-qubit quantum processor in silicon. Preprint at https://arxiv.org/abs/2202.09252 (2022).  
26. Angus, S. J., Ferguson, A. J., Dzurak, A. S. & Clark, R. G. Gate-defined quantum dots in intrinsic silicon. Nano Lett. 7, 2051-2055 (2007).  
27. Pioro-Ladriere, M. et al. Electrically driven single-electron spin resonance in a slanting Zeeman field. Nat. Phys. 4, 776-779 (2008).  
28. Connors, E. J., Nelson, J. & Nichol, J. M. Rapid high-fidelity spin state readout in Si/SiGe quantum dots via RF reflectometry. Phys. Rev. Appl. 10, 024019 (2020).  
29. Noiri, A. et al. Radio-frequency detected fast charge sensing in undoped silicon quantum dots. Nano Lett. 20, 947-952 (2020).  
30. Elzerman, J. M. et al. Single-shot read-out of an individual electron spin in a quantum dot. Nature 430, 431-435 (2004).  
31. Baart, T. A. et al. Single-spin CCD. Nat. Nanotechnol. 11, 330-334 (2016).  
32. Barenco, A. et al. Elementary gates for quantum information. Phys. Rev. A 52, 3457-3467 (1995).  
33. Gullans, M. J. & Petta, J. R. Protocol for a resonantly driven three-qubit Toffoli gate with silicon spin qubits. Phys. Rev. B 100, 85419 (2019).  
34. Ma, dzik, M. T. et al. Conditional quantum operation of two exchange-coupled single-donor spin qubits in a MOS-compatible silicon device. Nat. Commun. 12, 181 (2021).  
35. Nakajima, T. et al. Robust single-shot spin measurement with  $99.5\%$  fidelity in a quantum dot array. Phys. Rev. Lett. 119, 017701 (2017).  
36. Blumoff, J. Z. et al. Fast and high-fidelity state preparation and measurement in triple-quantum-dot spin qubits. PRX Quantum 3, 10352 (2022).  
37. Ha, W. et al. A flexible design platform for Si/SiGe exchange-only qubits with low disorder. Nano Lett. 22, 1443-1448 (2021).  
38. Xue, X. et al. CMOS-based cryogenic control of silicon quantum circuits. Nature 593, 205-210 (2021).  
39. Watson, T. F. et al. A programmable two-qubit quantum processor in silicon. Nature 555, 633-637 (2018).  
40. Acin, A., Bruß, D., Lewenstein, M. & Sanpera, A. Classification of mixed three-qubit states. Phys. Rev. Lett. 87, 040401 (2001).  
41. Barends, R. et al. Superconducting quantum circuits at the surface code threshold for fault tolerance. Nature 508, 500-503 (2014).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/c743dd63f9daae40226ef7dd4e05dc52284387d7414203296e262bf0d0d63bcd.jpg)

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate

credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2022

# Methods

# Quantum dot device

The triple-quantum-dot device is identical to the one characterized in ref.  $^{24}$ . The device is fabricated using an isotopically natural, undoped Si/SiGe heterostructure. The ohmic contacts are made by phosphorus ion implantation. Standard electron-beam lithography and lift-off techniques are used to fabricate the overlapping aluminium gates and the micro-magnet.

# Experimental setup

The GHZ state tomography and the iToffoli gate characterization (Fig. 2) are performed using the experimental setup as described in ref. [24]. In what follows, we detail the modified experimental setup used for the QEC experiments in Figs. 3 and 4. The sample is cooled down in a dry dilution refrigerator (Oxford Instruments Triton 300) to a base electron temperature of around  $40\mathrm{mK}$ . The configuration of d.c. lines is the same as in the previous report [24]. Control pulses are generated by four Keysight M3201A arbitrary waveform generator modules in a Keysight M9019APXle chassis (16 channels running at  $500\mathrm{MSa s^{-1}}$ ). The plunger (P1, P2 and P3), barrier (B2 and B3) and sensor plunger gates are connected to the outputs of the arbitrary waveform generator, each of which is filtered by a Mini Circuits SBLP-39+ Bessel low-pass filter. The filtering results in a minimum pulse rise/fall time of approximately 15 ns. Microwave signals are generated by three vector microwave signal generators (two Keysight E8267D and a Rohde & Schwarz SGS100A with an SGU100A upconverter). Each microwave signal is single sideband I/Q modulated to prevent unintentional spin rotations owing to microwave carrier leakage. Furthermore, we use pulse modulation to further suppress the bleed-through signal during the initialization and readout stages. The outputs of the three signal generators are combined at room temperature and connected to the lower screening gate. Radio-frequency reflectometry is used for fast measurement of the charge sensor conductance. The right reservoir of the charge sensor quantum dot in Fig. 1b is connected to a tank circuit with an inductance of  $1.2\mu \mathrm{H}$  and a resonance frequency of  $181\mathrm{MHz}$ . The reflected signal is amplified and demodulated, then digitized using an Alazar Tech ATS9440 digitizer card.

# Three-spin initialization and measurement

The three-spin initialization and measurement are performed as follows. The numbers  $(n_{1}n_{2}n_{3})$  indicate the respective number of electrons in the left, centre and right quantum dots. We collect 400 to 3,000 single-shot outcomes to obtain the measured probabilities. The labels A-E represent the gate voltage configurations depicted in Extended Data Fig. 1c.

1. Unload electrons in the left and centre quantum dots by biasing gate voltages so that the ground state charge configuration is (001) (A). The duration is  $100~\mu \mathrm{s}$ .  
2. Initialize  $Q_{1}$  by means of spin-selective tunnelling by biasing the voltages so that the charge configuration is near the (101)-(001) boundary (B). The duration is  $750~\mu \mathrm{s}$ .  
3. Shuttle the electron in the left quantum dot to the centre quantum dot by biasing the voltages so that the ground charge configuration is (011) (C). No intentional gate voltage ramp is used. The typical pulse rise time is 15 ns owing to the low-pass filter. We wait for  $1\mu \mathrm{s}$  in the (011) configuration.  
4. Initialize  $\mathrm{Q}_1$  by means of spin-selective tunnelling by biasing the voltages so that the charge configuration is near the (011)-(111) boundary (D). The duration is  $750~\mu \mathrm{s}$ .  
5. Initialize  $\mathrm{Q}_3$  by means of spin-selective tunnelling by biasing the voltages so that the charge configuration is near the (110)-(111) boundary (E). The duration is  $750~\mu s$ .  
6. Qubit manipulation in the (111) configuration (F). The typical duration is  $5\mu s$ . There is an extra waiting time of  $50~\mu s$  to reduce the effect of heating by the microwave pulses.

7. Read out  $Q_{1}$  by means of spin-selective tunnelling by biasing the voltages so that the charge configuration is near the (011)-(111) boundary (D). The total duration is  $600~\mu \mathrm{s}$ . The data for readout is collected for the first  $200~\mu \mathrm{s}$ . The extra waiting time of  $400 - \mu \mathrm{s}$  duration facilitates the initialization of  $Q_{1}$ .  
8. Perform controlled rotation between  $Q_{1}$  and  $Q_{2}$  to project the  $Q_{2}$  state to  $Q_{1}$  in (111). Here we pulse the virtual B2 gate to turn on  $J_{12}$  at the charge-symmetry point. Because  $Q_{1}$  is initialized to a spin-down state during the previous readout stage, for a  $Q_{2}$  input state  $\alpha | \uparrow \rangle + \beta | \downarrow \rangle$ , the resulting  $Q_{1}Q_{2}$  state is  $\alpha | \uparrow \downarrow \rangle + e^{i\theta} \beta | \downarrow \uparrow \rangle$ , in which  $e^{i\theta}$  is a phase factor that does not affect the readout. The duration is 1 μs. There is an extra waiting time of 50 μs to reduce the effect of heating by the microwave pulse.  
9. Read out  $\mathrm{Q}_2$  by means of spin-selective tunnelling of  $\mathrm{Q}_1$  by biasing the voltages so that the charge configuration is near the (011)-(111) boundary (D). The duration is  $200~\mu \mathrm{s}$ .  
10. Read out  $\mathrm{Q}_3$  by means of spin-selective tunnelling by biasing the voltages so that the charge configuration is near the (110)-(111) boundary (E). The duration is  $500~\mu s$ .

# Virtual gate

The effect of capacitive couplings between the gates is suppressed by the virtual gate technique. We measure the capacitive couplings between the gates and construct the virtual gate as follows. The crosstalk between the exchange couplings is not taken into account. The virtual gate voltages vB2 and vB3 are used to control the exchange couplings.

$$
\left( \begin{array}{c} v P 1 \\ v B 2 \\ v P 2 \\ v B 3 \\ v P 3 \end{array} \right) = \left( \begin{array}{c c c c c c} 1 & 0. 3 0 & 0. 5 4 & 0. 1 4 & 0. 1 7 \\ 0 & 1 & 0 & 0 & 0 \\ 0. 6 1 & 0. 3 5 & 1 & 0. 2 5 & 0. 3 1 \\ 0 & 0 & 0 & 1 & 0 \\ 0. 1 5 & 0. 1 0 & 0. 4 6 & 0. 3 1 & 1 \end{array} \right) \left( \begin{array}{c} \Delta P 1 \\ \Delta B 2 \\ \Delta P 2 \\ \Delta B 3 \\ \Delta P 3 \end{array} \right).
$$

# Single-qubit and two-qubit gates

The single-qubit rotations about the  $x$  and  $y$  axes are performed by applying microwave voltage pulses resonant with the Zeeman splitting of each spin qubit. The microwave voltage results in an effective out-of-plane a.c. magnetic field by the micro-magnet, which induces electric-dipolespin resonance. Thespin qubits have typical resonance frequencies of 19,942.6 MHz  $(Q_{1})$ , 20,372.6 MHz  $(Q_{2})$  and 20,923.2 MHz  $(Q_{3})$ . We use a shaped raised-cosine pulse with a duration of 124 (62) ns to implement a single-qubit  $\pi$  ( $\pi/2$ ) pulse. For the spectroscopy measurements in Fig. 2f, we use a Gaussian pulse (truncated at  $\pm 2\sigma$ ). The phase rotation is virtually implemented by shifting the reference phase of the I/Q modulation waveform. Wherever possible, the single-qubit gates are applied in parallel. The two-qubit CZ gate is implemented by adiabatically pulsing the exchange coupling by the barrier gates. To guarantee the adiabaticity, we use a shaped cosine pulse with a duration of 50 ns to implement the CZ/2 gates, which results in a nominal peak exchange coupling of 10 MHz. During the experiments in the main text, the coupling strengths are fine-tuned to account for the conditional phase accumulation owing to the residual couplings of about 0.2 MHz (Extended Data Fig. 3d–f). We set the minimum interval between pulses to 20 ns to avoid the pulse interference owing to reflection.

# Three-qubitToffoligate

The resonantly driven iToffoli gate consists of the three stages in Extended Data Fig. 5a. In the main text, the population transfer property of the iToffoli gate is shown. For that, we set  $f_{\mathrm{Rabi}} = J / \sqrt{3}$  ( $J = J_{12} = J_{23}$ ) so that the off-resonant rotation in the  $Q_1Q_3 = |\uparrow \downarrow \rangle / |\downarrow \uparrow \rangle$  subspaces is a  $2\pi$  rotation. Furthermore, to obtain a correct quantum action, any unwanted phase accumulations on the three-qubit state have to

# Article

be calibrated out. This can be achieved by setting an appropriate exchange pulse duration of  $t_{\mathrm{tot}} = t_{\mathrm{dc1}} + t_{\mathrm{MW}} + t_{\mathrm{dc2}}$  and pulse timing of  $\delta t = t_{\mathrm{dc1}} - t_{\mathrm{dc2}}$  (ref. 33). In theory, by setting the optimal exchange pulse duration to  $t_{\mathrm{tot}} = \pi (4 + \sqrt{3} - \sqrt{13}) / J$ , the conditional phases between the  $Q_1Q_3 = |\uparrow \downarrow \rangle$ ,  $|\downarrow \uparrow \rangle$  and  $|\uparrow \uparrow \rangle$  subspaces can be eliminated 32. For an exchange coupling of  $4.5\mathrm{MHz}$ , it is 473 ns. In the experiment, we typically use a 460-ns-long rectangular pulse, which is shorter than the theoretical length owing to the finite pulse bandwidth. The microwave pulse timing  $\delta t$  is then adjusted to eliminate the conditional phase between the  $Q_1Q_3 = |\downarrow \downarrow \rangle$  and the other subspaces. For the subspaces in which  $Q_2$  spin flip does not occur, shifting  $\delta t$  does not affect the outcome. In the case in which  $Q_2$  flips, when  $\delta t = 0$ , (quasi-)static phase accumulation is fully cancelled out by the spin-echo effect. The conditional phase in this case can be adjusted by varying  $\delta t$  because for finite  $\delta t$ , the echo works only partially and there is a phase accumulation of  $2\pi (f_1 - f_0)\delta t$ . The remaining single-qubit phase offset is removed by a virtual single-qubit phase rotation. The phase offsets on the ancilla qubits are uncalibrated in the QEC experiments, although they can be calibrated out similarly. In Extended Data Fig. 5b, we illustrate the experimental sequence to calibrate the iToffoli gate phase accumulation. Extended Data Fig. 5c shows an example of an uncalibrated iToffoli gate and Extended Data Fig. 5d shows a phase measurement after the calibration. In the QEC experiments, this calibration is performed just before the data acquisition to minimize the influence of the slow drift of the resonance frequencies.

# Readout error removal

For each of the experiments in which the readout errors are removed, we perform a reference measurement to obtain the readout fidelities. The spin-down (spin-up) readout fidelity  $F_{\downarrow i}(F_{\uparrow i})$  is directly obtained by preparing a spin-down (spin-up) state and a projective measurement of  $Q_{i}$ . Using the measured readout fidelities, we correct the raw probabilities

$\mathbf{P}_{\mathrm{M}} = (P_{\downarrow \downarrow \downarrow},\dots,P_{\uparrow \uparrow \uparrow})$  as  $\mathbf{P} = (F_1\otimes F_2\otimes F_3)^{-1}\mathbf{P}_{\mathrm{M}}$  , in which  $F_{i} = \left( \begin{array}{cc}F_{\downarrow i} & 1 - F_{\uparrow i}\\ 1 - F_{\downarrow i} & F_{\uparrow i} \end{array} \right)$  and  $\mathbf{P}$  is the corrected probabilities used for maximum likelihood estimation.

# Measurement of the iToffoligate truth table

To constrain all the elements of the truth table to be non-negative, we use a maximum likelihood procedure as follows. The input is a set of 64 measured probabilities  $P_{ij}$ , in which the input is the  $i$ th eigenstate and the measurement is projected at the  $j$ th eigenstate. The readout errors are removed following the procedure above. We then minimize a cost function  $C(P_{11}^{\mathrm{MLE}}, \dots, P_{88}^{\mathrm{MLE}}) = \sum_{i,j=1}^{8} (P_{ij}^{\mathrm{MLE}} - P_{ij})^2$  for non-negative parameters  $P_{ij}^{\mathrm{MLE}}$ . We constrain  $P_{ij}^{\mathrm{MLE}}$  so that the sum of probabilities in one cycle of data acquisition is unity, that is,  $\sum_{j=1}^{8} P_{ij}^{\mathrm{MLE}} = 1$ .

# Quantum state tomography

Owing to the noise in the experiment, the density matrix obtained by a linear inversion is not always physical. Therefore, we use a maximum likelihood estimation to restrict the density matrix to be physical. We start from a Cholesky decomposition of a physical density matrix  $\rho = T^{\dagger}T / \mathrm{Tr}(T^{\dagger}T)$ , in which  $T$  is a complex lower triangular matrix with real diagonal elements.  $T$  has  $2^{2D}$  ( $D$  is the number of qubits;  $D = 1$  in Fig. 4d and  $D = 3$  in Fig. 2d) real parameters  $\mathbf{t} = (t_{1},\dots,t_{2^{2D}})$  and we minimize the cost function

$$
C (\mathbf {t}) = \sum_ {\nu = 1} ^ {2 D} \frac {\left(\langle \psi_ {\nu} | \rho (\mathbf {t}) | \psi_ {\nu} \rangle - P _ {\nu}\right) ^ {2}}{2 \langle \psi_ {\nu} | \rho (\mathbf {t}) | \psi_ {\nu} \rangle},
$$

in which  $P_{\nu}$  is the measured probability projected at a basis  $|\psi_{\nu}\rangle$  .To determine the  $2^{2D}$  parameters, the projection outcomes for linearly independent pre-rotations (I, X/2, Y/2, X)  $\otimes^D$  are used. To remove the

error that could be introduced by the X pre-rotation, the projection outcomes for the X pre-rotations are calculated from the corresponding I rotation outcomes<sup>39</sup>.

# Quantum process tomography

We perform quantum process tomography to verify the process matrix and fidelity (Figs. 3 and 4 and Extended Data Fig. 5). The input state  $|\psi \rangle$  is prepared by a spin-down initialization followed by a single-qubit rotation  $R_{i} \in (1, X/2, Y/2, X)^{\otimes D}$  ( $D$  is the number of qubits;  $D = 1$  in Fig. 4b and  $D = 3$  in Extended Data Fig. 5e). After the quantum operations, tomographic readout of the resulting state is performed similarly to the case of quantum state tomography. For a quantum operation  $E$  acting on an input density matrix  $\rho_{\mathrm{in}}^{k}$ , the density matrix of the output state can be written as follows,

$$
E \left(\rho_ {\text {i n}} ^ {k}\right) = \sum_ {m, n = 1} ^ {2 ^ {D}} B _ {m} \rho_ {\text {i n}} ^ {k} B _ {n} ^ {\dagger} \chi_ {m n}, \tag {1}
$$

in which  $\chi$  is the process matrix defined with respect to the Pauli operators  $B = (1, \sigma_{\mathrm{x}}, \sigma_{\mathrm{y}}, \sigma_{\mathrm{z}})^{\otimes D}$ . Linear inversion of equation (1) can be performed to obtain a process matrix. However, the process matrix obtained in this way does not necessarily satisfy the physical conditions owing to the noise in the experiment. As in the state tomography, we can obtain an estimate of the physical process matrix by a maximum likelihood estimation. We start from a Cholesky decomposition  $\chi = S^{\dagger}S / \operatorname{Tr}(S^{\dagger}S)$ , in which  $S$  is a lower triangular matrix with real diagonal elements.  $S$  is parametrized by  $2^{4D}$  real parameters  $\mathbf{s} = (s_1, \dots, s_{2^{4D}})$  and we use a cost function  $L(\mathbf{s})$  as follows,

$$
L (\mathbf {s}) = \sum_ {k, l = 1} ^ {2 ^ {2 D}} \left[ P ^ {k l} - \sum_ {m, n = 1} ^ {2 ^ {2 D}} \chi_ {m n} \operatorname {T r} \left(M _ {l} B _ {m} \rho_ {\text {i n}} ^ {k} B _ {n} ^ {\dagger}\right) \right] ^ {2}, \tag {2}
$$

in which  $P^{kl}$  is the measured probability projected at  $|\downarrow\rangle (D = 1)$  or  $|\downarrow\downarrow\downarrow\rangle (D = 3)$  when an input state  $\rho_{\mathrm{in}}^k$  is prepared and an observable  $M_l$  is measured. We numerically minimize the cost function to obtain the most probable estimate of physical  $\chi$ . Then the process fidelity is calculated as  $\operatorname{Tr}(\chi_{\mathrm{ideal}}\chi)$ , in which  $\chi_{\mathrm{ideal}}$  is an ideal process matrix.

# Data availability

The data that support findings in this study are available from the Zenodo repository at https://doi.org/10.5281/zenodo.6601051.

42. Cramer, J. et al. Repeated quantum error correction on a continuously encoded qubit by real-time feedback. Nat. Commun. 7, 11526 (2016).  
43. Schwarz, G. Estimating the dimension of a model. Ann. Stat. 6, 461-464 (1978).  
44. Akaike, H. in Selected Papers of Hirotugu Akaike. Springer Series in Statistics (eds Parzen, E., Tanabe, K. & Kitagawa, G.) 199-213 (Springer, 1998).  
45. Kass, R. E. & Raftery, A. E. Bayes factors. J. Am. Stat. Assoc. 90, 773-795 (1995).

Acknowledgements This work was supported financially by Core Research for Evolutional Science and Technology (CREST), Japan Science and Technology Agency (JST) (JPMJCR15N2 and JPMJCR1675), JST Moonshot R&D grant no. JPMJMS2065, MEXT Quantum Leap Flagship Program (MEXT Q-LEAP) grant no. JPMXS0118069228 and JSPS KAKENHI grant nos. 18H01819, 19K14640 and 20H00237. T.N. acknowledges support from a Murata Science Foundation Research grant and JST PRESTO grant no. JPMJPR2017.

Author contributions K.T. and A.N. fabricated the device and performed the measurements. T.N. and T.K. contributed the data acquisition and discussed the results. K.T. wrote the paper with input from all co-authors. S.T. supervised the project.

Competing interests The authors declare that they have no competing interests.

# Additional information

Correspondence and requests for materials should be addressed to Kenta Takeda or Seigo Tarucha.  
Peer review information Nature thanks Stephen Bartlett, Joseph Kerckhoff and Arne Laucht for their contribution to the peer review of this work. Peer reviewer reports are available.  
Reprints and permissions information is available at http://www.nature.com/reprints.

![](images/a6d83676938d8b928339d1ff6a1f59a17985d8f76ec55e38805d7f526f360905.jpg)

![](images/ddb94cecb2ec9f9259258bca3b7ac4aaee40f95e154b2975c212a1166f50bd54.jpg)

![](images/a0009add692e2ab51c0d51af5bfb27ac107180d9bb4aa36a7231f7b89b31a7a3.jpg)  
Extended Data Fig.1| Three-spin initialization and measurement. The numbers  $(n_{1}n_{2}n_{3})$  represent the respective electron occupations in the right, centre and left quantum dots. The light blue circles with labels A-F show the initialization, readout and manipulation bias configurations. a, Charge stability diagram measured as a function of the P1 and P3 gate voltages. The variation of the background signal is due to the Coulomb oscillation of the  
sensor quantum dot. b, Charge stability diagram measured as a function of the P1 and P2 gate voltages. The dashed white lines are guides to the eye for the position of faint charge transition lines, which could be visible by retuning of the sensor quantum dot. c, Schematic of the three-spin initialization and measurement.

![](images/cac1be26ec6629b873c81f4f87be116eda38b88bdeb20cc0166694946cdacd6f.jpg)  
a

![](images/972302f4a4b409e7eb351b906b6b44662c7af7c6587b7ed1a7df8a8265bb3c53.jpg)  
b

![](images/f41a3a9d23f4b422c7b1a77c15b2e8c469bbcc66215fc2077e6e4630a27a6fa4.jpg)  
C

![](images/6348c235722233e217e701ff40134ec8818e222e10ee392decd573641aa07927.jpg)  
d

e  
![](images/e5976c35218dfab8ec2c3127ec7c5398a569a6cac5e969e5c98221d03b9cf775.jpg)  
C: random Clifford gate  $C_{R}$ : recovery Clifford gate

![](images/82de8650eae76626844a684f693c4503b8528a9d3623ae61bef0d6f4d31f195e.jpg)  
f

![](images/084e4116daad1e2636fbff321830bd7cc1fca4b5f62db7cab5f4b54feae8b263.jpg)  
Extended Data Fig. 2 | Single-qubit rotations. All measurements are performed with all qubits initialized to spin-down and the exchange couplings turned off. a, Rabi oscillation measurement sequence.  $t_{\mathrm{p}}$  is the duration of the microwave pulse. b-d, Rabi oscillation measurement results. The microwave amplitude is adjusted so that the Rabi frequency is 4 MHz. e, Schematic sequence of the randomized benchmarking measurement. We prepare 16 randomly generated Clifford gate sequences and average the outcomes to obtain the sequence fidelities. f-h, Randomized benchmarking results. The implementation is the same as in, for example, refs. 724. We perform two sets of benchmarking measurements, one designed to obtain an ideal spin-up  
g  
outcome and the other designed to obtain an ideal spin-down outcome, wherein both cases the measurement is projected at a spin-up state. The sequence fidelity  $F(m)$  is then defined as  $F(m) = F_{\uparrow}(m) - F_{\downarrow}(m)$ , in which  $F_{\uparrow}(m)$  ( $F_{\downarrow}(m)$ ) is the measured sequence fidelity for the spin-up (spin-down) final state. Each dataset is fit by an exponential decay  $F(m) = Vp^{m}$  to extract the depolarizing parameter  $p$  and visibility  $V$ . The primitive gate fidelity shown in each figure is obtained as  $1 - (1 - p) / (2 \times 1.875)$ , in which the factor 1.875 is the average number of primitive gates per Clifford gate. The errors are  $1\sigma$  from the mean.

![](images/3fc90c841c293dc12f3ee9019f7bb2d43517a670e187c38b9379e6b08f6ad4ea.jpg)  
h

![](images/f8e037012548f1a4b20ccb6de316b8feed2f4ae58db221b2ebf0062cd1050414.jpg)  
a

![](images/5d3d0bb613f153b71932e78474717f574d2360417df807fe72ab714806cf6e5c.jpg)  
e  
b

![](images/243f931d903bde43693a664de73c0022ec8947a270d1246bf62a1fc6eccbcd30.jpg)  
C  
f

![](images/4a0f6918dd7507d8ab87723c9db7172b479e2c99e4a5d3ad224a056844cbf7c7.jpg)  
d

![](images/12e39ac228ba17bbba3bedc9013a25b00bf57e5870d97835dae58099878a185c.jpg)

![](images/9715108592d016491c2f47581e34486c45e6a11d1af950e3d5e1bea5591cfaba.jpg)

![](images/03658c6502b15cfa297be6de94814eaef19f4dfdada919dcd14d171bede58fef.jpg)  
g

![](images/c07cb9c9d34c635c9442145306fed32572b0add0ff7724b6dc3236d24a1e1f0b.jpg)  
h  
Extended Data Fig. 3 | Two-qubit couplings. All measurements are performed with all qubits initialized to spin-down. a, Schematic sequence of the exchange spectroscopy measurement. To narrow the resonance peaks, the microwave power for the controlled rotation is decreased by 12 dB from the values used for single-qubit rotations. vBi  $(i = 2, 3)$  represents a virtual barrier gate voltage. b,c, Results of the exchange spectroscopy measurements. In each figure, the separation of the two peaks corresponds to the exchange coupling. The background slope of the resonance frequency is due to the displacement of the quantum dot position in the micro-magnet field gradient. The frequency offset from the values in Methods is due to the decay of the persistent current in the

![](images/231cf4e279bf6b478da01ce76079a50e102ba8a3c56b6f2642b2f4eff771e2e8.jpg)  
i  
superconducting magnet. d, Schematic sequence of the residual exchange-coupling measurement. e,f, Results of the measurement of residual exchange couplings between neighbouring qubits. Each dataset is fit with a sinusoidal function  $P(t_{\mathrm{evol}}) = V \sin(\pi t_{\mathrm{evol}} J_{\mathrm{off}})$  to extract the residual exchange coupling  $J_{\mathrm{off}}$ . Vis the visibility of the oscillation. The errors are  $1\sigma$  from the mean. g, Schematic sequence of the decoupled CZ oscillation measurement. h,i Typical decoupled CZ oscillations. The solid lines show the fit to a Gaussian decay. The decay times are  $3.27 \pm 0.08 \mu \mathrm{s} (\mathbf{h})$  and  $5.2 \pm 0.3 \mu \mathrm{s} (\mathbf{i})$ . Here we adjust the virtual barrier gate voltages so that the exchange coupling is roughly  $10 \mathrm{MHz}$ . All errors are  $1\sigma$  from the mean.

![](images/f3c495d570799dbac64bfae8a12f1cc157cd548eacc4f01d6cbf9038f292bae1.jpg)  
a

![](images/328d67016b8622f196ae422fdde30a6fbef0f969c2bec5e93f8f254b774b7620.jpg)  
b  
f

![](images/723259884b5fb382fe7d26538523dc21091e7841d43ff962105e0ee50624f7c8.jpg)  
C

![](images/2c36d43bea35a0ce9955dfa9387e9571604a224566f7c33c708fdc7226c3039a.jpg)  
d

![](images/7558e732351d4a56da5f96307f163ce899d93dc945d83320ffb9ced74e92125f.jpg)  
e

![](images/322430b083827711171e05ed49ba7a614ab33406ecdf31b0e0449a8c8dd25187.jpg)

![](images/46f23cde8651bf35078ab81e18c696064a4a06f151a2e3b37e673dcfd278642d.jpg)  
g

![](images/3d630a68359aad37abeec447b901c4f2762b86b5bdb9b59b91b2d09ec7e7a739.jpg)  
h

![](images/6a027ddb7dcf0b19d68cae4700bfdf4737c79d07b3d3555231ea84dd1f3d5bab.jpg)  
i

![](images/27eb3e13023f26889d71da7e654a2f4267ae6893284f939259b6108b4f2100f7.jpg)  
j  
Extended Data Fig. 4 | Coherence times. All measurements are performed with all qubits initialized to spin-down and the exchange couplings turned off. All errors are  $1\sigma$  from the mean. a, Schematic sequence of the  $T_{1}$  measurement. The qubit state is measured after the preparation of a spin-up excited state and an idle time of  $t_{\mathrm{w}}$ . b-d,  $T_{1}$  measurement results. Each dataset is fit by an exponential decay to extract the  $T_{1}$  relaxation time. e, Schematic sequence of the Ramsey interferometry. Instead of detuning the microwave frequency, we vary the phase of the second microwave pulse as  $\theta = 2\pi t_{\mathrm{evol}} \times (2\mathrm{MHz})$  such that we observe an oscillation at about  $2\mathrm{MHz}$ . f-h, Ramsey interferometry measurement results. To extract the  $T_{2}^{*}$  inhomogeneous dephasing time, each dataset is fitted with a Gaussian decay function  $P(t_{\mathrm{evol}}) = A\exp \left(-\left(\frac{t_{\mathrm{evol}}}{T_{2}^{*}}\right)^{2}\right)\cos(2\pi (\delta f)t_{\mathrm{evol}} + \phi) + B$ ,

![](images/0fbffb20398df46e7d15d0244cd83a3dcd9ac693991fc841a6a951edd53d3224.jpg)  
k  
in which  $A$  and  $B$  are the constants to account for the readout fidelities,  $\delta f$  is the oscillation frequency and  $\phi$  is the phase offset. The integration time is about 70 s for all traces. The larger scattering of the data points for  $Q_{2}(\mathbf{g})$  is due to the longer pulse cycle and less averaging. i, Schematic sequence of the Hahn echo measurement. j-I, Hahn echo results. For each dataset, the echo time  $T_{2}^{\mathrm{H}}$  is extracted by fitting with an exponential decay function  $P(t_{\mathrm{evol}}) = V\exp \left(-\left(\frac{t_{\mathrm{evol}}}{T_{2}^{\mathrm{H}}}\right)^{\gamma}\right)$ , in which  $V$  is the visibility and  $\gamma$  is the exponent. The exponents are  $\gamma = 0.98 \pm 0.09$  (Q1), 1.46 ± 0.05 (Q2) and 1.83 ± 0.07 (Q3).

![](images/1eeb13fcdc1bd550447e3cc3e6d55c8b62fbb7fb98c7ef8e97c366a745cc7d37.jpg)  
1

![](images/df5dc715d11e92ed628bedf3ef1992f8fefc68e9cccecae144ff02481b8f0860.jpg)  
a

![](images/2e5d4889fdd56342c537898c17850cfa8da02dfd35948862444ad78c7b728b65.jpg)  
C

![](images/f3801ea457b5ea78efad7e7fb3c0bf80f38ed358f1c785667c9ccbae2537db11.jpg)

![](images/2949d8eb0093ea63b5e0d51b9b30c55f239ab2fb8115c8197aa4caa688525d52.jpg)

![](images/87f8effc010d67729408d33a467caaa9a2760714da6e40e86343a41fe2b68bd4.jpg)

![](images/32dbbc49a52859c961de322dfa48d37270136972b8b719375911b7de2f90d066.jpg)  
d

![](images/a97ae70e055d5c2a5e27cd48bf4521e297984f4ae19749ea05f76f876c55fc61.jpg)  
b

![](images/6df091a3d2c95d506aa4881c9822e8031bc6c7c3de4a4b96d4825cc8b1029090.jpg)  
e  
Extended Data Fig. 5 | iToffoli gate characterizations. a, Schematic of the iToffoli gate implementation. The iToffoli gate can be realized by a combination of an exchange pulse and a microwave pulse. The exchange pulse duration  $(t_{\mathrm{dc1}} + t_{\mathrm{MW}} + t_{\mathrm{dc2}})$ , microwave pulse duration  $(t_{\mathrm{MW}})$  and timing  $(t_{\mathrm{dc1}} - t_{\mathrm{dc2}})$  are fine-tuned to obtain a correct phase evolution. b, Quantum circuit used to measure the phase accumulation during the iToffoli gate operation. The iToffoli gate is interleaved between two  $\pi/2$  pulses to realize Ramsey-type phase detection. Only when  $Q_1Q_3 = |\downarrow \downarrow\rangle$  does a spin flip occur, which is detected as a  $\pi$  phase shift for a correct iToffoli gate. For the other ancilla qubit configurations, the phase accumulation should be zero. c, Example phase measurement result before the iToffoli gate phase calibration. The resonance frequency and microwave amplitude are calibrated. d, Phase measurement after the calibration of both conditional and unconditional phases. In the calibration procedure, we optimize the duration of the exchange pulse and the timing of the microwave pulse

![](images/f07a77ba4d5c6d1591e5e3a710e808e8660756308a5a200c9d1c791a768154f3.jpg)  
f  
(see Methods). We obtain correct phase evolution for all ancilla qubit configurations. The phase offsets are  $(1.03\pm 0.01)\pi$ ,  $(0.04\pm 0.01)\pi$ ,  $(0.03\pm 0.01)\pi$  and  $(0.05\pm 0.01)\pi$  for  $Q_{1}Q_{3} = |\downarrow \downarrow\rangle$ ,  $|\uparrow \downarrow\rangle$ ,  $|\downarrow \uparrow\rangle$  and  $|\uparrow \uparrow\rangle$ , respectively. The errors are  $1\sigma$  from the mean. e, Experimental process matrix ( $\chi$  matrix) of the iToffoli gate obtained by three-qubit quantum process tomography (see Methods). The labels represent three-qubit Pauli operators. We obtain a gate fidelity of 0.67 from the data. f, Ideal process matrix of iToffoli gate. g, Simulated process matrix of iToffoli gate under quasi-static single-qubit phase noise. Here we assume  $T_{2}^{*} = 1.2$ , 1.2 and  $1.3~\mu s$  for  $Q_{1}$ ,  $Q_{2}$  and  $Q_{3}$ , respectively (ergodic  $T_{2}^{*}$  measured for long integration time). The effect of charge-noise-induced exchange fluctuation (noise in ZZ term) is not taken into account. The simulation reproduces some features in the experimental data. The gate fidelity estimated from the simulation is 0.69, which agrees well with the experimental result.

![](images/298e3b037cd1e5b89cb6bbf435352623813c05607128f42766b12de718efee30.jpg)  
g

![](images/10b5c60e62a6126a4877e3f4df7926d1dab8032432ffd2a68a0b7ebea638cade.jpg)  
Quadratic fit,  $a + cp^2 +dp^3$ $(\mathrm{AIC} = -173,\mathrm{BIC} = -170)$  
Data for corrected qubit  
Third-order polynomial fit,  $a + bp + cp^2 + dp^3$  (AIC = -171, BIC = -167)  
Linear fit,  $a + bp$ $(\mathrm{AIC} = -127,\mathrm{BIC} = -125)$

# Extended Data Fig. 6 | Comparison of different models for QEC result.

Comparison of the fitting results of quadratic  $(a + cp^2 + dp^3)$ , third-order polynomial  $(a + bp + cp^2 + dp^3)$  and linear functions  $(a + bp)$ . The coefficients  $a$ ,  $b$ ,  $c$  and  $d$  are the fitting parameters. We obtain  $a = 0.879 \pm 0.006$ ,

$c = -2.72 \pm 0.06$  and  $d = 1.89 \pm 0.06$  (quadratic function),  $a = 0.88 \pm 0.01$ ,

$b = 0.0\pm 0.1,c = -2.75\pm 0.24$  and  $d = 1.91\pm 0.16$  (third-order polynomial

function), and  $a = 0.94 \pm 0.02$  and  $b = -1.00 \pm 0.03$  (linear function) from the

fitting results. To compare the fitting results by different models, we calculate

the Bayesian information criterion $^{43}$  (BIC) and the Akaike information criterion $^{44}$  (AIC). Models with lower BIC are preferred, whereas models with lower AIC provide better prediction of the experimental behaviour. The difference between the linear fit and the others is found to be decisive $^{45}$ $(|\Delta \mathrm{BIC}| \approx 50)$ . In addition, although the difference is not as large  $(|\Delta \mathrm{BIC}| \approx 3)$ , the quadratic fit without the first-order term is more preferred than the polynomial function including the first-order term. The errors are  $1\sigma$  from the mean.

Extended Data Table 1 | Evolution of three-qubit state during QEC  

<table><tr><td></td><td>Q1 error</td><td>Q2 error</td><td>Q3 error</td></tr><tr><td>Encoded</td><td></td><td>α|+++) + β|---)</td><td></td></tr><tr><td>Error</td><td>α(√1-p|++) + √p|−++) +β(√1-p|−--) + √p|+--)</td><td>α(√1-p|++) + √p|+++) +β(√1-p|−--) + √p|+--)</td><td>α(√1-p|++) + √p|++-) +β(√1-p|−--) + √p|−++)</td></tr><tr><td>Decoded (Q2Q1Q3)</td><td>(α↓) + β↑)(√1-p|↓↓) + √p|↑↓)</td><td>√1-p(α↓) + β↑) |↓↓+ √p(β↓) + α↑) |↑↑</td><td>(α↓) + β↑)(√1-p|↓↓) + √p|↓↑)</td></tr><tr><td>Corrected (Q2Q1Q3)</td><td>(α↓) + β↑)(√1-p|↑↑) + √p|↓↑)</td><td>(α↓) + β↑)(√1-p|↑↑) + i√p|↓↓)</td><td>(α↓) + β↑)(√1-p|↑↑) + √p|↑↓)</td></tr><tr><td>Error syndrome</td><td>|↓↑)</td><td>|↓↓)</td><td>|↑↓)</td></tr></table>

The  $Q_{2}$  input state  $a|\downarrow\rangle + \beta|↑\rangle$  is encoded to the three-qubit state  $a|++\rangle + \beta|--\rangle$ . For the decoded and corrected states, we write  $Q_{2}$  first for the sake of brevity. When the error is a coherent phase rotation  $Z(\theta)$ , the error coefficient  $\sqrt{p} (\sqrt{1 - p})$  is replaced with  $-\mathrm{isin}(\theta / 2)(\cos(\theta / 2))$ , whereas the result remains essentially equivalent.