
SHELL = /bin/bash

package:
	docker build --tag bench:latest .
	docker run --name bench --volume $(shell pwd)/:/local -itd bench:latest bash
	docker cp bench:/tmp/package.zip package.zip
	docker stop bench
	docker rm bench
