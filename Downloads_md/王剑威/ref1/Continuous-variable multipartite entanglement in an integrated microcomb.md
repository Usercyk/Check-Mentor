# Continuous-variable multipartite entanglement in an integrated microcomb

https://doi.org/10.1038/s41586-025-08602-1

Received: 16 April 2024

Accepted: 7 January 2025

Published online: 19 February 2025

Open access

Check for updates

Xinyu Jia $^{1,2,9}$ , Chonghao Zhai $^{1,9}$ , Xuezhi Zhu $^{3,9}$ , Chang You $^{1}$ , Yunyun Cao $^{3}$ , Xuguang Zhang $^{4}$ , Yun Zheng $^{1}$ , Zhaorong Fu $^{1}$ , Jun Mao $^{1}$ , Tianxiang Dai $^{1}$ , Lin Chang $^{4}$ , Xiaolong Su $^{3,5}$ , Qihuang Gong $^{1,5,6,7,8}$  & Jianwei Wang $^{1,5,6,7,8}$

The generation of large-scale entangled states is crucial for quantum technologies, such as quantum computation<sup>1</sup>, communication<sup>2</sup> and metrology<sup>3</sup>. Integrated quantum photonics that enables on-chip encoding, processing and detection of quantum light states offers a promising platform for the generation and manipulation of large-scale entangled states<sup>4,5</sup>. Generating entanglement between qubits encoded in discrete variables within single photons is challenging, owing to the difficulty of making single photons interact on photonic chips<sup>6-11</sup>. Devices that operate with continuous variables are more promising, as they enable the deterministic generation and entanglement of qumodes, in which information is encoded in light quadratures. Demonstrations so far have been limited to entanglement between two qumodes<sup>12-20</sup>. Here we report the deterministic generation of a continuous-variable eight-mode entanglement on an integrated optical chip. The chip delivers a quantum microcomb that produces multimode squeezed-vacuum optical frequency combs below the threshold. We verify the inseparability of our eight-mode state and demonstrate supermode multipartite entanglement over hundreds of megahertz sideband frequencies through violation of the van Loock-Furusawa criteria. By measuring the full matrices of nullifier correlations with sufficiently low off-diagonal noises, we characterize multipartite entanglement structures, which are approximate to the expected cluster-type structures for finite squeezing. This work shows the potential of continuous-variable integrated photonic quantum devices for facilitating quantum computing, networking and sensing.

The basic units of quantum information are quantum bits (qubits) or quantum modes (qumodes). They can be physically represented in discrete-variable or continuous-variable quantum systems, for example, optical, atomic, superconducting and mechanical systems. A key objective is to entangle a large number of qubits or qumodes. Achieving large-scale entanglement of light is pivotal for advancing quantum technologies in computation<sup>1</sup>, networking<sup>2</sup> and metrology<sup>3</sup>. Universal optical quantum computation can be achieved by a sequence of measurements performed on large entangled cluster states<sup>21,22</sup>. With light, qubits are typically encoded in discrete modes of single photons<sup>23</sup>, whereas qumodes are encoded in continuous quadratures of light fields<sup>24</sup>. Discrete-variable encoding in single-photon allows ultrahigh-fidelity qubit operations but currently faces challenges in deterministic qubits generation and entanglement. It has led to impressive demonstrations of quantum information processing in discrete-variable experiments using probabilistic multi-qubit entanglement<sup>23</sup>. By contrast, continuous-variable encoding in light quadratures allows for deterministic generation and entanglement of qumodes,

at the expense of lower fidelity. The multiplexing of light in various degrees of freedom, for example, path $^{25,26}$ , time $^{27,28}$ , frequency $^{29-31}$  and spatial eigenmodes $^{32,33}$ , presents a promising approach to creating large-scale continuous-variable cluster states.

Integrated quantum photonics is a versatile platform that can on-chip encode, process and store quantum information of light $^{4,5}$ . Discrete-variable integrated quantum photonics (DVIQP) technologies have yielded integrated sources, circuits and detectors for single photons $^{6,34}$ , multi-qubit genuine entanglement $^{7,8}$ , as well as proof-of-principle demonstrations in quantum computing $^{9,10}$  and networking $^{11}$ . Continuous-variable integrated quantum photonics (CVIQP) is anticipated to provide high complexity, phase stability, precise mode matching, mode-cleaning-free and low interfacing loss, throughout the generation, manipulation and detection of quadratures of light. Recent advancements in integrated photonic materials and technologies have markedly progressed CVIQP. It includes the observation of single-mode and two-mode quadrature squeezed states (that is, Einstein-Podolsky-Rosen, EPR, states) in optical waveguides $^{12-14}$ ,

<sup>1</sup>State Key Laboratory for Mesoscopic Physics, School of Physics, Peking University, Beijing, China. <sup>2</sup>Beijing Academy of Quantum Information Sciences, Beijing, China. <sup>3</sup>State Key Laboratory of Quantum Optics Technologies and Devices, Institute of Opto-Electronics, Shanxi University, Taiyuan, China. <sup>4</sup>State Key Laboratory of Advanced Optical Communications System and Networks, School of Electronics, Peking University, Beijing, China. <sup>5</sup>Collaborative Innovation Center of Extreme Optics, Shanxi University, Taiyuan, China. <sup>6</sup>Frontiers Science Center for Nano-optoelectronics & Collaborative Innovation Center of Quantum Matter, Peking University, Beijing, China. <sup>7</sup>Peking University Yangtze Delta Institute of Optoelectronics, Nantong, China. <sup>8</sup>Hefei National Laboratory, Hefei, China. <sup>9</sup>These authors contributed equally: Xinyu Jia, Chonghao Zhai, Xuezhi Zhu. <sup>10</sup>e-mail: suxl@sxu.edu.cn; jww@pku.edu.cn

