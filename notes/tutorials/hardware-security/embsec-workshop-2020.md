#	Embedded Security Workshop 2020

From https://github.com/eda-ricercatore/gulyas-scripts/blob/master/notes/tutorials/hardware-security/embsec-workshop-2020.md


From Kevin Fu to Everyone: (3:22 PM):
+ I will repost the scribe notes periodically as participants join the chat.  https://docs.google.com/document/d/1RZ2Guor2Yc-X2hoDShbl9_skYHzTNe_NC5pOSXVhKWg/edit?usp=sharing 










##	Talk by Prof. Paul Kocher

+ personal biography, processor architecture security problems
+ phases of reindeer problem: exponential growth phrase, peak phase, and decline
+ Marc Andreessen 2011, Software is eating the world.
	- tech scales faster than traditional economic models/industries
	- Spectre exploited mismatch between software and hardware
		* conditional branches, intermediate ???
		* add instruction assume that registers for add operands don't affect timing
		* memory & swapfile compression/duplication
		* analog problems
			+ power, heat, clock throttling, ADC, entropy sources, RF interference
			+ resort to bandwith models
		* contract between HW and machine code
		* exploit ambiguity for future compiler optimization
		* 4768 page long Intel x86 ISA specification
			+ abstraction and complexity scaling
				- abstraction enables scaling
				- abstraction is dangerous because of assumptions regarding the assumptions
				- abstraction creates mediocrity when getting product teams to comply with standard interfaces
				- collapse the abstraction to span a broader range of topics - not scalable design task
				- use temporal separation to separate security domains in time, reset/zeroized between domains
				- abstraction is independent of most HW and SW complexity
					- works for VLSI design components, for digitial IC design
+ trade-off hardware resources for security features
+ separate security domains in space, with limited interfaces between
	- intra-chip separation
	- use SoC, or VLSI system, with different security domains (some domains are safer, and other domains are less safe)
	- specification of memory models...
		+ SRAM
		+ cache
		+ shared DRAM apertures
		+ encrypted RAM
		+ encrypted RAM + anti-replay
		+ oblivious RAM, which is slow...
			- need to improve speed of ORAM
+ use formal verification for detecting and correcting hardware security bugs, with RISC-V ISA
	- bug finding and bug patching leads to us toggling between "X is secure" and "X is insecure"
+ defect rates and probability of zero defects
+ 19:17... Error masking
+ redundancy in security systems
+ secrecy - intra-chip MPC
+ 











Questions:
+ Why can’t software be implemented, and tested and verified, to conform to temporal specifications using formal methods/verification and enable temporal separation in SW, too?
	- Formal methods play a significant role, though it’s hard to match (for example) higher-level software against compiler output, and dealing with all possible hardware it might run on.  Can discuss more in Q&A or breakout...!  [Great question]
+ Are you recommending these changes for general computing that everyone will use, or would these changes be targeted solely towards applications that require high security?
	- Given that the cost of transistors is nearly zero, these kinds of capabilities don’t really cost much to integrate broadly.
+ Regarding redundancy in security systems, does it lead to a greater requirement in effort for testing and verification?
	- Yes - and changes the requirements for test/verif.  For example, common failure modes are a lot more serious than ones that might affect a single component.  It also means that test failures need to be taken seriously even if there are mitigating factors.
	- For example, one some of the chip design projects I’ve led, a critical bug report might say “if you disable security detector X, then Y doesn’t behave safely”.
+ Does following Six Sigma, Total Quality Management, or similar quality control/improvement processes lead to better security bug funding and debugging? Or, do we need more/better solutions?
+ If we were to design for performance, power, would satisfying the security foci of CIA - confidentiality & availability & integrity - suffice?
	- The key philosophical question is how trade-offs get resolved.  If we decide that performance/power/cost/time-to-market cannot be materially affected, we’ve over-constrained the system and security goals will likely fail.  In contrast, it’s really an open question what systems would look like if we say that security properties (e.g., C-I-A) must be met with high likelihood.
	- Regarding, confidentiality/availability/integrity specifically, most failures at a low level can be sorted into these categories, though there are many other architectural characteristics that affect the ability to achieve these (e.g., testability, usability, etc.)
