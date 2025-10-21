# ACCEPTED MANUSCRIPT

# Loss-tolerant teleportation on large stabilizer states

To cite this article before publication: Sam Morley-Short et al 2018 Quantum Sci. Technol. in press https://doi.org/10.1088/2058-9565/aaf6c4

# Manuscript version: Accepted Manuscript

Accepted Manuscript is "the version of the article accepted for publication including all changes made as a result of the peer review process, and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an 'Accepted Manuscript' watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors"

This Accepted Manuscript is © 2018 IOP Publishing Ltd.

During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully protected by copyright and cannot be reused or reposted elsewhere. As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.

After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they adhere to all the terms of the licence https://creativecommons.org/licenses/by-nc-nd/3.0

Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.

View the article online for updates and enhancements.

# Loss-tolerant teleportation on large stabilizer states

Sam Morley-Short\*, Mercedes Gimeno-Segovia1,2,3, Terry Rudolph2, and Hugo Cable

<sup>1</sup>Quantum Engineering Technology Labs, H. H. Wills Physics Laboratory and Department of Electrical and Electronic Engineering, University of Bristol, BS8 1FD, UK

$^{2}$ Department of Physics, Imperial College London, London SW7 2AZ, UK

$^{3}$ Institute for Quantum Science and Technology, University of Calgary, Alberta T2N 1N4, Canada

# Abstract

We present a general method for finding loss-tolerant teleportation on large, entangled stabilizer states using only single-qubit measurements, known as stabilizer pathfinding (SPF). For heralded loss, SPF is shown to generate optimally loss-tolerant measurement patterns on any given stabilizer state. Furthermore, SPF also provides highly loss-tolerant teleportation strategies when qubit loss is unheralded. We provide a fast algorithm for SPF that updates continuously as a state is generated and measured, which is therefore suitable for real-time implementation on a quantum-computing device. When compared to simulations of previous heuristics for loss-tolerant teleportation on graph states, SPF provides considerable gains in tolerance to both heralded and unheralded loss, achieving a near-perfect teleportation rate  $(>95\%)$  in the regime of low qubit loss  $(< 10\%)$  on various graph state lattices. Using these results we also present evidence that points towards the existence of loss-tolerant thresholds on such states, which in turn indicates that the loss-tolerant behaviour we have found also applies as the number of qubits tends to infinity. Our results represent a significant advance towards the realistic implementation of teleportation in both large-scale and near-future quantum architectures that are susceptible to qubit loss, such as linear optical quantum computation and quantum communication networks.

# 1 Introduction

Many new quantum technologies demand the teleportation of quantum states across large, multiparty entangled states [1-6]. A common example is provided by measurement-based quantum computation (MBQC) [7, 8], which uses single-qubit measurements on cluster states and feed-forward of measurement outcomes to implement universal quantum computation. Teleportation steps are used extensively in MBQC, whether following the original proposal [7] or generalisations using alternative entangled resource states [9]. In practise, any protocol for quantum computation (or related applications such as in quantum communications [10]) must also tolerate qubit dephasing and loss. While the primary source of error for many quantum computing platforms is qubit dephasing, loss errors are known to dominate in architectures such as linear optical quantum computation (LOQC) [6, 11-13]. Currently, the main approach to mitigating significant degrees of loss are quantum error correcting codes (QECC) [14], loss-tolerant qubit encodings [15-17], or some other process imposing additional resource costs, such as the proposal of [18] which enables photon loss to be converted into a linear time cost, providing successful quantum gates within a modular light-matter based architecture.

In this work we present a new method for teleportation that exploits the correlations of large, entangled stabilizer states using only single-qubit measurements, known as stabilizer pathfinding (SPF). For heralded loss, we show that SPF provides optimally loss-tolerant measurement patterns for all stabilizer states, as well as tolerance of unheraldised qubit loss. To implement SPF in a realistic setting, we also provide an algorithm

that can generate SPF measurement patterns with low computational overhead based on applying minimal updates during states generation and measurement.

When compared to simulations of previous heuristics for teleportation on quantum graph states, SPF provides significant gains in loss tolerance for both the heralded and unheralded case. For example, when applied to the square-lattice graph states (i.e. cluster states) commonly used for MBQC, we find that SPF achieves a teleportation rate of  $T \approx 98\%$  for  $10\%$  heralded qubit loss, compared to  $T \approx 40\%$  using previous teleportation techniques based on localisable entanglement [7, 19]. When the loss is unheralded on the same state, SPF measurement strategies also achieve at least  $T \approx 84\%$  where there was no previously-known method for achieving loss tolerance for teleportation.

We also provide evidence of critical loss-tolerant thresholds on a variety of graph state lattices. These would show that loss-tolerant teleportation can be achieved in the limit of infinite lattice size, with existence of loss-tolerant measurement patterns guaranteed below some threshold loss rate. Our results provide an optimistic outlook on the reduction of loss rates in quantum computation and communication architectures as well as ensuring optimal use of intermediately-sized states generated by near-term devices.

The paper is structured as follows. Section 2 motivates our work by considering the task of teleportation on stabilizer states and presents previous approaches to achieving loss tolerance. The stabilizer pathfinding approach to teleportation is then presented in section 3 which outlines an algorithm for it's computation. Our main results are given in section 4 which provides numerical simulations to highlight SPF's improved loss tolerance in the case of both heralded and unheralded loss. Section 5 then discusses SPF's algorithmic efficiency and it's implications for LOQC and other quantum technology platforms. Finally, section 6 summarises the work and suggests a selection of avenues for further research.

# 2 Background and motivation

We now present a short introduction to teleportation on stabilizer states followed by an example to motivate the need for a general approach for finding teleportation measurement patterns. In what follows we will assume familiarity with the standard definitions on the stabilizer formalism, graph states and MBQC and refer the reader to [8, 20, 21] for more details. Also given the equivalence between stabilizer and graph states [22, 23], we shall only consider graph states here but note that the following applies to stabilizer states. An introduction to stabilizer formalism is also provided in Appendix A.

# 2.1 Teleportation on stabilizer states

Consider an arbitrary quantum state  $|\psi \rangle$  on input qubit  $I$  with logical operators  $\bar{X}_{\psi} = X_I, \bar{Z}_{\psi} = Z_I$ . Now consider the entangling of  $|\psi \rangle$  with  $n$  other qubits in some graph state such that the resultant state  $|\Psi \rangle$  is now defined by a pair of logical operators  $\bar{X}_{\Psi}, \bar{Z}_{\Psi}$  and stabilizer generators  $\mathcal{G}_{\Psi} = \{K_i\}_{i=1}^n$  that form the closed group  $S_{\Psi} = \langle \mathcal{G}_{\Psi} \rangle$  of all stabilizers of  $|\Psi \rangle$  under multiplication. Teleportation on  $|\Psi \rangle$  aims to find some set of single-qubit measurements or measurement pattern  $M$  that recovers  $|\psi \rangle$  on some output qubit  $O$ , or equivalently, that produce two anti-commuting logical operators acting only on  $O$ . Qubits not measured by any element of  $M$  can then be lost without impeding teleportation, such that maximal loss tolerance is achieved by minimising  $|M|$ . Hence, the set of all teleportation protocols which can tolerate some amount of loss can be known by finding all  $M$  that omit at least one qubit.

We now present a general method for finding valid  $M$  on  $|\Psi \rangle$ . First, recall that any product of the logical operator and stabilizer is also a logical operator on  $|\Psi \rangle$ , thereby defining the set of all logical operators  $\mathcal{L}_{\Psi} = \langle \bar{X}_{\Psi},\bar{Z}_{\Psi}\rangle \times S_{\Psi}$ . Given a pair of logical operators  $\bar{X},\bar{Z}\in \mathcal{L}_{\Psi}$  such that

$$
\{\bar {X} ^ {[ O ]}, \bar {Z} ^ {[ O ]} \} = 0, \quad \mathrm {a n d} \quad [ \bar {X} ^ {[ a ]}, \bar {Z} ^ {[ a ]} ] = 0 \forall a \neq O, \tag {1}
$$

where  $A^{[i]}$  denotes the Pauli operator of  $A$  acting on qubit  $i$ , then it is easy to see that the single-qubit measurement of all  $\bar{X}^{[a]},\bar{Z}^{[a]}\neq \mathbb{I}$  will achieve teleportation onto  $O$ . Specifically, the measurement pattern

# STABILIZER PATHFINDING CONDITIONS:

Consider the state  $|\Psi \rangle$  defined by logical operators  $\mathcal{L}_{\Psi}$  that encodes a single logical qubit state  $|\psi \rangle$ . A valid measurement pattern that recovers  $|\psi \rangle$  on qubit  $O$  of  $|\Psi \rangle$  can be found from any pair of logical operators  $\bar{X}, \bar{Z} \in \mathcal{L}_{\Psi}$  that:

a) anticommute on qubit  $O$ , and  
b) commute on each qubit which is not  $O$ .

Given these conditions are satisfied, teleportation is achieved by performing the set of single-qubit measurements represented by each non-identity Pauli operator of  $\bar{X},\bar{Z}$  on all qubits other than  $O$

Box 1: Conditions any pair of logical operators must satisfy to provide a teleportation measurement pattern.

produced by the pair of logical operators  $\bar{X}$  and  $\bar{Z}$  is given by

$$
M _ {\bar {X}, \bar {Z}} = \{\bar {X} ^ {[ i ]}: \bar {X} ^ {[ i ]} \neq \mathbb {I}, \forall i \neq O \} \cup \{\bar {Z} ^ {[ i ]}: \bar {Z} ^ {[ i ]} \neq \mathbb {I}, \forall i \neq O \}, \tag {2}
$$

which has weight  $w = |M_{\bar{X},\bar{Z}}|$ . The set of all valid measurement patterns  $\mathcal{M} = \{M_{\bar{X},\bar{Z}}\}$  is then given by finding all logical operator pairings satisfying equation (1). Given the equivalence between states' logical operators and stabilizers, we refer to this method for teleportation as stabilizer pathfinding (SPF). From the above requirements we define the stabilizer pathfinding conditions, which are summarised in box 1.

Given the significant number of  $\bar{X}, \bar{Z}$  pairs for large states, measurement patterns are often found from heuristic methods. The most common heuristic for finding a subset of  $\mathcal{M}$  on graph states is a technique we shall refer to as graph pathfinding (GPF), originally proposed for teleportation in MBQC and producing localizable entanglement [7, 19]. As used by MBQC on graph states, this approach requires finding a path  $P = \{I, \dots, O\}$  between qubits  $I$  and  $O$  and  $P$ 's graph neighbourhood  $\Pi$  (all qubits that neighbour a qubit in  $P$  that are not themselves in  $P$ ), on which single-qubit  $X$  and  $Z$  measurements are performed respectively. Finding  $M$  for loss-tolerant teleportation is thus achieved by minimising  $|P \cup \Pi|$ . The graph pathfinding heuristic is usually understood by observing that teleportation occurs from  $X$  measurements along a linear graph state between  $I$  and  $O$  produced from the  $Z$  measurements.

Equally, by recalling that graph state's generators are given by  $K_{i} = X_{i}\bigotimes_{j\in N_{G}(i)}Z_{j} \forall i = 1,\ldots ,n$  (where  $N_G(i)$  is the neighbourhood of  $i$  on graph  $G$ ), it is easy to see why such a technique works through the lens of stabilizer pathfinding. Specifically, given  $P$  there are two always logical operators  $\bar{X}$ ,  $\bar{Z}$  with  $X$  operators at odd and even positions along  $P$  respectively, either terminating with  $Z_O$  for  $\bar{X}$  when  $|P|$  is odd or for  $\bar{Z}$  when  $|P|$  is even, with  $Z$  operators on qubits in  $\Pi$ . When paired such logical operators then give the usual  $M$  for graph pathfinding.

# 2.2 Limitations of graph pathfinding

We now present a motivating example for the relevance of stabilizer pathfinding to loss-tolerant teleportation. Consider the state  $|\Psi \rangle$ , depicted below:

![](images/e002a0a44bfce33d61848c5b676bf747219bcf197392628b7fa941ff56eacf27.jpg)  
Figure 1: An example graph state on which teleportation is to be performed from input qubit  $I$  to output qubit  $O$ , defined by logical operators  $\bar{X}_{\Psi},\bar{Z}_{\Psi}$  and stabilizer generators  $\mathcal{G}_{\Psi}$ .

$$
\begin{array}{l} \bar {X} _ {\Psi} = Z _ {I} \\ \bar {Z} _ {\Psi} = X _ {I} Z _ {1} Z _ {2} Z _ {3} \\ \mathcal {G} _ {\Psi} = \left\{K _ {1} = Z _ {I} X _ {1} Z _ {4}, K _ {2} = Z _ {I} X _ {2} Z _ {5}, K _ {3} = Z _ {I} X _ {3} Z _ {6}, \right. \\ K _ {4} = Z _ {1} X _ {4} Z _ {7}, K _ {5} = Z _ {2} X _ {5} Z _ {8}, K _ {6} = Z _ {3} X _ {6} Z _ {9}, \\ K _ {7} = Z _ {4} X _ {7} Z _ {O}, K _ {8} = Z _ {5} X _ {8} Z _ {O}, K _ {9} = Z _ {6} X _ {9} Z _ {O}, \\ K _ {O} = Z _ {7} Z _ {8} Z _ {9} X _ {O} \} \\ \end{array}
$$

On the above example, graph pathfinding clearly provides only three measurement patterns, such as  $P = \{I, 2, 5, 8, O\}$ , and thus provides tolerance to the loss of at most (but not any) two qubits, such as  $\{4, 6\}$ , with the associated  $M$  depicted in figure 2a). Furthermore, since each  $M$  associated with a path contains anticommuting measurements on at least one qubit, there is little-to-no ability to switch between them in the case of unheralded loss.

Now consider an alternative set of three measurement patterns provided by stabilizer pathfinding:

$$
\begin{array}{l} \bar {X} = K _ {1} K _ {7} \bar {X} _ {\Psi} = X _ {1} X _ {7} Z _ {O}, \bar {Z} = K _ {4} K _ {5} K _ {6} K _ {O} \bar {Z} _ {\Psi} = X _ {I} X _ {4} X _ {5} X _ {6} X _ {O} \Rightarrow M _ {1} = \left\{X _ {I}, X _ {4}, X _ {5}, X _ {6}, X _ {1}, X _ {7} \right\} \\ \bar {X} = K _ {2} K _ {8} \bar {X} _ {\Psi} = X _ {2} X _ {8} Z _ {O}, \bar {Z} = K _ {4} K _ {5} K _ {6} K _ {O} \bar {Z} _ {\Psi} = X _ {I} X _ {4} X _ {5} X _ {6} X _ {O} \Rightarrow M _ {2} = \left\{X _ {I}, X _ {4}, X _ {5}, X _ {6}, X _ {2}, X _ {8} \right\} \\ \bar {X} = K _ {3} K _ {9} \bar {X} _ {\Psi} = X _ {3} X _ {9} Z _ {O}, \bar {Z} = K _ {4} K _ {5} K _ {6} K _ {O} \bar {Z} _ {\Psi} = X _ {I} X _ {4} X _ {5} X _ {6} X _ {O} \Rightarrow M _ {3} = \left\{X _ {I}, X _ {4}, X _ {5}, X _ {6}, X _ {3}, X _ {9} \right\} \\ \end{array}
$$

as depicted in figure 2b). There are two key differences between these  $M$  and those provided by graph pathfinding. Firstly, each  $M$  can tolerate twice the amount of lost qubits, equating to a four-fold increase in the number qubit loss configurations tolerable. Secondly, since no two patterns require contradictory measurements on any qubit, the attempt of one pattern does not preclude the later attempt of another. Although the latter difference is irrelevant in the case of heralded qubit loss, this fact crucially allows tolerance of unheralded loss events. For example, consider we begin a teleportation protocol by the successful measurement of  $X_{I}, X_{4}, X_{5}$ , and  $X_{6}$ , leaving three possible sets of measurements:  $\{X_{1}, X_{7}\}$ ,  $\{X_{2}, X_{8}\}$ , and  $\{X_{3}, X_{9}\}$ . Since only one pair must succeed, any loss on up to two pairs can be tolerated as long as one is completed<sup>1</sup>. This can also be seen by noting that if any pair is successfully measured, any remaining (and potentially lost) qubits are disentangled from the final state on qubit  $O$ .