![](images/302900f4d06c364ad70e3e86d8391e281762c7441722fe62310ec444af263665.jpg)  
Fig.1|Continuous-variable multipartite entanglement in an integrated-optical below-threshold microcomb. a, Coherent polychromatic phase-locked optical frequency combs (solid lines) are adopted to externally excite an integrated optical microresonator. b, In the microresonator, Kerr nonlinear-optic processes take place that operate below the threshold of parametric oscillation, and quantum frequency modes (Qi, dotted lines) are emerging in the microcombs. The FSRs of pump combs and microcombs satisfy  $\Delta f_{\mathrm{pump}} = m\Delta f_{\mathrm{cavity}}$  (where  $m$  is an integer). The microresonator can be controlled by an upper microheater to match the pump combs. The parametric processes, including spontaneous pair squeezing and Bragg scattering in the microresonator, result in the generation of complex Gaussian states of quantum frequency

circuits $^{15,16}$  and microresonators $^{17-19}$ . Multiple pairs of two-mode EPR states have been demonstrated in a squeezeer array for Gaussian boson sampling $^{35,36}$  and in a single microresonator-based frequency comb in which only two-mode entanglement is produced $^{20}$ . Recently, second-order single-photon correlations have been studied in soliton microcombs, which implies underlying multimode entanglement dominated by spontaneous parametric processes $^{37}$ . However, the generation and detection of continuous-variable multi-qumode or multipartite entanglement remain unknown in integrated quantum photonic platforms.

Here we report the first generation of continuous-variable multipartite entanglement on an integrated-optical quantum chip. An integrated-optical microresonator-based frequency comb (that is, microcomb) was operated to generate multimode Gaussian states in the below-threshold quantum frequency modes. The inseparability of eight frequency qumodes was demonstrated by violating the positive partial transposition (PPT) criteria. We show that, owing to the Bragg scattering effect in the microcomb, multipartite entanglement

modes, which can be linearly transformed to the eigen-supermodes (that is,  $Q_{\mathrm{e}}1$ ,  $Q_{\mathrm{e}}2$ , ...,  $Q_{\mathrm{e}}n$ , a superposition of frequency modes) with marked intrinsic squeezing, and further generate the supermode-based multipartite entangled states with various cluster-type structures. c, Approximate cluster-type states of multiple supermodes (that is,  $Q_{\mathrm{c}}1$ ,  $Q_{\mathrm{c}}2$ , ...,  $Q_{\mathrm{c}}n$ ) can be generated. The structure of multipartite entanglement can be reconfigured by tailoring the configurations of polychromatic pump beams and the measurement bases of local oscillator beams. In the graphical representation of multipartite entangled states, blue vertexes represent supermodes and black edges all equal to 1 represent deterministic entanglement.

with cluster-type structures cannot be directly generated in the frequency modes but rather in the supermodes, distinguishing the mechanics of multipartite entanglement in the microcomb from that in second-order squeezing processes. A coherent polychromatic pump-detection (CPPD) technique was adopted for the preparation, manipulation and measurement of multipartite entanglement with phase coherence throughout the system. Using experimental violations of the van Loock-Furusawa criteria, we validated the generation of various supermode multipartite entanglement. By the measurement of the full matrices of nullifier correlations with total off-diagonal correlations amounting to approximately  $4 - 8\%$  of diagonal correlations, we characterized entanglement structures of the generated states, which are approximate to the corresponding cluster-type structures for finite squeezing. Also, quadrature squeezing and multipartite entanglement were detected across broad sideband frequencies. Our results indicate the possibility of generating and processing large-scale entanglement on CVIQP chips for scalable photonic quantum technologies.

![](images/1fa4cdc6636c9da9b83ee62a150e4f9b373f05753db0076503050bd0b3e03d10.jpg)

![](images/cd4d23f333ed54fc9bf0e6a31d39eaa3c6ecae1c308cca38cde02133b2070a57.jpg)

![](images/e7810cedfd6884440e2023ce7bf590b1ab2fff51e8f473e3bc813279c7e5f08e.jpg)

![](images/0005da179c878f83c68b8c7d25e42888f23bfa28efe55782a3a18f3f63c7c85e.jpg)

![](images/b908f005b7c01210e28e843b4a29705ce791b11d62adeb4387b8dc1cc912f889.jpg)

![](images/b128179ab8823cce9d62a7c86d993d488124c9eaa2eb92d545bfcf5240afd9a2.jpg)  
Fig. 2 | An integrated silicon nitride microcomb and setup for the generation and characterization of continuous-variable multi- qumode entanglement. a, Photograph for chip carrier. The chip is fibre-coupled in and out using lensed single-mode fibres. The integrated microheater is controlled by d.c. probes. b, Optical microscope image for a fabricated silicon nitride microring microresonator with a radius of  $114\mu \mathrm{m}$ . c,d, False-colour scanning electron microscope images for single-mode waveguide with a cross-section of  $1\mu \mathrm{m} \times 800\mathrm{nm}$ , and a 400-nm gap between bus waveguide and microring. e,f, Measured spectra of electro-optic combs and the microring with an FSR of 39.98 GHz and 199.9 GHz, respectively. In the electro-optic combs, lights at the frequencies of  $P_{\pm 3,0}$  are selected as pumps (green windows), whereas those at  $f_{\pm 1,\pm 2,\pm 4,\pm 5}$  (orange windows) are selected as the local oscillator beams. In the microresonator, below-threshold multimode Gaussian states are generated at the frequencies of  $f_{\pm 1,\pm 2,\pm 4,\pm 5}$ . g, The CPPD experimental setup. A low-noise continuous-wave (CW) laser at 1,550 nm is modulated by three cascaded EOMs

Figure 1 shows the processes to generate continuous-variable multipartite entanglement with approximate cluster-type structures in the integrated microcomb. When the microresonator is pumped by synchronous phase-locked polychromatic beams $^{29,30}$ , parametric nonlinear-optic processes below the oscillation threshold can lead to the generation of quantum frequency squeezed vacuum modes. Taking the mean-field approximation for the bright pumping beams, the interacting Hamiltonian of quantum modes can be written as $^{37}$

$$
\hat {H} = - \hbar \kappa \left\{\sum_ {i, j, k, l} ^ {\mathrm {S P S}} \delta_ {1} \left(A _ {i} A _ {j} \hat {a} _ {k} ^ {\dagger} \hat {a} _ {l} ^ {\dagger} + \mathrm {h . c .}\right) + \sum_ {i, j, k, l} ^ {\mathrm {B S}} \delta_ {2} \left(A _ {i} ^ {*} A _ {j} \hat {a} _ {k} ^ {\dagger} \hat {a} _ {l} + \mathrm {h . c .}\right) \right\} \tag {1}
$$

