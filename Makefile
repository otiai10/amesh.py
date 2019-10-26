
release: dist
	twine upload dist/*

dist:
	python setup.py sdist

clean:
	$(RM) -rf dist
