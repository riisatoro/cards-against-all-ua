import { useDispatch } from 'react-redux';
import Landing from './Landing';
import { useFormik } from 'formik';
import { createAccount } from '../store/reducers/apiRequests';

const Registration = () => {
  const dispatch = useDispatch();
  
  const formik = useFormik({
    initialValues: {
      username: '',
      email: '',
      password: '',
      repeat_password: '',
    },
    onSubmit: (values) => {
      dispatch(createAccount(values));
    }
  });

  return (
    <div className="container">
      <div className="row">
        <div className="col col-sm-12 col-md-6">
          <Landing />
        </div>
        <div className="col col-sm-12 col-md-6 align-items-center">
          <form onSubmit={formik.handleSubmit}>
            <div className="form-group w-50 my-2">
              <input
                type="text"
                name="username"
                placeholder="Username"
                className='form-control'
                onChange={formik.handleChange}
                value={formik.values.username}
              />
            </div>
            <div className="form-group w-50 my-2">
              <input
                type="email"
                name="email"
                placeholder="Email"
                className='form-control'
                onChange={formik.handleChange}
                value={formik.values.email}
              />
            </div>
            <div className="form-group w-50 my-2">
              <input
                type="password"
                name="password"
                placeholder="Password"
                className='form-control'
                onChange={formik.handleChange}
                value={formik.values.password}
              />
            </div>
            <div className="form-group w-50 my-2">
              <input
                type="password"
                name="repeat_password"
                placeholder="Repeat password"
                className='form-control'
                onChange={formik.handleChange}
                value={formik.values.repeat_password}
              />
            </div>
            <button type="submit" className="btn btn-outline-success my-2">Registration</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Registration;
