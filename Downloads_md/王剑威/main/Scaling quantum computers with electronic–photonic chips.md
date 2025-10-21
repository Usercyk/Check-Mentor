# Scaling quantum computers with electronic–photonic chips

Yun Zheng, Xinyu Jia & Jianwei Wang

Check for updates

An electronic-photonic quantum system on a chip could be of use in the scaling of quantum information technologies.

The co-integration of electronic and photonic components into a single-chip system allows the computational power of electrons to be merged with the high-speed, low-energy data transmission of photons. The approach can be used to create efficient and scalable information processing systems for applications such as data centres and artificial intelligence. It is also an approach that could play a pivotal role in advancing quantum information science. Writing in Nature Electronics, Danielius Kramnik, Imbert Wang, Anirudh Ramesh and colleagues now report the co-integration of quantum photon-pair sources and classical electronic controls on a single complementary metal-oxide-semiconductor (CMOS)-fabricated silicon chip (Fig. 1a), providing a prototype of an electronic-photonic quantum system on a chip<sup>1</sup>.

Integrated quantum photonics has been instrumental in advancing quantum information processing, providing miniaturized on-chip components, devices and circuits that can create, guide, control and detect quantum states of light. For quantum hardware, a major research focus is achieving system-level scalability to address the substantial resource demands of fault-tolerant quantum computation, which requires millions of physical qubits and efficient error correction. High-volume CMOS-compatible silicon photonic integration is a promising path to building scalable quantum computers powered by light, and recent progress in silicon photonic quantum computing has been remarkable, with contributions from both academia and industry. Key developments include large-scale quantum integration, the monolithic integration of high-performance quantum photonic devices, the deterministic generation of entangled cluster states and the networking of multiple quantum chips. However, creating scalable classical control systems capable of individually addressing and controlling each active quantum component and quantum bit (qubit) as their numbers grow in large-scale quantum computers remains a key challenge.

Kramnik, Wang, Ramesh and colleagues - who are based at the University of California Berkeley, Boston University and Northwestern University - help address this challenge by monolithically integrating microring-resonator photon-pair sources and spectral filtering resonators with analogue and digital control electronics, all on a single silicon chip. The devices are fabricated on the same silicon-on-insulator layer (with a sub-100 nm thickness) using a 45 nm CMOS process. The integrated system exhibits precise control of microring-based single-photon sources, compensating for resonant wavelength mismatches and spectral drifts, both of which can degrade performance.

Real-time monitoring of pump laser microring detuning is achieved through non-invasive photocurrent sensing, implemented using integrated photodiodes alongside the sources. Feedback control

is enabled by amplifying detected signals via on-chip transimpedance amplifiers, analogue-to-digital converters, off-chip signal processing, and subsequent on-chip digital-to-analogue conversion to drive thermo-optic phase shifters on top of the sources. This approach allows the stabilized microring source to maintain consistent performance even under temperature fluctuations and during the simultaneous operation of multiple nearby microrings.

Further improvements in these electronic-photonic quantum systems will be needed to enhance their practical value. For example, the researchers highlight that adopting thicker silicon and buried oxide layers – already commercially available – could reduce waveguide propagation losses and enhance source brightness, both of which are essential for quantum applications. Additionally, the on-chip integration of logic electronic circuits could fully leverage the inherent advantages of high bandwidth and low latency in electrical signal processing. Moreover, despite the size mismatch between photonic and electronic waveguides and devices, which is due to the vastly different wavelengths of photons and electrons, electronic resources can be partially shared through multiplexing among photonic quantum devices. This approach avoids proportional scaling of electronic components with their photonic counterparts, highlighting the importance of optimizing electronic resource use in future designs.

Unlike other quantum computing platforms, silicon photonic quantum computers allow classical electronics to be integrated with quantum photonics using high-volume fabrication processes. This could potentially lead to the development of a hardware platform for universal measurement-based quantum computing with light<sup>7</sup>, empowered by scalable classical controls. Such a system requires electronic circuits to drive photonic quantum gates, program the quantum information processing unit, read out the detection signals of photonic quantum states, and perform classical logical processing and feedforward control of quantum operations (Fig. 1b). Furthermore, these co-integrated devices are inherently compatible with hybrid classical-quantum information processing systems, making them particularly promising for noisy intermediate-scale quantum applications, including biomolecular simulation and data processing.

