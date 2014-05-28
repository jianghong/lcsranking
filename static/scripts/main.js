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

require(['views/index.view'], function(IndexView){
	var indexView = new IndexView;
});