#!/bin/bash
echo "Running server"
uvicorn main:app --reload --reload-dir "/code/" \
  --host 0.0.0.0 --port 8080 --log-level debug --workers 1