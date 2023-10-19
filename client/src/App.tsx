import './App.css';
import { RouterProvider } from 'react-router-dom';
import router from './controllers/router/router';
import Header from './components/header/header';
import menus from './models/constants/nav-menus';
import NavItem from './components/nav-item/nav-item';
import { useDevice } from './controllers/hooks/';



function App() {

  return (<RouterProvider router={router} />);

}

export default App;
