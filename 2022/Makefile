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
	aoctools run_examples 6
	aoctools run_examples 7
	aoctools run_examples 8
	aoctools run_examples 9
	aoctools run_examples 10
