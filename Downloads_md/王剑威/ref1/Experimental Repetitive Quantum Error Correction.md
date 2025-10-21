38. J. B. Tenenbaum, C. Kemp, T. L. Griffiths, N. D. Goodman, Science 331, 1279 (2011).  
39. P. Sinha, B. Balas, Y. Ostrovsky, J. Wulff, in Object Categorization: Computer and Human Vision Perspectives, S. J. Dickinson, A. Leonardis, B. Schiele, M. J. Tarr, Eds. (Cambridge Univ. Press, Cambridge, 2009), pp. 301-323.  
40. G. Gergely, G. Csibra, Trends Cogn. Sci. 7, 287 (2003).  
41. C. L. Baker, R. Saxe, J. B. Tenenbaum, Cognition 113, 329 (2009).  
Acknowledgments: The research was supported by grants Friuli-Venezia-Giulia "PsyScope XL," Ministerio

de Ciencia E Innovacion PSI2009-08232PSIC, the James S. McDonnell Foundation Causal Learning Research Collaborative grant, Office of Naval Research grants N00014-09-0124 and N00014-07-1-0937, Army Research Office MURI W911NF-08-1-0242, the Swiss and Global-Fondazione Ca' Foscari, and Marie Curie 035975 Disorders and Coherence of the Embodied Self. E.T. and L.L.B. designed the experiments and analyzed the data. E.T. ran the experiments. J.B.T. and E.V. conceived the model and the simulations. E.T., E.V., J.B.T., and L.L.B. wrote the paper. All authors discussed the research and revised the text and the analyses. We thank D. Amati, L. Filippin, F. Gandolfo, N. Goodman, A. Isaja, and

N. Sebastian for support and suggestions. J. Mehler and the Language, Cognition, and Development Laboratory in Trieste, Italy made the experimental work possible. We are deeply grateful to them.

Supporting Online Material

www.sciencemag.org/cgi/content/full/332/6033/1054/DC1

Materials and Methods

Figs. S1 to S8

Movies S1 to S5

12 August 2010; accepted 21 April 2011

10.1126/science.1196404

# REPORTS

# Experimental Repetitive Quantum Error Correction

Philipp Schindler, $^{1}$  Julio T. Barreiro, $^{1}$  Thomas Monz, $^{1}$  Volckmar Nebendahl, $^{2}$  Daniel Nigg, $^{1}$  Michael Chwalla, $^{1,3}$  Markus Henrich, $^{1*}$  Rainer Blatt $^{1,3}$

The computational potential of a quantum processor can only be unleashed if errors during a quantum computation can be controlled and corrected for. Quantum error correction works if imperfections of quantum gate operations and measurements are below a certain threshold and corrections can be applied repeatedly. We implement multiple quantum error correction cycles for phase-flip errors on qubits encoded with trapped ions. Errors are corrected by a quantum-feedback algorithm using high-fidelity gate operations and a reset technique for the auxiliary qubits. Up to three consecutive correction cycles are realized, and the behavior of the algorithm for different noise environments is analyzed.

Information in a quantum computer is extremely vulnerable to noise induced by the environment and thus needs to be protected with quantum error correction (QEC) techniques. Pioneering theoretical work in this field has shown that all errors can be corrected for if imperfections of the quantum operations and measurements are below a certain (error) threshold and the correction can be applied repeatedly (1-3). Such error thresholds depend on details of the physical system, and quantifying them requires a careful analysis of the system-specific errors, the en- and decoding procedures, and their respective implementation (4). It is currently accepted that gate error probabilities ranging from  $10^{-4}$  to  $10^{-5}$  are tolerable (5), which seem to be in reach with technical improvements in conjunction with dynamical control techniques (6). In addition, fault-tolerant operation requires highly efficient, repeatable algorithms to minimize the computational overhead. So far, all experimental implementations (7-12) are limited to a single correction cycle, where the only experimental implementation in a scalable system (10) relies on projective mea

surements and classical feedback. Because high-fidelity measurements take time and potentially disturb the qubit system, it can be advantageous to use a measurement-free QEC algorithm based on implicit quantum feedback (4, 7). Also, in contrast to previous expectations (13), these measurement-free protocols lead to error thresholds comparable to those of their measurement-based counterparts (14).

We demonstrate repeated QEC with a system of trapped  $^{40}\mathrm{Ca}^{+}$ ions as qubits, and multiple repetitions of the algorithm are enabled by a toolbox consisting of high-fidelity quantum operations (15, 16), an optimized pulse sequence (17), and a qubit-reset technique that has a negligible effect on the system of qubits. The performance of the implementation is assessed with quantum process tomography in the presence of phase-flip errors, and its behavior is analyzed for different environments that show correlated and uncorrelated phase noise. Our approach is based on the three-qubit repetition code capable of detecting and correcting phase-flip errors on a single qubit (1, 4). This algorithm protects against phase noise, which is the dominant error source in our ion-trap quantum computer, causing gate errors as well as decoherence.

