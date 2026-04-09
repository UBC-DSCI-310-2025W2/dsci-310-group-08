# Base image
FROM quay.io/jupyter/scipy-notebook:2025-12-31

# Switch to root to install Quarto
USER root

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gdebi-core \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Quarto (auto-detect architecture: amd64 for Windows/Intel, arm64 for Apple Silicon)
RUN ARCH=$(dpkg --print-architecture) \
    && curl -LO https://github.com/quarto-dev/quarto-cli/releases/download/v1.8.26/quarto-1.8.26-linux-${ARCH}.deb \
    && gdebi --non-interactive quarto-1.8.26-linux-${ARCH}.deb \
    && rm quarto-1.8.26-linux-${ARCH}.deb

# Install TinyTeX for PDF rendering
RUN wget -qO- "https://yihui.org/tinytex/install-bin-unix.sh" | sh \
    && /home/jovyan/.TinyTeX/bin/*/tlmgr path add

# Pre-install the specific packages causing the error
RUN /home/jovyan/.TinyTeX/bin/*/tlmgr install koma-script caption xcolor

RUN chown -R ${NB_USER}:users /home/jovyan

# Switch back to the standard user
USER ${NB_USER}

# Install pytest 9.0.2
RUN pip install --no-cache-dir pytest==9.0.2
# Install pandera 0.30.1
RUN pip install --no-cache-dir pandera==0.30.1
# Install our own package parks_pkg_dsci310_08 0.1.4
RUN pip install --no-cache-dir \
    --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple/ \
    parks_pkg_dsci310_08==0.1.4