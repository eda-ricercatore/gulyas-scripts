#!/usr/bin/ruby -w

# Determine the search directory
if "#{ARGV[0]}".empty?
	#search_dir = "benchmarks"
	puts "3 arguments are required to run this script!"
	puts "Re-run script with the -help option for more information"
	exit
else
	if "#{ARGV[0]}" == "-help"
		puts "Please enter 3 arguments to run this script..."
		puts "To search for a string in all files..."
		puts "For a given file type in a given directory"
		puts "1st argument:		Search Directory"
		puts "2nd argument:		File Type (include period before file extension)"
		puts "3rd argument:		Search Key"
		exit
	else
		search_dir = "#{ARGV[0]}"
	end
end

# Determine the type of files to search for
if "#{ARGV[1]}".empty?
	file_extension = ".java"
else
	file_extension = "#{ARGV[1]}"
end
# Determine the search String
if "#{ARGV[2]}".empty?
	search_key = "IEEE"
else
	search_key = "#{ARGV[2]}"
end



puts "Searching #{file_extension} files for the String #{search_key}..."

# For each file in this directory...
for i in Dir.entries("#{search_dir}")
	# If it ends with the specified/default extension
	if i.include? "#{file_extension}"
		# Print out its filename
		puts "############################################################"
		puts "The file name is #{i}"
		#system("cat -n #{search_dir}/#{i} | wc -l")
		system("cat -n #{search_dir}/#{i} | grep #{search_key}")
	end
end

puts "End of search..."