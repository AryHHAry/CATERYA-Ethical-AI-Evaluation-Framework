# GitHub Actions Secrets & Templates (guidance)

Recommended secrets to set in repository settings -> Secrets and variables -> Actions:
- GH_PAGES_TOKEN: token with `repo` and `workflow` scope (used by pages deploy)
- CATERYA_S3_KEY / CATERYA_S3_SECRET: for uploading artifacts to S3 (if using object storage)
- BENCHMARK_NOTIFY_WEBHOOK: webhook to notify benchmark results
- DOCKERHUB_USERNAME / DOCKERHUB_TOKEN: if pushing container images
- SLACK_WEBHOOK: optional, for CI notifications

Example usage in workflow:
```yaml
env:
  S3_KEY: ${{ secrets.CATERYA_S3_KEY }}
```
