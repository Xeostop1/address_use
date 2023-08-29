$(document).ready(function () {
  let fetchedAddresses = [];
  let previousInput = "";
  let timeoutId = null;
  const MIN_INPUT_LENGTH = 3; // 최소 입력 길이 설정
  const DELAY_TIME_MS = 5000; // 딜레이 시간 설정(5초)

  let apiKey = "138657343210935212"; // 직접 api 키를 변수로 선언.

  const getAddressData = function (input) {
    console.log("주소 데이터를 요청합니다: ", input);
    return $.ajax({
      // url: `https://us-autocomplete-pro.api.smarty.com/lookup?search=${input}&max_results=10&key=${apiKey}`,
      url: `https://add-use.s3.ap-northeast-2.amazonaws.com/add_use/index.html/lookup?search=${input}&max_results=10&key=${apiKey}`,
      method: "GET",
    }).done(function () {
      console.log("주소 데이터 요청이 완료되었습니다.");
      console.log(url);
    });
  };

  const updateView = (data) => {
    $("#suggested-addresses-list").empty();

    if (data.error) {
      $("#suggested-addresses-list").append(`<li>${data.error}</li>`);

      return;
    }

    data.forEach(function (address) {
      const delivery_line_1 = address.delivery_line_1;
      const last_line = address.last_line;
      const zipcode = address.components.zipcode;

      let addressItem = $("<li>")
        .text(`${delivery_line_1}, ${last_line}`)
        .click(function () {
          $("#zipcode").val(zipcode);
          $("#street").val(delivery_line_1);
          console.log(`${delivery_line_1}, ${last_line}`);
        });

      $("#suggested-addresses-list").append(addressItem);
    });
  };

  $("#street").on("input", function () {
    clearTimeout(timeoutId);

    let inputValue = $(this).val().trim();

    console.log(`사용자 입력 처리 - '${inputValue}'`);

    if (!inputValue || inputValue.length < MIN_INPUT_LENGTH) {
      $("#suggested-addresses-list").empty();
      return;
    }

    timeoutId = setTimeout(() => {
      getAddressData(inputValue)
        .done(function (data) {
          if (!Array.isArray(data)) {
            if (data.error) {
              updateView(data);
            } else {
              console.error(
                "API 응답 오류 : 주소 데이터 배열이 아닙니다.",
                data
              );
            }

            return;
          }

          fetchedAddresses = data;
          previousInput = inputValue;
          let inputWordsSet = new Set(inputValue.toLowerCase().split(/\s+/));
          console.log(`입력 단어 :${[...inputWordsSet]}`);
          let filteredAddresses = fetchedAddresses.filter((address) => {
            let addressWordsSet = new Set(
              `${address.street}
                     ${address.city}
                     ${address.state}`
                .toLowerCase()
                .split(/\s+/)
            );

            // Check that every word in the input is present in the
            // set of words from the current address.
            return [...inputWordsSet].every((word) =>
              addressWordsSet.has(word)
            );
          });
          updateView(filteredAddresses);
        })
        .fail(function (jqXHR, textStatus, errorThrown) {
          console.error("API 호출에 실패했습니다.", errorThrown);
        });
    }, DELAY_TIME_MS);
  });
});
