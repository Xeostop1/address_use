$(document).ready(function () {
  let fetchedAddresses = [];
  let previousInput = "";
  let timeoutId = null;

  const MIN_INPUT_LENGTH = 6; // 최소 입력 길이 설정
  const DELAY_TIME_MS = 5000; // 딜레이 시간 설정 (1초)

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

  const updateView = (data) => {
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
