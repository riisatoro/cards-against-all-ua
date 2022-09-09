import Landing from './Landing';

function Login() {
  return (
    <div className="container">
      <div className="row">
        <div className="col col-sm-12 col-md-6">
          <Landing />
        </div>
        <div className="col col-sm-12 col-md-6 align-items-center">
          <form>
            <div className="form-group w-50 my-2">
              <input type="text" name="username" placeholder="Username" className='form-control' />
            </div>
            <div className="form-group w-50 my-2">
              <input type="password" name="password" placeholder="Password" className='form-control' />
            </div>
            <button type="submit" className="btn btn-primary my-2">Login</button>
          </form>
        </div>
      </div>
    </div>
  )
}

export default Login;
