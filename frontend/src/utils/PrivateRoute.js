import { Navigate } from 'react-router-dom';

const PrivateRoute = ({ children }) => {
    const authenticated = false;
    return (
        <div>{!authenticated ? <Navigate to="/login/" /> : children}</div>
    )
}

export default PrivateRoute;