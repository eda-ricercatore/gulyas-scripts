#!/usr/bin/ruby -w

# For each file in this directory...
for i in 1..50		#	45..50
	puts "@book{cite-key,"
	puts "	Date-Added = {2013-11-06 03:#{60-i}:00 +0200},"
	puts "	Date-Modified = {2013-11-06 03:#{60-i}:00 +0200}}"
	puts ""
end


=begin
@proceedings{cite-key,
        Date-Added = {2012-04-07 20:19:29 +0200},
        Date-Modified = {2012-04-07 20:19:54 +0200}}
=end



=begin
for i in 1..50		#	45..50
	puts "@proceedings{cite-key,"
	puts "	Date-Added = {2013-03-21 05:#{60-i}:00 +0200},"
	puts "	Date-Modified = {2013-02-21 05:#{60-i}:00 +0200}}"
	puts ""
end
=end