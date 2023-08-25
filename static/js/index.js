$(document).ready(function () {
  // 주소 데이터 저장
  let fetchedAddresses = [];
  // 이전 사용자 입력값 저장
  let previousInput = "";

  // 타임아웃 ID 저장
  let timeoutId = null;

  // 주소 데이터 요청 함수
  const getAddressData = function (input) {
    console.log("주소 데이터를 요청합니다: ", input);
    return $.ajax({
      url: "/search_address",
      method: "GET",
      dataType: "json",
      data: { query: input },
    }).done(function () {
      console.log("주소 데이터 요청이 완료되었습니다.");
    });
  };

  // 화면 업데이트 함수
  const updateView = (data) => {
    console.log("화면을 업데이트합니다.");

    $("#suggested-addresses-list").empty();

    if (data.error) {
      $("#suggested-addresses-list").append(`<li>${data.error}</li>`);
      return;
    }

    data.forEach(function (address) {
      const street = address.street;
      const city = address.city;
      const state = address.state;
      const zipcode = address.zipcode;

      let addressItem = $("<li>")
        .text(`${street} ${city} ${state} (${zipcode})`)
        .click(function () {
          $("#zipcode").val(zipcode);
          $("#street").val(`${street} ${city} ${state}`);
          console.log(`${street} ${city} ${state} (${zipcode})`);
        });

      $("#suggested-addresses-list").append(addressItem);
    });
  };

  $("#street").on("input", function () {
    clearTimeout(timeoutId);

    let inputValue = $(this).val().trim();

    console.log(`사용자 입력 처리 - '${inputValue}'`);

    if (!inputValue) {
      $("#suggested-addresses-list").empty();
      return;
    }

    getAddressData(inputValue)
      .done(function (data) {
        if (!Array.isArray(data)) {
          if (data.error) {
            updateView(data);
          } else {
            console.error("API 응답 오류: 주소 데이터 배열이 아닙니다.", data);
          }

          return;
        }

        fetchedAddresses = data;
        previousInput = inputValue;

        let inputWords = inputValue.toLowerCase().split(" ");

        let filteredAddresses = fetchedAddresses.filter((address) => {
          let addressString =
            `${address.street}${address.city}${address.state}`.toLowerCase();

          // 정규 표현식 생성
          let regexPattern = new RegExp(inputWords.join(".*"), "i");

          // match() 메서드를 이용해 매칭되는 주소 찾기
          return addressString.match(regexPattern);
        });

        updateView(filteredAddresses);
      })
      .fail(function (jqXHR, textStatus, errorThrown) {
        console.log("API 호출에 실패했습니다.", errorThrown);
      });

    timeoutId = setTimeout(() => {
      console.log("입력 대기중...");
    }, 100);
  });
});
