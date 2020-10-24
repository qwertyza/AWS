FROM cdrx/pyinstaller-linux

WORKDIR /usr/src/app

RUN pip install pysimplegui
RUN pip install awscli
RUN aws configure set aws_access_key_id ${ACCESSKEY}
RUN aws configure set aws_secret_access_key ${SECRETKEY}
RUN echo ${SECRETKEY}

ENTRYPOINT 
aws configure set aws_access_key_id ${ACCESSKEY} &&
aws configure set aws_secret_access_key ${SECRETKEY} &&
echo ${SECRETKEY} &&
curl ${INPUT_PYFILE_URL} --output tobuild.py &&
pyinstaller --onefile --windowed tobuild.py &&
aws s3 cp dist ${OUTPUT_BUCKET}