where  $\delta_{1} = \delta_{\omega_{k} + \omega_{l},\omega_{i} + \omega_{j}}$  and  $\delta_{2} = \delta_{\omega_{i} + \omega_{k},\omega_{j} + \omega_{l}}$  represent simplified phase matching conditions for the spontaneous pair squeezing (SPS) and Bragg scattering (BS) processes, respectively,  $\kappa$  is the nonlinear coupling coefficient,  $A_{i}$  is the classical amplitudes of pumps and  $\hat{a}$  and  $\hat{a}^{\dagger}$  represent the bosonic operators of qumodes. Notably, the presence

to produce electro-optic combs. One wave-shaper is used to tailor the pump and local oscillator beams. Three pumps are used to synchronously excite the microcomb to generate the multimode Gaussian states. Polychromatic homodyne detections, in which the local oscillators are reprogrammed with intensities and phases, are adopted to characterize and reconfigure the multipartite entangled states of supermodes. Quantum noises are recorded using a spectrum analyser. The polychromatic pumps and polychromatic local oscillators for homodyne detections are split from the same electro-optic comb, so that they are highly coherent throughout the system. RF Gen, radio-frequency generator; EOM, electro-optic modulator; AMP, electronic amplifier; EPS, electronic phase shifter; PC, polarization controller; EDFA, erbium-doped fibre amplifier; PID, proportional integral derivative; BS, fibre beamsplitter; CV, continuous variable. Orange lines indicate single-mode optical fibres and blue lines indicate electric cables. Scale bars,  $100\mu \mathrm{m}$  (b); 500 nm (c);  $1\mu \mathrm{m}$  (d).

of the Bragg scattering process (that is, absent in second-order nonlinear processes) makes a substantial difference when generating continuous-variable multipartite entanglement. In the microcomb, the distribution of intrinsic squeezing of multimode Gaussian states at different sideband frequencies is governed by the quantum Langevin equations<sup>38</sup>:

$$
\frac {\mathrm {d} \hat {\mathbf {x}} (t)}{\mathrm {d} t} = (M - \Gamma) \hat {\mathbf {x}} (t) + \sqrt {2 \Gamma} \hat {\mathbf {x}} _ {\text {i n}} (t), \tag {2}
$$

where  $\hat{\mathbf{x}} = (\hat{q}_1,\hat{q}_2,\dots ,\hat{q}_n|\hat{p}_1,\hat{p}_2,\dots ,\hat{p}_n)^\mathrm{T}$  is the vector of quadratures,  $\hat{q}_k = \hat{a}_k^\dagger +\hat{a}_k,\hat{p}_k = i(\hat{a}_k^\dagger -\hat{a}_k),\hat{\mathbf{x}}_{\mathrm{in}}$  is the quadrature vector of input fields that satisfy the input-output relation  $\hat{\mathbf{x}}_{\mathrm{in}}(t) + \hat{\mathbf{x}}_{\mathrm{out}}(t) = \sqrt{2T}\hat{\mathbf{x}} (t)$ $M = i[\hat{H}_{\mathrm{int}},\hat{\mathbf{x}} ] / \hbar$  and  $\Gamma = \mathrm{diag}(\gamma_1,\gamma_2,\dots ,\gamma_n|\gamma_1,\gamma_2,\dots ,\gamma_n)$  are the gain and damping matrices, respectively.

In Fig. 1, feeding excitations by large-number phase-locked synchronous polychromatic beams, for example, from one external coherent optical frequency comb, large-scale entangled multimode Gaussian

![](images/a80cf75633e41db1175418acdf89c0c25338816868662793d8811e9a4296aa62.jpg)  
Fig. 3 | Generations and characterizations of multimode squeezing. a, Experimental symplectic eigenvalues for all bipartitions of the eight-mode Gaussian state in the frequency comb modes. All symplectic eigenvalues are estimated to be below 1 (green dotted line), experimentally violating the PPT criteria for all bipartitions. b, Phase diagram for the six dominant eigensupermodes (that is,  $Q_{\mathrm{e}}1 - Q_{\mathrm{e}}6$ ). Blue ellipses represent the quadrature squeezing and anti-squeezing, whereas red circles represent vacuum fluctuations. c, Direct experimental measurement of noise powers for the six eigen-supermodes. Grey lines indicate the shot noise level, green lines are noise curves measured by periodically ramping the local oscillator phase. The red lines are measured by squeezing with locked phases and the orange lines are measured by antisqueezing with locked phases. d, Measured covariance matrix for the eight eigensupermodes (that is,  $Q_{\mathrm{e}}1 - Q_{\mathrm{e}}6$ ). The matrix is coded by colours with the key at the top. e, Quadrature squeezing and anti-squeezing of eight eigen-supermodes at different sideband frequencies. Points are experimental data, and lines are theoretical results of equation (2). The supermodes are doubly degenerate in theory, whereas they are experimentally discernible (indicated by those points with two similar colours). Data in a-d were collected at the 5 MHz sideband frequency.

![](images/5ae11578c6a58f44cac8f435824970b5a9821a8649f699bb68aff0577702b01d.jpg)

![](images/1a160dd33f53755304bd8f1a3b171262446a3e0a19f8a96f5c38589b1e4e9f90.jpg)

![](images/7f844066a6c1a34d25ed5b8786d415ba98de46421feb4d28fa37f0354eef0756.jpg)

![](images/499169e290441d6578ecf0bbf84801cb3fdf5eb4f3f31b983534178c532f5df3.jpg)

