import React, {useEffect, useState} from 'react';
import axios from 'axios'

const App = () => {

    const[cars, setCars]=useState([])

  useEffect(()=>{
    axios.get('/api/cars').then(value => setCars(value.data))
      },
      [])
    return (
        <div>
            <h4>Cars</h4>
            {cars.map(car=><div key={car.id}>{car.name}</div>)}
        </div>
    );
};

export default App;
