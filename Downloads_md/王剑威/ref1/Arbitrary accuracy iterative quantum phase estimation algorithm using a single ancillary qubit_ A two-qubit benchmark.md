# Arbitrary accuracy iterative quantum phase estimation algorithm using a single ancillary qubit: A two-qubit benchmark

Miroslav Dobšićek, $^{1,2}$  Göran Johansson, $^{1}$  Vitaly Shumeiko, $^{1}$  and Göran Wendl $^{1}$

<sup>1</sup>Microtechnology and Nanoscience, MC2, Chalmers, S-412 96 Göteborg, Sweden

$^{2}$ Department of Computer Science and Engineering, FEE CTU, 121 35 Prague, Czech Republic

(Received 12 July 2007; published 19 September 2007)

We discuss the implementation of an iterative quantum phase estimation algorithm with a single ancillary qubit. We suggest using this algorithm as a benchmark for multiqubit implementations. Furthermore, we describe in detail the smallest possible realization, using only two qubits, and exemplify with a superconducting circuit. We discuss the robustness of the algorithm in the presence of gate errors, and show that seven bits of precision is obtainable, even with very limited gate accuracies.

DOI: 10.1103/PhysRevA.76.030306

PACS number(s): 03.67.Lx, 85.25.Cp

Solid-state quantum computing is now entering the stage of exploration of multiqubit circuits. Coherent two-qubit coupling has been experimentally realized for all major types of superconducting qubits [1-10], and tunable coupling has been realized for flux qubits [11,12]. Two-qubit gates have been demonstrated for charge [7], phase [8,9], and flux qubits [10]. The question then arises, what kind of testbed application can be performed having at hand a very limited amount of qubits?

Here we propose to employ the phase estimation algorithm (PEA), which can be implemented with just two qubits. Furthermore, we suggest how to use this algorithm to characterize (benchmark) qubit circuits. The PEA is an algorithm to determine the eigenvalue of a unitary operator  $\hat{U}$ ; it is closely related to the quantum Fourier transform (QFT), which is a key element of many quantum algorithms, e.g., Shor's factoring algorithm [13] and in general an Abelian stabilizer type of problem [14]. The algorithm's relevance for quantum simulations was noticed by Abrams and Lloyd [15] and recently emphasized by Aspuru-Guzik et al. [16] simulating quantum computation of the lowest energy eigenvalue of several small molecules. It is clear that the PEA will be one of the important algorithms in future quantum information processing applications, and how accurately a phase can be determined will be an important figure of merit for any implementation.

The textbook [17] implementation of this algorithm requires  $n$  qubits representing the physical system in which  $\hat{U}$  operates, and  $m$  ancillary qubits for the work register. The number  $m$  determines the algorithm's precision  $1/2^{m}$ , i.e., the number of accurate binary digits extracted. There is also an alternative algorithm proposed by Kitaev [14], where the Fourier transform is replaced with a Hadamard transform. In implementing this algorithm to obtain a precision of order  $1/2^{m}$ , it is possible to run either  $\log m$  rounds (iterations) with  $m$  ancillary qubits or  $m\log(m)$  rounds with only a single ancilla. The precision increases exponentially with the number of rounds, but each round requires exponentially many applications of  $\hat{U}$ , unless powers  $U^{2^k}$  are available by different means [18].

Also the QFT-based PEA can be implemented in a multiround fashion, using a single ancillary qubit, based on the semiclassical QFT [19]. In this Rapid Communication, we

refer to this single ancilla QFT based PEA as iterative PEA (IPEA). The iterative version of Kitaev's algorithm is referred to as Kitaev's PEA. The relevance of the IPEA as a viable alternative to the textbook version was noticed by Mosca and Ekert [20] in the context of the hidden subgroup problem, by Zalka [21] for factoring, and by Childs et al. [22] and Knill et al. [23] in more physical contexts.

As long as the number of qubits is a limiting factor, implementations of phase estimation with only a single ancillary qubit will be of foremost importance. Thus it is instructive to compare the iterative PEA with Kitaev's PEA. In the IPEA scheme, the bits of the phase are measured directly, without any need for classical postprocessing. Moreover, each bit has to be measured only once, compared to  $\log(m)$  times. When the phase  $\phi$  has a binary expansion with no more than  $m$  bits, the IPEA deterministically extracts all bits, in contrast to Kitaev's PEA which is always probabilistic. The IPEA is also optimal in the sense that a full bit of information is gained in each measurement [24].

