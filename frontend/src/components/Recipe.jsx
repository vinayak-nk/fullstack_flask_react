import React from 'react'
import { Card, Button } from 'react-bootstrap'


const Recipe = ({ title, description, handleUpdate, handleDelete }) => {
  return (
    <Card className='item'>
      <Card.Body>
        <Card.Title>
          {title}
        </Card.Title>
        <Card.Text>
          {description}
        </Card.Text>  
        <Button variant='primary' onClick={handleUpdate} >Update</Button>
        {' '}
        <Button variant='danger' onClick={handleDelete} >Delete</Button>
      </Card.Body>
    </Card>
  )
}

export default Recipe