From the above it is clear the measurement patterns provided by graph pathfinding represent only a small fraction of all  $M \in \mathcal{M}$ . For example, when stabilizer pathfinding is applied on the previous state we find  $|\mathcal{M}| = 2657$ , allowing 60 different combinations of lost qubits, with at most four qubits left unmeasured. However, finding the set  $\mathcal{M}$  through an exhaustive search is impractical for large states in general. Furthermore, many, if not the majority of  $M \in \mathcal{M}$  will not tolerate any qubit loss. In order to overcome this challenge, we shall now present algorithm that finds all maximally lost-tolerant $^2$  measurement patterns without any exhaustive searches.

# 3 Stabilizer pathfinding

Given that  $O(2^{2n})$  possible pairs of logical operators exist for a state with  $n$  generators, computing  $\mathcal{M}$  by brute force is clearly impractical for even modestly sized states<sup>3</sup>. The most practical aspect of our work is an algorithm that implements stabilizer pathfinding to find loss-tolerant measurement patterns without the need for exhaustive searches.

![](images/b64e0370bbb93c491ac1118c6ec9692a95791aa8899c075676c7d37fa268f160.jpg)  
Figure 2: Possible measurement patterns for teleportation between qubits  $I$  and  $O$  provided by a) the graph pathfinding heuristic and b) our generalised stabilizer pathfinding (where measurement  $X_{I}$  is also needed in both cases). In a), all measurements must be successfully completed for teleportation, providing a loss tolerance to the two unlabelled qubits (with the associated path and neighbourhood highlighted in red and blue respectively). In b), if the centre column of qubits are successfully measured then teleportation is completed by the successful measurement of both qubits in any of the three pairs of the same colour. We note that stabilizer pathfinding also returns all graph pathfinding measurement patterns and so may still achieve teleportation even if at most two out of three central columns (red) qubits are lost. Not only does the latter case provide additional qubit loss tolerance, but also tolerance to loss events that are only heralded at the point of measurement (i.e. unheralded loss).

![](images/ff26fa716668837166e62143adf7cabae07367f266ec0e1abe9a87ac1a0c1aaf.jpg)

Functionally our algorithm is divided into two distinct subroutines: i) finding all stabilizers of the state that are relevant for teleportation, and ii) finding all pairs of logical operators that produce maximally loss-tolerant measurement patterns. In this section we provide an outline of each routine's challenges and our solutions, with full technical details found in Appendix B, including a full pseudocode description in algorithm 1. Readers primarily concerned with the degree of loss tolerance afforded by stabilizer pathfinding are directed to section 4.

# 3.1 Which stabilizers are relevant for teleportation?

To prevent the need to store and update all  $2^{n}$  stabilizers, we now consider which of a state's stabilizers are relevant to teleportation. This will allow the identification of the subset of stabilizers that must be tracked for stabilizer pathfinding.

# 3.1.1 Logical operators as combinations of stabilizer generators

Consider an arbitrary state  $|\Psi \rangle$  with stabilizers  $\mathcal{S}_{\Psi} = \langle \mathcal{G}_{\Psi}\rangle$ , where  $\mathcal{G}_{\Psi} = \{K_i\}_{i=1}^n$ . Given that  $\mathcal{S}_{\Psi}$  form a closed group under multiplication, we can label each stabilizer  $S_c \in \mathcal{S}_{\Psi}$  by the set of generator indices  $c$  from which it is produced, such that

$$
S _ {c} = \prod_ {i \in c} K _ {i}. \tag {3}
$$

We shall refer to  $c$  as the stabilizer's generator combination, by which it is uniquely defined (given a fixed  $\mathcal{G}_{\Psi}$ ).

However, not all stabilizers are equally useful for the task of producing teleportation measurement patterns. To see this, consider applying stabilizer pathfinding for teleportation from  $I$  to  $O$  on linear graph state  $|\Psi \rangle$  depicted below:

![](images/ed2809ab0e34b71072b0bb5d658a68e1acb82305e556ff5bba2aa110e87eed0e.jpg)

$$
\bar {X} _ {\Psi} = Z _ {I}
$$

$$
Z _ {\Psi} = X _ {I} Z _ {1}
$$

$$
\mathcal {G} _ {\Psi} = \left\{Z _ {I} X _ {1} Z _ {2} \quad , \quad \left(K _ {1}\right) \right.
$$

$$
Z _ {1} X _ {2} Z _ {3}, \left(K _ {2}\right)
$$

$$
Z _ {2}   X _ {3}   Z _ {O}  , \quad (K _ {3})
$$

$$
\left. Z _ {3}   X _ {O} \right\} \left(K _ {O}\right)
$$

Firstly consider the stabilizer  $S_{\{1,3\}} = K_1K_3 = Z_I X_1 X_3 Z_O$ , used to define the logical operator  $\bar{X}_{\{1,3\}} = S_{\{1,3\}} \bar{X}_\Psi = X_1 X_3 Z_O$ . This choice of stabilizer allows  $\bar{X}_{\{1,3\}}$  to be paired with some  $\bar{Z}$  that obeys the stabilizer pathfinding conditions for output qubit  $O$ . Specifically,  $\bar{Z}_{\{2,O\}} = S_{\{2,O\}} \bar{Z}_\Psi = X_I X_2 X_O$  satisfies equation (1) with  $M = \{X_I, X_1, X_2, X_3\}$ , in this case reproducing the measurement pattern provided by graph-pathfinding.

Now consider the stabilizer  $S_{\{1,O\}} = K_1K_O = Z_IX_1Z_2Z_3X_O$ , used to define the logical operator  $\bar{X}_{\{1,O\}} = S_{\{1,O\}}\bar{X}_\Psi = X_1Z_2Z_3X_O$ . In this case  $\bar{X}_{\{1,O\}}$  cannot be paired with any  $\bar{Z}$  to satisfy equation (1) to yield a valid measurement pattern. This can be seen by observing that  $\bar{X}_{\{\underline{1}\}} = X_1Z_2$  is also a valid  $\bar{X}$  operator. Hence, any measurement pattern constructed from  $\bar{X}_{\{1,O\}}$  and some  $\bar{Z}$  must contain measurements  $X_{1}$  and  $Z_{2}$  returning eigenvalues  $\lambda_{X_1}$  and  $\lambda_{Z_2}$  respectively. However,  $\langle X_\Psi \rangle = \langle \bar{X}_{\{1\}} \rangle = \lambda_{X_1}\lambda_{Z_2}$ , showing that after such measurements  $\bar{X}$  has been measured and thus teleportation has failed.

In this last example it is easy to see why  $S_{\{1,O\}}$  cannot be used to generate an  $\bar{X}$  satisfying equation (1) by noting that  $I \in \mathcal{Q}(K_1)$ ,  $O \in \mathcal{Q}(K_O)$  but  $\mathcal{Q}(K_1) \cap \mathcal{Q}(K_O) = \emptyset$ , where  $\mathcal{Q}(A)$  is the set of qubits on which  $A$  non-trivially acts. However it is not always the case that if some set of generators in a stabilizer combination share support then their combination is useful for stabilizer pathfinding. For example, consider applying stabilizer pathfinding to teleportation from  $I$  to  $O$  on star graph state  $|\Psi\rangle$  depicted below:

![](images/d2db53b38cb41595a607bcf092d051d8aacb9bfeb62f50c042e5a029e3caca13.jpg)

$$
\begin{array}{l} \bar {X} _ {\Psi} = Z _ {I} \\ \bar {Z} _ {\Psi} = X _ {I} Z _ {1} \\ \mathcal {G} _ {\Psi} = \left\{Z _ {I} X _ {1} Z _ {2} Z _ {3} Z _ {O}, \quad \left(K _ {1}\right) \right. \\ Z _ {1} X _ {2}, \quad (K _ {2}) \\ Z _ {1} \quad X _ {3} \quad , \quad (K _ {3}) \\ \left. \begin{array}{c c} Z _ {1} & X _ {O} \end{array} \right\} \left(K _ {O}\right) \\ \end{array}
$$

Consider the valid logical operator  $\bar{Z}_{\{2,3,O\}} = S_{\{2,3,O\}}\bar{Z}_{\Psi} = X_I X_2 X_3 X_O$  on  $|\Psi\rangle$ . Here we observe that  $\mathcal{Q}(\bar{Z}_{\{O\}}) \cap \mathcal{Q}(K_2 K_3) = \emptyset$  and therefore  $\bar{Z}_{\{2,3,O\}}$  represents the same logical operation as  $\bar{Z}_{\{O\}} = X_I X_O$  with  $I, O \in \mathcal{Q}(\bar{Z}_{\{O\}})$ . Even though in this case the inclusion of  $K_2$  and  $K_3$  does not prevent  $\bar{Z}_{\{O\}}$  from acting on  $I$  and  $O$ ,  $\bar{Z}_{\{2,3,O\}}$  still cannot be paired with any  $\bar{X}$  that satisfies the stabilizer pathfinding condition. This is seen by observing that any  $\bar{X}$  must be produced using  $K_1$  to ensure  $\{\bar{X}^{[O]}, \bar{Z}^{[O]}\} = 0$ , and so qubits 2 and 3 must be measured in either the  $Z$  or  $Y$  basis. On the other hand, a valid pair of logical operators satisfying equation (1) would be  $\bar{Z}_{\{O\}} = X_I X_O$  with  $\bar{X}_{\{1\}} = X_1 Z_2 Z_3 Z_O$  such that  $M = \{X_I, X_1, Z_2, Z_3\}$ , also reproducing the measurement pattern provided by graph-pathfinding.

From the above examples we have illustrated that while many possible logical operators exist, only a subset can be used to produce valid measurement patterns. Specifically, we have seen that teleportation can be prevented by logical operators which are decomposable into another logical operator (of reduced weight) and a non-overlapping stabilizer. We now introduce definitions to generalise this concept and explicitly specify which stabilizers are useful for teleportation.

# 3.1.2 Trivial and non-trivial stabilizers

Given the correspondence between logical operators and stabilizers, we shall define general conditions on the latter. To distinguish generator combinations that are and aren't useful for teleportation, we define the concepts of non-trivial and trivial combinations, respectively. A trivial stabilizer (produced by a trivial combination) is defined as a stabilizer  $S_{c}$  where there exists some bipartition  $(\alpha ,\beta)$  of  $c$  such that the bipartition's stabilizers do not share support, or

$$
S _ {c} = S _ {\alpha} S _ {\beta} \quad \text {w h e r e} \quad \mathcal {Q} \left(S _ {\alpha}\right) \cap \mathcal {Q} \left(S _ {\beta}\right) = \emptyset . \tag {4}
$$

If, as in the examples above, a logical operator  $\bar{L} \in \mathcal{L}_{\Psi}$  decomposes in a similar way<sup>4</sup> i.e.  $\mathcal{Q}(\bar{L}'S_{\alpha}) \cap \mathcal{Q}(S_{\beta}) = \emptyset$  or  $\mathcal{Q}(\bar{L}'S_{\beta}) \cap \mathcal{Q}(S_{\alpha}) = \emptyset$  for  $\bar{L}' \in \mathcal{L}_{\Psi}$ , then qubits  $I$  and  $O$  must either both be in the support of just one of the partitions or split across both. In such cases,  $\bar{L}$  either has unnecessary measurements that

# TRIVIAL AND NON-TRIVIAL LOGICAL OPERATORS:

Consider the task finding pairs of logical operators  $\mathcal{L}_{\Psi}$  that satisfy the stabilizer pathfinding conditions defined in box 1 for teleportation from qubit  $I$  to  $O$  on  $|\Psi \rangle$ . A logical operator  $\bar{L} \in \mathcal{L}_{\Psi}$  is known as trivial if it can be decomposed into some other lower-weight logical operator  $\bar{L}' \in \mathcal{L}_{\Psi}$  and stabilizer  $S \in S_{\Psi}$  with non-overlapping qubit supports  $\mathcal{Q}(\bar{L}') \cap \mathcal{Q}(S) = \emptyset$ . For trivial  $\bar{L}$ , either

a)  $O\in \mathcal{Q}(S)$  and  $\bar{L}$  cannot be used for teleportation, or  
b)  $O \notin \mathcal{Q}(S)$ , and  $\bar{L}$  contains operators  $S$  unnecessary for teleportation.

Therefore trivial logical operators should not be considered for teleportation. By contrast, non-trivial logical operators are those for which no such decomposition exists and so represent measurements that can produce teleportation.

Box 2: Definitions for trivial and non-trivial logical operators.

can prevent teleportation, or measurements which simply do not help teleport the input state onto  $O$ . The definitions of trivial and non-trivial logical operators are summarised in box 2.

A non-trivial stabilizer (produced by a non-trivial combination) is conversely defined as a stabilizer  $S_{c}$  for which no such bipartition of  $c$  exists, or equivalently  $\mathcal{Q}(S_{\alpha}) \cap \mathcal{Q}(S_{\beta}) \neq \emptyset$  for all possible bipartitions  $(\alpha, \beta)$  of  $c$ . Non-trivial stabilizers produce logical operators that can be used to teleport from  $I$  to  $O$  and do not contain unnecessary measurements. For a given stabilizer state  $|\Psi \rangle$  we denote the subsets of trivial and non-trivial stabilizers as  $S_{\Psi}^{\mathrm{T}}$  and  $S_{\Psi}^{\mathrm{NT}}$  respectively, such that  $S_{\Psi} = S_{\Psi}^{\mathrm{T}} \cup S_{\Psi}^{\mathrm{NT}}$ .

The task of stabilizer pathfinding is therefore to track all of  $S_{\Psi}^{\mathrm{NT}}$  without explicit tracking of  $S_{\Psi}^{T}$  as  $|\Psi\rangle$  is subject to gates, measurements and the addition of new qubits. For each operation  $|\Psi\rangle \mapsto |\Psi'\rangle$ , stabilizer pathfinding must therefore be able to add the set of stabilizers that are newly non-trivial  $S_{\Psi'}^{\mathrm{NT}} \setminus S_{\Psi}^{\mathrm{NT}}$ , remove the set of newly trivial stabilizers  $S_{\Psi'}^{\mathrm{T}} \setminus S_{\Psi}^{\mathrm{T}}$ , and apply an update to any non-trivial stabilizers that remain so.

# 3.2 Tracking non-trivial stabilizers

To simulate the preparation of a quantum state using some Clifford circuit, our algorithm must simulate four operations: i) preparation of qubits in computational basis states  $\{|0\rangle ,|1\rangle \}$ ; ii) the single-qubit Clifford gates  $H$ , and  $S$ ; iii) the two-qubit Clifford CZ gate; and iv) measurements in the computational basis. We also require the algorithm to be described by some small set of update rules, whereby each successive operation is simulated by updating an internal representation of the state (as opposed to rerunning a complete simulation for each new state). A simulation based on update rules is preferred not only for speed but also for practical purposes as it may be implemented in real-time.

# 3.2.1 Adding qubits and acting gates

For appending a single qubit  $|\Psi^{\prime}\rangle = |\Psi \rangle \otimes |0\rangle_{n + 1}$ , the state generators acquire one additional non-trivial stabilizer  $\mathcal{G}_{\Psi^{\prime}} = \mathcal{G}_{\Psi}\cup \{Z_{n + 1}\}$  and so  $S_{\Psi^{\prime}}^{\mathrm{NT}} = S_{\Psi}^{\mathrm{NT}}\cup \{Z_{n + 1}\}$  is updated accordingly.

