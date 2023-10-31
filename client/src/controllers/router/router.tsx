import { Route, RouteObject, Routes, createBrowserRouter, useLocation, } from "react-router-dom"
import DashboardPage from "../../pages/dashboard";
import DevicePage from "../../pages/device";
import PersonPage from "../../pages/person";
import ActionPage from "../../pages/action";
import SettingPage from "../../pages/setting";
import Header from "../../components/header/header";
import menus from "../../models/constants/nav-menus";
import NavItem from "../../components/nav-item/nav-item";
import { useDevice } from "../hooks";
import LoginPage from "../../pages/login/login";
import HomePage from "../../pages/home/home";
import DeviceDetailPage from "../../pages/device/slug";
import PersonDetailPage from "../../pages/person/slug";
import ActionDetailPage from "../../pages/action/slug";
import ZonePage from "../../pages/zone";


export const routes: RouteObject[] = [

    {
        path: '/dashboard',
        element: <DashboardPage />,
    },
    {
        path: '/device',
        element: <DevicePage />,
    },
    {
        path: '/device/:slug',
        element: <DeviceDetailPage />,
    },
    {
        path: '/person',
        element: <PersonPage />,
    },
    {
        path: '/person/:slug',
        element: <PersonDetailPage />,
    },
    {
        path: '/zone',
        element: <ZonePage />,

    },
    {
        path: '/action',
        element: <ActionPage />,
    },
    {
        path: '/action/:slug',
        element: <ActionDetailPage />,
    },
    {
        path: '/setting',
        element: <SettingPage />,
    },

];
function Root() {
    const [showNavbar, setShowNavbar] = useDevice();
    const { pathname } = useLocation();
    console.log(pathname);
    return (
        <div className="prose app flex flex-col">
            <Header />
            <div className='flex flex-row flex-grow'>

                {!showNavbar && <div className='flex flex-col bg-white w-[100px] mt-1 '>
                    {menus.map((item) => <NavItem key={item.path} {...item} selected={pathname.indexOf(item.path) >= 0} />)}
                </div>}
                <div className='flex-grow w-full'>
                    <Routes >
                        {routes.map((route) => <Route key={route.path} path={route.path} element={route.element} />)}
                    </Routes>


                </div>

            </div>

        </div>
    );

}
const router = createBrowserRouter([
    {
        path: "*", Component: Root,

    },
    {
        path: "/login",
        Component: LoginPage,
    },
    {
        path: "/",
        Component: HomePage,
    },
]);
export default router;