states could be generated in the microcomb. Instead of directly detecting the entanglement structure in the frequency comb modes (Q), we extract the eigen-supermodes  $(\mathrm{Q_e})$  and use them to generate multimode cluster-type states with various structures in corresponding supermodes  $(\mathrm{Q_c})$ . The supermode can be regarded as a superposition of frequency comb modes up to a linear transformation<sup>30</sup>. Measuring the states on the basis of eigen-supermodes, intrinsic quadrature squeezing and the degree of multimode entanglement can be characterized, which is carried out by polychromatic homodyne detections by tailoring the local oscillator beams. Moreover, entanglement structures can be reshaped by reconfiguring linear-optical Gaussian transformations through the polychromatic local oscillators<sup>39,40</sup>, together with dedicated controls of the polychromatic pumps. The CPPD method enables

precise and efficient generation, manipulation and measurement of large-scale entanglement in the frequency domain. In this study, we benchmark that with eight frequency qumodes as an example. The procedure for the generation, manipulation and measurement of supermode multipartite entangled states with various structures is provided in Supplementary Information section 2.1.

Figure 2a-d shows the quantum microcomb device fabricated in silicon nitride nanophotonic waveguides. It is considered an interesting integrated quantum photonic platform, possessing low optical loss, strong third-order nonlinearity, dense integration and complementary metal-oxide-semiconductor compatibility $^{35,41-43}$ . In the microring resonator, an anomalous dispersion is achieved by tailoring the structural dispersion of the waveguide (Supplementary Fig. 1). A large mode spacing of about 200 GHz free spectral range (FSR) enables well separation of combs, suppressing parametric fluorescence noises and non-parametric effects. Overcoupling is used to efficiently extract (about  $90\%$ ) squeezed light out of the cavity. A high intrinsic quality factor of 1 million is measured in Supplementary Fig. 1. In the experiment, the microring is tuned by an upper thermo-optical resistive microheater, to lock the resonant frequencies (Fig. 2f) to the frequencies of electro-optic (EO) pump combs (Fig. 2e), which were produced by modulating an ultralow noise laser at 1,550.245 nm (193.518 THz). The comb spacing of electro-optic combs is aligned with the mode spacing of microcombs having  $\Delta f_{\mathrm{cavity}} = 5\Delta f_{\mathrm{EO}}$ .

Figure 2g shows the CPPD experimental setup. The use of polychromatic pump and polychromatic homodyne detection technologies $^{30,31}$  played a crucial part in creating the first (to our knowledge) integrated-optic continuous-variable multipartite entanglements specifically implemented in the frequency domain, rather than others. Our CPPD combines these advanced technologies to achieve global phase-locking throughout polychromatic pumping and detection processes. Using a wave-shaper, the electro-optic combs of  $P_{\pm 3,0}$  serve as phase-locked pumps for synchronously polychromatic pump, whereas the combs of  $f_{\pm 1,\pm 2,\pm 4,\pm 5}$  serve as the local oscillators for polychromatic homodyne detection. The phases of the squeezed and local oscillator beams are inherently stable because of the coherent nature of the electro-optic combs. Moreover, the comb at  $f_{+3}$ , interfering with the post-beam splitter, is repurposed as a reference for globally locking the relative phase between the local oscillators and squeezed beams. This method enables precise measurements of quadrature squeezing, multimode entanglement and a comprehensive characterization of the covariance matrix of the generated states, all within a unified global phase-locking reference frame. In the experiment, monochromatic, bichromatic and polychromatic homodyne detections were implemented by tailoring the intensities and phases of local oscillators (Supplementary Fig. 3).

![](images/71afc482dbada9fd08de8ea1aa9b1d3f20c7fdd7f0a0dc8ae47065d8bd96f757.jpg)  
a

![](images/cbe528c9d3b8d156f7924592c5679b85531df3ec0db69c0eee02882cfc3468eb.jpg)  
b

![](images/06c76d242b6308684c48517461c6a5e9f3a224a603bf902774abed23916bfa6f.jpg)

![](images/b4a57eb777e7f9b6649660436c2b94e1cabb783b86ad6d168347070d0bfc9ae8.jpg)

![](images/d1a1e43d2d0e859f576d22baad012a3a0726c2cd36fef0800e0b8b96d5d2cbb3.jpg)

![](images/bcb8e7aba6d11bec008674e34044b335e5a7a61dc8afc31486ef2c082278b325.jpg)

![](images/ae80d112dfe82e16f9113e058f381e5cc4052fc331337ac431b1a1d3cfa6ded0.jpg)  
Fig. 4| Experimental measurements of nullifiers and violations of the van Loock-Furusawa inequalities. a, Direct experiment measurement of noise powers for the four nullifiers of the linear-type entanglement structure. The nullifier variances  $\{1.349(7), 1.874(10), 1.874(10), 1.347(8)\}$  are normalized to the shot noise (grey lines) with a rescale number of  $\{2, 3, 3, 2\}$ , respectively. Values in parentheses are  $\pm 1\sigma$  uncertainty, each of which is estimated from a full set of 400 data points. The grey regime above the shot noise represents the absence of squeezing, whereas the orange regime represents the presence of strong squeezing. b, Graphical representations of various cluster-type entanglement structures in supermodes ( $Q_{c}i$ ), including the linear-, box- and star-type

![](images/50fbe87b550780343ec24fb6e45dce7f071af29a63e5d153290825eb17ed69cf.jpg)

![](images/a8baf29bd8ca61f15e12af3c175206efaa0ee94f5550265672a78e71766dbbc4.jpg)  
C

![](images/0ca348b91ac31ab4c6f02c3dcae515c0856a53aac9a6673129771ccfcb7fe2be.jpg)

![](images/5fbde5f5a2a4a7e08f0000b2f0e2afb33b6aa3bde4f8febab0cfe46e3732b987.jpg)

![](images/a7367d4c1d34205d0ea95e71cff37185821fd1fa98d60abd250d37fc02e119e4.jpg)

![](images/aeaa1b7c17b7e5876e0c450934837f1e9e8ba1645e99f9a7ca7aa0f001c68343.jpg)  
d

![](images/2421ae6338332fab7a821f7d767154362413c2638f51d01497f759ea7cff1144.jpg)

![](images/0ff09a627a5525aabb6a3daebc04f983341aefa2a465728538a4d85178c1180b.jpg)

