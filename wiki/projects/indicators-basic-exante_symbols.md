# indicators-basic-exante_symbols

**Категория:** 🚀 [ProfitRadar Platform](../categories/profitradar_platform.md)
**Статус:** 📁 no-git
**Путь:** `/Users/andriy/gitlab-prod/indicators-basic-exante_symbols`

## 🛠 Tech Stack

- **Languages:** Python
- **Frameworks:** FastAPI, NumPy, Pandas
- **Tools:** Docker, Docker Compose, pip

## 📁 Files (32 indexed)

### Docs (6 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `requirements.txt` | 340 B | 2026-03-02 |
| `Readme.md` | 2 KB | 2026-03-02 |
| `API_EXAMPLES.md` | 2 KB | 2026-03-02 |
| `Blueprint.md` | 374 B | 2026-03-02 |
| `api/README.get_real_complex_ind.md` | 5 KB | 2026-03-02 |
| `api/readme-cache-endpoints.md` | 9 KB | 2026-03-02 |

### Config (2 files, 0.0 MB)

| File | Size | Modified |
|------|------|----------|
| `docker-compose.yml` | 269 B | 2026-03-02 |
| `.gitlab-ci.yml` | 2 KB | 2026-03-02 |

### Code (24 files, 0.5 MB)

| File | Size | Modified |
|------|------|----------|
| `app/test_data.py` | 3 KB | 2026-03-02 |
| `app/main.py` | 2 KB | 2026-03-02 |
| `app/data.py` | 6 KB | 2026-03-02 |
| `newapi/app.py` | 4 KB | 2026-03-02 |
| `api/ti_api.py` | 187 KB | 2026-03-02 |
| `api/ast_parser.py` | 42 KB | 2026-03-02 |
| `api/cache_diagnostics.py` | 13 KB | 2026-03-02 |
| `api/cache_api_endpoints.py` | 24 KB | 2026-03-02 |
| `api/cached.py` | 11 KB | 2026-03-02 |
| `api/calculate_vpfr_optimized.py` | 18 KB | 2026-03-02 |
| `api/ast_integration.py` | 44 KB | 2026-03-02 |
| `api/volume_profile.py` | 63 KB | 2026-03-02 |
| `api/test_api.py` | 19 KB | 2026-03-02 |
| `api/cache_tests.py` | 32 KB | 2026-03-02 |

## 📝 README

```
# Technical Indicators API

This is a FastAPI-based API for calculating various technical indicators for financial market data. It supports historical data retrieval, real-time data processing, and feature extraction.

## Features

- Historical data retrieval with technical indicators
- Real-time data processing with technical indicators
- Feature extraction and CSV file generation
- Support for multiple assets and timeframes
- Customizable technical indicators

## Prerequisites

- Python 3.9+
- ClickHouse database
- Docker (optional)

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with the following contents:

   ```bash
   CH_HOST=<your-clickhouse-host>
   CH_PASS=<your-clickhouse-password>
   CH_USER=<your-clickhouse-username>
   CH_PORT=<your-clickhouse-port>
   ```

4. Run the API:

   ```bash
   uvicorn ti_api:app --reload
   ```

## Docker Setup

1. Build the Docker image:

   ```bash
   docker build -t technical-indicators-api .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 5000:5000 -d technical-indicators-api
   ```

## Usage

The API provides three main endpoints:

1. `/historical`: Retrieve historical data with calculated indicators
2. `/realtime`: Get real-time data with calculated indicators
3. `/get_features`: E
```
