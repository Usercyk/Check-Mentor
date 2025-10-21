# From Three-Photon Greenberger-Horne-Zeilinger States to Ballistic Universal Quantum Computation

Mercedes Gimeno-Segovia, $^{1,*}$  Pete Shadbolt, $^{1}$  Dan E. Browne, $^{2}$  and Terry Rudolph $^{1}$ \
 $^{1}$ Department of Physics, Imperial College London, London SW7 2AZ, United Kingdom\
 $^{2}$ Department of Physics and Astronomy, University College London, London WC1E 6BT, United Kingdom\
(Received 28 October 2014; published 8 July 2015)

Single photons, manipulated using integrated linear optics, constitute a promising platform for universal quantum computation. A series of increasingly efficient proposals have shown linear-optical quantum computing to be formally scalable. However, existing schemes typically require extensive adaptive switching, which is experimentally challenging and noisy, thousands of photon sources per renormalized qubit, and/or large quantum memories for repeat-until-success strategies. Our work overcomes all these problems. We present a scheme to construct a cluster state universal for quantum computation, which uses no adaptive switching, no large memories, and which is at least an order of magnitude more resource efficient than previous passive schemes. Unlike previous proposals, it is constructed entirely from loss-detecting gates and offers a robustness to photon loss. Even without the use of an active loss-tolerant encoding, our scheme naturally tolerates a total loss rate  $\sim 1.6\%$  in the photons detected in the gates. This scheme uses only 3 Greenberger-Horne-Zeilinger states as a resource, together with a passive linear-optical network. We fully describe and model the iterative process of cluster generation, including photon loss and gate failure. This demonstrates that building a linear-optical quantum computer needs to be less challenging than previously thought.

DOI: 10.1103/PhysRevLett.115.020502

PACS numbers: 03.67.Lx, 03.67.Bg, 42.50.Dv, 42.50.Ex

In 2001, Knill, Laflamme, and Milburn [1] showed that scalable quantum computation was possible using only linear-optical elements—without the need for deterministic two-photon interactions. However, their proposal was more a proof of principle than a feasible construction as the scheme required tens of thousands of optical elements to acquire gates with a high probability of success. Since then, several proposals have developed the idea of a linear-optical quantum computer (LOQC), including Nielsen's proposal [2] of combining linear optics with cluster states, the Browne-Rudolph fusion mechanisms [3] to efficiently create optical cluster states, and Kieling's et al. proposal [4] of building an imperfect cluster that can be renormalized using ideas of percolation theory. While alternative schemes for LOQC [5] using parity state encoding [6] or small amplitude coherent states [7] have been proposed, we do not address these approaches in this Letter.

Recent demonstrations [8-12] have made significant progress towards experimental linear-optical quantum computing. In particular, the use of integrated photonics to implement large-scale, complex interferometers on a chip shows great promise. However, active feed forward remains challenging; it requires fast switching which is a dominant source of photon loss and has not yet been experimentally demonstrated in an integrated device.

Of previous approaches to linear-optical quantum computing, only Kieling et al.'s proposal [4] is ballistic—meaning that active switching is not required for the process of cluster state generation. It is thus the most

suitable previous approach to LOQC in an integrated setting. It has a number of shortcomings, however. First, it requires four- or five-photon entangled states as input, which are costly and difficult to generate in a (near)-deterministic manner. Second, it is not constructed from loss-tolerant components; photon loss during the process will lead to the generation of an undesired state.

In this Letter, we adapt new advances in the Bell state measurement [13,14] to the ballistic cluster state generation scheme to provide a new approach to scalable ballistic LOQC with significant advances on Kieling et al.'s approach. Off-line resources are reduced to three-photon entangled states, while all gates are loss detecting. The scheme has an in-built robustness to loss and will succeed, without additional loss encoding, even if  $>1\%$  of the photons entering the gates are lost. Deterministic  $n$ -qubit entangled state generation becomes increasingly experimentally challenging with  $n$  [15], and the reduction to resource states of only three photons is thus a significant improvement. For a fair comparison of our scheme against previous proposals [4], we count the number of Bell pairs needed to build the initial entangled states for both cases. As the construction of these initial states is probabilistic, we assume a multiplexing stage in order to achieve deterministic resource states, which then enables us to count the total number of Bell pairs used in each strategy. The full resource comparison, demonstrating at least an order of magnitude reduction in resources, is presented in the Supplemental Material [16].

