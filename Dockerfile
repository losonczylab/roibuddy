FROM python:2.7.11

RUN mkdir /roibuddy
WORKDIR /roibuddy

RUN apt-get update -qq && apt-get install -qq libatlas-dev libatlas-base-dev liblapack-dev libgeos-dev

ENV PYTHONPATH "/usr/share:/usr/lib/python2.7/dist-packages:$PATH"

RUN pip install sima

RUN apt-get install -qq python-qwt5-qt4 python-sip python-qt4

RUN rm -r /usr/lib/python2.7/dist-packages/numpy*

RUN pip install cython

RUN pip install guidata
 
RUN pip install guiqwt
 
RUN pip install matplotlib

COPY . /roibuddy

RUN pip install .

CMD python roibuddy/roi_buddy.py
