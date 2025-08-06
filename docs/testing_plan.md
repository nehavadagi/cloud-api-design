# Testing Methodology

## Load Testing
- **Tool**: Locust (see [example script](./src/examples/load_test.py))
- **Target**: 10,000 concurrent users
- **Metrics**: 99% requests <500ms at peak load