# Quantum experiments and graphs II: Quantum interference, computation, and state generation

Xuemei Gu $^{a,b,1}$ , Manuel Erhard $^{a,c}$ , Anton Zeilinger $^{a,c,1}$ , and Mario Krenn $^{a,c,1,2}$

$^{a}$ Institute for Quantum Optics and Quantum Information, Austrian Academy of Sciences, 1090 Vienna, Austria;  $^{b}$ State Key Laboratory for Novel Software Technology, Nanjing University, 210023 Nanjing City, China; and  $^{c}$ Vienna Center for Quantum Science & Technology, Faculty of Physics, University of Vienna, 1090 Vienna, Austria

Contributed by Anton Zeilinger, November 28, 2018 (sent for review September 13, 2018; reviewed by Austin Lund and Jianwei Wang)

We present an approach to describe state-of-the-art photonic quantum experiments using graph theory. There, the quantum states are given by the coherent superpositions of perfect matchings. The crucial observation is that introducing complex weights in graphs naturally leads to quantum interference. This viewpoint immediately leads to many interesting results, some of which we present here. First, we identify an experimental unexplored multiphoton interference phenomenon. Second, we find that computing the results of such experiments is #P-hard, which means it is a classically intractable problem dealing with the computation of a matrix function Permanent and its generalization Hafnian. Third, we explain how a recent no-go result applies generally to linear optical quantum experiments, thus revealing important insights into quantum state generation with current photonic technology. Fourth, we show how to describe quantum protocols such as entanglement swapping in a graphical way. The uncovered bridge between quantum experiments and graph theory offers another perspective on a widely used technology and immediately raises many follow-up questions.

quantum experiments | graph theory | linear optics | multiphoton quantum interference | quantum entanglement

Photonic quantum experiments prominently use probabilistic photon sources in combination with linear optics (1). This allows for the generation of multipartite quantum entanglement such as Greenberger-Horne-Zeilinger (GHZ) states (2-5), W states (6), Dicke states (7, 8), or high-dimensional states (9, 10); proof-of-principle experiments of special-purpose quantum computing (11-18); or applications such as quantum teleportation (19, 20) and entanglement swapping (21, 22).

Here we show that one can describe all of these quantum experiments* with graph theory. To do this, we generalize a recently found link between graphs and a special type of quantum experiments with multiple crystals (23)—which were based on the computer-inspired concept of entanglement by path identity (24, 25). By introducing complex weights in graphs, we can naturally describe the operations of linear optical elements, such as phase shifters and beam splitters, which enables us to describe quantum interference effects. This technique allows us to find several results: (i) We identify a multiphotonic quantum interference effect which is based on generalization of frustrated pair creation in a network of nonlinear crystals. (Frustrated pair creation is an effect where the amplitudes of two pair-creation events can constructively or destructively interfere.) Although the two-photon special case of this interference effect was observed more than 20 years ago (26), the multiphoton generalization with many crystals has not been investigated theoretically or experimentally. (ii) We find these networks of crystals cannot be calculated efficiently on a classical computer. The experimental output distributions require the summation of weights of perfect matchings (the weight of a perfect matching is the product of the weights of all containing edges) in a complex weighted graph (or, alternatively, probabilities proportional to the matrix function Permanent and its generalization Hafnian), which is

#P-hard (27, 28) (a #P-hard problem is at least as difficult as any problem in the complexity class #P)—and related to the Boson-Sampling problem. (iii) We show that insights from graph theory identify restrictions on the possibility of realizing certain classes of entangled states with current photonic technology. (iv) The graph-theoretical description of experiments also leads to a pictorial explanation of quantum protocols such as entanglement swapping. We expect that this will help in designing or intuitively understanding novel (high-dimensional) quantum protocols. The conceptual ideas that have led to this article are shown in Fig. 1.

Connections between graph theory and quantum physics have been drawn in earlier complementary works. A well-known example is the so-called graph states, which can be used for universal quantum computation (31, 32). That approach has been generalized to continuous-variable quantum computation (33), using an interesting connection between Gaussian states and graphs (34). Graphs have also been used to study collective phases of quantum systems (35) and used to investigate quantum random networks (36, 37). The bridge between graphs and quantum experiments that we present here is quite different, thus allowing us to explore entirely different questions. The

# Significance

Graph theory can be used to model and explain different phenomena from physics. In this paper, we show that one can interpret quantum experiments composed of linear optics and probabilistic sources with graph theory. The important understanding is that complex weights in the graph naturally describe the quantum interference. That point of view leads to several results: We uncover a yet unexplored type of multiphoton quantum interference. It can be used to solve questions that are intractable on a classical computer. Also, the connection points toward a general restriction on creating certain classes of quantum states. In general, it gives another perspective on a mature photonic technology and will be significant for future designs of such experiments.

Author contributions: X.G. and M.K. designed research; X.G., M.E., and M.K. performed research; X.G., M.E., A.Z., and M.K. wrote the paper; and A.Z. and M.K. supervised the research.

Reviewers: A.L., The University of Queensland; and J.W., Peking University.

The authors declare no conflict of interest.

Published under the PNAS license.

<sup>1</sup>To whom correspondence may be addressed. Email: anton.zeilinger@univie.ac.at, xmgu@smail.nju.edu.cn, or mario.krenn@univie.ac.at.  
2Present address: Department of Chemistry, University of Toronto, Toronto, ON M5S 3H6, Canada.

This article contains supporting information online at www.pnas.org/lookup/suppl/doi:10.1073/pnas.1815884116/-/DCSupplemental.

* The experiments mentioned before all consist of probabilistic photon pair sources and linear optics. This is what we mean by quantum experiments for the rest of this paper. We show that graphs can describe all of such experiments. Additionally, the property of perfect matchings corresponds to  $n$ -fold coincidence detection, which is widely used in quantum optics experiments.

![](images/8a5317dc85fb7cfcb44d7fc2d7694392811da86dd46ed217697299ce2174dff7.jpg)  
Fig. 1. A rough sketch of the influences that have led to the current paper. Three seminal papers (26, 29, 30) have influenced entanglement by path identity (25), which itself has led to quantum experiments and graphs in ref. 23. Here we connect these ideas with the mature field of research that investigates passive linear optics in the quantum regime. The results of the merger are described in the current paper.

correspondence between graph theory and quantum experiments is listed in Table 1.

# Entanglement by Path Identity and Graphs

In this section, we briefly explain the main ideas from entanglement by path identity in ref. 25 and quantum experiments and graphs in ref. 23, which form the basis for the rest of this paper. The concept of entanglement by path identity shows a very general way to experimentally produce multipartite and high-dimensional entanglement. This type of experiment can be translated into graphs (23). As an example, we show an experimental setup which creates a 2D GHZ state in polarization (Fig. 24). The probabilistic photon pair sources (for example, the nonlinear crystals) are set up in such a way that crystals I and II can create horizontally polarized photon pairs, while crystals III and IV produce vertically polarized photon pairs. All of the crystals are excited coherently and the laser pump power is set such that two photon pairs are produced simultaneously. $^{\dagger}$

