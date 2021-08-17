BUILD_FOLDER=build

build-lambda-layer: clean-up
		mkdir -p $(BUILD_FOLDER)/python
		python3 -m pip install -r requirements.txt -t $(BUILD_FOLDER)/python/
		cd $(BUILD_FOLDER) ; zip -9qr lambda_fastapi_layer.zip ./*

clean-up:
		rm -rf $(BUILD_FOLDER)