Theoretically the accuracy of the algorithm is limited only by the number of rounds, but in practice it will be limited by experimental imperfections. Thus the experimentally maximally obtainable accuracy can serve as a benchmark for any multiqubit implementation.

For benchmarking purposes a setup is needed where the phase to be measured can be set to an arbitrary value. We describe in detail such an implementation in a system of two superconducting qubits. Introducing gate noise, we also perform a robustness analysis, indicating which gates are most critical, and we calculate the number of repetitions needed as a function of noise levels.

Iterative PEA. We now describe the IPEA briefly, but still in some detail, in order to make the robustness analysis clear. The most straightforward approach for phase estimation is shown in Fig. 1. The upper line is the ancillary qubit which is measured, and the lower line describes the qubits representing the physical system in which  $\hat{U}$  operates. Initially the

![](images/e3c903a0ece658f825bf622fef1729cbf52a8ba8ad01e02e4ace323b96e42393.jpg)  
FIG. 1. The naive phase estimation algorithm.

![](images/de30b111ab1cf7cf928a0f55d326b9bf7700e64d7927206fbea1fd20c6756f0c.jpg)  
FIG. 2. The  $k$ th iteration of the iterative PEA. The feedback angle  $\omega_{k}$  depends on the previously measured bits (see text).

ancillary qubit is set to  $|0\rangle$  and the lower line register to an eigenstate  $|\Psi \rangle$  of the operator  $\hat{U}$  with eigenvalue  $e^{i2\pi \phi}$ . Right before the measurement the system state is  $\frac{1}{2} [(1 + e^{i2\pi \phi})|0\rangle +(1 - e^{i2\pi \phi})|1\rangle ]|\Psi \rangle$ , giving the probability  $P_0 = \cos^2 (\pi \phi)$  to measure "0." By repeating this procedure  $N$  times,  $P_0$  can be determined to an accuracy of  $1 / \sqrt{N}$ . Thus one needs to go through at least  $N\sim 2^{2m}$  independent rounds to obtain  $m$  accurate binary digits of  $\phi$ . The number of rounds corresponds to the number of measurements since each round is terminated with a measurement.

Kitaev's PEA allows the number of rounds and consequently the number of measurements to be drastically reduced, with the assumption that the controlled-  $\hat{U}^{2^k}$  gates are available [14]. For each  $k$ ,  $1 \leqslant k \leqslant m$ , the controlled- $\hat{U}^{2^{k-1}}$  gate is used to prepare an ancillary qubit in the state  $\frac{1}{\sqrt{2}} (|0\rangle + e^{i2\pi (2^{k-1}\phi)} |1\rangle)$ . After a number of repetitions, the ratio of resulting zeros and ones is used as an estimate for the fractional part of  $2^{k-1}\phi$ . A classical algorithm with polynomial runtime is then used to assemble  $\phi$  from the fractional parts.

The IPEA differs by the following modification of the above-described procedure: first less significant digits are evaluated and then the obtained information improves the quantum part of the search for more significant digits. The information is transferred through a single qubit  $Z$  rotation, as shown in Fig. 2. Note that  $k$  is iterated backwards from  $m$  to 1.

In order to derive the success probability for each bit being determined correctly, we first assume the phase  $\phi$  to have a binary expansion with no more than  $m$  bits,  $\phi = (0.\phi_1\phi_2\dots \phi_m000\dots)$ . In the first iteration  $(k = m)$  a controlled- $\hat{U}^{2^{m - 1}}$  gate is applied, and the  $m$ th bit of the expansion is measured. The probability to measure "0" is  $P_{0} = \cos^{2}[\pi (0.\phi_{m}00\dots)]$ , which is unity for  $\phi_{m} = 0$  and zero for  $\phi_{m} = 1$ . Thus the first bit  $\phi_{m}$  is extracted deterministically. In the second iteration  $(k = m - 1)$  the measurement is performed on the  $(m - 1)$ th bit. The phase of the first qubit before the  $Z$  rotation is  $2\pi (0.\phi_{m - 1}\phi_{m}00\dots)$ , and performing a  $Z$  rotation with angle  $\omega_{m - 1} = -2\pi (0.0\phi_{m})$ , the measurement probability becomes  $P_{0} = \cos^{2}[\pi (0.\phi_{m - 1}00\dots)]$ . Thus using feedback the second bit is also measured deterministically, and generally using the feedback angle  $\omega_{k} = -2\pi (0.0\phi_{k + 1}\phi_{k + 2}\dots \phi_{m})$  all  $m$  bits of  $\phi$  are extracted deterministically.

