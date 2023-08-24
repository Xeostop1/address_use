from flask import Flask, render_template, request, jsonify
import os
from smartystreets_python_sdk import (
    SharedCredentials,
    StaticCredentials,
    exceptions,
    ClientBuilder,
)
from smartystreets_python_sdk.us_street import Lookup as StreetLookup
from smartystreets_python_sdk.us_street.match_type import MatchType
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


# 인덱스 페이지를 렌더링
@app.route("/")
def index():
    return render_template("index.html")


# 미국 주소를 검색하여 결과를 반환
@app.route("/search_address", methods=["POST"])
def search_address_usa():
    logging.info("주소 검색 요청을 처리 중입니다.")
    query = request.form.get("query")
    key = "138657344295845235"
    hostname = "bak2.gvg.co.kr"
    credentials = SharedCredentials(key, hostname)
    client = (
        ClientBuilder(credentials)
        .with_licenses(["us-core-cloud"])
        .build_us_street_api_client()
    )

    # 주소 조회 설정
    lookup = StreetLookup()
    lookup.street = query
    lookup.candidates = 5  # 리스트수
    lookup.match = MatchType.INVALID

    # SmartyStreets API를 호출하고 예외 처리
    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        logging.error("API 호출에 실패했습니다: %s", err)
        return jsonify({"error": "API 호출에 실패했습니다."})

    # 주소 데이터 정리
    result = lookup.result

    if not result:
        logging.info("검색 결과가 없습니다.")
        return jsonify({"error": "검색 결과가 없습니다."})

    address_data = []

    for candidate in result:
        address_data.append(
            {
                "delivery_line_1": candidate.delivery_line_1,
                "last_line": candidate.last_line,
                "zipcode": candidate.components.zipcode,
            }
        )

    logging.info("주소 검색 결과를 반환합니다.")
    return jsonify(address_data)


if __name__ == "__main__":
    app.run(debug=True)
