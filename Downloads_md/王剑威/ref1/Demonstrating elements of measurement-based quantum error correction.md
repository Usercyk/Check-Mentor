# Demonstrating elements of measurement-based quantum error correction

Stefanie Barz, $^{1,*}$  Rui Vasconcelos, $^{1}$  Chiara Greganti, $^{1}$  Michael Zwerger, $^{2,3}$  Wolfgang Dür, $^{2}$  Hans J. Briegel, $^{2,3}$  and Philip Walther $^{1}$

$^{1}$ University of Vienna, Faculty of Physics, Boltzmanngasse 5, 1090 Vienna, Austria  
 $^{2}$ Institut für Theoretische Physik, Universität Innsbruck, Technikerstraße 25, A-6020 Innsbruck, Austria  
 $^{3}$ Institut für Quantenoptik und Quanteninformation der Österreichischen Akademie der Wissenschaften, Innsbruck, Austria (Received 20 January 2014; published 2 October 2014)

In measurement-based quantum computing an algorithm is performed by measurements on highly entangled resource states. To date, several implementations were demonstrated, most of them assuming perfect noise-free environments. Here we consider measurement-based information processing in the presence of noise and demonstrate quantum error detection. We implement the protocol using a four-qubit photonic cluster state where we first encode a general qubit nonlocally such that phase errors can be detected. We then read out the error syndrome and analyze the output states after decoding. Our demonstration shows a building block for measurement-based quantum computing which is crucial for realistic scenarios.

DOI: 10.1103/PhysRevA.90.042302

PACS number(s): 03.67.Lx, 03.67.Ac, 03.67.Bg, 42.50.-p

# I. INTRODUCTION

Measurement-based quantum computation (MBQC) is a framework for quantum computation that offers conceptual and practical advantages as compared to the circuit model. The most prominent example of MBQC is the one-way model [1-4] where the two-dimensional cluster state [5] serves as a universal resource. Quantum information is processed by sequences of (adaptive) single-qubit measurements on a highly entangled resource state which is prepared beforehand, without the need to perform coherent gates. MBQC is particularly suited for systems such as photons where the coherent manipulation of quantum information by gates is difficult, but the preparation of entangled states is possible by some other means. The resource state preparation can even be probabilistic, without jeopardizing the deterministic character of the overall computation. When a measurement-based approach is applied to special-purpose quantum information processors, one finds that specific tasks can be performed with small resource states [6,7]. In particular, any quantum circuit acting on  $N$  qubits that only contains Clifford gates [8] can be implemented with a resource state of size  $2N$ , independent of the length of the circuit. What is more, ancilla particles that are at some stage of the algorithm measured in the Pauli basis do not increase the size of the resource state. It follows that several tasks, including entanglement purification [9] or quantum error correction (QEC) [10], can be performed very efficiently in a measurement-based way, i.e., with resource states of minimal size. As an additional bonus, one encounters a significantly increased robustness against noise and imperfections [9,10].

Several elements of MBQC and QEC have been demonstrated in photonic setups [11-21], including elementary gates with feedforward [22] as well as simple quantum algorithms [23], together with encoding quantum information in an error-correction code [24,25]. The scheme in Ref. [25] demonstrates topological error correction and protects a correlation rather than a qubit, and the scheme in Ref. [26] demonstrates

a (measurement-based) single-qubit rotation in the presence of photon loss, using a graph state. Recently, an experimental demonstration of error correction using a graph state code was realized [27] combining path and polarization encodings.

Here we demonstrate how quantum error detection including encoding, syndrome readout, and decoding, can be performed in a measurement-based fashion, thereby providing another building block for experimental MBQC. We implement in a photonic experiment a two-qubit error-detection code where the state of a qubit is encoded in two further qubits such that a phase error on one of these qubits can be detected. The code can also be viewed as a heralded error-correction code as a phase error can be corrected if it is known which particle is subjected to noise. We implement such errors, thereby also demonstrating the process of digitalization of errors and show the error detecting and correcting capabilities of the code by reading out the error syndrome and performing subsequent decoding. All steps in the protocol are achieved only by single-qubit measurements on a four-qubit cluster state, thanks to the fact that all required operations are of Clifford type.

# II. ERROR-DETECTION SCHEME

In this experiment, we demonstrate several important paradigms of quantum error correction within MBQC: encoding a qubit into a code word, nondestructive readout of the error syndrome, and decoding and digitalization of errors. Our protocol allows one to protect a general qubit  $|\psi \rangle = \alpha |0\rangle +\beta |1\rangle$ , where  $|\alpha |^2 +|\beta |^2 = 1$ , against phase noise. The main idea of our protocol is to encode the state of qubit  $|\psi \rangle$  in two further qubits using measurement-based quantum computing [10]. By measuring these qubits, a single  $Z = \sigma_{Z}$  error occurring on one of them can be flagged, where  $\sigma_{Z}$  is the Pauli operator—error detection. Furthermore, if the error only affects one of the qubits and it is known beforehand which one, then it is possible to deterministically recover the initially encoded state—error detection and correction.

In detail, the basis of our protocol is a four-qubit cluster state (see Fig. 1), the so-called box cluster state,

$$
\begin{array}{l} | \psi_ {\text {b o x}} \rangle = \frac {1}{2} [ | 0 \rangle_ {1} | + \rangle_ {2} | + \rangle_ {3} | 0 \rangle_ {4} + | 0 \rangle_ {1} | - \rangle_ {2} | - \rangle_ {3} | 1 \rangle_ {4} \\ + | 1 \rangle_ {1} | - \rangle_ {2} | - \rangle_ {3} | 0 \rangle_ {4} + | 1 \rangle_ {1} | + \rangle_ {2} | + \rangle_ {3} | 1 \rangle_ {4} ], \tag {1} \\ \end{array}
$$

![](images/e6f977715868d3c146f166d481626d5543d480404e5b4a6a6dbeb0ceec3ab69f.jpg)  
(a) Four-qubit  
resource state

![](images/d85922fa580bb00d0e11d81c5916ec907f2c477afb336143beb79ca5967bd79f.jpg)  
(b) Encoding

![](images/0e727e1379c856e4b06a6315880d6e72f45bb8ada82d133c749e543b074bdc65.jpg)  
(c) Syndrome readout and decoding

![](images/b652b97b10b3bfef083beabc82798fe270da5ad16da569efa3d46b3f6a65d1a0.jpg)  
(d) Error type  
FIG. 1. (Color online) Scheme of measurement-based error correction. (a) The four-qubit box cluster state forms the resource. (b) The state of qubit 1 is encoded in qubit 2 and qubit 3 by measuring it (see the main text for details). (c) An error occurs on qubit 3. (d) Measurement instruction for the syndrome readout and respective recovery operations for different error types. Here,  $Z_{2}(Z_{3})$  denotes a phase error on qubit 2 (3). The result of the measurements on qubit 2 and qubit 3 shows if a  $X = \sigma_{x}$  recovery operation needs to be applied to qubit 4. We present in the main text the analysis related to the green-framed boxes, and further results are shown in Appendices C and D.

