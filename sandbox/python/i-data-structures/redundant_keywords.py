#!/usr/local/bin/python3

import statistics
from collections import Counter 



list_of_keywords = ["human-animal coexistence", "human-animal coexistence - recommendations", "transforming our mental & physical & spiritual lives", "antidote to the growing epidemic of human loneliness", "growing epidemic of human loneliness", "epidemic of human loneliness", "human loneliness", "loneliness", "loneliness - social challenge", "human loneliness - epidemic of", "loneliness - epidemic of", "empathy", "empathy-building interventions", "dogs teaching children ethical behavior", "animal-assisted therapy", "animal-assisted therapy - for loneliness", "mental health", "mental health issues", "mental health practice", "human-animal relationships", "spiritual health", "wildlife relocation", "growing populations of wild species in urban areas are blurring the lines between domestic and wild animals", "urban areas with growing populations of wild species", "therapeutic use of animals", "animals - therapeutic use of", "human-animal communication", "biological species loneliness", "human exceptionalism", "human exceptionalism - altered view of", "human-animal communication - life-changing encounters with animals", "human loneliness - aching hearts", "loneliness - aching hearts", "human-animal coexistence - wild animals & domestic animals & robotic pets", "herping", "US herping", "animal-assisted self-care", "human-animal coexistence - wildlife & therapy & pet effect", "uncanny valley of lifelike humanoid robots & realistic computer-generated faces", "virtual worlds", "virtual communities", "alternative universe", "age of connectedness", "cohabitation", "cohabitation - new contract for", "neophiles", "neophiliacs", "neophilia", "neophobia", "neophobes", "metathesiophobia", "prosophobia", "cainotophobia", "cainophobia", "kainophobia", "kainolophobia", "built environment", "built world", "urbanism - human interaction with wildlife in the built environment", "urbanism - human interaction with wildlife in the built world", "landscape urbanism", "green urbanism", "sustainable urbanism", "sustainable corridors", "biophilia hypothesis", "BET", "habitat fragmentation", "habitat fragmentation caused by urbanization", "habitat fragmentation caused by human development", "habitat fragmentation - exogenous threats", "habitat fragmentation - exogenous threats due to habitat degradation & habitat subdivision & habitat isolation", "habitat fragmentation - endogenous threats", "edge effects of habitat degradation", "edge effects of urbanism-driven habitat degradation", "microenvironments", "forest fragmentation", "island biogeography", "habitat destruction", "habitat loss", "habitat reduction", "habitat destruction caused by urbanization", "habitat loss caused by urbanization", "habitat reduction caused by urbanization", "deforestation", "clearance (deforestation)", "clearcutting (deforestation)", "clearing (deforestation)", "edge effects of urbanism-driven habitat degradation - increasing probabilities of human interaction with wildlife", "edge effects of urbanism-driven habitat degradation - increasing probabilities of human interaction with wildlife increases need for intelligent urbanism", "ecological habitats", "habitats (ecology)", "community (ecology)", "community ecology", "synecology", "macroecology", "microecosystems", "systems ecology", "ecosystems ecology", "ecological engineering", "human impact on the environment", "anthropogenic impact on the environment", "community resilience", "environmental issues", "relationship between urbanization & environmental issues", "impact of urbanization on biophysical environments", "evolutionary ecology", "sociobiology", "human behavioral ecology", "HBE", "human evolutionary ecology", "Darwinian anthropology", "biosemiotics", "social evolution", "ecosystem health", "human impact on the environment - due to urbanization", "relationship between urbanization & ecosystem health", "impact of urbanization on ecosystem health", "environmental epidemiology", "communicable disease epidemiology", "cultural epidemiology", "relationship between urbanization & deforestation & ecosystem health", "impact of urbanization & deforestation on ecosystem health", "exposure science", "ecosystem management", "ecosystem-based management", "natural resource management", "ecological health", "microhabitats", "spatial ecology", "spatial dynamics of population & community ecology", "population ecology", "autecology", "species distribution", "population dynamics", "deep ecology", "ecological stoichiometry", "biological stoichiometry", "environmental humanities", "ecological humanities", "cross-boundary subsidies", "habitat patch boundaries", "patches (landscape ecology)", "patch dynamics", "matrices (background ecological system)", "landscape ecology", "landscape connectivity", "biogeography", "historical biogeography", "ecological biogeography", "comparative biogeography", "systematic biogeography", "evolutionary biogeography", "biogeographic regionalization", "ecological disturbances", "natural disturbances (ecology)", "anthropogenic disturbances (ecology)", "major ecological disturbances", "cyclic disturbances (ecology)", "ecological succession (ecology)", "ecological succession", "human-wildlife conflict", "interaction between wild animals & humans", "interaction between wild animals & humans - negative impact on people & animals & resources & habitats", "interaction between wild animals & humans - growing human populations overlap with established wildlife territory & creating competition for space and resources", "interaction between wild animals & humans - loss of life & injury to humans and wild animals & depredation of livestock & degradation of habitat", "forest dynamics", "forest disturbances", "environmental stressors", "daily 'stress' events", "chemical stressors", "ecotones", "ecotone transitions", "ecoclines", "ecocline transitions", "ecotypes", "ecospecies", "landscape epidemiology", "metapopulations", "resource selection functions", "RSFs", "source-sink dynamics", "habitat/species management areas", "human development (economics)", "environmental security", "health security (human security)", "human security", "personal security", "community security", "political security", "wildlife crossings", "habitat conservation", "habitat fragmentation due to human-made barriers", "habitat fragmentation due to human-made barriers - roads & railroads & canals & electric power lines & pipelines", "wildlife populations", "wildlife populations affected by demographic & genetic & environmental stochasticity", "wildlife populations affected by demographic stochasticity", "wildlife populations affected by genetic stochasticity", "wildlife populations affected by environmental stochasticity", "restoration ecology", "ecological restoration", "community assembly (community ecology)", "conservation biology", "anthropogenic impact on ecosystems", "wildlife corridors", "habitat corridors", "green corridors", "generalist species", "specialist species", "SLOSS debate in ecology & conservation biology about single large or several small reserves", "edge effects (ecology)", "urban homesteading", "sustainable living", "urban agriculture", "urban gardening", "urban farming", "peri-urban agriculture"]
a = max(list_of_keywords, key=list_of_keywords.count)
print("a is:",a,"=")
"""
	Uncomment the next line if elements in the list have different occurring frequencies.
"""
#############print("mode is:", statistics.mode(list_of_keywords),"=")
"""
	From https://www.geeksforgeeks.org/python-list-frequency-of-elements/
	Last accessed on May 18, 2020.
	Author: manjeet_04.
	No date of publication.
"""
print("Test methods from: https://www.geeksforgeeks.org/python-list-frequency-of-elements/")
print("Method 1.")
res = dict(Counter(i for i in list_of_keywords))
#print("The list frequency of elements is: ", str(res), "=")
for j in res:
	print("j is:",j,"with count:",res[j],"=")
