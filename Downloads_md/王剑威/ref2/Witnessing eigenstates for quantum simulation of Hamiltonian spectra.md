# PHYSICS

# Witnessing eigenstates for quantum simulation of Hamiltonian spectra

Raffaele Santagati, $^{1*}$  Jianwei Wang, $^{1*}$  Antonio A. Gentile, $^{1*}$  Stefano Paesani, $^{1}$  Nathan Wiebe, $^{2\dagger}$  Jarrod R. McClean, $^{3,4}$  Sam Morley-Short, $^{1,5}$  Peter J. Shadbolt, $^{6}$  Damien Bonneau, $^{1}$  Joshua W. Silverstone, $^{1}$  David P. Tew, $^{7,8}$  Xiaoqi Zhou, $^{9\dagger}$  Jeremy L. O'Brien, $^{1}$  Mark G. Thompson $^{1\dagger}$

The efficient calculation of Hamiltonian spectra, a problem often intractable on classical machines, can find application in many fields, from physics to chemistry. We introduce the concept of an "eigenstate witness" and, through it, provide a new quantum approach that combines variational methods and phase estimation to approximate eigenvalues for both ground and excited states. This protocol is experimentally verified on a programmable silicon quantum photonic chip, a mass-manufacturable platform, which embeds entangled state generation, arbitrary controlled unitary operations, and projective measurements. Both ground and excited states are experimentally found with fidelities  $>99\%$ , and their eigenvalues are estimated with 32 bits of precision. We also investigate and discuss the scalability of the approach and study its performance through numerical simulations of more complex Hamiltonians. This result shows promising progress toward quantum chemistry on quantum computers.

Copyright © 2018 The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim to original U.S. Government Works. Distributed under a Creative Commons Attribution License 4.0 (CC BY).

# INTRODUCTION

The simulation of quantum mechanical systems, using conventional classical methods, requires resources that make the problems rapidly intractable when the size of the system grows (1). Since Feynman's seminal proposal, several algorithms for quantum simulation have followed (2-4), and many demonstrations have been reported in different physical systems (5-14). Calculating the spectrum of a given Hamiltonian is a fundamental problem of widespread applicability, necessary, for example, to understand reaction rates or optical spectra in quantum chemistry. In particular, characterization of excited states is required to study energy and charge transfer processes, such as those in bulk heterojunction solar cells or photosynthetic light-harvesting complexes (5-16). These kinds of problems are hard for classical computers and, in the most general case, for quantum computers as well. However, quantum devices are expected to provide scalable solutions to some instances of interest (2, 3). Furthermore, also in those cases where classical methods can successfully describe the ground state (for example, for weakly interacting Hamiltonians), excited states are often hard to access (17, 18), increasing the interest toward quantum methods able to address the problem of finding an efficient description of excited states. Here, we show promising progress in this direction by introducing the concept of an "eigenstate witness," a quantity that has no known efficient analog in classical algorithms. This witness is based on the entropy acquired by a quantum register, whose time evolution is controlled by an ancillary qubit.

<sup>1</sup>Quantum Engineering Technology Labs, H. H. Wills Physics Laboratory and Department of Electrical and Electronic Engineering, University of Bristol, Bristol BS8 1FD, UK. <sup>2</sup>Quantum Architectures and Computation Group, Microsoft Research, Redmond, WA 98052, USA. <sup>3</sup>Computational Research Division, Lawrence Berkeley National Laboratory, Berkeley, CA 94720, USA. <sup>4</sup>Google Inc., Venice, CA 90291, USA. <sup>5</sup>Quantum Engineering Centre for Doctoral Training, H. H. Wills Physics Laboratory and Department of Electrical and Electronic Engineering, University of Bristol, Bristol BS8 1FD, UK. <sup>6</sup>Department of Physics, Imperial College London, London, SW7 2AZ, UK. <sup>7</sup>School of Chemistry, University of Bristol, Bristol BS8 1TS, UK. <sup>8</sup>Max Planck Institute for Solid State Research, Heisenbergstraße 1, 70569 Stuttgart, Germany. <sup>9</sup>State Key Laboratory of Optoelectronic Materials and Technologies and School of Physics, Sun Yat-sen University, Guangzhou S10275, China.

*These authors contributed equally to this work.  
†Corresponding author. Email: raffaele.santagati@bristol.ac.uk (R.S.); nawiebe@microsoft.com (N.W.); zhouxq8@mail.sysu.edu.cn (X.Z.); mark.thompson@bristol.ac.uk (M.G.T.)

Given an approximate eigenstate, the quantum phase estimation algorithm (QPEA) can efficiently estimate the corresponding eigenvalue. A more practical version, the iterative phase estimation algorithm (IPEA) (19), has been demonstrated using different quantum hardware, such as nuclear magnetic resonance, photonic, and superconducting systems (9-11). To prepare the input eigenstates, adiabatic state preparation has been proposed as a potentially scalable solution (3), at the cost of expensive state preparation and deep circuits, making it unsuitable for near-term implementations on quantum computers.

Variational quantum eigensolvers (VQEs), using a hybrid quantum-classical approach, were designed to address these shortcomings (10, 12, 20-23). These methods prepare states described via a chosen parameterization, known as ansatz, leveraging pre-existing knowledge about the system. Different types of ansatz have been proposed for the variational search, such as the unitary coupled cluster (UCC), which is among the most promising ones to tackle quantum chemistry problems (12, 20, 24). In addition, VQE methods are believed to have unique robustness to certain errors in estimating the ground state and its eigenvalue (10, 25). They are, however, quadratically less precise than QPEA, because they rely on sampling for the energy estimation in the original formulation. Crucially, variational methods could only target ground states to date.

A linear response methodology and a spectrum folding method have been proposed as possible solutions (12, 25, 26). However, although the linear response methodology maintains the low coherence time advantages of the original VQE, it requires additional sampling measurements and cannot refine approximate excited states. Instead, the folded spectrum (FS) method requires a quadratic increase in the number of terms of the effective Hamiltonian and, consequently, in the computational cost of the procedure. Thus, experimental demonstrations have been limited to ground states, despite the practical importance of excited states.

Here, by introducing the concept of an eigenstate witness, we develop a new method that also targets excited states. A crucial limitation for the solution of the eigenvalue problem is that no method for eigenstate preparation is expected to be scalable in general (3). It remains unanswered, whether variational methods can solve particular classes of this problem. However, it is widely conjectured that eigenstates of physically relevant Hamiltonians often can be efficiently represented

within an ansatz (3, 4, 12, 20). In these cases, we estimate that the number of applications of controlled operations required to perform our algorithm increases polynomially with the size of the system.

We demonstrate this method in a proof-of-principle experiment and test its performance via numerical simulations on higher-dimensional Hamiltonians. For the implementation of the algorithm, we developed a two-qubit quantum photonic processor on a silicon photonic platform (27). This device embeds the key functionalities of on-chip entangled state generation (28-30), tomography (28, 31), and arbitrary controlled unitary operations  $(C\widehat{U})$ . To perform the latter, we exploited an entanglement-based scheme (32, 33).

# RESULTS

# The WAVES protocol

The approach proposed here, witness-assisted variational eigenspectra solver (WAVES), is divided into three main steps (Fig. 1A): (i) an ansatz-based variational search for the ground state; (ii) a witness-assisted variational search for excited states, starting with an initial guess obtained from the ground-state reference as outlined below; and (iii) IPEA for the accurate energy estimate of the eigenstates found.

The quantum logic circuits for WAVES are shown in Fig. 1 (B and C). The search (Fig. 1B) proceeds by preparing trial states  $|\Psi \rangle_T$  in the target register, according to the ansatz, and setting the control qubit to  $|+ \rangle_C$ . The combined state  $|+ \rangle_C \otimes |\Psi \rangle_T$  is then evolved through a controlled unitary  $(C\hat{U})$  operation that embeds the unitary  $\hat{U} = e^{-i\hat{H}t}$  for the evolution of  $|\Psi \rangle_T$  according to the Hamiltonian  $\hat{H}$ , for a time  $t$ . The emerging control qubit state  $\rho_C = \mathrm{Tr}_T(\rho)$  is then analyzed by single-qubit state tomography, from which it is possible to calculate the von Neumann entropy  $S(\rho_T) = S(\rho_C)$ . The entropy acts as an eigenstate witness: It is zero if the target state is an eigenstate of the Hamiltonian. In particular, for small  $t$ , the von Neumann entropy and the linear entropy are upper- and lower-bounded by monotonic functions of the support of  $|\Psi \rangle$  in the eigenbasis of  $\hat{H}$ ; that is, they are sensible measures of such support (see section S1).

This measurement of the entropy enables us to variationally target excited states as well as the ground state. The control qubit also provides

an energy estimator  $\mathcal{E} = -\mathrm{Arg}[T\langle \Psi |e^{-iHt}|\Psi \rangle_T] / t$  , evaluated using the offdiagonal elements of  $\rho_C$  . The variationally optimal ground state simultaneously minimizes the entropy  $S(\rho_C)$  and the energy estimate  $\mathcal{E}$  Computationally, the task of finding the ground state can be interpreted as an optimization problem using a physically motivated objective function. Here, we adopt  $\mathcal{F}_{\mathrm{obj}} = \mathcal{E} + TS(\rho_C) = \mathcal{E} - T\operatorname {Tr}[\rho_C\ln (\rho_C)]$  , analogous in form to a free energy, where  $T$  is a parameter that trades off between energy optimization and entropy optimization. We call  $\mathcal{P} =$ $\mathrm{Tr}[\rho_C^2 ]$  the purity of the reduced density matrix of the control qubit, which is used to measure the linear entropy  $1 - \mathcal{P}$  , here chosen as an approximation of the von Neumann entropy. We can therefore introduce the more practical objective function

