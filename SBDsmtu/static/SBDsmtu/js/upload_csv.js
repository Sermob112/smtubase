


// $(document).on('click', 'button[type="submit"]', function() {
//     var deleteRecordsUrl = $(this).data('url');
//     var recordIds = $('input[name="record_ids"]:checked').map(function() {
//         return $(this).val();
//     }).get();

//     // Получаем CSRF-токен из cookie
//     var csrftoken = getCookie('csrftoken');

//     // Отправляем данные формы с использованием AJAX
//     $.ajax({
//         url: deleteRecordsUrl,
//         type: 'POST',
//         data: {
//             csrfmiddlewaretoken: csrftoken, // Вручную добавляем CSRF-токен
//             record_ids: recordIds
//         },
//         dataType: 'json',
//         success: function(response) {
//             if (response.success) {
//                 // Отображаем модальное окно Bootstrap с сообщением
//                 $('#successModalMessage').text(response.message);
//                 $('#successModal').modal('show');
//             } else {
//                 $('#errorModal').modal('show');
//                 $('#errorMessage').text(response.message);
//             }
//         },
//         error: function() {
//             alert('Произошла ошибка при отправке запроса');
//         }
//     });
    
//     // Предотвращаем отправку формы и перенаправление
//     return false;
// });

// // Функция для получения CSRF-токена из cookie
// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = jQuery.trim(cookies[i]);
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }

$(document).ready(function(){
  // Функция для отображения модального окна
  function showModal(message, isSuccess) {
      $('#modalMessage').text(message);
      $('#modal').modal('show');
      if (isSuccess) {
          $('#modal').addClass('modal-success');
      } else {
          $('#modal').removeClass('modal-success');
      }
  }

  // Обработчик успешного ответа от сервера
  function handleSuccess(response) {
    if (response.success) {
        showModal(response.message, true);

        setTimeout(function () {
          location.reload();
      }, 3000);
    } else {
        showModal(response.errors, false);
    }
}


  // Обработчик ошибки от сервера
  function handleError(response) {
    showModal(response.errors, false);
}
  // Отправка формы с использованием AJAX
  $('form').submit(function(e) {
      e.preventDefault();

      $.ajax({
          type: 'POST',
          url: '/upload_csv/',
          data: new FormData(this),
          processData: false,
          contentType: false,
          success: handleSuccess,
          error: handleError
      });
  });
});

  // // Отправка формы с данными на удаление
  // $('form').on('submit', function (event) {
  //   event.preventDefault(); // Предотвращаем отправку формы по умолчанию
  //   var form = $(this);
  //   var formData = form.serialize();
  //   var url = form.attr('action');
    
  //   $.post(url, formData, handleResponse);
  // });




  // function handleResponse(response) {
  //   if (response.success) {
  //     $('#successModalMessage').text(response.message);
  //     $('#successModal').modal('show');
  //   } else {
  //     $('#errorMessage').text(response.message);
  //     $('#errorModal').modal('show');
  //   }
  // }

$(document).ready(function () {
  $('#deleteRecordsButton').click(function () {
    var form = $('#deleteRecordsForm');
    var formData = form.serialize();
    $.post("/delete_selected_records/", formData, function (data) {
      if (data.success) {
        $('#successModalMessage').text(data.message);
        $('#successModal').modal('show');
        setTimeout(function () {
          location.reload();
      }, 2000);
      } else {
        $('#errorMessage').text(data.message);
        $('#errorModal').modal('show');
      }
    });
  });
});