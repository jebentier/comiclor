(function($) {

	$.fn.getDatePickerValue = function(option){
		if(this.length == 1){
			switch(option){
				case "month":
					return this.find('select[name="dropdown_datepicker_month"]').val();
				case "day":
					return this.find('select[name="dropdown_datepicker_day"]').val();
				case "year":
					return this.find('select[name="dropdown_datepicker_year"]').val();
			}
		}
		else
			return undefined;
		return undefined;
	};

	$.fn.dropdown_datepicker = function(options){

		/*
			Settings / Options
				- css_class
				- css_name
				- month_format
					* Integer = i
					* Abreviated = a
					* Full = f
		*/

		var settings = $.extend({
			css_class: "dropdown_datepicker",
			month_format: "f"
		}, options );

		var months = [
			{id: 1, name: "Janurary", abv: "Jan", days: 31}, 
			{id: 2, name: "February", abv: "Feb", days: 29}, 
			{id: 3, name: "March", abv: "Mar", days: 31}, 
			{id: 4, name: "April", abv: "Apr", days: 30}, 
			{id: 5, name: "May", abv: "May", days: 31}, 
			{id: 6, name: "June", abv: "Jun", days: 30}, 
			{id: 7, name: "July", abv: "Jul", days: 31}, 
			{id: 8, name: "August", abv: "Aug", days: 31}, 
			{id: 9, name: "September", abv: "Sep", days: 30}, 
			{id: 10, name: "October", abv: "Oct", days: 31}, 
			{id: 11, name: "November", abv: "Nov", days: 30}, 
			{id: 12, name: "December", abv: "Dec", days: 31}
		];

		var today = new Date();

		var get_month_display_value = function(month_i){
			switch(settings.month_format){
				case "i":
					return months[month_i-1].id;
				case "a":
					return months[month_i-1].abv;
				case "f":
					return months[month_i-1].name;
			}
			return null;
		};

		var generate_month_dropdown = function(){
			var $month_dropdown = $("<select name='dropdown_datepicker_month' class='"+settings.css_class+"' style='width: auto; margin-right:5px;'></select>");
			for(var i = 1; i <= 12; i++){
				$month_dropdown.append("<option value='"+i+"'>"+get_month_display_value(i)+"</option>");
			}
			return $month_dropdown;
		};

		var generate_day_dropdown = function(month_i){
			var $day_dropdown = $("<select name='dropdown_datepicker_day' class='"+settings.css_class+"' style='width: auto; margin-right:5px;'></select>");
			for(var i = 1; i <= months[month_i-1].days; i++){
				$day_dropdown.append("<option value='"+i+"'>"+i+"</option>");
			}
			return $day_dropdown;
		}

		var generate_year_dropdown = function(){
			var $year_dropdown = $("<select name='dropdown_datepicker_year' class='"+settings.css_class+"' style='width: auto; margin-right:5px;'></select>");
			for(var i = today.getFullYear(); i >= today.getFullYear()-70; i--){
				$year_dropdown.append("<option value='"+i+"'>"+i+"</option>");
			}
			return $year_dropdown;
		};

		return this.each(function(){
			var $container = $(this);

			$container.addClass('dropdown_datepicker');

			var $month_dropdown = generate_month_dropdown();
			var $day_dropdown = generate_day_dropdown(1);
			var $year_dropdown = generate_year_dropdown();

			$container.append($month_dropdown).append($day_dropdown).append($year_dropdown);

			$container.on('change', 'select[name="dropdown_datepicker_month"]', function(){
				$day_dropdown = generate_day_dropdown($(this).val());
				$container.find('select[name="dropdown_datepicker_day"]').html($day_dropdown.html());
			});
		});
	};

})(jQuery);