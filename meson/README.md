### Building with meson
This project demonstrates how to build python/C++ modules using meson-python.
All meson related files are in **meson-build** directory. C++ compiler should be installed.
1. Initial setup
```bash
python -m venv .mp3
source .mp3/bin/activate
pip install -U pip
pip install -r requirements.txt
```
2. Development build (editable install)
```bash
pip install --no-build-isolation --editable .
```
3. Or install as normal
```bash
pip install .
```
4. Test installation
```bash
python test.py
```