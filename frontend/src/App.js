import React, { useEffect, useState } from 'react';
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Navbar from './components/Navbar';
import Home from './components/Home';
import SignUp from './components/SignUp'
import Login from './components/Login'
import CreateRecipe from './components/CreateRecipes'

import './App.css';

function App() {
  // const [message, setMessage] = useState('test')
  
  // useEffect(
  //   () => {
  //     fetch('/api/hello')
  //       .then(response => response.json())
  //       .then(data => setMessage(data.msg))
  //       .catch(error => console.log(error))
  //    }, []
  // )

  return (
    <BrowserRouter>
      <div className="">
      {/* <div className="container"> */}
        <Navbar />
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/login" element={<Login />} />
          <Route path="/blog" element={<CreateRecipe />} />
        </Routes>
      </div>
    </BrowserRouter>
  )
}

export default App;
