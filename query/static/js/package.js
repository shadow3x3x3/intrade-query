$(function() {
  $("#add-new-form").on("submit", function(event) {
    event.preventDefault();
    createNewId();
  });

  function createNewId() {
    var package_info = {
        query_id: $("#queryIdInput").val(),
        blackcat_id: $("#blackcatIdInput").val(),
        chinese_id: $("#chineseIdInput").val()
    }
    $.ajax({
      url: "/packages",
      type: "POST",
      datatype: "json",
      data: package_info,
      success: function(id_json) {
        if(id_json.query_id != "NOEXIST") {
          insertTable(id_json)
        }
      },
      error: function(xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText)
      }
    });
  }

  function insertTable(id_json) {
    var table = document.getElementById("packages-list");
    var row = table.insertRow(1);
    var cell0 = row.insertCell(0);
    var cell1 = row.insertCell(1);
    var cell2 = row.insertCell(2);
    cell0.innerHTML = id_json.query_id;
    cell1.innerHTML = id_json.blackcat_id + ": None at None";
    cell2.innerHTML = id_json.chinese_id + ": None at None";
  }

  // for django csrf token
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });
});