where  $|\pm \rangle = (|0\rangle \pm |1\rangle) / \sqrt{2}$  are the eigenstates of the Pauli operator  $\sigma_{x} = X$ .

The steps of our protocol are then encoding, measurement of the error syndrome, and decoding.

First, the encoding is accomplished by a single-qubit measurement on qubit 1 in the basis  $\{\alpha^{*}|0\rangle +\beta^{*}|1\rangle ,\beta |0\rangle -\alpha |1\rangle \}$  (see Fig. 1). If qubit 1 is projected onto state  $\alpha^{*}|0\rangle +\beta^{*}|1\rangle$  state  $|\psi \rangle$  is encoded on qubit 2 and qubit 3, and the remaining three-qubit state can then be written as

$$
\begin{array}{l} | \psi_ {3} \rangle = \frac {\alpha}{\sqrt {2}} (| + + \rangle_ {2 3} | 0 \rangle_ {4} + | - - \rangle_ {2 3} | 1 \rangle_ {4}) \\ + \frac {\beta}{\sqrt {2}} (| - - \rangle_ {2 3} | 0 \rangle_ {4} + | + + \rangle_ {2 3} | 1 \rangle_ {4}). \tag {2} \\ \end{array}
$$

In the case of the other projection  $\beta |0\rangle -\alpha |1\rangle$ , the desired encoding can still be achieved as long as this state differs from  $\alpha^{*}|0\rangle +\beta^{*}|1\rangle$  only by local Pauli operations, which is, e.g., the case if the coefficients  $\alpha$  and  $\beta$  are real (see Appendix A for details). Thus, in this example, qubits with real coefficients can be deterministically encoded, whereas for complex coefficients the encoding works only probabilistically. A deterministic encoding of an unknown qubit can be achieved by coupling this additional qubit by means of a Bell measurement to our resource state.

Now, an error can occur either on qubit 2 or on qubit 3. As our protocol detects errors on one of the qubits, we assume in the following that an error occurs on qubit 3—and thus we assume that the location of the error is known. The analysis for an error on qubit 2 is similar and hence not shown here.

The second step is to read out the error syndrome. The protocol presented here enables the detection of an error coming from any (continuous) rotation around the  $Z$  axis. Here, we focus on the demonstration of an  $e^{-i(\pi /2)Z}$  error, a full phase error, or an  $e^{-i(\pi /4)Z}$  error, which demonstrates the digitalization of errors. In the latter case, the syndrome

measurement projects the coherent superposition of an error and no error onto one of these possibilities. This demonstrates a crucial ingredient of quantum error correction, which ensures that quantum error-correcting codes can cope with continuous errors, by mapping them probabilistically to a discrete set of Pauli errors. The error syndrome and the decoding are achieved in a single step by measuring qubits 2 and 3 in the basis  $X$ . For an error on qubit 3, if qubits 2 and 3 are found in state  $| + + \rangle_{23}$  or  $| + - \rangle_{23}$ , qubit 4 is in state  $|\psi \rangle$ , and hence no recovery operation is necessary; if they are measured in state  $|- + \rangle_{23}$  or  $|- - \rangle_{23}$  a recovery operation on qubit 4 needs to be applied [see in Fig. 1(d) the green-framed boxes]. In the case of  $e^{-i(\pi /4)Z}$ , these measurements determine whether an error occurs.

Finally, the remaining qubit 4 holds the decoded output. Our protocol thus succeeds if the type and the location of the single error are known. If the location of the error is unknown, only in the case where qubits 2 and 3 are measured in state  $|++\rangle_{23}$  or  $|- - \rangle_{23}$  can the encoded qubit be recovered. In that sense the scheme allows one to detect errors on either of the two intermediate qubits.

One could argue here that if we knew from the very beginning that one particular particle will be effected by noise, we could equally well decouple it before. We would like to emphasize that we are doing more: A quantum error detection—and for this both particles are required. In principle, the additional knowledge of where the error happened allows one to perform quantum error correction. However, our demonstration is a particular case ( $n = 2$ ) of a more general scheme using a cluster state where one input qubit is connected to  $n$  neighbors, which are connected to the output qubit. In this scheme already  $n = 3$  would not require the location of the error to be known a priori for the realization of a full quantum error-correction scheme. This shows how our protocol could be easily extended with only one additional qubit required [9,10].

# III. EXPERIMENT AND RESULTS

In our experiment [see Fig. 2(a)], we generate the resource state using a photonic setup with polarization-entangled photons produced by a spontaneous parametric down-conversion (SPDC) process in a railway-cross scheme [11] (see Appendix B for details about the experimental setup). We obtain the box cluster state  $|\psi_{\mathrm{box}} \rangle$  from Eq. (1) by first experimentally producing a four-qubit cluster state (see Appendix B),

$$
\begin{array}{l} | \psi_ {\mathrm {l a b}} \rangle = \frac {1}{2} [ | 0 \rangle_ {1} | 0 \rangle_ {2} | 0 \rangle_ {3} | 0 \rangle_ {4} + | 0 \rangle_ {1} | 0 \rangle_ {2} | 1 \rangle_ {3} | 1 \rangle_ {4} \\ + | 1 \rangle_ {1} | 1 \rangle_ {2} | 0 \rangle_ {3} | 0 \rangle_ {4} - | 1 \rangle_ {1} | 1 \rangle_ {2} | 1 \rangle_ {3} | 1 \rangle_ {4} ]. \tag {3} \\ \end{array}
$$

We then apply local Hadamard gates  $H$  on each qubit and a SWAP gate on qubits 2 and 4 of  $|\psi_{\mathrm{lab}}\rangle$  to obtain

$$
| \psi_ {\text {b o x}} \rangle = \left(H _ {1} \otimes H _ {2} \otimes H _ {3} \otimes H _ {4}\right) \left(\mathrm {S W A P} _ {2 4}\right) | \psi_ {\text {l a b}} \rangle . \tag {4}
$$

In our experiment, we perform the SWAP gate by interchanging the qubits physically and absorb the local Hadamard operations in the measurement basis. In the following, we present all results in the basis of the box cluster state  $|\psi_{\mathrm{box}}\rangle$

We characterize the experimentally obtained box cluster state using state tomography and reconstruct its density matrix  $\rho$ , see Fig. 2(b). For the case where no error was introduced a fidelity of our experimentally obtained state with the ideal

![](images/2d10a8f9f539f2779b232fe9e3f2e3e610d8847d89cd731789744b09b89b1268.jpg)