![](images/131797d6d03cb3033b7ea573ba58ff6cfa145cdc9c8ca4f4e83a1a7882af4f48.jpg)  
entanglement structures. c, d, Experimentally measured  $\mathcal{L}\mathcal{F}$  values at the 5 MHz sideband frequency in c and at different sideband frequencies in d, for the corresponding entangled states. If the measured  $\mathcal{L}\mathcal{F}$  value is less than 4, the inequality is violated. Coloured data in c and d represent measured inequalities for different edges in b. If all inequalities are violated for all edges, we confirm the successful generation of multipartite entanglement. In c and d, in the orange regimes, all of the van Loock-Furusawa inequalities are experimentally violated, demonstrating the presence of multipartite entanglement at broad frequencies.

We choose 5 MHz as the basic sideband frequency in an experiment to accurately characterize quadrature squeezing and multipartite entanglement. More details are provided in Supplementary Information section 1.

We first verify the entanglement of eight frequency modes by the experimental violations of the continuous-variable version of PPT criteria $^{44}$ . If a state of the composite system can be decomposed into a product state of two subsystems, partially transposing one subsystem will still generate a physical state with symplectic eigenvalues greater than or equal to one. Conversely, if the partially transposed state has a symplectic eigenvalue less than one, the original state is proven to be inseparable. There are in total 127 different bipartitions for the eight-qumode Gaussian states, including  $\{1 \times 7, 2 \times 6, 3 \times 5, 4 \times 4\}$  bipartitions. Figure 3a shows the symplectic eigenvalues for their partially transposed states, estimated from the measured covariance matrix in the frequency modes, as shown in Supplementary Fig. 4). For all 127 bipartitions, the symplectic eigenvalues are less than one, which indicates that the eight-qumode state cannot be decomposed into any direct product of two separate subsystems. Violating the PPT criteria, therefore, demonstrates the presence of multipartite entanglement. The intrinsic eight-qumode state on-chip is also expected to possess much stronger entanglement (Supplementary Fig. 7).

Applying the Bloch-Messiah decomposition of the measured covariance matrix in Supplementary Fig. 4, we extracted the eigen-supermode bases. In the experiment, we carried out polychromatic homodyne detection to directly characterize squeezing for all the eight eigen-supermodes. For example, Fig. 3b,c shows the measured results for the six dominated squeezed eigen-supermodes selected to prepare multipartite entanglement with cluster-type structures. It acquires four supermodes with about 2 dB squeezing (on-chip 6 dB), and two supermodes with about 1.0 dB squeezing (on-chip 2.6 dB). The intrinsic on-chip squeezing in each supermode and the configuration of LO combs in polychromatic detections are provided in Supplementary Fig. 4. The measured full covariance matrix of all eight eigen-supermodes is reported in Fig. 3d, showing the essential orthogonality of supermodes with minimal off-diagonal terms, crucial for generating and validating multipartite entangled states. We remark that, in the frequency modes, the covariance matrix in Supplementary Fig. 4 exhibits strong off-diagonal correlations, stemming from the intrinsic Bragg scattering effect in the microcomb, which implies direct generation of multipartite entanglement with cluster-type structures is unattainable in the frequency modes through any Gaussian local unitaries $^{45,46}$  (Supplementary Information section 2.4). Instead, the generation of such entanglement can occur in the supermodes of

![](images/39f7cccfe977596590115d155a0b0de84524f90ffdca4cc391db348bd1bf08d1.jpg)  
a

![](images/f3085439f986cbfeeae5a783f0c9f622cfc5974dc760da4d32c832be7665e5ce.jpg)

![](images/5454f4375b489607aa84f405824946ecefd6d4c8494f313c964f4b2e4fc5072a.jpg)

![](images/bce1b342d9831658d4a2a3eacb08298e18c678431343afd4bafcb0169f97f643.jpg)

![](images/27dc6767fc212503fd43d6aac50fa3bae2b6f66abbcbd611f5e1802c6ff77a5f.jpg)  
b

![](images/77c816c4ae081646bca04fe3954cfcb3271327a475ef7fdd85e495fa57bb5682.jpg)

![](images/16dc125a46c55426a53bb61a3406c74382f02e4622626b735922ce229e86aef4.jpg)

![](images/1ac206969bd1546fc407ed40adb174a7b9bcf92feeda50bd2aa029cc628cf1da.jpg)

![](images/ac8a0f4655bb3ee3b0c2101108ace827d2b0e64931fab292f55aecf2652da4da.jpg)  
c  
Fig. 5| Full characterizations of nullifier correlations for various multipartite entanglement. a, Graphical representations of the linear-, box- and star-type entanglement structures. The transformed supermodes are denoted by  $Q_{c}i$ . b, Simulation results. c, Experimental results of full matrices of nullifier correlations for the on-chip generated entangled states with linear-, box-, and star-type entanglement structures. Simulation results are estimated from the measured squeezing distribution of eigen-supermodes

![](images/06a4a1815ec0c1627ae1e08f4e6c767ca8c3409a8b853081e88628882dfff8fe.jpg)

![](images/76301e9ed4e3c821f5fdee1b27e3d7dc786745d7ba17d2b5eba2b481c822bd83.jpg)  
for each entanglement structure. All matrices closely resemble an identity matrix scaled by a constant  $\lambda$ , as shown in Supplementary Table 1. The corresponding  $\gamma$  values, displayed at the top, indicate sufficiently lower off-diagonal correlations compared with diagonal correlations in our simulation and experiment. The nullifier correlation matrix is coded by colours by its absolute value (| $\operatorname{cov}(\mathcal{N}_i, \mathcal{N}_j)|$ ) and the key is provided at the bottom right. The value of each element is explicitly shown for clarity.

![](images/1b7ffa125da42f11ea7fc8a88d66fb7dc3d1ab80e4c0a15feaa28ef1a84a2005.jpg)

the microcomb, by applying non-local multimode operations on the selected eigen-supermodes (Supplementary Information section 2.1 and Supplementary Fig. 5). Results in Fig. 3 indicate an instance of multimode squeezing, whereas the squeezing strengths of eigen-supermode squeezers would be tailored by reconfiguring the polychromatic pumps for various entanglement structures.

