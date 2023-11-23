
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

document.addEventListener("DOMContentLoaded", function() {

    // Получаем ссылки на блоки по их идентификаторам
    const purchaseDataBlock = document.getElementById("purchaseDataBlock");
    const defenitionNMCKDataBlock = document.getElementById("defenitionNMCKDataBlock");

    // Получаем ссылку на кнопку "nxtButton"
    const nxtButton = document.getElementById("nxtButton");
    const prvButton = document.getElementById("prvButton");

    var queryCountDisplay = document.getElementById('queryCountDisplay');
var queryCountField = document.getElementById('queryCountField2');
var queryResponseDisplay = document.getElementById('ResponseCountDisplay');
var queryResponseField = document.getElementById('ResponseCountField2');
var TkpDisplay = document.getElementById('TKDadd');
var editQueryCountButton = document.getElementById('editQueryCountButton');
var additionallabels = document.querySelectorAll('.additional-label');
var additionalvalues = document.querySelectorAll('.additional-value');
var TKPCountFields = document.querySelectorAll('.TKPinput');
var NMCKMarket = document.getElementById('NMCKMarket');
var FinancingLimit = document.getElementById('FinancingLimit');
var NMCKMarketResponse = document.getElementById('ResponseNMCKMarket');

var FinancingLimitResponse = document.getElementById('ResponseFinancingLimit');
try {
document.getElementById("showAnalizForm").addEventListener("click", function() {
    window.location.href = "/analis/";
}); 
} catch (error) {
    console.error()
};
//     try {
//    nxtButton.addEventListener("click", function() {
//     try {
//         purchaseDataBlock.style.display = "none";
//         editQueryCountButton.style.display = "block";
//         defenitionNMCKDataBlock.style.display = "block";
//     } catch (error) {
//         console.error("An error occurred:", error);
//     }
    
// });
// } catch (error) {
//     console.error()};
//     try {

// prvButton.addEventListener("click", function() {
//     try {
//         editQueryCountButton.style.display = "none";
//         purchaseDataBlock.style.display = "block";
//         defenitionNMCKDataBlock.style.display = "none";
//     } catch (error) {
//         console.error("An error occurred:", error);
//     }
// });
// } catch (error) {
//     console.error()};

    try {
document.getElementById("nextButton").addEventListener("click", function() {
    try {
        window.location.href = document.getElementById("nextLink").getAttribute("href");
    } catch (error) {
        console.error("An error occurred:", error);
    }
});
} catch (error) {
    console.error()};

    try {
document.getElementById("previusButton").addEventListener("click", function() {
    try {
        window.location.href = document.getElementById("previusLink").getAttribute("href");
    } catch (error) {
        console.error("An error occurred:", error);
    }
});

} catch (error) {
    console.error()};

    try {
      editQueryCountButton.addEventListener('click', function () {

        if (queryCountField.style.display === 'none') {
            var additional_info = document.getElementById('additional-info');
            queryResponseDisplay.style.display = 'none';
            queryCountDisplay.style.display = 'none';
            NMCKMarketResponse.style.display = 'none';
            additional_info.style.display = 'none';
            queryCountField.style.display = 'block';
            FinancingLimitResponse.style.display = 'none';
            
            queryResponseField.style.display = 'block';
            TkpDisplay.style.display = 'block';
            NMCKMarket.style.display = 'block';
            FinancingLimit.style.display = 'block';
            
            for (var i = 0; i < additionallabels.length; i++) {
                additionallabels[i].style.display = 'none';
                additionalvalues[i].style.display = 'none';
                // TKPCountFields[i].style.display = 'block';
            }
             // Добавьте эту строку
            queryCountField.focus();
            editQueryCountButton.textContent = 'Сохранить';
        } else {
    
            queryCountDisplay.textContent = queryCountField.value;
            queryResponseDisplay.textContent = queryResponseField.value;
            NMCKMarketResponse.textContent =  NMCKMarket.value;
            FinancingLimitResponse.textContent = FinancingLimit.value;
            queryCountField.style.display = 'none';
            queryCountDisplay.style.display = 'block';
            queryResponseDisplay.style.display = 'block';
          
            NMCKMarket.style.display = 'none';
            FinancingLimit.style.display = 'none';
            queryResponseField.style.display = 'none';
            TkpDisplay.style.display = 'block';
            NMCKMarketResponse.style.display = 'block';
            FinancingLimitResponse.style.display = 'block';
            // additional_info.style.display = 'block';
  
            editQueryCountButton.textContent = 'Изменить';
            for (var i = 0; i < additionallabels.length; i++) {
                additionallabels[i].style.display = 'block';
                additionalvalues[i].style.display = 'block';
                TKPCountFields[i].style.display = 'none';
            }
            var tkpFieldsContainer = document.getElementById('tkpFieldsContainer');
            var tkpInputs = tkpFieldsContainer.querySelectorAll('.TKPinput');
        
            for (var i = 0; i < tkpInputs.length; i++) {
              tkpInputs[i].disabled = true;
            }
         
        }
    });
} catch (error) {
    console.error()};
    try {
    document.getElementById("showButtonForm").addEventListener("click", function() {
        try {
            window.location.href = "/upload_csv/";
        } catch (error) {
            console.error("An error occurred:", error);
        }
    });
} catch (error) {
    console.error()};
    try {
    document.getElementById("showUserProfiles").addEventListener("click", function() {
        try {
            window.location.href = "/view_users/";
        } catch (error) {
            console.error("An error occurred:", error);
        }
    });
} catch (error) {
    console.error()};
});
//функция добавление в модель данных
// $(function() {
//     $("#addPurchaseButton").click(function() {
//         $.ajax({
//             type: 'POST',
//             url: '/add_purchase/', 
//             data: $('#purchaseModal form').serialize(),  
//             success: function(data) {
//                 if (data.success) {
//                     $('#purchaseModal').modal('hide');  // Закрыть модальное окно
//                     location.reload();  // Обновить страницу или выполнить другие действия
//                     alert(data.message);  // Отобразить сообщение об успехе
//                 } else {
//                     alert('Ошибка при добавлении закупки: ' + data.errors);  // Отобразить сообщение об ошибке
//                 }
//             },
//             error: function() {
//                 alert('Ошибка при отправке формы');
//             }
//         });
//     });
// });



