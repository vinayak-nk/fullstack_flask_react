import React, {useState, useEffect} from 'react'
import { Form, Button } from 'react-bootstrap'
import { useForm } from "react-hook-form";
import { useNavigate } from 'react-router-dom'


const CreateRecipe = () => {
  const { register, handleSubmit, watch, reset, formState: { errors } } = useForm();
  const [serverResponse, setServerRespose] = useState('')
  const navigate = useNavigate();


  const submitForm = (data) => {
    console.log('submit', data)
    reset()

    const { title, description } = data
    const token = localStorage.getItem('REACT_TOKEN_AUTH_KEY')
      const requestOptions = {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          'Authorization': `Bearer ${JSON.parse(token)}`
        },
        body: JSON.stringify({ title, description })
      }
      fetch('/api/blogs', requestOptions)
        .then(res => res.json())
        .then(data => setServerRespose(data.message))
      .catch(error => console.log('error', error))
    
      navigate('/')
  }

  // console.log(watch('title'))
  // console.log(watch('description'))
  console.log('serverResponse=', serverResponse)
  return (
    <div className='container'>
      <h1>Create A Recipe</h1>
      <form action="">
        <Form.Group>
          <Form.Label>Title</Form.Label>
          <Form.Control type="text" {...register('title', { required: true, maxLength: 25 })} />
          {errors.title && <span style={{ color: 'red' }} >Title is required</span>}
        </Form.Group>
        <Form.Group>
          <Form.Label>Description</Form.Label>
          <Form.Control as="textArea" row={5} {...register('description', { required: true, maxLength: 250 })}  />
        </Form.Group>
        <br />
          <Form.Group>
            <Button as="sub" variant="primary" onClick={handleSubmit(submitForm)}>
              Save
            </Button>
          </Form.Group>
      </form>
    </div>
  )
}

export default CreateRecipe

