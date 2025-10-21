# Extreme Violation of Local Realism in Quantum Hypergraph States

Mariami Gachechiladze, Costantino Budroni, and Otfried Gühne  
Naturwissenschaftlich-Technische Fakultät, Universität Siegen, Walter-Flex-Straße 3, 57068 Siegen, Germany  
(Received 6 August 2015; revised manuscript received 27 November 2015; published 17 February 2016)

Hypergraph states form a family of multiparticle quantum states that generalizes the well-known concept of Greenberger-Horne-Zeilinger states, cluster states, and more broadly graph states. We study the nonlocal properties of quantum hypergraph states. We demonstrate that the correlations in hypergraph states can be used to derive various types of nonlocality proofs, including Hardy-type arguments and Bell inequalities for genuine multiparticle nonlocality. Moreover, we show that hypergraph states allow for an exponentially increasing violation of local realism which is robust against loss of particles. Our results suggest that certain classes of hypergraph states are novel resources for quantum metrology and measurement-based quantum computation.

DOI: 10.1103/PhysRevLett.116.070401

Introduction.-Multiparticle entanglement is central for discussions about the foundations of quantum mechanics, protocols in quantum information processing, and experiments in quantum optics. Its characterization has, however, turned out to be difficult. One problem hindering the exploration of multiparticle entanglement is the exponentially increasing dimension of the Hilbert space. This implies that making statements about general quantum states is difficult. So, one has to concentrate on families of multiparticle states with an easier-to-handle description. In fact, symmetries and other kinds of simplifications seem to be essential for a state to be a useful resource. Random states can often be shown to be highly entangled, but useless for quantum information processing [1].

An outstanding class of useful multiparticle quantum states is given by the family of graph states [2], which includes the Greenberger-Horne-Zeilinger (GHZ) states and the cluster states as prominent examples. Physically, these states have turned out to be relevant resources for quantum metrology, quantum error correction, or measurement-based quantum computation [2]. Mathematically, these states are elegantly given by graphs, which describe the correlations and also a possible interaction structure leading to the graph state. In addition, graph states can be defined via a so-called stabilizer formalism: A graph state is the unique eigenstate of a set of commuting observables, which are local in the sense that they are tensor products of Pauli measurements. These stabilizer observables are important for easily computing correlations leading to violations of Bell inequalities [3,4], as well as designing simple schemes to characterize graph states experimentally [5].

Recently, this family of states has been generalized to hypergraph states [6-11]. These states have been recognized as special cases of the so-called locally maximally entangleable states [6]. Mathematically, they are described by hypergraphs, a generalization of graphs, where a single

hyperedge can connect more than two vertices. They can also be described by a stabilizer formalism, but this time, the stabilizing operators are not local. So far, hypergraph states have turned out to play a role for search algorithms in quantum computing [12], quantum fingerprinting protocols [13], and they have been shown to be complex enough to serve as witnesses in all quantum-Merlin-Arthur problems [14]. They have recently been investigated in condensed matter physics as ground states of spin models with interesting topological properties [15,16]. In addition, equivalence classes and further entanglement properties of hypergraph states have been studied [9].

In this Letter, we show that hypergraph states violate local realism in an extreme manner, but in a way that is robust against the loss of particles. We demonstrate that this leads to applications of these states in quantum metrology and quantum computation. We see that the stabilizer formalism describing hypergraph states, despite being nonlocal, can be used to derive Hardy-type nonlocality arguments [17], Bell inequalities for genuine multiparticle entanglement [18], or a violation of local realism with a strength exponentially increasing with the number of particles. Our approach starts precisely with the properties of the stabilizer, in order to identify the useful correlations provided by quantum mechanics. This is in contrast to previous approaches that were either too general, e.g., Bell inequalities for general multiparticle states [19,20], or too restricted, considering only a few specific examples of hypergraph states and leading to nonrobust criteria [9]. The violation of local realism is the key to further applications in information processing. Indeed, it is well known that violation of a Bell inequality leads to advantages, in distributed computation scenarios [21,22]. In addition, we will explicitly show that certain classes of hypergraph states lead to Heisenberg scaling in quantum metrology and advantages in measurement-based quantum computation.

Hypergraph states.-A hypergraph  $H = (V, E)$  consists of a set of vertices  $V = \{1, \dots, N\}$  and a set of hyperedges  $E \subset 2^V$ , with  $2^V$  the power set of  $V$ . While for graphs edges connect only two vertices, hyperedges can connect more than two vertices; examples of hypergraphs are depicted in Fig. 1. For any hypergraph we define the corresponding hypergraph state  $|H\rangle$  as the  $N$ -qubit state

