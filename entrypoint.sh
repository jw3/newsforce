#!/usr/bin/env bash

if [[ "${INPUT_DEBUG,,}" == "true" ]]; then
  echo "=== Debug Mode Enabled ==="
  ls -al ${INPUT_ARTICLE_DIR}
fi

cd /action

python check.py --categories=${INPUT_CATEGORIES}         \
                --ignores=${INPUT_IGNORES}               \
                --contrib_guide_url=${INPUT_CONTRIB_URL} \
                ${INPUT_ARTICLE_DIR}
