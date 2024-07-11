import React, { useState } from 'react';
import axios from 'axios';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup'; // for validation schema


const Login = () => {
  const [errorMessage, setErrorMessage] = useState('');

  const initialValues = {
    username: '',
    password: '',
  };

  const validationSchema = Yup.object().shape({
    username: Yup.string().required('Username is required'),
    password: Yup.string()
      .required('Password is required')
      .min(8, 'Password must be at least 8 characters'),
  });

  const onSubmit = async (values, { setSubmitting }) => {
    try {
      const response = await axios.post('http://localhost:5555/login', values);

      if (response.data.success) {
        localStorage.setItem('access_token', response.data.access_token);
        // Redirect to home page (replace with your logic)
        window.location.href = '/';
      } else {
        setErrorMessage(response.data.error);
      }
    } catch (error) {
      console.error(error);
      setErrorMessage('An error occurred. Please try again.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="login-container container">
      <h1>Book Club Login</h1>
      {errorMessage && <div className="alert alert-danger">{errorMessage}</div>}
      <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={onSubmit}>
        {({ isSubmitting }) => (
          <Form>
            <div className="form-group">
              <label htmlFor="username">Username or Email</label>
              <Field
                type="text"
                id="username"
                name="username"
                placeholder="Username"
                className="form-control"
              />
              <ErrorMessage name="username" component="div" className="text-danger" />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <Field type="password" id="password" name="password" placeholder="Password" className="form-control" />
              <ErrorMessage name="password" component="div" className="text-danger" />
            </div>
            <button type="submit" className="btn btn-primary" disabled={isSubmitting}>
              {isSubmitting ? 'Submitting...' : 'Login'}
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
};

export default Login;
