find bbox/Bbox* -maxdepth 1 -mindepth 1 -exec mv -t bbox/ {} + && mkdir bbox/xml && mkdir bbox/labels && mv bbox/*.xml bbox/xml/ && rm -r bbox/Bbox*
