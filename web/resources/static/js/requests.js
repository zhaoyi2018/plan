document.write('<script src="./jquery-3.5.1.min.js"></script>')

function request(url, type, data) {
    $.ajax({
      url: url,
      type: type,
      data: data,
      dataType: "json",
      success: function (data){
        return data;
      },
      error: function (msg){
        return msg;
      }
    });
}