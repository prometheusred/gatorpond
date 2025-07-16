# gatorpond
A little end-to-end data lake dev box with an easy path to deployment


## 1️ Setup

```bash
git clone <your-repo-url>
cd gatorpond
python3 -m venv .venv
source .venv/bin/activate
pip install -r dev-requirements.txt
```

## 2 Run Local Dev
```bash
fab dev
```

## 3 Stop Services
```bash
fab down
```

## 4 Access Dagster UI
`http://localhost:3001`


## 5 Run with observability (optional)
Includes Grafana + Loki + Promtail:
```bash
fab dev_obs
```