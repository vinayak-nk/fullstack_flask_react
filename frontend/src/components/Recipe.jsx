import React from 'react'
import { Card } from 'react-bootstrap'


const Recipe = ({ data }) => {
  const { title, description } = data
  console.log(data)
  return (
    <Card className='item'>
      <Card.Body>
        <Card.Title>
          {title}
        </Card.Title>
        <Card.Text>
          {description}
        </Card.Text>  
      </Card.Body>
    </Card>
  )
}

export default Recipe
