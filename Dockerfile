FROM node:18

# ✅ Install Python, pip, and venv with -y
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ✅ Install pnpm
RUN npm install -g pnpm

# ✅ Set working directory
WORKDIR /app

# ✅ Copy files
COPY . .

# ✅ Install Node.js dependencies
RUN pnpm install --no-frozen-lockfile

# ✅ Create Python virtual environment and install yfinance
RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --no-cache-dir yfinance

# ✅ Start server (node code will call Python from /app/venv/bin/python)
CMD ["node", "server.js"]
