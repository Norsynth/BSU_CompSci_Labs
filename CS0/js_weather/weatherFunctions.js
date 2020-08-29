
// add your definintion of calculateDewPoint here
// dew point = temperature - (9(100 - humidity) / 25

function calculateDewPoint( temp, humidity)
{

	var dp;

	dp = temp - 9 * (100 - humidity) / 25 ;

	if (humidity >= 50){
	
	return dp;
	}

	else if (humidity < 50){
	alert('Alert! Humidity is too low');
	return "invalid";
}

}

// add your definintion of calculateWindChill here
// 35.74 + 0.6215*temperature + (0.4275 * temperature -
//35.75)*wind 0.16

function calculateWindChill( temp, wind)
{
	var wc;

	wc = 35.74 + (0.6215 * temp) + (0.4275 * temp - 35.75) * Math.pow(wind,0.16);
	
	if (wind <= 3) {
		
		wc = temp ;
	}
	
	
	if (temp <= 50) {

 	return wc;
	}

	else{
	alert('Alert! Temp is too high to calculate windchill') ;
	return "invalid";
}




}
