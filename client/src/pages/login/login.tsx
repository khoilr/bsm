import { Button, Input } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";

function LoginPage() {
    const navigate = useNavigate();
    const onLoginClick = () => {
        navigate('/dashboard')
    }
    return (
        <div className="app">
            <div className="flex items-center justify-center h-[100vh]">
                <div className="flex flex-col items-center bg-white p-8 min-w-[500px] space-y-2">
                    {/* <h1 className="font-extrabold text-4xl">BMS</h1> */}
                    <img className="w-[300px] h-[300px]" src="./images/bms-logo.png" />
                    <h5 className="text-xl">Welcome</h5>
                    <p className="text-sm font-light text-gray-400">Login to continue to BMS</p>

                    <Input borderRadius={0} title="Email" placeholder="Email" id="email" />

                    <Input borderRadius={0} placeholder="Password" type="password" id="password" />
                    <Button marginTop={16} borderRadius={0} onClick={onLoginClick} colorScheme="blue" width={'full'}>Login</Button>
                </div>
            </div>
        </div>
    );
}

export default LoginPage;