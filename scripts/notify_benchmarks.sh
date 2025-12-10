#!/usr/bin/env bash
# optional script used by CI to notify benchmark results
if [ -z "$BENCHMARK_NOTIFY_WEBHOOK" ]; then
  echo 'No webhook configured.'
  exit 0
fi
curl -X POST -H 'Content-Type: application/json' -d '{"text":"Benchmarks complete"}' "$BENCHMARK_NOTIFY_WEBHOOK"
