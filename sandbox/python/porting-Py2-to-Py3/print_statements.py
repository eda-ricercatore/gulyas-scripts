#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

print("1st String 1.")
print("2nd String {}." .format(27436))
print("3rd String {}.".format(-34567890987654))
print("4th String {0}, {1}%, {2}.".format(8723,23.1,98))
print("5th String:{}." "broken")
print("6th String:{}." .format("broken"))
println = "7th String:{}." 
print(println.format("ends here"))

print("========================================================")

BibTeX_entry_types = ["article", "book", "booklet", "inbook", "incollection", "inproceedings", "manual", "mastersthesis", "misc", "phdthesis", "proceedings", "techreport", "unpublished"]

println = "=	BibTeX entry type:"
for i in BibTeX_entry_types:
	print(println,i,"_")

print("========================================================")

println = "=	Show BibTeX entry type:{}="
for i in BibTeX_entry_types:
	print(println.format(i))

print("========================================================")

print(*BibTeX_entry_types)

print("========================================================")

println = "=	Display BibTeX entry type:"
print(println,*BibTeX_entry_types, sep=",")

print("========================================================")

println = "=	All BibTeX entry types:"
print(*BibTeX_entry_types, sep=",")

print("========================================================")

println = "=	Clean BibTeX entry types:"
print(*BibTeX_entry_types, sep=",", end=".\n")

print("========================================================")

println = "=	For all BibTeX entry types:"
print(println,*BibTeX_entry_types, sep="_", end=".\n")

print("========================================================")

println = "=	Print list (1):"
print(println,*BibTeX_entry_types, end=".\n")

print("========================================================")

println = "=	Print list (2):"
print("=".join(str(x) for x in BibTeX_entry_types))
print("")
println += "=".join(str(x) for x in BibTeX_entry_types)
print(println)
print("")
print("+".join(map(str, BibTeX_entry_types)))

print("========================================================")

print("=	Print stuff (1).")

a_string = "This is a string, "
b_string = "which I wrote."
a_string += b_string
print(a_string)















#	exec("ls -al") does not work. exec() only executes Python code.






