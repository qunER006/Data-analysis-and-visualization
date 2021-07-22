var ec_left2 = echarts.init(document.getElementById('l2'), "dark");
var ec_left2_Option = {
	color: ['#3398DB'],
	tooltip: {
		trigger: 'axis',
		axisPointer: {            // 坐标轴指示器，坐标轴触发有效
			type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
		}
	},
	// tooltip: {
	// 	trigger: 'axis',
	// 	//指示器
	// 	axisPointer: {
	// 		type: 'line',
	// 		lineStyle: {
	// 			color: '#7171C6'
	// 		}
	// 	},
	// },
	legend: {
		type: 'plain',
		data: ['Words', 'Frequency'],
		left: "right"
	},
	//标题样式
	title: {
		text: "Top 15 Words",
		textStyle: {
			color: 'white',
		},
		left: 'left'
	},
	//图形位置
	// grid: {
	// 	left: '4%',
	// 	right: '6%',
	// 	bottom: '4%',
	// 	top: 50,
	// 	containLabel: false
	// },
	// xAxis: [{
	// 	show: true,
	// 	type: 'category',
	// 	position:'bottom',
	// 	//x轴坐标点开始与结束点位置都不在最边缘
	// 	// boundaryGap : true,
	// 	data: [],
	// 	axisTick:{					//---坐标轴 刻度
	// 		show:true,					//---是否显示
	// 		inside:true,				//---是否朝内
	// 		lengt:3,					//---长度
	// 		lineStyle:{
	// 			//color:'red',			//---默认取轴线的颜色
	// 			width:1,
	// 			type:'solid',
	// 		},
	// 	}
	// }],
	// yAxis: [{
	// 	type: 'value',
	// 	//y轴字体设置

	// 	//y轴线设置显示
	// 	axisLine: {
	// 		show: true
	// 	},
	// 	axisLabel: {
	// 		show: false,
	// 		color: 'white',
	// 		fontSize: 12,
	// 		// formatter: function(value) {
	// 		// 	if (value >= 1000) {
	// 		// 		value = value / 1000 + 'k';
	// 		// 	}
	// 		// 	return value;
	// 		// }
	// 	},
	// 	//与x轴平行的线样式
	// 	splitLine: {
	// 		show: false,
	// 		lineStyle: {
	// 			color: '#17273B',
	// 			width: 1,
	// 			type: 'solid',
	// 		}
	// 	}
	// }],
	xAxis: {
        type: 'category',
        data: []
    },
    yAxis: {
        type: 'value'
    },
	series: [{
        data: [],
        type: 'bar',
		barMaxWidth:"50%"
    }]

	// series: [{
	// 	name: "Words",
	// 	type: 'bar',
	// 	smooth: true,
	// 	data: []
	// },
	// {
	// 	name: "Frequency",
	// 	type: 'line',
	// 	smooth: true,
	// 	data: []
	// }
	// ]
};

ec_left2.setOption(ec_left2_Option)
