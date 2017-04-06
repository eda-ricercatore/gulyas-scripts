#!/usr/bin/ruby -w

=begin
	Program to provide the functionality that the UNIX
	command/utility/tool "cscope" has.
	It shall search for keywords in file types specified by the user.

	This "search" tool shall be called as follows:
	find.rb [directory to search for keyword] [search key] [file types]

	NOTE: File types shall commence with a period. This is used to
	distinguish file extensions from substrings in the filename that
	can contain the same substring as file extensions.
	WARNING: The inherent bug with this choice is that source files
	for a particular language shall be associated with particular
	file extensions. If all of these extensions are not provided to
	this program by the user, this program will not search files that
	are not specified.

	Copyright (C) <2010>	<Zhiyang Ong>
	@author Zhiyang Ong; email address: [first name] -A_T.- the domain
			of IEEE ~D=O+t. o-r_g
=end

#####################################################################

# Beginning of the program

# -------------------------------------------------------------------

# Definition of methods used in this Ruby program.

# -------------------------------------------------------------------

=begin
	Method to compare two strings, and determine if they end with the
	same substring.

	One of the strings represents a filename, while the other represents
	a file extension. The filename should be longer than the file
	extension. The filename should contain the file extension as its
	terminating substring.

	Note that any filename starting with a period is a hidden file.
	If hidden files have file extensions in their filenames, the
	filenames should have multiple periods. Thus, the file extensions
	of these filenames start from the last period (just like regular
	files).
	
	Compare these strings by extracting the file extension from the
	filename and comparing it with the desired "file extension".
	If they are equal, the filename contains the desired file
	extension.
	Else, the filename does not contain the desired file extension.
	
	@param f_name - The filename of the file that is being enumerated.
	@param f_extn - The file extension that the program is currently
					enumerating files with.
	@precondition - The filename shall have at least one character more
					than the file extension.
	@return TRUE if f_name contains f_extn as its terminating substring;
			else, it returns FALSE.
=end
def fname_include_fextn(f_name, f_extn)
	# Precondition: Is the filename longer than the file extension?
	if f_name.length <= f_extn.length
		# No. The filename cannot contain the file extension.
		return false
	else
		# Yes. Extract the file extension of the filename, and compare
		# it with the desired "file extension". Are they equal?
		if (File.extname(f_name)).eql?(f_extn)
			# Yes. The filename contains the desired file extension.
			return true
		else
			# No. The filename does not contain the desired file
			# extension.
			return false
		end
	end
end

# -------------------------------------------------------------------

=begin
	Method to recursively search the specified directory for a
	specified search key in files of specified file types.
	
	@param dir -	The directory to commence recursive search in.
	@param key -	The search key.
	@param f_extn - The file extensions of files that are considered
					in the search.
	@precondition -	Check if "dir" is a valid directory that the user
					has access to.
	@return Nothing
=end
def search_files(dir, key, f_extn)
#puts "dir is: " + dir
puts "############################################################"
puts "Val of pwd: " + Dir.pwd
	# For each file in this directory...
	for i in Dir.entries("#{dir}")
		# Print the current directory
#puts "Current working directory: " + Dir.pwd + "/" + dir
	
		# Is this file a regular file?
		if File.file?(i)
puts "==>		Currently enumerating file: " + i
			# Yes. Print out its filename.
#			puts "The file name is #{i}"
#puts "File extension of current file is: " + File.extname(i)
			
			# Enumerate each file type that shall be processed.
			for j in f_extn
#				puts "Currently enumerating file extension: #{j}"
				# Does the file extension of this file match the
				# currently enumerated file extension?
				if (File.extname(i)).eql?(j)
					puts "------------------------------------------------------------"
#					puts "Enumerating file extension: #{j}"
					#system("cat -n #{dir}/#{i} | wc -l")
					system("cat -n #{dir}#{i} | grep #{key}")
				end
				# Enumerate the next file extension.
				j = (j.to_i+1).to_s
			end
		# Is this file a directory?
		elsif File.directory?(i)
			# Yes. If this directory does not refer to the current or
			# previous directory, and is a subdirectory, recursively
			# search files in this subdirectory.
