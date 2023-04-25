
.PHONY: all pip init pack packfolder clean test doc run installer

all: run

pack:
	mkdir ..\..\xjuric31_xbazoa00_xkrout04\repo
	mkdir ..\..\xjuric31_xbazoa00_xkrout04\installer
	mkdir ..\..\xjuric31_xbazoa00_xkrout04\doc
	copy /b ..\install\* ..\..\xjuric31_xbazoa00_xkrout04\installer\


clean:
	del requirements.txt

run:
	python -m main

profile:
	python -m profiling

help:
	@echo Run make setup to get all dependencies

test:
	python3 -m test_simple
	python3 -m test_complex
	python3 -m test_param

setup:
	pip3 freeze > requirements.txt
	pip3 install -r requirements.txt



