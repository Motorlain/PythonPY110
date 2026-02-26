from django.http import HttpResponse
from datetime import datetime


def datetime_view(request):
    if request.method == "GET":
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(current_time)


def dynamic_datetime_view(request):
    if request.method == "GET":
        data = """
        <script>
            function updateTime() {
                fetch("/datetime/")
                    .then(response => response.text())
                    .then(time => {
                        document.getElementById("time").innerText = time;
                    })
                    .catch(error => console.error("Ошибка загрузки:", error));
            }

            setInterval(updateTime, 1000);
            window.onload = updateTime;
        </script>
        <body>
            <h1>Текущее время:</h1>
            <p id="time">Загрузка...</p>
        </body>
        """
        return HttpResponse(data)