As indicated in Fig. 1A, each QEC cycle consists of (i) encoding the system qubit  $\{|0\rangle ,|1\rangle \}$  and two auxiliary qubits (ancillas) into an entangled state, (ii) error incidence, (iii) detecting and correcting the error, and (iv) resetting the

ancillas. Initially, the qubit to be protected is in the state  $|\Psi \rangle = \alpha | + \rangle +\beta | - \rangle$  , where  $|\pm \rangle = 1 / \sqrt{2}$ $(|0\rangle \pm |1\rangle)$  , and the two ancilla qubits are both prepared in the state  $|1\rangle$  . In the encoding stage, they are mapped into the entangled state  $\alpha | + + + \rangle$ $+\beta | - - - \rangle$  Next, a single-qubit phase-flip error may change  $|\pm \rangle$  to  $|\mp \rangle$  .In the decoding and correction stage, the error is identified by a simple majority vote, and the system qubit is corrected accordingly. It should be noted that this protocol maps the information in and out of the protected state between QEC cycles. Each cycle is concluded by resetting the ancilla qubits while preserving the information on the system qubit.

The textbook implementation of a single cycle of this QEC procedure would consist of a circuit using four controlled-NOT (CNOT) and one controlled controlled-NOT (Toffoli) gate operations (4) (Fig. 1B). Although the process fidelities of available CNOT  $(92\%)$  (18) and Toffoli  $(80\%)$  (19) implementations could possibly be improved, it seems more promising to pursue an approach based on global Mølmer-Sørensen entangling gate operations (fidelity of  $99\%$  ) (15, 20). These operations provide a universal set of gates in combination with individually addressed Stark-shift gates and collective single-qubit rotations (17, 21). Moreover, the optimization procedure of (17) allows us to rigorously simplify the pulse sequence for a complete algorithm based on this set of gates. Two additional refinements lead to the algorithm used for the optimization (Fig. 1B). First, the space of optimized solutions is increased by adding an arbitrary unitary operation,  $U$ , acting only on the ancillas before resetting them. Second, the encoding stage can be simplified by adding an operation,  $D$ , and its inverse,  $D^{-1}$ , that commutes with any phase error. As a result, the encoding stage consists of a single entangling operation, and the decoding stage can be implemented with a total of eight pulses with only three entangling operations (Fig. 1C). Formally, this encoding implements a stabilizer code with the generators  $G = \{\sigma_y^{(1)}\sigma_z^{(2)}\sigma_y^{(3)},\sigma_y^{(1)}\sigma_y^{(2)}\sigma_z^{(3)}\}$ , which are tensor products of the Pauli operators  $\sigma_{x,y,z}^{(i)}$  acting on qubit  $i$  (4).

The QEC protocol is realized in an experimental system consisting of a string of three  $^{40}\mathrm{Ca}^+$  ions confined in a macroscopic linear Paul trap. Each

ion represents a qubit in the  $|1\rangle = 4S_{1 / 2}(m_{\mathrm{J}} = -1 / 2)$  and  $|0\rangle = 3D_{5 / 2}(m_{\mathrm{J}} = -1 / 2)$  states. The state of the qubits is then manipulated by a series of laser pulses resonant with the qubit transition. Our universal set of gates consists of (i) collective local operations,  $X(\Theta) = \exp (-iS_x\Theta /2)$  and  $Y(\Theta) = \exp (-iS_y\Theta /2)$ ; (ii) single-qubit operations,  $Z_{k}(\Theta) = \exp [-i\sigma_{z}^{(k)}\Theta /2]$ ; and (iii) collective entangling Mølmer-Sørensen (15, 16, 20) operations,  $Y^{2}(\Theta) = \exp (-iS_{y}^{2}\Theta /4)$ , with  $S_{x,y} = \sum_{k = 1}^{3}\sigma_{x,y}^{(k)}$ . The collective operations are realized with a wide beam exciting all ions simultaneously, and the single-qubit operations are performed with a tightly focused beam affecting only individual ions. An experimental cycle consists of cooling the ion string to the motional ground state, applying the manipulating laser pulses, and measuring the population of the qubit states. This procedure is repeated up to 1000 times to obtain the final quantum state of the qubits.

