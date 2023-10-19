import { useEffect, useState } from "react";

const SMALL_DEVICE_WIDTH = 800;

const useDevice = () => {
    const [isSmallDevice, setSmallDevice] = useState(false);
    useEffect(() => {
        const onWidthChange = () => {
            if (window.innerWidth > SMALL_DEVICE_WIDTH) {
                setSmallDevice(false);
            } else {
                setSmallDevice(true);
            }
        }
        window.addEventListener('resize', onWidthChange);

        return () => window.removeEventListener('resize', onWidthChange);
    }, []);

    return [isSmallDevice, setSmallDevice];
}

export default useDevice;