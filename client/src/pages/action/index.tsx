import { InputGroup, Input, InputRightElement, Select } from "@chakra-ui/react";
import PageTitle from "../../components/headings/PageTitle";
import ContentLayout from "../../components/layouts/content_layout";
import { LiaSearchSolid } from 'react-icons/lia'
import { FaCalendarAlt } from 'react-icons/fa';
import SectionTitle from "../../components/headings/SectionTitle";
import ActivityCard from "../../components/cards/activity_card";
import { Link } from 'react-router-dom';

function ActionPage() {
    return (
        <ContentLayout>
            <PageTitle>Actions</PageTitle>
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
                <div className="w-[200px]">
                    <InputGroup>
                        <Input placeholder="dd-MM-yyyy" />
                        <InputRightElement>
                            <FaCalendarAlt />
                        </InputRightElement>
                    </InputGroup>
                </div>
                <SectionTitle>Zone 1</SectionTitle>
                <div className="flex flex-row justify-start flex-wrap">
                    {

                        Array.from({ length: 6 }, (_, index) =>
                            <Link key={index} className="mr-4 my-1  no-underline" to="/action/detail">
                                <ActivityCard />
                            </Link>
                        )
                    }
                </div>
                <SectionTitle>Zone 2</SectionTitle>
                <div className="flex flex-row justify-start flex-wrap">
                    {

                        Array.from({ length: 8 }, (_, index) =>
                            <Link key={index} className="mr-4  my-1 no-underline" to="/action/detail">
                                <ActivityCard />
                            </Link>
                        )
                    }
                </div>

            </div>
        </ContentLayout>
    )
}

export default ActionPage;