document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll(".sidebar a");

    links.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();

            // Скройте все таблицы
            const tables = document.querySelectorAll(".table");
            tables.forEach(table => {
                table.style.display = "none";
            });

            // Определите ID таблицы, связанной с выбранной ссылкой
            const targetId = this.getAttribute("href").substr(1);
            const targetTable = document.getElementById(targetId);

            // Если таблица уже видима, скройте ее
            if (targetTable.style.display === "block") {
                targetTable.style.display = "none";
            } else {
                // Иначе, отобразите таблицу
                targetTable.style.display = "block";
            }
        });
    });
});