![](images/25f4821f42b6811f9155f2c02bcc9df8e849896c6484f14d0afa8739a867c875.jpg)  
FIG. 2. (Color online) Experimental setup and results. (a) A UV pump beam makes two passes through a  $\beta$ -barium borate (BBO) crystal, generating entangled photon pairs in the forward and backward modes. The coherent overlap of the different emissions at the polarizing beam splitters (PBSs) together with postselection of fourfold coincidences yield the four components of the cluster state. The error unitaries, half-wave plates (HwPs) or quarter-wave plates (QwPs), implement physically the  $e^{-i(\pi /2)Z}$  ( $e^{-i(\pi /4)Z}$ ) error. Finally, the state is analyzed via the state quantum tomography using HwPs, QwPs, and PBSs. (b) The reconstructed density matrix (real part) of the four-qubit box cluster state in the eigenbasis of  $Z \otimes X \otimes X \otimes Z$ . The wire frame shows the ideal density matrix; the components of the imaginary part are below 0.037 and are hence not presented here.

box cluster state  $|\psi_{\mathrm{box}} \rangle$  of  $F = 0.656 \pm 0.006$  was obtained after local unitary transformations. The density matrices for the states after the implementation of errors have similar fidelities and are shown in Appendix C. To demonstrate the implementation of the protocol we choose a set of input states  $|\psi \rangle$  as shown in Fig. 3 to be encoded in the box cluster state and subsequently decoded, recovering the initial state.

We implement the errors on qubit 3 using additional half-wave and quarter-wave plates. In detail, we use a HWP (QWP) at  $45^{\circ}(-45^{\circ})$  for the implementation of the  $e^{-i(\pi /2)Z}$ $(e^{-i(\pi /4)Z})$  error (see Appendix B). We proceed with the error syndrome readout and, finally, the state of the decoded qubit is reconstructed through single-qubit tomography of qubit 4. In the case where an error is detected, the original qubit is recovered through implementation of a postprocessing recovery operation: either  $I$  or  $X$ .

![](images/298a2d806192c266e1d33994ac3f9a21e202ebb0f404d9ac6bd9d5e59d228403.jpg)

![](images/34601c76f8599f879a0414aa78a2e706e6d25afdc34cd367dde15dde96b0ab82.jpg)

![](images/b0f1e3d519a2588b6040b22adcd7beb469325f7de5637b525d8772429878ff8b.jpg)  
FIG. 3. (Color online) Representation of a set of encoded input states. (a) A Bloch sphere where different planes are marked with color codes. The green circle marks the  $X - Z$  plane, the red circle marks the  $X - Y$  plane, and the blue circle marks the  $Y - Z$  plane. (b)-(d) The encoded input states are shown in the correspondent plane of the Bloch sphere. For a complete definition of the chosen states, see Table III in Appendix D.

![](images/34926223827d4aa8f84a4b52c440abb8bb49a027a8c2154de3e74f6673d5fd9b.jpg)

The fidelities of experimentally obtained (and then decoded) qubits with respect to the ideal decoded qubits vary with the encoded state. For the cases where no recovery operation was needed the fidelities lie within the values  $[0.810 \pm 0.036, 0.990 \pm 0.009]$ . Decoded qubits in which a  $X$  recovery operation was applied present slightly lower fidelities  $[0.629 \pm 0.039, 0.982 \pm 0.008]$ . This discrepancy follows from nonideal resource states as shown in Fig. 2(b). Due to experimental noise, the single-qubit fidelities of qubit 4 vary for different projections of qubit 2 and qubit 3.

To illustrate some of the experimental results, in Fig. 4 we show the results obtained for the case where the state  $|N\rangle = (|+i\rangle + e^{-i(\pi/4)}| - i\rangle) / \sqrt{2}$  (here,  $|\pm_i\rangle = (|0\rangle \pm i|1\rangle) / \sqrt{2}$ ) was encoded (Fig. 4), subjected to a full phase error on qubit 3 and subsequently decoded.

A list of the fidelities of all operations performed is shown in Appendix D where we also present the results for errors occurring on qubit 2.

# IV. CONCLUSION

We have presented the implementation of an error-detection protocol in measurement-based quantum computing. Although the demonstration was performed using a photonic quantum computing architecture, measurement-based error detection and correction can be implemented with other physical systems as demonstrated recently with trapped ions [28].

Our protocol can be readily extended to larger cluster states containing more qubits. A five-qubit cluster state would

![](images/0bffc64bc31456d6df3b3d41417439da82a154a34847c81629f797abb059d77d.jpg)  
FIG. 4. (Color online) Experimental results. We encode a state into qubits 2 and 3 and then let a phase error act on qubit 3. (a) Representation of the ideal state  $|N\rangle = (|+_{i}\rangle + e^{-i(\pi /4)}| - _{i}\rangle) / \sqrt{2}$  to be encoded  $(|\pm_i\rangle = (|0\rangle \pm i|1\rangle) / \sqrt{2})$ . (b) State of qubit 4 after decoding when qubits 2 and 3 are measured in state  $|+-\rangle_{23}$ . In the case where no recovery operation is required [(b)] the fidelity of the experimentally obtained state after decoding with the ideal state is  $F = 0.940 \pm 0.024$ . (c) State of qubit 4 after decoding when qubits 2 and 3 are measured in state  $|- + \rangle_{23}$  before a recovery operation was applied. (d) Qubit 4 after applying the recovery operation  $X$  in (c) through postprocessing  $(F = 0.875 \pm 0.029)$ . (e) Overview of the encoded and decoded qubits of (a)-(d).

be sufficient to also correct the error within the experiment such that no postprocessing would be necessary. A structure containing seven qubits or more would allow for the detection and correction of multiple phase errors or a general error on a single qubit.

Our experiment constitutes a building block for larger-scale hybrid quantum computing networks where elements of different computational schemes are combined to provide a computational architecture that unifies the advantage of the different approaches [10]. In such a hybrid architecture, elementary blocks and gate sequences can be performed in a measurement-based way, i.e., by preparing specific resource states, and then combined in a sequential fashion as in the circuit model. This approach leads to a remarkable robustness against noise and imperfections with error thresholds on the order of  $10\%$  per particle. Our paper presents a proof-of-principle demonstration of one of the main building blocks in this scheme, thereby providing another step towards measurement-based quantum information processing in realistic scenarios.

# ACKNOWLEDGMENTS

This work was supported by the European Commission, Q-ESSENCE (Grant No. 248095), QUILMI (Grant No.295293), EQUAM (Grant No. 323714), PICQUE (Grant No. 608062), GRASP (Grant No. 613024), the ERA-Net CHISTERA project QUASAR, the John Templeton Foundation, the Vienna Center for Quantum Science and Technology (VCQ), the Austrian Nanoinitiative NAP Platon, the Austrian Science Fund (FWF) through the SFB FoQuS (Grants No. F4006-N16 and No. F4012-N16), START (Grant No. Y585-N20), grant (Grant No. P24273-N16) and the doctoral programme CoQuS, the Vienna Science and Technology Fund (WWTF) under Grant No. ICT12-041, and the Air Force Office of Scientific

Research, Air Force Material Command, United States Air Force, under Grant No. FA8655-11-1-3004.

# APPENDIX A: THEORY

# 1. Deterministic and probabilistic encoding

