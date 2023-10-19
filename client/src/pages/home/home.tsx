import { useEffect } from "react";
import { redirect, useNavigate } from "react-router-dom"

function HomePage() {
    const navigate = useNavigate();
    useEffect(() => {
        navigate('/login')
    }, [])


    return (
        <div>
            Home Page
        </div>
    )
}

export default HomePage