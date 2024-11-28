SOURCES=cgeo.c $(wildcard src/cgeo/*.py)

.PHONE: build clean

build: $(SOURCES)
	pip wheel -w dist .

clean:
	rm -rf dist build src/cgeo.egg-info src/cgeo/*.pyd src/cgeo/*.so
