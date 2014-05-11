$(function(){

    // Fill dates and times in the Logs filtering modal

    // Fill months
    for(var i=1; i<13; i++){
        $('.from-date-month').append('<option class="log-date-month">' + i + '</option>');
        $('.to-date-month').append('<option class="log-date-month">' + i + '</option>');
    }

    // Fill days
    for(var i=1; i<32; i++){
        $('.from-date-day').append('<option class="log-date-day">' + i + '</option>');
        $('.to-date-day').append('<option class="log-date-day">' + i + '</option>');
    }

    // Fill years. Year starts at 2014, since the program didn't exist before then...
    for(var i=2014; i<2020; i++){
        $('.from-date-year').append('<option class="log-date-year">' + i + '</option>');
        $('.to-date-year').append('<option class="log-date-year">' + i + '</option>');
    }

    // Fill hours
    for(var i=0; i<25; i++){
        $('.from-date-hour').append('<option class="log-date-hour">' + i + '</option>');
        $('.to-date-hour').append('<option class="log-date-hour">' + i + '</option>');
    }

    // Fill minutes
    for(var i=0; i<61; i++){
        $('.from-date-minute').append('<option class="log-date-minute">' + i + '</option>');
        $('.to-date-minute').append('<option class="log-date-minute">' + i + '</option>');
    }

});