$$
| H \rangle = \prod_ {e \in E} C _ {e} | + \rangle^ {\otimes N}, \tag {1}
$$

where  $| + \rangle = (|0\rangle + |1\rangle) / \sqrt{2}$ ,  $e$  is a hyperedge, and  $C_e$  is a multiqubit phase gate acting on the Hilbert space associated with the vertices  $v \in e$ , given by the matrix  $C_e = 1 - 2|1\dots 1\rangle \langle 1\dots 1|$ . The first nontrivial hypergraph state consists of  $N = 3$  qubits connected by a single hyperedge [see Fig. 1(a)]. Hypergraph states have been recognized as special cases of locally maximally entangleable states, generated via a fixed interaction phase of  $\phi = \pi$  [6].

Alternatively, we can define the hypergraph states using a stabilizer formalism [9]. For each qubit  $i$  we define the operator

$$
g _ {i} = X _ {i} \otimes_ {e \in E} C _ {e \backslash \{i \}}. \tag {2}
$$

Here and in what follows, we denote by  $X_{i}$  and  $Z_{i}$  the Pauli matrices, acting on the  $i$ th qubit. The hypergraph state can be defined as the unique eigenstate for all of them,  $g_{i}|H\rangle = |H\rangle$  with the eigenvalue  $+1$ . Consequently, the hypergraph state is an eigenstate of the entire stabilizer, i.e., the commutative group formed by all the products of the  $g_{i}$ . It should be noted that the  $g_{i}$  are, in general, nonlocal operators, as they are not tensor products of operators acting on single parties. We say that a hyperedge has cardinality  $k$ , if it circumscribes  $k$  vertices and a hypergraph is  $k$  uniform, if all edges have cardinality  $k$ . Finally, note that different hypergraphs may lead to equivalent hypergraph states, in the sense that the two states can be converted into one other by a local basis change. For small numbers of qubits, the resulting equivalence classes have been identified [9].

![](images/71c590dce73ad6b643cb04cf61784cf7aaa45957c971037fbdfa764777ee4c77.jpg)  
FIG. 1. Examples of hypergraphs. (a) A simple hypergraph with three vertices and a single edge  $e = \{1,2,3\}$  connecting all three vertices. The corresponding hypergraph state  $|H_3\rangle = C_{123}| + \rangle^{\otimes 3} = (|000\rangle +|001\rangle +\dots +|110\rangle -|111\rangle) / \sqrt{8}$  is discussed in detail in the text. (b) This hypergraph contains only edges of cardinality two, so it is an ordinary graph. The state corresponding to this fully connected graph is the five-qubit GHZ state. (c) The fully connected three-uniform hypergraph represents a state that can be seen as a generalization of the GHZ state.

![](images/d7003463b80226ad6080efcfa843b2d091c3a6a5528f957e2690a2915811d22b.jpg)

![](images/e0845f07359d759fbb032c3d431edee654d6df3e90ff7a3cb19edc931c664f50.jpg)

Local correlations from the nonlocal stabilizer.-The key observation for the construction of our nonlocality arguments is that the stabilizer of hypergraph states, despite being nonlocal, predicts perfect correlations for some local measurements. In the following, we explain this for the three-qubit hypergraph state  $|H_3\rangle$ , but the method is general. The stabilizing operators for the three-qubit hypergraph state are

$$
g _ {1} = X _ {1} \otimes C _ {2 3}, \quad g _ {2} = X _ {2} \otimes C _ {1 3}, \quad g _ {3} = X _ {3} \otimes C _ {1 2}. \tag {3}
$$

We can expand the controlled phase gate  $C_{23}$  on two qubits, leading to

$$
g _ {1} = X _ {1} \otimes (| 0 0 \rangle \langle 0 0 | + | 0 1 \rangle \langle 0 1 | + | 1 0 \rangle \langle 1 0 | - | 1 1 \rangle \langle 1 1 |) \tag {4}
$$

and similar expressions for the other  $g_{i}$ . Since  $g_{1}|H_{3}\rangle = +|H_{3}\rangle$ , the outcomes for  $X$  measurements on the first qubit and  $Z$  measurements on the second and third qubits are correlated: if one measures "+" on the first qubit, then the other two parties cannot both measure "−" in the  $Z$  direction, as this would produce -1 as the overall eigenvalue. So, we extract the first correlation from the stabilizer formalism:

