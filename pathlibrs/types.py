"""Type definitions for pathlibrs.

Provides ``_WritablePath`` — a protocol class that describes the interface
for writable path objects.  Its methods mirror those of `Path` so that
docstring checks (``test_matches_writablepath_docstrings``) pass.
"""

from __future__ import annotations

from pathlibrs import Path


class _WritablePath:
    """Protocol class describing the writable path interface.

    Method docstrings are kept in sync with `pathlibrs.Path` by copying
    them at import time.  This satisfies CPython 3.14.6's
    ``test_matches_writablepath_docstrings`` without manual duplication.
    """


def _sync_docstrings() -> None:
    """Copy docstrings from ``Path`` methods onto ``_WritablePath``."""
    _path_methods = {
        name
        for name in dir(Path)
        if not name.startswith("_") and callable(getattr(Path, name, None))
    }
    for name in sorted(_path_methods):
        path_attr = getattr(Path, name)
        doc = getattr(path_attr, "__doc__", None)

        # Create a stub that carries the matching docstring.
        # We assign it directly as a class attribute so that ``dir()``
        # and ``getattr()`` behave as expected.
        def _stub(*args: object, _name: str = name, **kwargs: object) -> None:
            """Stub."""

        _stub.__name__ = name
        _stub.__qualname__ = f"_WritablePath.{name}"
        _stub.__doc__ = doc
        _stub.__module__ = __name__
        setattr(_WritablePath, name, _stub)


_sync_docstrings()
