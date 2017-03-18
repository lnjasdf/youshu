docker run -v $(pwd):/runtime/app --name youshu -d --link some-mysql:mysql my/scrapy /bin/ash run.sh