For the case of applying the single-qubit Clifford gate  $U$

$$
\mathcal {S} _ {\Psi^ {\prime}} = \left\{U S _ {c} U ^ {\dagger} \forall S _ {c} \in \mathcal {S} _ {\Psi} \right\} \tag {5}
$$

In Remark B.1 we also show that the action  $U$  cannot affect the non-triviality of any stabilizer.

For the two-qubit CZ gate, finding  $S_{c}^{\prime} \in S_{\Psi^{\prime}}^{\mathrm{NT}}$  is more involved as new non-trivial and trivial stabilizers may be generated. We provide an example here with the update rule's full description found in Appendix section B.2.2. Consider the following graph state produced by applying  $\mathrm{CZ}_{6,8}$  to the state depicted in figure 1:

![](images/1166e5ad729a2771ba78d63ae874395671a6a600f21f117e22e36ce90d7afef7.jpg)  
Figure 3: The graph state produced by applying  $\mathrm{CZ}_{6,8}$  to the state depicted in figure 1.

$$
\begin{array}{l} \bar {X} = Z _ {I} \\ \bar {Z} = X _ {I} Z _ {1} Z _ {2} Z _ {3} \\ \mathcal {G} _ {\psi} = \left\{Z _ {I} X _ {1} Z _ {4}, \quad Z _ {I} X _ {2} Z _ {5}, \quad Z _ {I} X _ {3} Z _ {6}, \right. \\ Z _ {1} X _ {4} Z _ {7}, \quad Z _ {2} X _ {5} Z _ {8}, \quad Z _ {3} X _ {6} Z _ {8} Z _ {9}, \\ Z _ {4} X _ {7} Z _ {O}, \quad Z _ {5} Z _ {6} X _ {8} Z _ {O}, Z _ {6} X _ {9} Z _ {O}, \\ \left. Z _ {7} Z _ {8} Z _ {9} X _ {O} \right\} \\ \end{array}
$$

where the action of  $\mathrm{CZ}_{6,8}$  has been highlighted and the generators are indexed as before (by the qubit on which the Pauli  $X$  operator acts).

From inspection, it is seen that many stabilizers' triviality are unchanged, for example  $S_{\{5,9\}}' = Z_2X_5Z_6Z_8$ $X_9Z_O$  and  $S_{\{6,O\}}' = Z_3X_6Z_7X_O$ , remain trivial and non-trivial respectively. On the other hand, we see that  $S_{\{6,8\}}' = Z_3Z_5Y_6Y_8Z_9Z_O \in \mathcal{S}_{\Psi'}^{\mathrm{NT}}$ , whereas  $S_{\{6,8\}} = Z_3Z_5X_6X_8Z_9Z_O \in \mathcal{S}_{\Psi}^{\mathrm{T}}$  under bipartition ( $\{6\}, \{8\}$ ). We can also find examples of newly trivial stabilizers, for example  $S_{\{5,6,O\}}' = Z_2Z_3X_5X_6Z_7Z_8X_0 \in \mathcal{S}_{\Psi'}^{\mathrm{T}}$  under bipartition ( $\{5\}, \{6,O\}$ ), whereas  $S_{\{5,6,O\}} = Z_2Z_3X_5X_6Z_7X_0 \in \mathcal{S}_{\Psi}^{\mathrm{NT}}$ .

Although small, low-connectivity graph states are easy to analyse, larger graph states or non-graphical stabilizer states become increasingly difficult with a rapidly growing number of combinations available. Our approach identifies new trivial and non-trivial stabilizers using only information of the stabilizers in  $S_{\Psi}^{\mathrm{NT}}$ . Since there are  $2^{|c|}$  possible bipartitions of any given  $S_{c}$ , when a test of triviality is needed, our method avoids an exhaustive search by identifying a reduced set of bipartitions to be tested. Once all stabilizers with differing triviality have been found, the remaining non-trivial stabilizers can then be simply updated as described by equation (5).

# 3.2.2 Single-qubit measurements

Finally, we consider performing single-qubit Pauli measurements on the state. As with the CZ gate, Pauli measurements may also affect the triviality of a given stabilizer. For example, consider the state produced by measurement of  $Y_{9}$  (followed by applying corrective gates  $S^3$  on qubits 6 and  $O$ ) on the previous state, as depicted below:

![](images/575bc464dd2c2c23f031e629825f3fdabdc9a47040d6590a6625af54e19d8350.jpg)  
Figure 4: The graph state produced by measurement of  $Y_{9}$  on the state depicted in figure 3.

$$
\begin{array}{l} \bar {X} = Z _ {I} \\ \bar {Z} = X _ {I} Z _ {1} Z _ {2} Z _ {3} \\ \mathcal {G} _ {\psi} = \left\{Z _ {I} X _ {1} Z _ {4}, \quad Z _ {I} X _ {2} Z _ {5}, \quad Z _ {I} X _ {3} Z _ {6}, \right. \\ \begin{array}{c c c} Z _ {1} X _ {4} Z _ {7}, & Z _ {2} X _ {5} Z _ {8}, & Z _ {3} X _ {6} Z _ {8} Z _ {O}, \end{array} \\ Z _ {4} X _ {7} Z _ {O}, \quad Z _ {5} Z _ {6} X _ {8} Z _ {O}, Y _ {9}, \\ \left. Z _ {6} Z _ {7} Z _ {8} X _ {O} \right\} \\ \end{array}
$$

where the measurement's action has been highlighted and we have assumed qubit 9 is found in the  $+1$  Y eigenstate.

Again we see that many stabilizers' triviality are unchanged, such as  $S_{\{5,9\}}' = Z_2X_5Z_8Y_9$  and  $S_{\{6,O\}}' = -Z_3X_6Z_7X_8X_O$  as before. Similarly, new non-trivial stabilizers can be found, for example  $S_{\{3,O\}}' = Z_I X_3 Z_7 Z_8 X_O \in S_{\Psi'}^{\mathrm{NT}}$ , whereas before  $S_{\{3,O\}} = Z_I X_3 Z_6 Z_7 Z_8 Z_9 X_O \in S_{\Psi}^{\mathrm{T}}$  under bipartition ( $\{3\}, \{O\}$ ). Lastly, we also find new trivial stabilizers, for example  $S_{\{6,7,8\}}' = Z_3Z_4Z_5Y_6X_7Y_8Z_O \in S_{\Psi'}^{\mathrm{T}}$  under bipartition ( $\{6,8\}, \{7\}$ ), whereas prior to measurement  $S_{\{6,7,8\}} = Z_3Z_4Z_5Y_6X_7Y_8Z_9 \in S_{\Psi}^{\mathrm{NT}}$ . As before, identifying the

full set of stabilizers with triviality changed by measurement is somewhat involved, however our algorithm does achieve this with knowledge of only  $\mathcal{S}_{\Psi}^{\mathrm{NT}}$  and without the need for exhaustive triviality testing.

It must be noted that while we could not find an analytic expression for the worst-case efficiency of our algorithm, it will be highly state-specific and more crucially depend on intermediate states produced during the state's construction. These rules are therefore most efficient for states at or close to their minimal edge representation (or equivalent for non-graph states) [21]. For example, while for a completely connected graph state of  $n$  qubits  $S_{c} \in S_{\Psi}^{\mathrm{T}} \forall |c| \geq 4$ ,  $c$  even,  $2^{n}$  intermediate states must also be constructed and clearly such a construction would be inefficient. In these cases alternative construction strategies should be considered. For example, the previous state can be more efficiently created by first creating a  $n + 1$  star graph state (which is a minimal edge representation of the  $n + 1$  completely-connected graph state), followed by the measurement of the central qubit in the  $Y$  basis. While optimal construction strategies are beyond the scope of this paper, we note that minimum edge representation states are likely to be of interest for MBQC in many scenarios. For a further discussion of ways to increasing the algorithm's efficiency, see section 5.1.

# 3.3 Finding loss-tolerant measurement patterns

Once  $S_{\Psi}^{\mathrm{NT}}$  are known, the set of all non-trivial logical operators  $\mathcal{L}_{\Psi}^{\mathrm{NT}}$  and valid measurement patterns  $\mathcal{M}$  can be found. Our algorithm is designed to produce those  $M$  which can tolerate the most lost first, so that only a fraction of all  $\mathcal{M}$  need be found. This is achieved by grouping  $\mathcal{L}_{\Psi}^{\mathrm{NT}}$  into three sets defined by the Pauli operator on qubit  $O$ , namely  $X_O$ ,  $Y_O$  and  $Z_O$ . Within each group operators are then further sorted into groups of equal weight. All minimum-weight  $M$  are then found by considering pairings of operators taken from the lowest-weight operators in groups where  $\{A_O, B_O\} = 0$ . Higher weight  $M$  can then be iteratively produced by considering pairing between lowest-weight and second-to-lowest-weight groupings, etc.

Once some subset of  $\mathcal{M}$  is known, each  $M$  provides some set of loss-tolerant qubits and hence the set of all qubit loss configurations can be easily found. In practise we find that the majority of loss tolerance is provided by a few low-weight  $M$  that are among the first to be found—see numerical results provided in Appendix C.2. For a more detailed description of the above algorithm, see Appendix B.3.

# 4 Loss tolerance

To assess the loss tolerance of stabilizer pathfinding we compare the performance of GPF and SPF on a selection of graph state channels. Specifically, we consider the five channels depicted in figure 5: the square lattice, hexagonal lattice, triangular lattice, linear crazy graph, and a tree-to-tree graph. The choice of three lattice channels is motivated by their relevance to MBQC architectures; the so-called crazy graph is considered due it's use as a loss-tolerant qubit channel [24] and a tree-to-tree channel because it supports a high number of disjoint paths.

We consider two kinds of loss: heralded and unheralded. Herald ed refers to loss events whose location is known, whereas unheralded to loss events on qubits whose locations are unknown until measurement. Physically, heralded loss occurs when a qubit's existence can be inferred from some non-destructive measurement; for example, measurement of charge in a quantum dot can herald the existence of a spin-encoded qubit without measuring the qubit state. On the other hand, unheralded loss occurs in qubit systems that do not permit such measurements, such as a dual-rail encoded qubit in linear optics where measurements are typically performed using photon detectors which absorb the photons (such as avalanche photodiodes).

Importantly, unheralded loss presents a significant challenge to any MBQC scheme as it necessitates either loss-tolerantly encoded qubits or an architecture that can adapt dynamically to loss events when they occur. However, even in a system with unheralded loss, the performance of SPF under heralded loss provides an upper bound on the loss tolerance of any given channel or teleportation measurement strategy.

![](images/cb0ed85af70a7e70ed97438e2643c077daa0f7e4277d421da1cafa2bdf573878.jpg)  
a) Square Lattice

![](images/680780b19a5a9b623f54b5d860dc303b2b8dce9a3faf7a26b55011dd9e6df805.jpg)  
c) Triangular Lattice

![](images/506fec9810f59837ce55eba6448cdfe5e3a9391069f94be95363a227f85fbf72.jpg)  
e) Tree-to-Tree

![](images/8de3fd83461622377ec20ac9272be27d1ba44aa439ba1073e142ed1fd4b82eef.jpg)  
b) Hexagonal Lattice

![](images/289d6fbd311ed88438738e8d11ee36db5f4f6835f544757cbecffd61bad91783.jpg)  
d) Crazy Graph  
Figure 5: The five graph state channels considered for teleportation. Nodes are coloured by the number of measurement patterns that do not contain them (i.e. tolerant to their loss), with darker nodes indicating their loss can be more readily accommodated.

# 4.1 Heralded loss

Firstly, we consider the performance of SPF in the case of heralded loss. Once a set of measurement patterns for a state is known (be they produced by GPF or SPF), the rate of successful teleportation as a function of per-qubit loss probability can be easily found by Monte Carlo simulation. Specifically, for a single Monte Carlo instance this is achieved by randomly generating some set of lost qubits (at some per-qubit loss rate  $p_l$ ), which is cross-referenced with the set of all measurement patterns to find any pattern that do no include said qubits to allow successful teleportation. In figure 6 we compare the performance of SPF to that of GPF on the five aforementioned channels under heralded loss.

Firstly, it is clear that SPF provides a significant increase in the loss tolerance of teleportation rate  $T$ . As should be expected, GPF has greatest loss tolerance on the tree-to-tree channel and lowest on the crazy graph (where it can tolerate no loss) whereas the converse is true for SPF respectively. For all channels considered, the SPF's gain in loss tolerance peaks above 50%, even for the tree-to-tree channel. Note that the SPF teleportation rate for crazy graph agrees with the theoretical rate $^6$  of  $T = (1 - p_l^m)^n$ , where  $m$  and  $n$  are the number of qubits per column and channel depth respectively (with  $m = n = 4$  in the case considered). We further note that in the low-loss regime for  $p_l < 10\%$  SPF achieves  $T > 95\%$  for all lattice channels and even  $T \approx 1$  for the triangular lattice.

# 4.2 Unheralded loss

We now consider the performance of SPF in the case of unheralded loss. Any practical device that must tolerate unheralded loss during teleportation (without a loss-tolerant encoding) must be able to react to loss events as and when they occur. One method for achieving this is to pre-compile a set of possible measurement patterns  $\mathcal{M}$ , many of which will contain common measurements. Since teleportation can be achieved as long

