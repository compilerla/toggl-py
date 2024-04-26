FROM maven:3-eclipse-temurin-11

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    USER=compiler

RUN useradd --create-home --shell /bin/bash $USER && \
    chown -R $USER /home/$USER

RUN apt update && \
    apt install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt update && \
    apt install -y python3.11 python3-pip && \
    ln -s /usr/bin/python3.11 /usr/bin/python

RUN wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.19/swagger-codegen-cli-2.4.19.jar -O /home/$USER/swagger-codegen-cli.jar

USER $USER
ENV PATH "$PATH:/usr/bin:/home/$USER/.local/bin"
WORKDIR /home/$USER/toggl-py

RUN python -m pip install --upgrade pip && \
    pip install black pre-commit

CMD ["sleep", "infinity"]
