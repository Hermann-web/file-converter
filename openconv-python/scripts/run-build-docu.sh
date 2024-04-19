#!/bin/bash

poetry export -f requirements.txt --output ./docs/requirements.txt --without-hashes --with buildthedocs

sphinx-apidoc ./openconv/ -o ./docs/source/openconv/ -f -E

cd docs
make html
cd ..
open docs/build/html/index.html
