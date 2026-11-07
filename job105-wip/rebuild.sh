#!/bin/bash
# Rebuild the working master: approved edits, then Chapter 10. Result: ch10/BOOK2-ch10.md
set -e
SP=/tmp/claude-0/-home-user-private/08506865-a31e-5a6b-9772-f4733aaf6b07/scratchpad
python3 -I $SP/working/apply_approved.py
python3 -I $SP/ch10/build_ch10.py