![](images/ed142ace458d9a2b559e785d4635692d6f042420254fa3d6c83b512a725ece41.jpg)  
Stabilizer pathfinding performance under heralded loss  
Figure 6: The probability of successful teleportation across various graph state channels as a function of heralded qubit loss. Solid lines, dashed lines and shaded regions depict the performance of stabilizer pathfinding (SPF), the graph pathfinding (GPF) heuristic and the difference between them respectively (i.e. SPF's loss tolerance advantage). Each data point depicts  $10^{4}$  Monte Carlo instances and uncertainties have not been plotted as  $\Delta T < 0.5\%$  in all cases and so are smaller than the plotted lines. From these results it is clear that stabilizer pathfinding produces a significant improvement in terms of the loss tolerance of teleportation across these states. Additionally, the loss tolerance provided by SPF for the crazy graph channel agree with the theoretical prediction of  $T = (1 - p_l^m)^n$  for the case of  $n,m = 4$  presented here.

as one valid pattern can be performed that excludes all lost qubits, we require some measurement strategy that finds at least one such measurement pattern with high probability. For demonstrative purposes we only consider a single measurement strategy here, known as max tolerance. In the max tolerance measurement strategy the measurement that occurs most in the set of maximally loss-tolerant patterns is chosen; this process is then repeated until either a valid measurement pattern is completed and teleportation succeeds or none remain and teleportation fails. For further details on this strategy and other considered see Appendix section C.2.

Specifically, at each Monte Carlo simulation instance a set of lost qubits is again generated and qubits are sequentially measured. At each measurement, if the qubit is not lost then the measurement succeeds, and all measurement patterns not containing the measurement are discarded. Conversely, if the measured qubit is lost, all measurement patterns that required measurement of the qubit are discarded. Successful teleportation occurs when a successful measurement completes a measurement pattern, whereas if no patterns remain then teleportation fails.

Our Monte Carlo simulation results, depicted in figure 7, indicates that teleportation is surprisingly resilient to unheralded loss across the channels considered. Immediately, it is clear that the crazy graph channel does not experience any decrease in teleportation rate in the unheralded case. This can be understood by noting that, unlike the other channels considered, the crazy graph is a loss-tolerant encoding of a four qubit linear graph state and is specifically designed to tolerate unheralded loss.

For lattice channels, the disadvantage of unheralded loss decreases with increased node degree. Most importantly, the decrease of  $T$  with unheralded loss is far more favourable for higher degree in the regime of low loss  $p_l < 5\%$ , with the triangular lattice showing only a  $2\%$  decrease in loss tolerance. We finally note that although a fall in  $T$  is observed for unheralded loss, this drop is not as large as might be expected. Most

![](images/78fee46deccdf3a4f0cd1fe05caef45b85892b9703cb51ddc908a85df01615e8.jpg)  
Stabilizer pathfinding performance under unheralded loss  
Figure 7: The probability of successful teleportation across various graph state channels as a function of qubit loss in the heralded and unheralded case. Solid lines, dashed lines and shaded regions depict the performance of stabilizer pathfinding with heralded loss, unheralded loss and the difference between them respectively (i.e. the decrease in loss tolerance due to unheralded loss). Each data point depicts  $10^{4}$  Monte Carlo instances and uncertainties are not depicted as  $\Delta T < 0.5\%$  in all cases and so are smaller than the plotted lines. From these results it is clear that while unheralded loss does reduce the ability to teleport loss-tolerantly on MBQC resource states, high teleportation rates can still be achieved, especially for those lattices with higher degree. We also note that as expected the crazy graph channel does not show any decrease in loss tolerance in the unheralded case, indicating its unique construction as a loss-tolerant teleportation channel.

notably, SPF teleportation on the triangular lattice under unheralded loss performs almost as well as SPF teleportation on the hexagonal lattice under heralded loss (which already marks a significant improvement when compared to teleportation using GPF). Overall, these results present an optimistic outlook on the future of designing loss-tolerant architectures for quantum computation and other quantum technologies based on such states.

# 4.3 Loss tolerance thresholds

One interesting feature of loss tolerance provided by SPF is that  $T(p_{l})$  appears to exhibit threshold behaviour on the lattice channels considered here. We conjecture that such a threshold does exist in the infinite limit, allowing a loss-tolerant threshold  $p_{l}^{*}$  to be defined on these states. If this conjecture holds,  $p_{l}^{*}$  represents a distinct division in loss tolerance in the limit of infinite channel size (where  $n \to \infty$  on an  $n \times n$  lattice), where for  $p_{l} < p_{l}^{*}$  loss-tolerant teleportation can always be achieved, whereas for  $p_{l} > p_{l}^{*}$  it cannot. It is known from percolation theory that the probability of finding a spanning path  $\Gamma$  across some percolated lattice with edge/node percolation rate  $p$  exhibits a threshold at some critical probability  $p = p^{*}$ , which can be found from the stationary point in  $\Gamma(p)$  between finite lattices of various sizes [25].

Figure 8 depicts  $T(p_{l})$  for each lattice channel across lattice sizes  $2 \times 2$ ,  $3 \times 3$  and  $4 \times 4$ , with stationary points found for hexagonal and triangular lattice channels at  $p_{l} \approx 12 - 15\%$  and  $p_{l} \approx 27 - 30\%$  respectively. No clear crossing is observed in the square lattice case. While these results are not conclusive, it is surprising that any crossing points are found given the small lattice sizes considered here as larger systems are usually needed to overcome perturbative boundary effects. In the square lattice case, we conjecture that no crossing occurs because of such boundary effects, given their effect on per-node loss tolerance as depicted in figure

![](images/955544421fb3824414e116826be501b104ecf00f1b44f83aa6e78668560848cd.jpg)  
Figure 8: Loss-tolerant teleportation rates  $T(p_l)$  for the three lattice channels considered: hexagonal, square and triangular over lattice sizes  $2 \times 2$ ,  $3 \times 3$  and  $4 \times 4$  in the case of heralded loss. For the hexagonal and triangular lattice channels, stationary points appear at  $p_l \approx 12 - 15\%$  and  $p_l \approx 27 - 30\%$  respectively, whereas with the square lattice, no single crossing point occurs. If these points can be shown to represent a critical threshold in loss tolerance, then they define the channels' ultimate teleportation loss tolerance in limit of infinite channel size. However,  $T(p_l)$  at higher  $n$  are needed to verify the stationary points to prove such a conjecture.

5. We also note that while the crazy graph lattice does also appear to show threshold behaviour (from the sigmoidal form of its  $T$  curve in figure 6) for some threshold  $p_l < 1$  for the small sizes considered, this is not the case. This is because as  $n \to \infty$  for a  $n \times n$  channel,  $T = \lim_{n \to \infty} ((1 - p_l^n)^n) = 1$  for  $p_l < 1$ , in which case  $p_l^* = 1$ .

# 5 Discussion

We now provide possible optimisations and extensions of SPF and our algorithm as well as a discussion on it's applicability to various quantum architectures.

# 5.1 Optimisations and extensions

Our SPF algorithm allows for optimisation in various situations. Because we have focused on achieving loss tolerance across all possible states, our implementation of SPF necessarily tracked all non-trivial stabilizers, making simulation of over 20 qubit graph states infeasible without significant computational power. However, a more specialised implementation might suffice when applying SPF on a single type of channel, such as one which ignores isomorphic stabilizers on states with high symmetry.

More generally, many non-trivial stabilizers tracked during SPF have high weight and so typically don't contribute to loss-tolerant measurement patterns or to later future low-weight stabilizers as the state is grown. Because only stabilizers of up to  $\left\lfloor \frac{n}{2} \right\rfloor$  generators are needed for triviality tests, all high-weight stabilizers produced from combinations of over  $\left\lfloor \frac{n}{2} \right\rfloor$  generators may be disregarded. For large states this can significantly reduce computational runtime without either causing failure of our SPF algorithm or an appreciable reduction in loss tolerance.

Another route for optimisation and/or extension of SPF is provided by pre-Compilation. In a quantum architecture with probabilistic entangling operations within a fixed network structure, the non-trivial stabilizers for the ideal network may be pre-compiled (as an expensive but one-off computation) so that our algorithm can build down (rather than build up) to the target state. Alternatively, for large, regular graph state lattices, teleportation might be split up into many smaller SPF instances that are concatenated to

produce the required long-range measurement patterns. The challenge here is to ensure consistency across the boundaries between different SPF instances.

Finally, we observe that SPF can be extended to include parity checks for the detection of computational measurement errors. This is seen by noting that each of a state's stabilizers provides a parity check for measurement on the state. Therefore, if a stabilizer can be found whose non-trivial Pauli operators are a subset of the teleportation measurement pattern (or which contains additional available measurements), the operator provides a parity check on measurement outcomes. Combinations of parity checks which overlap on sets of qubits can thus be used to detect Pauli measurement errors, as demonstrated by tolerance of up to a  $50\%$  Pauli  $Z$  error rate on crazy-graph states argued in Ref. [24].

# 5.2 Relevance to quantum architectures

Firstly, our results provide important progress towards addressing the problem of photon loss within linear optical quantum computer. For example, some LOQC architecture proposals [6, 26-28] overcome probabilistic entangling gates by the renormalization of large blocks of percolated graph state to construct 3D topological error correction states such as the Raussendorf lattice [29]. But due their use of GPF for teleportation, these models previously lacked any tolerance to unheralded loss. The loss tolerance thresholds conjectured in section 4.3 indicate that loss tolerance can be straightforwardly achieved in these schemes by replacing GPF with SPF.

More generally, SPF can provide additional loss tolerance within many other quantum architectures without modification, before or after error-correction. For example, given that flow conditions are unaffected by Pauli  $X$ ,  $Y$  and  $Z$  measurements [30], SPF is readily compatible with teleportation in an MBQC architecture. Similarly, because SPF makes no assumptions on the physical encoding of qubits, our work equally extends to teleportation of logical qubits which are encoded for quantum error correction or other reasons. Hence in some systems it may be possible to substitute the resources associated with producing asymptotically-lossless logical qubits with the creation of a larger network of (heralded) low-loss logical qubits on which SPF can be applied.

One further aspect we have not explicitly addressed here is the ability to perform measurement-based qubit gates on top of an SPF teleportation scheme. Unlike GPF, because no linear cluster is directly generated during SPF the standard MBQC gate protocol cannot be directly applied. However, given that at least one unbroken qubit path of  $Y$  and  $X$  measurements must connect the input and output qubits, with all others effectively applying the necessary  $Z$  measurements, it is straightforward to understand how standard MBQC protocols may be similarly implemented. We leave a full description of such a protocol open for future works.

Lastly, it is clear from the results of section 4 that higher-degree graph states seem to provide a greater degree of loss tolerance in both the heralded and unheralded case. As such, it is an open question whether this result generalises for arbitrary  $n$ -degree random graphs or lattices. The identification of such a dependence would provide an important insight into the design of future network architectures.

# 6 Conclusion and outlook

Qubit loss presents a substantial roadblock to the realistic implementation of teleportation within many large-scale quantum technologies, such as LOQC and quantum communication networks. Previously, this could only be generally addressed through costly loss-tolerant encodings, especially so when qubit loss is unheralded. However, by applying a generalised approach to teleportation, SPF, our work provides losstolerant teleportation on any stabilizer state using only single-qubit Pauli measurements and feed-forward. We have show that SPF provides all maximally loss-tolerant teleportation measurement patterns (when loss is heralded) without use of an exhaustive search. Furthermore we have shown that SPF also allows for significant degrees of unheralded qubit loss to be tolerated by dynamic and computationally-inexpensive measurement strategies.

In addition to theoretical analysis, we have provided an algorithm that implements SPF as well as unheralded measurement strategies which incur minimal computational cost. Based on numerical simulations of SPF, we have further conjectured the existence of loss-tolerant thresholds on a variety of graph state lattices that exist in the limit of infinite lattice size. From a practical perspective our results provide both a novel technique for tolerating loss in large-scale quantum architectures as well as a tool for maximal use of so-called noisy intermediate-scale quantum (NISQ) devices in the near future [31].

# References

1. Pirandola, S., Eisert, J., Weedbrook, C., Furusawa, A. & Braunstein, S. L. "Advances in quantum teleportation". Nature Photonics 9, 641-652 (2015).  
2. Kimble, H. J. "The quantum internet". Nature 453, 1023-1030 (2008).  
3. Epping, M., Kampermann, H. & Bruß, D. "Large-scale quantum networks based on graphs". New Journal of Physics 18, 053036 (2016).  
4. Simon, C. "Towards a global quantum network". Nature Photonics 11, 678-680 (2017).  
5. Das, S., Khatri, S. & Dowling, J. P. "Robust quantum network architectures and topologies for entanglement distribution". Physical Review A 97, 012335 (2018).  
6. Gimeno-Segovia, M., Shadbolt, P., Browne, D. E. & Rudolph, T. "From Three-Photon Greenberger-Horne-Zeilinger States to Ballistic Universal Quantum Computation". Physical Review Letters 115, 020502 (2015).  
7. Raussendorf, R. & Briegel, H. J. “A One-Way Quantum Computer”. Physical Review Letters 86, 5188-5191 (2001).  
8. Raussendorf, R., Browne, D. E. & Briegel, H. J. "Measurement-based quantum computation on cluster states". Physical Review A 68, 022312 (2003).  
9. Gross, D. & Eisert, J. "Quantum computational webs". Physical Review A 82, 040303 (2010).  
10. Azuma, K., Tamaki, K. & Lo, H.-K. "All-photonic quantum repeaters". Nature Communications 6, 6787 (2015).  
11. Knill, E., Laflamme, R & Milburn, G. J. "A scheme for efficient quantum computation with linear optics." Nature 409, 46-52 (2001).  
12. Kok, P. et al. "Linear optical quantum computing with photonic qubits". Reviews of Modern Physics 79, 135-174 (2007).  
13. Li, Y., Humphreys, P. C., Mendoza, G. J. & Benjamin, S. C. "Resource Costs for Fault-Tolerant Linear Optical Quantum Computing". Physical Review X 5, 041007 (2015).  
14. Stace, T. M., Barrett, S. D. & Doherty, A. C. "Thresholds for topological codes in the presence of loss". Physical Review Letters 102, 1-4 (2009).  
15. Varnava, M., Browne, D. E. & Rudolph, T. "Loss tolerance in one-way quantum computation via counterfactual error correction". Physical Review Letters 97, 120501 (2005).  
16. Varnava, M., Browne, D. E. & Rudolph, T. "Loss tolerant linear optical quantum memory by measurement-based quantum computing". New Journal of Physics 9, 203-203 (2007).  
17. Varnava, M., Browne, D. E. & Rudolph, T. "How Good Must Single Photon Sources and Detectors Be for Efficient Linear Optical Quantum Computation?" Physical Review Letters 100, 060502 (2008).  
18. Campbell, E. T. & Benjamin, S. C. “Measurement-Based Entanglement under Conditions of Extreme Photon Loss”. Physical Review Letters 101, 130502 (2008).  
19. Hein, M. et al. "Entanglement in Graph States and its Applications". arXiv preprint. arXiv: 0602096 [quant-ph] (2006).

20. Gottesman, D. "Stabilizer Codes and Quantum Error Correction". arXiv: 9705052 [quant-ph] (1997).  
21. Hein, M., Eisert, J. & Briegel, H. J. "Multiparty entanglement in graph states". Physical Review A 69, 062311 (2004).  
22. Van den Nest, M., Dehaene, J. & De Moor, B. "Graphical description of the action of local Clifford transformations on graph states". Physical Review A 69, 022316 (2004).  
23. Anders, S. & Briegel, H. J. "Fast simulation of stabilizer circuits using a graph-state representation". Physical Review A 73, 022334 (2006).  
24. Rudolph, T. "Why I am optimistic about the silicon-photonic route to quantum computing". *APL Photonics* 2, 030901 (2017).  
25. Stauffer, D. & Aharony, A. Introduction to percolation theory (Taylor & Francis, 1994).  
26. Kieling, K., Rudolph, T. & Eisert, J. "Percolation, Renormalization, and Quantum Computing with Nondeterministic Gates". Physical Review Letters 99, 130501 (2007).  
27. Zaidi, H. A., Dawson, C., van Loock, P. & Rudolph, T. "Near-deterministic creation of universal cluster states with probabilistic Bell measurements and three-qubit resource states". Physical Review A 91, 042301 (2015).  
28. Morley-Short, S. et al. "Physical-depth architectural requirements for generating universal photonic cluster states". Quantum Science and Technology 3, 015005 (2018).  
29. Raussendorf, R., Harrington, J. & Goyal, K. "A fault-tolerant one-way quantum computer". Annals of Physics 321, 2242-2270 (2006).  
30. Browne, D. E., Kashefi, E., Mhalla, M. & Perdrix, S. "Generalized flow and determinism in measurement-based quantum computation". New Journal of Physics 9, 250-250 (2007).  
31. Preskill, J. "Quantum Computing in the NISQ era and beyond". arXiv: 1801.00862 (2018).

# Acknowledgements

This work was supported by the UK Engineering and Physical Sciences Research Council (EPSRC). SMS is supported by the Bristol Quantum Engineering Centre for Doctoral Training, EPSRC grant EP/L015730/1. SMS would like to thank Eric Johnston, Will McCutcheon, Stasja Stanisic, Sam Pallister, Chris Sparrow and Naomi Nickerson for fruitful discussions. Finally, we thank two anonymous referees for their constructive comments and feedback. All simulation code, data and analysis scripts are available for download and use at https://github.com/sammorley-short/spf.

# Appendices

The appendix is structured as follows. Appendix A gives an introduction to the stabilizer formalism and stabilizer states. Appendix B provides a complete description of the SPF algorithm, including necessary proofs and pseudocode. Finally, Appendix C presents a number of further results and discussion of the SPF algorithm.

# Appendix A Stabilizer states

Below we review the necessary theoretical results on which our work relies, namely the stabilizer formalism, graph states, and a generalised teleportation.

In the stabilizer formalism [20], for any given state  $|\Psi \rangle$  there exists an associated stabilizer group  $S_{\Psi}$ , consisting of the set of all operators that leave  $|\Psi \rangle$  unchanged, such that

$$
\mathcal {S} _ {\Psi} = \left\{S _ {i}: S _ {i} | \Psi \rangle = | \Psi \rangle \right\}. \tag {6}
$$

A state's stabilizer group is closed under multiplication, i.e. the product of any two stabilizers  $S_{i}$  and  $S_{j}$  is itself a stabilizer. Furthermore, any state can be defined by a set of stabilizer generators  $\mathcal{G}_{\Psi}$ , which generates the group under multiplication, which we write as  $S_{\Psi} = \langle \mathcal{G}_{\Psi}\rangle$ .

Stabilizer states are further defined as a subset of the  $n$ -qubit states that can be efficiently described by a set of  $n$  stabilizer generators

$$
\mathcal {G} _ {\Psi_ {S}} = \left\{K _ {i}: K _ {i} \mid \Psi_ {S} \right\rangle = \left| \Psi_ {S} \right\rangle , K _ {i} \in \mathcal {P} _ {n}, i = 1, \dots , n \rbrace \tag {7}
$$

where  $\mathcal{P}_n$  is the group of  $n$ -fold tensor products of Pauli operators  $\mathbb{I}$ ,  $X$ ,  $Y$  and  $Z$  up to multiplicative phase factors  $\pm 1$  and  $\pm i$  and hence  $\mathcal{S}_{\Psi} \subset \mathcal{P}_n$ . Specifically, stabilizer states are those produced by any stabilizer circuit which consists of only: i) preparation of qubits in computational basis states  $\{|0\rangle, |1\rangle\}$ ; ii) quantum gates from the Clifford group $^7$ $\mathcal{C} = \{H, S, CZ\}$ ; and iii) measurements in the computational basis. The Gottesman-Knill theorem [20] states that any such circuit can be simulated efficiently on a classical computer.

