from flask import Flask, render_template, request, jsonify
import os
import json
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


# 인덱스 페이지를 렌더링
@app.route("/")
def index():
    return render_template("index.html")


# 미국 주소를 검색하여 결과를 반환
@app.route("/search_address", methods=["GET"])
def search_address_usa():
    logging.info("주소 검색 요청을 처리 중입니다.")
    query = request.args.get("query")

    # 주소 데이터 파일 요청
    with open("./static/address_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 검색어가 없으면 기본적으로 모든 주소를 반환
    if not query:
        logging.info("주소 검색 결과를 반환")
        return jsonify(data)

    # 키워드를 기반으로 주소 데이터에서 필터링→ 실제데이터값 변경
    filtered_data = [
        address
        for address in data
        if query.lower() in address["street"].lower()
        or query.lower() in address["city"].lower()
        or query.lower() in address["state"].lower()
    ]

    if not filtered_data:
        logging.info("검색 결과가 없습니다.")
        return jsonify({"error": "검색 결과가 없습니다."})

    logging.info("주소 검색 결과를 반환합니다.")
    return jsonify(filtered_data)


if __name__ == "__main__":
    app.run(debug=True)