As described in detail in the main paper, we encode the input state by measuring qubit 1 in the basis  $\{\alpha^{*}|0\rangle +\beta^{*}|1\rangle ,\beta |0\rangle -$ $\alpha |1\rangle \}$  . If qubit 1 is projected onto state  $\alpha^{*}|0\rangle +\beta^{*}|1\rangle$  , the remaining three-qubit state is as follows:

$$
\begin{array}{l} | \psi_ {3} \rangle = \frac {\alpha}{\sqrt {2}} (| + + \rangle_ {2 3} | 0 \rangle_ {4} + | - - \rangle_ {2 3} | 1 \rangle_ {4}) \\ + \frac {\beta}{\sqrt {2}} (| - - \rangle_ {2 3} | 0 \rangle_ {4} + | + + \rangle_ {2 3} | 1 \rangle_ {4}), \tag {A1} \\ \end{array}
$$

and if qubit 1 is projected onto state  $\beta |0\rangle -\alpha |1\rangle$  , it is as follows:

$$
\begin{array}{l} | \psi_ {3} \rangle = \frac {\beta^ {*}}{\sqrt {2}} (| + + \rangle_ {2 3} | 0 \rangle_ {4} + | - - \rangle_ {2 3} | 1 \rangle_ {4}) \\ - \frac {\alpha^ {*}}{\sqrt {2}} (| - - \rangle_ {2 3} | 0 \rangle_ {4} + | + + \rangle_ {2 3} | 1 \rangle_ {4}). \tag {A2} \\ \end{array}
$$

In the latter case, a correction is possible whenever  $\beta |0\rangle -\alpha |1\rangle$  differs from  $\alpha^{*}|0\rangle +\beta^{*}|1\rangle$  only by local Pauli operations. This is the case for real coefficients  $\alpha ,\beta$  where the desired state can be obtained by applying local Pauli corrections  $[(XZ)_2\otimes Z_3]$  but, e.g., also for a  $\sigma_{y}$  eigenstate  $\alpha = 1 / \sqrt{2}$ ,  $\beta = \pm i / \sqrt{2}$ . In all other cases, the encoding procedure is probabilistic. Notice that the process can be made deterministic by using an additional qubit  $1^{\prime}$ , whose (unknown) state can be read-in deterministically (up to Pauli correction) by performing a Bell measurement on qubits 1 and  $1^{\prime}$ .

TABLE I. Recovery operations for the  $\left( {{e}^{-i\left( {\pi /2}\right) Z}}\right)$  phase error.  

<table><tr><td>Error type</td><td colspan="2">No error</td><td colspan="2">Z2error</td><td colspan="2">Z3error</td></tr><tr><td>Syndrome measurement</td><td>|++)23</td><td>|--)23</td><td>|+-)23</td><td>|+-)23</td><td>|+-)23</td><td>|--)23</td></tr><tr><td>Recovery operation</td><td>I</td><td>X</td><td>I</td><td>X</td><td>I</td><td>X</td></tr></table>

# 2. Syndrome readout and decoding

If an  $e^{-i(\pi /2)Z}$  error occurs on qubit 2, the three-qubit state related to (A1) becomes

$$
\begin{array}{l} | \psi_ {3} ^ {\prime} \rangle = \frac {\alpha}{\sqrt {2}} (| - + \rangle_ {2 3} | 0 \rangle_ {4} + | + - \rangle_ {2 3} | 1 \rangle_ {4}) \\ + \frac {\beta}{\sqrt {2}} (| + - \rangle_ {2 3} | 0 \rangle_ {4} + | - + \rangle_ {2 3} | 1 \rangle_ {4}). \tag {A3} \\ \end{array}
$$

If qubits 2 and 3 are measured to be in state  $|- + \rangle_{23}$ , the final state of qubit 4 is  $|\psi \rangle = \alpha |0\rangle + \beta |1\rangle$ ; whereas if they are measured to be in state  $|+ - \rangle_{23}$ , the state of qubit 4 will be  $\alpha |1\rangle + \beta |0\rangle$ , which can be corrected by applying a recovery operation  $X$ .

If an  $e^{-i(\pi /2)Z}$  error occurs on qubit 3, the three-qubit state related to (A1) becomes

$$
\begin{array}{l} | \psi_ {3} ^ {\prime} \rangle = \frac {\alpha}{\sqrt {2}} (| + - \rangle_ {2 3} | 0 \rangle_ {4} + | - + \rangle_ {2 3} | 1 \rangle_ {4}) \\ + \frac {\beta}{\sqrt {2}} (| - + \rangle_ {2 3} | 0 \rangle_ {4} + | + - \rangle_ {2 3} | 1 \rangle_ {4}). \tag {A4} \\ \end{array}
$$

In this case, if qubits 2 and 3 are projected onto state  $|+ - \rangle_{23}$ , the final state of qubit 4 will be  $|\psi \rangle$ , whereas for  $|- + \rangle_{23}$  we obtain  $|\psi \rangle$  only after applying a recovery operation  $X$ .

If an  $e^{-i(\pi /4)Z}$  error occurs on qubit 2, the three-qubit state related to (A1) becomes

$$
\begin{array}{l} | \psi_ {3} ^ {\prime} \rangle = \frac {\alpha}{2} (| + + \rangle_ {2 3} | 0 \rangle_ {4} - i | - + \rangle_ {2 3} | 0 \rangle_ {4} \\ + \left| - - \right\rangle_ {2 3} \left| 1 \right\rangle_ {4} - i \left| + - \right\rangle_ {2 3} \left| 1 \right\rangle_ {4}) \\ + \frac {\beta}{2} (| - - \rangle_ {2 3} | 0 \rangle_ {4} - i | + - \rangle_ {2 3} | 0 \rangle_ {4} \\ + \left| + + \right\rangle_ {2 3} \left| 1 \right\rangle_ {4} - i \left| - + \right\rangle_ {2 3} \left| 1 \right\rangle_ {4}). \tag {A5} \\ \end{array}
$$

The remaining state is a coherent superposition of the error case and no error case. If qubits 2 and 3 are projected onto state  $|++\rangle_{23}$  or  $|- - \rangle_{23}$ , then the encoded qubit has not been affected by noise, whereas for  $| + - \rangle_{23}$  or  $|- + \rangle_{23}$  a phase flip acted. In both cases the final state of qubit 4 will be equal to  $|\psi \rangle$  up to  $\mathbb{I}$  or  $X$  operations, respectively.

The same procedure is used to obtain the final state of qubit 4 after an  $e^{-i(\pi /4)Z}$  error occurred on qubit 3.

We summarize in Tables I and II the syndrome outcomes and respective recovery operations for an  $e^{-i(\pi /2)Z}$  error (see Table I) and an  $e^{-i(\pi /4)Z}$  error (see Table II).

# APPENDIX B: EXPERIMENTAL SETUP

In our experiment [see Fig. 2(a) in the main paper] entangled photon pairs are produced by a noncollinear type-II SPDC process on a BBO crystal.

