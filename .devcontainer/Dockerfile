FROM maven:3-eclipse-temurin-11

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    USER=compiler

RUN useradd --create-home --shell /bin/bash $USER && \
    mkdir /toggl_py && \
    mkdir -p /home/$USER/.local/bin && \
    chown -R $USER /toggl_py && \
    chown -R $USER /home/$USER

RUN apt update && \
    apt install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt update && \
    apt install -y python3.11 python3-pip && \
    ln -s /usr/bin/python3.11 /usr/bin/python

USER $USER

RUN wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.19/swagger-codegen-cli-2.4.19.jar \
        -O /home/$USER/.local/bin/swagger-codegen-cli.jar

ENV PATH "/home/$USER/.local/bin:$PATH"
WORKDIR /home/$USER/toggl-py

COPY toggl_py/docs/requirements.txt toggl_py/docs/requirements.txt

RUN python -m pip install --upgrade pip && \
    pip install black pre-commit && \
    pip install -r toggl_py/docs/requirements.txt

COPY LICENSE LICENSE
COPY codegen/ codegen/

CMD ["sleep", "infinity"]
