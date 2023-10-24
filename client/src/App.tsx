import './App.css';
import { RouterProvider } from 'react-router-dom';
import router from './controllers/router/router';
import PrivateRoute from './components/auth/PrivateRoute';
import { BrowserRouter as Router, Route, useNavigate } from 'react-router-dom';
import { AuthProvider } from './components/auth/AuthContext';
import DashboardPage from "./pages/dashboard";
import DevicePage from "./pages/device";
import PersonPage from "./pages/person";
import ActionPage from "./pages/action";
import SettingPage from "./pages/setting";
import Header from "./components/header/header";
import NavItem from "./components/nav-item/nav-item";
import LoginPage from "./pages/login/login";
import HomePage from "./pages/home/home";
import DeviceDetailPage from "./pages/device/slug";
import PersonDetailPage from "./pages/person/slug";
import ActionDetailPage from "./pages/action/slug";
import ZonePage from "./pages/zone";



function App() {

return (
  <AuthProvider>
  <Router>
      <Route path="/login" children={LoginPage()} />
      <PrivateRoute path="/protected" children={ZonePage()} />
  </Router>
</AuthProvider>
)
}

export default App;
