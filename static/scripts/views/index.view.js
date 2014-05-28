define([
	'jquery',
	'underscore',
	'backbone',
	'bootstrap',
	'jquery-tablesorter'
], function($, _, Backbone){
	var IndexView = Backbone.View.extend({
    el: $('body'),

		generate_index: function() {
			$.each($('.index:visible'), function(i, v){
				$(this).html(i+1);
			});
		},

		initialize: function() {
			var tap, tpp;
			$.each($('.eff'), function(i, v){
				tap = $(v).siblings('.tap').html();
				tpp = $(v).siblings('.tpp').html();
				$(this).html(((tap / tpp) - 1.00).toFixed(2));
			});
			$("#main-table").tablesorter( {sortList: [[2], [1,0]]} );
			this.generate_index();
		},

		events: {
			'click .position-sort': 'sortByPosition'
		},

		sortByPosition: function(e) {
      var dataPosition = $(e.target).data('position');
      $('.player-row').show();
      if (dataPosition !== 'all') {
        $('.player-row[data-sort!="' + dataPosition + '"]').hide();
      }
      this.generate_index();
		}
	});

	return IndexView;
});