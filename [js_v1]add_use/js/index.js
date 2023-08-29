$(document).ready(function () {
  let fetchedAddresses = [];
  let previousInput = "";
  let timeoutId = null;
  const MIN_INPUT_LENGTH = 2; // 최소 입력 길이 설정
  const DELAY_TIME_MS = 1000; // 딜레이 시간 설정(5초)

  let apiKey = "138657344596766144"; // 직접 api 키를 변수로 선언.

  const getAddressData = function (input) {
    console.log("주소 데이터를 요청합니다: ", input);
    return $.ajax({
      url: `https://us-autocomplete-pro.api.smarty.com/look/up?search=${input}&max_results=10&key=${apiKey}`,
      method: "GET",
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

    data.suggestions.forEach(function (address) {
      const street_line_1 = address.street_line;
      const secondary_1 = address.secondary;
      const city_1 = address.city;
      const state_1 = address.state;
      const zipcode_1 = address.zipcode;

      let addressItem = $("<li>")
        .text(`${street_line_1}, ${secondary_1}, ${city_1}, ${state_1}`)
        .click(function () {
          $("#zipcode").val(zipcode_1);
          $("#street").val(street_line_1);
          console.log(
            `${street_line_1}, ${secondary_1}, ${city_1}, ${state_1}`
          );
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
          console.log(data);
          if (data.error) {
            console.log(data);
            updateView(data);
            return;
          }

          fetchedAddresses[0] = data;
          previousInput = inputValue;

          updateView(fetchedAddresses[0]);
        })
        .fail(function (jqXHR, textStatus, errorThrown) {
          console.error("API 호출에 실패했습니다.", errorThrown);
        });
    }, DELAY_TIME_MS);
  });
});
