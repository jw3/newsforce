#!/usr/bin/env bash

cd /action

python check.py --categories=${INPUT_CATEGORIES}         \
                --ignores=${INPUT_IGNORES}               \
                --contrib_guide_url=${INPUT_CONTRIB_URL} \
                ${INPUT_ARTICLE_DIR}
