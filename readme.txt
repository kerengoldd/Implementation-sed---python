I have implement the functionality of linux's sed command in python.

Usage format:
There are 2 usage formats:

1. Run script as: (On a file)

	python sed.py -f  "pattern" "replacement"  file.txt

	Above command replicates:
	sed "s/pattern/replacement/" file.txt

	sed.py : is the python script file.
	-f : option that specify that last argument is text file (remove -f if you want last option to be a text string)
	"pattern": Any regular expression or word you want to replace. (Specified inside quotes i.e. "")
	"replacement": Word which will be substituted whenever the pattern is matched. (Specified inside quotes i.e. "")
	file.txt : path to any file.

2. Run script as: (On a string)

	python sed.py "pattern" "replacement" "test string" 

	Above command replicates:
	echo "test string" | sed "s/pattern/replacement/" 

	sed.py : is the python script file.
	"pattern": Any regular expression or word you want to replace. (Specifies inside quotes i.e. "")
	"replacement": Word which will be substituted whenever the pattern is matched. (Specified inside quotes i.e. "")
	"test string" : String on which sed will work. (Specified inside quotes i.e. "")

	Note: For String we dont specify -f
