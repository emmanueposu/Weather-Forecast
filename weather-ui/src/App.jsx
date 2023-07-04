import React from 'react';
import Weather from './components/Weather'

function App() {

  return (
    <div className='App'>
      <div className='intro'>
        <h1>weatherView</h1>
        <>View the weather of any city by searching below</>
      </div>
      <div>
      <Weather />
      </div>
      <footer>© 2023 Prince Emmanuel</footer>
    </div>
  );
}

export default App;