Stabilizer circuits include many that exhibit rich and canonically "quantum" phenomena such as superposition and entanglement, including the generation of large multipartite entangled states. For such states, many correlations between measurement outcomes exist across the whole state, a fact that allows them to be used as quantum error correction codes [20]. Just as all correlations present in a state are represented in it's state vector, they are equally present in a state's stabilizers.

One can intuitively interpret the set of stabilizer generators  $\mathcal{G}_{\Psi}$  as the minimal representation of the quantum correlations for  $|\Psi\rangle$ . For example, consider the Bell state  $|\Phi^{+}\rangle$

$$
\left| \Phi^ {+} \right\rangle = \frac {1}{\sqrt {2}} \left(\left| 0 0 \right\rangle + \left| 1 1 \right\rangle\right) = \frac {1}{\sqrt {2}} \left(\left| + + \right\rangle + \left| - - \right\rangle\right) = \frac {1}{\sqrt {2}} \left(\left| + i - i \right\rangle + \left| - i + i \right\rangle\right), \tag {8}
$$

where  $|\pm \rangle = \frac{1}{\sqrt{2}} (|0\rangle \pm |1\rangle)$  and  $|\pm i\rangle = \frac{1}{\sqrt{2}} (|0\rangle \pm i|1\rangle)$ . By noting that  $|\Phi^{+}\rangle = H_{1}\mathrm{CZ}_{1,2}H_{1}H_{2}|00\rangle$  it is easy to show that  $\mathcal{S}_{\Phi^{+}} = \{X_{1}X_{2},Z_{1}Z_{2}, - Y_{1}Y_{2}\} = \langle \mathcal{G}_{\Phi^{+}}\rangle = \langle X_{1}X_{2},Z_{1}Z_{2}\rangle$ , where  $A_{i}$  represents the operator that enacts unitary  $A$  on qubit  $i$  and  $\mathbb{I}$  everywhere else and similarly  $A_{i,j}$  for two-qubit gates. In this example it is clear that the stabilizers have provided the set all of correlations between single-qubit measurements on  $|\Phi^{+}\rangle$ , namely that the possible eigenvalues returned from measurements of both qubits in the  $X$  and  $Z$  basis are correlated ( $\lambda_{X_1}\lambda_{X_2} = \lambda_{Z_1}\lambda_{Z_2} = 1$ ), whereas the possible eigenvalues found for  $Y$  measurements are anti-correlated ( $\lambda_{Y_1}\lambda_{Y_2} = -1$ ).

Just as the action of unitary operators evolve a state's quantum state vector in the Schrödinger picture, a state's stabilizers are equivalently evolved within the Heisenberg picture [20]. The action of any Clifford gate unitary  $U$  on a state  $|\Psi\rangle$  therefore transforms  $S_{\Psi}$  as follows:

$$
\left| \Psi \right\rangle \xrightarrow {U} \left| \Psi^ {\prime} \right\rangle \quad \Leftrightarrow \quad \mathcal {S} _ {\Psi} \xrightarrow {U} \mathcal {S} _ {\Psi^ {\prime}} = \left\{S _ {i} ^ {\prime} = U S _ {i} U ^ {\dagger}: S _ {i} \in \mathcal {S} _ {\Psi} \right\} = \left\langle K _ {i} ^ {\prime} = U K _ {i} U ^ {\dagger}: K _ {i} \in \mathcal {G} _ {\Psi} \right\rangle . \tag {9}
$$

The effect of Pauli measurement operator  $M \in \mathcal{P}_n$  on a state  $|\Psi \rangle$  can also be represented by updating the stabilizer generators  $\mathcal{G}_{\Psi}$ . For any  $M$  there are two cases: either  $M$  commutes with all of the state's stabilizers, or  $M$  anti-commutes with one or more of them. In the first case it is easy to show that either  $M$  or  $-M \in S_{\Psi}$ , and hence  $|\Psi \rangle$  is an eigenstate of  $M$  and so unaffected by the measurement. However, in the latter case, the measurement  $M$  will change the state. In the case that the measurement  $M$  returns an eigenvalue of  $+1$ , the stabilizers are updated as follows:

1. Pick a  $K_{a}\in \mathcal{G}_{\Psi}$  such that  $\{M,K_a\} = 0$  . Replace  $K_{a}$  with  $M$  
2. For all other  $K_{i}\in \mathcal{G}_{\Psi}\backslash \{M\}$

(a) If  $[M, K_i] = 0$ , leave  $K_i$  unchanged  
(b) If  $\{M, K_i\} = 0$ , replace  $K_i$  with  $K_aK_i$ .

In the case that  $M$  returns eigenvalue  $-1$ , the same process is applied, except  $M \mapsto -M$  [20].

If the number of stabilizer generators on an  $n$ -qubit state  $|\Psi \rangle$  is reduced from  $n$ ,  $\mathcal{G}_{\Psi}$  no longer defines a single state, but rather a subspace of states. A set of logical basis states can be defined on this subspace together with logical operators that satisfy Pauli relations, thus creating an encoded logical qubit. While such constructions are commonly applied to design quantum error correcting codes, their application can be applied to other quantum information protocols, such as quantum teleportation.

In our case, we are specifically interested in the complete set of logical operators for a qubit input into some Clifford circuit  $U$  (with some set of input ancillae qubits). For example, consider an unknown state  $|\psi \rangle_I$  of a single input qubit  $I$  with logical operators  $\bar{X}_{\psi} = X_I$  and  $\bar{Z}_{\psi} = Z_I$ , which is then encoded via  $|\Psi \rangle = U(|\psi \rangle_I \otimes |0\rangle^{\otimes n})$ , such that

$$
\bar {X} _ {\Psi} = U X _ {I} U ^ {\dagger}, \quad \bar {Z} _ {\Psi} = U Z _ {I} U ^ {\dagger} \quad \text {a n d} \quad \mathcal {G} _ {\Psi} = \left\{U Z _ {i} U ^ {\dagger} \right\} _ {i = 1} ^ {n} \tag {10}
$$

However, after encoding there are many other valid logical operators, as the product of a logical operator and stabilizer is also a valid logical operator. Hence, the set of all logical operators for our encoded qubit is given by

$$
\mathcal {L} _ {\Psi} = i ^ {k} \times \left\{S \bar {L} _ {\Psi}: S \in \mathcal {S} _ {\Psi}, \bar {L} _ {\Psi} \in \left\{\bar {X} _ {\Psi}, \bar {Z} _ {\Psi}, \bar {Y} _ {\Psi} \right\} \right\} \tag {11}
$$

where  $i^k = \{1, -1, i, -i\}$  and  $\bar{Y}_{\Psi} = i\bar{X}_{\Psi}\bar{Z}_{\Psi}$ . Formally,  $\mathcal{L}_{\Psi}$  is the centralizer subgroup of operators in  $\mathcal{P}_n$  which commute with the stabilizers of  $|\Psi\rangle$ . Just as with stabilizers, the logical operators are similarly updated after a measurement  $M$ . If  $[\bar{L}, M] = 0$  for  $\bar{L} \in \mathcal{L}_{\Psi}$ , then  $\bar{L}$  is unchanged, otherwise the logical operators are transformed by  $\bar{L} \mapsto \bar{L}' = K_a\bar{L}$ .

# Appendix B Algorithm details

Here we present a full description of the update rules applied in our algorithm to achieve stabilizer pathfinding. First, we provide an algorithm that allows for stabilizers' and generators' triviality to be more efficiently tested. Secondly, we provide update rules to track a state's stabilizers for any Clifford circuit. Finally, we present a method for combining said stabilizers to produce valid teleportation measurement patterns. The summary pseudocode for the above algorithms are also presented in algorithm 1.

# B.1 Triviality tests

# B.1.1 Testing stabilizers' triviality

As part of the algorithm we shall describe, it will be necessary to remove some unknown trivial stabilizers, namely after applying a CZ or measurement. In the general case of deciding whether some arbitrary stabilizer  $S_{c}$  is trivial or not, given only  $\mathcal{G}_{\Psi}$ , the authors could not improve on a limited exhaustive search. In this case, the space of all bipartitions is explored by finding  $\mathcal{B}_c = \{S_b : b \in \mathcal{P}(c), |b| \leq \lfloor c / 2 \rfloor\}$ , where  $\mathcal{P}(c)$  is the power set of  $c$  and  $\{b : |b| \leq \lfloor c / 2 \rfloor\}$  being the set of all smaller halves of every possible bipartition of  $c$ . For each element of  $\mathcal{B}$ ,  $S_{b}S_{c}$  is found and if  $\mathcal{Q}(S_bS_c) \cap \mathcal{Q}(S_b) = \emptyset$ , then  $(b, c \setminus b)$  describes a trivial bipartition of  $S_{c}$ . If no such  $b$  is found, then  $S_{c}$  must be non-trivial. Clearly this method—which we refer to as single-shot triviality testing—becomes inefficient for large  $|c|$ .

However, a significantly faster triviality test can be performed within the context of our stabilizer pathfinding algorithm. Consider the case where you have a large set of stabilizers  $S_{\Psi}^{*}$ , some of which are trivial  $\mathcal{S}_{\Psi}^{t} \subseteq \mathcal{S}_{\Psi}^{T}$ , but which is otherwise guaranteed to contain all non-trivial stabilizers, such that  $\mathcal{S}_{\Psi}^{*} = \mathcal{S}_{\Psi}^{t} \cup \mathcal{S}_{\Psi}^{\mathrm{NT}}$ . The task is then to extract  $\mathcal{S}_{\Psi}^{\mathrm{NT}}$  by removal of  $\mathcal{S}_{\Psi}^{t}$  without an exhaustive search. To do so, initially consider testing a single  $S_{c} \in S_{\Psi}^{*}$  for triviality. If  $S_{c}$  is trivial, there must exist some minimal bipartition  $(\alpha, \beta)$  of  $c$  such that either  $S_{\alpha}$  and/or  $S_{\beta}$  are non-trivial. Since  $\mathcal{S}_{\Psi}^{\mathrm{NT}} \subseteq \mathcal{S}_{\Psi}^{*}$ , any such bipartitions can be identified by finding  $\mathcal{B}_{c}^{*} = \{S_{\beta}: \beta \subset c, |\beta| \leq \lfloor c / 2 \rfloor, S_{\beta} \in \mathcal{S}_{\Psi}^{*}\}$  and then tested using the same process as single-shot triviality testing<sup>8</sup>. By repeating all  $S_{c} \in \mathcal{S}_{\Psi}^{*}$  and removing any that fail,  $\mathcal{S}_{\Psi}^{\mathrm{NT}}$  can be found with less than  $\mathcal{O}(|\mathcal{S}_{\Psi}^{*}|^{2})$  tests (and far fewer in practise). We shall refer to this type of triviality testing as batch triviality testing.

# B.1.2 Testing generators' triviality

In rare cases, single-qubit measurements can cause generators themselves to become trivial. As triviality of stabilizers is assessed under the assumption of generator non-triviality, these trivial generators must be detected and replaced, in a process known as generator detrivialisation. Specifically, we consider the case when there exists some generator  $K_{a}$  and stabilizer  $S_{b}$  for  $a \notin b$  such that  $\mathcal{Q}(K_aS_b) \cap \mathcal{Q}(S_b) = \emptyset$  (recall that  $\mathcal{Q}(A)$  is the set of qubits on which  $A$  non-trivially acts).

For example, consider the 5-qubit stabilizer state  ${}^{9}|\Psi \rangle$  that undergoes measurement  ${X}_{4}$  as follows:

$$
\begin{array}{l} \bar {X} _ {\Psi} = Z _ {0} \quad \bar {X} _ {\Psi} = Z _ {0} \\ \bar {Z} _ {\Psi} = X _ {0} \quad Z _ {3} Z _ {4} \quad \bar {Z} _ {\Psi} = X _ {0} X _ {1} X _ {2} \\ \mathcal {G} _ {\Psi} = \left\{ \begin{array}{c c} X _ {1} & X _ {2} \\ & Z _ {3} \\ & (X _ {4}) \end{array} , \quad (K _ {1}) \right. \quad \text {M e a s u r e} X _ {4}, \quad \mathcal {G} _ {\Psi} = \left\{ \begin{array}{c c} & X _ {4}, \quad (K _ {1}) \\ & Z _ {3} \\ & (X _ {4}) \end{array} \right. \\ \begin{array}{c c c c} & Z _ {1} Z _ {2} & , (K _ {2}) \\ & Z _ {0} & Z _ {2} X _ {3} & , (K _ {3}) \end{array} \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad Z _ {1} Z _ {2} & , (K _ {2}) \\ & Z _ {0} & Z _ {2} X _ {3} & , (K _ {3}) \end{array} \\ Z _ {0} Z _ {1} \quad \left. \left(X _ {4} \right\} \left(K _ {4}\right) \right. \quad Z _ {0} Z _ {1} \quad \left. \left. \left. \left. \left(K _ {4}\right) \right. \right. \right. \right\} \\ \end{array}
$$

Here we observe that after measurement  $K_{3} = Z_{0}Z_{2}X_{3}$ , whereas  $S_{\{2,3,4\}} = X_{3}$  and so  $K_{3}$  is now trivial (or equivalently that  $\mathcal{Q}(S_{\{2,3,4\}}) \cap \mathcal{Q}(S_{\{2,4\}}) \neq \emptyset$  before the measurement whereas  $\mathcal{Q}(S_{\{2,3,4\}}) \cap \mathcal{Q}(S_{\{2,4\}}) = \emptyset$  after). To ensure all generators are non-trivial they are updated such that  $K_{3}' = K_{2}K_{3}K_{4} = X_{3}$  and  $K_{i}' = K_{i}$  otherwise.

However, because each stabilizer's combination now represents a different set of generators, this update can change bipartitions' support overlaps and so updating the set of non-trivial stabilizers is more involved. Firstly, stabilizers that do not contain the updated generator are unaffected, such that  $S_c' = S_c$  for  $a \notin c$  and hence their triviality is also unchanged. However, during detrivialisation previously trivial stabilizers  $S_c$  may become non-trivial  $S_c'$  if  $a \in c$ . To find all newly non-trivial stabilizers, all stabilizer pairs  $S_\alpha, S_\beta \in S_\Psi^{\mathrm{NT}}$ ,  $\alpha \cap \beta = \emptyset$  where

$$
\mathcal {Q} \left(S _ {\alpha}\right) \cap \mathcal {Q} \left(S _ {\beta}\right) = \emptyset \quad \text {b u t} \quad \mathcal {Q} \left(S _ {\alpha} ^ {\prime}\right) \cap \mathcal {Q} \left(S _ {\beta} ^ {\prime}\right) \neq \emptyset . \tag {12}
$$

are found and  $S_{\alpha \cup \beta}^{\prime}$  added to  $S_{\Psi^{\prime}}^{\mathrm{NT}}$ . This process is then repeated on the newly non-trivial stabilizers found to ensure all previously trivial tripartitions, etc. are found. Finally, any trivial stabilizers are then removed by applying a batch triviality test on all stabilizers  $S_c^\prime \in S_{\Psi '}^{\mathrm{NT}}$  with  $a\in c$ .

We lastly note that trivial generators are an unavoidable by-product of the multiplication of generators performed after measurement and hence is never required after any unitary operation.

# B.2 SPF Part 1: Tracking all non-trivial stabilizers

Stabilizer pathfinding must track the action of the three elements of any Clifford circuit, namely:

i) preparation of qubits in computational basis states  $\{|0\rangle, |1\rangle\}$ ;  
ii) quantum gates from the Clifford group  $\mathcal{C} = \{H, S, CZ\}$ ; and  
iii) measurements in the computational basis,

