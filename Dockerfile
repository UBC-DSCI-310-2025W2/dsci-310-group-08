FROM condaforge/miniforge3:25.9.1-0

COPY conda-lock.yml /tmp/conda-lock.yml

RUN conda install -n base -c conda-forge conda-lock -y
RUN conda-lock install -n group_08 /tmp/conda-lock.yml

RUN echo "source /opt/conda/etc/profile.d/conda.sh && conda activate group_08" >> ~/.bashrc

SHELL ["/bin/bash", "-l", "-c"]

WORKDIR /workplace

EXPOSE 8888

CMD ["/opt/conda/envs/group_08/bin/jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--IdentityProvider.token=''", "--ServerApp.password=''"]