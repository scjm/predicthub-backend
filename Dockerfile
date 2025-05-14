FROM node:18

# Install Python and pip
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install pnpm
RUN npm install -g pnpm

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install Node.js dependencies
RUN pnpm install --frozen-lockfile

# Install Python dependencies
RUN python3 -m pip install --no-cache-dir yfinance

# Start the server
CMD ["node", "server.js"]