on the state's non-trivial combinations  $S_{\Psi}^{\mathrm{NT}}$ . We shall define the action of these operations as a series of set update rules using the convention  $A_{\Psi}\mapsto A_{\Psi '}$

# B.2.1 Single-qubit gates

Firstly, consider appending qubit  $|0\rangle_{n + 1}$  to  $|\Psi_S\rangle$ . The stabilizer generators are simply updated by

$$
\mathcal {G} _ {\Psi} \mapsto \mathcal {G} _ {\Psi^ {\prime}} = \mathcal {G} _ {\Psi} \cup \{K _ {n + 1} \}, \tag {13}
$$

where  $K_{n + 1} = Z_{n + 1}$ . Since  $\mathcal{Q}(K_{n + 1}) \cap \mathcal{Q}(K_i) = \emptyset$  for all  $K_i \in \mathcal{G}_{\Psi}$ , there is only a single new non-trivial combination, namely  $\{n + 1\}$ , and hence the non-trivial stabilizers are similarly updated by

$$
\mathcal {S} _ {\Psi} ^ {\mathrm {N T}} \mapsto \mathcal {S} _ {\Psi^ {\prime}} ^ {\mathrm {N T}} = \mathcal {S} _ {\Psi} ^ {\mathrm {N T}} \cup \{S _ {\{n + 1 \}} \} \tag {14}
$$

Next, consider the action of quantum gates from  $\mathcal{C}$  on an  $n$ -qubit stabilizer state. As defined in section A, when acted on by  $U \in \mathcal{C}$  the stabilizer generators are simply updated as in equation (9), or

$$
\mathcal {G} _ {\Psi} \mapsto \mathcal {G} _ {\Psi^ {\prime}} = \left\{K _ {i j} ^ {\prime} \right\} _ {i = 1} ^ {n} = \left\{U K _ {i} U ^ {\dagger} \right\} _ {i = 1} ^ {n}, \tag {15}
$$

where  $K_{i} \in \mathcal{G}_{\Psi} \forall i$ . In the case of a single-qubit Clifford gate  $U \in \{H, S\}$ , it is simple to show that all non-trivial stabilizers can be similarly updated via

$$
\mathcal {S} _ {\Psi} ^ {\mathrm {N T}} \mapsto \mathcal {S} _ {\Psi^ {\prime}} ^ {\mathrm {N T}} = \left\{S _ {c} ^ {\prime} \right\} = \left\{U S _ {c} U ^ {\dagger} \right\}. \tag {16}
$$

Importantly, for the above statement to hold, it must also true that all non-trivial stabilizers remain nontrivial after applying  $U$  and similarly for those that are trivial. This requirement is shown to hold in the following Remark.

Remark B.1. If before the action of a single-qubit Clifford gate  $U$  a stabilizer is trivial (non-trivial),  $S_{c} \in S_{\Psi}^{\mathrm{T}}(S_{\Psi}^{\mathrm{NT}})$ , then after  $U$  it remains trivial (non-trivial),  $S_{c}^{\prime} \in S_{\Psi^{\prime}}^{\mathrm{T}}(S_{\Psi^{\prime}}^{\mathrm{NT}})$ .

Proof. Firstly, we consider the case of a trivial stabilizer  $S_{c}$ . If  $S_{c} \in S_{\Psi}^{\mathrm{T}}$ , there exists a trivial bipartition  $(\alpha, \beta)$  of  $c$  such that

$$
S _ {c} = S _ {\alpha} S _ {\beta} = \prod_ {i \in \alpha} K _ {i} \prod_ {j \in \beta} K _ {j} \quad \text {a n d} \quad \mathcal {Q} \left(S _ {\alpha}\right) \cap \mathcal {Q} \left(S _ {\beta}\right) = \emptyset . \tag {17}
$$

Without loss of generality, assume  $\mathcal{Q}(U) \subseteq \mathcal{Q}(S_{\alpha})$  (since  $|\mathcal{Q}(U)| = 1$ ). From equation (15), then  $S_{\alpha}^{\prime} = US_{\alpha}U^{\dagger}$  and  $S_{\beta}^{\prime} = US_{\beta}U^{\dagger} = S_{\beta}$ . Finally, since  $\mathcal{Q}(S_{\alpha}^{\prime}) = \mathcal{Q}(US_{\alpha}U^{\dagger}) = \mathcal{Q}(S_{\alpha})$ , then from equation (17),  $\mathcal{Q}(S_{\alpha}^{\prime}) \cap \mathcal{Q}(S_{\beta}^{\prime}) = \emptyset$  and hence  $(\alpha, \beta)$  is also a trivial bipartition of  $c$  after  $U$ , showing that  $S_{c}^{\prime} \in S_{\Psi^{\prime}}^{\mathrm{T}}$ . Secondly, in the non-trivial case, the above proof can be easily inverted to show that if after  $U$ ,  $S_{c}^{\prime} \in S_{\Psi^{\prime}}^{\mathrm{T}}$ , then  $S_{c}$  must also admit a trivial bipartition, and hence  $S_{c} \notin S_{\Psi}^{\mathrm{NT}}$ . It follows that  $S_{c} \in S_{\Psi}^{\mathrm{NT}} \Rightarrow S_{c}^{\prime} \in S_{\Psi^{\prime}}^{\mathrm{NT}}$ .

□

# B.2.2 Two-qubit gates

Now consider the  $\mathrm{CZ}_{u,v}$  gate applied to qubits  $u$  and  $v$ . For  $\mathrm{CZ}_{u,v}$  the stabilizer generators are similarly updated using equation (15), however it is also possible that new non-trivial stabilizers are produced and/or previously non-trivial stabilizers are made trivial. In general, this will cause the number of non-trivial stabilizers to change, for example,  $\mathcal{S}_{\Psi}^{\mathrm{NT}} = \{X_1,X_2\}$  for the empty two-qubit graph state, whereas  $\mathcal{S}_{\Psi'}^{\mathrm{NT}} = \{X_1Z_2,Z_1X_2,Y_1Y_2\}$  after  $\mathrm{CZ}_{1,2}$  is applied. Since the effect of  $\mathrm{CZ}_{u,v}$  on any  $K_{i}$  may either increase or decrease  $|\mathcal{Q}(K_i)|$  there are two cases that must be considered for stabilizer pathfinding: either stabilizers that go from i) non-trivial to trivial or ii) trivial to non-trivial. A method for efficiently updating  $\mathcal{S}_{\Psi}^{\mathrm{NT}}$  is now presented below.

First we address i), the case of  $\mathrm{CZ}_{u,v}$  causing previously non-trivial stabilizers to become trivial, where for some stabilizer initially  $S_{c} \in S_{\Psi}^{\mathrm{NT}}$  but  $S_{c}^{\prime} \in S_{\Psi^{\prime}}^{\mathrm{T}}$  afterwards. Given  $\mathrm{CZ}_{u,v}$  can change the qubit support of any stabilizer  $S_{i}$  by at most a single qubit  $u$  or  $v$  then it must be true for  $S_{c} \in S_{\Psi}^{\mathrm{NT}}$  that there exists some bipartition  $(\alpha, \beta)$  of  $c$  such that

$$
\mathcal {Q} \left(S _ {\alpha}\right) \cap \mathcal {Q} \left(S _ {\beta}\right) \subseteq \{u, v \} \tag {18}
$$

$$
\text {b u t} \quad \mathcal {Q} \left(S _ {\alpha} ^ {\prime}\right) \cap \mathcal {Q} \left(S _ {\beta} ^ {\prime}\right) = \emptyset \tag {19}
$$

where  $S_{\alpha}, S_{\beta} \in S_{\Psi}^{\mathrm{NT}}$ . Since  $S_{\Psi}^{\mathrm{NT}}$  is known, finding  $(\alpha, \beta)$  requires finding  $S_{\alpha}, S_{\beta} \in S_{\Psi}^{\mathrm{NT}}$  where the decrease in support of  $S_{\alpha}$  and  $S_{\beta}$  is exactly equal to the previous support overlap between them.

Next we consider ii), the case of  $\mathrm{CZ}_{u,v}$  causing previously trivial stabilizers to become non-trivial, where for some stabilizer initially  $S_{c} \in S_{\Psi}^{\mathrm{T}}$  but after  $S_{c}^{\prime} \in S_{\Psi^{\prime}}^{\mathrm{NT}}$ . For this case, an initial search must be performed to find some bipartition  $(\alpha, \beta)$  for which

$$
\mathcal {Q} \left(S _ {\alpha}\right) \cap \mathcal {Q} \left(S _ {\beta}\right) = \emptyset \tag {20}
$$

$$
\text {b u t} \quad \mathcal {Q} \left(S _ {\alpha} ^ {\prime}\right) \cap \mathcal {Q} \left(S _ {\beta} ^ {\prime}\right) \subseteq \{u, v \} \tag {21}
$$

where  $S_{\alpha}, S_{\beta} \in S_{\Psi}^{\mathrm{NT}}$ . Similarly to i), this can only be achieved if the increase in support is equal to the new support overlap. While equation (21) is a necessary condition for non-triviality, it is not sufficient as it must also hold across all possible bipartitions. In some cases it may be simultaneously possible to find two bipartitions of  $c$ , with one  $(\alpha, \beta)$  satisfying equations (20) and (21) and another  $(\gamma, \delta)$  that does not. Fortunately, these cases can be easily detected and there are three possible variants:

a)  $\mathcal{Q}(S_{\gamma}^{\prime})\cap \{u,v\} = \mathcal{Q}(S_{\delta}^{\prime})\cap \{u,v\} = \emptyset$  (neither has support on  $u,v$ ),  
b)  $\mathcal{Q}(S_{\gamma}^{\prime})\cap \{u,v\} = \{u\}$ $\mathcal{Q}(S_{\delta}^{\prime})\cap \{u,v\} = \{v\}$  (both are supported on  $u,v$  , but without overlap),  
c)  $\mathcal{Q}(S_{\gamma}^{\prime})\cap \{u,v\} = \emptyset$ $\mathcal{Q}(S_{\delta}^{\prime})\cap \{u,v\} \neq \emptyset$  (only one has support on  $u,v$

For a),  $S_{c} = S_{\gamma}S_{\delta} \Rightarrow u, v \notin \mathcal{Q}(S_{c})$  and Remark B.2 can be applied to show that if such a bipartition does exist then equations (20) and (21) cannot be simultaneously satisfied and hence a) never occurs.

Remark B.2. If before the action of  $\mathrm{CZ}_{u,v}$ , a stabilizer  $S_{c}$  where  $u, v \notin \mathcal{Q}(S_{c})$  is trivial (non-trivial), then after  $\mathrm{CZ}_{u,v}$  it remains trivial (non-trivial).

Proof. If  $u, v \notin \mathcal{Q}(S_c)$  then it must be the case that  $S_{\alpha}^{[u]} = S_{\beta}^{[u]}$  and  $S_{\alpha}^{[v]} = S_{\beta}^{[v]}$  for all possible bipartitions  $(\alpha, \beta)$ , where recall  $A^{[i]}$  is the Pauli operator of  $A$  acting on qubit  $i$ . Hence after  $\mathrm{CZ}_{u,v}$  then  $S_{\alpha}^{[u]} = S_{\beta}^{[u]}$  and  $S_{\alpha}^{[v]} = S_{\beta}^{[v]}$ , and so  $u, v \notin \mathcal{Q}(S_c')$ . For a stabilizer to become trivial from non-trivial (or vice versa), then it must be true that some bipartition must change from sharing support to not sharing support (or vice versa). However, it follows immediately from the previous comments that for any bipartition  $(\alpha, \beta)$  then

$$
\mathcal {Q} \left(S _ {\alpha}\right) \cap \mathcal {Q} \left(S _ {\beta}\right) = \emptyset \Leftrightarrow \mathcal {Q} \left(S _ {\alpha} ^ {\prime}\right) \cap \mathcal {Q} \left(S _ {\beta} ^ {\prime}\right) = \emptyset \tag {22}
$$

and hence trivial and non-trivial stabilizers respectively remain so.

For b) and c), because all  $S_{\gamma}, S_{\delta} \in S_{\Psi}^{\mathrm{NT}}$  that gain support are considered by the initial search for all  $(\alpha, \beta)$  satisfying equations (20) and (21), only  $S_{\gamma}, S_{\delta}$  with no support gain are relevant here. Additionally, since only one half of a trivial bipartition need be found to prove triviality, then we can further limit our search to stabilizers with some support on  $u, v$ , reducing the set of potentially trivial partitions of any stabilizer found by equations (20) and (21) to

$$
\mathcal {S} _ {\Psi^ {\prime}} ^ {*} = \left\{S _ {i} ^ {\prime}: \mathcal {Q} \left(S _ {i} ^ {\prime}\right) \cap \{u, v \} \neq \emptyset , S _ {i} \in \mathcal {S} _ {\Psi} ^ {\mathrm {N T}} \right\}. \tag {23}
$$

As this set is can be easily found from  $S_{\Psi}^{\mathrm{NT}}$ , a batch triviality test can be applied to  $S_{\Psi'}^*$  with the reduced partition batch  $\mathcal{B}_c^* = \{S_b : b \subset c, |b| \leq \lfloor c/2 \rfloor, S_b \in S_{\Psi'}^*\}$ , allowing any trivial bipartitions to be found with minimal overhead cost.

To summarise, after  $\mathrm{CZ}_{u,v}$ ,  $\mathcal{S}_{\Psi}^{\mathrm{NT}}$  is updated by applying the following steps:

