import { useFormik } from 'formik';
import { useDispatch, useSelector } from 'react-redux';
import { Navigate } from 'react-router-dom';
import { Navigation } from '../constants';
import { fetchAccessTokens } from '../store/reducers/apiRequests';


const Login = () => {
  const dispatch = useDispatch();
  const { accessToken } = useSelector((state) => state.auth);

  const formik = useFormik({
    initialValues: {
      email: '',
      password: '',
    },
    onSubmit: (values) => {
      dispatch(fetchAccessTokens(values));
    }
  });

  if (accessToken) return <Navigate to={Navigation.profile} />

  return (
    <div className="container">
      <div className="row">
        <div className="col col-sm-12 col-md-6">
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