"""
	Method cannot work for a list/set, because it works for a set of sets,
		or list of lists, or container of containers.

	print("Method 2.")
	from itertools import chain
	res = dict(Counter(chain.from_iterable(map(set, list_of_keywords))))
"""
#res = all([val[1] == ])
print("=======================================================")
print(" Test methods on list of keywords with duplicates.")
duplicates_in_list = ["wildlife relocation", "growing populations of wild species in urban areas are blurring the lines between domestic and wild animals", "urban areas with growing populations of wild species", "therapeutic use of animals", "animals - therapeutic use of", "human-animal communication", "biological species loneliness", "human exceptionalism", "human exceptionalism - altered view of", "human-animal communication - life-changing encounters with animals", "human loneliness - aching hearts", "loneliness - aching hearts", "human-animal coexistence - wild animals & domestic animals & robotic pets", "herping", "US herping", "animal-assisted self-care", "human-animal coexistence - wildlife & therapy & pet effect", "uncanny valley of lifelike humanoid robots & realistic computer-generated faces", "virtual worlds", "animals - therapeutic use of", "animals - therapeutic use of", "animals - therapeutic use of", "animals - therapeutic use of", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "herping", "virtual worlds", "virtual worlds", "virtual worlds", "human-animal communication", "human-animal communication", "human-animal communication", "human-animal communication", "US herping", "US herping", "loneliness - aching hearts"]
print("mode is:", statistics.mode(duplicates_in_list),"=")
res = sorted(duplicates_in_list, key = lambda ele: duplicates_in_list.count(ele))
for j in res:
	#print("j is:",j,"with count:",res[j],"=")
	print("j is:",j,"=")
print("res is:",res,"=")
res = dict(Counter(i for i in duplicates_in_list))
for j in res:
	print("j is:",j,"with count:",res[j],"=")
print("=======================================================")
print("From: https://stackoverflow.com/a/613218/1531728.")
import operator
print("	= Sorted dict in ascending order.")
res_sorted =  {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}
for j_s in res_sorted:
	print("j_s is:",j_s,"with count:",res[j_s],"=")
print("	= Sorted dict in descending order.")
res_x =  {k: v for k, v in sorted(res.items(), key=lambda item: item[1], reverse=True)}
for j_x in res_x:
	print("j_x is:",j_x,"with count:",res[j_x],"=")
"""
sorted_dict = sorted(res.values())
for j_d in sorted_dict:
	print("j_d is:",j_d,"with count:",res[j_d],"=")
"""
print("From https://stackoverflow.com/a/22150003/1531728")
res_des = dict(Counter(i for i in duplicates_in_list).most_common())
for j_des in res_des:
	print("j_des is:",j_des,"with count:",res[j_des],"=")
print("From https://stackoverflow.com/a/7947321/1531728")
for word in sorted(res, key=res.get, reverse=True):
	print("word is:",word, "and frequency is:",res[word],"=")
print("https://stackoverflow.com/a/50554874/1531728")
res_lst = sorted([(v, k) for k, v in res.items()], reverse=True)
for r in res_lst:
	print("r is:",r,"=")
"""
	References that were looked at, but did not use:
	+ https://www.geeksforgeeks.org/python-sort-given-list-by-frequency-and-remove-duplicates/?ref=rp
	+ https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/

	For more solutions, see:
	+ https://stackoverflow.com/q/613183/1531728
"""