![](images/84efc51de8bb87d08bbdd061dc208750ef15a569567a4f38bc3ea9bd3390d06e.jpg)  
FIG. 1 (color online). Boosted type-II fusion gate. Photons 1 and 2 represent the photons on which the gate is applied; the rest are ancillary photons. The implementation based on [13] requires a pair of maximally entangled photons, while the implementation based on [14] requires four single photons. The boosted gates have the exact same success and failure outcomes as the original type II but with a higher success probability. Note that all photons are measured. Here and in subsequent figures we will represent the boosted fusion by the hexagon marked "F".

The basic building block of our scheme is Browne and Rudolph's type-II fusion gate, which can be used to connect small cluster state fragments into a large cluster state for measurement-based quantum computing (MBQC). This gate is equivalent to a Bell state measurement (BSM) in a rotated basis. In linear optics, BSMs cannot be achieved deterministically. For a long time, the highest known probability of success for a linear-optical BSM was  $50\%$  [17], but recent breakthroughs have shown that this can be improved to  $75\%$  by incorporating ancillary resources—such as Bell pairs [13] or single photons [14]. We adapt these schemes to give a type-II fusion gate with the same enhanced probability, which is presented in Fig. 1. The advantage of using type-II fusion instead of type I as in previous proposals [4], is that this gate detects any lost photons and therefore does not introduce logical errors [18].

The phenomenon of percolation has been long studied [19] in classical statistical mechanics as a prototype phase transition on graphs that have lost some of their bonds and/or sites due to a randomized process with a probability  $1 - p$ . When  $p$  is above the percolation threshold, there exists at least one spanning path from one side of the lattice to the other. In the context of one-way LOQC, the percolation graph will define a cluster state, whose bonds or sites are effectively removed due to failure of probabilistic entangling gates together with photon loss. The percolation threshold marks a phase transition in the computational power of the resource state generated [20], which distinguishes the states that can be used for universal quantum computation from those which cannot.

Here, we exploit the  $75\%$  success probability of the boosted type-II gate, to develop a new percolation approach in which three-photon cluster states are fused together to

![](images/ceded19ff17235b9af5722d7107cd35c94ba7eb7e77204da16ebde3ab291acdc.jpg)  
FIG. 2 (color online). Full layout of a layer of the diamond graph using three-photon Greenberger-Horne-Zeilinger (GHZ) states as input. The legend at the bottom of the figure shows the role of each photon. There are two types of rotated fusion type-II gates used; their effect on the GHZ states is described in Figs. 3 and 4.

form a lattice. The underlying graph we choose is the diamond lattice, as it has the lowest vertex degree of all 3D lattices and yet it shows good percolation properties in comparison with 2D lattices with the same correlation number per site [21]. As it will be shown in Figs. 3 and 5, in our scheme, failure of a gate produces correlated bond losses as well as the appearance of bonds that do not belong to the diamond lattice form. This is very different from the uncorrelated bond loss model which is usually studied in statistical mechanics, and therefore we cannot employ existing analytic or numerical results.

The internal structure of a diamond lattice can equivalently be seen as a "brickwork" in three dimensions (Fig. 2). This picture is useful when arranging the microclusters prior to fusion, as all bonds then lie in one of three orthogonal directions. The diamond lattice is formally isotropic; however, its brickwork depiction is not; there is a greater average connectivity in the  $X$  direction and thus a preferred direction for percolation. The process by which the lattice is generated (Figs. 3 and 4) is optimized to take advantage of this anisotropy.

![](images/bc513513733a0b2723cada3bd2facb5f7968c62c69b697d5c211e05fb411d151.jpg)  
FIG. 3 (color online). Probabilistic creation of star microclusters.

![](images/961937830d85dc65a1eb608547dffb5a08d6a22d0468fc14ab6d1ad4fe32c7b4.jpg)  
FIG. 4 (color online). Fusion of five-quoit microclusters to form the final lattice.

In Fig. 2 we can see how the GHZ states are arranged to create the brickwork structure. For each site in the final lattice, we use three three-GHZ states to create a five-qubit microcluster. Each microcluster is created by performing two rotated type-II fusion gates [3], as described in Fig. 3. The five-star microcluster will be created when both fusions succeed; however, in the case of failure, the outcomes will still create connectivity in the lattice, contributing still to the percolation of the whole lattice. In the case where we have formed a five-qubit star graph state, all the qubits in the exterior are equivalent; however, in the cases where failure has happened, the way in which we arrange those external qubits affects the connectivity of the lattice. We have shown in Fig. 3 the arrangement that is most suitable for our scheme and that allows us to obtain the lowest percolation threshold.

