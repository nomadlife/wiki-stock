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
                              label: 'random number',
                              data: defaultData,
                              fill: false,
                              lineTension: 0,
                              borderColor: 'rgba(255,99,132,1)',
                              // showLine: false,
                        }]
                  },
                  options: {
                        animation: false,
                        responsive: true,
                        legend: {
                              position: 'bottom',
                        },
                        hover: {
                              mode: 'label'
                        },
                        scales: {
                              xAxes: [{
                                    display: true,
                                    scaleLabel: {
                                          display: true,
                                          labelString: 'Alphabet'
                                    }
                              }],
                              yAxes: [{
                                    display: true,
                                    ticks: {
                                          beginAtZero: true,
                                          steps: 10,
                                          stepValue: 5,
                                          max: 500
                                    }
                              }]
                        },
                        title: {
                              display: true,
                              text: 'sample chartd'
                        },
                  }
            })
      }