A solid-state 532-nm laser (Coherent Verdi-10) pumps a mode-locked Ti:sapphire oscillator (Coherent Mira 900), yielding a pulsed output ( $\tau = 200$  fs,  $\lambda = 789$  nm,  $76\mathrm{MHz}$ ). This is afterwards frequency doubled through second-harmonic generation in a 2-mm-thick lithium triborate (LBO) crystal, producing UV pulses with a  $0.7\mathrm{W}$  cw average. We achieve a stable source of UV pulses by translating the LBO to avoid optical damage to the antireflection coating of the crystal. Dichroic mirrors are used to separate the up-converted UV from the residual infrared light.

The UV pump beam is focused on the 2-mm-thick BBO, generating down-converted infrared photons in the forward modes  $a$  and  $b$ . Then, the UV beam is reflected back, crossing the BBO a second time and producing entangled photon pairs in the backward modes  $c$  and  $d$ . HwPs and additional BBOs are used to compensate for walk-off effects and allow the production of any Bell state in the forward and backward modes.

The modes of the different pairs  $a, b$  and  $d, c$ , respectively, are then coherently overlapped at PBSs by equalizing the different path lengths.

Narrow-band interference filters  $(\Delta \lambda = 3\mathrm{nm})$  are used to spatially and spectrally select the down-converted photons, which are then coupled into single-mode fibers that guide them to the polarization analysis setup. There, different polarization measurements are performed using QWPs, HWPs, and polarizing beam splitters as well as single-photon detectors (PerkinElmer—SPCM AQ4C).

The preparation of the four-qubit linear cluster state relies on the simultaneous detection of one (and only one) photon in each of the four outputs 1, 2, 3, and 4.

In order to produce the desired state, we align our setup such that a  $|\Phi^{-}\rangle_{ab} = (|HH\rangle_{ab} - |VV\rangle_{ab}) / \sqrt{2}$  state is emitted in the forward direction and a  $|\Phi^{+}\rangle_{cd} = (|HH\rangle_{cd} + |VV\rangle_{cd}) / \sqrt{2}$  state is emitted in the backward direction, where

TABLE II. Recovery operations for the  $\left( {{e}^{-i\left( {\pi /4}\right) Z}}\right)$  error.  

<table><tr><td rowspan="2">Error type</td><td colspan="4">e-ix(π/4)Z2error</td><td colspan="4">e-ix(π/4)Z3error</td></tr><tr><td colspan="2">No error</td><td colspan="2">Z2error</td><td colspan="2">No error</td><td colspan="2">Z3error</td></tr><tr><td>Syndrome measurement</td><td>|++⟩23</td><td>|--⟩23</td><td>|++⟩23</td><td>|++⟩23</td><td>|++⟩23</td><td>|--⟩23</td><td>|++⟩23</td><td>|--⟩23</td></tr><tr><td>Recovery operation</td><td>I</td><td>X</td><td>I</td><td>X</td><td>I</td><td>X</td><td>I</td><td>X</td></tr></table>

![](images/ce01d7843b823a76d080e826e42e06c3754df6163b63fc189cf1113b2dc401a0.jpg)  
FIG. 5. (Color online) Density matrix (real part) of the four-qubit box cluster state after a full-phase error occurred on qubit 3 ( $F = 0.656 \pm 0.006$  via local unitary operations). The components of the imaginary part are below 0.032 and are hence not presented here.

$|H\rangle (|V\rangle)$  denotes the horizontal (vertical) polarization state. The emission of only one entangled pair in the forward direction and only one pair in the backward direction results in two different four-photon terms:  $|H\rangle_{1}|H\rangle_{2}|H\rangle_{3}|H\rangle_{4}$  and  $-|V\rangle_{1}|V\rangle_{2}|V\rangle_{3}|V\rangle_{4}$  due to the properties of the PBSs. The two-pair emissions also lead to fourfold coincidences, namely, to a  $-|H\rangle_{1}|H\rangle_{2}|V\rangle_{3}|V\rangle_{4}$  state and a  $|V\rangle_{1}|V\rangle_{2}|H\rangle_{3}|H\rangle_{4}$  state for a double-pair emission in the forward and in the backward directions, respectively. We shift the phase of the term  $-|H\rangle_{1}|H\rangle_{2}|V\rangle_{3}|V\rangle_{4}$  by  $\pi$  to generate a sign shift. For this, we use the method described in Ref. [11] where a rotation of an additional wave plate has the desired effect. The final output state is a superposition of all these four terms. Experimentally,

![](images/74c9d78058b7ff5ed8e69c463ebfa57f8acea6248286c463b80bd5e74804edeb.jpg)  
FIG. 6. (Color online) Density matrix (real part) of the four-qubit box cluster state after a full-phase error occurred on qubit 2 ( $F = 0.646 \pm 0.008$  via local unitary operations rotations). The components of the imaginary part are below 0.027 and are hence not presented here.

![](images/fce0f2ccdf6ae83c3dd86316f9c9e783be77494bbd600fd6f8954602ee3a93d9.jpg)  
FIG. 7. (Color online) Density matrix (real part) of the four-qubit box cluster state after a half-phase  $(e^{-i(\pi /4)Z})$  error occurred on qubit  $3(F = 0.667\pm 0.009$  via local unitary operations).

we measure a count rate of 0.25 fourfold coincidences per second.

Theoretical considerations show that for a ratio of 1:3 between the backward  $(4.4\mathrm{ks}^{-1})$  and the forward  $(13.2\mathrm{ks}^{-1})$  twofold coincidences, the right amplitudes are attained by setting the HwP to  $27.5^{\circ}$  [11]. The ratio is adjusted by tweaking the coupling efficiencies of the forward and backward modes.

Additional phase shifts arising due to reflections at the PBS are compensated by tilting the BBO crystals in the forward direction (and effectively aligning for state  $|\Phi^{+}\rangle$ ).

In our experiment, the emitted Bell pairs show typical visibilities of about 0.9. The different photon emissions then interfere at the PBSs with average visibilities of 0.85. Additional errors arise due to phase drifts during the measurements. These main error contributions, together with minor errors, such as polarization drifts, decrease the fidelity of our cluster states with respect to the ideal state. In our calculations, we

![](images/3e13d7b194631d916a47d84c772482128f2be9f1c23d7706110a7ed37ce10b68.jpg)  
FIG. 8. (Color online) Density matrix (imaginary part) of the four-qubit box cluster state after a half-phase  $(e^{-i(\pi /4)Z})$  error occurred on qubit 3 (same fidelity as the real part, Fig. 7).

![](images/73349a802651e70243c584cf853271e398d7cc93c4b2f04ee2f408cda85337c7.jpg)  
FIG. 9. (Color online) Density matrix (real part) of the four-qubit box cluster state after a half-phase  $(e^{-i(\pi /4)Z})$  error occurred on qubit  $2(F = 0.641\pm 0.009$  via local unitary operations).