To assess the percolation properties of the lattice, we use a Monte Carlo simulation. In each independent run, our simulation builds the lattice sequentially, modeling the action of the success and failure of the fusion gates and attempts to find a percolation path. In doing so, we achieve a more realistic picture compared to the simpler alternative of deleting nodes from a perfectly formed lattice. This approach also allows us to observe the information which will ultimately be fed to a classical percolation algorithm. For each set of parameters, the simulation is run  $10^{4}$  times to ensure that the statistical error in the data is  $\lesssim 1\%$ .

In Fig. 5 we present an instance of the lattice, where we can see why this lattice is not the typical percolated diamond lattice. The failures of some of the fusion gates produce correlated bond losses together with the appearance of new diagonal bonds that can be seen in the figure. It must be noted that the presence or absence of the bonds will be known from the pattern of successes and failures of the fusion gates. Thus, in any experimental setup, the structure of the percolated lattice could be inferred by a simple classical algorithm.

Let us define  $\Pi(p, L)$  as the probability that a lattice of linear dimension  $L$  percolates when built with fusion gates that succeed with probability  $p$ . The percolation threshold can be calculated from finite size lattices by finding the crossing point of the function  $\Pi(p, L_i)$  for different values

![](images/a708fa13c7c4d70215a98cbdbe947c341926b6f2feb8d45e68eeb9387a84f3cc.jpg)  
FIG. 5 (color online). Instance of the percolated cluster  $(10 \times 3 \times 3)$ , highlighted in blue is the spanning cluster. In addition to the orthogonal bonds which are expected in the canonical brickwork lattice, we see some diagonal bonds—these are the result of failed fusions during the creation of microclusters.

of  $L_{i}$  (a justification for this procedure can be found in the Supplemental Material [16]).

We perform the simulation by generating instances of the lattice with fusion success probability  $p$ . In Fig. 6 we have represented the results for lattices of a different linear dimension and find the value for the percolation threshold, which is estimated to be  $p_c \simeq 0.625$ . We conclude that lattices built according to our scheme, using boosted fusion gates with a success probability of  $75\%$ , are well above the percolation threshold—and are therefore universal for quantum computing.

A single qubit channel. In traditional MBQC, a single qubit is replaced by a linear cluster. When two-qubit operations are required, a bond (gate) is created between two linear clusters (qubits). In a paradigm where the creation of entanglement between qubits is probabilistic (such as in LOQC), a three-dimensional piece of the cluster state can be used to implement a single functional qubit. If there exists a spanning path through the cluster, information can flow through the channel, allowing the computation to

![](images/8c788340f9db847b44e76b4c3b98bf39c0353446fe79ae6e080866d115a41425.jpg)  
FIG. 6 (color online). Results for simulations on a bulk of cluster of  $L = 15,20,25$ . Each cluster contains  $L^3$  sites and has been generated from  $3L^3$  GHZ states.

![](images/14f4ba034e6a4ee65200242a3160820a2c963e11bc20dd0baf60d42f15729bfa.jpg)  
FIG. 7 (color online). Percolation probabilities as a function of the length, for lattices of square cross section  $L^2$ . The length of the cluster correlates to the computational depth of the lattice. The exponential decay shown has a decay constant which depends quadratically on  $L$ .

progress. We can then calculate how many operations we can perform on this single qubit.

The cluster channel is parametrized by a fixed cross section (width and height) and variable length, which corresponds to the computational depth. The cross section of this cluster is directly related to its percolation properties—a larger cross section gives a higher percolation probability. Given a desired length, we must choose a cross section in order to have a percolation probability higher than some desired probability of success. In Fig. 7 we show the percolation probability for different cross sections, as a function of the length. We have chosen square cross sections because in preliminary simulations this geometry performed better than rectangular shaped cross sections.

As we can see from Fig. 7, for a cross section of  $6 \times 6$  qubits, we can make the cluster very deep. Because of computational constraints, simulating large clusters is very challenging. We fit an exponential decay function to the data, obtaining an estimated variance of  $10^{-7}$ . From this fit we extrapolate that for  $L = 6$  we have more than  $90\%$  probability of percolation in clusters up to 9000 qubits in length.