$$
\mathcal {F} _ {\mathrm {o b j}} (\mathcal {P}, \mathcal {E}) = \mathcal {E} - T \mathcal {P} = \mathcal {E} - T \operatorname {T r} [ \rho_ {C} ^ {2} ] \tag {1}
$$

up to negligible constants. The optimization of  $\mathcal{F}_{\mathrm{obj}}$  also permits one to identify excited states, because they occupy local minima in the high- $T$  limit for almost all evolution times  $t > 0$  (section S1). Defining an initial reference state  $|\Phi\rangle$  (usually obtained by mean-field approximations) and the complex vector  $\vec{\theta}$  as the list of parameters describing the ansatz-based state preparation  $\hat{A}(\vec{\theta})$ , that is,  $|\Psi\rangle_T = \hat{A}(\vec{\theta})|\Phi\rangle$ , our algorithm proceeds as follows:

(1) Variationally search for the state parameters  $\hat{\theta}_g$  that minimize the objective function  $\mathcal{F}_{\mathrm{obj}}$ , thus obtaining the unitary for the ground state  $\hat{A}_g = \hat{A} (\hat{\theta}_g)$ .  
(2) Construct a unitary for an approximate  $i$ th target excited state via  $\hat{E}_{p_i}\hat{A} (\vec{\theta}_g)$ , with  $\hat{E}_{p_i}$  being a system-dependent perturbation. Variationally search for the  $\theta_{e_i}$  that minimizes  $\mathcal{F}_{\mathrm{obj}}$  in the high- $T$  limit (entropy), obtaining the unitary for the target excited state  $\hat{A}_{e_i} = \hat{E}_{p_i}\hat{A} (\vec{\theta}_{e_i})$ .  
(3) Using the  $\hat{A}_g$  for the ground state or  $\{\hat{A}_{e_i}\}$  for the excited ones in the state preparation, perform the IPEA, which further projects each state onto the closest eigenstate (34) and refines the energy estimate.

Here, we adopted a swarm optimization method for the experimental variational searches, where, for each iteration,  $\mathcal{F}_{\mathrm{obj}}$  is measured for a swarm of trial states (particles), randomly sampled from a prior

![](images/eae900dbe98da09eab989c86fae95e047c9541020e4de043d3ab7e6cc4cb076f.jpg)  
Ground-state search using  $\mathcal{F}_{\mathrm{obj}}$  and  $\hat{E}_{\mathrm{p_0}} = \hat{I}$  
Excited-state search using  $\mathcal{S}$  and guessed  $\hat{E}_{p_i}$

![](images/f856ad03a1094d60c09c44146cd564eaf5782f6bca22fa2a559a579dde7e502e.jpg)  
A  
B  
Fig. 1. The WAVES protocol. (A) Flowchart describing the protocol. The optimization of  $\mathcal{F}_{\mathrm{obj}}(\vec{\theta}) = \mathcal{E} + TS$  using the circuit in (B) allows one to variationally find the ground state of the Hamiltonian, preparing trial states via the ansatz  $\hat{A} (\vec{\theta})$  with no perturbation  $(\hat{E}_{p_0} = \hat{l})$ . An initial guess for an excited state is given by a perturbation  $\hat{E}_{p_i}$  on the ground state and then refined using the same circuit by exploiting the eigenstate witness  $\mathcal{F}_{\mathrm{obj}}(\vec{\theta}) = S$  (high- $T$  limit). (C) For each target eigenstate found, the eigenvalues are precisely estimated via the IPEA using the quantum logic circuit, where  $H$  is the Hadamard gate. The color coding in (B) and (C), blue for the control and red for the target, refers to the difference in wavelength between the photon in the control qubit and the one in the target register in our experimental implementation. (D) Diagram schematically representing the intuition behind the proposed approach, where initial guesses of excited states are variationally refined using the witness and IPEA returns the eigenvalues.

![](images/ed65a7da4f1cf2927ddc9c97e9d395ae6dad3bcc3f37ea1262e6fafde2858339.jpg)  
C

![](images/03362245a7fe81ce94a32214c823d406787890cc421ca2ac9056596dc7f1c448.jpg)  
Eigenvalues estimation using IPEA  
D

distribution, and used to infer a posterior with lower  $\mathcal{F}_{\mathrm{obj}}$  (for more details on the optimization method, see section S2). We call each of the iterations an "epoch." The computational complexity of using our variational method to learn eigenvalues of the Hamiltonian can be quantified by the number of controlled unitary operations performed in the simulation, which depend on the optimization method used. For the particle swarm gradient-free optimization, the computational cost of sampling from the eigenspectrum of  $\hat{H}$  is described by Theorem 1. A version for gradient-based methods is instead reported in the "Computational cost of WAVES for gradient-based methods" section (both demonstrations can be found in section S3).

Theorem 1. Let  $\hat{H} \in \mathbb{C}^{2^n \times 2^n}$  be Hermitian and assume that after  $k \in \{1, \dots, N_{\mathrm{iter}}\}$  epochs, the state  $|\psi_T(k)\rangle = \sum \alpha_i(k)|\lambda_i\rangle$ , where  $\hat{H}|\underline{\lambda}_i\rangle = \lambda_i|\lambda_i\rangle$  for  $\lambda_i \geq 0$ , and that the sequence of sets of particles  $\{\Xi(k) := \{\theta_j\}\}$  satisfies  $\max_{\vec{\Theta} \in \Xi(k)} \|\vec{\phi} - \mathbb{E}_{\vec{\Theta} \in \Xi(k)}(\vec{\Theta})\|_{\max} \leq x_{\max}$  and  $\dim(\Xi(k)) = N \forall k$ . Then, the number of applications of controlled  $e^{-i\hat{H}t}$ , for  $[0, \pi/(2\|\hat{H}\|)] \ni t \in \Theta(\|\hat{H}\|^{-1})$ , required for our particle swarm optimization algorithm to learn an eigenvalue within error  $\epsilon$ , with a probability of at least  $1/2$  is in

$$
O \left(N _ {\text {i t e r}} N \dim (\vec {\theta}) \left(\frac {\| \hat {H} \| ^ {2}}{\min  _ {k} \sum_ {i} | \alpha_ {i} (k) | ^ {4}} + T ^ {2}\right) \left[ \frac {\Gamma}{\delta} \right] ^ {2} + \frac {1}{\epsilon}\right)
$$

where  $\delta$  is the maximum error in the evaluation of  $\mathcal{F}_{\mathrm{obj}}$  allowed and  $\{\epsilon_{\mu}^{2}(k)\}$  ( $\{\epsilon_{\Sigma}^{4}(k)\}$ ) is the corresponding tolerance in the (variance of the) trace of the covariance matrix of the sample mean. Finally, we define  $\Gamma \coloneqq \max_k(x_{\max}(k) / \epsilon_{\mu}(k), x_{\max}^2(k) / \epsilon_{\Sigma}^2(k))$ .

The above theorem implies that, in this regime, the relevant scaling parameter for iteration cost is the dimension of the parameter space. The problem of finding an appropriate ansatz is beyond the scope of this work: It is expected though to be polynomial in the number of spin orbitals for many physically relevant systems (3, 4, 20, 21, 24, 35). Similarly, the number of swarm particles required  $(N)$  and the number of variational steps  $(N_{\mathrm{iter}})$  depend on both the dimension of the relevant parameter space and prior knowledge about the solution. Because the particles are moved toward the true model as the algorithm learns,  $N$  is expected to scale polynomially (36) for problems, such as chemistry, where a good ansatz and a high degree of prior knowledge are possible. These considerations lead to the implicit scaling of the number of controlled unitary applications, which is expected to increase with the number of spin orbitals  $(n)$  in the system. The number of variational parameters, together with the number of swarm particles required for these specific ansätze to achieve chemical accuracy, will likely require empirical studies to be precisely estimated. Further breakdown in the cost estimates can be considered by decomposing the controlled unitary into fundamental gates using Trotter-Suzuki or linear combination-based methods (37), but here, we ignored these issues for simplicity. If Trotter-Suzuki methods are also taken into account for the simulation, then there is a factor of roughly  $n^{5.5}$  multiplied by the above costs (38).

Another fundamental point is how to choose the excitation operators used in the excited-state variational search. Consistent choices for the system- and state-specific perturbing unitaries  $\hat{E}_{p_i}$ , required to construct the excited states, can be inferred from readily computable properties of the simulated system (25). General many-body Hamiltonians for interacting particles decompose into  $\hat{H} = \hat{H}_0 + \hat{V}$ , where  $\hat{H}_0 = \sum \epsilon_i \hat{a}_i^\dagger \hat{a}_i$  is a one-particle term and  $\hat{V}$  is an interaction term. Because  $\hat{H}_0$  dominates  $\hat{H}$ , a transition from the ground state to an ex

