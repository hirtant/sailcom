import React, {useEffect} from 'react';
import DatePicker from "react-datepicker";
import {displayTimeDateFormatWithoutY} from "../../../store/constants"
import "react-datepicker/dist/react-datepicker.css";
import {dateToISOString, dateParseWithTimezone} from "../../../lib/helpers/formatDates";


export default function PeriodPicker(props) {
    const today = new Date()

     useEffect(() => {
        const datePickers = document.querySelectorAll('.react-datepicker__input-container input')
        datePickers.forEach( input => input.setAttribute("readOnly", true))
     })

    return (
        <div className='filter-datepicker-container'>
            <div id='boat-datepicker'>
                <div className='input-wrapper'>
                    <label>Zeitraum</label>
                    <DatePicker
                        selected={props.from ? dateToISOString(props.from) : null}
                        minDate={today}
                        onChange={date => props.onChangeDateHandler(dateToISOString(date), 'from_date_time')}
                        showTimeSelect
                        placeholderText="Von"
                        dateFormat={displayTimeDateFormatWithoutY}
                        id='from_date_time'
                    />
                    <DatePicker
                        selected={props.until ? Date.parse(props.until) : null}
                        minDate={Date.parse(props.from)}
                        onChange={date => props.onChangeDateHandler(dateToISOString(date), 'until_date_time')}
                        showTimeSelect
                        placeholderText="Bis"
                        dateFormat={displayTimeDateFormatWithoutY}
                        id='until_date_time'
                    />
                </div>
                <p id='datepicker-error' className='error'></p>
              </div>
        </div>
    );
};


/*
return (
        <div className='filter-datepicker-container'>
            <div id='boat-datepicker'>
                <div className='input-wrapper'>
                    <label>Zeitraum</label>
                    <DatePicker
                        selected={props.from ? Date.parse(props.from) : null}
                        minDate={today}
                        onChange={date => props.onChangeDateHandler(dateToISOString(date), 'from_date_time')}
                        showTimeSelect
                        placeholderText="Von"
                        dateFormat={displayTimeDateFormatWithoutY}
                        id='from_date_time'
                    />
                    <DatePicker
                        selected={props.until ? Date.parse(props.until) : null}
                        minDate={Date.parse(props.from)}
                        onChange={date => props.onChangeDateHandler(dateToISOString(date), 'until_date_time')}
                        showTimeSelect
                        placeholderText="Bis"
                        dateFormat={displayTimeDateFormatWithoutY}
                        id='until_date_time'
                    />
                </div>
                <p id='datepicker-error' className='error'></p>
              </div>
        </div>
    );
*/