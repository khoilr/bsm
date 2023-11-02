// AuthContext.tsx
import React, { createContext, useContext, ReactNode, useEffect, useState } from 'react';

interface AuthContextProps {
    isAuthenticated: boolean;
    login: () => void;
    logout: () => void;
}

const AuthContext = createContext<Partial<AuthContextProps>>({});

export const useAuth = () => {
    return useContext(AuthContext);
}

interface AuthProviderProps {
    children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
    const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);

    useEffect(() => {
        // Check if the user is authenticated when the component mounts
        // This can be an API call, or checking local storage, etc.
        const token = localStorage.getItem('user');
        if (token) {
            setIsAuthenticated(true);
        }
    }, []);

    const login = () => {
        // Do login logic
        setIsAuthenticated(true);
    }

    const logout = () => {
        // Do logout logic
        setIsAuthenticated(false);
    }

    return (
        <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}
