FROM python:3.7
USER root
WORKDIR /app

ENV DEBCONF_NOWARNINGS yes
RUN apt-get update && apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install web3
RUN pip install flask

RUN git clone https://github.com/wmapst/kenshow8_eth_api.git

EXPOSE 8080

SHELL ["/bin/bash", "-c"]

CMD ["/bin/bash"]