+ Question for Paul Kocher: For students hoping to develop more secure systems, how do we begin an interdisciplinary approach to making more secure architectures? Do you have any tips about where to start in terms of papers, tools, books, professors, etc?
+ Is it ever possible to make a networked device to be secure?
	- My answer would depend on nuances of the question.  First, “secure” probably needs to be rewritten as a probability and constrain the set of threats. For example, 100% protection against an insider threat that fully compromises the design team is impossible.  In contrast, 80% chance of no remote exploits that steal an on-device secret key used for authentication is pretty easy to achieve.  You also might want to define what “insecure” means, e.g. exploited at scale vs. theoretically breakable.
	- For example, some of the chip projects I’ve led had contract terms that made payments contingent on the tamper resistance not being broken at scale in the field.  I.e., if clones that pass authentication are available, the requirement is not met.  For applications like pay TV & anti-counterfeiting, attacks only matter at scale, so this kind of test makes sense.  And these were largely very successful.  (But they’re scary as a chip designer!)






##	Talk by Prof. Wayne Burleson

+ privacy problems/challenges
	- anonymous emails
	- k-anonymity
	- ...
	- subtle threat model
		* privacy metric is often a result of a complex attack
		* not yet conceived use of data
		* no boogie man
	- Ari Juels, RSA Labs, 2007
	- Can they support privacy-preserving protocols
+ applications of privacy problems/challenges:
	- transportation payments: ideminity, privacy, payment of public/private tranportation trips
		* ECC engine, eliptic curve cryptography (ECC)
		* electronic cash payments via the smart phone
		* NFC-smartphone e-cash implementation
			+ vulnerabilities versus costs trade-offs
	- implantable medical devices
		* biomedical
		* sports
		* implantable medical device, IMD
			+ drug/marker detection, data analysis, therapy - drugs or reminders to get people to consume medication or exercise
			+ power requirements/limitations
+ future work
	- security through obscurity
	- industry-standard source-code analysis
	- realistic threat model
	- crypto building blocks
	- authenticate 3rd-party devices
	encrypt sensitive traffic




Questions:
+ holomorphic encryption
+ security at the edge, networked CPS



## Talk by Prof. Daniel Holcomb

Delayed start of taking notes at slide 14/15:
+ Biometric signatures
	- iris, ear shape, CSs, retina, 
+ unique signatures for ICs
+ counterfeiter, manufacturer
	- trusted IC die, EID
		* EID = enrolled id. the claimed identity of the chip
	- digitally signed fingerprint, untrusted distribution channel and untrusted database
		* private key of ...
	- verification in 150 ms