cited state can be approximated by the action of a sequence of single-excitation operators  $\hat{a}_i^\dagger \hat{a}_j$ , each with a corresponding unitary  $\hat{E}_p = \exp \left[\pi /2\left(\hat{a}_i^\dagger \hat{a}_j - \hat{a}_j^\dagger \hat{a}_i\right)\right]$ . If excitation operators based on the Hartree-Fock approximation do not provide sufficient accuracy, then alternative approximations can be used. Advanced methods, such as multiconfiguration self-consistent field approximations (39), may ultimately be needed for hard instances with substantial electron correlations. In the "Excitation operators for chemical Hamiltonians" section, we further discuss how post-Hartree-Fock methods can be used to tackle these problems through the use of natural orbitals.

# Silicon quantum photonic chip and experimental setup

The experimental demonstration of WAVES was performed on a two-qubit silicon quantum photonic processor schematically described in Fig. 2. The device is fabricated via deep-ultraviolet lithography on a silicon-on-insulator wafer with  $450\mathrm{nm}\times 220\mathrm{nm}$  single-mode waveguides. A continuous-wave (CW) pump laser in the telecom C band with an off-chip power of approximately  $10\mathrm{mW}$  is coupled into the chip using polymer spot-size converters and lensed fibers, with a facet loss of approximately 8 dB. Pairs of single photons are generated in two 1.2-cm-long waveguide spiral sources through spontaneous four-wave mixing (SFWM) (27). Output photons are filtered using arrayed waveguide gratings (AWGs) with a  $0.9\mathrm{-nm}$  bandwidth, spectrally selecting signal photons (blue) for the control qubit and idler ones (red) for the target. The photons are detected by superconducting nanowire single-photon detectors (SNSPDs) with approximately  $85\%$  efficiency, obtaining a maximum photon coincidence rate of  $\approx 150\mathrm{Hz}$ . Optical interferometers consisting of thermo-optic phase shifters and multimode interferometer (MMI) beam-splitters are used for photonic qubit manipulation and analysis, driven by an electronic controller with 12-bit digital-to-analog converters. The automation for the WAVES algorithm, including the control of quantum gates, the data collection, and real-time analysis, is realized by a classical computer interfaced with the quantum photonic chip. More experimental details are reported in section S5.

Because of the low-power CW pump used in our experiment, multiphoton terms can be safely neglected. The use of the two spiral sources generates the Fock state  $(|20\rangle + |02\rangle) / \sqrt{2}$ . High-visibility two-photon quantum interference  $(\mathcal{V}_{\mathrm{Qua}} = 1.00 \pm 0.02)$  was observed in this experimental setup, as shown in the inset of Fig. 2. The photons are probabilistically split by two MMIs and then swapped by a waveguide crossing, yielding the maximally path-entangled state  $(|1010\rangle + |0101\rangle) / \sqrt{2}$  in the Fock basis (29, 31). The state of the target photon is then expanded by adding two optical spatial modes. These additional modes represent the two components of the target qubit, which is prepared in  $|\Psi\rangle_T$  for both paths and undergoes an arbitrary  $\hat{U}$ . That is, the operation performed on the target qubit—either  $\hat{I}$  or  $\hat{U}$ —depends on which path the photon is traveling on, indicated by  $|0\rangle_P$  or  $|1\rangle_P$ . Path, in turn, is controlled by the state of the control qubit (the two qubits are entangled),  $|0\rangle_C$  or  $|1\rangle_C$ , which yields a superposition of  $\hat{I}$  and  $\hat{U}$  gates in the circuit

$$
\frac {1}{\sqrt {2}} \left(| 0 \rangle_ {C} \otimes \hat {I} | \Psi \rangle_ {T} \otimes | 0 \rangle_ {P} + | 1 \rangle_ {C} \otimes \hat {U} | \Psi \rangle_ {T} \otimes | 1 \rangle_ {P}\right) \tag {2}
$$

By erasing the path information with the use of an additional waveguide crossing and two final MMIs and by detecting the signal

![](images/3c907367b104074c47b317dd91272ca570fde93a7baccc8a7f4749b255033c16.jpg)  
Fig. 2. Silicon quantum photonic processor. The quantum device enables one to produce maximally path-entangled photon states, perform arbitrary single-qubit state preparation and projective measurements, and, more importantly, perform any  $CU$  operation in the two-dimensional space. Photons are guided in the silicon waveguides and controlled by thermo-optical phase shifters. Photon pairs are directly generated inside the silicon spiral sources through SFWM, off-chip-filtered and postselected by AWG filters (not shown), and measured by SNSPDs. The generated signal (blue) and idler (red) photons are different in wavelength and form the control and target qubits, respectively. The quantum chip is interfaced with a classical computer. Inset: High-visibility quantum (blue) and classical (green) interference fringes obtained in the device using the photon sources part and configuring the top final interferometer. The high visibility is essential to verify the high-performance and correct characterization of the device.

photon and idler photon, we obtain the controlled unitary  $C\hat{U}$  operation (32, 33, 40, 41)

$$
\frac {1}{\sqrt {2}} \left(| 0 \rangle_ {C} \otimes \hat {I} | \Psi \rangle_ {T} + | 1 \rangle_ {C} \otimes \hat {U} | \Psi \rangle_ {T}\right) \tag {3}
$$

Note that this approach implements the  $C\hat{U}$  gate without decomposing it into multiple two-qubit gates (11). The state preparation is realized by  $\hat{A} = e^{i\phi_a}e^{i\phi_b\hat{\sigma}_z / 2}e^{i\hat{\phi}_c\hat{\sigma}_y / 2}$  operations, whereas the  $\hat{U}$  used to map the Hamiltonian is obtained by  $\hat{U} = e^{i\phi_c\hat{\sigma}_z / 2}e^{i\phi_d\hat{\sigma}_y / 2}e^{i\phi_e\hat{\sigma}_z / 2}$ , where  $\phi_{i}$  are phases applied by on-chip thermal phase shifters. The control qubit undergoes another single-qubit operation that can be used to perform the required operations both for tomography and for the IPEA.

# Experimental results

We used the quantum photonic chip to perform WAVES, calculating the eigenspectrum of a simplified exciton transfer Hamiltonian of two chlorophyll units in the 18-mer ring of the LHII complex. We remark that this simplified model is not intended to provide an accurate description of the LHII system, yet it serves as a useful demonstration and test for our algorithm. The Hamiltonian is parameterized by  $\alpha \simeq 1.46\mathrm{eV}$ , the exciton energy of a single chlorophyll unit, and  $\beta \simeq 0.037\mathrm{eV}$ , the coupling strength between the two units (42). This  $2\times 2$  Hamiltonian is written as  $\hat{H} = (\alpha -\ell)\hat{I} +\beta \hat{\sigma}_x$ , on the basis of Pauli operators (20), where  $\ell$  is a reference energy that can be chosen arbitrarily (see "The single-exciton Hamiltonian: Hamiltonian parameters, mapping, and eigenvalues" section). For this

Hamiltonian, the perturbing unitary for the excited state corresponds to  $\hat{E}_p = e^{i\pi \hat{\sigma}_z / 2}$ .

In Fig. 3, we show the experimental results of the WAVES approach for the ground- and excited-state search. The minimization of the objective function was performed in both cases, adopting the particle swarm method outlined above. In the experiment, the energy  $\mathcal{E}$  and purity  $\mathcal{P}$  used to evaluate  $\mathcal{F}_{\mathrm{obj}}$  were obtained by performing single-qubit tomography of the control photon. In Fig. 3 (A and B), we show the color-coded evolution of the swarm, achieving rapid convergence of the particle distribution toward the expected eigenstates of the Hamiltonian: the ground state  $|\neg \rangle$  and the first excited state  $|+\rangle$ . For the ground-state search, pessimistically assuming no pre-existing knowledge of the system, the prior is initialized to uniformly span the subsection of the Hilbert space identified by the ansatz. For the excited state, instead, the search is initialized with the guessed state obtained by applying  $\hat{E}_p$  to the ground state.

As shown in Fig. 3 (C and D), within 10 to 13 search steps,  $\mathcal{F}_{\mathrm{obj}}$  converges well to its minimal value, which corresponds to the ground state and excited state, respectively. Figure 3 (E and F) shows that the mean of the particle distribution achieves a high overlap with the eigenstate targeted: fidelities of  $99.48 \pm 0.28\%$  with the ground state and  $99.95 \pm 0.05\%$  with the excited state. All uncertainties are given by the variance of the prior distributions: A well-motivated error bar is among the amenable features derived from the adoption of a swarm optimization method.

The successful convergence of  $|\Psi \rangle_T$  is achieved by optimizing the  $\mathcal{F}_{\mathrm{obj}}$  function. In particular, for the ground-state search, we used a small value of  $T$  ( $T = 1.25$ ) in  $\mathcal{F}_{\mathrm{obj}}$ , whereas for the excited state case, we used  $\mathcal{F}_{\mathrm{obj}} \equiv -\mathcal{P}$  (that is, high- $T$  limit). Imperfect measurements of

![](images/991fb63dac0b51358ad1088bda4729c9e4e1936e068ae0e231c425b9d81f12fa.jpg)  
A  
B

![](images/140b37657a85a691a74f43ac128afbe0b8849f48dcd3e492512e0968f60e1995.jpg)

![](images/2fc00ff6773c3f1257704bea642488afb6dd6d658c00f778abe1cc52a68075c0.jpg)  
C

