import React from 'react'
import { Form, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { useForm } from "react-hook-form";

const SignUp = () => {
  const { register, handleSubmit, watch, reset, formState: { errors } } = useForm();

  const submitForm = (data) => {
    console.log('submit', data)
    reset()
  }

  console.log(watch('username'))
  console.log(watch('email'))
  console.log(watch('password'))
  console.log(watch('confirmPassword'))

  return (
    <div className='container'>
      <div className="form">
        <h1>Sign up page</h1>
        <form action="">
          <Form.Group>
            <Form.Label>Username</Form.Label>
            <Form.Control type="text" placeholder='enter your username' {...register("username", {required: true, maxLength:25})} />
          </Form.Group>
          {errors.username && <span style={{ color: 'red' }} >User name is required</span>}
          <br />
          {errors.username?.type=="maxLength" && <span style={{ color: 'red' }} >max length exceded</span>}
          <Form.Group>
            <Form.Label>Email</Form.Label>
            <Form.Control type="email" placeholder='enter your email' {...register("email", {required:true, maxLength:80})} />
          </Form.Group>
          {errors.username && <span style={{ color: 'red' }} >Email is required</span>}
          <br />
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder='enter your password' {...register("password", {required:true, minLength:4})} />
          </Form.Group>
          {errors.username && <span style={{ color: 'red' }} >Password is required</span>}
          <br />
          <Form.Group>
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control type="password" placeholder='enter your password'  {...register("confirmPassword", { required: true, minLength: 4 })}/>
          </Form.Group>
          {errors.username && <span style={{ color: 'red' }} >Password is required</span>}
          <br />
          <Form.Group>
            <Button as="sub" variant="primary" onClick={handleSubmit(submitForm)}>
              Sign Up
            </Button>
          </Form.Group>
          <br />
          <Form.Group>
            <small>
              Already have an account?
              &nbsp;
              <Link to='/login'>Click here</Link>
            </small>
          </Form.Group>

        </form>
      </div>
    </div>
  )
}

export default SignUp

