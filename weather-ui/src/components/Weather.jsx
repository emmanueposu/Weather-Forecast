import React, {useState, useEffect} from 'react';
import axios from 'axios';
import WeatherForm from './WeatherForm';
// API Keys
const weatherKey = import.meta.env.VITE_WEATHER_KEY;
const dateAndTimeKey = import.meta.env.VITE_DATE_AND_TIME_KEY;

// Helper functions
function initiateWeatherStates() {
    const [weatherState, setWeatherState] = useState({
        searchValue: '',
        isCheckedForDateAndTime: false,
        isCheckedForSuggestions: false,
        system: 'imperial',
        tempUnit: 'F',
        speedUnit: 'mph',
        icon: '',
        temperature: '',
        description: '',
        humidity: '',
        windSpeed: '',
        location: '',
        dateAndTime: '',
        suggestions: '',
        errorMsg: ''
    });
    return [weatherState, setWeatherState];
}

function clearSearchBar(setWeatherState){
    setWeatherState((prevState) => ({
        ...prevState,
        searchValue: '',
    }));
}

function setCheckBoxState(setWeatherState) {
    setWeatherState((prevState) => ({
        ...prevState,
        isCheckedForDateAndTime: document.getElementById('checkForDateAndTime').checked,
        isCheckedForSuggestions: document.getElementById('checkForSuggestions').checked
    }));
}

