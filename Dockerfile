# * @author        nobi Aris M <jaisinghmitrc+bot@gmail.com>
# * @date          2022-12-01 09:12:27
# * @projectName   NobitaXRobot
# * Copyright ©Nobi-Pro All rights reserved

# Base Docker Using Debian 12 (Bookworm), Python 3.11.6 and Built In Pip
## With Built in Pip Package
FROM jaisingh007/nobita-docker:ubuntu23.10
## Without Built in Pip Package
# FROM jaisingh007/nobita-docker:free

# Set Hostname
ENV HOSTNAME nobi-server
# Copy Files
COPY . .
# Instal pip package
# RUN pip3 install --no-cache-dir -r requirements.txt
# Set CMD Bot
CMD ["bash", "start.sh"]
