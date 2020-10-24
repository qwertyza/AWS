FROM cdrx/pyinstaller-linux

WORKDIR /usr/src/app

RUN pip install pysimplegui
RUN pip install awscli

ENTRYPOINT curl ${INPUT_PYFILE_URL} --output tobuild.py && pyinstaller --onefile --windowed tobuild.py && aws s3 cp dist ${OUTPUT_BUCKET}