$$
P (+ - - | X Z Z) = 0. \tag {5}
$$

The lhs of Eq. (5) denotes the probability of measuring  $+ -$  in XZZ on the qubit 1,2, and 3, respectively. Similarly, it follows that if one measures “-” in the  $X$  direction on the first qubit, then the other parties, both have to measure “-” in the  $Z$  direction. So we have

$$
P (- + + | X Z Z) + P (- + - | X Z Z) + P (- - + | X Z Z) = 0, \tag {6}
$$

which implies, of course, that each of the probabilities is zero. Since the three-qubit hypergraph state is symmetric, the same correlations for measuring  $X$  on other qubits can be obtained by considering  $g_{2}$  and  $g_{3}$ , leading to permutations of correlations in Eqs. (5) and (6).

Three-qubit hypergraph state  $|H_3\rangle$ . We start with the discussion of fully local hidden variable (HV) models. Such models assign for any value of the HV  $\lambda$  results to all measurements of the parties in a local manner, meaning that the probabilities for a given HV factorize. If we denote by  $r_i$  the result and by  $s_i$  the measurement setting on the  $i$ th particle, respectively, then the probabilities coming from local models are of the form

$$
\begin{array}{l} P \left(r _ {1}, r _ {2}, r _ {3} \mid s _ {1}, s _ {2}, s _ {3}\right) \\ = \int d \lambda p (\lambda) \chi^ {A} \left(r _ {1} \mid s _ {1}, \lambda\right) \chi^ {B} \left(r _ {2} \mid s _ {2}, \lambda\right) \chi^ {C} \left(r _ {3} \mid s _ {3}, \lambda\right). \tag {7} \\ \end{array}
$$

For probabilities of this form, it is well known that it suffices to consider models which are, for a given  $\lambda$ ,

deterministic. This means that  $\chi^i$  takes only the values 0 or 1, and there is only a finite set of  $\chi^i$  to consider.

Observation 1.—If a fully local hidden variable model satisfies the conditions from Eqs. (5) and (6) and their symmetric correlations coming from the permutations, then it must fulfill

$$
P (+ - - | X X X) + P (- + - | X X X) + P (- - + | X X X) = 0. \tag {8}
$$

The proof of this statement is done by exhausting all possible local deterministic assignments.

In contrast, for  $|H_3\rangle$  we have

$$
P (+ - - | X X X) = \frac {1}{1 6}, \tag {9}
$$

and the same holds for the permutations of the qubits. The above is a so-called Hardy argument [17], namely, a set of joint probabilities equal to 0 or, equivalently, logical implications that together imply that some other probability is equal to zero.

Our method shows how the correlations of the nonlocal stabilizer can be used for Hardy-type arguments. We recall that Hardy-type arguments have been obtained for all permutation-symmetric states [23,24]. However, they involved different settings and have no direct connection with the stabilizer formalism, making a generalization complicated. In contrast, we will see that our measurements can even be used to prove genuine multiparticle nonlocality of the hypergraph state. First, we translate the Hardy-type argument into a Bell inequality:

Remark 2.—Putting together all the null terms derived from the stabilizer formalism and subtracting the terms causing a Hardy-type argument, we obtain the Bell inequality

$$
\begin{array}{l} \left\langle \mathcal {B} _ {3} ^ {(1)} \right\rangle = \left[ P (+ - - | X Z Z) + P (- + + | X Z Z) \right. \\ + P (- + - | X Z Z) + P (- - + | X Z Z) + \text {p e r m u t a t i o n s} ] \\ - [ P (+ - - | X X X) + \text {p e r m u t a t i o n s} ] \geq 0, \tag {10} \\ \end{array}
$$

where the permutations include all distinct terms that are obtained by permuting the qubits. The three-uniform hypergraph state violates the inequality (11) with the value of  $\langle \mathcal{B}_3^{(1)}\rangle = -3 / 16$

This Bell inequality follows from the Hardy argument: If a deterministic local model predicts one of the results with the minus signs, it also has to predict at least one of the results corresponding to the terms with a plus sign, otherwise, it contradicts with the Hardy argument. In addition, all the terms with a minus sign are exclusive, so a deterministic LHV model can predict only one of them.