An important tool, critical to the repeated application of the QEC protocol, is the proper reset of the ancilla qubits, which is carried out with the optical-pumping technique (Fig. 1D). For the reset procedure, the population of the ancilla qubits in state  $|0\rangle$  is first transferred into the state  $|S^{\prime}\rangle = 4S_{1 / 2}(m_{\mathrm{J}} = +1 / 2)$  by using the addressed beam. This population in  $|S^{\prime}\rangle$  is then excited to the  $4P_{1 / 2}(m_{\mathrm{J}} = -1 / 2)$  level by a circularly polarized laser beam at a wavelength of  $397~\mathrm{nm}$ . Lastly, the population from the  $4P_{1 / 2}$  level spontaneously decays to the  $4S_{1 / 2}$  level (population loss into  $3D_{3 / 2}$  level is avoided by a repump laser resonant with the  $3D_{3 / 2} - 4P_{1 / 2}$  transition). The electronic state of the system qubit is not affected by the wide pumping laser because it couples only to the ancillas' population in  $|S^{\prime}\rangle$ . The effect on the moti- tional state of the ion string was calculated with a multilevel numerical simulation from which we estimate a heating rate of 0.015 phonons per reset step for our experimental parameters. Because the protocol uses only entangling operations of the Mølmer-Sørensen type, which are insensitive to the ion motion in first order, the reset has a negligible effect on the QEC protocol.

The operational quality of the QEC protocol can be assessed by exposing it to correctable errors, that is, single-qubit phase-flip errors. Ideally, the encoded qubit experiences an identity operation. Experimentally, the implemented process is characterized with quantum process tomography (22, 23), which yields a process matrix  $\chi$ . The performance of the implementation is given by the overlap of the identity process,  $\chi_{\mathrm{id}}$ , with the implemented process, also known as the process fidelity,  $F_{\mathrm{proc}} = \mathrm{Tr}(\chi \cdot \chi_{\mathrm{id}})$ . The achieved process fidelities for up to three repetitions (without inducing any errors),  $F_{\mathrm{none}}$ , are shown in Table 1. The process fidelity, however, does not distinguish between constant operational errors (that could be undone in principle) and decoherence (irreversible processes). A measure that is only sensitive to errors resulting from decoherence is the optimized process fidelity,  $F_{\mathrm{opt}}$ , as displayed in Table 1. It is defined as the maximum fidelity that could

be obtained if an additional fixed single-qubit rotation was perfectly implemented on the output state (24).

The error-correcting capability of the implementation is assessed by applying in each cycle either no-error or a single-qubit phase flip  $Z_{i}(\pi)$  on ion  $i$  (1 being the system ion and 2 and 3 being the first and second ancillas, respectively) followed by a process tomography for all combinations. Because these single-qubit errors are corrected by the algorithm, the ideal process is again the identity process. The mean process matrix,  $\overline{\chi}$ , is then reconstructed from the data obtained by averaging over all measured expectation values, as shown for zero to three correction cycles in Fig. 2. The results shown in Table 1 demonstrate that the optimized process fidelities with single-qubit errors,  $F_{\mathrm{opt}}$ , and without an induced error,  $F_{\mathrm{opt}}$ , are the same for one, two, and three correction cy

cles. From this data, we infer that the QEC protocol corrects single-qubit errors perfectly within our statistical uncertainty. The infidelities of the implementation are mainly caused by imperfections in the entangling gates as discussed in (24).

In addition to characterizing the implemented process in the presence of correctable errors, we investigate the algorithm's behavior in a dephasing environment, where also uncorrectable errors occur. For single qubits, a dephasing process can be described by a phase-flip probability  $p$ , which reduces the off-diagonal elements of the density matrix by a factor  $1 - 2p$  (for complete dephasing  $p = 0.5$ ). In a system of multiple qubits, the probability of simultaneous  $n$ -qubit phase flips, which cannot be corrected by the three-qubit QEC protocol, depends on the correlations between the qubits (24). We analyze the behavior of the QEC

![](images/8198b453d6133ecc110886fa735a675df3624bd985c805888bd69191d131deb2.jpg)  
Fig. 1. (A) Schematic view of three subsequent error-correction cycles. (B) Quantum circuit for the implemented phase-flip error-correction code. The operations labeled  $H$  are Hadamard gates. (C) Optimized pulse sequence implementing a single error-correction cycle. (D) Schematic of the reset procedure. The computational qubit is marked by filled dots. The reset procedure consists of (i) shelving the population from  $|0\rangle$  to  $|s^{\prime}\rangle = 4S_{1 / 2}(m_{1} = +1 / 2)$  and (ii) optical pumping to  $|1\rangle$  (straight blue arrow).

