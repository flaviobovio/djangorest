import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DataTable from 'react-data-table-component';


export function Tabla() {

    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            const response = await axios.get('https://flavioboviovt.pythonanywhere.com/api/v1/swimmer/');
            setData(response.data);
            setLoading(false);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const columns = [
        {
            name: "Name",
            selector: (row) => row.name,
            sortable: true,
        },
        {
            name: "Age",
            selector: (row) => row.age,
            sortable: true,
        },
        {
            name: "Club",
            selector: (row) => row.club,
        },
        {
            name: "City",
            selector: (row) => row.city,
        },

        {
            name: '',
            cell: row => <button onClick={() => handleAction(row)}>Action</button>,
            ignoreRowClick: true,
            allowOverflow: true,
            button: true
        }


    ];


    return (
        <div>
            <DataTable columns={columns} data={data} />
        </div>
    );
}
