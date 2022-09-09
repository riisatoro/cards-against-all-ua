import axios from 'axios';
import { useFormik } from 'formik';
import { useDispatch } from 'react-redux';
import Landing from './Landing';
import { LOGIN_URL } from '../constants/api.js';
import { login } from '../store/reducers/authSlice';
import { setLocation } from '../store/reducers/navigationReducer';
import Navigation from '../constants/navigation';


const Login = () => {
  const dispatch = useDispatch();

  const formik = useFormik({
    initialValues: {
      email: '',
      password: '',
    },
    onSubmit: (values) => {
      axios.post(LOGIN_URL, values)
      .then((response) => {
        dispatch(login(response.data));
      })
      .catch((error) => console.log(error));
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
              <input type="email" name="email" placeholder="Email" className='form-control' onChange={formik.handleChange} value={formik.values.username} />
            </div>
            <div className="form-group w-50 my-2">
              <input type="password" name="password" placeholder="Password" className='form-control' onChange={formik.handleChange} value={formik.values.password} />
            </div>
            <button type="submit" className="btn btn-outline-success my-2">Login</button>
          </form>
        </div>
      </div>
    </div>
  )
}

export default Login;