Applying linear operations on the eigen-supermode squeezers shown in Fig. 3b allows arbitrary preparation of supermode cluster states with various entanglement structures for infinite squeezed Gaussian states<sup>39</sup>. In practice, owing to finitely squeezed states, it allows for the creation of approximate cluster states, provided the squeezing strengths for the squeeze array can be finely adjusted to match their optimal distribution (Supplementary Information section 2.1). The continuous-variable cluster states in the limit of infinite squeezing can be defined as the multimode Gaussian states  $(\hat{p}_i - \sum_j \nu_{ij} \hat{q}_j) \to 0, i, j \in G$ , where  $G$  is a graph whose vertices represent qumodes and edges represent entanglement, and adjacent matrix  $\nu$  determines the entanglement edge, as shown in Fig. 1. The nullifiers  $\mathcal{N}_i$  for cluster states are defined as

$$
\mathcal {N} _ {i} = \hat {\boldsymbol {p}} _ {c, i} - \sum_ {j} \mathcal {V} _ {i j} \hat {\boldsymbol {q}} _ {c, j}, \tag {3}
$$

where the subscript  $c$  denotes the transformed  $Q_{c}$  supermodes. In our experiment, we linearly operated the polychromatic local oscillators (equivalent to applying linear transformations on the multimode Gaussian states $^{31}$ ) and finely tailor the intensity and detuning of polychromatic pumps to obtain the theoretically acquired squeezing strength of eigen-supermode squeezers, so as to prepare multipartite entanglement with cluster-type structures.

We then verify the violations of the van Loock-Furusawa inequalities for multipartite entangled states with different entanglement structures:

$$
\mathcal {L F} = \left\langle \left(\Delta \mathcal {N} _ {i}\right) ^ {2} \right\rangle + \left\langle \left(\Delta \mathcal {N} _ {j}\right) ^ {2} \right\rangle \geq 4, \tag {4}
$$

where the  $\mathcal{LF}$  represents the van Loock-Furusawa values measured in experiment. Figure 4a reports the four measured nullifiers (normalized to vacuum fluctuations) for the four-supermode entangled state with the linear-type entanglement structure. The nullifier variances  $\{1.349(7), 1.874(10), 1.874(10), 1.347(8)\}$  are obtained. The values in parentheses is  $\pm 1\sigma$  uncertainty. This results in experimental violations of all the three van Loock-Furusawa inequalities with values of  $\{3.223(13), 3.748(17), 3.221(13)\}$  in Fig. 4c. The violations of inequalities successfully demonstrate linear-type multipartite entanglement structure. Moreover, we experimentally measured the nullifiers and inequalities for the four-supermode box- and star-type entanglement structure, and the six-supermode linear-type entanglement structure, as shown in Fig. 4b. Results of measured  $\mathcal{LF}$  are reported in Fig. 4c. It is verified that multipartite entangled states, up to six supermodes, with different entanglement structures can violate the inequalities. The full set of nullifiers and inequalities as well as their experimental results are provided in Supplementary Table 2.

Moreover, as the violations of inequality (equation (4)) are insufficient for characterizing the full entanglement information in the generated states, especially for finite squeezing $^{46}$ , we conducted a comprehensive analysis by measuring the full matrices of nullifier correlations for the inferred on-chip states. The results are shown in Fig. 5.

It shows that the off-diagonal correlations are sufficiently lower than the diagonal correlations. This is a result of the precise adjustments made to the pump configurations to match the squeezing strength of squeezers for different states. To quantify the extent of additional hidden entanglement that may not be captured within the cluster structures of the generated states, we introduce a  $\gamma$ -factor that describes a suppression of the summed off-diagonal correlations in comparison to the diagonal correlations:

$$
\gamma = \max  _ {i} \sum_ {j = 1, j \neq i} ^ {n} \frac {\left| \operatorname {c o v} \left(\mathcal {N} _ {i} , \mathcal {N} _ {j}\right) \right|}{\left| \operatorname {c o v} \left(\mathcal {N} _ {i} , \mathcal {N} _ {i}\right) \right|}, \tag {5}
$$

where  $|\operatorname{cov}(\mathcal{N}_i, \mathcal{N}_j)|$  represent the absolute value of nullifier correlations. With the optimized squeezing distribution, the correlation matrices and corresponding  $\gamma$  values of {0.058, 0.048, 0.101, 0.109} reported in Fig. 5c are measured for the four generated states in our experiment, which match with the simulation results in Fig. 5b derived from the measured squeezing distribution of the eigen-supermodes. The simulation results in Fig. 5b indicate the optimal achievable values of  $\gamma$  to be {0.007, 0.019, 0.006, 0.016} for the current experimental pump configurations. The discrepancy from the diagonal matrices in theory arises from slight deviations in the configurations of polychromatic pumps and polychromatic local oscillators from their ideal settings. These results indicate that the cluster structures efficiently capture almost all the entanglement information in our experiment, closely approximating the characteristics of the corresponding cluster-type states. Future enhancements to the experimental system will enable a more accurate characterization of the generated multipartite entanglement. Details are provided in Supplementary Information sections 2.1 and 3.3.

The observed quadrature squeezing and multipartite entanglement strongly depend on the sideband frequencies involved in their measurements. Excess noise distributions at the sideband could destroy squeezing as well as entanglement at the low sideband frequencies. Moreover, in the presence of the Bragg scattering effect, the true covariance matrix at high sideband frequencies can be far from real-symmetric but Hermitian and cannot be fully captured by homodyne detections $^{38}$ . Figure 3e shows the squeezing levels of the eight eigen-supernodes at broad sideband frequencies, estimated from their measured covariance matrices. Theoretical results modelled by the quantum Langevin equation (2) (with the inclusion of system loss) and experimental results are in good agreement (Fig. 3e), considering the incompleteness of standard homodyne detections $^{48}$ . Notable quadrature squeezing greater than 1 dB has been observed across the broad sideband. Furthermore, in Fig. 4d, at different sideband frequencies, we measured the violations of inequalities for different cluster states. The inequalities are successfully violated for all four-qumode cluster states (linear, box and star cluster states) at up to about 200 MHz sideband frequencies, and for the six-qumode linear cluster state at up to about 100 MHz sideband frequencies. These results indicate the robustness of multi-qumode entanglement against low-frequency excess noises, which is substantial for practical implementations.