The final state is obtained under the condition of fourfold coincidences, which means that all four detectors click simultaneously. This can happen only if the two photon pairs originate either from crystals I and II or from crystals III and IV. There is no other case to fulfill the fourfold coincidence condition. For example, if crystals I and III fire together, there is no photon in path  $d$ , while there are two photons in path  $a$ . The final quantum state after postselection can thus be written as  $|\psi \rangle = \frac{1}{\sqrt{2}} (|H,H,H,H\rangle_{abcd} + |V,V,V,V\rangle_{abcd})$ , where  $H$  and  $V$  stand for horizontal and vertical polarization respectively, and the subscripts  $a,b,c,$  and  $d$  represent the photon's paths.

One can describe such types of quantum experiments using graph theory (23). There, each vertex represents a photon path

and each edge stands for a nonlinear crystal which can probabilistically produce a correlated photon pair. Therefore, the experiment can be described with a graph of four vertices and four edges depicted in Fig. 2B. A fourfold coincidence is given by a perfect matching of the graph, which is a subset of edges that contains every vertex exactly once. For example, there are two subsets of edges  $(E_{ab}, E_{dc})$  and  $(E_{ac}, E_{bd})$  in Fig. 2B, which form the two perfect matchings. Thus, the final quantum state after postselection can be seen as the coherent superposition of all perfect matchings of the graph.

# Complex Weighted Graphs—Quantum Experiments

Quantum Interference. Now we start generalizing the connection between quantum experiments and graphs. The crucial observation is that one can deal with a phase shifter in the quantum experiment as a complex weight in the graph. When we add phase shifters in the experiments and all of the crystals produce indistinguishable photon pairs, the experimental output probability with fourfold postselection is given by the superposition of the perfect matchings of the graph weighted with a complex number.

As an example shown in Fig. 3A, we insert a phase shifter between crystals I and III and all of the four crystals create horizontally polarized photon pairs. The phase  $\varphi$  is set to a phase shift of  $\pi$  and the pump power is set such that two photon pairs are created. With the graph-experimental connection, one can also describe the experimental setup as a graph which is depicted in Fig. 3B. The color of the edge stands for the phase in the experiments while the width of the edge represents the absolute value of the amplitude. To calculate fourfold coincidences from the outputs, we need to sum the weights of perfect matchings of the corresponding graph. There are two perfect matchings of the graph, where one is given by crystals III and IV while the other is from crystals I and II. The interference of the two perfect matchings (which means of the two fourfold possibilities) can be obtained by varying the relative complex weight  $e^{i\varphi}$  between them. Therefore, the cancellation of the perfect matchings shows the destructive interference in the experiment.

More quantitatively, each nonlinear crystal probabilistically creates photon pairs from spontaneous parametric downconversion (SPDC). We follow the theoretical method presented in refs. 29 and 38 and describe the down-conversion creation process as

$$
\hat {U} \approx 1 + g \left(\hat {a} ^ {\dagger} \hat {b} ^ {\dagger}\right) + \frac {g ^ {2}}{2} \left(\hat {a} ^ {\dagger} \hat {b} ^ {\dagger}\right) ^ {2} + O \left(g ^ {3}\right), \tag {1}
$$

where  $\hat{a}^{\dagger}$  and  $\hat{b}^{\dagger}$  are single-photon creation operators in paths  $a$  and  $b$ , and  $g$  is the down-conversion amplitude. The terms of  $O(g^{3})$  and higher are neglected. The quantum state can be expressed as  $|\psi\rangle = \hat{U} |vac\rangle$ , where  $|vac\rangle$  is the vacuum state.

Table 1. The analogies for quantum experiments and graph theory  

<table><tr><td>Linear optical quantum experiments</td><td>Graph theory</td></tr><tr><td>Quantum photonic setup including linear optical elements and nonlinear crystals as probabilistic photon pair sources</td><td>Complex weighted undirected graph</td></tr><tr><td>Optical output path</td><td>Vertex set S</td></tr><tr><td>Photonic modes in optical output path</td><td>Vertices in vertex set S</td></tr><tr><td>Mode numbers</td><td>Labels of the vertices</td></tr><tr><td>Photon pair correlation</td><td>Edges</td></tr><tr><td>Phase between photonic modes</td><td>Color of the edges</td></tr><tr><td>Amplitude of photonic modes</td><td>Width of the edges</td></tr><tr><td>n-fold coincidence</td><td>Perfect matching</td></tr><tr><td>#(terms in quantum state)</td><td>#(perfect matchings)</td></tr></table>

![](images/876799f599ffa144902cb4685fd8628c9fdd3b83d11874f19d0e41f1077bd9b5.jpg)  
Fig. 2. Generation of 2D four-photon GHZ state using entanglement by path identity (25) and corresponding graph description of the setup (23). (A) An optical setup consists of four probabilistic photon pair sources, for example nonlinear crystals. The crystals (gray squares) I-IV are pumped coherently and the pump power is set in such a way that two photon pairs are produced. Here we take the polarization for simplicity—crystals I and II each produce a photon pair with  $|H, H\rangle$  while crystals III and IV create a photon pair with  $|V, V\rangle$ . The fourfold coincidence requires a photon in each detector simultaneously, which can happen only when crystals I and II or crystals III and IV fire together. (B) The corresponding graph of the experiment. Each vertex stands for a photon path and each edge represents one crystal. Thus, the graph has four vertices and four edges. The condition of fourfold coincidence is represented by the perfect matchings of the graph—a subset of edges that contains every vertex exactly once. There are two subsets of edges  $(E_{ab}, E_{dc})$  and  $(E_{ac}, E_{bd})$  which form the perfect matchings in the graph. The final output state with postselection is in a superposition of all of the possibilities. Therefore, it can be seen as a superposition of all of the perfect matchings of the graph, which gives the result  $|\psi\rangle = \frac{1}{\sqrt{2}}(|H, H, H, H\rangle_{abcd} + |V, V, V, V\rangle_{abcd})$ .

Here we neglect the empty modes and higher-order terms and write only first-order terms and the fourfold term for second-order spontaneous parametric down-conversion. The full state up to second order can be seen in SI Appendix. Therefore, the final quantum state in our example is

$$
\begin{array}{l} | \psi \rangle = g (| H, H \rangle_ {a b} + | H, H \rangle_ {c d} + | H, H \rangle_ {b d} + e ^ {i \varphi} | H, H \rangle_ {a c}) \\ + g ^ {2} \left(1 + e ^ {i \varphi}\right) | H, H, H, H \rangle_ {a b c d} + \dots . \tag {2} \\ \end{array}
$$

We can see that the fourfold coincidence count rate varies with the tunable phase  $\varphi$  while the twofold coincidence count rate remains constant, which is depicted in Fig. 3C. This is a multiphotonic generalization of two-photon frustrated downconversion (26) that has never been experimentally observed.

Special-Purpose Quantum Computation. We here show a generalization of the setup in Fig. 3A, where the experimental results cannot be calculated efficiently on a classical computer. The output requires summation of weights of perfect matchings of a complex weighted graph, which is a remarkably difficult problem that is #P-hard (27, 28). The experiment consists of  $N$  nonlinear crystals and  $M$  optical output paths in total. We call this type of experiment "the crystal network" for the rest of this paper. One can experimentally adjust the pump power and phases for every crystal, which allows one to change every single weight of the edges of the corresponding graph independently. The crystals are pumped coherently and the pump power is set such that  $n$  ( $n < N$ ) crystals can produce photon pairs and higher-order pair creations can be neglected. Then we calculate the  $2n$ -fold coincidence in  $2n$  ( $2n < M$ ) output paths. Now one could ask, What is the probability of the  $2n$ -fold coincidences in one specific  $2n$  output when all crystals are pumped?

