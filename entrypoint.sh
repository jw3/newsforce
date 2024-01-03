#!/usr/bin/env bash

ARTICLE_DIR="${PWD}/${INPUT_ARTICLE_DIR}"

if [[ "${INPUT_DEBUG,,}" == "true" ]]; then
  echo "=== Debug Mode Enabled ==="
  echo "Article dir: ${ARTICLE_DIR}"
  ls -al ${ARTICLE_DIR}
fi

cd /action

python check.py --categories=${INPUT_CATEGORIES}         \
                --ignores=${INPUT_IGNORES}               \
                --contrib_guide_url=${INPUT_CONTRIB_URL} \
                ${ARTICLE_DIR}