![](images/a82da8449bbe57215d52f6700cdf424409d07766f87d4ca50957ce6ec34875d6.jpg)  
D

![](images/27d6c8be4862cad4b2e01e94032f356acdd0d056ca8dbebf886bbe384e72b280.jpg)  
G  
Fig. 3. Experimental results. A Hamiltonian representing a single-exciton transfer between two chlorophyll units is implemented on the silicon quantum photonic device for an experimental test of the protocol. (A and B) Color-coded evolution of the particle swarm for the WAVES search of the ground state  $(| - \rangle)$  and excited state  $(| + \rangle)$  shown on the Bloch spheres. Different colors correspond to different steps of the search protocol. For the ground and the excited state searches, we report the evolution of  $\mathcal{F}_{\mathrm{obj}}$  in (C) and (D) and the fidelity  $(F = |\langle \Psi |\Psi_{\mathrm{ideal}}\rangle |^2)$  versus search steps in (E) and (F), converging to a final value of  $99.48\pm 0.28\%$  and  $99.95\pm 0.05\%$ , respectively. Error bars are given by the variance of the particle distribution and photon Poissonian noise. Dashed lines are numerical simulations of the performance of the algorithm, averaged over 1000 runs, with shaded areas representing a  $67.5\%$  confidence interval. Insets: Behavior close to convergence. (G and H) Normalized photon coincidences used to calculate the 32 IPEA-estimated bits of the eigenphase for both eigenstates. The theoretical bit value is shown above each bar. Errors arising from Poissonian noise are shown as shaded areas on the bars.

![](images/8e8040b96bccd9a14ef979dfd2f1e5a1b524037083e47f272b581cb5f29d4c98.jpg)  
H

$\mathcal{F}_{\mathrm{obj}}$ , more evident in the regime close to convergence, are mainly due to experimental noise in the phase settings, given by residual thermal cross-talk among the phase shifters. The fast convergence of the algorithm, however, indicates a good robustness of the protocol to this kind of experimental noise.

After the eigenstate search, the WAVES algorithm embeds the IPEA to improve the accuracy of eigenvalue estimates (3, 11). In our implementation, we took advantage of circuit reconfigurability, mapping each  $\hat{U}^{2k}$  directly into the chip parameters (Fig. 1C). However, in universal quantum computers,  $\hat{U}^k$  can be efficiently achieved without classical precompilation by cascading  $k$  copies of  $\hat{U}$  (10). The IPEA estimated the binary fraction expansion of the eigenphase  $\varphi (\mathrm{mod} 2\pi)$  for both the ground- and excited-state energies up to 32 bits (that is, a precision of  $2.9\times 10^{-9}\mathrm{eV}$ ). The normalized photon counts are shown in Fig. 3 (G and H) for all the 32 bits. This precision is higher than what is typically achievable by spectroscopic methods.

# Numerical results for higher-dimensional systems

We complement these proof-of-principle experimental results with a set of numerical simulations, providing insight into the performance of our approach when applied to more complex Hamiltonians. For our numerical tests, we chose a set of molecular hydrogen systems  $(\mathrm{H}_2,\mathrm{H}_3^+,\mathrm{H}_3$  and  $\mathrm{H_4}$ ). The corresponding Hamiltonians (up to 8 qubits) are represented in a Slater-type orbital basis (43) in the Jordan-Wigner representation (see the "Hydrogen molecules: Mapping and ansatz" section) (20) and exhibit several degeneracies in the spectrum. For each set of degenerate excited states, we will refer generically to the excited subspace they span.

Figure 4 (A and B) shows the simulation results of the ground-state search and some exemplary excited-state variational searches, respectively, addressing the latter ones with a set of excitation operators of the form  $\hat{E}_{p_i}$ . Note that this is only the first (variational) part of WAVES and that the second part (IPEA) will further project the state found into the eigenstate with a higher overlap. This feature is absent in previous VQE implementations. For the different cases, we increased the number of particles to 8, 16, 30, and 50

for  $\mathrm{H}_2$ ,  $\mathrm{H}_3^+$ ,  $\mathrm{H}_3$ , and  $\mathrm{H}_4$ , respectively, which follows approximately linearly the number of parameters involved in the "parameterized Hamiltonian" (PH) ansatz provided in section S7 and adopted for these simulations.

In all the cases investigated here, WAVES is able to consistently find both the ground and excited states with high fidelities ( $\simeq 99\%$  in average). The insets of Fig. 4 show that the final fidelities achieved by each variational search do not decrease (within error tolerance) when increasing the size of the Hilbert space. Although these study cases do not imply scalability of the approach, they provide an encouraging result, suggesting that to keep constant the algorithm performances with the dimensionality of the problem, a subexponential increase in number of particles and iterations is enough, provided that a polynomial parameterization applies.

# DISCUSSION

We have introduced the concept of eigenstate witness and used it to develop WAVES, a new quantum method for targeting both ground and excited states of a physical Hamiltonian. We showed its proof-of-principle implementation on a silicon quantum photonic chip for a simplified exciton transfer Hamiltonian, obtaining its eigenstates with high fidelities and estimating the eigenvalues up to spectroscopic accuracy. Additional analysis of WAVES performances is provided by numerical simulations, where the protocol yields eigenstate estimates with high fidelity for Hamiltonians of up to 8 qubits.

All states found using the variational search, both in the experiments and in the numerical simulations, exhibited high fidelities with the target eigenstates. This preliminary refinement provides IPEA with an improved approximation of the target eigenstate, leading to an exponentially higher success probability in estimating the corresponding eigenvalue and reducing the overall complexity. Using IPEA, in addition to the variational search, allows the projection onto the eigenvectors, which is not guaranteed by the solely variational methods using a polynomial-sized ansatz. As the size of the system simulated increases, the shrinking of some energy gaps may lead to

![](images/f4c00f63268db9f19329f8b202f870015f01d3aa12f8be328ca3c360961925be.jpg)  
Fig. 4. Numerical simulations for higher-dimensional Hamiltonians. The cases studied refer to molecular hydrogen systems  $(\mathsf{H}_2,\mathsf{H}_3^+, \mathsf{H}_3,\mathsf{H}_4)$  with the full PH ansatz. (A) Variational search for the ground state of each physical system. (B) Variational search for the targeted subspace of degenerate excited states with an initial excitation perturbation  $\dot{E}_{p_i}$ . On the  $x$  axis, we refer to the cumulative number of trial states probed (that is, the number of particles in the swarm times the variational steps). For ease of comparison, the  $x$ -axis origin has been shifted in (A) for the various cases to have equivalent fidelity for the average initial guess. Dashed lines denote average fidelities, with the shaded areas indicating a  $67.5\%$  confidence interval. The average fidelities achieved by the particle swarm optimization for both ground and excited states are calculated for 100 independent runs of WAVES. In all simulations, a binomial noise model has been taken into account when performing projective measurements. Insets: Bar charts summarizing final fidelities obtained by each search. All the simulations converged to the same high fidelity within errors, as indicated by the dashed black line in the inset.

![](images/8f67fdd314b9c98f60f8f59eeea6e8b15d4a7042512557d41b0ff0834d6a696f.jpg)

eigenstates close in energy being sensed as effectively degenerate by the variational witness, within the precision achievable by the experimental platform of choice. In these cases, the VQE-refined guess will exhibit consistent overlap with more than one eigenstate. Nevertheless, careful modifications to the phase estimation procedure may allow one to learn exponentially quickly either one of the eigenvalues belonging to almost-degenerate eigenstates (section S4). In summary, the variational search acts as a state preparation stage for the phase estimation, whereas the IPEA step addresses the shortcomings present in the variational ansatz.

From our study, for a particular ansatz (for example, UCC) and using low-order Trotter formulas, the time required by WAVES is expected to explicitly scale with the problem size as  $O(Mn^{5.5})$ , where  $n$  is the number of spin orbitals and  $M$  is the number of variational parameters, in accordance with simulation results reported by Reiher et al. (37) for systems difficult to simulate classically, such as nitrogenase. This does not automatically imply that WAVES or any other eigenstate preparation method is efficient for any Hamiltonian, because that would imply that QMA = BQP, where QMA stands for "quantum Merlin Arthur" and BQP for "bounded-error quantum polynomial time," respectively (44), which is widely believed to be false. However, an optimization based on an eigenstate witness allows the variational algorithm to address the problem of efficiently estimating an eigenvalue in the vicinity of a generic targeted state, in those cases where a polynomial-sized ansatz can be provided. This problem is generally expected to be hard on classical machines, and it is challenging to solve using traditional variational methods.

WAVES offers key improvements over previous protocols. For those instances where a good ansatz is found, it can be used to locate excited states with a quantum method in a purely variational manner, in contrast to quantum-classical linear response methods (25). These methods avoid the need for additional nonlinear optimization, but this may limit their accuracy, and they do not yet use quantum phase estimation to improve the final accuracy and readout precision as in WAVES. Furthermore, one can speculate how the eigenstate witness provides an independent test of the protocol's success, detecting failure cases of convergence to local optima that do not represent a single eigenstate or excited subspace (see also section S7). These advantages come at the cost of controlling the evolution of the target register with an ancillary qubit, which is avoidable in previous VQE proposals. In addition, in WAVES, the ability to find specific eigenstates relies on the quality of the excitation operators. Further optimization on the objective function, for example, including the use of an energy penalty, can, in principle, overcome some of these limitations.