In Fig. 4, we show some examples to answer this question. In the first example, we have in total six output paths  $(a - f)$ :

$M = 6$  ) and nine crystals  $(N = 9)$  from which probabilistically two  $(n = 2)$  produce photon pairs. Now we calculate the fourfold probability for a subset of four output paths (for example,  $a,b,c,$  and  $d$  highlighted in orange). With the graph-experimental link, a subset of four outputs in the quantum experiment corresponds to a subset of four vertices in the corresponding graph, depicted in orange in Fig. 4A. The experimental outcome corresponds to summing weights of perfect matchings of the subgraph, which is related to calculating the Permanent of the submatrix of the adjacency matrix. (An adjacency matrix is a square matrix used to represent a simple graph. The elements of the matrix stand for the weights of the edges between two vertices.) Therefore, we find that the probability  $P_{abcd}$  is proportional to the Permanent,  $P_{abcd} \propto |\mathrm{Perm}(U_{P_s})|^2$ .

For experiments with general arrangements of crystals, the  $2n$ -fold probability can be calculated by a generalization of the Permanent—the so-called Hafnian (39), shown in Fig. 4B. When the crystal network consists of a large number of crystals, it is unknown how to efficiently approximate the Hafnian (40, 41). To the best of our knowledge, the fastest algorithm to compute the Hafnian of an  $n \times n$  complex matrix runs in  $O(n^{3}2^{n/2})$  time (42).

The task described above is connected to BosonSampling (11, 13-17), which requires the matrix function Permanent to calculate the experimental results. However, the experimental implementation is fundamentally different. In BosonSampling experiments to date, single photons undergo a multiphotonic Hong-Ou-Mandel effect (43-45) in a passive linear optical network. In contrast to that, our concept is based solely on probabilistic pair sources where frustrated pair creation occurs. Computing Hafnians has only recently been investigated by a complementary approach called Gaussian BosonSampling (46-48).

An interesting question is the scaling of expected count rates of BosonSampling and the approach presented here. In the original BosonSampling proposal,  $n$  pairs of heralded single photons

