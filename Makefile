lint:
	@uv run black --line-length 80 backend/.
	@uv run isort backend/.
	@uv run ruff check backend/.
