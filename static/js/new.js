
function start_request(){
        let Stock = document.body.getElementsByClassName('stock-name');
        Stock[0].innerHTML = '안녕하세요';
        Stock[1].innerHTML = '안녕하세요';
        Stock[2].innerHTML = '안녕하세요';
}

function requestChart(name) {
  const xhttp = new XMLHttpRequest();
    //Insert stock name
    let stockName = document.getElementsByClassName('stock-name');
    stockName[0].innerHTML = '안녕';
    stockName[1].innerHTML = name;
    stockName[2].innerHTML = name;

  xhttp.onload = function () {
    // Parse data
    let responseData = JSON.parse(this.responseText);



    // Insert yahoo link
    let stockLink = document.getElementById('stock-link');
    console.log(document.getElementById('stock-link'));
    stockLink.href = 'https://finance.yahoo.com/' + name

    // Show chart 
    var ctx = document.getElementById("myAreaChart");
    var myLineChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: responseData.labels,
        datasets: [{
          label: "Earnings",
          lineTension: 0.3,
          backgroundColor: "rgba(78, 115, 223, 0.05)",
          borderColor: "rgba(78, 115, 223, 1)",
          pointRadius: 3,
          pointBackgroundColor: "rgba(78, 115, 223, 1)",
          pointBorderColor: "rgba(78, 115, 223, 1)",
          pointHoverRadius: 3,
          pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
          pointHoverBorderColor: "rgba(78, 115, 223, 1)",
          pointHitRadius: 10,
          pointBorderWidth: 2,
          data: responseData.data,
        }],
      },
      options: {
        maintainAspectRatio: false,
        layout: {
          padding: {
            left: 10,
            right: 25,
            top: 25,
            bottom: 0
          }
        },
        scales: {
          xAxes: [{
            time: {
              unit: 'date'
            },
            gridLines: {
              display: false,
              drawBorder: false
            },
            ticks: {
              maxTicksLimit: 7
            }
          }],
          yAxes: [{
            ticks: {
              maxTicksLimit: 5,
              padding: 10,
              // Include a dollar sign in the ticks
              callback: function (value, index, values) {
                return '$' + number_format(value);
              }
            },
            gridLines: {
              color: "rgb(234, 236, 244)",
              zeroLineColor: "rgb(234, 236, 244)",
              drawBorder: false,
              borderDash: [2],
              zeroLineBorderDash: [2]
            }
          }],
        },
        legend: {
          display: false
        },
        tooltips: {
          backgroundColor: "rgb(255,255,255)",
          bodyFontColor: "#858796",
          titleMarginBottom: 10,
          titleFontColor: '#6e707e',
          titleFontSize: 14,
          borderColor: '#dddfeb',
          borderWidth: 1,
          xPadding: 15,
          yPadding: 15,
          displayColors: false,
          intersect: false,
          mode: 'index',
          caretPadding: 10,
          callbacks: {
            label: function (tooltipItem, chart) {
              var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
              return datasetLabel + ': $' + number_format(tooltipItem.yLabel);
            }
          }
        }
      }
    });
  }
  xhttp.open("GET", "/stock/getdata?name=" + name, true);
  xhttp.send();
}