from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

# 로그 설정
logging.basicConfig(level=logging.INFO)


def build_address(suggestion):
    white_space = ""
    if suggestion.get("secondary"):
        if suggestion.get("entries", 0) > 1:
            suggestion["secondary"] += f" ({suggestion['entries']} entries)"
        white_space = " "
    return f"{suggestion['street_line']}{white_space}{suggestion['secondary']} {suggestion['city']}, {suggestion['state']} {suggestion['zipcode']}"


@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    try:
        # SmartyStreets API 키 (환경 변수 또는 직접 문자열로 입력) dl
        api_key = "138657343210935212"

        # 클라이언트에서 받은 검색어
        search_term = request.args.get("search", "")

        # 선택적 파라미터들. 필요에 따라 추가 가능.
        max_results = request.args.get("max_results", "10")

        # 기타 필요한 매개변수들을 여기에 추가하세요.
        api_url = f"https://us-autocomplete-pro.api.smarty.com/lookup?search={search_term}&max_results={max_results}&key={api_key}"

        response = requests.get(api_url)

        if response.status_code != 200:
            logging.error("API 요청에 실패했습니다.")
            return jsonify({"error": "API 요청에 실패했습니다."}), 500

        data = response.json()

        for suggestion in data["suggestions"]:
            address = build_address(suggestion)
            print(address)

        return jsonify(data)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500


if __name__ == "__main__":
    app.run(debug=True)
