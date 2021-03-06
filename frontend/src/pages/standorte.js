import React, { useEffect, useState } from 'react';
import BoatListFilter from '../components/BoatsList/Filter';
import Loading from '../components/GenericLoading';
import Accordion from '../components/Accordion';
import { dateToISOString } from '../lib/helpers/formatDates';
import Axios from '../axios';
import Maps from '../components/Map/mapContainer';
import {toggleAccordionHandler} from '../lib/helpers/filters'

export default function LocationContainer(props) {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [visibilityFilter, setVisibilityFilter] = useState();

    useEffect(() => {
        const fetchBoats = async () => {
            setLoading(true)
            let url = 'boat/';

            if (visibilityFilter) {
                url += visibilityFilter;
            }
            try {
                const response = await Axios.get(url);
                setData(response.data.results);
                setLoading(false);
                return response;
            } catch (error) {
                if (error.response) {
                    console.log('an error occurred', error);
                }
            }
        };
        fetchBoats();
    }, [visibilityFilter]);

    const resetFilter = (e) => {
        e.preventDefault();
        setVisibilityFilter(null);
        toggleAccordionHandler('panel-0', 'icon-0')

    };

    const submitFilterHandler = (e, filterQuery) => {
        e.preventDefault();
        toggleAccordionHandler('panel-0', 'icon-0')
        let count = 0;
        let query = '?';
        for (const [key, value] of Object.entries(filterQuery)) {
            if (value) {
                if (key === 'from_date_time' || key === 'until_date_time') {
                    const formatted_date = dateToISOString(value);
                    console.log('is date', formatted_date);
                    query += `${key}=${formatted_date}&`;
                } else {
                    query += `${key}=${value}&`;
                }
                count++;
            }
        }
        const searchURL = query.slice(0, -1);
        if (count > 0) {
            setVisibilityFilter(searchURL);
        } else {
            resetFilter(e);
        }
    };

    const accordionContent = [
        {
            title: 'Filter',
            content: (
                <BoatListFilter
                    submitFilterHandler={submitFilterHandler}
                    resetFilter={resetFilter}
                />
            ),
        },
    ];

    return (
        <>
            <div className='main-wrapper map-filter-wrapper'>
                <Accordion content={accordionContent} />
            </div>
            {loading ? (
                <Loading />
            ) : (
                <div className='filtered-map'>
                    <Maps boatOverview={data} />
                </div>
            )}
        </>
    );
}
