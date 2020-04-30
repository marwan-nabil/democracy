import React, { useState } from 'react';
import 'typeface-roboto';
import NavBar from './components/NavBar';
import Avatar from '@material-ui/core/Avatar';
import Chip from '@material-ui/core/Chip';
import axios from 'axios';

function App() {
  const [count, setCount] = useState(0);

  const handleDelete = () => {
    console.info('You clicked the delete icon.');
  };

  // (marwan): simple api request to test server
  const getCatalog = (event) => {
    event.preventDefault();
    axios.get('http://localhost:8000/api/thread_count/')
      .then(function (response) {
        setCount(response.data);
      })
  };

  return (
    <div>
      <NavBar getCatalog={getCatalog} />
      <div>
        <Chip
          avatar={<Avatar>M</Avatar>}
          label={"there's " + count + " threads"}
          clickable
          color="primary"
          onDelete={handleDelete}
        />
      </div>
    </div>
  );
}

export default App;