Denoting the first  $m$  bits of the binary expansion of the phase  $\phi$  as  $\widetilde{\phi} = 0$ .  $\phi_1\phi_2\dots \phi_m$ , there is in general a remainder  $0\leqslant \delta < 1$ , defined by  $\phi = \widetilde{\phi} +\delta 2^{-m}$ . In this case, the probability to measure  $\phi_{m}$  is  $\cos^2 (\pi \delta /2)$ . If  $\phi_{m}$  was measured correctly, the probability to measure  $\phi_{m - 1}$  in the second iteration is  $\cos^2 (\pi \delta /4)$ , and so on. Thus the conditional probability  $P_{k}$  for each bit to be measured correctly is  $P_{k} = \cos^{2}(\pi 2^{k - m - 1}\delta)$

and the overall probability for the algorithm to extract  $\tilde{\phi}$  is

$$
P (\delta) = \prod_ {k = 1} ^ {m} P _ {k} = \frac {\sin^ {2} (\pi \delta)}{2 ^ {2 m} \sin^ {2} (\pi 2 ^ {- m} \delta)}, \tag {1}
$$

which is the same outcome probability as the textbook phase estimation, based on the QFT [17]. For  $\delta \leqslant 1 / 2$  the best  $m$ -bit approximation to  $\phi$  is indeed  $\tilde{\phi}$ , while for  $\delta > 1 / 2$  rounding up to  $\tilde{\phi} + 2^{-m}$  is better. The probability to extract  $\tilde{\phi} + 2^{-m}$  is  $P(1 - \delta)$ . The success probability  $P(\delta)$  decreases monotonically for increasing  $m$ . In the limit  $m \to \infty$ , the lower bound for the probability to extract the best rounded approximation to  $\phi$  is  $P(1 / 2) = 4 / \pi^2$ . An accuracy of  $1 / 2^{m}$  implies accepting both answers  $\tilde{\phi}$  and  $\tilde{\phi} + 2^{-m}$ . Thus the iterative PEA determines the phase with accuracy  $1 / 2^{m}$  and with an error probability  $\varepsilon < 1 - 8 / \pi^2$ , which is independent of  $m$ .

Success probability amplification can be performed by extracting  $m' = m + \log(2 + 1/2\varepsilon)$  bits. The estimate is then accurate to  $m$  bits, with probability at least  $1 - \varepsilon$ . However, implementing the  $\hat{U}^{2^k}$  gate for large  $k$  is the algorithm's bottleneck in a realistically noisy environment, as discussed below. A different approach, which avoids implementing  $\hat{U}^{2^k}$  for  $k > m$ , is to repeat the whole algorithm a number of times, choosing the most frequent result. In natural ensemble systems, such as NMR, this is exploited with advantage [25]. For single systems such as superconducting qubits, it is better to use bitwise repetitions. For large  $m$ , the bare bitwise error probability  $\sin^2(\pi 2^{k-m-1}\delta)$  decreases exponentially with decreasing  $k$ . Using majority voting, the effective error probability decreases exponentially with the number of repetitions, according to the binomial distribution. Thus repeating the iterations for the  $O(\log(1/\varepsilon))$  least significant bits an  $O(\log(1/\varepsilon))$  number of times gives an error probability smaller than  $\varepsilon$ , independently of  $m$ .

Benchmark circuit. The minimal system for implementing the iterative PEA is a two-qubit system, where one qubit is a read-out ancilla, and the second qubit represents a physical system. From the work of Barenco et al. [26] we know an explicit construction of any controlled- $\hat{U}$  gate, where  $\hat{U}$  is an arbitrary single-qubit gate. This construct involves three single-qubit gates and two controlled-NOT (CNOT) gates.

For benchmarking purposes we propose to use the very simple  $Z$ -rotation operator

$$
\hat {U} = \left( \begin{array}{c c} e ^ {- i \alpha} & 0 \\ 0 & e ^ {i \alpha} \end{array} \right), \tag {2}
$$