In summary, we have demonstrated chip-scale deterministic generation of continuous-variable multipartite entanglement in an integrated optical microcomb and verified entanglement by experimental violations of the van Loock-Furusawa criteria. We have measured the full nullifier correlations to characterize multipartite entanglement structures of the generated states, which are closely approximated to the corresponding cluster-type structures $^{45-47}$ . This demonstration was made possible by a thorough exploration of the physical mechanisms underlying multipartite entanglement generation in microcombs, coupled with the coherent integration of advanced polychromatic pumping-detection schemes and technologies $^{30,31,39,40}$ . Despite working with small-scale entangled states and modest squeezing levels,

leveraging the unique capabilities of integrated photonics opens avenues for further scaling and enhancement (see discussions in Supplementary Information section 4). Scaling the number of entangled qumodes to hundreds or thousands can be facilitated by using larger microcomb sizes, using broadband microcombs $^{49}$  or using soliton combs as polychromatic pumps $^{37}$ . Furthermore, multiplexing frequency modes with path and temporal modes in integrated photonics platforms offers a pathway for further increasing the size of entangled states. Dedicated optimizations of the escape efficiency of squeezed beams in ultrahigh-Q microresonators can lead to enhanced squeezing $^{50}$ . The scalability and capability of CVIQP technologies could be ultimately unlocked by co-integrating continuous-variable quantum light sources, linear-optic quantum circuits and homodyne detectors $^{51}$ , as well as DVIQP devices such as single-photon sources and photon-number resolving detectors $^{6,34}$ . The development of discrete- and continuous-variable hybrid integrated quantum photonics $^{4,5,52}$  provides opportunities for deployable chip-scale quantum sensing $^{3,14}$ , practical quantum networking $^{2,11}$  and universal quantum computing $^{53,54}$ .

# Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41586-025-08602-1.

1. Ladd, T. D. et al. Quantum computers. Nature 464, 45-53 (2010).  
2. Wehner, S., Elkouss, D. & Hanson, R. Quantum internet: a vision for the road ahead. Science 362, eaam9288 (2018).  
3. Degen, C. L., Reinhard, F. & Cappellaro, P. Quantum sensing. Rev. Mod. Phys. 89, 035002 (2017).  
4. Wang, J., Sciarrino, F., Laing, A. & Thompson, M. G. Integrated photonic quantum technologies. Nat. Photon. 14, 273-284 (2020).  
5. Pelucchi, E. et al. The potential and global outlook of integrated photonics for quantum technologies. Nat. Rev. Phys. 4, 194-208 (2022).  
6. Bao, J. et al. Very-large-scale integrated quantum graph photonics. Nat. Photon. 17, 573-581 (2023).  
7. Llewellyn, D. et al. Chip-to-chip quantum teleportation and multi-photon entanglement in silicon. Nat. Phys. 16, 148-153 (2020).  
8. Javid, U. A. et al. Chip-scale simulations in a quantum-correlated synthetic space. Nat. Photon. 17, 883-890 (2023).  
9. Vigliar, C. et al. Error-protected qubits in a silicon photonic chip. Nat. Phys. 17, 1137-1143 (2021).  
10. Huang, J. et al. Demonstration of hypergraph-state quantum information processing. Nat. Commun. 15, 2601 (2024).  
11. Zheng, Y. et al. Multichip multidimensional quantum networks with entanglement retrievalability. Science 381, 221-226 (2023).  
12. Mondain, F. et al. Chip-based squeezing at a telecom wavelength. Photon. Res. 7, A36-A39 (2019).  
13. Nehra, R. et al. Few-cycle vacuum squeezing in nanophotonics. Science 377, 1333-1337 (2022).  
14. Stokowski, H. S., et al. Integrated quantum optical phase sensor in thin film lithium niobate. Nat. Commun. 14, 3355 (2023).  
15. Masada, G. et al. Continuous-variable entanglement on a chip. Nat. Photon. 9, 316-319 (2015).  
16. Lenzini, F. et al. Integrated photonic platform for quantum information with continuous variables. Sci. Adv. 4, eaat9331 (2018).  
17. Stefszky, M. et al. Waveguide cavity resonator as a source of optical squeezing. Phys. Rev. Appl. 7, 044026 (2017).  
18. Zhao, Y. et al. Near-degenerate quadrature-squeezed vacuum generation on a silicon-nitride chip. Phys. Rev. Lett. 124, 193601 (2020).  
19. Vaidya, V. D. et al. Broadband quadrature-squeezed vacuum and nonclassical photon number correlations from a nanophotonic device. Sci. Adv. 6, eaba9186 (2020).  
20. Yang, Z. et al. A squeezed quantum microcomb on a chip. Nat. Commun. 12, 4781 (2021).  
21. Raussendorf, R. & Briegel, H. J. A one-way quantum computer. Phys. Rev. Lett. 86, 5188-5191 (2001).  
22. Menicucci, N. C. et al. Universal quantum computation with continuous-variable cluster states. Phys. Rev. Lett. 97, 110501 (2006).  
23. O'Brien, J. L., Furusawa, A. & Vučković, J. Photonic quantum technologies. Nat. Photon. 3, 687-695 (2009).  
24. Weedbrook, C. et al. Gaussian quantum information. Rev. Mod. Phys. 84, 621-669 (2012).  
25. Yukawa, M., Ukai, R., van Loock, P. & Furusawa, A. Experimental generation of four-mode continuous-variable cluster states. Phys. Rev. A 78, 012301 (2008).  
26. Su, X. et al. Gate sequence for continuous variable one-way quantum computation. Nat. Commun. 4, 2828 (2013).

# Article