In terms of resource costs, the use of IPEA gives a quadratic speedup compared to standard VQE in estimating the energy of an eigenstate within a chosen precision. These advantages are significant given the high accuracy required in quantum chemical applications (24). Moreover, WAVES does not require lengthy adiabatic preparation of targeted eigenstates (3, 9, 20) or an increase in the number of terms of the implemented Hamiltonian and a precise knowledge of the spectral gap, unlike the FS method. In particular, the FS method reduces to variational optimization of a shifted and squared Hamiltonian  $H' = (H - \lambda)^2$ , thus squaring both its norm and number of terms. The choice of the shift parameter  $\lambda$  can also result in accidental degeneracies in the spectrum and dramatic closing of small spectral gaps. In the case of a problem, such as quantum chemistry, this can lead to  $O(n^8)$  terms formally in the Hamiltonian, drastically increasing the cost and making it cumbersome for even small instances (12, 20). Moreover,

the ultimate accuracy of FS methods matches the accuracy of the variational ansatz used. However, WAVES corrects essentially all of these difficulties. It retains the original norm, spectrum, and number of terms in the Hamiltonian  $O(n^{4})$ ; does not depend on a shift parameter; and exceeds the accuracy of the variational ansatz used through projective phase estimation. In sections S6 and S7, the interested reader can find numerical simulations comparing WAVES with previous VQE implementations and with the FS method. The results show, in particular, that the FS method finds states with poor overlap with any true eigenstate in cases exploiting its weaknesses, whereas WAVES provides estimates exceeding  $99\%$  fidelity with a correct eigenstate in all cases tested. This direct comparison indicates higher reliability for WAVES, adding to the improvements in terms of resource costs.

In conclusion, WAVES is a new approach to tackling the search for both ground and excited states of physical Hamiltonians. The analysis performed shows that the method is expected to be scalable, under the assumption that a good ansatz can be found. The experimental demonstration on a quantum photonic chip and numerical simulations show the method performance on small-scale scenarios, indicating good noise resilience properties and better performances if compared to previous approaches. Our algorithm is, in principle, amenable to short circuit depths and leverages methods known to exhibit error robustness, thus enabling near-term experiments on non-fault-tolerant machines. By introducing new objective functions for variational algorithms, this protocol opens the way to the investigation of new methods for computing Hamiltonian spectra and represents a promising tool for future developments of quantum simulation on quantum computers.

# MATERIALS AND METHODS

Computational cost of WAVES for gradient-based methods In the following theorem, the computational cost for the case of gradient-based methods is reported. Proof is given in section S3.1.

