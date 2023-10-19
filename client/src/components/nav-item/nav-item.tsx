
import React from "react";
import { IconBaseProps, } from "react-icons";
import { Link } from "react-router-dom";



type NavItemProps = {
    title: string,
    icon: JSX.Element,
    selected?: boolean,
    path: string,
}

function NavItem(props: NavItemProps) {

    const { title, icon, selected, path } = props;

    return (
        <Link className="text-links no-underline" to={path}>
            <div className={`py-4 px-2 flex flex-col items-center justify-center ${selected ? "selected-btn" : "unselected-btn"}`} >
                {React.cloneElement<IconBaseProps>(icon, { size: 40 })}
                <h5>{title}</h5>
            </div>
        </Link>
    )
}

export default NavItem;