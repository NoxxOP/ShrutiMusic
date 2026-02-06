FROM nikolaik/python-nodejs:python3.10-nodejs20

RUN curl -L https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
    -o ffmpeg.tar.xz && \
    tar -xJf ffmpeg.tar.xz && \
    mv ffmpeg-*-static/ffmpeg /usr/local/bin/ && \
    mv ffmpeg-*-static/ffprobe /usr/local/bin/ && \
    rm -rf ffmpeg*

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start"]
