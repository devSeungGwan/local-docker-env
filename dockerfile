# Base Image
FROM ubuntu:18.04

# install package
RUN apt-get update
RUN apt-get -y install postgresql libpq-dev wget curl git build-essential openssl bzip2 patch

# install pyenv
RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
RUN echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
RUN echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
RUN source ~/.bashrc

RUN sudo apt-get install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel

# Requirement Download
RUN git clone git@github.com:devSeungGwan/local-docker-env.git
RUN cd local-docker-env

# install python version
RUN pyenv install 3.7.7
RUN pyenv global 3.7.7
RUN pip install -r requirement.txt