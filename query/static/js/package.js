$(function() {
  $("#add-new-form").on("submit", function(event) {
    event.preventDefault();
    createNewId();
  });

  function createNewId() {
    var newId = $("#queryIdInput").val();
    $.ajax({
      url: "/packages",
      type: "POST",
      data: {'query_id': newId},
      success: function(json) {
        insertTable(json.packages)
      },
      error: function(xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText)
      }
    });
  }

  function insertTable(id) {
    var table = document.getElementById("packages-list");
    var row = table.insertRow(1);
    var cell = row.insertCell(0);
    cell.innerHTML = id;
  }

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