Theorem 2. Let  $\hat{H} \in \mathbb{C}^{2^n \times 2^n}$  be Hermitian and assume that after  $k \in \{1, \dots, N_{\mathrm{iter}}\}$  epochs, the state  $|\psi_T(k)\rangle = \sum_i \alpha_i(k)|\lambda_i\rangle$ , where  $\hat{H}|\lambda_i\rangle = \lambda_i|\lambda_i\rangle$  for  $\lambda_i \geq 0$ . Furthermore, assume that there exists a numerical differentiation formula that evaluates  $\partial_{\theta_q} \mathcal{F}_{\mathrm{obj}}$  using a constant number of function evaluations on a grid of spacing  $h > 0$  within error at most  $\kappa(h\Lambda)^p$  for positive  $\kappa$  and  $\Lambda$  for  $p \in \Theta(1)$ . Then, the number of applications of controlled  $e^{-i\hat{H}t}$ , for  $(0, \pi/(2\|\hat{H}\|) \ni t \in \Theta(\|\hat{H}\|^{-1})$ , required in the algorithm is in

$$
O \left(N _ {\text {i t e r}} \kappa^ {\frac {2}{p}} \Lambda^ {2} \dim (\vec {\theta}) \left(\frac {\| \hat {H} \| ^ {2}}{\min _ {k} \sum_ {i} | \alpha_ {i} (k) | ^ {4}} + T ^ {2}\right) \left[ \frac {\dim (\vec {\theta})}{\delta} \right] ^ {\frac {2 p + 4}{(p + 1)}} + \frac {1}{\epsilon}\right)
$$

where  $\delta$  is the maximum error in the two-norm of the gradient of  $\mathcal{F}_{\mathrm{obj}}$  allowed and  $\epsilon$  is the maximum error allowed in phase estimation of the final system with a probability of  $1/2$ .

It is then clear from the analyses contained in Theorems 1 and 2 that the particle swarm method has the potential to outperform the gradient-based method in cases where many parameters are required to describe the ansatz state and  $\Gamma$  is modest. However, the rate at which the two learn can differ substantially, because the same number of iterations may provide more or less information than the other case. In practice, gradient-based methods may be

more practical to find an optimal solution in the vicinity of local optima, whereas global methods, such as our particle swarm method, may provide a better method for approaching them. Because the scaling of the Bayesian optimization approach with the number of variational parameters is better than the bounds that we prove for gradient-based optimization, we assumed that these approaches would be better in high-dimensional problems. Moreover, being inspired by ideas from approximate Bayesian inference, the latter retains part of their noise robustness. For these reasons, we focused on the particle swarm method for experiment and simulations in this work.

Finally, although both methods scale quadratically with  $T$ , in practice, the scaling will not typically be so bad. If  $\delta$  is chosen to guarantee fixed relative error for the process, then the cost approaches  $T^2 / \delta^2$ , which is constant. This means that the quadratic scaling of  $T$  is not necessarily problematic in cases where the WAVES algorithm is optimizing for purity.

# Excitation operators for chemical Hamiltonians

Our method for locating excited states variationally used approximate excitation operators to enhance the rate at which excited states may be located. Quantum chemistry has a long history of using the theory of linear response to external perturbations to approximate excited states of the system (45). The accuracy of this approximation relies on the partitioning of the total Hamiltonian into  $\hat{H} = \hat{H}_0 + \hat{V}$ , where  $\hat{H}_0$  is a noninteracting Hamiltonian of the form  $\hat{H}_0 = \sum_{ij} h^{ij} b_i^\dagger b_j$  and  $\hat{V}$  is an interacting perturbation. In quantum chemistry, this partitioning is often taken to be  $\hat{H}_0 = \hat{F}$ , where  $F$  is the Fock operator that includes one-body and averaged two-body interactions, and  $V$  is the remainder. For many systems,  $\hat{V}$  is small enough such that a perturbation treatment suffices (46).

As a noninteracting Hamiltonian,  $\hat{H}_0$  may be efficiently diagonalized by a unitary transformation such that  $\hat{H}_0 = \sum_i\epsilon_i a_i^\dagger a_i$ , where  $\epsilon_{i}$  are the eigenvalues of the free-fermion Hamiltonian. In this model, excited states may be formed through excitation operators of the form  $a_{i}^{\dagger}a_{j}$  acting on the ground state, where  $j$  indexes sites currently occupied by electrons and  $i$  indexes unoccupied sites. If  $\hat{V}$  is comparatively small, these eigenstates will approximate eigenstates of the true Hamiltonian, and one may refine estimates within the single-particle approximation space by diagonalizing the Hamiltonian on the basis of vectors  $\{a_i^\dagger a_j|\Psi \rangle \}$ , where  $|\Psi \rangle$  is some reference state. This method is called the configuration interaction singles method. The connection may also be seen in the context of the first-order time-dependent response to an external field. For quantum computers, variations of these states may be prepared by the unitary operators  $\hat{E}_{\mathrm{ij}}(\theta) = \exp [\theta (a_i^\dagger a_j - a_i^\dagger a_i)]$ .

In the case of weak interactions, classical methods, such as coupled cluster, have been successful in describing the ground state; however, even low-lying excited states in these systems may exhibit correlation structures and entanglement that prevent their efficient description. This is reflected in their difficulty of simulation by current classical methods (17, 18) and represents a key motivation for quantum methods, such as WAVES, to study excited states. Moreover, we stress that the single excitations here represent initial guesses for WAVES to search through correlated states not accessible to classical simulation and that these single excitations may be derived from a reduced density matrix, using a procedure described below, which was not accessible classically due to quantum correlations in the ground state. The WAVES method refines these initial guesses

through optimization and then projects to a dominant eigenstate by using phase estimation.

In quantum computing, one hopes to go beyond states that are well approximated by mean-field solutions through preparation of states with nontrivial entanglement. In the VQE approach, these states are defined by the parameterization of the ansatz; however, unlike classical approaches, we may not have efficient access to full knowledge of the wave function we are preparing. In these cases, a possible approach to generating excitation operators is to look for the "closest" one-body system. This problem defines the so-called natural orbitals in quantum chemistry (47), which are the orbitals that diagonalize the one-electron reduced density matrix (1-RDM) of the prepared state, given by

$$
D _ {i j} = \left\langle \Psi \right| a _ {i} ^ {\dagger} a _ {j} | \Psi \rangle \tag {4}
$$

that may be efficiently measured on any prepared quantum state, including those with entanglement. As a symmetric positive semidefinite matrix, it may be diagonalized to yield a set of excitation operators  $c_{i}^{\dagger}c_{j}$  to approximate the excited states of the interacting system. Note that in the case of an antisymmetric product state reference, such as that generated by Hartree-Fock, these orbitals are identical to those discussed above for  $\hat{H}_0 = \hat{F}$ , as the canonical Hartree-Fock orbitals diagonalize the 1-RDM of a single antisymmetric product state.

# The single-exciton Hamiltonian: Hamiltonian parameters, mapping, and eigenvalues

Previous demonstrations of digital quantum simulation have focused almost exclusively on systems of interacting fermions such as electronic structure in molecules or the Fermi-Hubbard spin lattice model. Here, we performed numerical simulations for several such cases in section S7, reporting performances of WAVES in correctly identifying the eigenstates for the molecules  $\mathrm{H}_{2}$  to  $\mathrm{H}_{4}$ .

However, physically interesting Hamiltonians are not restricted to interacting fermions and it is important to extend quantum simulation methodologies to general systems of interacting quantum particles and quasi-particles so that quantum simulation can have an impact on a broad range of problems relevant to physics, chemistry, biology, and materials science. The spectrum of a  $2 \times 2$  bosonic Hamiltonian was adopted for the experimental demonstration of WAVES in the main paper. We therefore required a method to convert the bosonic Hamiltonian  $e^{-i\hat{H}t}$  into a sequence of unitary operations that can be implemented on a quantum computer. This is significant because there is not a simple analog of the Jordan-Wigner transformation that maps bosonic occupation numbers to qubits. For example, if  $\hat{H}$  had a concise Pauli decomposition, then Trotter-Suzuki formulas can be used to write  $e^{-i\hat{H}t} \approx e^{-i\hat{P}_1t} e^{-i\hat{P}_2t} \dots$  for Pauli operators  $\hat{P}_1, \hat{P}_2, \dots$ . General-purpose simulation methods can be used to express  $\hat{H}$  as a sum of (at most)  $O(N^6)$  one-sparse matrices, provided that  $\hat{H}$  does not contain interactions higher than two-body (11, 20). However, these methods are ill-suited for present-day experiments, because they require a coherent implementation of a graph coloring method, which requires additional qubits.

Notwithstanding this open challenge, we selected to demonstrate our WAVES approach on the exciton transfer between two chlorophyll units found in the light-harvesting complexes of purple bacteria.

On the basis of localized excitons on each chlorophyll unit, the exciton transfer Hamiltonian is

$$
\hat {H} = \left( \begin{array}{l l} \alpha & \beta \\ \beta & \alpha \end{array} \right) \tag {5}
$$

where  $\alpha = 1.46\mathrm{eV}$  is the energy of the exciton on one of the chlorophyll units and  $\beta = 0.037\mathrm{eV}$  is the interaction between the excitons arising from the transition dipole between the two units. The qubit representation of this two-state Hamiltonian is obtained using compact mapping (20) and is

$$
\hat {H} _ {\text {q u b i t}} = \alpha \hat {\mathcal {I}} + \beta \hat {\sigma} ^ {x} \tag {6}
$$

where  $\hat{\mathcal{I}}$  and  $\hat{\sigma}^x$  are the usual Pauli matrices in the computational basis.

The WAVES approach sequentially performs a witness-assisted variational search to find the eigenstates and a QPEA to obtain an accurate energy. At this point, we recall a well-known property of eigenfunction equations: The Hamiltonian  $\hat{H}^{\prime} = \hat{H} -\ell \hat{\mathcal{I}}$  has the same eigenstates as  $\hat{H}$  and has eigenvalues  $\lambda^{\prime} = \lambda -\ell$ , where  $\lambda$  are the eigenvalues of  $\hat{H}$  and  $\ell$  is a constant. The parameter  $\ell$  simply redefines arbitrarily the energy zero and we were free to exploit this mathematical equivalence to improve the performance of our algorithm.

In many quantum simulation applications, the natural choice of energy zero results in Hamiltonians where the total energy is orders of magnitude larger than the energy differences relevant to the phenomena under investigation. This is particularly true, for example, for reaction energies in quantum chemistry and is also the case for our excitonic Hamiltonian where we are interested in the difference between the ground and excited state  $2\beta \ll \alpha$ . Because QPEA requires a bitwise readout of the eigenvalue of each state of interest, any shift  $\ell$  that reduces the magnitude of the corresponding energy increases the precision that can be obtained with a given length in the QPEA binary expansion. In practice, a reasonable choice for  $\ell$  may be obtained, for example, from a mean-field calculation, which can be performed efficiently on a classical computer. That is, such an algorithm directly estimates the correlation energy rather than the ground-state energy. To mimic a realistic problem where mean-field theory provides a rather poor guess for the exact eigenvalues, we selected an arbitrary value of  $\ell \simeq 1.24\mathrm{eV}$  in the experiment.

The energy estimation in WAVES adopts the form  $\mathcal{E} = -\mathrm{Arg}[_{T}\langle \Psi |e^{-i\hat{H} t}|\Psi \rangle_{T}] / t$ , and this imposes restrictions on the value of  $t$  to avoid issues due to the  $2\pi$  periodicity of the Arg function. This is a limitation already known from QPEA, normally addressed by choosing  $t$  small enough to prevent the algorithm from providing any eigenvalues mod  $2\pi$  (11).

However, in the WAVES protocol, additional boundaries for  $t$  emerge from considerations about the  $\mathcal{P}$  estimator, as described in section S1.2. The span in purity within the accessible Hilbert space also dominated the choice of the evolution time  $t = 26$ . It is also easy to verify that  $26(\lambda_g - \lambda_e) \neq 0 \mod 2\pi$ ; therefore, our choice satisfies all the conditions stated for  $t$ , concerning the value of  $\mathcal{P}$  in the objective function.

# Hydrogen molecules: Mapping and ansatz

In addition to the experimental verification described, we report numerical simulations of chemical Hamiltonians using classical com

puters in section S7, which are partially shown in Fig. 4. In particular, we had simulated ground and excited electronic states of  $\mathrm{H}_2$ ,  $\mathrm{H}_3^+$ , and  $\mathrm{H}_4$  in a STO-3G basis (43) in the Jordan-Wigner representation (20) to assess the scalability of our proposal. These represent four-, six-, and eight-qubit Hamiltonians, respectively. In our investigations, we looked at two different ansatz. First, we used a PH ansatz, where we took

$$
\hat {U} (\vec {t}) = \exp \left[ i \left(\sum_ {i j} t _ {i j} \left(a _ {i} ^ {\dagger} a _ {j}\right) + \sum_ {i j k l} t _ {i j k l} \left(a _ {i} ^ {\dagger} a _ {j} ^ {\dagger} a _ {k} a _ {l}\right)\right) \right] \tag {7}
$$

and allowed variation of the terms  $t_{ij}$  and  $t_{ijkl}$  to define the ansatz. The  $a_i^\dagger$  and  $a_j$  represent creation and annihilation operators in the Hartree-Fock basis, respectively. Variation was performed after transformation to Pauli operators via the Jordan-Wigner transformation. In all cases, the reference state on which  $U(\vec{t})$  acts was taken to be the Hartree-Fock state with the correct number of particles. This is essentially a deformation of the original Hamiltonian, allowing one to preserve its symmetries and giving a natural connection to the original interaction structure of the problem. We also used an unrestricted UCC ansatz of the form

$$
\hat {U} (\vec {t}) = \exp \left[ \sum_ {i j} t _ {i j} \left(a _ {i} ^ {\dagger} a _ {j} - a _ {j} ^ {\dagger} a _ {i}\right) + \sum_ {i j k l} t _ {i j k l} \left(a _ {i} ^ {\dagger} a _ {j} a _ {k} ^ {\dagger} a _ {l} - a _ {l} ^ {\dagger} a _ {k} a _ {j} ^ {\dagger} a _ {i}\right) \right] \tag {8}
$$

The key difference between this ansatz and the previous one is that excitations between arbitrary orbitals are allowed, not just those found in the Hamiltonian. The consequence of this is that one may create or repair symmetry-broken states that have been produced by some other means, allowing additional flexibility in the description of the state at the cost of more parameters. In the following, we will refer synthetically to a parameterization of the ansatz  $\hat{A} (\theta)$ , corresponding to

$$
\hat {A} (\vec {\theta}) = \exp \left[ \left(\sum_ {i} \theta_ {i} \hat {A} _ {i}\right) t \right] \tag {9}
$$

Similarly, the approximate excitation operators used were defined in this basis as

$$
E _ {i j} = \exp \left[ \frac {\pi}{2} \left(a _ {i} ^ {\dagger} a _ {j} - a _ {j} ^ {\dagger} a _ {i}\right) \right] \tag {10}
$$

where we take  $j$  to index the occupied orbitals of the Hartree-Fock reference and  $i$  to index the occupied orbitals of the reference.

# SUPPLEMENTARY MATERIALS

Supplementary material for this article is available at http://advances.sciencemag.org/cgi/ content/full/4/1/eaap9646/DC1

section S1. Notes on the objective function

section S2. Swarm optimization algorithm

section S3. Complexity analysis of the variational protocol

section S4. Phase estimation without quantum collapse

section S5. Experimental details

section S6. Robustness against experimental noise of the variational search

section S7. Numerical simulations of hydrogen molecules

fig. S1. Median inference error in eigenvalue inference with  $\alpha = 1/2$  for a distribution with two randomly chosen eigenvalues and likelihood function (37) is used.  
fig. S2. Schematic representation of the experimental setup.  
fig. S3. Numerical simulations of the variational ground state search robustness for the bosonic one-qubit  $\hat{H}$  against gate infidelities using  $\mathcal{F}_{\mathrm{obj}}$  or  $\mathcal{E}$  alone.  
fig. S4. Synopsis of numerical simulations of excited states searches for the molecules  $\mathsf{H}_2$  and  $\mathsf{H}_3^+$ . fig. S5. Numerical simulations of the WAVES variational search for the synthetically truncated PH ansatz are studied in the molecular hydrogen systems  $(\mathsf{H}_2, \mathsf{H}_3^+, \mathsf{H}_3, \mathsf{H}_4)$ .  
fig. S6. Convergence of the WAVES algorithm to a subspace of excited states for different hydrogen systems.  
fig. S7. Comparison between different ansaetze adopted in the search for excited states in the  $\mathsf{H}_3^+$  system.  
Fig. S8. Behavior comparison of the first part of WAVES and an equivalent implementation of the FS method when applied to the initial guess provided by the  $\hat{E}_{\mathfrak{p}_3}$  excitation operator for the  $\mathrm{H}_2$  system.  
table S1. Summary of ansätze used for simulations in the main paper and in the Supplementary Materials for the various systems investigated, along with the cardinality of their parameterization, dim  $(\vec{\theta})$ .  
table S2. Summary of possible situations occurring in numerical simulations when WAVES is performed with different ansätze and excitation operators, targeting a certain excited subspace  $\mathbb{E}_{\mathrm{t}}$  from an initial guess  $|\Psi_0\rangle$ .  
References (48-56)

# REFERENCES AND NOTES

1. R. P. Feynman, Simulating physics with computers. Int. J. Theor. Phys. 21, 467-488 (1982).  
2. S. Lloyd, Universal quantum simulators. Science 273, 1073-1078 (1996).  
3. A Aspuru-Guzik, A. D. Dutoi, P. J. Love, M. Head-Gordon, Simulated quantum computation of molecular energies. Science 309, 1704-1707 (2005).  
4. I. M. Georgescu, S Ashhab, F Nori, Quantum simulation. Rev. Mod. Phys. 86, 153-185 (2014).  
5. I. Bloch, J. Dalibard, S. Nascimbène, Quantum simulations with ultracold quantum gases. Nat. Phys. 8, 267-276 (2012).  
6. R. Blatt, C. F. Roos, Quantum simulations with trapped ions. Nat. Phys. 8, 277-284 (2012).  
7. B. P. Lanyon, C. Hempel, D. Nigg, M. Müller, R. Gerritsma, F. Zähringer, P. Schindler, J. T. Barreiro, M. Rambach, G. Kirchmair, M. Hennrich, P. Zoller, R. Blatt, C. F. Roos, Universal digital quantum simulation with trapped ions. Science 334, 57-61 (2011).  
8. K. R. Brown, R. J. Clark, I. L. Chuang, Limitations of quantum simulation examined by simulating a pairing Hamiltonian using nuclear magnetic resonance. Phys. Rev. Lett. 97, 050504 (2006).  
9. J. Du, N. Xu, X. Peng, P. Wang, S. Wu, D. Lu, NMR implementation of a molecular hydrogen quantum simulation with adiabatic state preparation. Phys. Rev. Lett. 104, 030502 (2010).  
10. P. J. J. O'Malley, R. Babbush, I. D. Kivlichan, J. Romero, J. R. McClean, R. Barends, J. Kelly, P. Roushan, A. Tranter, N. Ding, B. Campbell, Y. Chen, Z. Chen, B. Chiaro, A. Dunsworth, A. G. Fowler, E. Jeffrey, E. Lucero, A. Megrant, J. Y. Mutus, M. Neeley, C. Neill, C. Quintana, D. Sank, A. Vainsencher, J. Wenner, T. C. White, P. V. Coveney, P. J. Love, H. Neven, A. Aspiru-Guzik, J. M. Martinis, Scalable quantum simulation of molecular energies. Phys. Rev. X 6, 031007 (2016).  
11. B. P. Lanyon, J. D. Whitfield, G. G. Gillett, M. E. Goggin, M. P. Almeida, I. Kassal, J. D. Biamonte, M. Mohseni, B. J. Powell, M. Barbieri, A. Aspuru-Guzik, A. G. White, Towards quantum chemistry on a quantum computer. Nat. Chem. 2, 106-111 (2010).  
12. A. Peruzzo, J. McClean, P. Shadbolt, M.-H. Yung, X.-Q. Zhou, P. J. Love, A. Aspiru-Guzik, J. L. O'Brien, A variational eigenvalue solver on a photonic quantum processor. Nat. Commun. 5, 4213 (2014).  
13. I. Pitsios, L. Banchi, A. S. Rab, M. Bentivegna, D. Caprara, A. Crespi, N. Spagnolo, S. Bose, P. Mataloni, R. Osellame, F. Sciarrino, Photonic simulation of entanglement growth and engineering after a spin chain quench. Nat. Commun. 8, 1569 (2017).  
14. A. Kandala, A. Mezzacapo, K. Temme, M. Takita, M. Brink, J. M. Chow, J. M. Gambetta, Hardware-efficient variational quantum eigensolver for small molecules and quantum magnets. Nature 549, 242-246 (2017).  
15. M. H. M. Olsson, J. Mavri, A. Warshel, Transition state theory can be used in studies of enzyme catalysis: Lessons from simulations of tunnelling and dynamical effects in lipoxygenase and other systems. Philos. Trans. R. Soc. Lond. B Biol. Sci. 361, 1417-1432 (2006).  
16. D. Lidar, H. Wang, Calculating the thermal rate constant with exponential speedup on a quantum computer. Phys. Rev. E 59, 2429-2438 (1999).  
17. L. Serrano-Andrés, M. Merchán, Quantum chemistry of the excited state: 2005 overview. J. Mol. Struct. THEOCHEM. 729, 99-108 (2005).  
18. T. D. Crawford, J. F. Stanton, Some surprising failures of Brueckner coupled cluster theory. J. Chem. Phys. 112, 7873-7879 (2000).  
19. M. Dobšićek, G. Johansson, V. Shumeiko, G. Wendin, Arbitrary accuracy iterative quantum phase estimation algorithm using a single ancillary qubit: A two-qubit benchmark. Phys. Rev. A 76, 030306 (2007).

20. J. R. McClean, J. Romero, R. Babbush, A. Aspuru-Guzik, The theory of variational hybrid quantum-classical algorithms. New J. Phys. 18, 023023 (2016).  
21. J. Romero, R. Babbush, J. R. McClean, C. Hempel, Strategies for quantum computing molecular energies using the unitary coupled cluster ansatz. https://arxiv.org/abs/1701.02691 (2017).  
22. G. G. Guerreschi, M. Smelyanskiy, Practical optimization for hybrid quantum-classical algorithms. https://arxiv.org/abs/1701.01450 (2017).  
23. Y. Li, S. C. Benjamin, Efficient variational quantum simulator incorporating active error minimization. Phys. Rev. X 7, 021050 (2017).  
24. D. Wecker, M. B. Hastings, M. Troyer, Progress towards practical quantum variational algorithms. Phys. Rev. A 92, 042303 (2015).  
25. J. R. McClean, M. E. Kimchi-Schwartz, J. Carter, W. A. de Jong, Hybrid quantum-classical hierarchy for mitigation of decoherence and determination of excited states. Phys. Rev. A 95, 042308 (2017).  
26. J. I. Colless, V. V. Ramasesh, D. Dahlen, M. S. Blok, J. R. McClean, J. Carter, W. A. de Jong, I. Siddiqi, Robust determination of molecular spectra on a quantum processor. https://arxiv.org/abs/1707.06408 (2017).  
27. J. E. Sharping, K. F. Lee, M. A. Foster, A. C. Turner, B. S. Schmidt, M. Lipson, A. L. Gaeta, Generation of correlated photons in nanoscale silicon waveguides. Opt. Express 14, 12388-12393 (2006).  
28. R. Santagati, J. W. Silverstone, M. J. Strain, M. Sorel, S. Miki, T. Yamashita, M. Fujiwara, M. Sasaki, H. Terai, M. G. Tanner, C. M. Natarajan, R. H. Hadfield, J. L. O'Brien, M. G. Thompson, Silicon photonic processor of two-qubit entangling quantum logic. J. Opt. 19, 114006 (2017).  
29. J. W. Silverstone, R. Santagati, D. Bonneau, M. J. Strain, M. Sorel, J. L. O'Brien, M. G. Thompson, Qubit entanglement between ring-resonator photon-pair sources on a silicon chip. Nat. Commun. 6, 7948 (2015).  
30. L. Sansoni, F. Sciarino, G. Vallone, P. Mataloni, A. Crespi, R. Ramponi, R. Osellame, Polarization entangled state measurement on a chip. Phys. Rev. Lett. 105, 200503 (2010).  
31. J. Wang, D. Bonneau, M. Villa, J. W. Silverstone, R. Santagati, S. Miki, T. Yamashita, M. Fujiwara, M. Sasaki, H. Terai, M. G. Tanner, C. M. Natarajan, R. H. Hadfield, J. L. O'Brien, M. G. Thompson, Chip-to-chip quantum photonic interconnect by path-polarization interconversion. Optica 3, 407-413 (2016).  
32. X.-Q. Zhou, T. C. Ralph, P. Kalasuwan, M. Zhang, A. Peruzzo, B. P. Lanyon, J. L. O'Brien, Adding control to arbitrary unknown quantum operations. Nat. Commun. 2, 413 (2011).  
33. R. B. Patel, J. Ho, F. Ferreyrol, T. C. Ralph, G. J. Pryde, A quantum Fredkin gate. Sci. Adv. 2, 1501531 (2016).  
34. Z. Li, M.-H. Yung, H. Chen, D. Lu, J. D. Whitfield, X. Peng, A. Aspiru-Guzik, J. Du, Solving quantum ground-state problems with nuclear magnetic resonance. Sci. Rep. 1, 88 (2011).  
35. G. Carleo, M. Troyer, Solving the quantum many-body problem with artificial neural networks. Science 355, 602-606 (2017).  
36. A. Beskos, D. Crisan, A. Jasra, On the stability of sequential Monte Carlo methods in high dimensions. Ann. Appl. Probab. 24, 1396-1445 (2014).  
37. M. Reiher, N Wiebe, K. M. Svore, D. Wecker, M. Troyer, Elucidating reaction mechanisms on quantum computers. Proc. Natl. Acad. Sci. U.S.A. 114, 7555-7560 (2017).  
38. D. Poulin, M. B. Hastings, D. Wecker, N. Wiebe, A. C. Doherty, M. Troyer, The trotter step size required for accurate quantum simulation of quantum chemistry. Quantum Inf. Comput. 15, 361-384 (2015).  
39. T. Helgaker, P. Jorgensen, J. Olsen, Molecular Electronic structure Theory (John Wiley & Sons, 2014).  
40. S Paesani, A. A. Gentile, R. Santagati, J. Wang, N. Wiebe, D. P. Tew, J. L. O'Brien, M. G. Thompson, Experimental Bayesian quantum phase estimation on a silicon photonic chip. Phys. Rev. Lett. 118, 100503 (2017).  
41. J. Wang, S. Paesani, R. Santagati, S. Knauer, A. A. Gentile, N. Wiebe, M. Petruzella, J. L. O'Brien, J. G. Rarity, A. Laing, M. G. Thompson, Experimental quantum Hamiltonian learning. Nat. Phys. 13, 551-555 (2017).  
42. R. J. Cogdell, A. Gall, J. Kohler, The architecture and function of the light-harvesting apparatus of purple bacteria: From single molecules to in vivo membranes. Q. Rev. Biophys. 39, 227-324 (2006).  
43. W. J. Hehre, R. F. Stewart, J. A. Pople, Self-consistent molecular-orbital methods. I. Use of Gaussian expansions of Slater-type atomic orbitals. J. Chem. Phys. 51, 2657-2664 (1969).  
44. J. Kempe, A. Kitaev, O. Regev, The complexity of the local Hamiltonian problem. SIAM J. Comput. 35, 1070-1097 (2006).  
45. T. Watermann, A. Scherrer, D. Sebastiani, Linear response methods in quantum chemistry, in Manyelectron Approaches in Physics, Chemistry and Mathematics, V. Bach, L. Delle Site, Eds. (Springer, 2014), p. 97.  
46. C. Møller, M. S. Plesset, Note on an approximation treatment for many-electron systems. Phys. Rev. 46, 618-622 (1934).  
47. P.-O. Löwdin, H. Shull, Natural orbitals in the quantum theory of two-electron systems. Phys. Rev. 101, 1730-1739 (1956).

48. R. Babbush, J. McClean, D. Wecker, A. Aspuru-Guzik, N. Wiebe, Chemical basis of Trotter-Suzuki errors in quantum chemistry simulation. Phys. Rev. A 91, 022311 (2015).  
49. N. Wiebe, D. Berry, P. Hoeyer, B. C. Sanders, Higher order decompositions of ordered operator exponentials. J. Phys. A Math. Theor. 43, 065203 (2010).  
50. V. Kliuchnikov, D. Maslov, M. Mosca, Fast and efficient exact synthesis of single qubit unitaries generated by Clifford and T gates. Quantum Inf. Comput. 13, 0607-0630 (2013).  
51. R. Babbush, D. W. Berry, I. D. Kivlichan, A. Y. Wei, P. J. Love, A. Aspuru-Guzik, Exponentially more precise quantum simulation of fermions in second quantization. New J. Phys. 18, 033032 (2016).  
52. S. Aaronson, Computational complexity: Why quantum chemistry is hard. Nat. Phys. 5, 707-708 (2009).  
53. Q Lin, G. P. Agrawal, Silicon waveguides for creating quantum-correlated photon pairs. Opt. Lett. 31, 3140-3142 (2006).  
54. U. Las Heras, U. Alvarez-Rodriguez, E. Solano, M. Sanz, Genetic algorithms for digital quantum simulations. Phys. Rev. Lett. 116, 230504 (2016).  
55. L.-W. Wang, A. Zunger, Solving Schrödinger's equation around a desired energy: Application to silicon quantum dots. J. Chem. Phys. 100, 2394-2397 (1994).  
56. A. R. Tackett, M. Di Ventra, Targeting specific eigenvectors and eigenvalues of a given Hamiltonian using arbitrary selection criteria. Phys. Rev. B 66, 245104 (2002).

Acknowledgments: We thank G. Marshall, C. Sparrow, A. Montanaro, A. Laing, E. Johnston, and J. Barreto for useful discussion and feedback. We thank A. Murray and M. Loutit for experimental support. We thank K. Ohira, N. Suzuki, H. Yoshida, N. Iizuka, and M. Ezaki for the device fabrication. We thank S. Miki, T. Yamashita, M. Fujiwara, M. Sasaki, H. Terai, M. G. Tanner, C. M. Natarajan, and R. H. Hadfield for the Superconducting Nanowire Single Photon Detectors (SNSPDs) used for part of the characterization of the device. Funding: This work was supported by the UK Engineering and Physical Sciences Research Council (EPSRC; grant nos. K033085/1, J017175/1, and K02193/1). We acknowledge support from the European Research Council (grant nos. 648667, 608062, 641039, and 640079). J.R.M. was supported by the Luis W. Alvarez fellowship in computing sciences and by the Laboratory

Directed Research and Development funding from Berkeley Laboratory provided by the Director of the Office of Science of the U.S. Department of Energy under contract no. DE-AC02-05CH11231. S.M.-S. was supported by the Bristol Quantum Engineering Centre for Doctoral Training, EPSRC grant EP/L015730/1. X.Z. acknowledges support from the National Key Research and Development Program (grant nos. 2016YFA0301700 and 2017YFA0305200), the National Young 1000 Talents Plan, and the Natural Science Foundation of Guangdong (2016A030312012). J.L.O. acknowledges a Royal Society Wolfson Merit Award and a Royal Academy of Engineering Chair in Emerging Technologies. P.J.S. was supported by the Army Research Office grant no. W911NF-14-013. D.P.T. thanks the Royal Society for a University Research Fellowship (UF130574). Author contributions: R.S., J.W., A.A.G., S.P., N.W., J.R.M., and X.Z. developed the algorithm. R.S., J.W., D.B., X.Z., and M.G.T. designed the experiment. R.S., A.A.G., N.W., and J.R.M. performed simulations. R.S., J.W., A.A.G., S.P., P.J.S., and J.W.S. performed the experiment, with theoretical support from N.W., J.R.M., S.M.-S., and D.P.T. N.W. developed the theorems and their proofs. R.S., J.W., A.A.G., S.P., N.W., and J.R.M. wrote the manuscript with feedback from all authors. J.L.O. and M.G.T. supervised the project. Competing interests: The authors declare that they have no competing interests. Data and materials availability: All experimental data are accessible at 10.6084/m9.figshare.5605456, whereas the simulation data are accessible at 10.6084/m9.figshare.5605465. All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to this paper may be requested from the authors.

Submitted 19 September 2017

Accepted 27 December 2017

Published 26 January 2018

10.1126/sciadv.aap9646

Citation: R. Santagati, J. Wang, A. A. Gentile, S. Paesani, N. Wiebe, J. R. McClean, S. Morley-Short, P. J. Shadbolt, D. Bonneau, J. W. Silverstone, D. P. Tew, X. Zhou, J. L. O'Brien, M. G. Thompson, Witnessing eigenstates for quantum simulation of Hamiltonian spectra. Sci. Adv. 4, eaap9646 (2018).

# Science Advances

# Witnessing eigenstates for quantum simulation of Hamiltonian spectra

Raffaele Santagati, Jianwei Wang, Antonio A. Gentile, Stefano Paesani, Nathan Wiebe, Jarrod R. McClean, Sam Morley-Short, Peter J. Shadbolt, Damien Bonneau, Joshua W. Silverstone, David P. Tew, Xiaqi Zhou, Jeremy L. O'Brien and Mark G. Thompson

Sci Adv 4 (1), eaap9646. DOI: 10.1126/sciadv.aap9646

ARTICLE TOOLS

http://advances.sciencemag.org/content/4/1/eaap9646

SUPPLEMENTARY MATERIALS

http://advances.sciencemag.org/content/suppl/2018/01/22/4.1.eaap9646.DC1

REFERENCES

This article cites 51 articles, 6 of which you can access for free http://advances.sciencemag.org/content/4/1/eaap9646#BIBL

PERMISSIONS

http://www.sciencemag.org/help/reprints-and-permissions

Use of this article is subject to the Terms of Service