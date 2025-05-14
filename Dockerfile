FROM node:18

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Install pnpm
RUN npm install -g pnpm

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install Node.js dependencies
RUN pnpm install

# Install Python dependencies (if any)
RUN pip3 install yfinance

# Default command
CMD ["node", "server.js"]