Looking ahead, the development of quantum computation with single photons now needs to focus on combining electronic-photonic co-integration with recent advances in monolithic integration. This includes integrating photon-pair sources, pump rejection filters (also demonstrated by Kramnik, Wang, Ramesh and colleagues), reconfigurable quantum gates and single-photon detectors (Fig. 1c). Efficient single-photon detection typically relies on superconducting materials, which require cryogenic operating conditions at  $2 - 3\mathrm{K}$ , a regime far less demanding compared with the extreme millikelvin temperatures required for superconducting qubit systems. Cryogenic CMOS electronics and electro-optical modulation could be adapted for this purpose, but thermal management remains a major engineering challenge, as they may introduce additional thermal load.

![](images/c3c9255affcee4cf46f041814717296b534e7904ea231a52529d38fcc87630fe.jpg)  
a

![](images/1a4e5bcb4dba54a3c155fd5eb2164340fc9de071fe5548c1386fd82fefc41618.jpg)  
Fig. 1 | Co-integrated electronic–photonic chips for quantum information technologies. a, Optical microscope images of the electronic–photonic quantum system developed by Kramnik, Wang, Ramesh and colleagues, showing the monolithic integration of microring-based photon-pair sources and electronic controls on the same silicon chip. The right image shows the entire  $2\mathrm{mm} \times 9\mathrm{mm}$  electronic–photonic CMOS chip, while the left image presents two interleaved electronic–photonic quantum circuit blocks. b, The detection of quantum states of light is facilitated by single-photon detectors (SPDs) or photodiodes (PDs). The detection outcomes are read out by electronic circuits, which then trigger on-chip operations or initiate feedforward controls of quantum gates. Green lines represent static control signal loading, and red lines indicate pathways requiring low-latency and high-speed electrical signal processing. c, A future monolithic integrated electronic–photonic quantum chip, including electronic controls and classical processing units, as well as quantum light sources, linear optical circuits (LOCs) for quantum gate implementation, quantum memories (QMs) for quantum storage, and SPDs for detection. SFWM, spontaneous four-wave mixing. Panel a adapted from ref. 1, Springer Nature Limited.

![](images/0626792d31c021c5737490a620f43247f65033f364daca22ad1d8a558fff68a2.jpg)  
b

![](images/addcac1666493a36b96ca10f36551f22791b809162ad106419a2a40ce936db7c.jpg)  
C

An alternative approach for optical quantum computation employs squeezed states and cluster states as fundamental quantum resources $^{5,6}$ . The detection of squeezed light relies on room-temperature homodyne detection, and recent progress has demonstrated the co-integration of electronic readout and photonic detection using bipolar CMOS technology $^{8}$ . Nevertheless, the cryogenic operation of electronic-photonic quantum chips may be indispensable for achieving fault-tolerant universal quantum computing, as single-photon or photon-number-resolving detection is still a key requirement $^{9}$ . Back-end-of-line integration and heterogeneous integration $^{10}$  of silicon-based electronic-photonic devices with non-CMOS-compatible materials may provide a flexible platform for the next generation of quantum computing devices, leading to further advancements in scalability and performance.

# Yun Zheng, Xinyu Jia & Jianwei Wang

State Key Laboratory for Mesoscopic Physics, School of Physics,

Peking University, Beijing, China.

e-mail: jww@pku.edu.cn

Published online: 14 July 2025

# References

1. Kramnik, D. et al. Nat. Electron. https://doi.org/10.1038/s41928-025-01410-5 (2025).  
2. Wang, J., Sciarrino, F., Laing, A. & Thompson, M. G. Nat. Photon. 14, 273-284 (2020).  
3. Zheng, Y. et al. Science 381, 221-226 (2023).  
4. Alexander, K. et al. Nature 641, 876-883 (2025).  
5. Jia, X. et al. Nature 639, 329-336 (2025).  
6. Aghaee Rad, H. et al. Nature 638, 912-919 (2025).  
7. Raussendorf, R. & Briegel, H. J. Phys. Rev. Lett. 86, 5188-5191 (2001).  
8. Tasker, J. F., Frazer, J., Ferranti, G. & Matthews, J. C. F. Sci. Adv. 10, eadk6890 (2024).  
9. Konno, S. et al. Science 383, 289-293 (2024).  
10. Xiang, C. et al. Nature 620, 78-85 (2023).

# Competing interests

The authors declare no competing interests.