The Hardy-type argument and the Bell inequality can be generalized to a higher number of qubits, if we consider  $N$ -qubit hypergraphs with the single hyperedge having a cardinality  $N$ :

Observation 3.—Consider the  $N$ -qubit hypergraph state with a single hyperedge of cardinality  $N$ . Then, all the correlations coming from the stabilizer [as generalizations of Eqs. (5) and (6)] imply that for any possible set of results  $\{r_i\}$  where one  $r_{i_1} = +1$  and two  $r_{i_2} = r_{i_3} = -1$  one has

$$
P \left(r _ {1}, r _ {2}, \dots , r _ {N} \mid X _ {1} X _ {2} \dots X _ {N}\right) = 0. \tag {11}
$$

For the hypergraph state, however, this probability equals  $1 / 2^{(2N - 2)}$ . This Hardy-type argument leads to a Bell inequality as in Eq. (10) which is violated by the state with a value of  $-(2^N - N - 2) / 2^{(2N - 2)}$ .

Clearly, the violation of the Bell inequality is not strong, as it does not increase with the number of particles. Nevertheless, observation 3 shows that the nonlocal stabilizer formalism allows one to easily obtain nonlocality proofs. In fact, one can directly derive similar arguments for other hypergraph states (e.g., states with one hyperedge of cardinality  $N$  and one further arbitrary hyperedge). These results will be presented elsewhere. Note that these states are not symmetric, so the results of Refs. [23,24] do not apply.

So far, we considered only fully local models, where for a given HV all the probabilities factorize. Now we go beyond these restricted types of models to the so-called hybrid models [18]. We consider a bipartition of the three particles, say  $A|BC$ , and consider a model of the type  $P(r_1, r_2, r_3 | s_1, s_2, s_3) = \int d\lambda p(\lambda) \chi^A(r_1 | s_1, \lambda) \chi^{BC} \times (r_2, r_3 | s_2, s_3, \lambda)$ . Here, Alice is separated from the rest, but  $\chi^{BC}$  may contain correlations, e.g., coming from an entangled state between  $B$  and  $C$ . In order to be physically reasonable, however, we still request  $\chi^{BC}$  not to allow instantaneous signaling.

This kind of model, even if different bipartitions are mixed, cannot explain the correlations of the hypergraph state, meaning that the hypergraph state is genuine multi-particle nonlocal. First, one can see by direct inspection that the stabilizer conditions from Eqs. (5) and (6) are not compatible with the hypergraph correlations  $P(- - |XXX) = 1 / 16$  and  $P(- - - |ZZZ) = 1 / 8$ . Contrary to the correlations in Eq. (9) these are symmetric, and allow the construction of a Bell-Svetlichny inequality [18] valid for all the different bipartitions.

Observation 4. - Putting all the terms from the hypergraph stabilizer formalism and the correlations  $P(- - - |XXX)$  and  $P(- - - |ZZZ)$  together, we obtain the following Bell-Svetlichny inequality for genuine multi-particle nonlocality,

$$
\begin{array}{l} \langle \mathcal {B} _ {3} ^ {(2)} \rangle = [ P (+ - - | X Z Z) + P (- + + | X Z Z) \\ + P (- + - | X Z Z) + P (- - + | X Z Z) + \text {p e r m u t a t i o n s} ] \\ + P (- - - | X X X) - P (- - - | Z Z Z) \geq 0, \tag {12} \\ \end{array}
$$

which is violated by the state  $|H_3\rangle$  with  $\langle \mathcal{B}_3^{(2)}\rangle = -1\backslash 16$ .

The proof is done by an exhaustive assignments of nonsignaling and local models.

To investigate the noise tolerance of inequality (12), we consider states of the type  $\varrho = (1 - \varepsilon)|H\rangle \langle H| + \varepsilon \mathbb{1} / 8$  and ask how much noise can be added, while the inequality is still violated. The white noise tolerance of inequality (13) is  $\varepsilon = 1 / 13\approx 7.69\%$  and is optimal in the sense that for larger values of  $\varepsilon$  a hybrid model can be found which explains all possible measurements of  $X$  and  $Z$  (within numerical precision). The existence of such a model can be shown by linear programming (see Appendix A [25]). With the same method we can also prove that the state becomes fully local with respect to  $X$  and  $Z$  measurements for  $\varepsilon \geq 2 / 3\approx 66.6\%$ .

