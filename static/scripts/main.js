require.config({
	baseUrl: '/static/scripts',
	paths: {
		'underscore': 'lib/underscore-min',
		'backbone': 'lib/backbone-min',
		'bootstrap': 'lib/bootstrap.min',
		'jquery': 'lib/jquery.min'
	},
	shim: {
		'underscore': {
			exports: '_'
		},
		'backbone': {
			deps: ['underscore', 'jquery'],
			exports: 'Backbone'
		}
	}
});

require(['jquery'], function($){
	var tap, tpp;
	$.each($('.eff'), function(i, v){
		tap = $(v).siblings('.tap').html();
		tpp = $(v).siblings('.tpp').html();
		$(this).html((tap / tpp).toFixed(2));
	});
});