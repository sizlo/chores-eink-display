FROM python:3

RUN pip3 install Pillow
RUN pip3 install inky
RUN pip3 install requests

CMD python3 /home/chores-eink-display.py --type impressions
