lint-backend:
	@uv run black --line-length 80 backend/.
	@uv run isort backend/.
	@uv run ruff check backend/.
	@uv run mypy --explicit-package-bases \
		--fast-module-lookup \
		--ignore-missing-imports \
		--strict backend/.

lint-frontend:
	@pnpm run format
	@pnpm run lint

dev-run:
	@docker compose up --build