always assume Poissonian errors. In fact, these indicate a lower bound for the actual error that takes all the experimental imperfections into account.

The implementation of the errors is accomplished by inserting additional QWPs and HWPs in the respective modes. Note that due to the swap operation, noise affecting qubit 2 of the box cluster is experimentally implemented on qubit 4 of our experimental cluster state. Likewise, because of the H gate (implemented in the postprocessing), the phase flip  $e^{-i(\pi /2)Z}$  is implemented via a bit flip  $(X)$  in the experiment.

The error was estimated running a 100-cycle Monte Carlo simulation with Poissonian noise added to the experimental counts.

The data-acquisition time was  $600~\mathrm{s}$  per measurement setting for the state tomographies (Appendix C) of the box cluster state and  $1800~\mathrm{s}$  for each of the measurements where a full phase error was implemented. For the cases where a half-phase error was implemented, the acquisition time per

![](images/bcfee8be750c86614830fee9a29ae3c0b3fb82f3eecd4b77c1aea5cdd91d80ad.jpg)  
FIG. 10. (Color online) Density matrix (imaginary part) of the four-qubit box cluster state after a half-phase  $(e^{-i(\pi /4)Z})$  error occurred on qubit 2 (same fidelity as the real part, Fig. 9).

setting was  $3600\mathrm{~s~}$  (see Appendix D) with the exception of the first column of Table VI (1800 s per setting).

# APPENDIX C: FOUR-QUBIT DENSITY MATRICES

We present the full-tomographic reconstructions of the box cluster resource state after the occurrence of an  $e^{-i(\pi /2)Z}$  error on qubit 2, an  $e^{-i(\pi /2)Z}$  error on qubit 3, an  $e^{-i(\pi /4)Z}$  error on qubit 2, and an  $e^{-i(\pi /4)Z}$  error on qubit 3. The density matrices are presented in the eigenbasis of  $Z\otimes X\otimes X\otimes Z$  to easily visualize the state (see Figs. 5-10). The wire frames represent the ideal state after the error occurred.

# APPENDIX D: DECODING RESULTS

In Tables IV-VII we report fidelities of the experimentally obtained and then decoded qubits (see Table III for encoded states) with the ideal state for each type of implemented error  $(e^{-i(\pi /2)Z}$  error on qubit 2,  $e^{-i(\pi /2)Z}$  error on qubit 3,  $e^{-i(\pi /4)Z}$

TABLE III. Initial states of qubit 1 reported in different notations: The measured state laboratory shows the projection state  $\alpha^{*}|0\rangle +\beta^{*}|1\rangle$  of qubit 1 of  $|\psi_{\mathrm{lab}}\rangle$  (see the main paper) and the relative basis; the measured state box shows the projection state  $\alpha^{*}|0\rangle +\beta^{*}|1\rangle$  of qubit 1 of  $|\psi_{\mathrm{box}}\rangle$  and the relative basis; and the encoded state box notation shows the encoded qubit 1 in the box cluster notation. In this case we report per input state the explicit qubit, the relative basis, and the spherical coordinates.  

<table><tr><td colspan="2">Measured state laboratory</td><td colspan="2">Measured state box</td><td colspan="4">Encoded state box</td><td></td></tr><tr><td>Qubit</td><td>Basis</td><td>Qubit</td><td>Basis</td><td>Qubit</td><td>Basis</td><td>θ</td><td>φ</td><td></td></tr><tr><td>|+)</td><td>σx</td><td>|0)</td><td>σz</td><td>|0)</td><td>σz</td><td>0°</td><td>0°</td><td></td></tr><tr><td>|0)</td><td>σz</td><td>|+)</td><td>σx</td><td>|+)</td><td>σx</td><td>90°</td><td>0°</td><td></td></tr><tr><td>|-i)</td><td>-σy</td><td>|+i)</td><td>σy</td><td>|-i)</td><td>-σy</td><td>90°</td><td>-90°</td><td></td></tr><tr><td>|P)</td><td>σx + σy</td><td>|U)</td><td>σz - σy</td><td>|T)</td><td>1/√2( |+⟩ + e- iπ/4 |-⟩)</td><td>σz + σy</td><td>45°</td><td>90°</td></tr><tr><td>|M)</td><td>σx - σy</td><td>|T)</td><td>σz + σy</td><td>|U)</td><td>1/√2( |+⟩ + e iπ/4 |-⟩)</td><td>σz - σy</td><td>45°</td><td>-90°</td></tr><tr><td>|Q)</td><td>σx + σz</td><td>|Q)</td><td>σz + σx</td><td>|Q)</td><td>1/√2( |+⟩ + e iπ/4 |-⟩)</td><td>σz + σx</td><td>45°</td><td>0°</td></tr><tr><td>|S)</td><td>σx - σz</td><td>|N)</td><td>σz - σx</td><td>|N)</td><td>1/√2( |+⟩ + e- iπ/4 |-⟩)</td><td>σz - σx</td><td>45°</td><td>180°</td></tr><tr><td>|T)</td><td>σz + σy</td><td>|M)</td><td>σx - σy</td><td>|P)</td><td>1/√2( |0⟩ + e+ iπ/4 |1⟩)</td><td>σx + σy</td><td>90°</td><td>45°</td></tr><tr><td>|U)</td><td>σz - σy</td><td>|P)</td><td>σx + σy</td><td>|M)</td><td>1/√2( |0⟩ + e- iπ/4 |1⟩)</td><td>σx - σy</td><td>90°</td><td>-45°</td></tr></table>

TABLE IV. Fidelities of different encoded and decoded states after an  $e^{-i(\pi /2)Z}$  error was implemented but no recovery operation was necessary.  

<table><tr><td>Encoded state</td><td>No error</td><td>Error Z3</td><td>Error Z2</td><td>Error Z2Z3</td></tr><tr><td>|0)</td><td>F=0.967±0.011</td><td>F=0.874±0.022</td><td>F=0.904±0.021</td><td>F=0.886±0.022</td></tr><tr><td>|+)</td><td>F=0.944±0.017</td><td>F=0.945±0.016</td><td>F=0.943±0.015</td><td>F=0.969±0.009</td></tr><tr><td>|-i)</td><td>F=0.956±0.012</td><td>F=0.925±0.019</td><td>F=0.912±0.019</td><td>F=0.905±0.019</td></tr><tr><td>|T)</td><td>F=0.820±0.030</td><td>F=0.965±0.021</td><td>F=0.971±0.014</td><td>F=0.907±0.028</td></tr><tr><td>|U)</td><td>F=0.863±0.025</td><td>F=0.957±0.013</td><td>F=0.927±0.025</td><td>F=0.885±0.028</td></tr><tr><td>|Q)</td><td>F=0.938±0.026</td><td>F=0.898±0.033</td><td>F=0.915±0.026</td><td>F=0.976±0.009</td></tr><tr><td>|N)</td><td>F=0.967±0.020</td><td>F=0.940±0.024</td><td>F=0.915±0.026</td><td>F=0.922±0.024</td></tr><tr><td>|P)</td><td>F=0.895±0.033</td><td>F=0.902±0.026</td><td>F=0.810±0.036</td><td>F=0.910±0.028</td></tr><tr><td>|M)</td><td>F=0.918±0.026</td><td>F=0.965±0.016</td><td>F=0.947±0.023</td><td>F=0.970±0.018</td></tr></table>

