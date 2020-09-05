from flask import Blueprint, Response, request, jsonify
from backend import image_code_dict
from lib.captcha.captcha import captcha

verification_bp = Blueprint("verifications", __name__)


# 验证验证码图片
@verification_bp.route("/imagecodes/<string:image_code_id>/", methods=["GET"])
def verifications_image(image_code_id):
    yanzhengma, image = captcha.generate_captcha()

    image_code_dict[image_code_id] = yanzhengma

    response = Response(image, mimetype="image/jpeg")

    return response


# 验证验证码数字(是否一样)
@verification_bp.route("/digital/<string:mobile>/", methods=["GET"])
def verifications_digital(mobile):
    text = request.arges.get("text")
    image_code_id = request.arges.get("image_code_id")
    date = {
        "code": 200,
        "msg": "success"
    }
    if text == image_code_dict["image_code_id"]:
        date = {
            "code": 200,
            "msg": "success"
        }
    else:
        date = {
            "code": 200,
            "error_msg": "not success"
        }
        return jsonify(date)

