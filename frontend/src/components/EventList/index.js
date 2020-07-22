import React, {useEffect, useState} from 'react';
import {baseUrl} from "../../store/constants";
import {connect} from "react-redux";
import {NavLink} from 'react-router-dom'
import Loading from '../GenericLoading'
import EventsContainer from './eventscontainer'
import EventModal from './modal'
import EventListFilter from './Filter'
import Accordion from "../Accordion";
import {dateToISOString} from "../../lib/helpers/formatDates";
import Axios from "../../axios";

function EventListContainer(props) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [visibilityFilter, setVisibilityFilter] = useState()

     useEffect(() => {
        console.log(visibilityFilter)
        const fetchBoats = async () => {
            let url = 'event/'

            if (visibilityFilter) {
                url += visibilityFilter
            }
            try {
                const response = await Axios.get(url);
                setData(response.data.results)
                setLoading(false)
                return response;
            } catch (error) {
                console.log(error.response.data)
            }
       }
       fetchBoats()
    }, [visibilityFilter])

    const updateState = event_id => {
        console.log('old state', data)
        const user_id = props.currentUser.userData.id
        let event_index = 0
        data.forEach((item, index) =>{
            if(item.id === event_id) {
                event_index = index;
            }
        })
        let new_participants = data[event_index].participants
        if (new_participants.includes(user_id)) {
            console.log('it contains id')
            new_participants.splice(new_participants.indexOf(user_id), 1);
        } else {
            console.log('it does not contain id')
            new_participants.push(user_id)
        }
        let newState = data
        newState[event_index].participants = new_participants
        console.log('new State', newState)
        setData(newState)
    }

 const resetFilter = (e) => {
        e.preventDefault()
        setVisibilityFilter(null)
    }

    const submitFilterHandler = (e, filterQuery) => {
        e.preventDefault()
        let count = 0
        let query = '?'
        for (const [key, value] of Object.entries(filterQuery)) {
            if(value) {
                query += `${key}=${value}&`
                count++
            }
        }
        const searchURL = query.slice(0, -1)
        if(count > 0) {
            setVisibilityFilter(searchURL)
        } else {
            resetFilter(e)
        }
    }

    const accordionContent = [
        {
            title: 'Filter',
            content: <EventListFilter submitFilterHandler={submitFilterHandler} resetFilter={resetFilter}/>,
        }
    ];

    return (
        <>
            <div className='main-wrapper'>
                <Accordion content={accordionContent}/>
            </div>
            {props.events.activeModal
                ? <EventModal activeModal={props.events.activeModal} event={props.events.modalEvent} updateState={updateState}/>
                : null
            }
            <h1>Veranstaltungen</h1>
            {
                props.currentUser.authorized
                ? <NavLink to='/event-erstellen' className='btn primary create-event'>Event erstellen</NavLink>
                : null
            }
            {loading ?
                <Loading /> : <EventsContainer data={data}/>
            }
            {
                props.currentUser.authorized
                ? <NavLink to='/event-erstellen' className='btn primary create-event'>Event erstellen</NavLink>
                : null
            }
        </>
    );
};

const mapStateToProps = (state) => {
    return {
        currentUser: state.currentUser,
        events: state.events
    }
}
const connection = connect(mapStateToProps);
const ConnectedEventListContainer = connection(EventListContainer);

export default ConnectedEventListContainer;