TABLE V. Fidelities of different encoded and decoded states after an  $e^{-i(\pi /2)Z}$  error was implemented and a recovery operation was performed.  

<table><tr><td>Encoded state</td><td>No error</td><td>Error Z3</td><td>Error Z2</td><td>Error Z2Z3</td></tr><tr><td>|0)</td><td>F=0.767±0.032</td><td>F=0.716±0.035</td><td>F=0.793±0.030</td><td>F=0.784±0.028</td></tr><tr><td>|+)</td><td>F=0.948±0.016</td><td>F=0.945±0.018</td><td>F=0.944±0.014</td><td>F=0.943±0.015</td></tr><tr><td>|-i)</td><td>F=0.684±0.036</td><td>F=0.674±0.038</td><td>F=0.710±0.036</td><td>F=0.658±0.034</td></tr><tr><td>|T)</td><td>F=0.686±0.033</td><td>F=0.809±0.031</td><td>F=0.792±0.032</td><td>F=0.700±0.028</td></tr><tr><td>|U)</td><td>F=0.681±0.037</td><td>F=0.771±0.032</td><td>F=0.662±0.034</td><td>F=0.740±0.038</td></tr><tr><td>|Q)</td><td>F=0.741±0.044</td><td>F=0.776±0.034</td><td>F=0.833±0.031</td><td>F=0.813±0.029</td></tr><tr><td>|N)</td><td>F=0.793±0.047</td><td>F=0.875±0.029</td><td>F=0.843±0.029</td><td>F=0.962±0.027</td></tr><tr><td>|P)</td><td>F=0.750±0.029</td><td>F=0.811±0.031</td><td>F=0.790±0.028</td><td>F=0.862±0.024</td></tr><tr><td>|M)</td><td>F=0.800±0.035</td><td>F=0.801±0.038</td><td>F=0.823±0.029</td><td>F=0.895±0.030</td></tr></table>

TABLE VI. Fidelities of different encoded and decoded states after an  $e^{-i(\pi /4)Z}$  error was implemented but no recovery operation was performed.  

<table><tr><td rowspan="2">Encoded state</td><td colspan="2">e-ix(π/4)Z3error</td><td colspan="2">e-ix(π/4)Z2error</td></tr><tr><td>No error</td><td>Error Z3</td><td>No error</td><td>Error Z2</td></tr><tr><td>|0)</td><td>F=0.896±0.027</td><td>F=0.865±0.035</td><td>F=0.909±0.021</td><td>F=0.927±0.015</td></tr><tr><td>|+)</td><td>F=0.861±0.034</td><td>F=0.913±0.022</td><td>F=0.936±0.021</td><td>F=0.986±0.007</td></tr><tr><td>|-i)</td><td>F=0.908±0.024</td><td>F=0.865±0.025</td><td>F=0.945±0.017</td><td>F=0.914±0.022</td></tr><tr><td>|T)</td><td>F=0.850±0.042</td><td>F=0.880±0.040</td><td>F=0.823±0.036</td><td>F=0.842±0.030</td></tr><tr><td>|U)</td><td>F=0.951±0.034</td><td>F=0.951±0.013</td><td>F=0.930±0.028</td><td>F=0.903±0.028</td></tr><tr><td>|Q)</td><td>F=0.849±0.037</td><td>F=0.854±0.035</td><td>F=0.905±0.031</td><td>F=0.937±0.028</td></tr><tr><td>|N)</td><td>F=0.963±0.023</td><td>F=0.942±0.024</td><td>F=0.894±0.027</td><td>F=0.923±0.025</td></tr><tr><td>|P)</td><td>F=0.871±0.030</td><td>F=0.964±0.021</td><td>F=0.972±0.011</td><td>F=0.972±0.015</td></tr><tr><td>|M)</td><td>F=0.956±0.022</td><td>F=0.984±0.016</td><td>F=0.990±0.009</td><td>F=0.929±0.025</td></tr></table>

TABLE VII. Fidelities of different encoded and decoded states after an  $e^{-i(\pi /4)Z}$  error was implemented and a recovery operation was performed.  

<table><tr><td rowspan="2">Encoded state</td><td colspan="2">e-ix(π/4)Z3error</td><td colspan="2">e-ix(π/4)Z2error</td></tr><tr><td>No error</td><td>Error Z3</td><td>No error</td><td>Error Z2</td></tr><tr><td>|0)</td><td>F = 0.702 ± 0.038</td><td>F = 0.843 ± 0.280</td><td>F = 0.690 ± 0.036</td><td>F = 0.721 ± 0.029</td></tr><tr><td>|+)</td><td>F = 0.948 ± 0.015</td><td>F = 0.981 ± 0.008</td><td>F = 0.896 ± 0.024</td><td>F = 0.837 ± 0.023</td></tr><tr><td>|-i)</td><td>F = 0.629 ± 0.039</td><td>F = 0.814 ± 0.035</td><td>F = 0.697 ± 0.040</td><td>F = 0.644 ± 0.030</td></tr><tr><td>|T)</td><td>F = 0.658 ± 0.033</td><td>F = 0.691 ± 0.038</td><td>F = 0.699 ± 0.037</td><td>F = 0.656 ± 0.033</td></tr><tr><td>|U)</td><td>F = 0.677 ± 0.032</td><td>F = 0.814 ± 0.037</td><td>F = 0.813 ± 0.039</td><td>F = 0.776 ± 0.034</td></tr><tr><td>|Q)</td><td>F = 0.832 ± 0.032</td><td>F = 0.818 ± 0.031</td><td>F = 0.842 ± 0.0345</td><td>F = 0.734 ± 0.033</td></tr><tr><td>|N)</td><td>F = 0.932 ± 0.028</td><td>F = 0.857 ± 0.038</td><td>F = 0.794 ± 0.041</td><td>F = 0.894 ± 0.031</td></tr><tr><td>|P)</td><td>F = 0.749 ± 0.029</td><td>F = 0.919 ± 0.028</td><td>F = 0.799 ± 0.031</td><td>F = 0.706 ± 0.031</td></tr><tr><td>|M)</td><td>F = 0.775 ± 0.034</td><td>F = 0.941 ± 0.025</td><td>F = 0.906 ± 0.028</td><td>F = 0.823 ± 0.032</td></tr></table>

