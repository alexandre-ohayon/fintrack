# 📊 FinTrack – Générateur de rapports financiers

![CI](https://github.com/alexandre-ohayon/fintrack/actions/workflows/ci-cd.yml/badge.svg)

FinTrack est une API REST écrite en Flask permettant de **générer dynamiquement des rapports financiers en PDF**.  
Le projet inclut une stack DevOps complète avec :
- CI/CD via GitHub Actions ✅
- Monitoring via **Prometheus + Grafana** 📈
- Conteneurisation **Docker + Docker Compose** 🐳

---

## 🚀 Fonctionnalités

- Génération de PDF avec ReportLab
- Export téléchargeable `/api/report.pdf`
- Compteur de requêtes Prometheus (`/metrics`)
- Dashboard Grafana en live
- Artefact PDF attaché à chaque build CI

---

## ⚙️ Stack technique

- **Backend** : Python 3.11, Flask
- **CI/CD** : GitHub Actions
- **Observabilité** : Prometheus, Grafana
- **Conteneurs** : Docker, Docker Compose
- **Tests** : Pytest, flake8

---

## 🔧 Installation locale

```bash
git clone https://github.com/alexandre-ohayon/fintrack.git
cd fintrack/docker
docker-compose up --build
```
---

## 📬 Utilisation de l'API

### Générer un PDF :
```bash
curl -X POST http://localhost:5000/api/report \
  -H "Content-Type: application/json" \
  -d '{"name":"Alexandre", "amount":3000}'
```

## 📬 Utilisation de l'API (Kubernetes)

> ⚠️ Dans un environnement Kubernetes, récupérez l'URL avec :

```bash
minikube service backend --url
```

```bash
API_URL=$(minikube service backend --url)
curl -X POST "$$API_URL/api/report" \
  -H "Content-Type: application/json" \
  -d '{"name":"Alexandre", "amount":3000}'
  ```i

### Télécharger le PDF :
[http://localhost:5000/api/report.pdf](http://localhost:5000/api/report.pdf)

---

## 📈 Dashboard Grafana

> Accessible sur [http://localhost:3000](http://localhost:3000)

![Dashboard Grafana](docs/grafana-preview.png)

---

## 🤖 CI/CD GitHub Actions

- ✅ Lint (flake8)  
- ✅ Tests unitaires (pytest)  
- ✅ Génération de PDF  
- ✅ Upload du PDF en artefact attaché au job  

---

## 🧪 Test local

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
---

## 🛣️ À venir

- Kafka ou Redis pour traitement async  
- Export vers S3 ou Google Drive  
- Alertes Prometheus  
- Intégration avec un front Angular

---

## 🔒 Login Grafana
URL : http://127.0.0.1:xxxxx (fourni par minikube service)

Login : admin
Password : admin