#! /bin/bash

# Get current working directory
working_dir=$(dirname $0)

# Delete existing distributions
rm -r "${working_dir}/dist"

# Build distribution
python setup.py sdist bdist_wheel

# Upload to PyPi
twine upload \
--repository-url "https://test.pypi.org/legacy/" \
"${working_dir}/dist/*"