#!/usr/bin/ruby -w

=begin
	Script to run a UNIX command on files of a certain type
	in a specified directory
=end

search_dir = "."
file_extension = ".ps"



# For each file in this directory...
for i in Dir.entries("#{search_dir}")
	# If it ends with the specified/default extension
	if i.include? "#{file_extension}"
		# Print out its filename
		puts "Processing the file: #{i}"
		# And convert the PS file to PDF
		#system("cat -n #{search_dir}/#{i} | wc -l")
		system("ps2pdf #{search_dir}/#{i}")
	end
end

puts "Converted all PS files to PDF."