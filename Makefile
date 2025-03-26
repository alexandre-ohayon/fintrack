# 📦 Variables
DOCKER_COMPOSE = docker-compose -f docker/docker-compose.yml
ANSIBLE_PLAYBOOK = ansible-playbook -i ansible/inventory.ini ansible/playbooks/local.yml

# 🐳 Docker
up:
	@echo "🚀 Démarrage de la stack Docker..."
	$(DOCKER_COMPOSE) up --build -d

down:
	@echo "🧹 Arrêt des conteneurs..."
	$(DOCKER_COMPOSE) down

logs:
	@echo "📋 Logs backend..."
	$(DOCKER_COMPOSE) logs -f backend

# 🧪 Tests
test:
	@echo "🧪 Lancement des tests unitaires avec couverture..."
	cd backend && PYTHONPATH=$$PWD pytest --cov=app --cov-report=term tests

lint:
	@echo "🔍 Lint du code Python..."
	cd backend && flake8 app

# ⚙️ Provision Ansible
ansible:
	@echo "⚙️  Provisionnement local via Ansible..."
	$(ANSIBLE_PLAYBOOK)

# 📁 Nettoyage
clean:
	@echo "🧽 Suppression des fichiers générés..."
	rm -rf backend/output/*.pdf backend/__pycache__ backend/app/__pycache__

# 🚨 All
all: lint test