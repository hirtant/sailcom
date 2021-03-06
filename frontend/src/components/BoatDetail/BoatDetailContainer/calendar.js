import React, {useEffect, useState} from 'react';
import { Calendar, momentLocalizer } from 'react-big-calendar'
import 'react-big-calendar/lib/css/react-big-calendar.css';
import Loading from '../../GenericLoading'
import CalendarLegend from '../../GenericCalendarLegend'
import {connect} from "react-redux";
import moment from 'moment'

const localizer = momentLocalizer(moment)

function BoatCalendar(props) {
    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true)

    const eventStyleGetter = (event, start, end, isSelected) => {
        let className = ''
        if (event.currentUser.authorized) {
            if (event.currentUser.userData.id === event.booking.user.id) {
                className += 'your-booking '
            }
            if (event.booking.event) {

                className += 'event '

                if(event.booking.event.participants.includes(event.currentUser.userData.id)) {
                    className += 'signed-up '
                }
            }
        }

        return {
            className
        }
    }

    useEffect( () => {
        const bookings = props.boatlist[props.boatID].bookings
        const events = []
        bookings.forEach(booking => {

            const start = moment(booking.from_date_time).add(-2, 'hours')
            const end = moment(booking.until_date_time).add(-2, 'hours')

            events.push({
                currentUser: props.currentUser,
                booking: booking,
                start: new Date(start),
                end: new Date(end),
            })
        })

        setData(events)
        setLoading(false)

    }, [props.boatlist, props.currentUser])

    return (<>
        {   loading
        ? <Loading />
        :
            <div className='boat-calendar-wrapper'>
                <div id='boat-calendar'>
                <Calendar
                    culture='de-CH'
                    localizer={localizer}
                    events={data}
                    step={60}
                    defaultDate={new Date()}
                    defaultView='week'
                    format={"DD/MM/YYYY HH:mm"}
                    eventPropGetter={eventStyleGetter}
                />
              </div>
                <CalendarLegend />
            </div>

       }</>
    );
};


const mapStateToProps = (state) => {
    return {
        boatlist: state.boats.boatlist,
        currentUser: state.currentUser
    }
}
const connection = connect(mapStateToProps);
const ConnectedBoatCalendar = connection(BoatCalendar);

export default ConnectedBoatCalendar