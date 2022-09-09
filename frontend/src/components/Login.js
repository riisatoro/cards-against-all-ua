import Landing from './Landing';

function Login () {
    return (
        <div className="row">
            <div className="col col-sm-12 col-md-6">
                <Landing />
            </div>
            <div className="col col-sm-12 col-md-6">
                <form>
                    <div className="form-group">
                        <label htmlFor="username">Username</label>
                        <input type="text" name="username" id="username" />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input type="password" name="password" id="password" />
                    </div>
                    <button type="submit" className="btn btn-primary">Login</button>
                </form>
            </div>
        </div>
    )
}

export default Login;
