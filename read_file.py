import sys  # To read command-line arguments

# sys.argv is a list of arguments passed to the script
# sys.argv[0] = script name
# sys.argv[1:] = arguments you pass

for filename in sys.argv[1:]:  # skip script name
    print(filename)
