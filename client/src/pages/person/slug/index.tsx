import { Avatar, Table, TableContainer, Tbody, Td, Tr } from "@chakra-ui/react";
import PageTitle from "../../../components/headings/PageTitle";
import SectionTitle from "../../../components/headings/SectionTitle";
import ContentLayout from "../../../components/layouts/content_layout";
import { BiEdit } from 'react-icons/bi';
import AddButton from "../../../components/buttons/add_button";
import ActivityCard from "../../../components/cards/activity_card";
function PersonDetailPage() {
    return (
        <ContentLayout>
            <PageTitle>Devices</PageTitle>
            <div className="flex flex-col space-y-6 w-full">

                {/* Information */}
                <div className="flex flex-col items-start bg-white p-4 rounded-lg w-full">
                    <div className="flex flex-row justify-start">
                        <SectionTitle fontSize={14}>Personal Information</SectionTitle>
                        <BiEdit color="#A1ACAB" size={16} />
                    </div>
                    <div className="flex flex-row mt-2 justify-start">
                        <Avatar className="m-6 w-[80px] h-[80px]" size={'2xl'} />
                        <TableContainer >
                            <Table className="space-y-4" variant={'unstyled'} size='sm'>

                                <Tbody>
                                    <Tr className="">
                                        <Td className="w-[150px] text-[14px] text-[#A1ACAB] font-medium">Email</Td>
                                        <Td className="text-[14px] font-light text-black">khoilcm@1cinnovation.com</Td>

                                    </Tr>
                                    <Tr className="">
                                        <Td className="w-[150px] text-[14px] text-[#A1ACAB] font-medium">Name</Td>
                                        <Td className="text-[14px] font-light text-black">Le Cong Minh Khoi</Td>

                                    </Tr>
                                    <Tr className="">
                                        <Td className="w-[150px] text-[14px] text-[#A1ACAB] font-medium">Gender</Td>
                                        <Td className="text-[14px] font-light text-black">Male</Td>

                                    </Tr>
                                    <Tr className="">
                                        <Td className="w-[150px] text-[14px] text-[#A1ACAB] font-medium">Date of birth</Td>
                                        <Td className="text-[14px] font-light text-black">01/01/2001</Td>

                                    </Tr>
                                    <Tr className="">
                                        <Td className="w-[150px] text-[14px] text-[#A1ACAB] font-medium">Phone</Td>
                                        <Td className="text-[14px] font-light text-black">(+84) 9xx xxx xxx</Td>

                                    </Tr>
                                </Tbody>

                            </Table>
                        </TableContainer>
                    </div>
                </div>
                {/*  Register face */}
                <div className="flex flex-col items-start bg-white p-4 rounded-lg w-full ">
                    <div className="flex flex-row justify-between items-center w-full">
                        <SectionTitle>Registered Faces (2)</SectionTitle>
                        <AddButton title={'Add face'} />
                    </div>
                    <div className="flex flex-row flex-wrap mt-2 space-x-2  ">
                        <Avatar size={'xl'} />
                        <Avatar size={'xl'} />

                    </div>
                </div>
                {/*  Recent Activity */}
                <div className="flex flex-col items-start bg-white p-4 rounded-lg w-full ">
                    <SectionTitle>Recently Activity</SectionTitle>
                    <div className="flex flex-row justify-start items-center overflow-clip space-x-3 p-2">
                        <ActivityCard />
                        <ActivityCard />
                        <ActivityCard />

                    </div>
                </div>
            </div>


        </ContentLayout>
    )
}

export default PersonDetailPage;