![](images/763e246f0d1ca2d00bb5c865313796aab1abd0c529b828e25bbe09ef68ad5965.jpg)  
Fig. 3. Interference of perfect matchings. (A) A setup with all crystals producing horizontally polarized photon pairs. A phase shifter with a phase of  $\varphi$  is inserted between crystals I and III. (B) The corresponding graph of the experimental setup. The complex weight  $e^{i\varphi}$  introduced by the phase shifter  $(e^{i\varphi}$ , here  $\varphi = \pi$ ) is depicted with different colors. Here red and blue of each edge stand for 0 and  $\pi$  phase shifts. There are two perfect matchings of the graph, which come from crystals I and II and crystals III and IV, respectively. When one calculates the sum of the perfect matchings, the quantum state is given by  $|\psi\rangle = (1 + e^{i\pi})|H,H,H,H\rangle_{abcd} = 0$ . This means the two perfect matchings cancel each other. (C) When the phase  $\varphi$  changes from 0 to  $2\pi$ , one can see the fourfold coincidence [depicted as  $\#(abcd)$ ] count rate changes while the twofold coincidence [for example, number of photon pairs in outputs a and  $b$ , depicted as  $\#(ab)$ ] count rate remains constant.

![](images/46eda8a9309cc268e4adead1920327a447cbed951745ce6722e16720e0bc9a32.jpg)  
A

![](images/0dd35dd8e62d4ae158b0d736a3a98e6a8ba7edec29e36c83a0a136241576dede.jpg)  
Fig. 4. Quantum experiments and computation complexity. (A, Top) An experiment consisting of 9 nonlinear crystals (with labels I-IX) and 18 phase shifters (gold-colored lines). They are arranged such that paths  $a$ ,  $c$ , and  $e$  are parallel. All of the crystals are pumped coherently and can produce indistinguishable photon pairs. The pump power is set in such a way that two crystals can produce photon pairs. One can adjust the phase shifters and pump power to change the phases and transition amplitudes (the values are shown in SI Appendix). (A, Bottom) The corresponding graph  $G_P$  and its adjacency matrix  $adj(G_P)$  for the setup. The ordering of the columns and rows is  $(a, c, e, b, d,$  and  $f)$ . Calculating fourfold coincidences in one specific subset path  $(a, b, c,$  and  $d)$  of four outputs relates to summing the weights of perfect matchings of the subgraph with related vertices, which corresponds to computing the matrix function Permanent of submatrix  $U_{P_s}$  highlighted in orange. Thus, the probability that a certain arrangement of detectors clicks is proportional to  $|Perm(U_{P_s})|^2$ . All of the combinations for the fourfold coincidence are depicted in the histogram (details in SI Appendix). (B, Top) A crystal network that shows the general case. The 9 crystals and 18 phase shifters are randomly put in order. Analogous to  $A$ , the pump power is also set such that two photon pairs can be generated. (B, Bottom) The corresponding graph  $G_H$  and its adjacency matrix  $adj(G_H)$ , where the ordering is the same as  $U_P$ . Again, we calculate the fourfold coincidence in specific outputs  $a$ ,  $b$ ,  $c$ , and  $e$ . This corresponds to computing the Hafnian of submatrix  $U_{H_s}$ , which is a generalization of the Permanent. The probability  $P_{abce}$  is given by the matrix function Hafnian,  $P_{abc} \propto |Haf(U_{H_s})|^2$ .

![](images/ecbfdab0fc129e756148d6bc776f9d4c225c56129b639fedadf9e4fd426b533c.jpg)  
B

![](images/0d76b24923e8d8d26fed63c5ecfd02156813996cabc28021fb819427ff970a32.jpg)  
GH:

![](images/1015903e9f37bdc2c2d487372f22b618456bb0769adc388092ca80f8db98f7a6.jpg)

![](images/01a0a8edb213010e7948b706ea1e370b1d0c8f3481d48846090950f6a1c2c592.jpg)

from  $n$  SPDC crystals (with emission probability  $p$ ) are the input into a linear optical network with  $m$  input and output paths. The count rate for  $n$ -fold coincidences  $R$  is  $R_{BS} \approx p^n$ . Later, two independent groups discovered a method to exponentially increase the count rate, called Gaussian BosonSampling and Scattershot BosonSampling (46, 49). There, each of the  $m$  inputs of the BosonSampling device is fed with one output of an SPDC crystal (the second SPDC photon is heralded). That means, there are  $m$  SPDC crystals ( $m > n$ ). That leads to an exponential increased count rate for  $n$ -fold coincidences of  $R_{SS} \approx \binom{m}{n} p^n (1 - p)^{m-n}$ .

Estimating the count rates in our approach needs a slightly more subtle consideration, as our photons are not the input to a BosonSampling device, but their generation itself is in a superposition. Let us look at the example given in Fig. 4A. Here we compare a complete bipartite graph to Scattershot BosonSampling. For a complete bipartite graph, we have two sets of paths  $\{a, c, e\}$  and  $\{b, d, f\}$ . To calculate the probability of detecting a fourfold coincidence, we first derive all possible crystal combinations that could lead to a fourfold detection. There are  $\binom{3}{2}$  ways to choose two elements from the two sets of paths. Therefore, there exist  $\binom{3}{2} \times \binom{3}{2}$  combinations of crystal pairs that produce fourfold coincidences. In general, for  $m^2$  crystals and  $2n$ -fold coincidences we have  $\binom{m}{n}^2$ . Furthermore, each combination can arise due to two (in general  $n!$ ) indistinguishable crystal combinations. For example, an (abcd) fourfold detection can arise from a photon pair emission from either crystals I and IV or II and VI, as depicted in Fig. 4A. Of course, the relative phase between these possibilities determines whether we expect constructive or destructive interference. The latter case would not contribute any counts. Since for BosonSampling the phases are randomly distributed, we average over a uniform phase distribution to account for all possible phase settings. This is equivalent to a 2D random walk. Thus, in general the average magnitude of the amplitude gives  $\sqrt{n!}$ . Therefore, the count rate is mag-

nified by  $n!$ . Finally, the estimated count rate for our approach based on path identity is  $R_{PI} \approx \binom{m}{n}^2 n! p^n (1 - p)^{m^2 - n}$ . The ratio of the path identity sampling and Scattershot Boson-Sampling thus is  $\frac{R_{PI}}{R_{SS}} = \binom{m}{n} n! (1 - p)^{m(m-1)}$ . This exponential increase is due to the additional number of crystals (while Scattershot BosonSampling uses  $m$  crystals, we use  $m^2$ ) and the coherent superposition of  $n!$  possibilities to receive the output. We compare now this ratio for two recent experimental implementations of Scattershot BosonSampling. In 2015, a group performed Scattershot BosonSampling with  $m = 13$  and  $n = 3$  (50). With  $P \approx 0.01$ , our approach would lead to roughly 350 times more  $2n$ -fold count rates. In 2018, a different group performed Scattershot BosonSampling with  $m = 12$  and up to  $n = 5$  (51). With the same number of modes and photon pairs, we would expect roughly 25,000 more  $2n$ -fold count rates. In SI Appendix, we explain the scaling based on an example.

For realistic experimental situations, one needs to carefully consider the influence of multipair emissions, stimulated emission, loss of photons (including detection efficiencies), and amount of photon-pair distinguishabilities in connection with statements of computation complexity (such as done, for instance, in refs. 52-55). A full investigation of these very interesting questions is beyond the scope of the current paper.

Linear Optics and Graphs. With the complex weights, one can apply the graph method to describe linear optical elements in general linear optical experiments. First, we describe the action of a beam splitter (BS) with our graph language. A crystal produces one photon pair in paths  $a$  and  $b$  while no photon is in path  $c$ , as shown in Fig. 5. Therefore, there is an edge between vertices  $a$  and  $b$  and there is no edge connecting vertex  $c$ . The incoming photon from path  $b$  propagates to the BS, which gives two possibilities: reflection to path  $b$  or transmission to path  $c$ . In the case of reflection, photons in path  $b$  stay in path  $b$  with an

![](images/c6e084eff0d2f7094bf254738a6e268cfafed9d194228f285e32cdc0a0ff64bf.jpg)  
Fig. 5. The action of a beam splitter described with a graph. Here we show a simple linear optical setup with one 50:50 beam splitter. Using graph technique, one can describe the setup as a graph depicted at Right. Step 1: A crystal produces a correlated photon pair in paths  $a$  and  $b$  and no photon goes to path  $c$ . Therefore, there is an edge between vertices  $a$  and  $b$  and there is no edge connecting vertex  $c$ . Step 2: The photon in path  $b$  propagates to the beam splitter which will transmit to path  $c$  or reflect to path  $b$  with an additional phase of  $\pi/2$ . Therefore, in the case of transmission, the existent red edge  $E_{ab}$  will connect the vertices  $a$  and  $c$ . While in the case of reflection, the existent edge  $E_{ab}$  gets a complex weight with phase of  $\pi/2$  shown in green.

additional relative phase of  $\pi /2$ . Thus, the correlation between paths  $a$  and  $b$  will stay and get a relative phase of  $\pi /2$ . This can be represented as the original red edge keeps connecting vertices  $a$  and  $b$  while the color of the edge changes to green, which stands for a relative phase shift  $\pi /2$ . In the case of transmission, photons in path  $b$  go to path  $c$ , which changes the original correlation between paths  $a$  and  $b$  to that between paths  $a$  and  $c$ . Therefore, the original red edge is changed to connect vertices  $a$  and  $c$ .

From the description of the BS above, we can derive the following general rules for BSs, which we call BS operation: (i) A BS has two input paths  $v$  and  $w$ , which correspond to vertices  $v$  and  $w$  of the graph. Take one input path  $v$  as the start. (ii) For transmission, duplicate the existent edges to connect the adjacent vertices of  $v$  with vertex  $w$  which stands for the other input path of the BS. (iii) For reflection, change the colors of the existent edges to the colors which represent a relative phase shift  $\pi / 2$ . (iv) Apply steps ii and iii for path  $w$ .

Another important optical device in photonic quantum experiments is the mode shifter, e.g., half-wave plates for polarization or holograms for orbital angular momentum (OAM). The action of mode shifters can also be described within the graph language (Fig. 6A). The crystal produces an orthogonally or horizontally polarized photon pair in paths  $a$  and  $b$ . A mode shifter (such as half-wave plates) is inserted in path  $a$ , which will change the photon's horizontal polarization to vertical polarization and vice versa in path  $a$ . In the graph, we introduce labels for each vertex (small light-gray disks), which indicate the mode numbers of a photon. For example, vertices  $a$  and  $b$  carry the labels H and V, which stand for the horizontal and vertical polarizations. All of the mode numbers of one photon in one path are included in a large black circle—a vertex set. In the graph language, the operation of a mode shifter can be represented by changing the labels of the vertex.

As another example for the use of the graph technique, we describe the manipulation of the polarizing beam splitter (PBS) shown in Fig. 6B. In quantum experiments, a PBS transmits horizontally polarized photons and reflects vertically polarized photons with an additional phase of  $\pi /2$ . If the crystal produces horizontally polarized photon pairs  $(|H,H\rangle_{ab})$ , photons in path  $a$  go to path  $b$  and photons in path  $b$  go to path  $a$ . The connection between paths  $a$  and  $b$  remains. Therefore, the edge between vertices  $a$  and  $b$  stays as the original red one. If the crystal produces orthogonally polarized photon pairs  $(|H,V\rangle_{ab})$ , there are

two photons in path  $b$  — one photon comes from path  $a$  and another photon with an additional phase of  $\pi / 2$  comes from path  $b$  because of reflection. Thus, in the corresponding graph, there are two labeled vertices in vertex set  $b$  and there is no vertex in vertex set  $a$ .

Introducing linear optical elements in the graph representation of quantum experiments allows us to describe a prominent quantum effect—Hong-Ou-Mandel (HOM) interference (57), which is shown in Fig. 6C. HOM interference can be observed if two indistinguishable photons propagate to different input paths of a BS.

By using the BS operation, one can obtain the final graph. When the crystal produces a horizontally polarized photon pair, we can immediately see that the edges between vertex sets  $a$  and  $b$  vanish. Thus, the experimental setup shows the destructive interference. If the created photons are in orthogonal

![](images/2f806788d29ee82b4fb73bf41efd32c171c71fcd6d99c2e18f72582bc80e6870.jpg)  
Fig. 6. (A) An example for describing mode shifters with a graph. (A, Left) A crystal generates a polarized photon pair in paths  $a$  and  $b$ . A half-wave plate (HWP@45) changes the photon's polarization such that horizontal polarization changes to vertical polarization and vice versa. A, Right depicts the corresponding graphs. The vertices with labels  $H$  or  $V$  represent horizontal or vertical polarization of photons. Therefore, the label  $H$  changes to  $V$  in the vertex set  $a$ . (B) Graph description for the polarizing beam splitter (PBS). A PBS can transmit a horizontally polarized photon and reflect a vertically polarized photon. When the crystal creates a horizontally polarized photon pair, photons in paths  $a$  and  $b$  transmit to paths  $b$  and  $a$ . When the crystal produces an orthogonally polarized photon pair, the photon in path  $a$  is transmitted and the photon in path  $b$  is reflected with phase of  $\pi/2$ . Therefore, there are two correlated photons in path  $b$ . In the graph  $(B, Right)$ , there are two labeled vertices in vertex sets  $b$  with a green edge connecting them. (C) An optical setup for Hong-Ou-Mandel (HOM) interference. A crystal produces a photon pair in paths  $a$  and  $b$  which propagate to a 50:50 BS. By using the BS operation, we get the final graph. Now let us look at two cases where the photons are indistinguishable or distinguishable. For simplicity, we show the example with polarization. When the two photons are indistinguishable—all of their mode numbers are identical such as  $|H, H\rangle_{ab}$ —the edges that connect vertices  $a$  and  $b$  cancel. The remaining green edges with two vertices in vertex sets  $a$  or two vertices in vertex sets  $b$  show that there are two photons in path  $a$  or path  $b$ . This is a manifestation of the HOM interference. While in the case that the input photons have orthogonal polarization such as  $|H, V\rangle_{ab}$ , we clearly see that no interference can be observed. Therefore, the four possible outputs remain ( $|H, V\rangle_{aa}$ ;  $|H, V\rangle_{ab}$ ;  $|V, H\rangle_{ab}$ ;  $|V, H\rangle_{bb}$ ).

polarization, the superposition of the perfect matchings is not zero and then no interference can be observed in the experiment.

Every other linear optical element can be described with graphs. That is because linear optics do not change the number of photons and cannot destroy photon pair correlations. They can change phases (which changes the complex weight of edges), intrinsic mode numbers (such as polarization or OAM, which changes the mode number in the vertex set), or the extrinsic mode number (i.e., the path of the photon, which leads to reconnection of edges). All of these actions can be described within our graph method. Thus, every linear optical setup with probabilistic photon pair sources corresponds to an undirected graph with complex weights.

Therefore, we are equipped with the powerful technique of the mathematical field of graph theory, which we can now apply to many state-of-the-art photonic experiments.

Restriction for GHZ State Generation. In ref. 23, we have shown a restriction on the generation of high-dimensional GHZ states. The limitation stems from the fact that certain graphs with special properties (concerning their perfect matchings) cannot exist. Since we have extended the use of graphs to linear optics, this restriction applies more generally. We show this restriction by investigating a particular linear optical experiment.

To understand this example, let us first analyze the creation of the 2D GHZ state. For creating a three-particle GHZ state, we can connect two crystals with a PBS. If the two crystals both create a Bell state, a three-photonic GHZ state with a trigger in

$a$  is created (shown in Fig. 7A) (58). Extending this to a four-particle GHZ state, we add another crystal that is connected via a PBS as depicted in Fig. 7B. (A four-particle polarization GHZ state can also be created in a simpler way by connecting two crystals via a PBS without a trigger with the same setup in Fig. 7A. However, thereby we emphasize the analogy to the 3D case.)

Now we are trying exactly the same in a 3D system. To create a 3D GHZ state, we can use two crystals (each generating a 3D entangled photon pair) and connect them with a 3D multiport (10), as shown in Fig. 7C. The graphical description for the setup is depicted in Fig. 7E. There are five perfect matchings of the final graph. When we calculate the sum of the perfect matchings (two of them cancel), we can get the final quantum state written as  $|\psi \rangle = \frac{1}{\sqrt{3}}(|3,1,1\rangle - |2,0,0\rangle - |-1, -1, -1\rangle)_{bcd}$ , which describes a 3D three-particle GHZ state. [Three-particle GHZ state can be written as  $|\psi \rangle = \frac{1}{\sqrt{3}}(|x,y,z\rangle + |\bar{x},\bar{y},\bar{z}\rangle + |\bar{\bar{x}},\bar{\bar{y}},\bar{\bar{z}}\rangle)$ , where  $m \perp \bar{m} \perp \bar{m}$  with  $m = x, y, z$ . The properties of entanglement cannot be changed by local transformations.]

In exact analogy to the 2D case, we add another crystal to the setup and connect it with another multiport (Fig. 7D). As in the 2D case, we would naturally expect to create a four-particle GHZ state in 3D with this setup. However, in this setup, six photons are used (two triggers and four photons for the GHZ state), and therefore the corresponding graph has six vertices. From ref. 23 we know that such graphs cannot generate high-dimensional GHZ states because additional terms (so-called Maverick terms)

![](images/e385b7d2b40d8ae832f1002d0e435482669249399bd2f53d15f1c7a1713ae7c6.jpg)  
A

![](images/238c62e69373d991e7850e4f74fe777b89c43940baff5b6c147411a6cb44e695.jpg)  
B

![](images/fd570b0f22f0c1c0f99b6daba47c186b4fb0a255018d02b57f59418336241cd5.jpg)  
E

![](images/1bedfe49747eb372237dcc6eb5675588a3f571f131c1276ee0e9a830447e9ea9.jpg)  
C

![](images/d2ff1e979eea2479a127df1ff7c917176fe8337d86c9274a9a488bcd1cae3ffd.jpg)  
D

![](images/b089aa021efcabaeea779f6fe7808737308c63719a30268d5982a9a3a541141d.jpg)  
F

![](images/4cd4c4f593d155e6c489a2b7c99a193d1ee12a2479bcebee307e0434460afa6f.jpg)  
Fig. 7. Generating high-dimensional multiphotonic states with linear optical setups. (A) An optical setup for creating a 2D three-photon GHZ state. In this example, each crystal produces an entangled state  $|\psi^{+}\rangle = 1 / \sqrt{2} (|H,H\rangle + |V,V\rangle)$ . The photons propagate to a polarizing beam splitter (PBS), and fourfold coincidences lead to a 2D three-photon GHZ state (where the photon in path a acts as a trigger). (B) For generating high-photon-number GHZ states, one can add more crystals and connect them via many PBSs. (C) In an analogous way, a 3D three-photon GHZ state  $(|\psi\rangle = 1 / \sqrt{3} (|0,0\rangle + | - 1,1\rangle + |1, - 1\rangle))$  has been created recently, by connecting two crystals (each producing a 3D entangled photon pair) with a 3D multiport (MP) (10). The MP consists of a reflection (R, such as mirrors), a spiral-phase plate (SPP), a BS, an OAM mode sorter (56), and a coherent mode projection (CMP) which projects the photon in path a on  $| + \rangle = |T\rangle = 1 / \sqrt{2} (|0\rangle + | - 1\rangle)$ . (C, Bottom) The corresponding transformation is described in ref. 10. (D) To create a higher-dimensional GHZ state, we now want to extend the setup to create a 3D GHZ state with four particles. However, since this setup uses six photons, we expect (due to the result in ref. 23) to get an additional term in the final quantum state after postselection. (E) The graphs describing the setup in C, where the vertex set (large black circle) shows the mode numbers of the photons. The initial state shows three connections for each vertex set, which stands for the initial 3D entanglement (details in SI Appendix). The quantum state conditioned on fourfold coincidences is obtained by calculating the perfect matchings of the graph. There are five perfect matchings and two of them cancel each other, which results in a 3D GHZ state after triggering the photon in path a on  $|T\rangle = 1 / \sqrt{2} (|0\rangle + | - 1\rangle)$ . (F) These graphs describe the experimental setup in D. As expected, it has four perfect matchings (the other four perfect matchings are canceled), three corresponding to the GHZ state while the fourth one (highlighted in light blue) is the so-called Maverick term.

![](images/c27b1247648089c2aabd093d5b278838500234d20ee22e4da51eec0c05d9e482.jpg)  
Final

![](images/d66e9363cc6e124e6ad602a2d9289345a0620de315b0149fc29dce9016c51ed7.jpg)

![](images/963a11a2a047617b28aea94dd251ce4487e8fa5df9a1c04c796f9780599e9b35.jpg)

![](images/597a305e9cb08fdaffda141f76ba0907fbac9658c6c87bbecb66963594b68c38.jpg)

occur in the final state. (If the quantum state is independent of the trigger photons, then it consists of only four vertices, and these can be in a 3D GHZ state. Independent means that edges between the trigger vertices and the state vertices do not appear in any perfect matching.) And indeed, when we compute the perfect matchings of the graph, the final quantum state with postselection is given by  $|\psi \rangle = \frac{1}{2} (|-1, -1, 1, 3\rangle - |2,0,0,2\rangle + |3,1, -1, -1\rangle + |-1,0,0, -1\rangle)_{bcde}$ , which is not a GHZ state because of the additional term  $|-1,0,0, -1\rangle_{bcde}$ . This is the additional perfect matching that leads to the Maverick term (Fig. 7F), which comes from the tripled photon pairs emission of the middle crystal.

For higher dimensions, even more additional terms will appear—which can be understood by perfect matchings of graphs. The Maverick term is therefore a genuine manifestation of the graph description in a linear optical quantum experiment with a probabilistic photon source. Therefore, 2D  $n$ -particle GHZ states can be created while the 3D GHZ state with four particles is the highest-dimensional entangled GHZ state producible with linear optics and probabilistic photon sources in this way (for instance, without exploiting further ancillary photons).

Graphical Description for Quantum Protocols. Finally, we show that using graphs can also help to interpret quantum protocols. In Fig. 8, the entanglement swapping is described with graphs (1, 59). One crystal produces an entangled state  $|\psi^{-}\rangle = \frac{1}{\sqrt{2}}(|0,1\rangle - |1,0\rangle)$ . Therefore, the initial graph has two edges between the vertex set  $a$  and  $b$  and two edges between  $c$  and  $d$ . The weights of the two edges have a phase difference of  $\pi$ . With the BS operation, we can obtain the final graph. In the end, we obtain all perfect matchings and redraw the graph, which shows the entanglement swapping. The link between graphs and quantum experiments offers a graphical way to understand experimental quantum applications such as entanglement swapping.

# Conclusion

We have presented a connection between linear optical quantum experiments with probabilistic photon pair sources and graph theory. The final quantum state after postselection emerges as a superposition of graphs (more precisely, as a superposition of perfect matchings). With complex weights in the graphs, we find interference of perfect matchings which describes the interference of quantum states. Equipped with that technique, we identify a multiphotonic interference effect and show that calculating the outcome of such an experiment on a classical computer is remarkably difficult. Different from the interference which occurs in the BosonSampling experiments with linear optics, the underlying effect in our crystal network is multiphotonic frustrated photon generation. It would be exciting to see an actual implementation in a laboratory—potentially in integrated platforms which allow for on-chip photon pair generation (60-67). While we have shown that the expected  $n$ -fold coincidence counts will be larger than in conventional BosonSampling systems, an important question is how these systems compete under realistic experimental situations.

Another important question is how these setups can be applied to tasks in quantum chemistry, such as calculations of vibrational spectra of molecules (68, 69), or topological indexes of molecules (70), or graph theory problems (71).

So far, we have focused on  $n$ -fold coincidences with one photon per path, which is directly connected to perfect matchings. A generalized graph description which allows for arbitrary photons per path would also be a very interesting question for future research, which will need to exploit not only per

![](images/b120235853a12126c74ac92d86f98900152c023cdcdf26f9e96d560c4862ad6d.jpg)  
A

![](images/76104266e25ec363911ca09d5d772d5622514b59a5902a4936e370ec6f144326.jpg)  
B  
Fig. 8. Experimental diagram for entanglement swapping and corresponding graph description. (A) An experimental setup for entanglement swapping. Each crystal probabilistically generates an entangled state  $|\psi^{-}\rangle = \frac{1}{\sqrt{2}}(|0,1\rangle - |1,0\rangle)$ . When the photons emerge in paths  $b$  and  $c$  after the BS, the two-photon state in a and  $d$  is projected into the Bell state in  $|\psi^{-}\rangle$ . (B) Here we show the experiment using graphs. The initial  $|\psi^{-}\rangle$  states (depicted in dashed box I) both have a relative phase of  $\pi$ , which is represented by edges with different colors (red and blue). Using the BS operation, we get the final graph shown at Right. There are eight perfect matchings, and four of them cancel (highlighted in gray). Due to the symmetry in the quantum state (for example,  $|0,0,1,1\rangle_{abcd} = |0,1,0,1\rangle_{abcd}$ ), we rearrange the edges between different vertices after identifying perfect matchings. With  $e^{\frac{i3\pi}{2}}e^{\frac{i3\pi}{2}} = e^{i\pi}e^{i2\pi} = e^{i\pi}e^{0}$ , perfect matching of two purple edges can be redescribed as one edge in red and another in blue. The perfect matching for green edges is depicted in the same way. Finally, we obtain the final graph shown in dashed box II. From the two dashed boxes, we can clearly see the swapping of quantum entanglement.

fect matchings, but also more general techniques in matching theory.

With this connection, we uncovered restrictions on classes of quantum states that can be created using state-of-the-art photonic experiments with probabilistic photon sources, in particular, higher-dimensional GHZ states. The graph-experimental link could be used for investigating restrictions of other, much larger types of quantum states (72, 73) or could help in understanding the (non)constructability of certain 2D states. Restrictions for the generation of quantum states have been found before, using properties of Fock modes (74) for instance, and it would be interesting to discover whether those two independent techniques could be merged. Also severe restrictions on high-dimensional Bell-state measurements are known (75), which limits the application of protocols such as high-dimensional teleportation. The application of the graphene theory link to such types of quantum measurements would be worthwhile.

As an example, we have shown that entanglement swapping can be understood with graphs. A different graphical representation has been developed to describe quantum processes at a more abstract level (76, 77). Furthermore, directed graphs have recently been investigated to simplify certain calculations in quantum optics, by representing creation and annihilation operators in a visual way (78-80). A combination of these pictorial approaches with our methods could hopefully

improve the abstraction and intuitive understanding of quantum processes.

In ref. 23, we have shown that every experiment (based on crystal configurations as shown in Fig. 2) corresponds to an undirected graph and vice versa. It is still an open question whether for every undirected weighted graph, one can find a linear optical setup without path identification. This is an important question for the design of new experiments.

Our method can conveniently describe linear optical experiments with probabilistic photon sources. It will be useful to understand how the formalism can be extended to other types of probabilistic sources, such as single-photon sources based on weak lasers (81), or three-photon sources based on cascaded down-conversion (82, 83), or general multiphotonic sources (84). Can it also be applied to other (nonphotonic) quantum systems with a probabilistic source of quanta?

A final, very important question is how to escape the restrictions imposed by the graph-theory link. Deterministic quantum sources (85-87) would need an adaption of the description, and it is not yet known how to describe active feedforward (88-90). Can they be described with graphs? What are the techniques that cannot be described in the way presented here?

ACKNOWLEDGMENTS. The authors thank Armin Hochrainer, Johannes Handsteiner, and Kahan Dare for useful discussions and valuable comments on the manuscript. X.G. thanks Lijun Chen for support. This work was supported by the Austrian Academy of Sciences and by the Austrian Science Fund with Spezialforschungsbereiche F40 (Foundations and Applications of Quantum Science). X.G. acknowledges support from the National Natural Science Foundation of China (Grant 61771236) and its Major Program (Grants 11690030 and 11690032), the National Key Research and Development Program of China (Grant 2017YFA0303700), and a scholarship from the China Scholarship Council.

1. Pan J-W, et al. (2012) Multiphoton entanglement and interferometry. Rev Mod Phys 84:777-838.  
2. Bouwmeester D, Pan J-W, Daniell M, Weinfurter H, Zeilinger A (1999) Observation of three-photon Greenberger-Horne-Zeilinger entanglement. Phys Rev Lett 82:1345-1349.  
3. Yao X-C, et al. (2012) Observation of eight-photon entanglement. Nat Photon 6:225-228.  
4. Wang X-L, et al. (2016) Experimental ten-photon entanglement. Phys Rev Lett 117:210502.  
5. Wang X-L, et al. (2018) 18-qubit entanglement with six photons' three degrees of freedom. Phys Rev Lett 120:260502.  
6. Eibl M, Kiesel N, Bourennane M, Kurtsiefer C, Weinfurter H (2004) Experimental realization of a three-qubit entangled W state. Phys Rev Lett 92:077901.  
7. Wieczorek W, et al. (2009) Experimental entanglement of a six-photon symmetric Dicke state. Phys Rev Lett 103:020504.  
8. Hiesmayr BC, De Dood MJA, Loffler W (2016) Observation of four-photon orbital angular momentum entanglement. Phys Rev Lett 116:073601.  
9. Malik M, et al. (2016) Multi-photon entanglement in high dimensions. Nat Photon 10:248-252.  
10. Erhard M, Malik M, Krenn M, Zeilinger A (2018) Experimental Greenberger-Horne-Zeilinger entanglement beyond qubits. Nat Photon 12:759-764.  
11. Aaronson S, Arkhipov A (2011) The computational complexity of linear optics. Proceedings of the Forty-Third Annual ACM Symposium on Theory of Computing (ACM, New York), pp 333-342.  
12. Rahimi-Keshari S, Lund AP, Ralph TC (2015) What can quantum optics say about computational complexity theory? Phys Rev Lett 114:060501.  
13. Lund AP, Bremner MJ, Ralph TC (2017) Quantum sampling problems, BosonSampling and quantum supremacy. npj Quan Inf 3:15.  
14. Spring JB, et al. (2013) Boson sampling on a photonic chip. Science 339:798-801.  
15. Broome MA, et al. (2013) Photonic boson sampling in a tunable circuit. Science 339:794-798.  
16. Tillmann M, et al. (2013) Experimental boson sampling. Nat Photon 7:540-544.  
17. Crespi A, et al. (2013) Integrated multimode interferometers with arbitrary designs for photonic boson sampling. Nat Photon 7:545-549.  
18. Carolan J, et al. (2015) Universal linear optics. Science 349:711-716.  
19. Bouwmeester D, et al. (1997) Experimental quantum teleportation. Nature 390:575-579.  
20. Wang X-L, et al. (2015) Quantum teleportation of multiple degrees of freedom of a single photon. Nature 518:516-519.  
21. Pan J-W, Bouwmeester D, Weinfurter H, Zeilinger A (1998) Experimental entanglement swapping: Entangling photons that never interacted. Phys Rev Lett 80:3891-3894.  
22. Zhang Y, et al. (2017) Simultaneous entanglement swapping of multiple orbital angular momentum states of light. Nat Commun 8:632.  
23. Krenn M, Gu X, Zeilinger A (2017) Quantum experiments and graphs: Multiparty states as coherent superpositions of perfect matchings. Phys Rev Lett 119:240403.  
24. Krenn M, Malik M, Fickler R, Lapkiewicz R, Zeilinger A (2016) Automated search for new quantum experiments. Phys Rev Lett 116:090405.  
25. Krenn M, Hochrainer A, Lahiri M, Zeilinger A (2017) Entanglement by path identity. Phys Rev Lett 118:080401.  
26. Herzog TJ, Rarity JG, Weinfurter H, Zeilinger A (1994) Frustrated two-photon creation via interference. Phys Rev Lett 72:629-632.  
27. Valiant LG (1979) The complexity of computing the permanent. Theor Comput Sci 8:189-201.  
28. Aaronson S (2011) A linear-optical proof that the permanent is # P-hard. Proc R Soc A 467:3393-3405.  
29. Wang LJ, Zou XY, Mandel L (1991) Induced coherence without induced emission. Phys Rev A 44:4614-4622.  
30. Hardy L (1992) Source of photons with correlated polarisations and correlated directions. Phys Lett A 161:326-328.  
31. Raussendorf R, Briegel HJ (2001) A one-way quantum computer. Phys Rev Lett 86:5188-5191.

32. Hein M, et al. (2006) Entanglement in graph states and its applications. arXiv:quant-ph/0602096. Preprint, posted February 11, 2006.  
33. Menicucci NC, et al. (2006) Universal quantum computation with continuous-variable cluster states. Phys Rev Lett 97:110501.  
34. Menicucci NC, Flammia ST, van Loock P (2011) Graphical calculus for Gaussian pure states. Phys Rev A 83:042335.  
35. Shchesnovich VS, Bezerra MEO (2018) Collective phases of identical particles interfering on linear multiports. Phys Rev A 98:033805.  
36. Perseguers S, Lewenstein M, Acin A, Cirac JI (2010) Quantum random networks. Nat Phys 6:539-543.  
37. Cuquet M, Calsamiglia J (2009) Entanglement percolation in quantum complex networks. Phys Rev Lett 103:240503.  
38. Lahiri M, Lapkiewicz R, Lemos GB, Zeilinger A (2015) Theory of quantum imaging with undetected photons. Phys Rev A 92:013832.  
39. Caianiello ER (1953) On quantum field theory-I: Explicit solution of Dyson's equation in electrodynamics without use of Feynman graphs. II Nuovo Cimento 10:1634-1652.  
40. Björklund A (2012) Counting perfect matchings as fast as Ryser. Proceedings of the Twenty-Third Annual ACM-SIAM Symposium on Discrete Algorithms (Society for Industrial and Applied Mathematics, Philadelphia), pp 914-921.  
41. Alexander B (2017) Approximating permanents and hafnians. Discrete Anal, 10.19086/da.1244.  
42. Björklund A, Gupt B, Quesada N (2018) A faster hafnian formula for complex matrices and its benchmarking on the titan supercomputer. arXiv:1805.12498. Preprint, posted May 31, 2018.  
43. Tillmann M, et al. (2015) Generalized multiphoton quantum interference. Phys Rev X 5:041015.  
44. Menssen AJ, et al. (2017) Distinguishability and many-particle interference. Phys Rev Lett 118:153603.  
45. Dittel C, et al. (2018) Totally destructive many-particle interference. Phys Rev Lett 120:240404.  
46. Lund AP, et al. (2014) Boson sampling from a Gaussian state. Phys Rev Lett 113: 100502.  
47. Hamilton CS, et al. (2017) Gaussian boson sampling. Phys Rev Lett 119:170501.  
48. Brádler K, Dallaire-Demers P-L, Rebentrost P, Su D, Weedbrook C (2017) Gaussian boson sampling for perfect matchings of arbitrary graphs. Phys Rev A 98: 032310.  
49. Aaronson S (2013) Scattershot BosonSampling: A new approach to scalable Boson-Sampling experiments. Shtetl-Optimized. Available at https://www.scottaarsonson.com/blog/?p=1579. Accessed January 27, 2019.  
50. Bentivegna M, et al. (2015) Experimental scattershot boson sampling. Sci Adv 1:e1400255.  
51. Zhong H-S, et al. (2018) 12-photon entanglement and scalable scattershot boson sampling with optimal entangled-photon pairs from parametric down-conversion. arXiv:1810.04823. Preprint, posted October 11, 2018.  
52. Rohde PP, Ralph TC (2012) Error tolerance of the boson-sampling model for linear optics quantum computing. Phys Rev A 85:022332.  
53. Arkhipov A (2015) Bosonsampling is robust against small errors in the network matrix. Phys Rev A 92:062326.  
54. Rahimi-Keshari S, Ralph TC, Caves CM (2016) Sufficient conditions for efficient classical simulation of quantum optics. Phys Rev X 6:021039.  
55. Wang H, et al. (2018) Toward scalable boson sampling with photon loss. Phys Rev Lett 120:230502.  
56. Leach J, Padgett MJ, Barnett SM, Franke-Arnold S, Courtial J (2002) Measuring the orbital angular momentum of a single photon. Phys Rev Lett 88:257901.  
57. Hong C-K, Ou Z-Y, Mandel L (1987) Measurement of subpicosecond time intervals between two photons by interference. Phys Rev Lett 59:2044-2046.  
58. Pan J-W, Daniell M, Gasparoni S, Weihs G, Zeilinger A (2001) Experimental demonstration of four-photon entanglement and high-fidelity teleportation. Phys Rev Lett 86:4435-4438.  
59. Zukowski M, Zeilinger A, Horne MA, Ekert AK (1993) "Event-ready-detectors" bell experiment via entanglement swapping. Phys Rev Lett 71:4287-4290.

60. Jin H, et al. (2014) On-chip generation and manipulation of entangled photons based on reconfigurable lithium-niobate waveguide circuits. Phys Rev Lett 113: 103601.  
61. Silverstone JW, et al. (2014) On-chip quantum interference between silicon photon-pair sources. Nat Photon 8:104-108.  
62. Silverstone JW, et al. (2015) Qubit entanglement between ring-resonator photon-pair sources on a silicon chip. Nat Commun 6:7948.  
63. Krapick S, Brecht B, Herrmann H, Quiring V, Silberhorn C (2016) On-chip generation of photon-triplet states. Opt Express 24:2836.  
64. Feng L-T, et al. (2019) On-chip transverse-mode entangled photon pair source. npj Quantum Inf 5:2.  
65. Wang J, et al. (2018) Multidimensional quantum entanglement with large-scale integrated optics. Science 360:eaar7053.  
66. Santagati R, et al. (2018) Witnessing eigenstates for quantum simulation of Hamiltonian spectra. Sci Adv 4:eap9646.  
67. Adcock JC, Vigliar C, Santagati R, Silverstone JW, Thompson MG (2018) Programmable four-photon graph states on a silicon chip. arXiv:1811.03023. Preprint, posted November 7, 2018.  
68. Huh J, Guerreschi GG, Peropadre B, McClean JR, Aspuru-Guzik A (2015) Boson sampling for molecular vibronic spectra. Nat Photon 9:615-620.  
69. Sparrow C, et al. (2018) Simulating the vibrational quantum dynamics of molecules using photonics. Nature 557:660-667.  
70. Hosoya H (2002) The topological index  $Z$  before and after 1971. _Internet Electron J Mol Des_ 1:428-442.  
71. Bradler K, Friedland S, Izaac J, Killoran N, Su D (2018) Graph isomorphism and Gaussian boson sampling. arXiv:1810.10644. Preprint, posted October 24, 2018.  
72. Huber M, de Vicente JI (2013) Structure of multidimensional entanglement in multipartite systems. Phys Rev Lett 110:030501.  
73. Goyeneche D, Bielawski J, Žyczkowski K (2016) Multipartite entanglement in heterogeneous systems. Phys Rev A 94:012346.  
74. Migdal P, Rodriguez-Laguna J, Ozsmaniec M, Lewenstein M (2014) Multiphoton states related via linear optics. Phys Rev A 89:062329.  
75. Calsamiglia J (2002) Generalized measurements by linear elements. Phys Rev A 65: 030301.

76. Coecke B (2006) Kindergarten quantum mechanics: Lecture notes. AlP Conference Proceedings: Quantum Theory: Reconsideration of Foundations, eds Adenier G, Khrennikov A, Nieuwenhuizen TM (American Institute of Physics, College Park, MD), Vol 810, p 81.  
77. Abramsky S, Coecke B (2004) A categorical semantics of quantum protocols. Proceedings of the 19th Annual IEEE Symposium on Logic in Computer Science (IEEE Computer Society, Washington, DC), pp 415-425.  
78. Ataman S (2014) Field operator transformations in quantum optics using a novel graphical method with applications to beam splitters and interferometers. Eur Phys J D 68:288.  
79. Ataman S (2015) The quantum optical description of three experiments involving non-linear optics using a graphical method. Eur Phys J D 69:44.  
80. Ataman S (2018) A graphical method in quantum optics. J Phys Commun 2: 035032.  
81. Zhao Z, et al. (2004) Experimental demonstration of five-photon entanglement and open-destination teleportation. Nature 430:54-58.  
82. Hübel H, et al. (2010) Direct generation of photon triplets using cascaded photon-pair sources. Nature 466:601-603.  
83. Hamel DR, et al. (2014) Direct generation of three-photon polarization entanglement. Nat Photon 8:801-807.  
84. Lahiri M (2018) Many-particle interferometry and entanglement by path identity. Phys Rev A 98:033822.  
85. Santori C, Fattal D, Vuckovic J, Solomon GS, Yamamoto Y (2002) Indistinguishable photons from a single-photon device. Nature 419:594-597.  
86. Michler P, et al. (2000) A quantum dot single-photon turnstile device. Science 290:2282-2285.  
87. Senellart P, Solomon G, White A (2017) High-performance semiconductor quantum-dot single-photon sources. Nat Nanotechnol 12:1026-1039.  
88. Giacomini S, Sciarrino F, Lombardi E, De Martini F (2002) Active teleportation of a quantum bit. Phys Rev A 66:030302.  
89. Pittman TB, Jacobs BC, Franson JD (2002) Demonstration of feed-forward control for linear optics quantum computation. Phys Rev A 66:052305.  
90. Ma X-S, et al. (2012) Quantum teleportation over 143 kilometres using active feedforward. Nature 489:269-273.