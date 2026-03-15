# Base image
FROM quay.io/jupyter/scipy-notebook:2025-12-31

# Switch to root to install Quarto
USER root

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gdebi-core \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Quarto
RUN curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.8.26/quarto-1.8.26-linux-amd64.deb \
    && gdebi --n quarto-1.8.26-linux-amd64.deb \
    && rm quarto-1.8.26-linux-amd64.deb

# Install TinyTeX for PDF rendering
RUN quarto install tinytex --no-prompt

# Switch back to the standard user
USER ${NB_USER}