+ counterfoil, inexpensive equipment
	- cameras from different vendors (>= 2 vendors)
	- OpenCV for image processing
	- Crpto++ for crypto-proessing
	- naive/na{\"{i}}ve fingerprinting
	- fingerprinting using computer vision algorithms
		- using object detection & matching, motion tracking, stitching panoramic views
	- feature extraction with 4 prominent algors: SIFT, SURF, ORB, BRISK
	- keypoints: position & descriptor
	- geometric estimation
	- inlier only if match is nearest in feature space and fits geometry
+ forge packages to match enrolled fingerprint in sophisticated attacks
	- same chip, same modl, different mold
+ suitability for IC distribution
	- real-time verification in 700 ms, pick-and-place task
		* read image
		* ROI...
+ counterfiet ICs threaten critical systems and profits
	- counterfoil verifies IC provenance using fingerprints from surface texture of plastic packages
+ SRAM, ubiquitous memory in VLSI circuits
	- SRAM power-up fingerprint
		* device authentication
		* ...
		* intrinsic ID start-up
	- challenge response using read with contention
	- dta retention voltage



From Sara Rampazzi to All panelists and other attendees: (2:53 PM)
+ Feel free to email Prof. Wayne Burleson to chat more! burleson@umass.edu







Questions:
+ What does EID mean?
	- enrolled id. the claimed identity of the chip
+ What do you mean by panoramic views? How is this used to detect the fingerprints?
	- I don’t know what is referenced by “panoramic” in the question. The keypoints in the fingerprint are matched using RANSAC. Similar techniques are used to stich panoramic images. In that case too they are using the fact that common features appear in the overlaps of the multiple images that are being stiched together.
+ For SRAM PUF authentication, can we use DRAM, FLASH memory or non-volatile memory cells instead?
	- lots of cells, can get a lot of info
	- differences of values leaking off DRAM cells
	- DRAM and FLASH are not integrated with IC, has to go off-chip, unlike SRAM solutions
+ Would it be practical to imprint your own microscopic fingerprint/introduce surface roughness for ceramic and metal IC's so counterfoil can be applied to them?
	- I don’t know for sure, but it could be. we want the fingerprint to be  unique to each instance. but if you randomly roughed them up that might be unique and hopefully hard to reproduce. You could also add a random pattern of some things to it during manufacture
+ Is the SRAM fingerprint consistent each time you power up a device?
	- temperature dependent
+ How to address chip recycling with CounterFoil?
	- check with record book... Looks new, but made in 2011. Put new tops, destroy bumps and fingerprints




##	VLSI Breakout Room

General introduction:
+ Ben Cyr, Prof. Kevin Fu's group
+ Ms. Xiali Hei, CPS attack
+ Ms. Lanier, ultrasonic microphone array
+ Miguel, root of trust definitions.
+ Demba, wireless communication system
+ Prof. Dan Holcomb
+ Prof. Sara Rampazzi
+ Prof. Reza


Specific
+ 10 minutes, high-level about VLSI security, 
+ GLSVLSI 2011, paper with Yusuf Leblebici, persistent trends in VLSI produce challenges in designing security mechanisms
+ hw security considerations
	- counterfeits and unauthorized re-use
		* counterfeit hardware may lead to malware and failure
	- hardware trojans
		* stopping hardware trojans in their tracks
	- analog malicious hardware, using one additional gate to hack analog IC
	- acoustic microphone via acoustic/sonic imaging
		* unonbstructive monitoring using acoustics
		* Alexa & Siri, oversensing
			+ designers fail to consider oversampling of data, and usage by hackers to exploit people's privacy
	- are counterfeits or trojans more dangerous
	- ways to defend against counterfeits or trojans
	- methods to inspire people of different backgrounds to become interested in VLSI security
+ FPGA-based hardware acceleration for data center computing, Takeshi Sugawara from UEC Tokyo
	- development ecosystem for FPGAs is more accessible, via AWS instance
		* reduce distance between sw and hw people
	- interface between digital and analog world
	- AWS instance, upload oscillator, bypass checking by making strange circuit that look likes an oscillator but is (or looks like) a sequential circuit
	- Fault injection, overclocking, Wayne Burleson
		* FPGAs are limited by Xilinx and Altera
		* FPGA in the cloud, part of computing culture, make things accessible behind layers/abstraction
		* VLSI design in the 1980s (from late 1970s to the early 1990s): Allow sw and hw people to work together in the past
+ Miguel Osorio, root of trust component, feature creep in big design, focus on anchor in hw that is more verifiable
	- system/logic security, connected to hw security people
	- small, verifiable root of trust
		* don't produce physical thing...
		* ripples all the way down, along the supply chain
	- ways to mitigate attacks in manufacturing, counter-measures for physical design (layout), interaction with vendors in the manufacturing process, ...
	- analogous to smart card
	- issues at run-time, deployed in production, provision keys in silicon and protect them from attackers, at manufacturing 
+ Frank Courbon, OpenTiton, PDK, firmware, cybernetics, root of trust
	- Miguel Osorio, make things open source, make stuff from fabs that don't want stuff open source... Make RTL stuff open source... 120 nm cell library with netlists... OpenPDK... 
	- create IC designs, using open source tools, need authentication mechanism to process masks at foundry... Timing information to trace information...
	- need to trust the tools...
	- 
+ Prof. Andrew Kahng has helped people create a set of open-source EDA tools
	- $1500 IC manufacturing
	- Andrew B. Kahng (PI) – OpenROAD
	- add more assurance tools to the tools, Takeshi Sugawara
	- analysis tools of different kinds, malicious tools... People usually don't assume that...
		* use verifier as a trusted 3rd party tool
+ remote-controlled robot to do labs... Replicate the set-up, sw like MATLAB and hw tools like logical analyzers... Take-home kits using Analog Discovery 2 device
	- Regarding take-home kits, Texas A&M University's ECE department uses the Analog Discovery 2 device as a platform to get students to design circuits on a small breadboard at home, and get their circits to be checked by TAs; the device provides power supplies and does data acquisition.












## Erika A. Petersen


Data privacy and cybersecurity in modern neurosurgery and neuromodulation
+ harms regarding data collection, and legal implications
+ computer-guided and regulated tools
+ neuroanatomical navigation for surgical planning and performance
+ high use of imaging before, during, and after surgery
+ ICU monitoring and diagnostic testing
+ implanted neuromodulation devices



+ 3-D imaging sw for planning surgical paths
	- biopsy
	- dbs - deep brain stimulation, pace maker for the brain, device placed near the heart to avoid harming the brain
	- stell cell implantation 
	- RF incision
	- laser ablation for epilepsy
	- radiosurgery
	- robotic surgery, sub-mm precision
+ neuromodulation definition
	- places where there is a nerve in the body, we can use devices to improve body functions/sensory
	- functional neurosurgery & neuromodulation, neuropsychiatry
	- demands minimal risk of inflicting morbidity and mortality
	-neuromodulation sites of intervention
		* SCS, lateral recess
+ intrathecal drug delivery
	- vulnerability to magnets, stalls, and airs... hazards to devices
+ RNS for epilepsy, adaptive and responsive neurostimulation
	- adaptive DBS for PD (Parkinson's disease)
+ spinal cord stimulation for pain
	- gate control theory
+ spinal cord stimulation, drg lead placement
+ supraorbital stimulation
+ OR awake testing
	- testing implanted electrodes in the OR shows immediate improvement in function
	- test while conscious to avoid side effects
	- consequences of poor accuracy
	- known stimulation complications of DBS
+ hijack in vivo medical devices
+ transmit data from medical devices to the cloud for data access by medical (or health care) staff
	- use data to track building configurations and landscape of government/private property
	- track people's mood, behavior 
+ risks and vulnerabilities
	- DoS, denial of service
	- get position, data/time, and movement information
+ 5th amendment protects what we say, rather than data in medical devices. Limited constitutional protection. Allow people to opt out, delete data, how to share data.
	- role of industry self-policing









Questions:
+ By gate control theory, do you mean gait for walking/running?
	- no, biochemical messages passing through gate in the nervous system
+ Are these neuroprostheses programmable by software?
	- yes, via a programming tablet, Bluetooth, or proprietary frequency.
+ Do these devices consist of programmable hardware? When I took a course at USC about neuroprostheses, they used programmable FPGA devices for prototypes.
+ Would ex vivo (or in vitro) medical devices have less security problems than in vitro medical devices?
	- Yes, hardware can be upgraded
+ If possible, can you please kindly show the slide for the “risks and vulnerabilities” again?
	- 
+ Would ex vivo (or in vitro) medical devices have less security problems than in vitro medical devices?
	- "External devices may be more networked than implanted ones, so these might be more vulnerable. If I understand what you are asking, I  think there are vulnerabilities to both implanted and external devices, but the perception of level of hazard for the internal device may be higher than the externals that are limited in their patient interaction. Who wants a “broken” and “malfunctioning” device inside them, giving them severe sense of vulnerability."
+ What did you mean when you mentioned data anonymization is not enough to protect privacy?
	- alias pool data
	- without differential privacy, can track who the patient is
+ What do you think about the side effects of a surgery to implement a brain machine interface with many electrodes ?Thank you.
	- need to know neuroconnectivity
	- minimize contact points of medical devices, while allowing some redundancy, to reduce points of failures
+ Are these implanted devices ever streaming data to the hospital or is data locally available only?
	- external controller can be uploaded
	- uploaded to local equipment/computer, or to the cloud, via smart devices/phones and tablet computers


Additional comments:
+ Any implanted device is for that patient only and will be discarded after explantation due to infection risks. I agree there should be a “wipe” prior to disposing of a device, but this work flow does not currently exist. Temporary external stimulators are reused, and are reset between patients.







## Talk by Takeshi Sugawara


laser injection attacks on ICs and sensors
+ security of senors
	- affect data integrity in the analog domain
	- conventional solutions for digital data
	- affects autonomous vehicles
	- voice controllable systems, VCSs
		* can hack such systems to make VCS to do something else
+ conventional attacks on VCS
	- ultrasound
		* stealthy attack using inaudible sound
+ light commands: laser-based audio injection
	- microphones capture light as sound
	- end-to-end attacks across two buildings
	- light commands are dangerous... sound is difficult to transmit to the VCS, and people can notice attacks and report them to the police... With light commands, we can hack VCS-connected smart homes/buildings/offices.
	- lightcommands.com
+ MEMS microphone, several millimeters/mm
	- package with MEMS diaphragm (smaller than 1 mm) and ASIC
	- MEMS diaphragm mvoes with acoustic pressure wave
	- ASIC converts analog signal to digital signal
		- laser light intensity can be modulated to create acoustic pressure wave on MEMS diaphragm
		- voice modulated light commands, rather than modulated light commands
	- smart speakers can be controlled with light commands at distances of 110+ meters, for 5 mW or 60 mW (milli-Watt) devices
	+ photoacoustic effects on the MEMS diaphram, light converts to audio signal by photoelectric effect
+ consequences
	- brute force unlock door
	- turn on/off enable/disable smart devices
+ countermeasures
	- sw approaches
		* interactive authentication/liveness test
		* sensor fusion
			+ comparing outputs from multiple microphones
	- hw approaches
		* light-blocking covers
		* on the VCS, fabric
		* inside the MEMS microphone
+ laser fault injection attack for crypto-implemented world
+ crypto-implementations can be used in hostile environments
	- device owner can be an attacker
		* increase balance on smart cards
		* side-channel and fault-injection attacks
+ smartcard industry is a technology driver, establishing certification scheme...
+ LFI, laser fault injection
	- shoot laser to cause a bit to flip or get stuck in memory
	- bypass access checks
	- nullifying random number generator
	- cause crypto device output to create faulty outputs
	- parasitic photo diode of CMOS devices, shine modulated light on such CMOS devices
+ sensor as a countermeasure against LFI
	- detect and react to LFI attempts using built-in sensors
	- efficiency of sensors and integration



Questions:
+ How did you start vehicles using light?
	- Tesla, start engine of the car using voice-dmoulated light commands
+ Slide 22: Is the CMOS device a normal CMOS device?
	- standard CMOS device, not CMOS sensor imaging device.







##	Prof. Yongdae Kim



Remote physical attacks on sensors: case study on unmanned vehicles
+ sensors - electrical device to measure physical quantities
	- passive and active sesnsors
	- for RF, actuation, gyroscope, electric shock, flight control
+ Tesla accident, with trailer
	- diagram of accident
	- sensor failed to distinguish between the sky and the side/back of the autonomous cars, lower-quality sensors
	- accident, not security attack
	- sensor security, prevention and detection mechanism
		* malicious network traffic
		* sw vulnerabilities
			- sandbox protection
		* sensor: new attack vector
			+ input/output can be used to control IoT device
			+ from SenSys paper, sensors can be affected by spoofing attack on legitimate channels and attacks on non-legitimate channels
				- these sensors are controlled by an embedded system
+ gyroscope on drone
	- inertial measurement unit, IMU
	- device to measure velocity, orientation, or rotation
	- combination of MEMS gyroscopes and accelerometers used to determine position and direction of movement for drones
		* has resonant frequencies, and attacks at resonant frequencies affect drone performance/function
		* gyroscope resonates, and causes rotors to resonate, too
			+ rotor control data samples
		* sound attacks don't travel far, and is hard to focus
+ GPS spoofing effect on Tesla autopilot control
	- slow down in 3 seconds, affect autopilot speed limit
+ spoof point cloud
+ injected video is used, instead of sensing information.
	- use laser pointer to control the lidar sensors of the cars, blinding effects on video cameras of autonomous cars
+ sensor attack defense
	- impossible fundamental defense
	- most important solution: fail safe mode design
	- easy defense: detect saturation then fail safe mode
	- harder defense: to handle spoofing
		* physical fingerprinting
		* redundancy improves security linearly
		* robust sensor fusion
		* recover sensor values after erasing noise
		* detect control failure early




Questions:
+ For the acoustic attacks on the gyroscope, do you think that “shielding” the MEMS would be sufficient?
	- Yes.
+ Can we use laser light to modulate sounds to attack MEMS gyroscopes of drones?
	- Maybe... MEMS sensor is not exposed outside, so it is difficult to do it.
+ How did you get permission to spoof GPS signals from the government? Would the institution review board of KAIST or Samsung Research submit a request on your behalf?
	- talk directly to the government; informal permission granted for research purposes
+ Re Mobileye object detection, have you formally calculated the minimum level of perturbation needed to fool the detection?
	- Mobileye sensors and computer vision system reacts to cartoons and PowerPoint slides
+ Is there a publication that addresses the linearity of redundancy on improving security? The slide mentioned, “redundancy improves security linearly”.
	- If you use two cameras, I can blind one by one. So no proof is required. Of course, good fusion might improve security non-linearly.
+ What kind of training data does Mobieye use?
+ Are sounds used to attack the gyro generally inside or outside of the audible range?
	- in the audible range












## Prof. Z. Morley Mao, or Prof. Morley Mao


Towards Robust LiDAR-based Perception in Autonomous Driving: General Black-Box Adversarial Sensor Attack and Countermeasures
+ autonomous vehicle (AV) perception
	- sensors, perception (position, speed, object detection), prediction (object future path), planning (AV future path), control (steering, breaking)
+ machine learning, especially deepp learning
+ security of AV perception
	- camera-based perception model
	- LiDAR-based perception model
	- LiDAR physical attacks
	- Baidu Apollo, open-source AV system
	- LiDAR systems have difficulty differentiating real signals from spoofing signals
		* use azimuth of signal source to determine authenticity
		* limited access to testing facility
+ use adversarial machine learning (for Adv-LiDAR) to cause AV to crash into obstacles
	- create spoof 3-D point cloud (via strategically injecting points in the LiDAR-based perception model) to detect fake obstacles/objects
	- white-box attack limitation
		* know about pre-processing, Apollo 2.5 model, and post-processing
		* these are linked by differentiable approximation function
		* difficult to generalize to other machine learning models
		* general defense solutions
	- attack generality limitation
	- no practical defense solution
+ explore general vulnerability
	- security threat models
		* physical sensor attack capability
			+ location of points
		* spoofing attack place fake obstacles to affect future path of car/AV
		+ easier to protect against black-box attacks than white-box attacks
+ state-of-the-art LiDAR-based perception models, based on computer vision workflow/model/architecture
	- bird's eye view -based model
	- voxel-based model
	- point-wise model
+ blackbox adversarial attack, Adv-LiDAR
	- occluded vehicle
		* occludee
		* occluder
	- distant vehicle
+ test for two specific false positive scenarios in the AV system
	- DNN models prefer local features
	- object detection are insentitive to the location of objects
	- use KITTI point clouds to create fake obstacles/objects
	- free space, frustrum, straight-line path, from LiDAR sensor and points in the point cloud... fake vehicle's bounding box
	- CARLO - post-processing module to distinguish between real and fake obstacles
		* ad-hoc architecture/solution
+ front-view representation need for computer vision for AV sensor systems
+ sequential field view, for verifying data points for front-view representation
	- adaptive attack changes strategy of attacks
+ limitations:
	- vulnerability completeness
	- attack practicality
		- limited work
	- defense guarantees
		- limited work
+ sensor fusion for different modalities need to reconcile discrepancies for different data, based on sensor/camera limitations, and majority vote or hierarchy of preferences for valuing certain sensor data over other sensor data
+ fake object creation is easier than removing real object from sensor data
	- simulate physical end-to-end test
	- MCD physical testing facility
+ Why is it possible to only spoof a small number of points? and how long does it take to spoof these points
	- because we have a small anount of time to spoof data via shooting laser into the sensors
+ 
+ 





Questions:
+ Great work and talk! In practice, the perception module  in Baidu' Appolo and many other AV platforms (e.g., Uber and Ford) is actually achieved by multi-sensor fusion from lidar, cameras and even radars. 
Would the discussed perception attack be trivially mitigated by simple fusion with cameras and radars? Physically attacking all of the on-board senors that fools perception seems very difficult.
+ Regarding the sensor-level attack, is it possible to hide existing legitimate points while creating fake points?








## AI and Autonomous Systems



Benjamin Cyr, SPQR Lab
+ autonomous systems, especially cyber-physical systems
	- robotics
	- AV, autonomous vehicles
	- IoT, Internet of Things networks/systems
+ system failures have physical consequences
	- property theft, property damage, injuries, deaths
+ What makes autonomous systems vulnerable?
	- blind trust of the autonomous systems
	- non-autonomous systems: humans are a root of trust
		* trust the intelligence and perception of the user
		* responnsibility is held by the operator
+ autonomous systems: little reliance on humans
	- must trust its own intelligence and perception
+ Shouldn't be a blind trust of autonomous systems
	- trick perception to attack AI and machine learning models
	- there exists a gap between AI and human intelligence
+ Adversarial LiDAR, blind trust in LiDAR sensors
	- LiDAR, spoofed points, spoofer at 13 meters away
	- adversarial 3-D point cloud
	- spoofed 3-D point cloud
	- gap between AI and human intelligence leads to more vulnerabilities
+ protection of autonomous systems
	- "trust but verify"
	- AI
		* anomaly detection
		* adversarial training
		* robust algorithms
	- sensor perception
		* anomaly detection
		* sensor fusion
		* randomized sampling
	- autonomy reduction
		* human-in-the-loop
+ Why are you interested in this set of security problems?
+ Other vulnerable systems
	- What other autonomous systems might be vulnerable because of blind trust?
	- robotic manufacturing systems for biotech companies
	- AI for data sheet scrubbing
	- medical devices, autonomous medical devices, such as RF attacks on pacemakers
		* blind trust exists because people don't think about it
		* knowledge graphs are based on one training set, rather than a reasoning system
+ Wilson et. al. 2019, computer vision models have racial/ethnic bias
	- bias reduction
+ Areas of focus for the next 5-10 years.
+ Introduction of people
+ inference engine for smart phones at Qualcomm Research
	- security aspects of ML hardware
	- high-level description of attacks
		* attacks by academics are expected to follow with data sets, attacks, and solutions to mitigate attacks
	- defense - important part of the company
	- protect hardware, including ML/AI hardware
	- build standards for ML hardware security, chipset, ICs, across the hardware/software/network stack
+ expensive hardware need to be reconfigurable/programmable, so that it can be updated to address hardware/system security vulnerabilities
	- encrypt channels, fix security problems/vulnerabilities at the source
	- tend to address issues downstream
	- use ML to do anomaly detection to determine baseline set of signals/data, and to detect RF interference (or other anomalies)
		* where you attack from
		* differentiate accidents from security attacks
			+ investigate attacks more
+ need to recompose solutions for subproblems to be a consistent solution, and address inconsistencies in composed solution
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 












## Closing Remarks


+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 
+ 











#	Author Information

The MIT License (MIT)

Copyright (c) <2020> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.