1. Update all  $S_c' \in S_{\Psi'}^{\mathrm{NT}}$  with non-trivial support on  $u$  and/or  $v$ , via  $S_c' \mapsto \mathrm{CZ}_{u,v} S_c \mathrm{CZ}_{u,v}$ .  
2. Remove from  $S_{\Psi}^{\mathrm{NT}}$  any  $S_c^\prime$  that admits a bipartition no longer containing support overlap.  
3. Add to  $S_{\Psi'}^{\mathrm{NT}}$  any new  $S_c'$  that can be produced by stabilizer pairs that now share support.  
4. Apply a batch triviality test to  $S_{\Psi'}^{\mathrm{NT}}$  with reduced partition batch  $\mathcal{B}_c^*$  to remove any trivial stabilizers.

# B.2.3 Qubit measurement

We shall consider the general case of performing an arbitrary single-qubit Pauli measurement  $M \in \{X, Y, Z\}$  (returning a  $+1$  eigenvalue). In the standard approach to updating  $\mathcal{G}_{\Psi}$ , as described in Appendix A and Ref. [20], generators for which  $\{K_i, M\} = 0$  are updated as  $K_i' = K_a K_i$  for some chosen  $\{K_a, M\} = 0$  (with  $K_a' = M$ ). However, after this update is applied,  $K_i' = K_a K_i$  may now be a trivial generator with respect to  $M$ , such that  $\mathcal{Q}(MK_a K_i) \cap \mathcal{Q}(M) = \emptyset$ . In these cases, rather than applying the generator detrivialisation described section B.1.2, we can apply a modified update to the generators  $K_i' = MK_a K_i$ . Similar remarks can apply for some cases where  $[K_i, M] = 0$ , in which case the update rule  $K_i' = MK_i$  is applied. To summarise, after measurement  $M$ , the state's stabilizer generators are updated  $\mathcal{G}_{\Psi} \mapsto \mathcal{G}_{\Psi'} = \{K_i'\}$  using the five following rules:

$$
K _ {a} ^ {\prime} = M \quad \text {f o r s o m e} \{K _ {a}, M \} = 0
$$

$$
K _ {i} ^ {\prime} = K _ {a} K _ {i} \quad \text {i f} \{K _ {i}, M \} = 0, K _ {i} \neq K _ {a}, \mathcal {Q} (M K _ {a} K _ {i}) \cap \mathcal {Q} (M) \neq \emptyset
$$

$$
K _ {i} ^ {\prime} = M K _ {a} K _ {i} \quad \text {i f} \{K _ {i}, M \} = 0, K _ {i} \neq K _ {a}, \mathcal {Q} (M K _ {a} K _ {i}) \cap \mathcal {Q} (M) = \emptyset
$$

$$
K _ {i} ^ {\prime} = K _ {i} \quad \text {i f} [ K _ {i}, M ] = 0, \mathcal {Q} (M K _ {i}) \cap \mathcal {Q} (M) \neq \emptyset
$$

$$
K _ {i} ^ {\prime} = M K _ {i} \quad \text {i f} \left[ K _ {i}, M \right] = 0, \mathcal {Q} (M K _ {i}) \cap \mathcal {Q} (M) = \emptyset
$$

We further define two key sets of updated generators  $A$  and  $B$ , such that  $A = \{i: K_i' = K_aK_i\} \cup \{i: K_i' = MK_aK_i\}$  and  $B = \{i: K_i' = MK_i\} \cup \{i: K_i' = MK_aK_i\}$ . From  $A$  and  $B$  we can derive the general update rule for arbitrary post-measurement stabilizers

$$
\begin{array}{l} S _ {c} ^ {\prime} = M ^ {| c \cap \{a \} |} \left(\prod_ {i \in c \cap (B \backslash A)} M K _ {i}\right) \left(\prod_ {j \in c \cap (A \cap B)} M K _ {a} K _ {j}\right) \left(\prod_ {k \in c \cap (A \backslash B)} K _ {a} K _ {k}\right) \left(\prod_ {l \in c \backslash (A \cup B \cup \{a \})} K _ {l}\right) (24) \\ = M ^ {| c \cap \{a \} |} M ^ {| c \cap B |} K _ {a} ^ {| c \cap A |} \prod_ {i \in c \backslash \{a \}} K _ {i} (25) \\ = M ^ {\left| c \cap (B \cup \{a \}) \right|} K _ {a} ^ {\left| c \cap A \right|} S _ {c \backslash \{a \}} (26) \\ \end{array}
$$

where  $|A|$  denotes the cardinality of the set  $A$ ,  $A \setminus B$  the set difference of  $A$  and  $B$ , and we have used the fact that  $[M, MK_i] = 0 \forall i \in B \setminus A$  and  $[K_i, K_j] = 0 \forall i, j$ . From this,  $S_c \in S_\Psi^{\mathrm{NT}}$  can be easily updated. However, given that a single measurement  $M$  may change the support of many generators, updating  $S_\Psi^{\mathrm{NT}}$  finding newly trivial and non-trivial stabilizers is more involved.

Firstly, in the following description of measurement update rules, we will require the following Lemma:

Lemma B.3. After single-qubit measurement  $M$  is made on state  $|\Psi \rangle$ , all new non-trivial stabilizers, are contained within the set  $\{S_c : a \notin c, S_{c \cup \{a\}} \in S_\Psi^{\mathrm{NT}}\}$  and where  $K_a$  is the generator removed from  $\mathcal{G}_{\Psi}$  and replaced with  $M$ .

Proof. Firstly, since  $|\mathcal{Q}(M)| = 1$  and  $K_{a}^{\prime} = M$ , then  $S_{c}^{\prime} \in S_{\Psi^{\prime}}^{\mathrm{T}}$  for all  $c \ni a$ . Hence only combinations that do not contain  $a$  need be considered.

Now consider the previously trivial combination  $c \ni a$  with bipartition  $(\alpha, \beta)$  such that  $\mathcal{Q}(S_{\alpha}) \cap \mathcal{Q}(S_{\beta}) = \emptyset$  for  $S_{c} = S_{\alpha}S_{\beta} \in S_{\Psi}^{\mathrm{T}}$  before measurement. As in equation (24), we can write the updated stabilizer as

$$
S _ {c} ^ {\prime} = S _ {\alpha} ^ {\prime} \cdot S _ {\beta} ^ {\prime} = \left(M ^ {| \alpha \cap B |} K _ {a} ^ {| \alpha \cap A |} S _ {\alpha}\right) \cdot \left(M ^ {| \beta \cap B |} K _ {a} ^ {| \beta \cap A |} S _ {\beta}\right) \tag {27}
$$

We first consider the cases in which  $|\alpha \cap B|$  and  $|\beta \cap B|$  are even, for which there are three further sub-cases:

i)  $|\alpha \cap A|$  and  $|\beta \cap A|$  even  $\Rightarrow S_{\alpha}^{\prime} = S_{\alpha}$  and  $S_{\beta}^{\prime} = S_{\beta}$ ;  
ii)  $|\alpha \cap A|$  and  $|\beta \cap A|$  odd  $\Rightarrow S_{\alpha}^{\prime} = K_{a}S_{\alpha}$  and  $S_{\beta}^{\prime} = K_{a}S_{\beta}$ ;  
iii)  $|\alpha \cap A|$  odd and  $|\beta \cap A|$  even  $\Rightarrow S_{\alpha}^{\prime} = K_{a}S_{\alpha}$  and  $S_{\beta}^{\prime} = S_{\beta}$  (and vice versa).

For i),  $S_{\alpha}^{\prime} = S_{\alpha}$  and  $S_{\beta}^{\prime} = S_{\beta} \Rightarrow \mathcal{Q}(S_{\alpha}^{\prime}) \cap \mathcal{Q}(S_{\beta}^{\prime}) = \emptyset$ , and  $S_{c}^{\prime} \in S_{\Psi^{\prime}}^{\mathrm{T}}$  remains trivial. For ii), if  $S_{\alpha} \mapsto S_{\alpha}^{\prime} = K_{a}S_{\alpha}$ , then  $\{S_{\alpha}, M\} = 0$  and hence  $\mathcal{Q}(M) \subset \mathcal{Q}(S_{\alpha})$ . Since the same applies for  $S_{\beta}^{\prime}$ , then  $\mathcal{Q}(S_{\alpha}) \cap \mathcal{Q}(S_{\beta}) \neq \emptyset$  and therefore  $(\alpha, \beta)$  is not a trivial bipartition of  $S_{c}$ , which is a contradiction and so ii) does not occur. Finally for iii),  $S_{c}^{\prime} = K_{a}S_{\alpha} \cdot S_{\beta} = S_{\alpha \cup \{a\}} \cdot S_{\beta} = S_{e \cup \{a\}}$ , and therefore  $(\alpha, \beta)$  is only a trivial bipartition for  $S_{c}^{\prime}$  if  $(\alpha \cup \{a\}, \beta)$  is for  $S_{c \cup \{a\}}$ .

In the cases in which  $|\alpha \cap B|$  and/or  $|\beta \cap B|$  are odd, we observe that the effect of applying  $M$  is to remove support on  $\mathcal{Q}(M)$ . The previous three cases then also apply except with  $\mathcal{Q}(S_{\alpha}^{\prime}) \mapsto \mathcal{Q}(MS_{\alpha}^{\prime}) \subset \mathcal{Q}(S_{\alpha}^{\prime})$  (and similarly for  $\beta$ ) which can only decrease the number of cases where  $\mathcal{Q}(S_{\alpha}^{\prime}) \cap \mathcal{Q}(S_{\beta}^{\prime}) = \emptyset$ .

It therefore follows that the only instances of trivial  $S_{c}$  and non-trivial  $S_{c}^{\prime}$  that occur are those for which  $S_{c \cup \{a\}}$  is non-trivial. Or equivalently, if  $S_{c} \in \mathcal{S}_{\Psi}^{\mathrm{T}}$  then  $S_{c} \in \mathcal{S}_{\Psi^{\prime}}^{\mathrm{NT}}$  iff  $S_{c \cup \{a\}} \in \mathcal{S}_{\Psi}^{\mathrm{NT}}$ .

