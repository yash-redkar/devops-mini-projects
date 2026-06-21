# Project 09 Notes

## Prometheus Queries

Request rate:
sum(rate(sample_app_requests_total[1m]))

Error rate:
sum(rate(sample_app_requests_total{http_status=~"5.."}[1m]))

Request rate by endpoint:
sum(rate(sample_app_requests_total[1m])) by (exported_endpoint)

Pod CPU:
sum(rate(container_cpu_usage_seconds_total{namespace="monitoring-demo", pod=~"monitoring-demo-app.*"}[1m])) by (pod)

Pod memory:
sum(container_memory_working_set_bytes{namespace="monitoring-demo", pod=~"monitoring-demo-app.*"}) by (pod)