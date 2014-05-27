require.config({
	baseUrl: '/static/scripts',
	paths: {
		'underscore': 'vend/underscore-min',
		'backbone': 'vend/backbone-min',
		'bootstrap': 'vend/bootstrap.min',
		'jquery': 'vend/jquery.min',
		'jquery-tablesorter': 'vend/jquery.tablesorter.min'
	},
	shim: {
		'underscore': {
			exports: '_'
		},
		'backbone': {
			deps: ['underscore', 'jquery'],
			exports: 'Backbone'
		},
		'jquery-tablesorter': {
			deps: ['jquery']
		},
		'bootstrap': {
			deps: ['jquery']
		}
	}
});

require(['jquery', 'jquery-tablesorter'], function($){
	var generate_index = function() {
		$.each($('.index'), function(i, v){
			$(this).html(i+1);
		});
	};

	var tap, tpp;
	$.each($('.eff'), function(i, v){
		tap = $(v).siblings('.tap').html();
		tpp = $(v).siblings('.tpp').html();
		$(this).html(((tap / tpp) - 1.00).toFixed(2));
	});
	$("#main-table").tablesorter( {sortList: [[2], [1,0]]} );
	generate_index();
});