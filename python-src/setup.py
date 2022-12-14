import os
from pathlib import Path
from setuptools import setup, find_packages  # type: ignore[import]

reqs = Path("requirements.txt").read_text().splitlines()


def main() -> None:
    this_dir = Path(__file__).absolute().parent
    if os.getcwd() != str(this_dir):
        print(f"setuptools: cd'ing to {this_dir}")
        os.chdir(this_dir)

    setup(
        name="seanb",
        packages=["seanb"],
        url="https://github.com/seanbreckenridge/core",
        author="Sean Breckenridge",
        author_email="seanbrecke@gmail.com",
        python_requires=">=3.8",
        zip_safe=False,
        install_requires=reqs,
        description="seanb core utilities/functions",
        package_data={"seanb": ["py.typed"]},
        license="MIT",
        version="0.1.0",
    )


if __name__ == "__main__":
    main()
