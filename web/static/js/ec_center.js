var ec_center = echarts.init(document.getElementById('c1'), "dark");


var ec_center_option = {
    title: {
        text: '好评率',
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },
    dataset: {
        source: [
            ['score','product'],
            [95.4, 'iPhone 12'],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
            // [89.3, 58212, 'Matcha Latte'],
            // [57.1, 78254, 'Milk Tea'],
            // [74.4, 41032, 'Cheese Cocoa'],
            // [50.1, 12755, 'Cheese Brownie'],
            // [89.7, 20145, 'Matcha Cocoa'],
            // [68.1, 79146, 'Tea'],
            // [19.6, 91852, 'Orange Juice'],
            // [10.6, 101852, 'Lemon Juice'],
            // [32.7, 20112, 'Walnut Brownie'],
            // [32.7, 20112, 'Walnut']
        ]
    },
    grid: {containLabel: true},
    xAxis: {name: 'score'},
    yAxis: {type: 'category'},
    visualMap: {
        orient: 'horizontal',
        left: 'center',
        min: 10,
        max: 100,
        text: ['High Score', 'Low Score'],
        // Map the score column to color
        dimension: 0,
        inRange: {
            color: ['#65B581', '#FFCE34', '#FD665F']
        }
    },
    series: [
        {
            type: 'bar',
            encode: {
                // Map the "amount" column to X axis.
                x: 'score',
                // Map the "product" column to Y axis
                y: 'product'
            }
        }
    ]
};
ec_center.setOption(ec_center_option)