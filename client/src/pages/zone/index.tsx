import { InputGroup, Input, InputRightElement, Button, useDisclosure, Modal, ModalBody, ModalCloseButton, ModalContent, ModalFooter, ModalHeader, ModalOverlay, Heading, Switch, Select, NumberInput, Checkbox, NumberDecrementStepper, NumberIncrementStepper, NumberInputField, NumberInputStepper, Collapse } from "@chakra-ui/react"
import { LiaSearchSolid } from "react-icons/lia"
import { BsUpload } from 'react-icons/bs';
import PageTitle from "../../components/headings/PageTitle"
import ContentLayout from "../../components/layouts/content_layout"
import ZoneCard from "../../components/cards/zone_card"
import ConfigRow from "../../components/data/config_row"
import { useState } from "react";
import EventBadge from "../../components/badges/event-badge";
import zones from "../../models/mocks/zones";

function ZonePage() {
    const { isOpen, onToggle, onClose } = useDisclosure()
    const [settingVisible, setSettingVisible] = useState(false);
    const [selectedZone, setSelectedZone] = useState(zones.length > 0 ? 0 : -1);

    return (
        <ContentLayout>
            <PageTitle>Devices</PageTitle>
            <div className="flex flex-row w-full space-x-2">
                <InputGroup bgColor={'white'} className="flex-grow">
                    <Input placeholder="Search" />
                    <InputRightElement pointerEvents={'none'}>
                        <LiaSearchSolid size={20} />
                    </InputRightElement>
                </InputGroup>
            </div>
            <div className="flex flex-col items-start bg-white rounded-xl w-full flex-grow p-3 space-y-2">
                <div className="">
                    <Button colorScheme="purple">+ Add new zone</Button>
                </div>
                <div className="flex flex-wrap justify-start items-start gap-4">
                    {zones.map((zone, index) => <ZoneCard key={index} name={zone.name ?? ""} onTap={() => {
                        setSelectedZone(index);
                        onToggle();
                    }} />)}
                </div>
            </div>
            {/* Modal Data */}
            {selectedZone >= 0 && <Modal isOpen={isOpen} onClose={onClose}>
                <ModalOverlay />
                <ModalContent>
                    <ModalHeader >{zones[selectedZone].name}</ModalHeader>
                    <ModalCloseButton />
                    <ModalBody className="flex flex-col items-start space-y-2">
                        {/* Information section */}
                        <Heading size={'md'}>Information</Heading>
                        <ConfigRow title="ID:" component={<Input value={zones[selectedZone].id} readOnly disabled />} titleWidth={100} />
                        <ConfigRow title="Name:" component={<Input defaultValue={zones[selectedZone].name} />} titleWidth={100} />
                        <ConfigRow title="Description:" component={<Input defaultValue={zones[selectedZone].description} />} titleWidth={100} />
                        <span className={`text-[#A1ACAB] font-semibold text-[14px] flex justify-start`}>Display</span>
                        <img className="w-[60px] h-[60px] object-contain m-0 " src='/images/zone_placeholder.png' />
                        <Button gap={2} colorScheme="gray" size={'sm'}><BsUpload /> Change...</Button>
                        <input type='file' hidden />
                        <div className="w-full h-[1px] bg-slate-300 mt-3"></div>
                        {/* Setting */}
                        <div className="flex items-center justify-between space-x-2 w-full">
                            <Heading size={'md'}>Secutity settings</Heading>
                            <Switch size={'sm'} onChange={(e) => setSettingVisible(!settingVisible)} />
                        </div>
                        <Collapse className="space-y-2" in={settingVisible} animateOpacity>
                            <ConfigRow title="Event trigger: " component={
                                <Select size={'sm'} className="w-full">
                                    <option value={'check-in'}>
                                        <EventBadge colorScheme="green">check-in</EventBadge>
                                    </option>
                                </Select>
                            } titleWidth={200} />
                            <ConfigRow title="People limit:" component={
                                <NumberInput width={200} size={'sm'} defaultValue={zones[selectedZone].setting?.limitPeople} min={0}>
                                    <NumberInputField />
                                    <NumberInputStepper >
                                        <NumberIncrementStepper />
                                        <NumberDecrementStepper />
                                    </NumberInputStepper>
                                </NumberInput>
                            } titleWidth={200} />
                            <ConfigRow title="Notifiy when reach limit:" component={<Checkbox defaultValue={zones[selectedZone].setting?.notify ? 0 : 1} />} titleWidth={200} />

                        </Collapse>
                    </ModalBody>


                    <ModalFooter>
                        <Button colorScheme='blue' mr={3} onClick={onClose}>
                            Close
                        </Button>

                    </ModalFooter>
                </ModalContent>
            </Modal>}
        </ContentLayout>
    )
}

export default ZonePage