#puts "Current directory: #{i}"
#			if (!i.eql?(".")) and (!i.eql?("./")) and (!i.eql?(".."))
			if !(i.eql?(".") or i.eql?("./") or i.eql?(".."))
				# Enter recursive research...
puts "==>		Recursively search: " + Dir.pwd + "/" + i
#puts "Value of i for recursive research: " + i
				# Change to working directory to subdirectory
#				Dir.chdir(Dir.pwd + "/" + i)
				Dir.chdir("./" + i)
#puts "--	Changed current working dir to: " + Dir.pwd
#				search_files(i, key, f_extn)
#				search_files("./" + i, key, f_extn)
				search_files("./", key, f_extn)
				# Return to original working directory
				Dir.chdir("../")
#puts "--	Returned current working dir to: " + Dir.pwd
			end
			
		# Else, don't process files that aren't regular nor directories.
		end
	end
end

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------

# Start of the main procedure/method/function

puts "--------------------------------------------------------"

=begin
	Determine if there are at least three inputs to the program.

	If there exists at least one input argument, and first input
	argument is "-help", print out the specifications for the input
	arguments.
	Else, inform the user that at least three input arguments are
	required to run the program.
=end
# Are there less than 3 input arguments?
if ARGV.length < 3
	# Yes, is there a valid first argument?
	if !("#{ARGV[0]}".empty?)
		# Yes, is the first input argument "-help"?
		if "#{ARGV[0]}" == "-help"
			# Yes. Print out the input requirements
			puts "Please enter at least 3 arguments to run this script."
			puts "To recursively search for a string in all files..."
			puts "of specified/given file types in a given directory."
			puts "1st argument:			Search Directory"
			puts "2nd argument:			Search Key"
			puts "3rd to the n^{th} arguments:	File Types"
			puts
			puts "File types shall begin with a period."
			exit
		end
	end
		

	puts "At least 3 arguments are required to run this script!"
	puts "Re-run script with the -help option for more information"
	puts "on what to specify for the arguments"
	exit
end

# -------------------------------------------------------------------

# Process the arguments

=begin
	The first argument indicates the directory to carry out the
	recursive search.
=end
search_dir = "#{ARGV[0]}"
# The second argument indicates the search String.
search_key = "#{ARGV[1]}"
# The remaining arguments indicate the types of files to search for.
file_extension = "#{ARGV[2]}"

# Concatenate all the file extensions into a string.
file_ext_cp = ARGV
# What class does "file_ext_cp" belong to?
#puts "file_ext_cp.class: #{file_ext_cp.class}"

=begin
	Delete the first two arguments of the copied concatenation of
	arguments.
	
	arg_1, arg_2, arg_3, arg_4, arg_5, ...
	arg_2, arg_3, arg_4, arg_5, ... // Delete the first element
	arg_3, arg_4, arg_5, ... // Delete the "second"/first element
=end
file_ext_cp.delete_at(0)
file_ext_cp.delete_at(0)
=begin
	Obtain a String created by converting each element of the array
	to a String, separated by aSepString (" ; " in this case).
=end
file_ext_cp_cat = file_ext_cp.join(", ")
# Print the String containing all the file extensions
#puts "The concatenated string is: #{file_ext_cp_cat}"

# -------------------------------------------------------------------

# Commence the recursive search.

puts "Recursively searching #{file_ext_cp_cat} files for the String #{search_key} in #{search_dir} ..."

# Recursively search all files in the specified directory for the search key
search_files(search_dir,search_key,file_ext_cp)

puts ""
puts "End of search..."


=begin
	File extensions that I would be testing my software with.

	.cpp .h .java .mp .pl .rb .tex .txt
	
	.cpp
	.h
	.java
	.mp
	.pl
	.rb
	.tex
	.txt
		
	Dummy file extensions that are tested end with the spelling of a
	number: e.g., ".seven" or ".one". Their filenames excluding the
	file extensions are either: "random", "one", or "dummy".
	
	
	I will also test for files without file extensions. These files
	shall commence with "no_file_extn". A number is appended to the
	file name to distinguish the different files.
	That is, the filenames are given as: no_file_extn[number]
	
	
	I will also be testing files representing directories (directories).
=end