where  $\alpha$  is an arbitrary rotation angle. The advantages of this operator are (1) it is diagonal in the qubit eigenbasis, thus the initial preparation of its eigenstate is straightforward, (2) the phase to be measured is controlled directly, and (3) controlled powers of this gate are generated by a single entangling gate,  $ZZ(\alpha) = \mathrm{diag}(e^{-i\alpha}, e^{i\alpha}, e^{i\alpha}, e^{-i\alpha})$ ; this gate can be straightforwardly implemented by using the most common superconducting qubit coupling schemes. As shown in Fig. 3, a step of the iterative PEA is implemented using one ZZ gate, and in addition only three single-qubit gates. The phase we

![](images/9cadf566db07647bfd05221bb220fc5107bd756e2433a35902fb7f764339b31c.jpg)  
FIG. 3. The  $k$ th step of the iterative PEA, implemented on a two-qubit system using the entangling gate  $ZZ(\alpha)$ .

are measuring in this case is set by the coupling strength  $\lambda$ , rather than by the free qubit energy that is the case using the general construction with two CNOT gates,  $\alpha 2^{k} = \lambda T$ ,  $T$  is the pulse duration.

Let us consider implementation of the ZZ gate with superconducting qubits in more detail. For superconducting charge and charge-phase qubits operated at the charge degeneracy point, and physically connected via a Josephson junction placed at the intersection of the qubit loop-shaped electrodes, inductive interaction of persistent currents circulating in the loops creates direct switchable  $zz$  coupling [27-29]. Thus the implementation of the ZZ gate is straightforward.

Furthermore, the ZZ gate is a generic gate for the qubits coupled via a tunable linear oscillator: this gate is generated by applying a composite dc pulse sweeping through the qubit-cavity resonances as shown in [30].

For the permanent transverse coupling (xx coupling in the qubit eigenbasis) frequently discussed in the context of charge [6], phase [8], and flux [31] qubits, the ZZ gate can be realized with dynamic control schemes [31,32]. The parametric coupling method [31] was recently experimentally verified [12] and suggests harmonic modulation of the coupling strength  $\lambda(t)$  with the two resonant frequencies corresponding to the sum and the difference of the qubit energies. This induces the Rabi rotations  $U_R^P$  and  $U_R^S$  in the parallel spin  $(|00\rangle, |11\rangle)$ , and antiparallel spin  $(|01\rangle, |10\rangle)$  subspaces, respectively. The ZZ gate is then obtained, up to a single qubit  $Z$  rotation, by applying the Hadamard gates to both the qubits,  $H = H_1 \otimes H_2$ , according to the scheme,  $ZZ(\alpha) = H[U_R^P(\alpha) \oplus U_R^A(\alpha)]H$ .

The method [32] is similar although more time-consuming. In this case, the resonant rf pulses are simultaneously applied to both the qubits, inducing Rabi rotations  $U_{R}$ . The pulse amplitudes are set equal to the half difference between the qubit energies. Such an operation produces the gate which is equivalent to the rotation in the  $|00\rangle ,|11\rangle$  subspace,  $U_{R}(\alpha) = HU_{R}^{P}(\alpha /4)H$ . Rotation in the  $|01\rangle ,|10\rangle$  subspace can be performed by first swapping the states of one of the qubits, and then applying the same pulse,  $U_{R}^{S}(\alpha /4) = X_{1}HU_{R}(\alpha)HX_{1}$ . Thus the ZZ gate is achieved applying the Rabi pulses twice, the full operation sequence taking the form  $ZZ(\alpha) = U_{R}(4\alpha)Z_{1}U_{R}(4\alpha)Z_{1}$ .

Robustness analysis. There are numerous imaginable sources of error, in all parts of the algorithm from initialization via gate manipulation to readout. With our setup initialization will probably be accurate, but the gates will certainly suffer from imperfections due to environmental noise. First we consider the effect of pure dephasing in the computational basis, with rate  $\Gamma_{\varphi}$ . This is an unavoidable effect of the weak interaction with the dissipative elements of the control circuitry [28] and will eventually limit the accuracy of the  $ZZ(\alpha 2^{k})$  gate. In addition, we consider imperfect  $x$  rotations of the form  $R_{x}(\pm \pi /2 + \delta_{x})$ , where  $\delta_{x}$  is a normally distributed

