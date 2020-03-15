    class MyCharts
    {
        constructor(Xdata, Ydata, chartname)
        {

            this.Xdata = Xdata;
            this.Ydata = Ydata;
            this.chartname = chartname
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

            new Chartist.Line(this.chartname, data);
        }
    }

    var Xdata = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'];

    var Ydata = [1, 2, 3, 4, 5];
    var obj = new MyCharts(Xdata, Ydata, '.ct-chart');
    obj.createGraph();
   
    var obj2 = new MyCharts(Xdata, Ydata, '.ct2-chart');
    obj2.createGraph();

    var obj3 = new MyCharts(Xdata, Ydata, '.ct3-chart');
    obj3.createGraph();
   