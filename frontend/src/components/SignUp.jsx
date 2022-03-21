import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap'
import { Link } from 'react-router-dom'

const SignUp = () => {
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')

  const submitForm = () => {
    console.log('submit')

    setUsername('')
    setEmail('')
    setPassword('')
    setConfirmPassword('')
  }

  return (
    <div className='container'>
      <div className="form">
        <h1>Sign up page</h1>
        <form action="">
          <Form.Group>
            <Form.Label>Username</Form.Label>
            <Form.Control type="text" placeholder='enter your username' value={username} name='username' onChange={(e) => setUsername(e.target.value)} />
          </Form.Group>
          <br />
          <Form.Group>
            <Form.Label>Email</Form.Label>
            <Form.Control type="email" placeholder='enter your email' value={email} name='email' onChange={(e) => setEmail(e.target.value)} />
          </Form.Group>
          <br />
          <Form.Group>
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder='enter your password' value={password} name='password' onChange={(e) => setPassword(e.target.value)} />
          </Form.Group>
          <br />
          <Form.Group>
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control type="password" placeholder='enter your password' value={confirmPassword} name='confirmPassword' onChange={(e) => setConfirmPassword(e.target.value)} />
          </Form.Group>
          <br />
          <Form.Group>
            <Button as="sub" variant="primary" onClick={submitForm}>
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

