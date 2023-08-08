SOURCES=cgeo.c $(wildcard cgeo/*.py)

.PHONE: build clean

build: $(SOURCES)
	pip wheel .

clean:
	rm -rf build/ *.egg-info/ *.whl