![](images/83704eec68113ac05b554d3a8db037fefd701edc61198ca6ce6d7e1468fc76e0.jpg)  
FIG. 4. (Color online) The success probability of the IPEA to correctly determine the phase  $\alpha$ , with precision better than  $2^{-5}$  (upper/green line) and  $2^{-7}$  (lower/blue line) as a function of the noise level. The three cases of pure  $X$ -gate errors (dotted line), pure dephasing (dashed line), and both types of noise acting simultaneously (full line) are considered. The simulation was averaged over  $\alpha$  evenly distributed in the range  $-\pi \leqslant \alpha < \pi$ .

random angle with variance  $\Delta_{x}$ . These errors modify the probability of measuring the correct value of the  $k$ th bit into

$$
P _ {k} ^ {\prime} = \frac {1}{2} [ 1 + e ^ {- \Delta_ {x} ^ {2} - | \alpha | 2 ^ {k} \Gamma_ {\varphi / \Lambda}} \cos (\pi 2 ^ {k - m} \delta) ]. \tag {3}
$$

In Fig. 4 the algorithm's success probability, as a function of the dephasing rate and variance  $\Delta_{x}$ , is shown for  $m = 5$  and 7. The algorithm is rather robust against  $x$ -rotation errors, while being much more sensitive to dephasing, which is evident from the exponentially growing factor  $2^{k}\alpha$  in the exponent of Eq. (3).

As discussed below Eq. (1), the success probability can be improved by repeated measurements of each bit. To achieve an overall success probability of  $1 - \varepsilon$ , we need to increase the per bit success probability to  $(1 - \varepsilon / m)$ , using  $N_{k}$  repeated measurements. For  $P_{k}^{\prime}$  close to  $1 / 2$ , many repetitions are needed, and the binomial distribution approaches the normal distribution giving

![](images/c76089ba86f19e2d37c2aa218b612dab3701bbb100342e6fa5635097faf441be.jpg)  
FIG. 5. (Color online) The total number of measurements needed to obtain the phase  $\alpha$  with precision better than  $2^{-m}$  ( $2 \leqslant m \leqslant 11$ ), with an error probability  $\varepsilon < 0.05$ .

$$
N _ {k} = \frac {1}{8} \left(\frac {\operatorname {e r f} ^ {- 1} \left(1 - \frac {2 \varepsilon}{m}\right)}{P _ {k} ^ {\prime} - \frac {1}{2}}\right) ^ {2}, \tag {4}
$$

where  $\mathrm{erf}^{-1}$  is the inverse of the error function. Considering the dominating effect of dephasing, we find that the number of repetitions grows quickly with the desired number of bits  $m$ ,  $N_{k} \propto e^{2|\alpha|2^{m}\Gamma_{\varphi}/\lambda}$ . In Fig. 5 we plot the total number of measurements  $N_{tot} = \Sigma_{k}N_{k}$  needed to obtain  $2 \leqslant m \leqslant 11$  bits of the phase  $\alpha$ , with an error probability  $\varepsilon < 0.05$ . For a realistic dephasing rate of  $1\% - 10\%$  percent of the qubit-qubit coupling  $(0.01 < \Gamma_{\varphi}/\lambda < 0.1)$ , between 5 and 8 binary digits of  $\alpha$  can be extracted with less than  $10^{4}$  measurements.

In experiments on superconducting qubits, the environ

ment can often be modeled using sets of bistable fluctuators [33]. An analysis of how the non-Markovian effects from such an environment influences the phase estimation algorithm would be a natural extension to the present analysis.

In conclusion, we have described a benchmark implementation of the iterative PEA on two superconducting qubits and analyzed its robustness towards dephasing and gate errors. The number of extractable binary digits is mainly limited by the dephasing, and for realistic parameters amounts to 5-8. We believe phase estimation will be an essential part of future applications of quantum computing and propose that the number of accurate binary digits can be used as a benchmark for multiqubit implementations.

This work was supported by the European Commission through the IST-015708 EuroSQIP integrated project and by the Swedish Research Council.

