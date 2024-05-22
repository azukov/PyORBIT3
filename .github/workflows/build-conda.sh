. /opt/conda/etc/profile.d/conda.sh
conda env create -n pyorbit --file environment.yml
conda activate pyorbit
pip install -U meson-python setuptools setuptools-scm
pip install --no-build-isolation --editable .