$(document).ready(function () {
  let fetchedAddresses = [];
  let timeoutId = null;

  // 화면 초기화 함수
  const resetView = () => {
    console.log("화면 초기화");
    $("#suggested-addresses-list").empty();
    $("#zipcode").val("");
  };

  // 주소 데이터 요청 함수
  const getAddressData = function (input) {
    console.log("주소 데이터 요청");
    return new Promise((resolve, reject) => {
      $.ajax({
        url: "/search_address",
        method: "POST",
        dataType: "json",
        data: { query: input },
        success: resolve,
        error: reject,
      });
    });
  };

  // 화면 업데이트 함수
  const updateView = (data) => {
    console.log("화면 업데이트");
    if (data.error) {
      console.log("검색 결과가 없습니다.");
      $("#suggested-addresses-list").empty().append(`<li>${data.error}</li>`);
      return;
    }

    //json꼭 살펴보기!
    console.log("검색된 주소 출력");
    data.forEach(function (address, index) {
      const deliveryLine = address.delivery_line_1;
      const lastLine = address.last_line;
      const zipcode = address.zipcode;
      const addressItem = $(
        `<li>${deliveryLine}, ${lastLine} (${zipcode})</li>`
      );

      console.log(`주소 항목 생성 - ${deliveryLine}, ${lastLine} (${zipcode})`);
      addressItem.on("click", function () {
        console.log(`주소 선택 - ${deliveryLine}, ${lastLine} (${zipcode})`);
        $("#zipcode").val(zipcode);
      });

      $("#suggested-addresses-list").append(addressItem);
    });
  };

  // 주소 입력 이벤트 처리
  $("#street").on("input", async function () {
    clearTimeout(timeoutId);

    const inputValue = $(this).val().trim();
    if (!inputValue) {
      resetView();
      return;
    }

    // 주소 검색 지연 처리 1초
    timeoutId = setTimeout(async () => {
      try {
        resetView();
        const data = await getAddressData(inputValue);
        fetchedAddresses = data;
        updateView(data);
      } catch (error) {
        console.log("API 호출에 실패했습니다.", error);
      }
    }, 1000);
  });
});
