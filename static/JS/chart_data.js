var temperature = document.getElementById('temperature');
var temp_chart = new Chart(temperature, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(244, 67, 54, 0.1)',
            borderColor:'rgba(244, 67, 54, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


var humidity = document.getElementById('humidity');
var humid_chart = new Chart(humidity, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Humidity W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(33, 150, 243, 0.1)',
            borderColor:'rgba(33, 150, 243, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var moisture = document.getElementById('moisture');
var moist_chart = new Chart(moisture, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Moisture W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(0, 150, 136, 0.1)',
            borderColor:'rgba(0, 150, 136, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


var light = document.getElementById('light');
var light_chart = new Chart(light, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Light W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(255, 152, 0, 0.1)',
            borderColor:'rgba(255, 152, 0, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.shift();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
    });
    chart.update();
}

var couter = 0;   
function requestTemp() {
    var requests = $.get('/api/kuchnhi/temperature');
    var tm = requests.done(function (result){
        
        addData(temp_chart, result[0], result[1]);
        if (couter >= 10) {
            removeData(temp_chart);
        }
        couter++;
        
        document.getElementById("card-temp").innerHTML = result[1];
        
         setTimeout(requestTemp, 2000);
        setTimeout(requestHumidity, 2000);
        setTimeout(requestMoisture, 2000);
        setTimeout(requestLight, 2000);
    });
}

function requestHumidity() {
    var requests = $.get('/api/kuchnhi/moisture');
    var tm = requests.done(function (result){
        addData(humid_chart, result[0], result[1]);
        if (couter >= 11) {
            removeData(humid_chart);
        }
        
        document.getElementById("card-moisture").innerHTML = result[1];

    });
}


function requestMoisture() {
    var requests = $.get('/api/kuchnhi/humidity');
    var tm = requests.done(function (result){
        addData(moist_chart, result[0], result[1]);
        if (couter >= 11) {
            removeData(moist_chart);
        }
        
        document.getElementById("card-humidity").innerHTML = result[1];

    });
}


function requestLight() {
    var requests = $.get('/api/kuchnhi/light');
    var tm = requests.done(function (result){
        addData(light_chart, result[0], result[1]);
        if (couter >= 11) {
            removeData(light_chart);
        }
        
        document.getElementById("card-light").innerHTML = result[1];

    });
}

requestTemp();

var apikey = document.getElementById('apikey').value ;