.PHONY: lint
lint:
	pylint aoc tests
	mypy aoc tests

.PHONY: test
test:
	python -m unittest discover
	aoctools run_examples 1
	aoctools run_examples 2
	aoctools run_examples 3
	aoctools run_examples 4
	aoctools run_examples 5
