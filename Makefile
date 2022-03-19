.PHONY: all install

all: printText

install:
	mkdir -p ${RPM_BUILD_ROOT}/usr/local/bin
	install ./printText ${RPM_BUILD_ROOT}/usr/local/bin

printText: printText.cc
	g++ -g -o printText printText.cc
