import React from "react";
import {FaInfoCircle} from 'react-icons/fa'
import {Tooltip} from 'react-tooltip'

// WeatherForm component
function WeatherForm({weatherState, setWeatherState, handleFormSubmit}) {
    const toolTipContent = `Get suggestions such as appropriate <br/> apparel for forecast. 
                            This option may <br/> increase page load time.`
                            
    return (
        <form id='form' onSubmit={handleFormSubmit}>
            <input 
                type='text' 
                value={weatherState.searchValue} 
                onChange={(e) => setWeatherState((prevState) => ({
                    ...prevState,
                    searchValue: e.target.value
                }))}
                placeholder='Enter city name'
                required
            />
            <button id='submitBtn' type='submit'>Search</button>
            <div className='checkBox'>
                <input type='checkbox' id = 'checkForDateAndTime'/>
                <label>city date and time</label>
                <br></br>
                <input type='checkbox' id = 'checkForSuggestions'/>
                <label>suggestions </label> 
                <FaInfoCircle
                    data-tooltip-id="tooltip"
                    data-tooltip-html= {toolTipContent}
                    data-tooltip-place="right"
                />
                <Tooltip id="tooltip" multiline={true}/>
            </div>
        </form>
    );
}

export default WeatherForm;