![](images/84295f3c5524149b0ccacac2a7ec9ce637fcbd95b74b72b0af3c2bcccbb26935.jpg)  
FIG. 11. (Color online) Experimental decoding results in Bloch sphere representation for an  $e^{-i(\pi /4)Z}$  error on qubit 3. (a) Encoded or ideal state  $|M\rangle$ , an eigenstate of the operator  $(X - Y)$ . (b) Decoded qubit reading the outcomes  $|- + \rangle$  of qubits 2 and 3,  $F = 0.984 \pm 0.016$ . (c) and (d) Decoded qubit reading the outcomes  $|+ - \rangle$  before and after applying the recovery operation  $X$ ,  $F = 0.941 \pm 0.025$ . (e) Overview of the encoded and decoded qubits.

error on qubit 2, and  $e^{-i(\pi /4)Z}$  error qubit 3) and considering different syndrome outcomes (associated with applying or not the recovery operation  $X$ ). Specifically we report two tables for the  $e^{-i(\pi /2)Z}$  error type, the first related to the outcomes with no need of a recovery operation, and the second related to the results after the recovery operation  $X$ . The same for the  $e^{-i(\pi /4)Z}$  error type.

The last column of each table shows fidelities for decoded qubits in the presence of two errors on both qubits 2 and 3. When this case happens we have to discard the obtained results since the relative syndrome outcomes can be confused with the ones respective to the one-qubit error case. However, in order to fully characterize our experiment, we reconstruct the decoded qubit (knowing a priori the two errors occurred on qubits 2 and 3).

The experimentally obtained fidelities for the cases where an error occurs are sometimes found to be higher than the no-error cases. This effect occurs due to experimental imperfections (phase shifts, polarization rotations, and nonideal overlap of the photons at the beam splitters), which lead to nonideal four-photon state fidelities. These experimental imperfections do not act on all states in the same way, thus our experimental noise is not white noise but depends on the states. Thus, it can easily happen that for some settings, the fidelity of the output state is higher when errors (which basically are phase shifts) on two qubits were applied.

Furthermore, we show in the Bloch sphere representation the decoded qubit  $|M\rangle$  after an  $e^{-i(\pi /4)Z}$  error acted on qubit 3 (see Fig. 11).

[1] R. Raussendorf and H. J. Briegel, Phys. Rev. Lett. 86, 5188 (2001).  
[2] J. Zhang and S. L. Braunstein, Phys. Rev. A 73, 032318 (2006).  
[3] N. C. Menicucci, P. van Loock, M. Gu, C. Weedbrook, T. C. Ralph, and M. A. Nielsen, Phys. Rev. Lett. 97, 110501 (2006).  
[4] H. J. Briegel, D. E. Browne, W. Dür, R. Raussendorf, and M. Van den Nest, Nat. Phys. 5, 19 (2009).  
[5] H. J. Briegel and R. Raussendorf, Phys. Rev. Lett. 86, 910 (2001).  
[6] R. Raussendorf, D. E. Browne, and H. J. Briegel, Phys. Rev. A 68, 022312 (2003).  
[7] M. Zwerger, W. Dür, and H. J. Briegel, Phys. Rev. A 85, 062326 (2012).  
[8] D. Gottesman, Ph.D. thesis, California Institute of Technology, 1997.  
[9] M. Zwerger, H. J. Briegel, and W. Dür, Phys. Rev. Lett. 110, 260503 (2013).  
[10] M. Zwerger, H. J. Briegel, and W. Dür, Sci. Rep. 4, 5364 (2014).

[11] P. Walther, K. Resch, T. Rudolph, E. Schenck, H. Weinfurter, V. Vedral, M. Aspelmeyer, and A. Zeilinger, Nature (London) 434, 169 (2005).  
[12] K. Chen, C.-M. Li, Q. Zhang, Y.-A. Chen, A. Goebel, S. Chen, A. Mair, and J.-W. Pan, Phys. Rev. Lett. 99, 120503 (2007).  
[13] C. Lu, X. Zhou, O. Gühne, W. Gao, J. Zhang, Z. Yuan, A. Goebel, T. Yang, and J. Pan, Nat. Phys. 3, 91 (2007).  
[14] Y. Tokunaga, S. Kuwashiro, T. Yamamoto, M. Koashi, and N. Imoto, Phys. Rev. Lett. 100, 210501 (2008).  
[15] G. Vallone, E. Pomerico, F. De Martini, and P. Mataloni, Phys. Rev. A 78, 042335 (2008).  
[16] G. Vallone, G. Donati, N. Bruno, A. Chiuri, and P. Mataloni, Phys. Rev. A 81, 050302(R) (2010).  
[17] R. Ukai, N. Iwata, Y. Shimokawa, S. C. Armstrong, A. Politi, J.-i. Yoshikawa, P. van Loock, and A. Furusawa, Phys. Rev. Lett. 106, 240504 (2011).  
[18] R. Ukai, S. Yokoyama, J.-i. Yoshikawa, P. van Loock, and A. Furusawa, Phys. Rev. Lett. 107, 250501 (2011).

[19] X.-C. Yao, T.-X. Wang, P. Xu, H. Lu, G.-S. Pan, X.-H. Bao, C.-Z. Peng, C.-Y. Lu, Y.-A. Chen, and J.-W. Pan, Nat. Photonics 6, 225 (2012).  
[20] X. Su, Y. Zhao, S. Hao, X. Jia, C. Xie, and K. Peng, Opt. Lett. 37, 5178 (2012).  
[21] S. Yokoyama, R. Ukai, S. C. Armstrong, C. Sornphiphatphong, T. Kaji, S. Suzuki, J.-i. Yoshikawa, H. Yonezawa, N. C. Menicucci, and A. Furusawa, Nat. Photonics 7, 982 (2013).  
[22] R. Prevedel, P. Walther, F. Tiefenbacher, P. Böhi, R. Kaltenbaek, T. Jennewein, and A. Zeilinger, Nature (London) 445, 65 (2007).  
[23] M. S. Tame, R. Prevedel, M. Paternostro, P. Böhi, M. S. Kim, and A. Zeilinger, Phys. Rev. Lett. 98, 140501 (2007).

[24] Z. Zhao, Y.-A. Chen, A.-N. Zhang, T. Yang, H. J. Briegel, and J.-W. Pan, Nature (London) 430, 54 (2004).  
[25] X.-C. Yao, T.-X. Wang, H.-Z. Chen, W.-B. Gao, A. G. Fowler, R. Raussendorf, Z.-B. Chen, N.-L. Liu, C.-Y. Lu, Y.-J. Deng et al., Nature (London) 482, 489 (2012).  
[26] C.-Y. Lu, W.-B. Gao, J. Zhang, X.-Q. Zhou, T. Yang, and J.-W. Pan, Proc. Natl. Acad. Sci. USA 105, 11050 (2008).  
[27] B. A. Bell, D. A. Herrera-Martí, M. S. Tame, D. Markham, W. J. Wadsworth, and J. G. Rarity, Nat. Commun. 5, 3658 (2014).  
[28] B. P. Lanyon, P. Jurcevic, M. Zwerger, C. Hempel, E. A. Martinez, W. Dur, H. J. Briegel, R. Blatt, and C. F. Roos, Phys. Rev. Lett. 111, 210501 (2013).