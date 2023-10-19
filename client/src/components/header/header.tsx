import { Button, Avatar, useDisclosure, Drawer, DrawerBody, DrawerContent, DrawerHeader, DrawerOverlay } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { GiHamburgerMenu } from "react-icons/gi";
import menus from "../../models/constants/nav-menus";
import NavItem from "../nav-item/nav-item";
import useDevice from "../../controllers/hooks/useDevice";



function Header() {
    const { isOpen, onOpen, onClose } = useDisclosure();
    const [drawerVisible, setDrawerVisible] = useDevice();
    return (
        <div className='flex flex-row justify-between items-center  bg-[#217EAA] px-4 py-3'>
            <div className="flex justify-start items-center space-x-2">
                {drawerVisible ?
                    <Button padding={0} onClick={onOpen}>
                        <GiHamburgerMenu />
                    </Button>
                    : <h2 className='text-white m-0'>BUILDING MANAGEMENT</h2>
                }

            </div>

            <div className='flex flex-row items-center'>
                <Avatar size={'md'} />
                <span className="ml-2 text-white font-semibold">
                    Hi, User
                </span>
            </div>
            {drawerVisible &&
                <Drawer size={'xs'} placement={'left'} onClose={onClose} isOpen={isOpen}>
                    <DrawerOverlay />
                    <DrawerContent>
                        <DrawerHeader borderBottomWidth='1px'>BUILDING MANAGEMENT</DrawerHeader>
                        <DrawerBody>
                            {menus.map((item) => <NavItem key={item.path} {...item} />)}
                        </DrawerBody>
                    </DrawerContent>
                </Drawer>}
        </div>
    )
}
export default Header;