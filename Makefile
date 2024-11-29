SOURCES=cgeo.c $(wildcard src/cgeo/*.py)

.PHONY: build clean

build: $(SOURCES)
	pip wheel -w dist .

clean:
	rm -rf dist build src/*.egg-info src/cgeo/*.pyd src/cgeo/*.so