$(function() {
    // Открывать модальное окно при нажатии кнопки "Удалить закупку"
    $("#deletePurchaseButton").click(function(event) {
        event.preventDefault();
        var purchaseId = $(this).data("purchase-id"); // Получите Id закупки из атрибута data-purchase-id
      
        // Поместите Id в скрытое поле в модальном окне
        $("#purchaseIdField").val(purchaseId);

        $("#deletePurchaseModal").modal("show");
    });

    $("#confirmDeleteButton").click(function() {

        var purchaseId = $("#purchaseIdField").val();
        console.log(purchaseId);

        var csrfToken = getCookie('csrftoken');


        $.ajax({
            type: "POST",
            url: "/delete_purchase/" + purchaseId + "/",  // Замените на правильный URL
            data: {
                csrfmiddlewaretoken: csrfToken  // Добавьте CSRF токен в данные запроса
            },
            success: function(data) {
                // Здесь можно добавить обработку успешного удаления, например, перезагрузить страницу
                location.reload();
            },
            error: function() {
                alert("Ошибка при удалении закупки");
            }
        });

        // Закрыть модальное окно после удаления
        $("#deletePurchaseModal").modal("hide");
    });
    


    
});
// $(document).ready(function () {
//     $('#purchase_order').change(function (event) {
//         event.preventDefault(); // Предотвращаем автоматическую отправку формы
//         console.log("Purchase order changed");
//         // Отправка формы при выборе значения из выпадающего списка
//         $('form').submit();
//     });
// });

// $(document).ready(function () {
//     $('#customer_name').change(function () {
//         // Отправка формы при выборе значения из выпадающего списка
//         $('form').submit();
//     });
// });

// $(document).ready(function () {
//     $('#procurement_organization').change(function () {
//         // Отправка формы при выборе значения из выпадающего списка
//         $('form').submit();
//     });
// });



$(document).ready(function () {
    $('#procurement_organization').on('input', function () {
        var inputText = $(this).val().toLowerCase();
        $('#orgSuggestions option').each(function() {
            var optionValue = $(this).val().toLowerCase();
            if (optionValue.indexOf(inputText) === -1) {
                $(this).prop('disabled', true);
            } else {
                $(this).prop('disabled', false);
            }
        });
    });
});
$(document).ready(function () {
    $('#search_input').on('input', function () {
        var inputText = $(this).val().toLowerCase();
        $('#suggestions option').each(function() {
            var optionValue = $(this).val().toLowerCase();
            var category = $(this).data('category');
            if (optionValue.indexOf(inputText) === -1) {
                $(this).prop('disabled', true);
            } else {
                $(this).prop('disabled', false);
            }
        });
    });
});