async function getWeatherData(weatherState, setWeatherState) {
    const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${weatherState.searchValue}
                        &appid=${weatherKey}&units=${weatherState.system}`;
    const weatherResponse = await axios.get(weatherUrl);
    const {weather: {0: {description, icon}}} = weatherResponse.data;
    const {main: {humidity, temp}, wind: {speed}, name} = weatherResponse.data;
    setWeatherState((prevState) => ({
        ...prevState,
        icon: icon,
        temperature: temp,
        description: description,
        humidity: humidity,
        windSpeed: speed,
        location: name
    }));
    return weatherResponse.data;
}

async function getDateAndTimeData(xCoord, yCoord, setWeatherState) {
    const dateAndTimeUrl = `http://api.timezonedb.com/v2.1/get-time-zone?key=${dateAndTimeKey}
                            &format=json&by=position&lat=${yCoord}&lng=${xCoord}`;
    const dateAndTimeResponse = await axios.get(dateAndTimeUrl);
    setWeatherState((prevState) => ({
        ...prevState,
        dateAndTime: dateAndTimeResponse.data.formatted
    }));
}

function getSuggestionsFromServer(setWeatherState, temp, description , tempUnit) {
    const dataForSuggestions = {
        'temperature': temp,
        'description': description,
        'unit': tempUnit
    }
    axios.post('http://localhost:3000/suggestions', dataForSuggestions)
    .then(serverResponse =>{
        setWeatherState((prevState) => ({
            ...prevState,
            suggestions: serverResponse.data
        }));
    })
    .catch(error => {
        console.error('Server Error: ', error);
    });   
}

function highlightMetricButton() {
    document.getElementById('C').style.backgroundColor = 'white';
    document.getElementById('C').style.color = '#3d405b';
    document.getElementById('F').style.backgroundColor = '#3d405b';
    document.getElementById('F').style.color = 'white';
}

function highlightImperialButton() {
    document.getElementById('F').style.backgroundColor = 'white';
    document.getElementById('F').style.color = '#3d405b';
    document.getElementById('C').style.backgroundColor = '#3d405b';
    document.getElementById('C').style.color = 'white';
}

function convertTemperature (system, temperature, setWeatherState) {
    if (temperature == ''){
        return;
    }if(system == 'metric'){
        setWeatherState((prevState) => ({
            ...prevState,
            temperature: (temperature - 32) * (5/9),
            tempUnit: 'C'
        }));
        highlightMetricButton();
    }else if(system == 'imperial'){
        setWeatherState((prevState) => ({
            ...prevState,
            temperature: (temperature * (9/5) + 32),
            tempUnit: 'F'
        }));
        highlightImperialButton();
    }
}

function convertWindSpeed (system, speed, setWeatherState) {
    if (speed == ''){
        return;
    }if(system == 'metric') {
        setWeatherState((prevState) => ({
            ...prevState,
            windSpeed: speed / 2.237,
            speedUnit: 'm/s'
        }));
    } else if(system == 'imperial'){
        setWeatherState((prevState) => ({
            ...prevState,
            windSpeed: speed * 2.237,
            speedUnit: 'mph'
        }));
    }
}
// Weather component
function Weather() {
    const [weatherState, setWeatherState] = initiateWeatherStates();

    const handleFormSubmit = async (e) => {
        e.preventDefault();
        clearSearchBar(setWeatherState);
        setCheckBoxState(setWeatherState);
        
        try {
            const weatherData = await getWeatherData(weatherState, setWeatherState);

            if (document.getElementById('checkForDateAndTime').checked) {
                await getDateAndTimeData(
                    weatherData.coord.lon, 
                    weatherData.coord.lat, 
                    setWeatherState);
            }
            
            if (document.getElementById('checkForSuggestions').checked) {
                getSuggestionsFromServer(
                    setWeatherState, 
                    weatherData.main.temp, 
                    weatherData.weather[0].description, 
                    weatherState.tempUnit);
            }
    
        } catch (error) {
            console.error('Error:', error);
            setWeatherState((prevState) => ({
                ...prevState,
                errorMsg: 'Unable to retrieve weather forecast'
            }));
        }
    };
    // Convert temperature when the system of measure changes
    useEffect(() => {
        convertTemperature(weatherState.system, weatherState.temperature, setWeatherState);
        convertWindSpeed(weatherState.system, weatherState.windSpeed, setWeatherState);
    }, [weatherState.system]
    );

    return (
        <div className='weather'>       
            {weatherState.errorMsg ? (<p>{weatherState.errorMsg}</p>) :
            weatherState.location ? (
                <>  
                    {/* Display weather information */}
                    <div className='tempIcon'>
                        <img 
                            src={`https://openweathermap.org/img/wn/${weatherState.icon}@2x.png`} 
                            alt='Weather Icon'
                        />
                        <p>{Math.round(weatherState.temperature)}° {weatherState.tempUnit}</p>
                    </div>
                    <div className='unitBtn'>
                        <button 
                            id='F' 
                            value='imperial' 
                            onClick={(e) => setWeatherState((prevState) => ({
                                ...prevState,
                                system: e.target.value
                            }))}>
                            °F, imperial
                        </button>
                        <button 
                            id='C' 
                            value='metric' 
                            onClick={(e) => setWeatherState((prevState) => ({
                                ...prevState,
                                system: e.target.value
                            }))}>
                            °C, metric
                        </button>
                    </div>
                    <p>{weatherState.description}</p>
                    <p>Humidity: {weatherState.humidity}%</p>
                    <p>Wind Speed: {Math.round(weatherState.windSpeed)} {weatherState.speedUnit}</p>
                    <p>{weatherState.location}</p>
                    {/* Display date and time if checked */}
                    {weatherState.isCheckedForDateAndTime && <p>{weatherState.dateAndTime}</p>}
                    {/* Display suggestions if checked */}
                    {weatherState.isCheckedForSuggestions && (
                        <div className='suggestions'>
                            <p><b>Clothing:</b> {weatherState.suggestions.clothing}</p>
                            <p><b>Activity:</b> {weatherState.suggestions.activity}</p>
                            <p><b>Precautions:</b> {weatherState.suggestions.precautions}</p>
                            <p><b>Accessories:</b> {weatherState.suggestions.accessories}</p>
                        </div>
                    )}
                </>
            ) : 
            null}
            {/* Render the WeatherForm component */}
            <WeatherForm
                weatherState={weatherState}
                setWeatherState={setWeatherState}
                handleFormSubmit={handleFormSubmit}
            />    
        </div>
    );
};

export default Weather;