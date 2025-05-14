FROM node:18

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install Node.js dependencies
RUN npm install

# Install Python dependencies (if any)
RUN pip3 install yfinance  # Uncomment if you need pip modules

# Default command
CMD ["node", "server.js"]
