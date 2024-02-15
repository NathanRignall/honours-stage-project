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

TEX_DEPS := $(shell find . -name '*.tex')

%.pdf: %.tex $(TEX_DEPS)
	(pdflatex $<; makeindex $*; makeglossaries $*; bibtex $*; pdflatex $<)
	while grep 'Rerun to get ' $*.log ; do (makeindex $*; makeglossaries $*; bibtex $*; pdflatex $<); done
	
all: thesis.pdf   # or thesis.ps

clean:
	rm -f *~ *.dvi *.log *.bak *.aux *.toc *.ps *.eps *.blg *.bbl
	rm -f *.glg *.glo *.gls *.idx *.ild *.ind *.ist *.ilg *.iso *.out
	rm -f *.pstex *.pstex_t
	rm -f thesis.pdf