// $(function() {
//     // Открывать модальное окно при нажатии кнопки "Открыть модальное окно"
//     $("#openModalButton").click(function(event) {
//         event.preventDefault();
//         var purchaseId = $("#purchaseIdField").val();
//         $("#addPurchaseModal").show();
//     });

//     // Закрыть модальное окно при нажатии на кнопку "Сохранить"
//     $("#saveDataButton").click(function(event) {
//         event.preventDefault();  // Предотвращение стандартного поведения кнопки
//         var purchaseId = $("#purchaseIdField").val();
//         var queryCount = $("#queryCountField").val();
//         var responseCount = $("#responseCountField").val();
//         var tkpValues = {}; // Объект для хранения значений TKP

//         var csrfToken = getCookie('csrftoken');


//         $("input[id^='tkp']").each(function() {
//             var tkpNumber = $(this).attr('id').match(/\d+/)[0];
//             var tkpValue = $(this).val();
//             tkpValues['tkp' + tkpNumber] = tkpValue;
//         });
//         // Отправьте данные на сервер Django с использованием AJAX
//         $.ajax({
//             url: "/save_data/" + purchaseId + "/",   // Замените на URL вашего представления Django
//             method: "POST",
//             data: {
//                 csrfmiddlewaretoken: csrfToken,
//                 purchaseId: purchaseId,  // Добавьте purchaseId
//                 queryCount: queryCount,
//                 responseCount: responseCount,
//                 tkpValues: JSON.stringify(tkpValues),

          
                
//             },
//             success: function(response) {
//                 // Обработка успешного ответа
//                 // Закрыть модальное окно
//                 $("#addPurchaseModal").hide();
//             },
//             error: function(error) {
//                 // Обработка ошибки
//             }
//         });
//     });
// });

// $(document).ready(function() {
//     var editQueryCountButton = $("#editQueryCountButton");

//     editQueryCountButton.click(function(event) {

//         if (editQueryCountButton.text() === 'Сохранить') {
       
//         var purchaseId = $("#purchaseIdField").val();
//         var queryCount = $("#queryCountField2").val(); // Обновленное поле ввода для QueryCount
//         var responseCount = $("#ResponseCountField2").val(); // Обновленное поле ввода для ResponseCount
//         var tkpValues = {}; // Объект для хранения значений TKP

//         var csrfToken = getCookie('csrftoken');

//         // Соберите значения TKP с полями ввода
//         $("input.TKPinput").each(function() {
//             var tkpValue = $(this).val();
//             tkpValues[$(this).attr('id')] = tkpValue;
//         });

//         // Отправьте данные на сервер Django с использованием AJAX
//         $.ajax({
//             url: "/save_data/" + purchaseId + "/",   // Замените на URL вашего представления Django
//             method: "POST",
//             data: {
//                 csrfmiddlewaretoken: csrfToken,
//                 purchaseId: purchaseId,
//                 queryCount: queryCount,
//                 responseCount: responseCount,
//                 tkpValues: JSON.stringify(tkpValues),
//             },
//             success: function(response) {

//                 $("#addPurchaseModal").hide();
//             },
//             error: function(error) {
//                 // Обработка ошибки
//             }
//         });}
//         else {
         
//         }
        
//     });
// });

$(function() {
    var isEditMode = false; // Флаг для отслеживания режима редактирования

    // Обработчик клика на кнопку "Изменить"/"Сохранить"
    $("#editQueryCountButton").click(function() {
        if (!isEditMode) {
            // Вход в режим редактирования
            isEditMode = true;
            editQueryCountButton.textContent = 'Сохранить';
            // Отобразить поля для редактирования
            $("#queryCountDisplay").hide();
            $("#queryCountField2").show();
        } else {
            // Выход из режима редактирования
            isEditMode = false;
            editQueryCountButton.textContent = 'Изменить';
            // Собрать данные для сохранения
            var purchaseId = $("#purchaseIdField").val();
            var queryCount = $("#queryCountField2").val();
            var responseCount = $("#ResponseCountField2").val();

            var NMCKMarket =  $("#NMCKMarket").val();
            var  FinancingLimit = $("#FinancingLimit").val();
            var tkpValues = {}; // Объект для хранения значений TKP

            $("input[id^='tkp']").each(function() {
                            var tkpNumber = $(this).attr('id').match(/\d+/)[0];
                            var tkpValue = $(this).val();
                            tkpValues['tkp' + tkpNumber] = tkpValue;
                        });
         

            // Отправить данные на сервер Django
            $.ajax({
                url: "/save_data/" + purchaseId + "/",   // Замените на URL вашего представления Django
                method: "POST",
                data: {
                    csrfmiddlewaretoken: getCookie('csrftoken'),
                    purchaseId: purchaseId,
                    queryCount: queryCount,
                    FinancingLimit:FinancingLimit,
                    NMCKMarket:NMCKMarket,
                    responseCount: responseCount,
                    tkpValues: JSON.stringify(tkpValues),
                },
                success: function(response) {
                    // Обработка успешного ответа
                },
                error: function(error) {
                    // Обработка ошибки
                }
            });
        }
    });
});