27. Asavanant, W. et al. Generation of time-domain-multiplexed two-dimensional cluster state. Science 366, 373-376 (2019).  
28. Larsen, M. V., Guo, X., Breum, C. R., Neergaard-Nielsen, J. S. & Andersen, U. L. Deterministic generation of a two-dimensional cluster state. Science 366, 369-372 (2019).  
29. Chen, M., Menicucci, N. C. & Pfister, O. Experimental realization of multipartite entanglement of 60 modes of a quantum optical frequency comb. Phys. Rev. Lett. 112, 120505 (2014).  
30. Roslund, J., de Araújo, R., Jiang, S., Fabre, C. & Treps, N. Wavelength-multiplexed quantum networks with ultrafast frequency combs. Nat. Photon. 8, 109-112 (2014).  
31. Cai, Y. et al. Multimode entanglement in reconfigurable graph states using optical frequency combs. Nat. Commun. 8, 15645 (2017).  
32. Armstrong, S. et al. Programmable multimode quantum networks. Nat. Commun. 3, 1026 (2012).  
33. Wang, W., Zhang, K. & Jing, J. Large-scale quantum network over 66 orbital angular momentum optical modes. Phys. Rev. Lett. 125, 140501 (2020).  
34. Cheng, R. et al. A 100-pixel photon-number-resolving detector unveiling photon statistics. Nat. Photon. 17, 112-119 (2023).  
35. Arrazola, J. M. et al. Quantum circuits with many photons on a programmable nanophotonic chip. Nature 591, 54-60 (2021).  
36. Paesani, S. et al. Generation and sampling of quantum states of light in a silicon chip. Nat. Phys. 15, 925-929 (2019).  
37. Guidry, M. A., Lukin, D. M., Yang, K. Y., Trivedi, R. & Vučković, J. Quantum optics of soliton microcombs. Nat. Photon. 16, 52-58 (2022).  
38. Gouzien, E., Tanzilli, S., D'Auria, V. & Patera, G. Morphing supermodes: a full characterization for enabling multimode quantum optics. Phys. Rev. Lett. 125, 103601 (2020).  
39. van Loock, P., Weedbrook, C. & Gu, M. Building Gaussian cluster states by linear optics. Phys. Rev. A 76, 032321 (2007).  
40. Fabre, C. & Treps, N. Modes and states in quantum optics. Rev. Mod. Phys. 92, 035005 (2020).  
41. Moss, D. J., Morandotti, R., Gaeta, A. L. & Lipson, M. New CMOS-compatible platforms based on silicon nitride and Hydex for nonlinear optics. Nat. Photon. 7, 597-607 (2013).  
42. Kues, M. et al. Quantum optical microcombs. Nat. Photon. 13, 170-179 (2019).  
43. Lu, X. et al. Chip-integrated visible-telecom entangled photon pair source for quantum communication. Nat. Phys. 15, 373-381 (2019).  
44. Adesso, G., Serafini, A. & Illuminati, F. Extremal entanglement and mixedness in continuous variable systems. Phys. Rev. A 70, 022318 (2004).  
45. Menicucci, N. C., Flammia, S. T. & van Loock, P. Graphical calculus for Gaussian pure states. Phys. Rev. A 83, 042335 (2011).

46. González-Arciniegas, C., Nussenzeig, P., Martinelli, M. & Pfister, O. Cluster states from Gaussian states: essential diagnostic tools for continuous-variable one-way quantum computing. PRX Quantum 2, 030343 (2021).  
47. van Loock, P. & Furusawa, A. Detecting genuine multipartite continuous-variable entanglement. Phys. Rev. A 67, 052315 (2003).  
48. Barbosa, F. A. S. et al. Beyond spectral homodyne detection: complete quantum measurement of spectral modes of light. Phys. Rev. Lett. 111, 200402 (2013).  
49. Kippenberg, T. J., Gaeta, A. L., Lipson, M. & Gorodetsky, M. L. Dissipative Kerr solitons in optical microresonators. Science 361, eaan8083 (2018).  
50. Vernon, Z. et al. Scalable squeezed-light source for continuous-variable quantum sampling. Phys. Rev. Appl. 12, 064024 (2019).  
51. Tasker, J. F. et al. Silicon photonics interfaced with integrated electronics for 9 GHz measurement of squeezed light. Nat. Photon. 15, 11-15 (2021).  
52. Andersen, U. L., Neergaard-Nielsen, J. S., van Loock, P. & Furusawa, A. Hybrid discrete and continuous-variable quantum information. Nat. Phys. 11, 713-719 (2015).  
53. Ra, Y.-S. et al. Non-Gaussian quantum states of a multimode light field. Nat. Phys. 16, 144-147 (2020).  
54. Konno, S. Logical states for fault-tolerant quantum computation with propagating light. Science 383, 289-293 (2024).

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

![](images/bd56842eb0e7c27bc71266a5f9d56f50dc7b4c32ab673d7e75dc8514ac127fe7.jpg)

Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or

format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

© The Author(s) 2025

# Data availability

The data that support the findings of this study are available in the Article and its Supplementary Information. All other relevant data are available from the corresponding authors upon reasonable request. Source data are provided with this paper.

# Code availability

The code that supports the findings of this study is available from the corresponding authors upon reasonable request.

Acknowledgements We acknowledge support from the National Natural Science Foundation of China (nos. 12325410, 62235001, 12434015, 11834010 and 123B2065), the Innovation Program for Quantum Science and Technology (no. 2021ZDO301500), the National Key R&D Program of China (no. 2019YFA0308702), the Beijing Natural Science Foundation (Z220008),

the Fundamental Research Program of Shanxi Province (no. 20210302121002) and the Fund for Shanxi '1331 Project' Key Subjects Construction.

Author contributions X.J. and J.W. designed the quantum photonic devices and experiment. X.J., C.Z., X. Zhu, C.Y., Y.C., X. Zhang, Y.Z., Z.F., J.M. and T.D. implemented the experiment. C.Z., X.J., X. Zhu and C.Y. provided the simulations and performed the theoretical analysis. L.C., X.S., Q.G. and J.W. managed the project. X.J., C.Z., X. Zhu, X.S. and J.W. wrote the paper with input from all the authors. All the authors discussed the results and contributed to the paper.

Competing interests The authors declare no competing interests.

# Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41586-025-08602-1.

Correspondence and requests for materials should be addressed to Xiaolong Su or Jianwei Wang.

Peer review information Nature thanks the anonymous reviewers for their contribution to the peer review of this work. Peer reviewer reports are available.

Reprints and permissions information is available at http://www.nature.com/reprints.