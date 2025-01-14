lint:
	@uv run black --line-length 80 backend/.
	@uv run isort backend/.
	@uv run ruff check backend/.
	@uv run mypy --explicit-package-bases \
		--fast-module-lookup \
		--ignore-missing-imports \
		--strict backend/.
