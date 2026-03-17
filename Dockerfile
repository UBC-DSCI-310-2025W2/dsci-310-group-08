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
# RUN curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.8.26/quarto-1.8.26-linux-amd64.deb \
#     && gdebi --n quarto-1.8.26-linux-amd64.deb \
#     && rm quarto-1.8.26-linux-amd64.deb

# Install Quarto (auto-detect architecture: amd64 for Windows/Intel, arm64 for Apple Silicon)
RUN ARCH=$(dpkg --print-architecture) \
    && curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.8.26/quarto-1.8.26-linux-${ARCH}.deb \
    && gdebi --non-interactive quarto-1.8.26-linux-${ARCH}.deb \
    && rm quarto-1.8.26-linux-${ARCH}.deb

# Install TinyTeX for PDF rendering
RUN quarto install tinytex --no-prompt
RUN chown -R ${NB_USER}:users /home/jovyan

# Switch back to the standard user
USER ${NB_USER}