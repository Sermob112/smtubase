
 // Функция для получения значения куки по имени
 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function showRoleOptions(userId) {
    const roleCell = $(`#user-roles-${userId}`);
        
    // Создание выпадающего списка
    const select = $('<select>')
    .append('<option value="Пользователь"> --  -- </option>')
    .append('<option value="Пользователь">Пользователь</option>')
    .append('<option value="Редактор">Редактор</option>')
    .append('<option value="Администратор">Администратор</option>')
    .on('change', function() {
        const newRole = $(this).val();

        const csrftoken = getCookie('csrftoken');

        $.ajax({
            url: `/update_user_role/${userId}/`,
            type: 'POST',
            data: { 
                role: newRole,
                csrfmiddlewaretoken: csrftoken,
            },
            success: function(response) {
                roleCell.html(response.updatedRoles);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

// Проверка, является ли ячейка текущим контейнером выпадающего списка
if (!roleCell.data('dropdown')) {
    roleCell
        .html(select)
        .data('dropdown', true);
}

    // Замена текущего текста ячейки выпадающим списком
    roleCell.innerHTML = '';
    roleCell.appendChild(select);
}


