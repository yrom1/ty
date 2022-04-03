If `ty` is used to run a file in a different folder, it uses the default `mypy`
because it can't find a `pyproject.toml` in the `$(realpath dirname $PWD)`.

Should it do this? Is it possible to find what module a script belongs to?
What happens for namespace packages?

---

Fix the paths in the tests folders using new `example` path

---
