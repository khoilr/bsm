import React, { ReactElement } from 'react';
import { Navigate, Route, RouteProps } from 'react-router-dom';
import { useAuth } from './AuthContext';

type PrivateRouteProps = RouteProps & {
  children: ReactElement | null;
}

const PrivateRoute: React.FC<PrivateRouteProps> = ({ children, ...rest }) => {
  const { isAuthenticated } = useAuth();

  return isAuthenticated ? (
    <Route {...rest}>{children}</Route>
  ) : (
    <Route {...rest}>
      <Navigate to="/login" />
    </Route>
  );
};

export default PrivateRoute;
