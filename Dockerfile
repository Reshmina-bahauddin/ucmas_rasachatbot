FROM ubuntu:20.04
ENTRYPOINT []
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --no-cache --upgrade pip && \
pip install --no-cache rasa==3.4.2 && pip3 install python==3.8.16 && pip3 install -U spacy && \
pip install spacy[transformers] && python -m spacy download en_core_web_lg && pip3 install db-sqlite3
ADD ./ app/
RUN chmod +x/app/start_services.sh
CMD /app/start_services.sh