Three uniform hypergraph states. Let us extend our analysis to hypergraph states with a larger number of particles. Here, it is interesting to ask whether the violation of Bell inequalities increases exponentially with the number of parties. Such a behavior has previously been observed only for GHZ states [3] and some cluster states [4].

GHZ states are described by fully connected graphs (see Fig. 1), i.e., fully connected two-uniform hypergraph states. It is thus natural to start with fully connected three-uniform hypergraph states. First, we observe that for such states on  $N$  qubits and for even  $m$  with  $1 < m < N$

$$
\langle \underbrace {X \dots X Z \dots Z} _ {m} \rangle = \left\{ \begin{array}{l l} + \frac {1}{2} & \text {i f} m = 2 \bmod 4, \\ - \frac {1}{2} & \text {i f} m = 0 \bmod 4. \end{array} \right. \tag {13}
$$

Moreover, if  $m = N$ , then the correlations are given by

$$
\langle \underbrace {X X . . . X X} _ {N} \rangle = \left\{ \begin{array}{l l} 0 & \text {i f} N = 0 \bmod 4, \\ 1 & \text {i f} N = 2 \bmod 4. \end{array} \right. \tag {14}
$$

Finally, we always have  $\langle ZZ\dots ZZ\rangle = 0$  (see Appendix B for details [25]).

We then consider the following Bell operator:

$$
\begin{array}{l} \mathcal {B} _ {N} = - [ A A A \dots A A ] + [ B B A \dots A + \text {p e r m u t a t i o n s} ] \\ - \left[ B B B B A \dots A + \text {p e r m u t a t i o n s} \right] + [ \dots ] - \dots . \tag {15} \\ \end{array}
$$

Note that this Bell operator is similar to  $\langle \mathcal{B}_N^M\rangle$  of the original Mermin inequality [3], but it differs in the number of  $B$  (always even) considered. Using the correlations computed above, we can state:

Observation 5.—If we fix in the Bell operator  $\mathcal{B}_N$  in Eq. (15) the measurements to be  $A = Z$  and  $B = X$ , then the  $N$ -qubit fully connected three-uniform hypergraph state violates the classical bound, by an amount that grows exponentially with the number of qubits, namely

$$
\langle \mathcal {B} _ {N} \rangle_ {C} \leq 2 ^ {\lfloor N / 2 \rfloor} \quad \text {f o r l o c a l H V m o d e l s , a n d}
$$

$$
\left\langle \mathcal {B} _ {N} \right\rangle_ {Q} \geq 2 ^ {N - 2} - \frac {1}{2} \quad \text {f o r t h e h y p e r g r a p h s t a t e .} \tag {16}
$$

The proof is given in Appendix C [25].

Four-uniform hypergraph states.—Finally, let us consider four-uniform complete hypergraph states. For them, the correlations of measurements as in Eq. (13) are not so simple: They are not constant, and depend on  $m$  as well as on  $N$ . Nevertheless, they can be explicitly computed, and detailed formulas are given in Appendix D [25]. From these correlations, we can state:

Observation 6. The  $N$ -qubit fully connected four-uniform hypergraph state violates local realism by an amount that grows exponentially with the number of qubits. More precisely, one can find a Mermin-like Bell operator  $\mathcal{B}_N$  such that

$$
\frac {\left\langle \mathcal {B} _ {N} \right\rangle_ {Q}}{\left\langle \mathcal {B} _ {N} \right\rangle_ {C}} \stackrel {N \rightarrow \infty} {\sim} \frac {\left(1 + \frac {1}{\sqrt {2}}\right) ^ {N - 1}}{\sqrt {2} ^ {N + 3}} \approx \frac {1 . 2 0 7 1 1 ^ {N}}{2 \sqrt {2} + 2}. \tag {17}
$$

A detailed discussion is provided in Appendix E [25].

Robustness.-So far, we have shown that three- and four-uniform hypergraph states violate local realism comparable to GHZ states. A striking difference is, however, that the entanglement and Bell inequality violation of hypergraph states is robust under particle loss. This is in stark contrast to GHZ states, which become fully separable if a particle is lost. We can state:

Observation 7.-The  $N$ -qubit fully connected four-uniform hypergraph state preserves the violation of the local realism even after loss of one particle. More precisely, for  $N = 8k + 4$  we have  $\langle \mathcal{B}_{N - 1}\rangle_{Q} / \langle \mathcal{B}_{N}\rangle_{Q}\stackrel {N\to \infty}{\sim}1 / (\sqrt{2} +1)$ . This means that the reduced state shows the same exponential scaling of the Bell inequality violation as the original state.

For detailed discussions, see Appendix F [25].

For three-uniform complete hypergraph states we can prove that the reduced states are highly entangled, as they violate inequalities testing for separability [26] exponentially. This violation decreases with the number of traced out qubits, but persists even if several qubits are lost. This suggests that this class of hypergraph states is also more robust than GHZ states; details can be found in Appendix G [25]. Despite the structural differences, this property resembles the  $W$  state, which is itself less entangled but more robust than the GHZ state [27]. In addition, this may allow the lower detection efficiency in the experiments.

Discussion and conclusion.-A first application of our results is quantum metrology. In the standard scheme of quantum metrology one measures an observable  $M_{\theta}$  and tries to determine the parameter  $\theta$  which describes a phase in some basis [28,29]. If one takes product states, one obtains a signal  $\langle M_{\theta} \rangle \sim \cos(\theta)$  on a single particle. Repeating it on  $N$  particles allows us to determine  $\theta$  with an accuracy of  $\delta \theta \sim 1/\sqrt{N}$ , the so-called standard quantum limit. Using an  $N$ -qubit GHZ state, however, one observes  $\langle (M_{\theta})^{\otimes N} \rangle \sim \cos(N\theta)$  and this phase superresolution allows us to reach the Heisenberg limit  $\delta \theta \sim 1/N$ . For a general state  $\varrho$ , it has been shown that the visibility of the phase superresolution is given by the expectation value of

the Mermin-type inequality,  $V = \mathrm{Tr}(\mathcal{B}_N\varrho) / 2^{N - 1}$  [29]. So, since the three-uniform hypergraph states violate this inequality with a value  $\langle \mathcal{B}_N\rangle_Q\sim 2^{(N - 2)}$  the visibility is  $V\sim 1 / 2$ , independently of the number of particles. This means that these states can be used for Heisenberg-limited metrology, and from our results they can be expected to have the advantage of being more robust to noise and particle losses.

The second application of exponential violation of Bell inequalities is nonadaptive measurement-based quantum computation with linear side processing  $(NMQC_{\oplus})$  [30].  $NMQC_{\oplus}$  is a nonuniversal model of quantum computation where linear classical side processing is combined with quantum measurements in a nonadaptive way; i.e., the choice of settings is independent of previous outcomes. In Ref. [30] the authors connect the expectation value of a full-correlation Bell expression [20] with the success probability of computing a Boolean function, specified as a function of the inequality coefficients, via  $NMQC_{\oplus}$ . In particular, the exponential violation of generalized Svetlichny inequalities [31] (equal to Mermin inequalities for even  $N$ ), corresponds to a constant success probability  $P_{\mathrm{suc}}$  of computing the pairwise AND on  $N$  bits extracted from a uniform distribution, whereas in the classical case  $P_{\mathrm{suc}} - 1/2$  decreases exponentially with  $N$ . As a consequence, the exponential violation of the full-correlation Bell expression  $\mathcal{B}_N$  can be directly related to an exponential advantage for computation tasks in the  $NMQC_{\oplus}$  framework. Moreover, in several cases, e.g., four-uniform hypergraph states of  $N = 6\bmod 8$  qubits, also the Svetlichny inequality is violated exponentially, providing an advantage for computation of the pairwise AND discussed in Ref. [30].

In summary, we have shown that hypergraph states violate local realism in many ways. This suggests that they are interesting resources for quantum information processing. Moreover, this makes the observation of hypergraph states a promising task for experimentalists. In our work, we focused only on some classes of hypergraph states, but for future research, it would be desirable to identify classes of hypergraph states which allow for an all-versus-nothing violation of local realism or which are strongly genuine multiparticle nonlocal.

We thank D. Nagaj, F. Steinhoff, M. Wiesniak, and B. Yoshida for discussions. This work has been supported by the EU (Marie Curie CIG 293993/ENFOQI), the FQXi Fund (Silicon Valley Community Foundation), the DFG, and the ERC (Consolidator Grant No. 683107/TempoQ).

[1] P. Hayden, D. W. Leung, and A. Winter, Commun. Math. Phys. 265, 95 (2006); D. Gross, S. T. Flammia, and J. Eisert, Phys. Rev. Lett. 102, 190501 (2009); M. J. Bremner, C. Mora, and A. Winter, Phys. Rev. Lett. 102, 190502 (2009).

[2] M. Hein, W. Dur, J. Eisert, R. Raussendorf, M. Van den Nest, and H.-J. Briegel, Entanglement in Graph States and Its Applications, in Quantum Computers, Algorithms and Chaos, edited by G. Casati, D. L. Shepelyansky, P. Zoller, and G. Benenti (IOS Press, Amsterdam, 2006); arXiv:quant-ph/0602096.  
[3] N.D. Mermin, Phys. Rev. Lett. 65, 1838 (1990).  
[4] O. Gühne, G. Toth, P. Hyllus, and H. J. Briegel, Phys. Rev. Lett. 95, 120405 (2005); G. Toth, O. Gühne, and H. J. Briegel, Phys. Rev. A 73, 022303 (2006).  
[5] O. Gühne and G. Tóth, Phys. Rep. 474, 1 (2009).  
[6] C. Kruszynska and B. Kraus, Phys. Rev. A 79, 052304 (2009).  
[7] R. Qu, J. Wang, Z. S. Li, and Y. R. Bao, Phys. Rev. A 87, 022311 (2013).  
[8] M. Rossi, M. Huber, D. Bruß, and C. Macchiavello, New J. Phys. 15, 113022 (2013).  
[9] O. Gühne, M. Cuquet, F. E. S. Steinhoff, T. Moroder, M. Rossi, D. Bruß, B. Kraus, and C. Macchiavello, J. Phys. A 47, 335303 (2014).  
[10] X.-Y. Chen and L. Wang, J. Phys. A 47, 415304 (2014).  
[11] D. W. Lyons, D. J. Upchurch, S. N. Walck, and C. D. Yetter, J. Phys. A 48, 095301 (2015).  
[12] M. Rossi, D. Bruß, and C. Macchiavello, Phys. Scr. T160, 014036 (2014).  
[13] H. Buhrman, R. Cleve, J. Watrous, and R. de Wolf, Phys. Rev. Lett. 87, 167902 (2001); C. E. Mora, H. J. Briegel, and B. Kraus, Int. J. Quantum. Inform. 05, 729 (2007).  
[14] A. B. Grilo, I. Kerenidis, and J. Sikora, arXiv:1410.2882.  
[15] B. Yoshida, arXiv:1508.03468.  
[16] J. Miller and A Miyake, arXiv:1508.02695.  
[17] L. Hardy, Phys. Rev. Lett. 71, 1665 (1993).  
[18] G. Svetlichny, Phys. Rev. D 35, 3066 (1987).  
[19] S. Popescu and D. Rohrlich, Phys. Lett. A 166, 293 (1992).  
[20] R. F. Werner and M. M. Wolf, Phys. Rev. A 64, 032112 (2001); M. Zukowski and C. Brukner, Phys. Rev. Lett. 88, 210401 (2002).  
[21] N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani, and S. Wehner, Rev. Mod. Phys. 86, 419 (2014).  
[22] C. Brukner, M. Zukowski, J.-W. Pan, and A. Zeilinger, Phys. Rev. Lett. 92, 127901 (2004).  
[23] S. Abramsky and C. Constantin, Electron. Proc. Theor. Comput. Sci. 171, 10 (2014) [arXiv:1412.5213].  
[24] Z. Wang and D. Markham, Phys. Rev. Lett. 108, 210407 (2012).  
[25] See Supplemental Material at http://link.aps.org/ supplemental/10.1103/PhysRevLett.116.070401 for the appendix.  
[26] S. M. Roy, Phys. Rev. Lett. 94, 010402 (2005).  
[27] M. Koashi, V. Buzek, and N. Imoto, Phys. Rev. A 62, 050302(R) (2000).  
[28] V. Giovannetti, S. Lloyd, and L. Maccone, Science 306, 1330 (2004).  
[29] W.-B. Gao, C.-Y. Lu, X.-C. Yao, P. Xu, O. Gühne, A. Goebel, Y.-A. Chen, C.-Z. Peng, Z.-B. Chen, and J.-W. Pan, Nat. Phys. 6, 331 (2010).  
[30] M.J. Hoban, E.T. Campbell, K. Loukopoulos, and D.E. Browne, New J. Phys. 13, 023014 (2011).  
[31] D. Collins, N. Gisin, S. Popescu, D. Roberts, and V. Scarani, Phys. Rev. Lett. 88, 170405 (2002).