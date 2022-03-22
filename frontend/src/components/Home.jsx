import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Modal, Form, Button } from 'react-bootstrap'

import { useAuth } from '../auth'
import Recipe from './Recipe'

import { useForm } from "react-hook-form";
import { useNavigate } from 'react-router-dom'



const LoggedInHome = () => {
  const { register, handleSubmit, watch, setValue, reset, formState: { errors } } = useForm()
  const [blogs, setBlogs] = useState([])
  const [show, setShow] = useState(false)
  const [blogID, setBlodID] = useState()

  const ModalBody = ({ title, description }) => {
    const submitForm = (data) => {
      reset()
      const { title, description } = data
      const token = localStorage.getItem('REACT_TOKEN_AUTH_KEY')
        const requestOptions = {
          method: 'PUT',
          headers: {
            'content-type': 'application/json',
            'Authorization': `Bearer ${JSON.parse(token)}`
          },
          body: JSON.stringify({ title, description })
        }
        fetch(`/api/blog/${blogID}`, requestOptions)
          .then(res => res.json())
          .then(data => {
            console.log(data)
            window.location.reload()
          })
          .catch(error => console.log('error', error))  
    }
  
    return (
      <form action="">
        <Form.Group>
          <Form.Label>Title</Form.Label>
          <Form.Control type="text" placeholder={title} {...register('title', { required: true, maxLength: 25 })} />
          {errors.title && <span style={{ color: 'red' }} >Title is required</span>}
        </Form.Group>
        <Form.Group>
          <Form.Label>Description</Form.Label>
          <Form.Control as="textArea" placeholder={description} row={5} {...register('description', { required: true, maxLength: 250 })}  />
        </Form.Group>
        <br />
          <Form.Group>
            <Button as="sub" variant="primary" onClick={handleSubmit(submitForm)}>
              Save
            </Button>
          </Form.Group>
      </form>
    )
  }
  
  const showModal = (id) => {
    setShow(true)

    blogs.map((blog) => {
      if (blog.id === id) {
        setValue('title', blog.title)
        setValue('description', blog.description)
        setBlodID(blog.id)
      }
    })
  }

  const handleDelete = (id) => {
    const token = localStorage.getItem('REACT_TOKEN_AUTH_KEY')
    const requestOptions = {
      method: 'DELETE',
      headers: {
        'content-type': 'application/json',
        'Authorization': `Bearer ${JSON.parse(token)}`
      },
    }
    fetch(`/api/blog/${id}`, requestOptions)
      .then(res => res.json())
      .then(data => {
        console.log(data)
        window.location.reload()
      })
      .catch(error => console.log('error', error))
  }

  useEffect(() => {
    fetch('/api/blogs')
      .then(res => res.json())
      .then(data => {
        setBlogs(data)
      })
      .catch(error => console.log(error))
  }, [])

  return (
    <div className='blogs'>
      <Modal show={show} size="lg" onHide={() => setShow(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Update Blog</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <ModalBody />
        </Modal.Body>
      </Modal>
      <h1>List of Blogs</h1>
      {blogs.map((blog) => <Recipe key={blog.id} title={blog.title} description={blog.description} handleUpdate={() => showModal(blog.id)} handleDelete={() => handleDelete(blog.id)}/>) }
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

