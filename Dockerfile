FROM lambgeo/lambda:gdal2.4-py3.7-geolayer

WORKDIR /tmp

ENV PYTHONUSERBASE=/var/task

COPY setup.py setup.py

# Install dependencies
RUN pip install . --user
RUN cd ${PYTHONUSERBASE}/lib/python3.7/site-packages/ && zip -r9q /tmp/package.zip *

COPY handler.py handler.py
RUN zip -r9q /tmp/package.zip handler.py

COPY tests/ tests/
RUN zip -r9q /tmp/package.zip tests/
