# Variables
IMAGE_NAME := my_model_image

all: build run

build:
	@docker build -t $(IMAGE_NAME) .

run:
	@docker run $(IMAGE_NAME)

clean:
	@docker image rm $(IMAGE_NAME)
