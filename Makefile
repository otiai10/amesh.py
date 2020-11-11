
release: dist
	twine upload dist/*

dist: clean
	python setup.py sdist

clean:
	$(RM) -rf dist
