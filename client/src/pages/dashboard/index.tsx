import { Input, InputGroup, InputRightElement, Select, } from "@chakra-ui/react";
import { LiaSearchSolid } from 'react-icons/lia'
import DetectedFaceCard from "../../components/cards/detected_face_card";
import BarChart from "../../components/charts/bar_chart";
import PageTitle from "../../components/headings/PageTitle";
import SectionTitle from "../../components/headings/SectionTitle";
import ContentLayout from "../../components/layouts/content_layout";

function DashboardPage() {
    return (
        <ContentLayout>
            <PageTitle>Dashboard</PageTitle>
            <div className="flex flex-row w-full space-x-2">
                <InputGroup bgColor={'white'} className="flex-grow">
                    <Input placeholder="Search" />
                    <InputRightElement pointerEvents={'none'}>
                        <LiaSearchSolid size={20} />
                    </InputRightElement>
                </InputGroup>
                {/* <Select className="w-[150px]" placeholder="Zone">
                    <option value="zone-a">Zone A</option>
                    <option value="zone-b">Zone B</option>
                    <option value="zone-c">Zone C</option>
                </Select> */}
                <Select width={150} bgColor={'white'} placeholder="Camera">
                    <option value="camera-1">Camera 1</option>
                    <option value="camera-2">Camera 2</option>
                    <option value="camera-3">Camera 3</option>
                </Select>
            </div>
            <div className="flex flex-col p-4 bg-white w-full flex-grow items-start">
                <div className="flex flex-row justify-between w-full">
                    <SectionTitle>Recently detected faces</SectionTitle>
                    <span>More</span>
                </div>
                <div className="flex flex-row overflow-x-auto auto space-x-6 pl-2 py-2 max-w-full">
                    <DetectedFaceCard />
                    <DetectedFaceCard />
                    <DetectedFaceCard />
                    <DetectedFaceCard />

                </div>
                <SectionTitle>Activity log</SectionTitle>
                <BarChart />
            </div>
        </ContentLayout>

    )
}

export default DashboardPage;