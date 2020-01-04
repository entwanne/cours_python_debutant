PDF = zeste_de_python.pdf
ZIP = zeste_de_python.zip
SRC = $(shell find src -name "*.md" | sort -V)

FLAGS = --top-level-division=part --toc

GEN = $(PDF) $(ZIP)

$(PDF):	$(SRC)
	pandoc -V lang=fr -V geometry:margin=1in -V colorlinks=true $^ -o $@ $(FLAGS)

$(ZIP): $(SRC)
	./gen_archive.py $@ $^

clean:
	rm -f $(GEN)

re:	clean $(GEN)

.PHONY:	clean re
