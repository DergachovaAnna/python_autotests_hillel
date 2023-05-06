# crete image with Chome browser

FROM jetbrains/teamcity-agent

USER root

# instal wget
RUN apt-get update && apt-get install -y wget && rm -rf var/lib/apt/lists/*

# install Chrome
RUN \
   echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/chrome.list && \
   wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
   apt-get update && \
   apt-get install -y xvfb google-chrome-stable jq && \
   ln -sf /usr/bin/xvfb-chrome /usr/bin/google-chrome

# set Chrome binary path
ENV CHROME_BIN usr/bin/google-chrome-stable
ENV SERVER_URL "http://192.168.0.136:8111"

# expose port for Chrome remout debugging
EXPOSE 9222

# set entrypoint to start TesmCity agent
ENTRYPOINT ["/run-services.sh"]