Table 1. Process fidelity for a single uncorrected qubit as well as for one, two, and three error-correction cycles.  $F_{\text{none}}$  is the process fidelity without inducing any errors.  $F_{\text{single}}$  is obtained by averaging over all single-qubit errors.  $F_{\text{opt}}$  and  $F_{\text{sopt}}$  are the respective process fidelities where constant operations are neglected. The statistical errors are derived from propagated statistics in the measured expectation values where the numbers in parentheses indicate one standard deviation. Dash entries indicate not applicable.  

<table><tr><td>Number of QEC cycles</td><td>No error Fnone</td><td>Optimized no error Fopt</td><td>Single-qubit errors Fsingle</td><td>Optimized single-qubit errors Fsopt</td></tr><tr><td>0</td><td>97(2)</td><td>97(2)</td><td>-</td><td>-</td></tr><tr><td>1</td><td>87.5(2)</td><td>90.1(2)</td><td>89.1(2)</td><td>90.1(2)</td></tr><tr><td>2</td><td>77.7(4)</td><td>79.8(4)</td><td>76.3(2)</td><td>80.1(2)</td></tr><tr><td>3</td><td>68.3(5)</td><td>72.9(5)</td><td>68.3(3)</td><td>70.2(3)</td></tr></table>

algorithm in the presence of the two most prominent noise types, namely uncorrelated and correlated phase noise, where the qubits are affected by independent or one and the same noise source, respectively. In our system, the inherent phase noise is correlated because it originates predominantly from fluctuations in the magnetic field strength and the laser frequency, which are both equal on all qubits (16). A controlled amount of this noise can be simply applied by inserting a waiting time between the encoding and the decoding stage. The second noise type, uncorrelated phase noise, can be engineered by performing a weak qubit projection (4), which is realized by a short laser pulse on the detection transition once the qubit is encoded (24). We characterized the phase noise by Ramsey-type experiments (24), which translate phase flips into bit flips. The presence of the respective noise type can then be verified by the probability of simultaneous  $n$ -qubit bit flips (Fig. 3A).

For both uncorrelated and correlated phase noise, our error correction algorithm performs as

depicted in Fig. 3B. Because uncorrectable two- and three-qubit phase flips occur more frequently in the presence of correlated noise (Fig. 3A), the QEC implementation yields lower fidelities. It should be noted though, that correlated phase noise can be completely eliminated by encoding the qubits in decoherence-free subspaces (DFS) (9, 25, 26) at the expense of a further increased complexity. For uncorrelated phase noise, no (DFS) exist, and therefore only quantum error correction can protect the qubit. In our implementation, a protected qubit shows less noise than an unencoded qubit for an error probability  $p$  larger than 0.15 (Fig. 3B). In the investigation with uncorrelated noise, the weak projection collapses each qubit with a small probability into the computational basis. Our data thus indicate that the algorithm can recover the quantum information from this single-qubit state collapse.

Our results demonstrate an implementation of a repeatable error correction algorithm in a system of three trapped-ion qubits. The use of global

![](images/e03c455fb159035e45087a7790db4e06b180ecc9afa91cf7669f5cbfb74e75e4.jpg)  
Fig. 2. Mean single-qubit process matrices  $\overline{\chi}_n$  (absolute value) for  $n$  QEC cycles with single-qubit errors. Transparent bars show the identity process matrix, and the red bar denotes a phase-flip error. These process matrices were reconstructed from a data set averaged over all possible single-qubit errors.

![](images/c2a4798256e4fb528348e61fbd26bbfbb17deb539cfb9b6daf002f2bf6de8413.jpg)  
Fig. 3. (A) Probability of simultaneous two-qubit phase flips as a function of the single-qubit phase flip probabilities for uncorrelated (square) and correlated (circle) noise measured by a Ramsey-type experiment. (B) Process fidelity of the QEC algorithm in the presence of correlated (circle) and uncorrelated (square) phase noise as a function of the single-qubit phase flip probability. The theory is shown for an unencoded qubit (solid line), a corrected qubit in presence of correlated (dashed line), and uncorrelated noise (dash-dot line). Error bars indicate one standard deviation derived from propagated statistics in the measured expectation values.

entangling and local-qubit operations in an optimized pulse sequence allows for very short and efficient QEC cycles. For uncorrelated errors, a (single-cycle) corrected qubit performs better than an uncorrected qubit for a range of error probabilities. The algorithm can be extended to a five-qubit implementation, where the qubit stays protected during error correction (17). Although technically challenging, such an implementation in conjunction with DFS encoding appears as a viable route toward quantum error correction for trapped ions.

# References and Notes