A question that naturally arises in large-scale schemes for LOQC is tolerance to photon loss. This scheme has been designed with loss robustness from the outset. The type-II boosted fusion gates can detect all losses that happen in the photons incident in the fusion gates. Our scheme is operating above the percolation threshold for the lattice, and this headroom leads to a natural loss tolerance. The incoherence induced in the state by a loss error can be fixed by measuring neighbors of lost qubits in the  $Z$  basis, thus cutting bonds from our graph. We have simulated the building of the lattice where each photon has probability  $p_l$  of being lost, and when a loss is detected, we measure all neighbors of the lost qubits in the  $Z$  basis to cut it out. In Fig. 8, we can see the loss tolerance of a cubic lattice of  $L = 25$  in blue; in orange we have highlighted the constant success probability of  $90\%$  for comparison. The success probability of the fusion gates used has been taken to be  $75\%$ . As we can see, the probability or having a spanning path is larger than  $90\%$  for loss rates of up to  $1.6\%$ .

![](images/2516316fd675b1fe255af8edc0f300dfd89ecb73106168ea76087b95a46ffe79.jpg)  
FIG. 8 (color online). Loss tolerance (blue) for a cubic lattice of linear dimension  $L = 25$ .

We want to stress that this is a natural loss tolerance of the system. Previous proposals [4] have given thresholds for heralded loss, where the location of all loss errors in the final lattice is known. Heraldved loss is not experimentally justified in LOQC and only serves as an upper bound for loss tolerance. In order to compare our scheme with previous work, we have performed the same kind of heralded loss simulations and found that in this scenario we could tolerate loss rates up to  $15\%$ , which is an improvement of  $5\%$  on the numerical results reported in [4]. The improvement over previous proposals [4] is not only on the overall robustness of the construction, which is indicated by the  $5\%$  improvement on the heralded loss tolerance, but also the reduction of the amount of resources needed by at least an order of magnitude.

We have presented a ballistic scheme for the construction of a linear-optical cluster state that is universal for MBQC. While we have not explicitly included error-correcting codes to provide robustness to loss and errors in the photons in the final computational cluster state, the universality of the cluster state implies a number of ways forward, incorporating tree clusters [22] or the surface code [23,24] as loss-error and general error-correcting codes. Raussendorf's 3D cluster encoded surface code [25], in particular, seems well suited to ballistic generation.

To implement this scheme with only three-photon GHZ as resources we have proposed a boosted fusion mechanism based on [13] and [14] that works with  $75\%$  probability, which is well above the percolation threshold  $(p_c = 62.5\%)$  of this lattice. We have shown the robustness of the scheme in the presence of small amounts of photon loss (up to  $1.6\%$ ) and its favorable resource scaling. Even though this scheme was devised with linear optics in mind, it applies for any physical system with probabilistic gates, and if that probability is higher than  $75\%$  it might be conceivable that the resources needed could be reduced even further.

For this scheme to be implemented experimentally, it would need a near-deterministic three-photon GHZ source. It is not yet known what the optimal way of producing these photonic states is; options range from multiplexing a linear-optical circuit such as that proposed in [18], using a similar

scheme to the multiplexed single photon source such as [26], to producing a three-photon linear cluster (local Clifford equivalent to a GHZ) with a quantum dot [27]. As any linear-optical fully-loss-detecting gate must necessarily measure all photons incident on it, the three-photon GHZ is the minimal resource for a loss-detecting BSM-based ballistic scheme.

Ballistic generation of cluster states for MBQC remains the most attractive approach to scalable linear-optical quantum computing. By developing a loss-tolerant and significantly more resource-efficient scheme, we have shown that new theoretical ideas continue to ameliorate the technical challenges of building a scalable linear-optical quantum computer.

The authors would like to thank Hussain Zaidi, Aida Moreno-Moral, Martik Aghajanian, Chris Dawson, and Gabriel Mendoza for helpful discussions. T. R. and P. S. are supported by the Vienna Science and Technology Fund (WWTF) Grant No. ICT 12-041 and the Army Research Office (ARO) Grant No. W911NF-14-1-0133. M. G. S. is supported by EPSRC. The numerical simulations were possible thanks to the High Performance Cluster of Imperial College.

Note added. We would like to draw the reader's attention to the concurrent work in [28] which proposes an alternative approach to this problem.