[1] J. B. Majer, F. G. Paauw, A. C. J. ter Haar, C. J. P. M. Har-mans, and J. E. Mooij, Phys. Rev. Lett. 94, 090501 (2005).  
[2] H. Xu et al., Phys. Rev. Lett. 94, 027003 (2005).  
[3] A. C. J. ter Haar, Ph.D. thesis, Delft University, 2005 (unpublished).  
[4] M. Grajcar et al., Phys. Rev. Lett. 96, 047006 (2006).  
[5] A. O. Niskanen, K. Harrabi, F. Yoshihara, Y. Nakamura, and J. S. Tsai, Phys. Rev. B 74, 220503(R) (2006).  
[6] Yu. A. Pashkin, T. Yamamoto, O. Astafiev, Y. Nakamura, D. V. Averin, and J. S. Tsai, Nature (London) 421, 823 (2003).  
[7] T. Yamamoto, Yu. Pashkin, O. Astafiev, Y. Nakamura, and J. S. Tsai, Nature (London) 425, 941 (2003).  
[8] R. McDermott et al., Science 307, 1299 (2005).  
[9] M. Steffen et al., Science 313, 1423 (2006).  
[10] J. Plantenberg, P. C. de Groot, C. J. P. M. Harmans, and J. E. Mooij, Nature (London) 447, 836 (2007).  
[11] T. Hime et al., Science 314, 1427 (2006); S. H. W. van der Ploeg et al., Phys. Rev. Lett. 98, 057004 (2007); R. Harris et al., ibid. 98, 177001 (2007).  
[12] A. O. Niskanen, K. Harrabi, F. Yoshihara, Y. Nakamura, and J. S. Tsai, Science 316, 723 (2007).  
[13] P. W. Shor, SIAM J. Comput. 26, 1484 (1997).  
[14] A. Yu. Kitaev, Electron. Coll. Comput. Complex. 3 (1996).  
[15] D. S. Abrams and S. Lloyd, Phys. Rev. Lett. 83, 5162 (1999).  
[16] Alán Aspuru-Guzik et al., Science 309, 1704 (2005).  
[17] R. Cleve, A. Ekert, C. Macchiavello, and M. Mosca, Proc. R. Soc. London, Ser. A 454, 339 (1998); Michael A. Nielsen and Isaac L. Chuang, Quantum Computation and Quantum Information (Cambridge University Press, Cambridge, England, 2001).

[18] V. Giovannetti, S. Lloyd, and L. Maccone, Phys. Rev. Lett. 96, 010401 (2006).  
[19] R. B. Griffiths and C.-S. Niu, Phys. Rev. Lett. 76, 3228 (1996).  
[20] M. Mosca and A. Ekert, Lect. Notes Comput. Sci. 1509, 174 (1999).  
[21] C. Zalka, e-print arXiv:quant-ph/9806084.  
[22] A. M. Childs, J. Preskill, and J. Renes, J. Mod. Opt. 47, 155 (2000).  
[23] E. Knill, G. Ortiz, and R. D. Somma, Phys. Rev. A 75, 012328 (2007).  
[24] W. van Dam, G. M. D'Ariano, A. Ekert, C. Macchiavello, and M. Mosca, Phys. Rev. Lett. 98, 090501 (2007).  
[25] J. A. Jones and M. Mosca, Phys. Rev. Lett. 83, 1050 (1999).  
[26] A. Barenco et al., Phys. Rev. A 52, 3457 (1995).  
[27] J. Q. You and F. Nori, Phys. Rev. B 68, 064509 (2003).  
[28] G. Wendin and V. S. Shumeiko, in Handbook of Theoretical and Computational Nanotechnology, edited by M. Rieth and W. Schommers (ASP, Los Angeles, 2006), Vol. 3, pp. 223-309.  
[29] J. Lantz, M. Wallquist, V. S. Shumeiko, and G. Wendin, Phys. Rev. B 70, 140507(R) (2004).  
[30] M. Wallquist, V. S. Shumeiko, and G. Wendin, Phys. Rev. B 74, 224506 (2006).  
[31] P. Bertet, C. J. P. M. Harmans, and J. E. Mooij, Phys. Rev. B 73, 064512 (2006).  
[32] C. Rigetti, A. Blais, and M. Devoret, Phys. Rev. Lett. 94, 240502 (2005).  
[33] G. Falci, E. Paladino, and R. Fazio, in Quantum Phenomena in Mesoscopic Systems, edited by B. Altshuler, V. Tognetti, and A. Tagliacozzo (IOS, Amsterdam, 2003).