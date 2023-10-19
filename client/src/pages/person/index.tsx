import { InputGroup, Input, InputRightElement, Select, Button } from "@chakra-ui/react";
import { BiPlus, BiSolidGridAlt } from "react-icons/bi";
import { LiaSearchSolid } from "react-icons/lia";
import { VscListSelection } from "react-icons/vsc";
import PageTitle from "../../components/headings/PageTitle";
import ContentLayout from "../../components/layouts/content_layout";
import { ViewType } from "../../models/constants";
import { useState } from "react";
import PersonCard from "../../components/cards/person_card";
import { Link } from "react-router-dom";
import AddButton from "../../components/buttons/add_button";

function PersonPage() {
    const [viewType, setViewType] = useState<ViewType>('item');
    const changeViewType = (value: ViewType) => setViewType(value);
    const empLength = 3;
    const uknownEmpLength = 2;
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
                <Select width={150} bgColor={'white'} placeholder="Zone" alignContent={'center'}>
                    <option value="zone-a">Zone A</option>
                    <option value="zone-b">Zone B</option>
                    <option value="zone-c">Zone C</option>
                </Select>
                <Select width={150} bgColor={'white'} placeholder="Camera">
                    <option value="camera-1">Camera 1</option>
                    <option value="camera-2">Camera 2</option>
                    <option value="camera-3">Camera 3</option>
                </Select>
            </div>
            <div className="flex flex-col p-4 bg-white w-full flex-grow items-start space-y-2">
                <div className="flex justify-between items-end w-full">
                    <AddButton title={'Add person'} />
                    <div className="flex justify-end items-end space-x-2">
                        <span className="text-base font-bold text-black">View: </span>
                        <BiSolidGridAlt size={28} color={viewType === 'item' ? '#217EAA' : 'black'} onClick={() => changeViewType('item')} />
                        <VscListSelection size={28} color={viewType === 'list' ? '#217EAA' : 'black'} onClick={() => changeViewType('list')} />
                    </div>
                </div>

                <h3>Employee {empLength > 0 ? `(${empLength})` : ''}</h3>
                <div className="w-full flex flex-row flex-wrap">
                    {
                        Array.from({ length: empLength }, (_, i) =>
                            <Link className="no-underline mr-4" to={'/person/detail'}>
                                <PersonCard key={i} name={'KhoiLCM'} />
                            </Link>
                        )
                    }
                </div>

                <h3>Uknown people {uknownEmpLength > 0 ? `(${uknownEmpLength})` : ''}</h3>
                <div className="w-full flex flex-row flex-wrap">
                    {
                        Array.from({ length: uknownEmpLength },
                            (_, index) =>
                                <Link className="no-underline mr-4" to={'/person/detail'}>
                                    <PersonCard
                                        key={index}
                                        name={`ID-${Math.floor(Math.random() * 1000)}`}
                                        isUnknown
                                    />
                                </Link>)
                    }
                </div>
            </div>
        </ContentLayout>
    )
}

export default PersonPage;