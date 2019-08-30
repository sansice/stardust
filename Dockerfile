FROM python:3

WORKDIR /usr/src/app

COPY reqs.txt ./
RUN pip install --no-cache-dir -r reqs.txt

EXPOSE 5000

COPY . .

CMD [ "python", "./book_search/start.py" ]