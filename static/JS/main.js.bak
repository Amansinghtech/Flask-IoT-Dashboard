    class MyCharts
    {
        constructor(Xdata, Ydata, chartname)
        {

            this.Xdata = Xdata;
            this.Ydata = Ydata;
            this.chartname = chartname;
            this.options = {
                height: 200
              };
        }
        createGraph()
        {
            var data = 
            {
                labels: this.Xdata,
                series: 
                [
                    this.Ydata    
                ]
            }

            new Chartist.Line(this.chartname, data, this.options);
        }
    }

    var Xdata_temp = [];
    var Ydata_temp = [];
    
    var Xdata_humid = [];
    var Ydata_humid = [];

    var Xdata_moist = [];
    var Ydata_moist = [];
    
    var Xdata_light = [];
    var Ydata_light = [];

    var obj = new MyCharts(Xdata_temp, Ydata_temp, '.ct-chart');
    obj.createGraph();

    var obj2 = new MyCharts(Xdata_humid, Ydata_humid, '.ct2-chart');
    obj2.createGraph();
    
    var obj3 = new MyCharts(Xdata_moist, Ydata_moist, '.ct3-chart');
    obj2.createGraph();
    
    var obj4 = new MyCharts(Xdata_light, Ydata_light, '.ct4-chart');
    obj2.createGraph();
    
    function requestTemp() {
        var requests = $.get('/api/kuchnhi/temperature');
        var tm = requests.done(function (result){
            
            Xdata_temp.push(result[0]);
            Ydata_temp.push(result[1]);
            
            if (Xdata_temp.length >= 10) {
                Xdata_temp.shift()
                Ydata_temp.shift()
            }

            var obj = new MyCharts(Xdata_temp, Ydata_temp, '.ct-chart');
            obj.createGraph();
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
            
            Xdata_moist.push(result[0]);
            Ydata_moist.push(result[1]);
            
            if (Xdata_moist.length >= 10) {
                Xdata_moist.shift()
                Ydata_moist.shift()
            }

            var obj1 = new MyCharts(Xdata_moist, Ydata_moist, '.ct2-chart');
            obj1.createGraph();
            document.getElementById("card-moisture").innerHTML = result[1];

        });
    }


    function requestMoisture() {
        var requests = $.get('/api/kuchnhi/humidity');
        var tm = requests.done(function (result){
            
            Xdata_humid.push(result[0]);
            Ydata_humid.push(result[1]);
            
            if (Xdata_humid.length >= 10) {
                Xdata_humid.shift()
                Ydata_humid.shift()
            }

            var obj1 = new MyCharts(Xdata_humid, Ydata_humid, '.ct3-chart');
            obj1.createGraph();
            document.getElementById("card-humidity").innerHTML = result[1];

        });
    }


    function requestLight() {
        var requests = $.get('/api/kuchnhi/light');
        var tm = requests.done(function (result){
            
            Xdata_light.push(result[0]);
            Ydata_light.push(result[1]);
            
            if (Xdata_light.length >= 10) {
                Xdata_light.shift()
                Ydata_light.shift()
            }

            var obj1 = new MyCharts(Xdata_light, Ydata_light, '.ct4-chart');
            obj1.createGraph();
            document.getElementById("card-light").innerHTML = result[1];

        });
    }

    requestTemp();