// $(document).ready(function() {
//     var tkpFieldCount = 0;

//     // Обработчик клика на кнопку "Добавить TKP"
//     $("#addTkpFieldButton").click(function() {
//         tkpFieldCount++;
 

//         var newTkpField = $('<input type="text" class="TKPinput">').attr({
//             id: 'tkp' + tkpFieldCount + 'Field',
//             style: 'display: block',
//             placeholder: 'Значение TKP' + tkpFieldCount
//         });

//         // Добавить новое поле ввода в контейнер
//         $("#tkpFieldsContainer").append(newTkpField);
//     });
// });
$(document).ready(function() {
    var tkpFieldCount = 0;

    // Обработчик ввода цифры в поле "#queryCountField2"
    $("#queryCountField2").on("input", function() {
        // Очистить контейнер перед добавлением новых полей
        $("#tkpFieldsContainer").empty();

        // Получить количество полей TKP, которое нужно добавить
        var count = parseInt($(this).val(), 10) || 0;

        // Добавить новые поля TKP в контейнер
        for (var i = 1; i <= count; i++) {
            var newTkpField = $('<input type="number" class="TKPinput">').attr({
                id: 'tkp' + i + 'Field',
                style: 'display: block',
                placeholder: 'Значение TKP' + i
            });

            $("#tkpFieldsContainer").append(newTkpField);
        }
    });
});
$(document).ready(function() {
    var tkpFieldCount = 0;

    // Обработчик ввода для основного поля TKP
    $("#tkpInput").on("input", function() {
        calculateAndDisplayStatistics();
    });
    function calculateStandardDeviation(values) {
        const n = values.length;
    
        // Среднее значение
        const mean = values.reduce((acc, value) => acc + value, 0) / n;
    
        // Сумма квадратов разностей от среднего значения
        const sumOfSquares = values.reduce((acc, value) => acc + Math.pow(value - mean, 2), 0);
    
        // Стандартное отклонение для выборки (с использованием исправления Bessel's correction)
        const standardDeviation = Math.sqrt(sumOfSquares / (n - 1));
    
        return standardDeviation;
    }
    // Функция для вычисления и отображения статистики
    function calculateAndDisplayStatistics() {
        var tkp_values_all = [];
        tkp_values_all.push(parseFloat($("#tkpInput").val()) || 0);

        $(".TKPinput").each(function() {
            tkp_values_all.push(parseFloat($(this).val()) || 0);
        });
        var nonZeroValues = tkp_values_all.filter(value => value !== 0 && !isNaN(value));
        // Вычислить статистику
        var max_tkp = Math.max(...tkp_values_all);

        var min_tkp = nonZeroValues.length > 0 ? Math.min(...nonZeroValues) : NaN;
        var avg_tkp = nonZeroValues.length > 0 ? nonZeroValues.reduce((a, b) => a + b) / nonZeroValues.length : 0;
        var standard_deviation = calculateStandardDeviation(nonZeroValues);
        var cv = (standard_deviation / avg_tkp) * 100;

        // Обновить соответствующие элементы DOM
        $("#averagePrice").text(avg_tkp.toFixed(2));
        $("#minPrice").text(min_tkp.toFixed(2));
        $("#maxPrice").text(max_tkp.toFixed(2));
        $("#standardDeviation").text(standard_deviation.toFixed(2));
        $("#coefficientOfVariation").text(cv.toFixed(2)+ " %");
        console.log(tkp_values_all);
     
    }

    // Обработчик ввода для динамически созданных полей TKP
    $(document).on("input", ".TKPinput", function() {
        calculateAndDisplayStatistics();
    });
});