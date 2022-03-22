import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

import { useAuth } from '../auth'
import Recipe from './Recipe'

const LoggedInHome = () => {
  const [recipes, setRecipes] = useState([])

  useEffect(() => {
    fetch('/api/recipes')
      .then(res => res.json())
      .then(data => {
        setRecipes(data)
      })
      .catch(error => console.log(error))
  }, [])
  console.log('recipes', recipes)
  return (
    <div className='recipes'>
      <h1>List of Recipes</h1>
      {recipes.map((recipe) => <Recipe key={recipe.id} data={recipe} />)}

    </div>
  )
}

const LoggedOutHome = () => {
  return (
    <div className="home container">
      <h1 className='heading'>Welcome to the Home Page</h1>
      <Link to='/signup' className='btn btn-primary btn-lg' >Get started</Link>
    </div>
  )
}


const Home = () => {
  const [logged] = useAuth()
  
  return (
    <>
      { logged ? <LoggedInHome /> : <LoggedOutHome /> }
    </>
  )
}

export default Home

