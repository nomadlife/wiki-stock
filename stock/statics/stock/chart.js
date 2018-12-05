var datatemp = "{{ customers }}" * 134
      var defaultData = []
      var labels = []

      $.ajax({
            type: "GET",
            url: "/stock/api/chart/data",
            success: function (data) {
                  console.log(data);

                  labels = data.labels
                  defaultData = data.default
                  setChart()

            },
            error: function (error_data) {
                  console.log("error")
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
                        responsive: true,
                        legend: {
                              position: 'top',
                        },
                        hover: {
                              mode: 'label'
                        },
                        title: {
                              display: true,
                              text: 'sample chart, 008500.KS 일정실업'
                        },
                  }
            })
      }