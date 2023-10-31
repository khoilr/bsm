import { Button, Input } from "@chakra-ui/react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import { useState } from 'react';

function LoginPage() {
    const navigate = useNavigate();
    const [username, setUsername] = useState(''); // Controlled input state for username
    const [password, setPassword] = useState(''); // Controlled input state for password

    const goToDashboard = () => {
        navigate('/dashboard');
    }

    const onFinish = async () => {
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        const reqOptions = {
            url: 'http://localhost:30000/api/auth/sign-in',
            method: 'POST',
            data: formData
        };

        try {
            await axios.request(reqOptions).then(res => {
                if (res.status === 201) {
                    localStorage.setItem('bearer', res.data['access_token'])
                    goToDashboard();
                }
            });
        } catch (error) {
        }
    }

    return (
        <div className="app">
            <div className="flex items-center justify-center h-[100vh]">
                <div className="flex flex-col items-center bg-white p-8 min-w-[500px] space-y-2">
                    <img className="w-[300px] h-[300px]" src="./images/bms-logo.png" alt="BMS Logo" />
                    <h5 className="text-xl">Welcome</h5>
                    <p className="text-sm font-light text-gray-400">Login to continue to BMS</p>

                    <Input 
                        borderRadius={0} 
                        title="Email" 
                        placeholder="Email" 
                        value={username} 
                        onChange={(e) => setUsername(e.target.value)} 
                    />

                    <Input 
                        borderRadius={0} 
                        placeholder="Password" 
                        type="password" 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)}
                    />

                    <Button 
                        marginTop={16} 
                        borderRadius={0} 
                        onClick={onFinish} 
                        colorScheme="blue" 
                        width={'full'}>
                        Login
                    </Button>
                </div>
            </div>
        </div>
    );
}

export default LoginPage;
