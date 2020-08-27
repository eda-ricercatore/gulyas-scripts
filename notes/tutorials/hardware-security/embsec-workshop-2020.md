#	Embedded Security Workshop 2020


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
+ Would it be practical to imprint your own microscopic fingerprint/introduce surface roughness for ceramic and metal IC's so counterfoil can be applied to them?























#	Author Information

The MIT License (MIT)

Copyright (c) <2020> Zhiyang Ong

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Email address: echo "cukj -wb- 23wU4X5M589 TROJANS cqkH wiuz2y 0f Mw Stanford" | awk '{ sub("23wU4X5M589","F.d_c_b. ") sub("Stanford","d0mA1n"); print $5, $2, $8; for (i=1; i<=1; i++) print "6\b"; print $9, $7, $6 }' | sed y/kqcbuHwM62z/gnotrzadqmC/ | tr 'q' ' ' | tr -d [:cntrl:] | tr -d 'ir' | tr y "\n"		Don't compromise my computing accounts. You have been warned.
