var parseAlienQuotes = function(record){
	record['Yes Percentage'] = +record['Yes Percentage'];
	return record;
}

var loadChart = function(record){
	const WIDTH = 1200;
	const HEIGHT = 700;

	var svg = d3.select('.container').append('svg')
		.attr("width",WIDTH)
		.attr("height",HEIGHT);



}

d3.csv("../data/alienCountryWise.csv",parseAlienQuotes, loadChart);