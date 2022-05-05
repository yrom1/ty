When entering the terminal with `ty -`, black isort and the type checker
    should run. If they didn't run it would offer no benefit to using `py`
    and sometimes I want to test something in a terminal and running the
    suite would be helpful to not import something with type errors in the tty.

---

If `ty` is used to run a file in a different folder, it uses the default `mypy`
because it can't find a `pyproject.toml` in the `$(realpath dirname $PWD)`.

Should it do this? Is it possible to find what module a script belongs to?
What happens for namespace packages?

---

Fix the paths in the tests folders using new `example` path

---
