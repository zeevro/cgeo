# /// script
# dependencies = ["tomlkit"]
# ///
import pathlib

import tomlkit


def main() -> None:
    pyproject_toml = pathlib.Path('pyproject.toml')
    doc = tomlkit.loads(pyproject_toml.read_text())
    try:
        del doc['tool']['setuptools']['ext-modules']  # type: ignore[index,union-attr]
    except KeyError:
        return
    pyproject_toml.write_text(doc.as_string())


if __name__ == '__main__':
    main()
