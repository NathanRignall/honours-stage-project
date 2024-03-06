# Basic Makefile for LaTeX projects by Markus Kuhn modified by Nathan Rignall

# requires GNU make
SHELL=/bin/bash

.DELETE_ON_ERROR:

# Build rules for LaTeX-related files
%.dvi: %.tex
	(latex $<; makeindex $*; makeglossaries $*; bibtex $*; latex $<)
	while grep 'Rerun to get ' $*.log ; do (makeindex $*; makeglossaries $*; bibtex $*; latex $<); done
	-killall -USR1 -r xdvi || true

%.ps: %.dvi
	dvips -Ppdf -G0 $*.dvi

# build the final PDF from the LaTeX source
TEX_DEPS := $(shell find . -name '*.tex') $(shell find . -name '*.py')
%.pdf: %.tex $(TEX_DEPS)
	(pdflatex $<; makeindex $*; makeglossaries $*; bibtex $*; pdflatex $<)
	while grep 'Rerun to get ' $*.log ; do (makeindex $*; makeglossaries $*; bibtex $*; pdflatex $<); done
	
# run all python scripts to generate figures
PYTHON_DEPS := $(shell find . -name 'generate.py')
graphics: $(PYTHON_DEPS)
	@echo "Running python scripts to generate figures"
	@for f in $(PYTHON_DEPS); do cd `dirname $$f` && python `basename $$f` && cd -; done

all: graphics thesis.pdf

clean:
	rm -f *~ *.dvi *.log *.bak *.aux *.toc *.ps *.eps *.blg *.bbl
	rm -f *.glg *.glo *.gls *.idx *.ild *.ind *.ist *.ilg *.iso *.out
	rm -f *.pstex *.pstex_t
	rm -f thesis.pdf