*Corresponding author.  
m.gimeno-segovia11@imperial.ac.uk  
[1] E. Knill, R. Laflamme, and G. J. Milburn, Nature (London) 409, 46 (2001).  
[2] M. A. Nielsen, Phys. Rev. Lett. 93, 040503 (2004).  
[3] D. E. Browne and T. Rudolph, Phys. Rev. Lett. 95, 010501 (2005).  
[4] K. Kieling, T. Rudolph, and J. Eisert, Phys. Rev. Lett. 99, 130501 (2007).  
[5] P. Kok, K. Nemoto, T. C. Ralph, J. P. Dowling, and G. J. Milburn, Rev. Mod. Phys. 79, 135 (2007).  
[6] A.J.F. Hayes, H.L. Haselgrove, A. Gilchrist, and T.C. Ralph, Phys. Rev. A 82, 022323 (2010).  
[7] A. P. Lund, T. C. Ralph, and H. L. Haselgrove, Phys. Rev. Lett. 100, 030503 (2008).  
[8] J. Carolan, J.D. A. Meinecke, P.J. Shadbolt, N.J. Russell, N. Ismail, K. Wörhoff, T. Rudolph, M.G. Thompson,

J. L. O'Brien, J. C. F. Matthews, and A. Laing, Nat. Photonics 8, 621 (2014).  
[9] J. W. Silverstone, R. Santagati, D. Bonneau, M. J. Strain, M. Sorel, J. L. O'Brien, and M. G. Thompson, arXiv:1410.8332.  
[10] N. Spagnolo, C. Vitelli, M. Bentivegna, D.J. Brod, A. Crespi, F. Flamini, S. Giacomini, G. Milani, R. Ramponi, P. Mataloni, R. Osellame, E.F. Galvão, and F. Sciarrino, Nat. Photonics 8, 615 (2014).  
[11] X.-D. Cai, D. Wu, Z.-E. Su, M.-C. Chen, X.-L. Wang, L. Li, N.-L. Liu, C.-Y. Lu, and J.-W. Pan, Phys. Rev. Lett. 114, 110504 (2015).  
[12] S. Barz, R. Vasconcelos, C. Greganti, M. Zwerger, W. Dur, H.J. Briegel, and P. Walther, Phys. Rev. A 90, 042302 (2014).  
[13] W.P. Grice, Phys. Rev. A 84, 042331 (2011).  
[14] F. Ewert and P. van Loock, Phys. Rev. Lett. 113, 140403 (2014).  
[15] The best known theoretical GHZ building strategy from Bell pairs has a success probability of  $p_{\mathrm{suc}} = (1/2)^{\lfloor (n - 1) / 2 \rfloor} (3/4)^{\lceil (n - 1) / 2 \rceil}$ . Gimeno-Segovia et al. (to be published).  
[16] See Supplemental Material in http://link.aps.org/ supplemental/10.1103/PhysRevLett.115.020502 for a full resource comparison and a justification for the method of finding the percolation threshold.  
[17] J. Calsamiglia and N. Lütkenhaus, Appl. Phys. B 72, 67 (2001).  
[18] M. Varnava, D. E. Browne, and T. Rudolph, Phys. Rev. Lett. 100, 060502 (2008).  
[19] D. Stauffer and A. Aharony, Introduction to Percolation Theory (Taylor and Francis, London, 1994), Vol. 1, p. 192.  
[20] K. Kieling and J. Eisert, in Quantum and Semiclassical Percolation and Breakdown in Disordered Solids (Springer, Berlin, 2009), pp. 287-319.  
[21] Y. Y. Tarasevich and S. C. van der Marck, Int. J. Mod. Phys. C 10, 1193 (1999).  
[22] M. Varnava, D. E. Browne, and T. Rudolph, Phys. Rev. Lett. 97, 120501 (2006).  
[23] S. B. Bravyi and A. Y. Kitaev, arXiv:quant-ph/9811052.  
[24] E. Dennis, A. Kitaev, A. Landahl, and J. Preskill, J. Math. Phys. (N.Y.) 43, 4452 (2002).  
[25] R. Raussendorf, J. Harrington, and K. Goyal, Ann. Phys. (Amsterdam) 321, 2242 (2006).  
[26] D. Bonneau, G.J. Mendoza, J.L. O'Brien, and M.G. Thompson, New J. Phys. 17, 043057 (2015).  
[27] N. H. Lindner and T. Rudolph, Phys. Rev. Lett. 103, 113602 (2009).  
[28] H. A. Zaidi, C. Dawson, P. van Loock, and T. Rudolph, Phys. Rev. A 91, 042301 (2015).