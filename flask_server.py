from flask import Flask, request, Response
import pytesseract
import requests
import json
import cv2
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/process-ocr', methods=['POST'])
def process_ocr():
    try:
        # JSON 데이터 가져오기
        data = request.get_json()
        if not data or 'imageUrl' not in data:
            return Response(json.dumps({'error': 'Invalid JSON data or imageUrl not provided'}, ensure_ascii=False), status=400, mimetype='application/json')

        image_url = data['imageUrl']

        # URL에서 이미지 가져오기
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))

        # OCR 처리
        config = '-l kor+eng --oem 3 --psm 6'
        text = pytesseract.image_to_string(image, config=config)

        # OCR 결과 반환 (ensure_ascii=False 설정)
        response_data = json.dumps({'text': text}, ensure_ascii=False)
        return Response(response_data, status=200, mimetype='application/json')

    except Exception as e:
        error_data = json.dumps({'error': str(e)}, ensure_ascii=False)
        return Response(error_data, status=500, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)