## [카카오 API key 발급받기](https://kadosholy.tistory.com/25)
## [kakao vision-api](https://vision-api.kakao.com/)
## [kakao ocr](https://developers.kakao.com/docs/latest/ko/vision/dev-guide#ocr)


import json

import cv2
import requests
import sys

LIMIT_PX = 1024
LIMIT_BYTE = 1024*1024  # 1MB
LIMIT_BOX = 40


def kakao_ocr_resize(image_path: str):
    """
    ocr detect/recognize api helper
    ocr api의 제약사항이 넘어서는 이미지는 요청 이전에 전처리가 필요.

    pixel 제약사항 초과: resize
    용량 제약사항 초과  : 다른 포맷으로 압축, 이미지 분할 등의 처리 필요. (예제에서 제공하지 않음)

    :param image_path: 이미지파일 경로
    :return:
    """
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    if LIMIT_PX < height or LIMIT_PX < width:
        ratio = float(LIMIT_PX) / max(height, width)
        image = cv2.resize(image, None, fx=ratio, fy=ratio)
        height, width, _ = height, width, _ = image.shape

        # api 사용전에 이미지가 resize된 경우, recognize시 resize된 결과를 사용해야함.
        image_path = "{}_resized.jpg".format(image_path)
        cv2.imwrite(image_path, image)

        return image_path
    return None


def kakao_ocr(image_path: str, appkey: str):
    """
    OCR api request example
    :param image_path: 이미지파일 경로
    :param appkey: 카카오 앱 REST API 키
    """
    API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'

    headers = {'Authorization': 'KakaoAK {}'.format(appkey)}

    image = cv2.imread(image_path)
    jpeg_image = cv2.imencode(".jpg", image)[1]
    data = jpeg_image.tobytes()


    return requests.post(API_URL, headers=headers, files={"image": data})


def main():
    if len(sys.argv) != 3:
        print("Please run with args: $ python example.py /path/to/image appkey")
    image_path, appkey = sys.argv[1], sys.argv[2]

    resize_impath = kakao_ocr_resize(image_path)
    if resize_impath is not None:
        image_path = resize_impath
        print("원본 대신 리사이즈된 이미지를 사용합니다.")

    output = kakao_ocr(image_path, appkey).json()
    print("[OCR] output:\n{}\n".format(json.dumps(output, sort_keys=True, indent=2)))



# import sys
# import requests

# API_URL = 'https://dapi.kakao.com/v2/vision/text/ocr'
# RESTAPI_KEY = '1에서 복사한 REST API 키 복사'

# def get_ocr_result(filename):
#     headers = {
#         "Authorization": "KakaoAK " + RESTAPI_KEY
#     }

#     try:
#         files = { 'image' : open(filename, 'rb')}
#         resp = requests.post(API_URL, headers=headers, files=files)
#         print(f"status_code = {resp.status_code}")
#         return resp.json()
#     except Exception as e:
#         print(str(e))
#         sys.exit(0)

# if __name__ == "__main__":
#         filename = "text1.jpg"

#         detect_result = get_ocr_result(filename)

#         for kk in detect_result['result']:
#             print(f"{kk['recognition_words'][0]} ", end='')



if __name__ == "__main__":
    main()