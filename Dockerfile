FROM python:3.9 

ENV bot_token=''
ENV chat_id=""

WORKDIR /wordeli/

RUN apt-get update 
RUN apt-get -y install cron nano

COPY wordeli.py ./
COPY tgbot.py ./
COPY post.sh ./
COPY requirements.txt ./
COPY stardict.py ./
COPY trans.py ./
COPY wordeli_dict wordeli_dict/
COPY stardicts stardicts/

RUN pip3 install -r requirements.txt

RUN chmod +x post.sh

RUN touch /var/log/cron.log

RUN (crontab -l ; echo "0 6,9,18 * * * cd /wordeli/ && sh post.sh "${bot_token}" "${chat_id}" >> /var/log/cron.log 2>&1") | crontab

CMD cron;python3 tgbot.py ${bot_token}
