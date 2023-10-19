import { InputGroup, Input, InputRightElement, Button, Select } from "@chakra-ui/react";
import { LiaSearchSolid } from "react-icons/lia";
import { BiPlus, BiSolidGridAlt } from 'react-icons/bi';
import { VscListSelection } from 'react-icons/vsc'
import PageTitle from "../../components/headings/PageTitle";
import ContentLayout from "../../components/layouts/content_layout";
import DeviceCard from "../../components/cards/device_card";
import { useState } from "react";
import { StreamType, ViewType } from "../../models/constants";

import { MultiSelect } from "react-multi-select-component";
import zones from "../../models/mocks/zones";
import cameras from "../../models/mocks/cameras";

type ZoneOption = {
    label: string,
    value: string,
}
const zoneOptions: ZoneOption[] = [...zones.map(zone => {
    return {
        label: zone.name ?? '',
        value: zone.id ?? '',
    };
})]

function DevicePage() {
    const [viewType, setViewType] = useState<ViewType>('item');
    const changeViewType = (value: ViewType) => setViewType(value);
    const [selectedZones, setSelectedZones] = useState<ZoneOption[]>([]);

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
                <MultiSelect className="w-[200px]"

                    options={[...zones.map(zone => {
                        return {
                            label: zone.name ?? '',
                            value: zone.id ?? '',
                        };
                    })]} value={selectedZones}
                    labelledBy={"Zone"}
                    onChange={setSelectedZones} />

                {/* <Select width={150} bgColor={'white'} placeholder="Camera">
                    <option value="camera-1">Camera 1</option>
                    <option value="camera-2">Camera 2</option>
                    <option value="camera-3">Camera 3</option>
                </Select> */}
            </div>
            <div className="flex flex-col p-4 bg-white w-full flex-grow items-start space-y-2">
                <div className="flex justify-between items-end w-full">
                    <Button textAlign={'center'} colorScheme="purple" borderRadius={20}> <BiPlus color="white" /> Add Device</Button>
                    <div className="flex justify-end items-end space-x-2">
                        <span className="text-base font-bold text-black">View: </span>
                        <BiSolidGridAlt size={28} color={viewType === 'item' ? '#217EAA' : 'black'} onClick={() => changeViewType('item')} />
                        <VscListSelection size={28} color={viewType === 'list' ? '#217EAA' : 'black'} onClick={() => changeViewType('list')} />
                    </div>
                </div>
                <div className="flex flex-col w-full">
                    {
                        ((selectedZones.length == 0 || selectedZones.length == zoneOptions.length) ? zoneOptions : selectedZones)
                            .map((zone) => (<div className=" flex flex-col w-full justify-start" key={zone.value}>
                                <h2 className="w-fit mb-1">{zone.label}</h2>
                                <div className="flex flex-row flex-wrap">
                                    {cameras
                                        .filter(camera => camera.zoneId === zone.value)
                                        .map((camera, index) =>
                                            <DeviceCard
                                                key={camera.id}
                                                streamType={camera.type}
                                                displayName={camera.name}
                                                zone={camera.zoneName}
                                                uri={camera.uri}
                                            />)}
                                </div>
                            </div>))
                    }
                    {/* <DeviceCard streamType={StreamType.DEFAULT} />
                    <DeviceCard streamType={StreamType.EZVIZ} />
                    <DeviceCard streamType={StreamType.SOCKET} /> */}
                    {/* <DeviceCard />
                    <DeviceCard />
                    <DeviceCard />
                    <DeviceCard />
                    <DeviceCard />
                    <DeviceCard />
                    <DeviceCard /> */}

                </div>

            </div>
        </ContentLayout>
    )
}

export default DevicePage;