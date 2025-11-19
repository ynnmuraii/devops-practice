
#!/bin/bash
set -e

APP_DIR="/home/user/devops/devops-practice"
VENV_DIR="$APP_DIR/venv"
LOG_FILE="$APP_DIR/uvicorn.log"
PORT=8181

echo "🚀 Starting deploy at $(date)"
cd "$APP_DIR"
git pull
# Активируем venv
source "$VENV_DIR/bin/activate"

# Ищем и убиваем старый uvicorn (если работает)
PID=$(pgrep -f "uvicorn app.main:app --port $PORT" || true)
if [ ! -z "$PID" ]; then
  echo "🛑 Останавливаем старый процесс uvicorn (PID=$PID)..."
  kill -9 $PID
fi

# Запуск нового uvicorn
echo "🔄 Запуск нового uvicorn на порту $PORT..."
nohup uvicorn app.main:app --host 0.0.0.0 --port $PORT > "$LOG_FILE" 2>&1 &

echo "✅ Deploy completed at $(date)"