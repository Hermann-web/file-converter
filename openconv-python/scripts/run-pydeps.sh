#!/bin/bash
pydeps --noshow ./openconv/  --cluster --rankdir LR  --max-module-depth=2 -o ./docs/deps-d2.svg
pydeps --noshow ./openconv/  --cluster --rankdir LR  --max-module-depth=3 -o ./docs/deps-d3.svg
