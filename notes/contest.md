#	Contests


Domenic Forte shared a link.
Admin · May 31

Take part in the UF/FICS Hardware De-obfuscation Competition!

We are pleased to announce the first ever hardware de-obfuscation competition. Research in hardware obfuscation has grown significantly over the last decade. Unfortunately, many obfuscation schemes have been broken quickly since they are mostly based on figures of merit provided only by the authors. At the University of Florida (FICS Research Institute), we have recently proposed two new schemes (more details below). Rather than speculate about their resistance to attacks, we have decided to initiate a crowd-hacking based competition to fully evaluate them. The results of this competition will either provide confidence in their security or feedback on their weaknesses. This is similar in vein to the AES competitions sponsored by NIST in the late 90’s.

We would like to acknowledge sponsorship by NSF (Award #1651701) in development of these benchmarks as well as this competition.

What is the Hardware De-obfuscation Competition?

Participating teams will attack two recently proposed system-on-chip (SoC) obfuscation and camouflaging techniques:
• Covert Gate from “Covert Gates: Protecting Integrated Circuits with Undetectable Camouflaging” (https://tches.iacr.org/index.php/TCHES/article/view/8290).
• Dynamically Obfuscated Scan Chain (DOSC) – adapted from “Secure Scan and Test Using Obfuscation Throughout Supply Chain” (https://ieeexplore.ieee.org/stamp/stamp.jsp…). A dedicated ePrint will be provided later with more details on DOSC and preliminary security evaluation.

Points of contacts for questions on both techniques will also be provided for interested participants soon.
Teams will be provided with multiple locked benchmarks (as netlists) ranging from smaller (easy to break) to large (very difficult to break) along with an executable of the unlocked netlists to behave as oracles. Teams are free to use any tools and techniques of their choosing to analyze the locked netlists, but should not explicitly hack the oracle. Further, teams should refrain from using known public benchmarks to trivially de-obfuscate or de-camouflage the locked/camouflaged netlists. In the case of camouflaging, teams will be successful if they can identify and recover the functionality of all the covert gates in the design. In the case of obfuscation, teams will be successful if they can recover the obfuscation key (or DOSC seed), or remove all obfuscation elements to recover the original (pre-obfuscation) design. Participants will be judged objectively by the success of their attacks (percentage of corruptibility from original design, percentage of keys/gates recovered correctly, time of recovery, etc.) as well as subjectively by a panel of judges based on the novelty and merits of their proposed attacks.
Participating teams are required to register for the competition by e-mailing Domenic Forte (dforte@ece.ufl.edu) with the team name, team members, and university affiliations. All universities are eligible to compete, except for UF/FICS.

The competition will consist of four phases:
1. Preliminary Investigation – Interested teams will start by performing background research on the covert gates and DOSC. They will register for the competition during this phase, and will be pre-screened based on their expertise and preliminary attack strategies (July 1 – August 1, 2019)
2. First Round – Advancing teams will be given oracles and associated locked netlists for small benchmarks which have been obfuscated by covert gate or DOSC. To move on to the next phase, teams should be able to break the smallest benchmark for at least covert gate or DOSC techniques (August 1 – September 1, 2019)
3. Second Round – Advancing teams from the first round will continue to develop their attacks on covert gates and DOSC. They will be asked to demonstrate improved scalability and/or success on larger benchmarks in order to move on to the final phase. (September 1 – October 1, 2019)
4. Final Evaluation – A student member from each of the finalist teams will present and demo their attacks on new (unseen) benchmarks at the final TAME forum at University of Florida. Travel expenses will cover up to $1000 per team by UF/FICS. The victors will also be awarded with prizes at the event (November 2019).

Please let us know if you have any questions or concerns about the competition.

+ https://tches.iacr.org/index.php/TCHES/article/view/8290
+ https://doi.org/10.13154/tches.v2019.i3.86-118
+ https://www.usenix.org/conference/enigma2020/call-for-participation

+ https://amitelazari.com/
+ https://www.law.berkeley.edu/academics/doctoral-programs/jsd/j-s-d-student-profiles/amit-elazari/
+ https://www.ischool.berkeley.edu/people/amit-elazari
+ https://semiengineering.com/transistor-options-beyond-3nm/
