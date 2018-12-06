var ticker = "{{ticker}}"
var customers = '{{customers}}'
var defaultData = []
var labels = []

$.ajax({
      type: "GET",
      url: "{% url 'api-chart-data' ticker=ticker %}",
      success: function (data) {
            console.log("success")
            labels = data.labels
            defaultData = data.values
            setChart()
      },
      error: function (error_data) {
            console.log("error")
            console.log('url:', url)
            console.log(error_data)
      }
});

function setChart() {
      var ctx = document.getElementById("myChart");
      var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                  labels: labels,
                  datasets: [{
                        label: '종가',
                        data: defaultData,
                        fill: false,
                        lineTension: 0,
                        borderColor: 'rgba(255,99,132,1)',
                        borderWidth: 1,
                        // showLine: false,
                        pointRadius: 1,
                        // pointBackgroundColor: [],
                        // pointBorderColor: [],
                  }]
            },
            options: {
                  animation: false,
                  responsive: false,
                  // maintainAspectRatio: true,
                  legend: {
                        display: false,
                        position: 'top',
                  },
                  hover: {
                        mode: 'label'
                  },
                  title: {
                        display: true,
                        text: "{{ data.1 }} : {{ ticker }}"
                  },
            }
      })
}