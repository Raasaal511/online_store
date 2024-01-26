import React, {useState, useEffect } from 'react';
import axios from 'axios'
import { Link, useParams} from 'react-router-dom';


function UserRegister() {
    const [register, setRegister] = useState();

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/v1/users/register/', {username, email, password})
        .then(response => {
            setRegister(response.data)
        })
        .catch(err => {
            console.log(err);
        });

    }, []);

    return (
        <form>
            <label>
            Имя:
                <input type="text" name="name" />
                </label>
                <input type="submit" value="Отправить" />
        </form>
    )
}
