FROM python:3.6
WORKDIR /web-song-share/app

COPY requirements.txt /web-song-share/app
RUN apt-get update && apt-get install sudo

# RUN pip3 install --no-cache-dir --compile -r requirements.txt
RUN pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

COPY ./ /web-song-share/app

# CMD ["sudo", "gunicorn", "-w", "1", "-b", "0.0.0.0:80", "app:app"]
CMD ["python3", "app.py"]
# gunicorn -w 1 -b 0.0.0.0:80 run:app --daemon
