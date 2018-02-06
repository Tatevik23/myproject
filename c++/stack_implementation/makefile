# The compiler to use.
CC = g++
# Source files of the project.
SOURCES = stack.cpp
# Object files of the project.
OBJECTS = $(SOURCES:.cpp=.o)
# The executable.
EXECUTABLE = stack

outputfile: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@

.cpp.o:
	$(CC) -c $^ -o $@
