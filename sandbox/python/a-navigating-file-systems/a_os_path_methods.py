#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import os

print("= Perform split() operation.")
path_prefix, last_pathname_component = os.path.split('/my/path/to/whatever/somefile.ext')
print(path_prefix)
print(last_pathname_component)

print("= Perform splitext() operation.")
filename, file_extension = os.path.splitext('/some/path/to/somefile.ext')
print(filename)
print(file_extension)

print("= Perform splitext() operation again.")
filename, file_extension = os.path.splitext('fosca.battati')
print(filename)
print(file_extension)


print("= Perform splitext() operation yet another time.")
filename, file_extension = os.path.splitext('daniela-stefanescu')
print(filename)
print(file_extension)



print("= Perform splitext() operation on multiple file extensions.")
filename, file_extension = os.path.splitext('ansu_mani.tar.gz')
print(filename)
print(file_extension)
f_name, f_extension = os.path.splitext(file_extension)
print(f_name)
print(f_extension)
f_name1, f_extension1 = os.path.splitext(filename)
print(f_name1)
print(f_extension1)