We now proceed with the description of measurement update rules. After the single-qubit measurement  $M$  all stabilizer combinations containing  $a$  become trivial, since  $|\mathcal{Q}(K_a')| = 1$ , and so all  $S_c'$  with  $a \in c$  are removed. Next, using Lemma B.3 we show that for any single-qubit Pauli measurement  $M$  then all new non-trivial stabilizers are contained within the set  $\Gamma = \{S_c : a \notin c, S_{c \cup \{a\}} \in S_\Psi^{\mathrm{NT}}\}$ . Since all previously non-trivial  $S_{c \cup \{a\}} \in S_\Psi^{\mathrm{NT}}$  stabilizers are known,  $\Gamma$  is easily found. However, not all stabilizers in  $\Gamma$ , nor the remaining updated stabilizers  $\Delta = \{S_c' : S_c \in S_\Psi^{\mathrm{NT}}\} \setminus \{S_c' : a \in c\}$ , are necessarily still non-trivial. But since  $S_{\Psi'}^{\mathrm{NT}} \subseteq \Gamma \cup \Delta$ , all trivial stabilizers can be identified and removed using the batch triviality test described in section B.1.1.

Finally, we note that in some cases measurement  $M$  can cause the updated generators to be trivial in a manner not captured above. For example, in the simplest case, this can occur when performing  $M$  also performs the indirect single-qubit measurement  $M'$ . However, this can be easily identified as a non-trivial replacement for the trivial generator will always be contained within  $S_{\Psi}^{\mathrm{NT}}$ . Once any trivial generators are identified, the process described in section B.1.2 can then be applied to return  $\mathcal{G}_{\Psi}$  to its proper form.

To summarise,  $S_{\Psi}^{\mathrm{NT}}$  is updated by applying the following steps:

1. Remove from  $S_{\Psi^{\prime}}^{\mathrm{NT}}$  any  $S_{c}$  with  $a \in c$ , but keeping them in memory.  
2. Using the discarded stabilizers, find and add the set of potential new non-trivial stabilizers  $\{S_c : S_{c \cup \{a\}} \in \mathcal{S}_{\Psi}^{\mathrm{NT}}, S_c \notin \mathcal{S}_{\Psi}^{\mathrm{NT}}\}$ .  
3. Apply a batch triviality test to  $S_{\Psi'}^{\mathrm{NT}}$  to remove any trivial stabilizers.  
4. Test generators for triviality and update if required.

# B.3 SPF Part 2: Finding loss-tolerant measurement patterns

We now consider the task of using the set of non-trivial stabilizers to identify a set of measurement patterns that teleport from  $I$  to  $O$ , as outlined in section 3.3. In this case, each non-trivial stabilizer  $S_{a} \in S_{\Psi}^{\mathrm{NT}}$  represents three possible anti-commuting logical operators, namely  $S_{c}\bar{X}$ ,  $S_{c}\bar{Y}$  and  $S_{c}\bar{Z}$ . For each valid teleportation measurement pattern, this logical operator must then be combined with another represented by a second stabilizer  $S_{d}$  to satisfy equation (1). For states of significant size and complexity, this presents a large number of possible measurement patterns, which are prohibitively expensive to calculate and validate. However, due to requirement for achieving maximal loss tolerance, our algorithm is specifically concerned with measurement patterns that have minimal qubit weight, and only needs to consider a restricted subset of all patterns. We shall now present an algorithm that finds all measurement patterns below a certain qubit weight given  $S_{\Psi}^{\mathrm{NT}}$ , and hence the set of maximally loss-tolerant measurement patterns<sup>10</sup>.

Following equation (1), the set of all measurement patterns  $\mathcal{M}$  that achieve the desired teleportation is

$$
\mathcal {M} = \left\{M _ {\bar {L} _ {i}, \bar {L} _ {j}}: \left\{\bar {L} _ {i} ^ {[ O ]}, \bar {L} _ {j} ^ {[ O ]} \right\} = 0, \left[ \bar {L} _ {i} ^ {[ a ]}, \bar {L} _ {j} ^ {[ a ]} \right] = 0, \forall a \neq O \right\} \tag {29}
$$

Given that  $|M_{\bar{L}_i,\bar{L}_j}| \geq \max(|\mathcal{Q}(\bar{L}_i)|, |\mathcal{Q}(\bar{L}_j)|) - 1$ , the set  $\mathcal{M}_w$  of measurement patterns with weight  $w$  is a subset of all  $M_{\bar{L}_i,\bar{L}_j}$  produced by logical operators with at most weight  $w + 1$ , such that

$$
\mathcal {M} _ {w} \subset \left\{M _ {\bar {L} _ {i}, \bar {L} _ {j}}: | \mathcal {Q} (\bar {L} _ {i}) |, | \mathcal {Q} (\bar {L} _ {j}) | \leq w + 1 \right\}. \tag {30}
$$

Note that it is necessarily true that  $\mathcal{M}_v \subseteq \mathcal{M}_w$  for  $v < w$ , and also that any measurement pattern that does not contain (i.e. is loss-tolerant to) a certain set of qubits, is also loss-tolerant to any subset of those qubits. Hence, many loss-tolerant configurations on an  $n$ -qubit state can be found from combining logical operators with weight  $w \ll n$ . In practise,  $w$  can be increased until no additional loss tolerance is found, thereby providing all possible loss-tolerant configurations without the need for an exhaustive search<sup>11</sup>.

# Appendix C Further results

# C.1 Unheralded loss tolerance for smaller lattice channels

Figure 9 depicts the comparison between heralded SPF and unheralded SPF for  $2 \times 2$ ,  $3 \times 3$  and  $4 \times 4$  lattice channels. In the unheralded case, no threshold crossing is observed and the unheralded teleportation rate is found to decrease with increasing lattice size. Unlike the heralded loss case, for unheralded loss no clear threshold crossing point is observed in the teleportation rate of different sized lattices. As with the heralded case, the small size of lattice investigated means that these results are not conclusive. However, unlike the performance of heralded GPF, in this case the form of  $T(p_{l})$  remains sigmoidal, and so it is unclear whether such results indicate no threshold exists, or whether it exists but at  $p_{l} \approx 0$ . Given that  $p_{l}^{*} = 1$  for unheralded loss on the crazy graph, we therefore conjecture that unheralded thresholds do exist (even if they occur at  $p_{l}^{*} = 0$  on some lattices). If true, this suggests it may be possible to achieve  $p_{l}^{*} > 0$  using larger lattices, improved measurement strategies or some lattice structure not considered here.

Algorithm 1: The STABILIZERSTATE object used to implement stabilizer pathfinding.  
Method INITIALISESTATE  
 $\begin{array}{l}Q = \{I\} \\ \bar{X}\leftarrow X_I,\bar{Z}\leftarrow Z_I\\ \mathcal{G}\leftarrow \emptyset ,\mathcal{S}\leftarrow \emptyset \end{array}$  // Creates qubit register  $Q$  // Creates logical operators // Creates logical operators  
 $\mathcal{G}\gets \emptyset ,\mathcal{S}\gets \emptyset$  // Creates generators  $\mathcal{G}$  and stabilizer combos S  
Method ADDQUBIT(q)  
 $\begin{array}{l}Q\leftarrow Q\cup \{q\} \\ \bar{X}\leftarrow \bar{X}\otimes \mathbb{I}_q,\bar{Z}\leftarrow \bar{Z}\otimes \mathbb{I}_q\\ \mathcal{G}\leftarrow \{K_i\otimes \mathbb{I}_q:K_i\in \mathcal{G}\} ,\mathcal{S}\leftarrow \{S_c\otimes \mathbb{I}_q:S_c\in \mathcal{S}\} \end{array}$  // Appends qubit to register // Extends logical ops.  
Method APPLYQUBITUNITARY(q,U)  
 $\begin{array}{l}\bar{X}\leftarrow U\bar{X}U^{\dagger},\bar{Z}\leftarrow U\bar{Z}U^{\dagger}\\ \mathcal{G}\leftarrow \{UK_iU^\dagger :K_i\in \mathcal{G}\} ,\mathcal{S}\leftarrow \{US_cU^\dagger :S_c\in \mathcal{S}\} \end{array}$  // Updates logical operators // Updates logical operations  
Method APPLYCZ(u,v)  
 $\begin{array}{l}\bar{X}\leftarrow \mathrm{CZ}_{uv}\bar{X}\mathrm{CZ}_{uv}^\dagger ,\bar{Z}\leftarrow \mathrm{CZ}_{uv}\bar{Z}\mathrm{CZ}_{uv}^\dagger \\ \mathcal{G}\leftarrow \{\mathrm{CZ}_{uv}K_i\mathrm{CZ}_{uv}^\dagger :K_i\in \mathcal{G}\} \\ \mathcal{S}'\leftarrow \{\mathrm{CZ}_{uv}Sc\mathrm{CZ}_{uv}^\dagger :S_c\in \mathcal{S},S_c^{[u]}\otimes S_c^{[v]}\neq \mathbb{I}_u\otimes \mathbb{I}_v\} \\ \textbf{for } S_c'\textbf{ in } S'\textbf{ do}\\ \textbf{| if ISTRIVIAL}(S_c')\textbf{ then}\\ \textbf{| } S'\leftarrow S'\setminus \{S_c'\} \\ \textbf{for } S_c',S_d'\textbf{ in } S'\textbf{ do}\\ \textbf{| if }\mathcal{Q}(S_c)\cap \mathcal{Q}(S_d) = \emptyset \bigwedge \mathcal{Q}(S_c')\cap \mathcal{Q}(S_d')\subseteq \{u,v\} \textbf{then}\\ \textbf{| } S'\leftarrow S'\cup \{S_c'S_c'S_d'\} \\ \mathcal{S}^*\\ \mathcal{S}'\leftarrow \{S_c':S_c\in \mathcal{S},\mathcal{Q}(S_c')\cap \{u,v\} \neq \emptyset \} \\ \mathcal{S}\leftarrow S'\setminus FINDTRIVSTABS(S^*)\\ \end{array}$  // Finds post-CZ combo stabs.  
Method MEASUREQUBIT(q,M)  
 $K_{a}\gets$  FIRSTANTICOMMGEN(G,M) //Picks anti-comm. gen. to remove //Updatesgens.  
for  $K_{i}'$  in  $G^{\prime}\backslash \{S_{c}^{\prime}\}$  // Removes trivial combo stabs.  
if  $K_{i}'(M) = 0$  then  
b←BOOL(Q(MKaKi)∩Q(M)=∅) //BOOL(TRUE)=1,BOOL(FALSE)=0  
K'←MbKaKi  
else if [Ki',M]=0 then  
b←BOOL(Q(MK_i)∩Q(M)=∅)  
K'←MbKi  
S'←S\{Sc:Sc∈S,a∈c} //Updates combo stabs.  
A← {i:Ki'∈G,Ki'=KaKi}∪ {i:Ki'∈G,Ki'=MKaKi},  
B← {i:Ki'∈G,Ki'=MKi'∈G,Ki'=MKaKi}  
S'= {M|c∩(B∪a)}|Ka|c∩A|Sc(a):Sc∈S'}  
S'←S'∪ {Sc:Sc∪a}∈S,Sc∉S  
S←S'FINDTRIVSTABS(S')  
G←DETRIVIALGEN(G'∪{M}) // Detrivs. any trivialisedgens.  
Method FINDMEASUREMENTPATTERNS(O,w)  
Lw← {Sc,L:Sc∈S,L∈{X,Z,Y},|Q(L)|≤w+1} // Get low-weight logical ops.  
Mw← {M,Lj,Lj:Li,Lj∈L, {Lj[O],Lj[O]}=0,[Lj[a],Lj[a]]=[0∀a≠O]} // Find mnt. pats.  
return Mw

![](images/755de2e4b57e12a28fdfe89c1601f678f41b0d8d2b366fe9368e03e5737c6eea.jpg)  
Figure 9: Comparison between loss tolerance threshold behaviour for stabilizer pathfinding in the unheralded and heralded regimes for each lattice channel considered (with the "max-tolerance" measurement strategy applied for unheralded loss).

One possible hypothesis is that all lattice channels exhibit a threshold in the heralded SPF case, but suffer a drop in threshold when loss is unheralded, such that for all the cases considered  $p_l^* \to 0$ . To assess this hypothesis it may be possible to find some lattice channel with a high  $p_l^*$  in the heralded case with  $p_l^* > 0$  when loss is unheralded. Alternatively, one could attempt to tune between both thresholds (or between threshold and non-threshold behaviour in the case of the null-hypothesis) by simulating intermediately heralded loss where only some fraction of loss is unheralded.

Regardless of whether an unheralded threshold exists or not, it is perhaps unsurprising that SPF under unheralded loss exhibits different behaviour than the heralded case. In analogy with a quantum error correction protocol consisting of distinct detectability (identifying erroneous qubits) and correctability (calculating some correction operator to apply) substages, SPF under heralded loss has a trivial detectability stage followed by a correctability problem solved over the global state, for which we similarly find a threshold. On the other hand, when loss is unheralded one cannot separate detectability and correctability into different problems, but rather SPF must solve them simultaneously and with only partial, time-ordered knowledge of the state. In this case it is therefore not surprising if the phenomena of the heralded case cannot be straightforwardly recovered. Further study is therefore required to fully understand the differences and similarities of these cases.

# C.2 Measurement strategies

A general measurement strategy algorithm for teleportation with unheralded loss is given in box 3. Based on the particular choice of  $\widetilde{\mathcal{M}}^*$ , we present two possible measurement strategies and compare their ability to tolerate unheralded loss. The most-common strategy performs the measurement that occurs most in all available measurement patterns, such that  $\widetilde{\mathcal{M}}^* = \widetilde{\mathcal{M}}$ , whereas the max tolerance strategy performs the measurement that occurs most in the most loss-tolerant available measurement patterns such that  $\widetilde{\mathcal{M}}^* = \{M: |M| = w, \forall M \in \widetilde{\mathcal{M}}\}$ , where  $w$  is the minimum measurement pattern weight taken over all  $M \in \widetilde{\mathcal{M}}$ .

Figure 10a) compares the performance of the two strategies on a  $4 \times 4$  triangular lattice. Figure 10b) depicts the performance of the max-tolerance strategy with access to a greater number of measurement patterns as produced by pairs of logical operators with greater maximum weight.

# C.3 Algorithm efficiency

Figure 11 depicts the average computational runtime for building  $|\Psi \rangle$  and the finding of associated measurement patterns  $\mathcal{M}$  using the algorithms described in Appendix B.

# UNHERALDED LOSS MEASUREMENT STRATEGY:

1) Initialise the set of performed measurements as empty  $\widetilde{M} = \emptyset$  and the set of available patterns to the set of valid measurement patterns  $\widetilde{\mathcal{M}} = \mathcal{M}$ .  
2) Identify some subset of available measurement patterns  $\widetilde{\mathcal{M}}^* \subseteq \widetilde{\mathcal{M}}$ .  
3) Attempt the most common single-qubit measurement  $P_{i}$  across all  $M \in \widetilde{\mathcal{M}}^{*}$ . In the case of multiple such  $P_{i}$ , pick one at random.

a) If measurement  $P_{i}$  succeeds (i.e. qubit  $i$  is not lost), discard all measurement patterns that are no longer available. If no patterns remain, teleportation succeeds.

Such that  $\widetilde{M} \mapsto \widetilde{M} \cup \{P_i\}$  and  $\widetilde{\mathcal{M}} \mapsto \{M : P_i \in M \forall M \in \widetilde{\mathcal{M}}\}$ .  
b) If measurement  $P_{i}$  fails (i.e. qubit  $i$  is lost), discard all measurement patterns that contain any measurement on qubit  $i$ . If no patterns remain, teleportation fails.  
Such that  $\widetilde{\mathcal{M}}\mapsto \{M:X_i,Y_i,Z_i\notin M,\forall M\in \widetilde{\mathcal{M}}\}$

4) Repeat from 2).

![](images/7cd274a080f78f6c3086edda1512bbfa9ab6543799c5fd4d217219a022847206.jpg)  
Figure 10: a) Teleportation rates under unheralded loss for the most-common and max tolerance strategies on the  $4 \times 4$  triangular lattice. Each data point depicts the average teleportation rate over 100 Monte Carlo instances and error bars are plotted at one standard deviation. Measurement patterns were found from pairs of logical operators with at most five weight greater than the minimum. Such results show that the prioritisation of the lowest-weight measurement patterns is preferred for unheralded loss over a greater selection of possible measurements. We note that the most-common strategy requires approximately  $6 \times$  longer to compute given a greater number of measurement patterns must be considered. b) Teleportation rates for stabilizer pathfinding on the  $4 \times 4$  triangular lattice with unheralded loss depicted across various measurement pattern maximum weights. Recall that  $\mathcal{M}_w$  found to a higher maximum weight  $w$  will contain increasingly more measurement patterns, although with decreasing loss tolerance. Each data point depicts the average value for 1000 Monte Carlo instances and shaded error regions are depicted for a single standard deviation. While a small increase in loss tolerance is achieved by an increase above the minimum logical operator weight  $w = 10$  to  $w = 11$ , above this any advantage is marginal at best. Such results support the conjecture that the majority of useful loss tolerance is provided by a small selection of maximally loss-tolerant measurement patterns produced by  $\mathcal{M}_w$  with the minimum  $w$ .

![](images/5ff9b5a60100edefa403603a2d21b6609af0550ff6ec57e28372fc0408d555ba.jpg)  
Box 3: Algorithm for finding teleportation measurement patterns in case of unheralded loss. (

![](images/deec594e12564cf166638e0cad4f3adae7b19ee71463278f8c6dd76058ba8d3c.jpg)  
Figure 11: Average algorithm runtime for building states, i.e. finding and updating all non-trivial stabilizers (solid lines), and finding measurement patterns from said stabilizers (dashed line). Each data point depicts the average run-time for the given algorithm applied to teleportation across 1000 instances of random  $n$ -qubit graph states with measurement patterns only found from pairs of logical operators with a weight at most three greater than the minimum. Specifically, each graph generated is an instance of an Erdős-Renyi  $G_{n,m}$  random connected graph with  $n$  nodes,  $m$  edges and  $n - 1 \leq m \leq n(n - 1) / 2 - 1$  (also ensuring no edge connecting input qubit  $I$  and output  $O$ ). Simulations were performed with Python using a standard PC running a 2.8 GHz Intel Core i7 CPU with 16GB of RAM and leveraging a NVIDIA GeForce GT 750M graphics card for GPU processing.

For building  $|\Psi \rangle$ , algorithm runtime is primarily a factor of the number of non-trivial stabilizers for the state  $|S_{\Psi}^{\mathrm{NT}}|$ . From this it is easy to see that as  $m$  rises, so does the multiplicity of possible generator combinations, with increased  $n$  further providing additional qubits to distribute support among. However, here we observe a drop in build runtime occurs for the highest  $m$  when  $n \geq 10$ . We conjecture this phenomena is explained by noting that any stabilizer produced from an even number  $k$  of generators (where  $K_{i} = X_{i}\bigotimes_{i\neq j}Z_{j}$ ) is trivial for  $k > 2$  as  $K_{i}K_{j} = Y_{i}Y_{j}$  on the completely connected graph of  $n$  vertices  $K_{n}$  (given the conventional choice of  $\mathcal{G}_{\Psi}$  for graph states). Each  $k$ -clique (i.e.  $k$ -node complete subgraph) within the graph will also have this property. Hence, as  $G_{n,m}$  approaches  $K_{n}$ , the number of and size of cliques increases, hence decreasing the number of non-trivial  $S_{c}$  for even  $|c| > 2$ .

For finding  $\mathcal{M}$ , we conversely observe an increase in runtime for the most connected graphs. In this case, the number of near-minimum weight logical operators is the primary factor in the algorithm's runtime. If the previous conjecture holds, this may also explain the observed increase in runtime here. As connectivity increases, the number of low-weight  $S_{c}$  associated with cliques also rises and so the number of low-weight logical operators would be expected to increase and hence so to the possible pairings tested for  $\mathcal{M}$ . For graphs with near-maximum  $m$  it may therefore be sufficient to reduce a search of logical operator pairs to those with absolutely minimal weight.

Finally, we note that the runtime in building  $|\Psi \rangle$  depends to some extent on the construction order of the edges. For example, on the lattices considered in section 4, building edges within a vertical layer before building edge between layers was found to be decrease runtime. While a deep analysis of such optimal construction strategies is beyond the scope of this paper, we conjecture that construction techniques that build highly connected subgraphs first (which are later connected) is preferred to sequentially adding edges to a single growing component.

![](images/4651ce1a0f2cc5a436effba87e5ce1083f167313b45eedd30665aaadb2d6ad6a.jpg)  
C.4 Configuration loss tolerance

![](images/4362e93e64c425fd1f15f2ccaae49cec52f56370b1f53372c7b4f0887c2541b0.jpg)

![](images/9ceece7b4ef7c895128355e67267a0e240273876d85e28748a3c7c74cc5fdc5c.jpg)

![](images/7ad75836c5b0d8b464ee4f3e51777130620b53b858b2155cecaf6be2b025639b.jpg)

![](images/79f6056b9b5df58f541df124bffb4f4880af51c27e21558bbfadc2ffec52a65f.jpg)

![](images/ff8ab100379998b3e2627d923d1c804f33f11abe04b733a0857ae6442361f719.jpg)

![](images/a8bff835c9aaa7167d6fe16f6d51d236c3cf4d80215c93e63a86f10b8ccc1472.jpg)

![](images/8db0f9bcc7eaddbced654965b6019a3d62c9f18f8ed60b9f4b8f29813526e14b.jpg)

![](images/14dab83381301ff65d226b81e4c6476b76288827e72c3a8e66f78014c8c445e6.jpg)

![](images/8351e21cf04fbcef90fe371bccb0bc9447f6d695f1d3406c54593e740b071292.jpg)

![](images/6ee029fa4f38908e9eb0968f0e8f9d7b38a3b78d25d702ec2ab8b681560fca59.jpg)

![](images/8bba55c833a2c339d280534886df8d55383d19e0a7bfe24af89586f24d354bda.jpg)

![](images/657d1d534644f6eed71054dba060e1c8b9f8649abf4249843ceac9e86770a7e7.jpg)  
Figure 12: The proportion (left) and absolute number (center) of  $n_l$ -qubit loss configurations tolerable for each considered channel (right) with both GPF (blue) and SPF (red) compared to the total number of  $n_l$  qubit configurations (grey). Note that the scales of the right-hand plots are logarithmic. The total number of  $n_l$ -qubit configurations for each  $n_l$  is shown in grey, given by  $\binom{N}{n_l}$ , where  $N$  is the total number of channel qubits (excluding input and output qubits, which are assumed to be lossless). For crazy graph, no GPF loss tolerance exists, and so such data points are omitted.

![](images/83612279d5be733974390cab8f244e9165f9a6d93d340c24553ebef00857b900.jpg)

![](images/960e37513274fa94f606ed46145ad5a7f8a75aff9c28178b7fd4a2efd0943d8e.jpg)