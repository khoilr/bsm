import { AiFillHome } from 'react-icons/ai';
import { BsFillCameraVideoFill, BsFillSignIntersectionFill } from 'react-icons/bs';
import { BiFace } from 'react-icons/bi';
import { MdPendingActions } from 'react-icons/md';
import { RiSettings5Fill } from 'react-icons/ri';
const menus = [
    {
        title: "Dashboard",
        icon: <AiFillHome />,
        path: "/dashboard",
    },
    {
        title: "People",
        icon: <BiFace />,
        path: "/person",
    },
    {
        title: "Devices",
        icon: <BsFillCameraVideoFill />,
        path: "/device",
    },
    {
        title: "Zones",
        icon: <BsFillSignIntersectionFill />,
        path: "/zone",
    },

    {
        title: "Actions",
        icon: <MdPendingActions />,
        path: "/action",
    },
    {
        title: "Settings",
        icon: <RiSettings5Fill />,
        path: "/setting",
    },

];

export default menus;