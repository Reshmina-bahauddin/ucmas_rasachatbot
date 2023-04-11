FROM python:3
ENTRYPOINT []
RUN  python3 -m pip install --upgrade pip && pip install rasa && pip install -U spacy && python -m spacy download en_core_web_lg && pip install db-sqlite3
ADD ./ app/
RUN chmod +x/app/start_services.sh
CMD /app/start_services.sh