1. A. R. Calderbank, P. W. Shor, Phys. Rev. A 54, 1098 (1996).  
2. A. Steane, Proc. R. Soc. London Ser. A 452, 2551 (1996).  
3. J. Preskill, Proc. R. Soc. London Ser. A 454, 385 (1998).  
4. M. A. Nielsen, I. L. Chuang, Quantum Computation and Quantum Information (Cambridge Univ. Press, Cambridge, 2000).  
5. P. Aliferis, A. W. Cross, Phys. Rev. Lett. 98, 220502 (2007).  
6. K. Khodjasteh, D. A. Lidar, L. Viola, Phys. Rev. Lett. 104, 090501 (2010).  
7. D. G. Cory et al., Phys. Rev. Lett. 81, 2152 (1998).  
8. E. Knill, R. Laflamme, R. Martinez, C. Negrevergne, Phys. Rev. Lett. 86, 5811 (2001).  
9. N. Boulant, L. Viola, E. M. Fortunato, D. G. Cory, Phys. Rev. Lett. 94, 130501 (2005).  
10. J. Chiaverini et al., Nature 432, 602 (2004).  
11. T. Aoki et al., Nat. Phys. 5, 541 (2009).  
12. T. B. Pittman, B. C. Jacobs, J. D. Franson, Phys. Rev. A 71, 052332 (2005).  
13. D. P. DiVincenzo, P. Aliferis, Phys. Rev. Lett. 98, 020501 (2007).  
14. G. A. Paz-Silva, G. K. Brennen, J. Twamley, Phys. Rev. Lett. 105, 100501 (2010).  
15. J. Benhelm, G. Kirchmair, C. F. Roos, R. Blatt, Nat. Phys. 4, 463 (2008).  
16. T. Monz et al., Phys. Rev. Lett. 106, 130506 (2011).  
17. V. Nebendahl, H. Häffner, C. F. Roos, Phys. Rev. A 79, 012312 (2009).  
18. M. Riebe et al., Phys. Rev. Lett. 97, 220407 (2006).  
19. T. Monz et al., Phys. Rev. Lett. 102, 040501 (2009).  
20. A. Sorensen, K. Mølmer, Phys. Rev. Lett. 82, 1971 (1999).  
21. F. Schmidt-Kaler et al., Europhys. Lett. 65, 587 (2004).  
22. I. L. Chuang, M. A. Nielsen, J. Mod. Opt. 44, 2455 (1997).  
23. M. Riebe et al., N. J. Phys. 9, 211 (2007).  
24. Materials and methods are available as supporting material on Science Online.  
25. P. Zanardi, M. Rasetti, Phys. Rev. Lett. 79, 3306 (1997).  
26. D. A. Lidar, I. L. Chuang, K. B. Whaley, Phys. Rev. Lett. 81, 2594 (1998).  
Acknowledgments: We thank C. F. Roos for helpful discussions and R. Gerritsma, G. Paz-Silva, G. Brennen, and J. Twamley for carefully reading the manuscript. We gratefully acknowledge support by the Austrian Science Fund (FWF), by the European Commission [Scalable Quantum Computing with Light and Atoms (SCALA) and Atomic Quantum Technologies (AQUTE) projects], by the Institut für Quanteninformation GmbH, and by the European Research Council. This material is based on work supported in part by the Intelligence Advanced Research Projects Activity. J.T.B. acknowledges support by a Marie Curie International Incoming Fellowship within the 7th European Community Framework Programme.

# Supporting Online Material

www.sciencemag.org/cgi/content/full/332/6033/1059/DC1

Materials and Methods

Figs. S1 to S4

References

25 January 2011; accepted 23 March 2011

10.1126/science.1203329

This copy is for your personal, non-commercial use only.

If you wish to distribute this article to others, you can order high-quality copies for your colleagues, clients, or customers by clicking here.

Permission to republish or repurpose articles or portions of articles can be obtained by following the guidelines here.

The following resources related to this article are available online at www.sciencemag.org (this information is current as of June 17, 2015):

Updated information and services, including high-resolution figures, can be found in the online version of this article at: http://www.sciencemag.org/content/332/6033/1059.full.html

Supporting Online Material can be found at: http://www.sciencemag.org/content/suppl/2011/05/25/332.6033.1059.DC1.html

This article cites 24 articles, 2 of which can be accessed free: http://www.sciencemag.org/content/332/6033/1059.full.html#ref-list-1

This article has been cited by 6 articles hosted by HighWire Press; see: http://www.sciencemag.org/content/332/6033/1059.full.html#related-urls

This article appears in the following subject collections: Physics http://www.sciencemag.org/cgi/collection/physics